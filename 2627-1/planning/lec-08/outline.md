# Dàn ý Bài 08: Deep Q-Learning

## Phạm vi

- Nguồn chính: `RL-hk2-2025-2026/lecture8-dqn.pdf`, 36 trang.
- Không có tài liệu bài tập hay code demo đi kèm.
- Đối tượng: sinh viên đã học Q-learning dạng bảng (Bài 06), xấp xỉ hàm tuyến tính, Q-learning bán gradient và bộ ba bất ổn (Bài 07).
- Đầu ra sau đợt sửa 2026-10-22: 7 mạch, 120 phút trên lớp (10 + 25 + 15 + 30 + 10 + 15 + 15) và 30 phút chữa bài. Danh sách trang theo mạch nằm trong `storyboard.md`, mục "Đợt sửa 2026-10-22: bản đồ bảy mạch".

## Mục tiêu học tập (đợt sửa 2026-10-22)

Mỗi mục tiêu ứng với một mạch từ 2 đến 7 và một sản phẩm kiểm được.

1. (Mạch 2) Viết $\mathbf q_\theta(o)\in\mathbb R^{|\mathcal A|}$, chọn $Q_\theta(O_i,A_i)$ theo hành động đã lưu và tính đích $y=R+\gamma(1-Z)\max_{a'}Q_{\theta^-}(O',a')$; phân biệt kết thúc ($Z$) với cắt ngắn ($U$). Sản phẩm: đích của hai mẫu chuyển, một mẫu có $Z=1$.
2. (Mạch 3) Nêu tác dụng và giới hạn của bộ nhớ phát lại; chỉ ra hai nguồn dữ liệu khác chính sách và lý do Q-learning một bước không cần tỉ số lấy mẫu quan trọng. Sản phẩm: xác suất hai mẫu liền nhau cùng vào một mini-batch.
3. (Mạch 4) Tính hàm mất mát và gradient theo $q$ trên một mini-batch; truy dấu một vòng DQN với hai bộ đếm $t$ và $k_{\mathrm{opt}}$. Sản phẩm: bảng lời giải mini-batch hai mẫu và bản sửa lỗi cài đặt đích.
4. (Mạch 5) Viết SGD, RMSprop và Adam theo từng tọa độ; nêu những gì lựa chọn bộ tối ưu không thay đổi (công thức đích, cách thu thập dữ liệu, lớp hàm), nên không loại được nguồn bất ổn. Sản phẩm: bảng so sánh trạng thái phụ và siêu tham số.
5. (Mạch 6) Tính độ thay đổi của đích tại mốc đồng bộ; nêu các giả thiết còn thiếu để có bảo đảm hội tụ khi đủ bộ ba bất ổn. Sản phẩm: $\Delta y$ của một mẫu chuyển và thiết kế thí nghiệm loại bỏ.
6. (Mạch 7) Giải một bước DQN trên mini-batch có cả kết thúc lẫn cắt ngắn, nêu kết quả và giả thiết đã dùng. Sản phẩm: lời giải bài tổng hợp CartPole.

## Bảy mạch (đợt sửa 2026-10-22)

HTML có đúng 7 section ngoài, độ sâu tối đa 2. Mạch $N$ mở tại `#/N`; từ mạch 2, trang đầu là trang tiêu đề mạch `L08-MNT`, `id="mach-N"`.

1. Mở đầu (10 phút): bìa có câu luận đề; Tiên quyết và quy ước (Nhắc lại, Ký hiệu); Mục tiêu học tập; Nội dung; Vấn đề trung tâm.
2. Mạng giá trị hành động và đích hồi quy (25 phút): giới hạn của bảng, đầu vào bốn khung Atari, giao diện $\mathbf q_\theta(o)$, tính Markov của bốn khung, ví dụ một tham số tạo cả dự đoán lẫn đích, mạng mục tiêu, đích hồi quy có mặt nạ, kết thúc và cắt ngắn.
3. Bộ nhớ phát lại (15 phút): tương quan giữa các mẫu chuyển liên tiếp, bộ nhớ phát lại, dữ liệu khác chính sách trong bộ nhớ, giới hạn của bộ nhớ phát lại.
4. Hàm mất mát và thuật toán DQN (30 phút): hàm mất mát trên mini-batch, dừng gradient ở đích, bài tập một mini-batch, vòng huấn luyện, thuật toán DQN (ba trang), kích thước tensor, bài tập lỗi cài đặt đích.
5. Bộ tối ưu theo gradient (10 phút): vai trò của bộ tối ưu, SGD, RMSprop, Adam, so sánh ba bộ tối ưu.
6. Bất ổn và phạm vi bảo đảm của DQN (15 phút): hai nguồn bất ổn và hai cơ chế giảm, ví dụ đích qua mốc đồng bộ, bộ ba bất ổn trong DQN, ví dụ hai trạng thái dùng chung tham số với mạng mục tiêu, bài tập thí nghiệm loại bỏ.
7. Tổng kết và chuyển tiếp (15 phút): kết quả và giả thiết, so sánh Q-learning bảng, tuyến tính và DQN, bài tập tổng hợp CartPole và lời giải, trả lời vấn đề trung tâm, câu hỏi tự kiểm tra, bài tập về nhà và tài liệu đọc.

Lời giải đầy đủ của các bài tập trên trang chiếu thuộc 30 phút chữa bài, ngoài 120 phút trên lớp.

## Bảng thuật ngữ Việt–Anh

Thuật ngữ theo Bài 06–07. Lần đầu xuất hiện trong mỗi tài liệu (trang chiếu, ghi chú bài giảng), viết tên tiếng Việt kèm tên tiếng Anh trong ngoặc; các lần sau chỉ dùng tên tiếng Việt.

| Tiếng Việt | Tiếng Anh | Quy ước |
|---|---|---|
| thăm dò | exploration | không dùng "khám phá" |
| tham lam | greedy | |
| $\epsilon_{\mathrm{exp}}$-tham lam | $\epsilon$-greedy | dòng "Ký hiệu:" nối $\epsilon_{\mathrm{exp}}$ với $\varepsilon$ của Bài 06 |
| mẫu chuyển | transition | không dùng "chuyển tiếp" |
| lượt | episode | |
| lợi tức | return | |
| sai số TD | TD error | |
| bootstrap, đích bootstrap | bootstrap, bootstrap target | giữ như Bài 07 |
| bán gradient | semi-gradient | Bài 07 |
| xấp xỉ hàm | function approximation | Bài 07 |
| học khác chính sách | off-policy learning | |
| tỉ số lấy mẫu quan trọng | importance sampling ratio | Bài 07 |
| bộ ba bất ổn | deadly triad | không dùng "bộ ba nguy hiểm", kể cả trong SVG và ghi chú bài giảng |
| mạng giá trị hành động | action-value network | DQN: Deep Q-Network, giữ tên riêng |
| mạng trực tuyến | online network | $Q_\theta$ |
| mạng mục tiêu | target network | $Q_{\theta^-}$ |
| đồng bộ (sao chép cứng) | hard target update | $\theta^-\leftarrow\theta$ |
| đích hồi quy | regression target | $y_i$ |
| mặt nạ kết thúc | terminal mask | $(1-Z)$ |
| kết thúc | termination | cờ $Z$ |
| cắt ngắn | truncation | cờ $U$ |
| đặt lại, tự đặt lại | reset, autoreset | |
| bộ nhớ phát lại | experience replay; replay buffer | $\mathcal D$ |
| bộ đệm vòng; con trỏ ghi | ring buffer (circular buffer); write pointer | dung lượng $N$ |
| rút đều (có hoặc không hoàn lại) | uniform sampling (with or without replacement) | $b$ lần rút |
| làm nóng bộ nhớ | warm-up | $N_{\mathrm{start}}$ |
| phép chọn theo hành động | gather | |
| dừng gradient | stop-gradient | $\operatorname{sg}$ |
| hàm mất mát | loss | $L_B$ |
| sai số bình phương trung bình | mean squared error (MSE) | |
| bộ tối ưu | optimizer | |
| hạ gradient ngẫu nhiên | stochastic gradient descent (SGD) | |
| hiệu chỉnh lệch | bias correction | Adam |
| mạng tích chập | convolutional neural network (CNN) | |
| lan truyền ngược | backpropagation | |
| thí nghiệm loại bỏ | ablation | |

## Mục cũ trước đợt sửa 2026-10-22

Các mục dưới đây mô tả bản trước đợt sửa. Mục nào sai khác với cấu trúc mới sẽ được thay khi sửa trang tương ứng.

### Truy nguyên các trang bổ sung (bản cũ)

- `L08-20` (kích thước tensor của mini-batch Atari): truy nguyên từ công thức loss `L08-17` và giao diện mạng `L08-07`; biến công thức thành shape/dtype/device cụ thể trước khi kiểm tra.
- `L08-21` (kiểm tra dấu gradient hai mẫu): truy nguyên từ ví dụ số `X01` và công thức loss; kiểm hướng cập nhật trước khi sửa giả mã.
- `X01` (bài tính đích, TD error, MSE, gradient): truy nguyên trực tiếp từ công thức đích và loss của nguồn.
- `X03` (bài ablation): truy nguyên từ hai cơ chế replay và mạng mục tiêu; dùng lại đúng hai cơ chế đã dạy và thu hồi bốn kết quả `L08-02`.

### Câu hỏi khám phá nguồn tr.36 (bản cũ)

Câu hỏi khám phá ở nguồn tr.36 không được đưa lên mặt trang vì đã có `L08-33` (kiểm tra tổng hợp bốn câu) và `X03` (ablation) phủ cùng mục tiêu kiểm; nội dung liên quan được đưa vào notes của `L08-33`. Không thêm câu hỏi mới lên mặt trang.

## Ánh xạ lecture note → deck

Mỗi trang có đúng một `data-note-topic-id`; một chủ đề có thể trải trên nhiều trang.

| `note-topic-id` | `data-slide-id` |
|---|---|
| `lec-08-topic-01` | `L08-M2T`, `L08-03` |
| `lec-08-topic-02` | `L08-07`, `L08-07b`, `L08-07c` |
| `lec-08-topic-03` | `L08-08` |
| `lec-08-topic-04` | `L08-09` |
| `lec-08-topic-05` | `L08-12`, `L08-12b` |
| `lec-08-topic-06` | `L08-13` |
| `lec-08-topic-07` | `L08-14` |
| `lec-08-topic-08` | `L08-10`, `L08-10b` |
| `lec-08-topic-09` | `L08-M4T`, `L08-17`, `X01`, `L08-21` |
| `lec-08-topic-10` | `L08-11`, `L08-18a`, `L08-18`, `L08-19`, `L08-19b`, `X02`, `X02b` |
| `lec-08-topic-11` | `L08-20` |
| `lec-08-topic-12` | `L08-M6T`, `L08-27`, `L08-29`, `L08-30`, `L08-30b`, `X03`, `X03b` |
| `lec-08-topic-13` | `L08-01b`, `L08-01b2`, `L08-01c` |
| `lec-08-topic-14` | `L08-M5T`, `L08-22`–`L08-26` |
| `lec-08-topic-15` | `L08-M7T`, `L08-34`, `L08-34b`, `L08-K1`, `L08-K1b`, `L08-K2`, `L08-33` |
| `lec-08-topic-16` | `L08-31`, `L08-32` |
| `lec-08-topic-17` | `L08-01`, `L08-02`, `L08-02b`, `L08-02c` |
| `lec-08-topic-18` | `L08-M3T`, `L08-28` |
| `lec-08-topic-19` | `L08-05r` |

## Ánh xạ nguồn (bản cũ; cột "trang đích" được cập nhật khi sửa từng trang, các lệch thứ tự của đợt sửa 2026-10-22 ghi trong `storyboard.md`)

| trang nguồn | trang đích | quyết định | lý do |
|---|---|---|---|
| 1 | `L08-01` | giữ | Tiêu đề. |
| 2 | `L08-02` | sửa | Đổi dàn ý thành kết quả học tập. |
| 3 | `L08-04`–`L08-05` | tách | Tách loại thuật toán khỏi hành vi–đích. |
| 4 | `L08-04`, `L08-08`–`L08-09` | sửa | Chuẩn hóa chỉ số và thêm mặt nạ kết thúc. |
| 5 | `L08-04`, `L08-18`–`L08-19` | tách | Dùng cầu nối dạng bảng rồi xây giả mã DQN đầy đủ. |
| 6 | `L08-05`, `L08-33` | gộp | Hoàn tất vai trò khám phá và kiểm tra. |
| 7 | `L08-05` | sửa | Giới hạn kết luận hội tụ vào dạng bảng với giả thiết rõ. |
| 8–9 | `L08-06` | gộp, lược | Bỏ cận mẫu thiếu mô hình định lý; giữ vấn đề quy mô. |
| 10–11 | `L08-03`, `L08-06` | gộp, lược | Bỏ cận tuyến tính thiếu cấu trúc MDP và thuật toán cụ thể. |
| 12–13 | `L08-27`, `L08-30` | gộp, sửa | Hai nguồn bất ổn; bộ ba bất ổn xét riêng ở `L08-30`. |
| 14–15 | `L08-03`, `L08-07` | gộp | Giới hạn bảng và giao diện DQN. |
| 16 | `L08-07`–`L08-10`, `L08-17` | tách, sửa | Đặt phản ví dụ mục tiêu di động trước hai mạng; thêm mặt nạ, batch và dừng gradient. |
| 17 | `L08-07`, `L08-31` | gộp | MLP cho vector, CNN cho ảnh. |
| 18 | `L08-11`, `L08-18`–`L08-19` | tách, sửa | Vẽ lại vòng huấn luyện; bổ sung warmup, tần suất cập nhật và hai bộ đếm. |
| 19 | `L08-13`–`L08-16` | tách, sửa | Replay và target network là hai cơ chế riêng. |
| 20 | `L08-13`, `L08-17` | gộp, sửa | Chuẩn hóa $\theta,\theta^-$ và batch từ $\mathcal D$. |
| 21 | `L08-12`, `L08-18`–`L08-19`, `X02` | tách, sửa | Chuẩn hóa hai cờ, final observation khi autoreset và mặt nạ theo MDP đang mô hình hóa. |
| 22 | `L08-10`, `L08-22` | tách, sửa | Gradient chỉ qua giá trị đã gather từ mạng online; khai báo miền optimizer. |
| 23 | `L08-22`, `L08-26` | gộp | Thu hẹp vai trò optimizer. |
| 24 | `L08-23` | giữ, sửa | Công thức SGD và phạm vi. |
| 25 | `L08-24` | giữ, sửa | Nêu phép toán theo tọa độ và quy ước $\epsilon_{\mathrm{opt}}$. |
| 26 | `L08-25` | giữ, sửa | Sửa mẫu số Adam và bổ sung khởi tạo. |
| 27–28 | `L08-26` | gộp, sửa | Không tuyên bố phương pháp thắng tuyệt đối hay hội tụ nhanh. |
| 29 | `L08-07`, `L08-27` | tách, sắp xếp lại | Đặt phản ví dụ mục tiêu di động trước mạng mục tiêu. Hai nguồn bất ổn; bộ ba bất ổn xét riêng ở `L08-30`. |
| 30 | `L08-14`, `L08-28` | sửa | Replay giảm tương quan, không tạo i.i.d. |
| 31 | `L08-29` | giữ, sửa | Mục tiêu đổi ở mốc đồng bộ. |
| 32 | `L08-13`–`L08-14` | gộp, sửa | Cơ chế và giới hạn của replay. |
| 33 | `L08-07`, `L08-15`–`L08-16` | tách, sắp xếp lại | Khai báo và khởi tạo hai mạng trước đích; sau đó nối đường gradient với đồng bộ cứng. |
| 34 | `L08-17` | giữ, sửa | Mục tiêu tích hợp có mặt nạ và stop-gradient. |
| 35 | `L08-31`–`L08-32` | tách, sửa | Bốn khung là lịch sử quan sát, không bảo đảm Markov. |
| 36 | `L08-33` | sửa | Chuyển thành kiểm tra tổng hợp có phạm vi. |

## Thuật ngữ và ký hiệu

Bảng này khớp trang `L08-01c` (ký hiệu dùng ở nhiều mạch) và mục "Bảng ký hiệu" của ghi chú bài giảng; ký hiệu riêng một mạch ($Z$, $U$, $\mathcal D$, $N$, $b$, $C$, $F$, $N_{\mathrm{start}}$, $q_i$, …) được giới thiệu tại trang dùng lần đầu.

| ký hiệu | nghĩa |
|---|---|
| $\mathcal O$, $O_t$ | tập quan sát; quan sát hoặc biểu diễn trạng thái đưa vào mạng |
| $S_t$ | trạng thái Markov khi giả thiết đủ quan sát được áp dụng |
| $A_t\in\mathcal A$, $\lvert\mathcal A\rvert$ | hành động; số hành động; DQN cơ bản cần $\mathcal A$ rời rạc hữu hạn (không dùng $m$ như Bài 06–07 vì $m_j$ dành cho Adam) |
| $q_*$ | giá trị hành động tối ưu |
| $\theta\in\mathbb R^d$ | tham số mạng trực tuyến, đóng vai $w$ của Bài 07 |
| $Q_\theta(o,a)$, $\mathbf q_\theta(o)$ | giá trị hành động do mạng tính; vector theo mọi hành động |
| $R_{t+1}$ | phần thưởng sau khi thực hiện $A_t$ trong chỉ số thời gian |
| $Z_{t+1}$ | cờ kết thúc thật của MDP |
| $U_{t+1}$ | cờ cắt ngắn do cơ chế thu thập |
| $Q_\theta$ | mạng trực tuyến, nhận gradient |
| $Q_{\theta^-}$ | mạng mục tiêu, giữ cố định giữa các lần đồng bộ |
| $\mathcal D$ | bộ nhớ phát lại |
| $\operatorname{sg}$ | dừng gradient qua đối số |
| $(O_i,A_i,R_i,O'_i,Z_i,U_i)$ | mẫu thứ $i$ sau khi lấy mini-batch, $i=1,\ldots,b$ |
| $b$ | số mẫu chuyển trong mini-batch |
| $q_i$ | dự đoán của mạng trực tuyến trên mẫu $i$, $q_i=Q_\theta(O_i,A_i)$; khác giá trị thật $q_*$, cần dòng "Ký hiệu:" khi dùng lần đầu |
| $y_i$ | đích hồi quy của mẫu $i$ |
| $\delta_t$, $\delta_i$ | sai số TD theo thời gian; theo mẫu |
| $L_B(\theta)$ | hàm mất mát trên mini-batch $B$ |
| $g_j$ | gradient mini-batch ở bước tối ưu $j$ |
| $t\in\mathbb N_0$ | bộ đếm bước môi trường |
| $k_{\mathrm{opt}}\in\mathbb N_0$ | bộ đếm bước tối ưu; tăng sau khi cập nhật $\theta$ |
| $N\in\mathbb N_+$ | dung lượng bộ nhớ phát lại |
| $N_{\mathrm{start}}\in\mathbb N_+$ | số mẫu tối thiểu trước bước tối ưu đầu tiên, $b\le N_{\mathrm{start}}\le N$ |
| $F\in\mathbb N_+$ | số bước môi trường giữa hai lần tối ưu |
| $C\in\mathbb N_+$ | số bước tối ưu giữa hai lần đồng bộ cứng |
| $\gamma\in[0,1)$ | hệ số chiết khấu; bài dùng $\gamma<1$ như giả thiết của định lý hội tụ dạng bảng (`L08-01c`) |
| $\alpha_t>0$ | bước học dạng bảng; nếu phát biểu hội tụ, dãy bước phải thỏa Robbins–Monro theo từng cặp trạng thái–hành động |
| $\eta>0$ | tốc độ học của bộ tối ưu |
| $j\in\mathbb N_+$ | chỉ số bước của bộ tối ưu, $j=k_{\mathrm{opt}}$ sau khi tăng |
| $\rho,\beta_1,\beta_2\in[0,1)$ | hệ số suy giảm của RMSprop và Adam; $\rho$ ở đây khác tỉ số lấy mẫu quan trọng $\rho_t$ của Bài 07, khai báo bằng dòng "Ký hiệu:" ở mạch 5 |
| $m_j,v_j$ | trung bình trượt của $g_j$ và của $g_j\odot g_j$; khác $v_\pi$, khai báo bằng dòng "Ký hiệu:" ở mạch 5 |
| $\epsilon_{\mathrm{exp}}\in[0,1]$ | xác suất thăm dò của chính sách hành vi; là $\varepsilon$ của Bài 06 |
| $\epsilon_{\mathrm{opt}}>0$ | hằng số ổn định số trong mẫu số của bộ tối ưu |

Quy ước thời gian chỉ dùng khi tương tác với môi trường: $(O_t,A_t,R_{t+1},O_{t+1},Z_{t+1},U_{t+1})$. Sau khi lấy mini-batch, dùng duy nhất $(O_i,A_i,R_i,O'_i,Z_i,U_i)$ với $i=1,\ldots,b$; không trộn $i+1$ vào chỉ số batch.

## Phân bổ thời lượng (đợt sửa 2026-10-22)

- 120 phút trên lớp: mạch 1 10 phút, mạch 2 25 phút, mạch 3 15 phút, mạch 4 30 phút, mạch 5 10 phút, mạch 6 15 phút, mạch 7 15 phút.
- Trong mạch 5, ba trang SGD, RMSprop, Adam là phần co giãn; khi thiếu giờ, đi thẳng từ trang vai trò của bộ tối ưu sang bảng so sánh, nên bảng so sánh phải tự đọc được nhờ dòng "Ký hiệu:".
- 30 phút chữa bài (ngoài 120 phút): lời giải đầy đủ của bài tập một mini-batch, lỗi cài đặt đích, thí nghiệm loại bỏ và bài tổng hợp CartPole.

## Tài sản SVG

`table-vs-dqn.svg`, `dqn-training-loop.svg`, `replay-buffer.svg`, `target-network-timeline.svg`, `dqn-computation-graph.svg`, `tensor-contract.svg`, `deadly-triad.svg`, `atari-pipeline.svg`.
