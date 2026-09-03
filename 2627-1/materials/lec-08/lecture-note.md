# Bài 08 — Deep Q-Learning

**Giảng viên:** Tạ Việt Cường · **Học kỳ 1, 2026–2027** · **Thời lượng:** 120 phút chính + 30 phút bài tập.

Ghi chú này dùng tài liệu nguồn `lecture8-dqn.pdf`. Phần chính kéo dài 120 phút;
30 phút cuối dành cho ba bài tập tính tay và thảo luận. Nguồn không có chương
trình minh hoạ, nên bài chỉ dùng công thức và giả mã.

Sau bài này, người học có thể giải thích hai cơ chế ổn định của DQN; lập đúng
đích có mặt nạ kết thúc; kiểm tra kích thước tensor và đường gradient; viết vòng
huấn luyện với hai đồng hồ; và đánh giá đúng giới hạn hội tụ của thuật toán.

---

## Bản đồ chủ đề (bốn nhóm)

### Nhóm cầu nối

| Mã | Chủ đề | Nguồn trang | Vai trò | Vào → Ra |
|---|---|---|---|---|
| `lec-08-topic-13` | Cầu nối từ Q-learning dạng bảng (Bài 07) | tr. 3–7 | Nhắc quy tắc cập nhật, off-policy, điều kiện hội tụ | Vào: Bài 07 → Ra: đích bootstrap dạng bảng |

### Nhóm cốt lõi

| Mã | Chủ đề | Nguồn trang | Vai trò | Vào → Ra |
|---|---|---|---|---|
| `lec-08-topic-01` | Vì sao cần Deep Q-learning | tr. 8–15 | Đặt vấn đề quy mô và khái quát hóa | Vào: topic-13 → Ra: nhu cầu $Q_\theta$ |
| `lec-08-topic-02` | Giao diện DQN và hai mạng | tr. 14–17, 20, 31, 33 | Định nghĩa $Q_\theta$, $Q_{\theta^-}$ | Vào: topic-01 → Ra: hai bản sao mạng |
| `lec-08-topic-03` | Bootstrap thành bài toán hồi quy | tr. 16, 20–22, 34 | Đích $y_t$ và sai số TD | Vào: topic-02 → Ra: nhãn hồi quy |
| `lec-08-topic-04` | Kết thúc thật và mặt nạ $(1-Z)$ | tr. 21 | Phân biệt $Z$ và $U$ | Vào: topic-03 → Ra: đích đúng |
| `lec-08-topic-05` | Chuyển tiếp và hai cờ, autoreset | tr. 21 | Hợp đồng dữ liệu | Vào: topic-04 → Ra: bộ sáu thành phần |
| `lec-08-topic-06` | Bộ nhớ phát lại | tr. 19–21, 32 | Cơ chế lưu và lấy mẫu | Vào: topic-05 → Ra: mini-batch |
| `lec-08-topic-07` | Replay giảm tương quan, không tạo i.i.d. | tr. 19, 29–32 | Giới hạn của replay | Vào: topic-06 → Ra: phát biểu đúng phạm vi |
| `lec-08-topic-08` | Gather và dừng gradient | tr. 16, 22, 34 | Đồ thị tính toán | Vào: topic-03 → Ra: loss batch |
| `lec-08-topic-09` | Mất mát và gradient batch | tr. 21–22, 34 | MSE và $\nabla_\theta L$ | Vào: topic-08 → Ra: gradient cho optimizer |
| `lec-08-topic-10` | Vòng DQN: hai đồng hồ $t$ và $k_{\mathrm{opt}}$ | tr. 18–22 | Giả mã đầy đủ | Vào: topic-05–09 → Ra: thuật toán hoàn chỉnh |
| `lec-08-topic-11` | Hợp đồng tensor của batch | tr. 14–22, 35 | Kích thước và kiểu tensor | Vào: topic-09 → Ra: kiểm tra cài đặt |
| `lec-08-topic-12` | Mạng mục tiêu và các nguồn bất ổn | tr. 19, 21, 29–33 | Đồng bộ đích và giới hạn ổn định | Vào: topic-10 → Ra: phạm vi bảo đảm của DQN |

### Nhóm bổ sung

| Mã | Chủ đề | Nguồn trang | Vai trò | Vào → Ra |
|---|---|---|---|---|
| `lec-08-topic-14` | SGD, RMSprop, Adam theo từng tọa độ | tr. 22–28 | Ba quy tắc cập nhật và giới hạn | Vào: topic-09 → Ra: lựa chọn optimizer có căn cứ |

### Nhóm đọc thêm/thực hành

| Mã | Chủ đề | Nguồn trang | Vai trò | Vào → Ra |
|---|---|---|---|---|
| `lec-08-topic-15` | Atari, kiểm tra tổng hợp, ba bài thảo luận, đọc thêm | tr. 12–13, 29–36 | Ứng dụng và tổng kết | Vào: topic-12, 14 → Ra: kết luận cuối tệp |

### Bảy mạch và thời lượng (120 phút)

1. Mở và cầu nối Q-learning dạng bảng — 12 phút (topic-13, 01).
2. Giao diện DQN và hai mạng — 20 phút (topic-02, 03).
3. Mặt nạ kết thúc, chuyển tiếp, replay và làm nóng — 29 phút (topic-04, 05, 06).
4. Gather, dừng gradient, mất mát, vòng DQN và tensor — 24 phút (topic-08, 09, 10, 11).
5. Bộ tối ưu — 10 phút linh hoạt (topic-14).
6. Tương quan, mục tiêu di động, bộ ba bất ổn và giới hạn — 17 phút (topic-07, 12).
7. Atari, kiểm tra tổng hợp và kết luận — 8 phút (topic-15).

Ba bài tập ở cuối dùng 30 phút sau phần chính.

---

## Phần 1 — Cầu nối từ Q-learning dạng bảng

<!-- note-topic-id: lec-08-topic-13 -->
### Q-learning dạng bảng và những gì cần nhớ lại

**Vấn đề.** Trước khi thay bảng bằng mạng, cần chốt chính xác Q-learning học gì,
cập nhật thế nào và hội tụ dưới điều kiện nào, vì mọi thành phần này sẽ được
"tham số hóa" ở các chủ đề sau.

**Trực giác.** Q-learning học hàm giá trị hành động $Q(s,a)$: với mỗi cặp
trạng thái–hành động, ước lượng tổng phần thưởng chiết khấu dài hạn khi thực hiện
$a$ tại $s$ rồi hành xử tham lam về sau. Tác tử tương tác bằng hành động tham lam
hoặc $\epsilon$-tham lam theo ước lượng hiện tại.

**Ví dụ.** Với một mẫu $(s,a,r,s')$, đích là
$y = r + \gamma \max_{a'} Q_k(s',a')$ và cập nhật dạng bảng là

$$Q_{k+1}(s,a) = Q_k(s,a) + \alpha\bigl(y - Q_k(s,a)\bigr).$$

Ở đây $\alpha$ là tốc độ học, $\gamma$ là hệ số chiết khấu, và $\max_{a'}Q_k(s',a')$
là giá trị bootstrap: dùng ước lượng hiện tại cho trạng thái kế tiếp thay vì chờ
đợi return thật.

**Hình thức.** Với $t\in\mathbb N_0$, $\gamma\in[0,1]$, $\alpha_t>0$,
$S_t\in\mathcal S$, $A_t\in\mathcal A$, $R_{t+1}\in\mathbb R$ và
$Z_{t+1}\in\{0,1\}$:

$$y_t = R_{t+1} + \gamma(1-Z_{t+1})\max_{a'\in\mathcal A}Q_t(S_{t+1},a'),$$
$$Q_{t+1}(S_t,A_t) = Q_t(S_t,A_t) + \alpha_t\bigl(y_t - Q_t(S_t,A_t)\bigr).$$

Cờ $Z_{t+1}=1$ khi chuyển tiếp kết thúc quy trình quyết định Markov đang được mô
hình hóa; khi đó nhánh bootstrap bị triệt tiêu. Dùng $\gamma<1$ cho nhiệm vụ
tiếp diễn; $\gamma=1$ chỉ phù hợp khi episode kết thúc thích hợp và return hữu hạn.

**Hai chính sách cần phân biệt ngay từ đầu.**

- *Chính sách hành vi* tạo dữ liệu: quy tắc $\epsilon_{\mathrm{exp}}$-greedy với
  $\epsilon_{\mathrm{exp}}\in[0,1]$ — với xác suất $\epsilon_{\mathrm{exp}}$ chọn
  hành động ngẫu nhiên đều, ngược lại chọn
  $a=\arg\max_{a'}Q(s,a')$.
- *Phép sao lưu đích* là phép cực đại theo $a'$, thuộc toán tử tối ưu Bellman,
  không phải trung bình theo xác suất của một chính sách đích ngẫu nhiên.

Vì phép sao lưu lấy cực đại thay vì kỳ vọng dưới chính sách đích, Q-learning
không cần trọng số lấy mẫu quan trọng. Nhưng thuật toán vẫn là *học lệch chính
sách* (off-policy): dữ liệu lệch hành vi vì khám phá và — sau này — vì replay giữ
chuyển tiếp từ các chính sách cũ.

**Điều kiện hội tụ dạng bảng.** Q-learning hội tụ tới $Q^*$ khi: mọi cặp
$(s,a)$ được thăm vô hạn lần; dãy bước học thỏa điều kiện Robbins–Monro theo từng
cặp; môi trường có tính dừng; bảng được biểu diễn chính xác. Các điều kiện này
gắn với biểu diễn bảng và **không tự chuyển sang mạng sâu**.

**Ứng dụng và giới hạn.** Cập nhật từ điển (đổi một ô bảng) rẻ và có bảo đảm
trong thiết lập tiêu chuẩn, nhưng số ô tăng theo $|\mathcal S||\mathcal A|$ và
không xử lý trực tiếp không gian trạng thái liên tục.

**Kiểm tra nhanh.** Nếu $\epsilon_{\mathrm{exp}}=0$ mãi mãi, điều kiện hội tụ nào
bị vi phạm? — Điều kiện thăm đủ mọi cặp $(s,a)$; chính sách thuần tham lam có
thể không bao giờ thử hành động chưa biết.

**Về độ phức tạp mẫu.** Nguồn nêu cận cho một số thiết lập nhưng không xác định
đủ mô hình lấy mẫu, chuẩn sai số, xác suất thành công, điều kiện bao phủ và thuật
toán tương ứng. Vì vậy ghi chú không dùng các cận đó như kết quả áp dụng được.
Thông điệp giữ lại: chi phí phụ thuộc quy mô biểu diễn, khả năng bao phủ, chiến
lược khám phá và các giả thiết ổn định; không thể suy ra một cận mẫu chung chỉ
từ việc thay bảng bằng đặc trưng hoặc mạng sâu.

---

## Phần 2 — Giao diện DQN, dữ liệu, đích và vòng huấn luyện

<!-- note-topic-id: lec-08-topic-01 -->
### Vì sao cần Deep Q-learning

**Vấn đề.** Bảng Q cần một ô cho mỗi cặp $(s,a)$; khi không gian trạng thái lớn
hoặc liên tục, lưu tường minh là bất khả thi.

**Trực giác.** Thay vì lưu giá trị riêng cho từng cặp, xấp xỉ hàm giá trị bằng
mạng neural $Q_\theta(s,a)$. Các trạng thái tương tự chia sẻ biểu diễn, nên một
cập nhật có thể cải thiện nhiều dự đoán cùng lúc.

**Ví dụ.** Đầu vào có cấu trúc — vector đặc trưng, ảnh, bàn cờ — được mạng xử lý
thành vector giá trị hành động; bảng không có cơ chế chia sẻ thông tin giữa các ô.

**Hình thức.** Tham số hóa $Q_\theta(s,a)$ (tuyến tính hoặc MLP) đem lại: hiệu
quả bộ nhớ (không lưu mọi cặp), khái quát hóa, trích xuất đặc trưng, và tính khả
vi của hàm mục tiêu — có thể tối ưu bằng gradient.

**Ứng dụng và giới hạn.** Mạng đổi chi phí lưu trữ lấy sai số xấp xỉ và *sự giao
thoa*: một cập nhật đổi nhiều giá trị Q cùng lúc, có thể phá các giá trị đang đúng.
Với xấp xỉ hàm, bảo đảm mẫu cần giả thiết cấu trúc; với MLP, tối ưu không lồi và
không có bảo đảm hội tụ toàn cục.

**Kiểm tra nhanh.** Đổi chi phí gì khi chuyển bảng → mạng? — Đổi bộ nhớ tường minh
lấy sai số xấp xỉ, giao thoa giữa dự đoán và mất bảo đảm hội tụ dạng bảng.

<!-- note-topic-id: lec-08-topic-02 -->
### Giao diện DQN và hai mạng

**Vấn đề.** Nếu cùng một bộ tham số $\theta$ vừa tạo dự đoán vừa tạo đích
bootstrap, một bước cập nhật có thể đổi cả dự đoán lẫn nhãn — vòng phản hồi di động.

**Trực giác.** Tách hai bản sao của cùng kiến trúc: mạng trực tuyến nhận gradient,
mạng mục tiêu tạo đích và được giữ cố định giữa các lần đồng bộ.

**Ví dụ.** Khởi tạo $\theta$, rồi đặt $\theta^-\leftarrow\theta$. Mạng mục tiêu
không được cập nhật bởi loss; nó chỉ đổi khi được sao chép từ mạng online.

**Hình thức.** Giao diện DQN cho hành động rời rạc:

$$\mathbf q_\theta(o)\in\mathbb R^{|\mathcal A|},\qquad Q_\theta(o,a)=[\mathbf q_\theta(o)]_a.$$

- $Q_\theta$: mạng trực tuyến (online), tham số $\theta$, nhận gradient.
- $Q_{\theta^-}$: mạng mục tiêu (target), tham số $\theta^-$, tạo phần bootstrap,
  cố định giữa hai lần đồng bộ.

Ký hiệu $o$ (quan sát) khi đầu vào chưa chắc đủ Markov; chỉ dùng $s$ khi biểu
diễn đủ Markov.

**Ứng dụng và giới hạn.** Mạng mục tiêu làm chậm vòng phản hồi nhưng không tạo
mục tiêu bất biến vĩnh viễn; nó vẫn đổi tại các mốc đồng bộ. Các lựa chọn kiến
trúc điển hình: MLP cho đặc trưng số chiều thấp, CNN cho đầu vào giống ảnh, hàm
kích hoạt ReLU/tanh/sigmoid; số tầng, độ rộng và cách biểu diễn đầu vào ảnh hưởng
trực tiếp đến năng lực xấp xỉ và độ ổn định.

**Kiểm tra nhanh.** Mạng mục tiêu có nhận gradient từ loss hiện tại không? — Không;
nó chỉ cung cấp phần bootstrap và nằm trong vùng dừng gradient.

<!-- note-topic-id: lec-08-topic-03 -->
### Bootstrap trở thành bài toán hồi quy

**Vấn đề.** Cập nhật từ điển của Q-learning không cho biết cách cập nhật một mạng;
cần chuyển bootstrap thành một bài toán hồi quy có nhãn.

**Trực giác.** Giữ $Q_{\theta^-}$ cố định, đích trở thành một "nhãn" tạm thời cố
định; mạng online học để dự đoán gần nhãn đó.

**Ví dụ.** Mạng online dự đoán $q_t = Q_\theta(O_t,A_t)$; nhãn hồi quy là

$$y_t = R_{t+1} + \gamma(1-Z_{t+1})\max_{a'}Q_{\theta^-}(O_{t+1},a').$$

Sai số sai phân thời gian: $\delta_t = y_t - q_t$.

**Hình thức.** Đích gồm phần thưởng quan sát được $R_{t+1}$ và một ước lượng
bootstrap từ mạng mục tiêu. Vì $\theta^-$ cố định giữa các lần đồng bộ, đích của
một chuyển tiếp không đổi trong khoảng đó; nó chỉ đổi tại mốc đồng bộ.

**Ứng dụng và giới hạn.** Cách viết này cho phép dùng toàn bộ công cụ hồi quy
(mini-batch, gradient, optimizer), nhưng nhãn vẫn phụ thuộc vào một bản sao gần
đây của chính mạng đang học — nguồn gốc của mục tiêu di động.

**Kiểm tra nhanh.** Đích đổi khi nào? — Chỉ khi $\theta^-$ được đồng bộ; giữa hai
lần đồng bộ, đích của một chuyển tiếp cố định.

<!-- note-topic-id: lec-08-topic-04 -->
### Kết thúc thật làm mất nhánh bootstrap

Quay lại đích hồi quy ở chủ đề trước, bước này xử lý riêng trường hợp chuyển tiếp
kết thúc.

**Vấn đề.** Nếu chỉ viết $y = r + \gamma\max_{a'}Q_{\theta^-}(s',a')$ mà không xử
lý kết thúc, đích tại chuyển tiếp kết thúc sẽ chứa một ước lượng vô nghĩa về
"trạng thái sau khi kết thúc".

**Trực giác.** Mặt nạ $(1-Z)$ triệt tiêu nhánh bootstrap đúng khi quy trình đang
mô hình hóa đã kết thúc.

**Ví dụ.** Cho $\gamma=0{,}9$, $R_{t+1}=-2$,
$\max_{a'}Q_{\theta^-}(O_{t+1},a')=100$:

- Chưa kết thúc ($Z_{t+1}=0$): $y_t = -2 + 0{,}9\cdot 100 = 88$.
- Đã kết thúc ($Z_{t+1}=1$): $y_t = -2$. Giá trị $100$ **không** ảnh hưởng đến đích.

**Hình thức.** $Z_{t+1}=1$ là kết thúc thật của MDP đang mô hình hóa. Mặt nạ nhân
nhánh bootstrap với không, không phải một hiệu chỉnh nhỏ.

**Ứng dụng và giới hạn.** Lỗi phổ biến: dùng một biến `done` đã gộp máy móc
(terminated OR truncated) làm mặt nạ. Cắt ngắn ngoài mô hình ($U=1$) **không** tự
động đặt bootstrap bằng 0 — xem topic-05.

**Kiểm tra nhanh.** Tại chuyển tiếp kết thúc, đích bằng gì? — Đúng bằng phần
thưởng $R_{t+1}$; nhánh bootstrap bị nhân với $0$.

<!-- note-topic-id: lec-08-topic-05 -->
### Một chuyển tiếp cần hai cờ: $Z$ và $U$

**Vấn đề.** Dữ liệu thu thập thực tế có hai sự kiện khác nhau bị gộp thành "done":
kết thúc của nhiệm vụ và việc dừng thu thập do giới hạn bên ngoài.

**Trực giác.** Chỉ kết thúc của MDP mới xóa tương lai; cắt ngắn chỉ dừng *việc thu
thập*, nhiệm vụ tiếp diễn vẫn còn tương lai nên vẫn bootstrap.

**Ví dụ.** Chuyển tiếp lưu trong replay:

$$(O_t, A_t, R_{t+1}, O_{t+1}, Z_{t+1}, U_{t+1}).$$

- $Z_{t+1}=1$: quy trình đang mô hình hóa kết thúc → không bootstrap.
- $U_{t+1}=1$: bộ thu thập dừng (hết thời lượng, hết ngân sách bước); nhiệm vụ
  tiếp diễn thường vẫn bootstrap.

**Hình thức — môi trường tự khởi động lại.** Khi API tự reset sau bước cuối,
quan sát trả về thuộc *lượt mới*, không thuộc chuyển tiếp vừa xảy ra. Replay phải
lưu *quan sát cuối của chuyển tiếp* (ví dụ trường `final_observation`), không thay
bằng quan sát đầu của lượt mới. Mặt nạ trong loss phải theo $Z$ (kết thúc MDP),
không theo một biến done đã gộp.

**Ứng dụng và giới hạn.** Phân biệt đúng hai cờ quyết định đích có đúng nghĩa
Bellman hay không; nhầm $U$ làm $Z$ làm mất giá trị tương lai một cách tùy tiện.

**Kiểm tra nhanh.** $U_i=1$ có nghĩa là không bootstrap không? — Không; $U_i$ là
cắt ngắn do cơ chế thu thập, nhiệm vụ tiếp diễn vẫn bootstrap; chỉ $Z_i=1$ mới
triệt tiêu nhánh bootstrap.

<!-- note-topic-id: lec-08-topic-06 -->
### Bộ nhớ phát lại (experience replay)

**Vấn đề.** Học từ các chuyển tiếp liền nhau theo thứ tự thời gian khiến mini-batch
chứa thông tin trùng lặp và lệch theo quỹ đạo gần nhất.

**Trực giác.** Thay vì học từ chuỗi liên tiếp, DQN lưu nhiều chuyển tiếp vào bộ
đệm $\mathcal D$ và huấn luyện trên các bộ sáu thành phần được lấy ngẫu nhiên.

**Ví dụ.** Bộ đệm vòng dung lượng $N\in\mathbb N_+$; mini-batch có $b\in\mathbb N_+$
mẫu với $b\le N$. Lấy đều các vị trí trong $\mathcal D$ và tái sử dụng chuyển tiếp.
Replay trộn cả hành vi khám phá hiện tại lẫn các phiên bản hành vi cũ — đây là
nguồn lệch chính sách thứ hai của DQN (nguồn thứ nhất là $\epsilon$-greedy so với
phép cực đại Bellman).

**Hình thức.** Lưu
$(O_t,A_t,R_{t+1},O_{t+1},Z_{t+1},U_{t+1})$ vào $\mathcal D$; lấy ngẫu nhiên
mini-batch từ $\mathcal D$ để tính mất mát. Q-learning dùng phép sao lưu tối ưu nên mất mát DQN cơ
bản không gắn tỷ trọng lấy mẫu quan trọng.

**Ứng dụng và giới hạn.** Lợi ích: phá vỡ tương quan theo thời gian, tái sử dụng
dữ liệu quá khứ, cải thiện hiệu quả mẫu. Giới hạn: xem topic-07.

**Kiểm tra nhanh.** Vì sao loss DQN cơ bản không cần importance sampling? — Vì đích
dùng phép cực đại Bellman, không phải kỳ vọng hành động dưới một chính sách đích
ngẫu nhiên.

<!-- note-topic-id: lec-08-topic-07 -->
### Replay giảm tương quan, không tạo i.i.d.

**Vấn đề.** Tối ưu mạng neural thường giả sử mini-batch gần i.i.d.; chuyển tiếp
liên tiếp thu thập trực tuyến tương quan mạnh. Replay có giải quyết triệt để không?

**Trực giác.** Các chuyển tiếp liền nhau đi qua quan sát gần nhau và dùng cùng
phiên bản chính sách; mini-batch liên tiếp có cỡ mẫu hiệu dụng nhỏ hơn số phần tử,
gradient dao động theo đoạn quỹ đạo gần nhất, mạng có thể quá khớp vùng trạng thái
mới và "quên" vùng cũ.

**Ví dụ.** Lấy mẫu từ replay trộn các thời điểm, nhưng các mẫu vẫn có thể chồng
lấn quan sát, đến từ các chính sách hành vi khác nhau, và bộ đệm hữu hạn loại dần
dữ liệu cũ.

**Hình thức — phát biểu đúng phạm vi.**

- Replay *làm được*: giảm tương quan ngắn hạn của mẫu liền nhau; tăng tái sử dụng
  dữ liệu; làm mini-batch đa dạng hơn quỹ đạo mới nhất.
- Replay *không bảo đảm*: độc lập cùng phân phối (i.i.d.); phân phối bộ đệm đứng
  yên; thuật toán hội tụ.

**Ứng dụng và giới hạn.** Dùng từ "giảm", không dùng "loại bỏ" tương quan. Không
nói tương quan luôn làm gradient bị chệch; hệ quả chắc chắn hơn là tự tương quan,
độ đa dạng thấp và phương sai cập nhật phụ thuộc quỹ đạo.

**Kiểm tra nhanh.** Replay có biến dữ liệu thành i.i.d. không? — Không; nó chỉ
giảm tương quan ngắn hạn và tăng tái sử dụng.

<!-- note-topic-id: lec-08-topic-08 -->
### Gather và dừng gradient ở đích

**Vấn đề.** Trong batch, mạng xuất giá trị cho *mọi* hành động, nhưng loss chỉ cần
giá trị của *hành động đã lưu*; đồng thời gradient không được chảy vào đường tạo đích.

**Trực giác.** Hai đường tính tách bạch:

- *Đường dự đoán*: $q_i = Q_\theta(O_i,A_i)$, phụ thuộc $\theta$, nhận gradient.
- *Đường tạo đích*: dùng $Q_{\theta^-}(O'_i,\cdot)$, $\theta^-$ cố định giữa hai
  lần đồng bộ, được đặt trong toán tử dừng gradient $\operatorname{sg}$.

**Ví dụ.** Gather là phép chọn theo chỉ số: từ tensor $[b,|\mathcal A|]$, lấy một
phần tử mỗi hàng theo hành động đã lưu $A_i$, tạo vector $q\in\mathbb R^b$.
Ký hiệu $\operatorname{sg}$ tương ứng detach/no-grad trong mã thực tế.

**Hình thức.** Với batch
$\{(O_i,A_i,R_i,O'_i,Z_i,U_i)\}_{i=1}^b$:

$$L_B(\theta)=\frac1b\sum_{i=1}^b\bigl(\operatorname{sg}(y_i)-q_i\bigr)^2.$$

Gradient chỉ truyền qua mạng online $Q_\theta$, không qua mạng mục tiêu.

**Ứng dụng và giới hạn.** Bài dùng sai số bình phương trung bình (MSE) để giữ phép
tính minh bạch; Huber là biến thể thực hành có thể thay MSE trong một cài đặt
thực tế. Lỗi phổ biến: quên dừng gradient khiến gradient chảy vào mạng mục tiêu
(nếu nó chia sẻ tham số) hoặc tính gradient trên cả đích.

**Kiểm tra nhanh.** Nếu bỏ $\operatorname{sg}$ quanh $y_i$ và hai mạng chia sẻ
$\theta$, điều gì xảy ra? — Gradient đổi cả dự đoán lẫn nhãn trong cùng một bước;
vòng phản hồi di động trở lại.

<!-- note-topic-id: lec-08-topic-09 -->
### Mất mát và gradient của batch

**Vấn đề.** Cần viết loss và gradient với hệ số đúng để kiểm tra dấu cập nhật.

**Trực giác.** MSE trung bình trên batch; gradient theo từng $q_i$ tỉ lệ với sai
số $q_i - y_i$.

**Ví dụ.** Với batch $B$:

$$L_B(\theta)=\frac{1}{b}\sum_{i=1}^{b}\bigl(y_i-Q_\theta(O_i,A_i)\bigr)^2,
\qquad \theta\leftarrow\theta - \eta\nabla_\theta L_B(\theta).$$

**Hình thức.** Với $q_i = Q_\theta(O_i,A_i)$ và $y_i$ như chủ đề 03, có mặt nạ
theo chủ đề 04:

$$\nabla_\theta L_B=\frac{2}{b}\sum_{i=1}^b(q_i-y_i)\,\nabla_\theta q_i.$$

Tương đương, $\partial L_B/\partial q_i=(2/b)(q_i-y_i)$; quy tắc dây chuyền
nhân đại lượng này với $\nabla_\theta q_i$ rồi cộng theo lô.

Hệ số $\tfrac{2}{b}$ đến từ đạo hàm bình phương và phép lấy trung bình. Dấu của
$(q_i - y_i)$ quyết định $q_i$ tăng hay giảm dưới một bước gradient descent nhỏ:
sai số dương ($q_i > y_i$) làm $q_i$ giảm; sai số âm làm $q_i$ tăng.

**Ứng dụng và giới hạn.** Loss giảm trên batch không đồng nghĩa return đánh giá
tăng. MSE nhạy với sai số lớn; Huber là lựa chọn thực hành khác.

**Kiểm tra nhanh.** Với một mẫu, $\partial L/\partial q_i$ bằng gì? —
$\tfrac{2}{b}(q_i - y_i)$; với $b=2$, hệ số hiệu dụng là $(q_i-y_i)$.

<!-- note-topic-id: lec-08-topic-10 -->
### Vòng DQN: hai đồng hồ $t$ và $k_{\mathrm{opt}}$

**Vấn đề.** Tương tác và tối ưu xen kẽ nhau với các nhịp khác nhau; cần tách rõ
bước môi trường $t$ khỏi bước tối ưu $k_{\mathrm{opt}}$ để giả mã không mơ hồ.

**Trực giác.** Tương tác tạo chuyển tiếp; tối ưu lấy chuyển tiếp đã lưu. Ba siêu
tham số nhịp: $N_{\mathrm{start}}$ (số mẫu làm nóng replay trước khi tối ưu),
$F$ (số bước môi trường giữa hai lần tối ưu), $C$ (chu kỳ đồng bộ mạng mục tiêu,
đếm theo bước tối ưu).

**Hình thức — giả mã.**

*Đầu vào:* $\gamma,\epsilon_{\mathrm{exp}}\in[0,1]$;
$b,N_{\mathrm{start}},N,F,C\in\mathbb N_+$ với $b\le N_{\mathrm{start}}\le N$;
optimizer với tốc độ học $\eta>0$. *Đầu ra:* $\theta$ và chính sách tham lam theo
$Q_\theta$.

1. Khởi tạo $\mathcal D$, $\theta$; đặt $\theta^-\leftarrow\theta$; $O_0$ từ
   reset; $t\leftarrow 0$; $k_{\mathrm{opt}}\leftarrow 0$.
2. Chọn $A_t$ theo $\epsilon_{\mathrm{exp}}$-greedy từ $Q_\theta(O_t,\cdot)$.
3. Bước môi trường; nhận $R_{t+1}$, hai cờ $Z,U$, quan sát trả về và thông tin API.
4. Xác định quan sát của chuyển tiếp: nếu giao diện tự đặt lại môi trường và cung
   cấp `final_observation` trong thông tin trả về, dùng quan sát cuối đó; nếu
   không, dùng quan sát do bước môi trường trả về; lưu vào $\mathcal D$.
5. Nếu cần reset mà API chưa tự reset, gọi reset; gán quan sát bắt đầu vòng kế;
   tăng $t\leftarrow t+1$.
6. Nếu $|\mathcal D|\ge N_{\mathrm{start}}$ và $t\bmod F=0$ (kiểm sau khi tăng $t$):
   lấy đều mini-batch từ $\mathcal D$; gather $q_i=Q_\theta(O_i,A_i)$; trong
   no-grad tính $y_i$; tính MSE; cập nhật $\theta$;
   $k_{\mathrm{opt}}\leftarrow k_{\mathrm{opt}}+1$.
7. Sau cập nhật, nếu $k_{\mathrm{opt}}\bmod C=0$ thì $\theta^-\leftarrow\theta$.
8. Ngoài điều kiện tối ưu: dừng theo ngân sách hoặc tiêu chuẩn đánh giá định trước.

**Ứng dụng và giới hạn.** Bản đơn giản có thể chọn $F=1$, nhưng vẫn phải chờ đủ
$N_{\mathrm{start}}$. Đánh giá dùng chính sách tham lam riêng, không trộn return
khám phá với return đánh giá. Dùng $\gamma<1$ cho nhiệm vụ tiếp diễn.

**Kiểm tra nhanh.** $t\bmod F=0$ và $k_{\mathrm{opt}}\bmod C=0$ đếm trên cùng một
đồng hồ không? — Không; $t$ đếm bước môi trường, $k_{\mathrm{opt}}$ đếm bước tối
ưu; $F$ và $C$ thuộc hai đồng hồ khác nhau.

<!-- note-topic-id: lec-08-topic-11 -->
### Hợp đồng tensor của batch

**Vấn đề.** Lỗi cài đặt DQN thường là lỗi kích thước và kiểu tensor, không phải lỗi
toán.

**Trực giác.** Mọi tensor trong loss phải khớp hợp đồng: batch quan sát đi qua hai
mạng, gather và max tạo hai vector cùng kích thước $[b]$.

**Ví dụ — hợp đồng cho batch Atari:**

- $O, O'$: `float32`, dạng $[b,4,h,w]$.
- $A$: `int64`, dạng $[b]$.
- $R$: `float32`, dạng $[b]$.
- $Z, U$: `bool`, dạng $[b]$.
- Hai mạng tạo $[b,|\mathcal A|]$; gather chọn một hành động mỗi hàng; max tạo một
  giá trị mỗi hàng; $q, y\in\mathbb R^b$; loss là vô hướng.

**Hình thức.** Nếu $A$ có dạng cột $[b,1]$, gather rồi squeeze về $[b]$; tránh
broadcasting thành ma trận $[b,b]$. Chuyển $Z$ sang kiểu số khi tính $1-Z$. Replay
có thể lưu quan sát `uint8` rồi chuyển `float32` khi tạo batch. Mọi tensor dùng
trong loss phải ở cùng thiết bị.

**Ứng dụng và giới hạn.** Hợp đồng này là giao diện tối thiểu để đọc và kiểm tra
tensor, không phải đặc tả tái lập kết quả.

**Kiểm tra nhanh.** Nếu $A$ có dạng $[b,1]$ mà quên squeeze, gather có thể tạo gì?
— Tensor $[b,b]$ do broadcasting; phải squeeze về $[b]$ trước khi tính sai số.

<!-- note-topic-id: lec-08-topic-12 -->
### Mạng mục tiêu và các nguồn bất ổn

**Vấn đề.** Nếu $\theta^-$ đổi mỗi bước, đích di động như khi chỉ có một mạng; nếu
không bao giờ đổi, đích lỗi thời. Cần một nhịp đồng bộ rõ ràng.

**Trực giác.** Giữ $\theta^-$ cố định trong $C$ bước tối ưu, rồi sao chép mạng
online sau bước tối ưu:

$$k_{\mathrm{opt}}\leftarrow k_{\mathrm{opt}}+1,\qquad
k_{\mathrm{opt}}\bmod C=0:\ \theta^-\leftarrow\theta.$$

Thứ tự đúng: cập nhật $\theta$, tăng bộ đếm tối ưu, rồi mới kiểm tra đồng bộ.

**Ví dụ — đích nhảy bao nhiêu khi đồng bộ?** Xét ngay sau $\theta^-\leftarrow\theta$:

$$y_i^{\mathrm{new}}-y_i^{\mathrm{old}}
=\gamma(1-Z_i)\Bigl[\max_{a'}Q_{\theta}(O'_i,a')-\max_{a'}Q_{\theta^-}(O'_i,a')\Bigr].$$

Mẫu cũ trong replay có thể nhận đích mới dù bộ sáu thành phần
$(O_i,A_i,R_i,O'_i,Z_i,U_i)$ không đổi.

**Hình thức.** Với một chuyển tiếp cố định và $\theta^-$ chưa đổi, $y_i$ cố định.
Mạng mục tiêu làm chậm đích di động; $C$ là một đánh đổi thực nghiệm.

**Ứng dụng và giới hạn.** Mạng mục tiêu không tạo mục tiêu bất biến vĩnh viễn,
không bảo đảm hội tụ, và không phải "mạng đánh giá chính sách" — nó chỉ cung cấp
phần bootstrap. $C$ lớn làm đích ổn định hơn nhưng lỗi thời hơn.

**Kiểm tra nhanh.** Sau đồng bộ, đích của một chuyển tiếp cũ có đổi không? — Có;
nó được tính lại bằng $\theta^-$ mới tại lần lấy mẫu kế tiếp, dù dữ liệu không đổi.

**Ba nguồn bất ổn cần theo dõi.** Chuyển tiếp liên tiếp có tương quan mạnh; đích
bootstrap thay đổi theo mạng; và DQN đồng thời dùng xấp xỉ hàm, bootstrap cùng
dữ liệu lệch chính sách. Sự kết hợp sau thường được gọi là *bộ ba nguy hiểm*.
Nó có thể gây dao động hoặc phân kỳ trong một số thiết lập, không có nghĩa DQN
luôn phân kỳ. Bộ nhớ phát lại giảm tương quan ngắn hạn, còn mạng mục tiêu làm
chậm sự thay đổi của đích. Hai cơ chế này không tạo dữ liệu độc lập, phân phối
đồng nhất và không cho bảo đảm hội tụ tổng quát.

---

## Phần 3 — Bộ tối ưu

<!-- note-topic-id: lec-08-topic-14 -->
### SGD, RMSprop và Adam theo từng tọa độ

**Vấn đề.** Optimizer nhận gradient của loss và đổi nó thành bước tham số; nó
không sửa đích hay dữ liệu sai. Ba quy tắc cập nhật phổ biến chuẩn hóa gradient
theo những cách khác nhau.

**Hình thức chung.** Với chỉ số cập nhật $j\in\mathbb N_+$ (trùng $k_{\mathrm{opt}}$)
và tốc độ học $\eta>0$:

$$g_j=\nabla_\theta L_{B_j}(\theta_{j-1}),\qquad \theta_j=\operatorname{Update}(\theta_{j-1},g_j).$$

Các hệ số $\rho,\beta_1,\beta_2\in[0,1)$; $\epsilon_{\mathrm{opt}}>0$ ổn định phép
chia. **Lưu ý:** $\epsilon_{\mathrm{opt}}$ (số học của optimizer) khác hoàn toàn
$\epsilon_{\mathrm{exp}}$ (xác suất khám phá của chính sách hành vi).

**SGD.**

$$\theta_j=\theta_{j-1}-\eta g_j.$$

Không cần trạng thái phụ theo từng tham số; mọi tọa độ dùng cùng hệ số bước $\eta$.
Đơn giản, tiết kiệm bộ nhớ, dễ phân tích; nhưng nhạy với tốc độ học và có thể dao
động trong bài toán điều kiện kém.

**RMSprop** (theo từng tọa độ, $v_0=0$, $\rho\in[0,1)$; biến thể epsilon ngoài căn):

$$v_j=\rho v_{j-1}+(1-\rho)\,g_j\odot g_j,\qquad
\theta_j=\theta_{j-1}-\eta\, g_j\oslash\bigl(\sqrt{v_j}+\epsilon_{\mathrm{opt}}\bigr).$$

Gradient lớn kéo dài ở một tọa độ làm giảm bước hiệu dụng tại tọa độ đó; gradient
nhỏ nhận bước tương đối lớn hơn. Hữu ích trong DQN vì mục tiêu TD nhiễu và không
dừng; RMSprop xuất hiện trong các cài đặt DQN ban đầu.

**Adam** ($m_0=v_0=0$, $\beta_1,\beta_2\in[0,1)$):

$$m_j=\beta_1m_{j-1}+(1-\beta_1)g_j,\qquad v_j=\beta_2v_{j-1}+(1-\beta_2)g_j\odot g_j,$$
$$\hat m_j=\frac{m_j}{1-\beta_1^j},\qquad \hat v_j=\frac{v_j}{1-\beta_2^j},\qquad
\theta_j=\theta_{j-1}-\eta\,\hat m_j\oslash\bigl(\sqrt{\hat v_j}+\epsilon_{\mathrm{opt}}\bigr).$$

Hiệu chỉnh lệch quan trọng ở các bước đầu vì hai moment khởi tạo bằng không. Adam
kết hợp động lượng (làm trơn hướng tìm kiếm) với chuẩn hóa thích nghi kiểu RMS,
thường giúp tăng tốc huấn luyện trong deep RL.

**So sánh và lựa chọn.**

| Phương pháp | Trạng thái phụ | Điều cần tinh chỉnh |
|---|---|---|
| SGD | không | tốc độ học và lịch giảm |
| RMSprop | $v_j$ | $\eta,\rho,\epsilon_{\mathrm{opt}}$ |
| Adam | $m_j,v_j$ | $\eta,\beta_1,\beta_2,\epsilon_{\mathrm{opt}}$ |

So sánh cần đồng thời: return đánh giá, độ ổn định qua nhiều lần chạy độc lập,
loss huấn luyện và chi phí tính toán. **Không có lựa chọn thắng tuyệt đối**; một
lịch bước phù hợp có thể quan trọng hơn tên optimizer.

**Giới hạn.** Một bộ tối ưu tốt hơn không tự giải quyết bất ổn cốt lõi của
Q-learning với xấp xỉ hàm: nó không sửa cấu trúc bootstrap, tính khác chính sách
hay xấp xỉ hàm. Replay memory và mạng mục tiêu vẫn là thiết yếu. Công thức Adam
không tạo bảo đảm hội tụ cho DQN.

**Kiểm tra nhanh.** Optimizer thích nghi có sửa mục tiêu Bellman không? — Không;
nó chỉ chuẩn hóa gradient theo từng tọa độ, đích và dữ liệu không đổi.

---

## Phần 4 — Bất ổn, Atari, thực hành

<!-- note-topic-id: lec-08-topic-15 -->
### Atari, kiểm tra tổng hợp, thảo luận và đọc thêm

**Giao diện tối thiểu cho Atari.** Một quy trình DQN kinh điển:

- Đầu vào trạng thái: chồng bốn khung hình gần nhất đã tiền xử lý; một ảnh đơn
  lẻ không biểu lộ vận tốc hay hướng chuyển động, nhiều khung cung cấp động học
  ngắn hạn.
- Bộ mã hóa CNN theo sau bởi các tầng kết nối đầy đủ; đầu ra là một giá trị Q cho
  mỗi hành động khả dụng ($|\mathcal A|$ giá trị).
- Phần thưởng: thay đổi điểm số tức thời.

**Giới hạn.** Bốn khung là lựa chọn thiết kế kinh điển, **không phải định lý bảo
đảm Markov**: nó bổ sung động học ngắn hạn nhưng có thể vẫn thiếu biến ẩn hoặc
lịch sử dài hơn. Một đặc tả tái lập kết quả Atari còn cần tiền xử lý, lặp khung,
khởi đầu episode, kiến trúc, siêu tham số và giao thức đánh giá — nguồn không
cung cấp đầy đủ, nên ghi chú này không bịa các con số đó.

**Kiểm tra tổng hợp (bốn câu).**

1. Replay giảm cơ chế nào và để lại giới hạn nào? — Giảm tương quan ngắn hạn và
   tăng tái sử dụng dữ liệu; không tạo i.i.d., không bảo đảm hội tụ.
2. Mạng mục tiêu làm chậm đại lượng nào? — Sự thay đổi của đích bootstrap giữa
   các lần đồng bộ; đích vẫn nhảy tại mốc $\theta^-\leftarrow\theta$.
3. Khi nào cắt ngắn vẫn cần bootstrap? — Khi nhiệm vụ tiếp diễn và việc dừng chỉ
   do giới hạn thu thập ($U=1$, $Z=0$).
4. Optimizer thích nghi có sửa bộ ba nguy hiểm không? — Không; nó chỉ chuẩn hóa
   bước cập nhật, không đụng vào xấp xỉ hàm, bootstrap hay dữ liệu khác chính sách.

**Ba bài thảo luận (từ nguồn).**

1. Vì sao experience replay làm cho cập nhật mini-batch đáng tin cậy hơn?
2. Vì sao các bộ tối ưu thích nghi có thể giúp DQN dù chúng không sửa trực tiếp
   mục tiêu Bellman?
3. Tìm các phương pháp để tăng tính khám phá trong DQN.

**Đọc thêm / thực hành.** Đọc giả mã "Deep Q-learning with experience replay"
trong nguồn (tr. 20–21) và đối chiếu từng dòng với vòng DQN ở topic-10: điểm nào
giả mã nguồn đã có (replay dung lượng $N$, hai mạng $\theta,\theta^-$, đích có
mặt nạ terminal, đồng bộ mỗi $C$ bước), điểm nào ghi chú này bổ sung (hai cờ
$Z,U$, làm nóng $N_{\mathrm{start}}$, nhịp $F$, autoreset, dừng gradient). Khi
thực hành trên Atari, chỉ cần giữ hợp đồng tối thiểu: bốn khung → CNN → vector
$|\mathcal A|$ giá trị hành động.

---

## Ba bài tập (30 phút, 10 phút mỗi bài)

::: exercise Bài tập 1 — Tính đích, mất mát và gradient

Cho $b=2$, $\gamma=0{,}9$:

| $i$ | $R_i$ | $Z_i$ | $\max_{a'}Q_{\theta^-}(O'_i,a')$ | $q_i=Q_\theta(O_i,A_i)$ |
|---|---|---|---|---|
| 1 | 1 | 0 | 4 | 3,1 |
| 2 | −2 | 1 | 100 | −1,5 |

Tính $y_i$, $\delta_i=y_i-q_i$, MSE $L_B$ và $\partial L/\partial(q_1,q_2)$.
Cho biết mẫu nào làm tăng $q$ dưới một bước hạ gradient nhỏ.
:::

::: hint
Áp dụng mặt nạ $(1-Z_i)$ trước khi tính sai số. Số 100 ở mẫu 2 là mồi
kiểm tra: chuyển tiếp đã kết thúc nên nó không đi vào đích. Với MSE trung bình
trên hai mẫu, đạo hàm theo $q_i$ là $\tfrac{2}{b}(q_i-y_i)$.
:::

::: solution

- $y_1 = 1 + 0{,}9\cdot(1-0)\cdot 4 = 4{,}6$; $y_2 = -2 + 0{,}9\cdot(1-1)\cdot 100 = -2$.
- $\delta_1 = 4{,}6-3{,}1 = 1{,}5$; $\delta_2 = -2-(-1{,}5) = -0{,}5$.
- $L_B = \tfrac12(1{,}5^2 + 0{,}5^2) = \tfrac12(2{,}25+0{,}25) = 1{,}25$.
- $\partial L/\partial q_1 = 2\cdot\tfrac12\cdot(3{,}1-4{,}6) = -1{,}5$;
  $\partial L/\partial q_2 = 2\cdot\tfrac12\cdot(-1{,}5+2) = 0{,}5$.
- Mẫu 1 có gradient theo $q_1$ âm, nên phép trừ gradient làm $q_1$ tăng; mẫu 2
  có gradient dương nên $q_2$ giảm.
:::

::: exercise Bài tập 2 — Sửa bốn lỗi trong giả mã

Đoạn giả mã sau chứa bốn lỗi:

```
done = terminated or truncated
next_o = obs_after_step        # API có thể đã tự reset
y = r + gamma * (1 - done) * q_target(next_o).max()
loss = ((y - q_online(o)[a]) ** 2).mean()
```

Sửa: (i) quan sát kế tiếp, (ii) mặt nạ theo kết thúc MDP, (iii) đường gradient
(dừng gradient ở đích), (iv) phép chọn hành động theo lô.
:::

::: hint
Quan sát sau bước có thể thuộc lượt mới nếu API tự đặt lại — cần quan sát
cuối của chuyển tiếp. Biến done gộp không được dùng trong loss; cắt ngắn ngoài mô
hình vẫn bootstrap. Đích phải tính trong no-grad. Chọn một hành động đã lưu trên
mỗi hàng bằng gather, không lập chỉ mục vô hướng.
:::

::: solution

```
final_o = info.get("final_observation")
next_o = obs_after_step if final_o is None else final_o
z = terminated.float()          # kết thúc của MDP đang mô hình hóa
with no_grad():
    y = r + gamma * (1 - z) * q_target(next_o).max(dim=1).values
q = q_online(o).gather(1, a[:, None]).squeeze(1)
loss = ((y - q) ** 2).mean()
```

Giải thích: (i) dùng `final_observation` làm quan sát cuối của chuyển tiếp; (ii)
mặt nạ chỉ theo `terminated`, biến done gộp không dùng trong loss; (iii) `no_grad`
dừng gradient qua mạng mục tiêu; (iv) `gather` chọn một phần tử mỗi hàng rồi
`squeeze` về $[b]$. Giả định `final_observation` là quan sát cuối đúng và cờ
`terminated` của API trùng kết thúc MDP đang mô hình hóa; cắt ngắn ngoài mô hình
vẫn bootstrap.
:::

::: exercise Bài tập 3 — Thiết kế thí nghiệm loại bỏ

Thiết kế thí nghiệm loại bỏ (ablation) công bằng để đo tác động của replay và của
mạng mục tiêu: dự đoán trước tác động của từng nhánh lên tự tương quan của batch,
độ đa dạng mẫu, tốc độ đổi của đích, TD error, dao động tham số và đường return.
Nêu cách tổng hợp nhiều lần chạy độc lập. Không yêu cầu viết chương trình.
:::

::: hint
Công bằng nghĩa là mọi nhánh dùng cùng kiến trúc, ngân sách, bộ tối ưu,
lịch khám phá và cùng tập seed (hoặc ghép cặp seed giữa các nhánh). Chọn chỉ số đo
trước khi chạy; đừng chỉ nhìn một lần chạy.
:::

::: solution
Thiết kế: ba nhánh — đầy đủ, bỏ replay (học trên chuyển tiếp liên
tiếp), bỏ mạng mục tiêu (bootstrap từ mạng online); định trước cùng số lần chạy
cho mỗi nhánh và cùng ngân sách bước. Giữ nguyên mọi thành phần khác. Chỉ số đo:
return đánh giá theo chính sách tham lam riêng, TD error, chuẩn gradient, độ phân
tán giữa các lần chạy, và (cho replay) tự tương quan theo độ trễ của mẫu trong
batch. Tổng hợp: dùng cùng tập seed hoặc ghép cặp giữa các nhánh để giảm nhiễu so
sánh; báo thống kê trung tâm và độ phân tán (không chỉ trung bình). Kết luận mong
đợi theo lý thuyết của bài: bỏ replay làm tăng tương quan ngắn hạn; bỏ mạng mục
tiêu làm đích đổi sau mỗi bước tối ưu; cả hai nhánh không thay đổi việc bộ ba
nguy hiểm vẫn tồn tại — không nhánh cho bảo đảm hội tụ.
:::

---

## Kết luận

Hợp đồng của một bản DQN đúng gồm sáu điểm kiểm tra:

1. **Biểu diễn:** quan sát vào, vector giá trị Q cho tập hành động rời rạc ra;
   $Q_\theta$ nhận gradient, $Q_{\theta^-}$ tạo đích.
2. **Chuyển tiếp:** chỉ số nhất quán; phân biệt kết thúc MDP $Z$ với cắt ngắn
   ngoài mô hình $U$; lưu quan sát cuối của chuyển tiếp khi môi trường tự reset.
3. **Đích:** có mặt nạ $(1-Z)$, mạng mục tiêu và dừng gradient;
   $y_i=R_i+\gamma(1-Z_i)\max_{a'}Q_{\theta^-}(O'_i,a')$.
4. **Dữ liệu:** replay giảm tương quan và tái sử dụng dữ liệu nhưng không tạo
   i.i.d. và không bảo đảm hội tụ.
5. **Đồng bộ:** giữ $\theta^-$ cố định rồi sao chép $\theta^-\leftarrow\theta$ sau
   bước tối ưu theo chu kỳ $C$; hai đồng hồ $t$ và $k_{\mathrm{opt}}$ tách biệt.
6. **Kết luận:** đánh giá thực nghiệm qua nhiều lần chạy độc lập; không suy ra hội
   tụ tổng quát. Bộ ba nguy hiểm — xấp xỉ hàm, bootstrap, dữ liệu khác chính sách —
   vẫn còn trong DQN; replay và mạng mục tiêu giảm nhẹ hai biểu hiện trực tiếp
   (tương quan, mục tiêu di động) nhưng không loại bỏ nguyên nhân cấu trúc.

Mỗi mục trên chặn một lỗi có thể làm thuật toán sai nghĩa hoặc làm kết luận vượt quá
bằng chứng; dùng danh sách này như kiểm tra cuối trước khi đọc hoặc viết một cài
đặt DQN.
