# Chỉ dẫn cho người soạn Bài 12

Tệp này chứa chỉ dẫn nội bộ. Không đưa mã trang, thời lượng, nhánh cắt, trạng thái rà soát hoặc lời nhắc cho người soạn lên mặt trang chiếu hay ghi chú diễn giả.

## Mạch bắt buộc

Giữ thứ tự:

Tám mục dưới đây là thứ tự nội dung; khi trình bày, chúng được gộp thành bảy mạch ngoài theo `outline.md`.

1. hợp đồng trò chơi Markov và MDP cảm sinh;
2. CTDE và miền thông tin;
3. COMA;
4. VDN rồi QMIX;
5. MADDPG như cầu nối từ Bài 11;
6. IPPO/MAPPO rồi HAPPO/HATRPO;
7. benchmark và framework;
8. giao tiếp.

Không chuyển phần benchmark lên trước công thức. Không dạy communication như một thuộc tính mặc định của CTDE.

## Tuyến 110 và 120 phút

- Tuyến cốt lõi 110 phút dùng 42 trang. Tại `L12-34` (`#/5/6`), bấm Phải để sang `L12-38` (`#/6/1`). Tại `L12-42` (`#/6/5`), bấm Phải để sang kết luận `L12-45` (`#/7/1`).
- Tuyến đủ 120 phút dùng phím Xuống tại hai điểm cắt: `L12-35`–`L12-37` (`#/5/7`–`#/5/9`, 6 phút) và `L12-43`–`L12-44` (`#/6/6`–`#/6/7`, 4 phút). Sau đuôi dọc, bấm Phải để tiếp tục.
- Cụm bài tập luôn đứng sau kết luận trong mạch cuối. Từ `L12-45` (`#/7/1`), dùng phím Xuống cho `X01`–`X03` (`#/7/2`–`#/7/4`). Trên mỗi bài, lần Xuống đầu mở đáp án fragment; lần Xuống kế tiếp sang bài sau. Ba bài dùng 8, 12 và 10 phút; không xen chúng vào mạch 120 phút.
- Nếu chỉ có 110 phút, giao bảng framework, checklist tái lập, tích hợp message và mô hình đe dọa làm tài liệu tự đọc. `L12-34`, `L12-38`, `L12-42` và `L12-45` vẫn nối được khi bỏ hai đuôi.
- Không cắt `L12-04`–`L12-12` cùng `L12-07B`, `L12-13`–`L12-22B` hoặc các công thức `L12-23`, `L12-25`, `L12-28`.

## Hợp đồng ký hiệu

- $\Delta(\mathcal X)$ là tập phân phối trên $\mathcal X$; $P:\mathcal S\times\mathcal A\to\Delta(\mathcal S)$ và $\Omega:\mathcal S\to\Delta(\mathcal O)$.
- $s$ là trạng thái môi trường; $o_i$ là quan sát hiện tại; $\tau_{t,i}=(o_{0,i},a_{0,i},\ldots,o_{t,i})$ là lịch sử cục bộ làm input actor.
- Tích $\prod_{j\ne i}\pi_j(a_j\mid s)$ ở MDP cảm sinh giả định hành động cục bộ độc lập có điều kiện theo $s$; nếu joint policy có tương quan, phải dùng phân phối joint có điều kiện.
- $a_i$ là hành động cục bộ; $\mathbf a=(a_1,\ldots,a_N)$ là hành động chung.
- $Q$ không chỉ có một nghĩa: COMA dùng critic chung $Q(s,\mathbf a)$; MADDPG dùng critic riêng $Q_i(x,\mathbf a)$; VDN/QMIX dùng $Q_i(\tau_i,a_i)$ và $Q_{\mathrm{tot}}$.
- $A_i^{\mathrm{COMA}}$ là advantage; $A_{t,i}$ trong log-policy là biến hành động. Khi nói, phân biệt bằng ngữ cảnh và tên đầy đủ.
- $r_{t,i}(\theta)$ ở MAPPO là tỷ số policy, không phải reward $r_i$.
- $x$ là input chung của critic MADDPG; phải ghi là joint observation, state hay biến khác. Dấu gạch trên $\bar\theta$, $\bar\phi$ chỉ tham số target.
- $m=1-d$, bằng $0$ ở terminal thật và $1$ nếu tiếp tục; cutoff chưa terminal phải giữ bootstrap theo hợp đồng implementation.
- QMIX dùng utility/mixer online để học, utility online để chọn next action và target mixer/utility để đánh giá trong biến thể double-Q của bài.
- HAPPO giữ $M_m$ cố định khi clip ratio tác tử hiện tại, rồi đặt $M_{m+1}=r_m^{\mathrm{new}}M_m$.

## Công thức không được phục hồi từ nguồn

1. Không viết joint policy deterministic $\pi:S\to\mathcal A$ rồi dùng như stochastic product policy.
2. Không viết zero-sum dưới dạng $0=r=\sum_i r_i$.
3. Không bỏ trọng số $\pi_i(a_i'\mid\tau_i)$ trong baseline COMA.
4. Không dùng $\nabla\log\pi_i$ dưới nhãn MADDPG; MADDPG dùng deterministic chain rule.
5. Không gọi $Q_{\mathrm{tot}}=\sum_iQ_i$ là QMIX; đó là VDN.
6. Không viết hai `argmax` như vector bằng nhau khi có tie; dùng quan hệ bao hàm giữa tích các tập local argmax và tập global argmax.
7. Không chọn và đánh giá next action QMIX bằng một mạng mơ hồ; ghi rõ online/target, mask terminal và đường backprop.
8. Không đưa global state vào actor MAPPO khi thực thi hoặc bỏ chỉ số $i$ khỏi $\pi_{\theta_i}$ khi các actor có tham số riêng.
9. Không nói HAPPO chỉ nhân ratio cũ mà bỏ objective clipped của tác tử hiện tại; không tái tính GAE sau mỗi agent.
10. Không gọi full communication là CTDE hoặc định nghĩa full bằng chu kỳ $T$.

## Đáp án và lỗi dễ mắc

### `X01`

- $5^{10}=9.765.625$.
- Zero-sum ba tác tử: $r_1(s,\mathbf a)+r_2(s,\mathbf a)+r_3(s,\mathbf a)=0$.
- Critic tập trung, actor cục bộ là CTDE.
- MDP cảm sinh đổi vì phân phối hành động của các tác tử khác dưới $\pi_{-i}$ đổi; không bắt buộc $P$ nền đổi.
- Nếu một lệch đơn phương tăng $J_i$ từ $5$ lên $5{,}4$ trong khi giữ $\pi_{-i}^*$, joint policy không phải Nash.

### `X02`

- Baseline COMA: $5$; nếu action thực có $Q=6$, advantage bằng $1$.
- QMIX double-Q: utility online chọn từng action khả dụng; target mixer/utility đánh giá; $\gamma m$ loại bootstrap ở terminal.
- Với $M_2=2{,}2$, $r_2(\theta)=1{,}3$, $\epsilon=0{,}2$, hạng clipped dương bằng $\min(2{,}86,2{,}64)=2{,}64$; nếu $r_2^{\mathrm{new}}=0{,}9$ thì $M_3=1{,}98$.
- MADDPG actor chạy từ $o_i$; centralized critic học từ $x$ và joint action; target dùng mọi target actor.

### `X03`

- Chấp nhận nhiều benchmark nếu người học nêu đúng action, observation và cấu hình phải khóa.
- Actor dùng message thì message phải có khi thực thi.
- Full topology trả lời “gửi cho ai”; chu kỳ $T$ trả lời “gửi khi nào”.
- Ít nhất phải có seed/số lần chạy, metric và aggregation/uncertainty, budget và protocol. Chấp nhận phiên bản environment như một trường đúng.

## Phạm vi bằng chứng

- Không dựng lại các đường cong ở trang nguồn 21, 26, 28, 31, 38, 40, 42 và 46. Ảnh không cung cấp đủ dữ liệu seed, aggregation, uncertainty và cấu hình.
- Không gọi MAPPO, HARL hoặc framework nào là tốt nhất hay state of the art ngoài một benchmark và mốc cụ thể.
- Số tác tử trong MAgent/Pogema là cấu hình nguồn, không phải giới hạn hệ thống.
- AutoGen là framework agent LLM; không mặc nhiên là MARL hoặc self-training.
- OpenAI Five là ca lịch sử. Nếu dùng tỷ lệ $99{,}4\%$, phải nói rõ Arena 18–21/4/2019 và mẫu $7215/7257$.
- Tính năng PyMARL, EPyMARL, MARLlib và HARL phải gắn phiên bản/commit nếu dùng cho bài thực hành mới.

## Chỉ dẫn SVG

- Không thay SVG bằng screenshot để tiết kiệm thời gian.
- Giữ `role="img"`, `title`, `desc`, nhãn và đường viền. Mọi phân biệt bằng màu phải có thêm vị trí, nhãn hoặc hình dạng.
- `two-views.svg`: không vẽ $P$ nền biến đổi; nhãn phải nói $\pi_{-i}$ đổi.
- `ctde-flow.svg`: training và execution phải là hai dải riêng.
- `coma-counterfactual.svg`: chỉ thay $a_i'$, giữ $\mathbf a_{-i}$.
- `qmix-mixer.svg`: trọng số không âm và state conditioning chỉ thuộc mixer lúc huấn luyện.
- `comm-topologies.svg` và `comm-gate.svg`: topology và frequency/gating là hai hình riêng.
- Khi giảng `L12-38`–`L12-41`, giữ đúng ba tầng: input actor trong ví dụ robot kho → topology cho biết cạnh nào hợp lệ → policy/gate quyết định có dùng cạnh đó và khi nào. Không đưa topology trở lại hàng “quyết định gửi”.
- Mọi nhãn SVG có nghĩa phải giữ cỡ nguồn ít nhất `30px`; không thu hình đến mức chữ hiển thị dưới khoảng `0.75em`. `path-to-marl.svg`, `two-views.svg` và `benchmark-map.svg` đã có chiều cao cục bộ riêng.

## Kiểm tra sau sửa

Sau mọi thay đổi công thức ở `L12-07`–`L12-09`, gồm `L12-07B`, `L12-16`, `L12-21`–`L12-22B`, `L12-23`, `L12-25` hoặc `L12-28`, yêu cầu tác tử toán rà lại. Sau thay đổi thứ tự, rà trang bị đổi và hai trang lân cận mỗi phía. Không cập nhật `index.html` cho tới khi bài qua kiểm định cuối.
