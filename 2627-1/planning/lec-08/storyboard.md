# Storyboard Bài 08

## Hành trình khái niệm và thời lượng

| cụm | chu trình | trang | đầu vào → sản phẩm | tuyến chính | linh hoạt |
|---|---|---|---|---:|---:|
| Mở bài | vấn đề → trực giác | `L08-01`–`L08-03` | Bảng Q → nhu cầu tham số dùng chung | 7 phút | 0 |
| Q-learning làm cầu nối | hình thức → giới hạn | `L08-04`–`L08-06` | Cập nhật bảng → hành vi/đích và phạm vi kết luận | 13 phút | 0 |
| Giao diện, hai mạng và đích | vấn đề → trực giác → ví dụ → hình thức → ứng dụng → kiểm tra | `L08-07`–`L08-10`, `L08-20`, `X01` | Hai mạng đã khởi tạo → đích có mặt nạ, loss, tensor và gradient | 17 phút | 0 |
| Vòng DQN | vấn đề → trực giác → ví dụ → hình thức → ứng dụng → kiểm tra | `L08-11`–`L08-21`, `X02` | Chuyển tiếp → replay, đồng bộ, giả mã và batch Atari | 43 phút | 0 |
| Bộ tối ưu phụ trợ | chu trình rút gọn | `L08-22`–`L08-26` | Gradient loss → quy tắc cập nhật có phạm vi | 7 phút | 10 phút |
| Bất ổn | vấn đề → trực giác → ví dụ → hình thức → ứng dụng → kiểm tra | `L08-27`–`L08-30`, `X03` | Bootstrap đang học → mục tiêu di động, replay và deadly triad | 13 phút | 0 |
| Atari và tổng hợp | ứng dụng → kiểm tra | `L08-31`–`L08-34` | Lịch sử bốn khung → kiểm hợp đồng DQN | 10 phút | 0 |

Tuyến chính có 110 phút. Ba bài tập dọc có 30 phút: `X01`, `X02`, `X03`, mỗi bài 10 phút. Từ `L08-22`, đi ngang sang `L08-26` để giữ tuyến cốt lõi; đi xuống `L08-23`–`L08-25` cho 10 phút linh hoạt về SGD, RMSprop và Adam. Optimizer là công cụ phụ nên không chiếm một chu trình trọng tâm riêng.

## Chu trình sáu bước cho các khái niệm trọng tâm

### 1. Từ bảng Q sang biểu diễn DQN

| bước | mã trang | kiến thức hoặc dữ kiện đầu vào | sản phẩm học tập | gộp / không áp dụng |
|---|---|---|---|---|
| Vấn đề | `L08-03` | Bảng có một ô cho mỗi $(s,a)$ | Nêu được giới hạn không chia sẻ thông tin | Gộp với trực giác vì cùng một hình so sánh. |
| Trực giác | `L08-03` | Tham số dùng chung | Giải thích được khái quát và giao thoa | Gộp với vấn đề; hai hệ quả đi cùng một phép thay thế. |
| Ví dụ | `L08-06` | $|\mathcal S||\mathcal A|$ và không gian liên tục | So sánh được chi phí bảng với xấp xỉ hàm | Ví dụ định tính; không dùng cận mẫu thiếu giả thiết. |
| Hình thức / thuật toán | `L08-07` | $o\in\mathcal O$, $a\in\mathcal A$ | Đọc được giao diện vector Q và lý do tách hai mạng | Cùng trang đặt phản ví dụ một mạng trước $\theta^-\leftarrow\theta$. |
| Ứng dụng | `L08-20`, `L08-31` | Giao diện vector Q | Truy được đầu vào ảnh $[b,4,h,w]$ đến đầu ra $[b,|\mathcal A|]$ | Hai trang: hợp đồng tensor trước, pipeline Atari sau. |
| Kiểm tra | `L08-32` | Lịch sử bốn khung | Phân biệt biểu diễn giàu thông tin với bảo đảm Markov | Không gộp. |

Dữ kiện truyền xuyên cụm: $o$, $\mathcal A$ và $\mathbf q_\theta(o)$ từ `L08-07` được giữ nguyên ở `L08-20`, `L08-31` và `L08-32`.

### 2. Đích bootstrap và loss DQN

| bước | mã trang | kiến thức hoặc dữ kiện đầu vào | sản phẩm học tập | gộp / không áp dụng |
|---|---|---|---|---|
| Vấn đề | `L08-04`, `L08-07` | Phép sao lưu tối ưu Bellman và tham số dùng chung | Nhận ra một mạng đang học có thể làm đổi cả dự đoán lẫn đích | `L08-04` khôi phục đích bảng; `L08-07` đặt phản ví dụ trước giải pháp hai mạng. |
| Trực giác | `L08-08` | $Q_\theta$, $Q_{\theta^-}$ đã khởi tạo | Xem bootstrap như nhãn hồi quy tạm thời | Không gộp. |
| Ví dụ | `L08-09` | $R=-2$, $\gamma=0{,}9$, giá trị bootstrap 100 | Tính được hai đích khi $Z=0$ và $Z=1$ | Không gộp. |
| Hình thức / thuật toán | `L08-10`, `L08-15`–`L08-17` | Batch $\{(O_i,A_i,R_i,O'_i,Z_i,U_i)\}_{i=1}^b$ | Viết đúng $y_i$, MSE, gather, $\operatorname{sg}$ và thứ tự đồng bộ | `L08-15` nối hai đường tính; `L08-16` đồng bộ sau cập nhật. |
| Ứng dụng | `L08-20` | $b$, bốn khung Atari, $|\mathcal A|$ | Truy đủ $O,O'$, online/target, gather/max, $R,Z,U$ và loss | Không gộp với kiểm tra để người học thấy hợp đồng tensor trước khi tính. |
| Kiểm tra | `X01`, `L08-21` | Batch hai mẫu, $y=(4{,}6,-2)$ | Tính loss và kiểm đúng dấu gradient | Bài dọc tính đủ; trang chính kiểm dấu cập nhật. |

Dữ kiện truyền xuyên cụm: quy ước batch $(O_i,A_i,R_i,O'_i,Z_i,U_i)$, $i=1,\ldots,b$, bắt đầu ở `L08-10`, được dùng lại nguyên dạng ở `L08-17`, `L08-19`, `L08-20` và `L08-29`.

### 3. Bộ nhớ phát lại

| bước | mã trang | kiến thức hoặc dữ kiện đầu vào | sản phẩm học tập | gộp / không áp dụng |
|---|---|---|---|---|
| Vấn đề | `L08-11` | Chuyển tiếp liên tiếp từ một quỹ đạo | Nhận ra thu thập và tối ưu dùng hai nhịp khác nhau | Gộp với trực giác qua sơ đồ vòng huấn luyện. |
| Trực giác | `L08-11` | Hai luồng tương tác và tối ưu | Giải thích vì sao cần nơi lưu rồi lấy lại dữ liệu | Gộp với vấn đề. |
| Ví dụ | `L08-13` | Dòng thời gian các chuyển tiếp | Chỉ được các vị trí rải ra trong một mini-batch | Hình replay đồng thời minh họa cơ chế. |
| Hình thức / thuật toán | `L08-12`–`L08-14` | Schema thời gian và final observation | Mô tả hai cờ, autoreset, bộ đệm vòng và giới hạn không i.i.d. | `L08-12` là tiên quyết schema; `L08-13` gộp ví dụ với hình thức. |
| Ứng dụng | `L08-18`–`L08-19` | $\mathcal D$, $N$, $N_{\mathrm{start}}$, $b$, $F$ | Truy dấu lưu, làm nóng và lấy batch theo tần suất | Không gộp. |
| Kiểm tra | `X02`, `L08-33` | Hai cờ, final observation và batch lấy lại | Sửa bốn lỗi: quan sát, mask, dừng gradient, gather | `X02` kiểm cài đặt; `L08-33` kiểm giải thích. |

Dữ kiện truyền xuyên cụm: chuyển tiếp theo thời gian ở `L08-12` được lưu tại `L08-13`, rồi sau khi lấy batch đổi tên chỉ số sang $(O_i,A_i,R_i,O'_i,Z_i,U_i)$ ở `L08-19`.

### 4. Vòng DQN hoàn chỉnh

| bước | mã trang | kiến thức hoặc dữ kiện đầu vào | sản phẩm học tập | gộp / không áp dụng |
|---|---|---|---|---|
| Vấn đề | `L08-11` | Mạng cần vừa tương tác vừa học từ dữ liệu cũ | Xác định hai luồng phải ghép trong một vòng | Gộp với trực giác. |
| Trực giác | `L08-11` | Vòng môi trường–replay–hai mạng | Kể được hướng đi của dữ liệu và gradient | Gộp với vấn đề bằng sơ đồ. |
| Ví dụ | `L08-12` | Một chuyển tiếp có $Z$, $U$ và API tự reset | Phân biệt final observation, reset và mask bootstrap | Dùng một schema kiểm được thay cho ví dụ số mới. |
| Hình thức / thuật toán | `L08-17`–`L08-19` | Loss batch, $N_{\mathrm{start}}$, $F$, $C$, $t$, $k_{\mathrm{opt}}$ | Truy dấu chọn, lưu, warmup, update, sync sau update và dừng | Giả mã tách hai trang để giữ cỡ chữ ít nhất 0,77 em. |
| Ứng dụng | `L08-20`, `L08-31` | Batch và giao diện mạng | Áp dụng vòng vào ảnh Atari và hành động rời rạc | `L08-20` đặt trước kiểm tra số theo yêu cầu sư phạm. |
| Kiểm tra | `L08-21`, `X02`, `L08-34` | Dấu gradient, mask, detach và sáu điều kiện | Phát hiện được cài đặt sai nghĩa DQN | Ba mức: số, code, danh sách kiểm. |

Dữ kiện truyền xuyên cụm: $Z$ che bootstrap theo MDP đang mô hình hóa; $U$ điều khiển reset; $O_{t+1}$ là final observation nếu autoreset; $t$ đếm bước môi trường; $k_{\mathrm{opt}}$ tăng sau update rồi mới kiểm tra chu kỳ $C$.

### 5. Bất ổn, mạng mục tiêu và bộ ba nguy hiểm

| bước | mã trang | kiến thức hoặc dữ kiện đầu vào | sản phẩm học tập | gộp / không áp dụng |
|---|---|---|---|---|
| Vấn đề | `L08-07`, `L08-27` | Một mạng vừa đổi dự đoán vừa đổi đích; dữ liệu phụ thuộc hành vi | Thấy phản ví dụ trước mạng mục tiêu và nối hai biểu hiện với deadly triad | `L08-07` đặt nguyên nhân sớm; `L08-27` quay lại ánh xạ cấu trúc. |
| Trực giác | `L08-28` | Các quan sát gần nhau và chính sách thay đổi | Giải thích cỡ mẫu hiệu dụng và giới hạn replay | Không gộp. |
| Ví dụ | `L08-29` | Một chuyển tiếp cố định qua mốc đồng bộ | Chỉ ra đích có thể đổi dù dữ liệu không đổi | Gộp với hình thức bằng hiệu $y_i^{\mathrm{new}}-y_i^{\mathrm{old}}$. |
| Hình thức / thuật toán | `L08-29`–`L08-30` | $\theta^-\leftarrow\theta$, xấp xỉ hàm, bootstrap, khác chính sách | Nêu đúng quan hệ nhân quả và phạm vi deadly triad | `L08-29` gộp ví dụ–hình thức; `L08-30` tổng quát hóa. |
| Ứng dụng | `X03` | Hai cơ chế replay và mạng mục tiêu | Thiết kế phép loại bỏ đúng một thành phần | Gộp với kiểm tra vì sản phẩm là một thiết kế thí nghiệm. |
| Kiểm tra | `X03`, `L08-33` | Thước đo và nhiều lần chạy độc lập | Phân biệt dự đoán cơ chế với kết luận thực nghiệm | Không yêu cầu một số seed cố định; phải nêu cách tổng hợp độ phân tán. |

Dữ kiện truyền xuyên cụm: cùng chuyển tiếp batch ở `L08-29` giữ nguyên $(O_i,A_i,R_i,O'_i,Z_i,U_i)$; chỉ tham số tạo phần bootstrap đổi tại mốc đồng bộ.

### Chu trình rút gọn: bộ tối ưu

Optimizer không phải khái niệm trọng tâm của DQN trong bài này. `L08-22` nêu vai trò, miền siêu tham số và giới hạn; tuyến ngang đi sang `L08-26`. `L08-23`–`L08-25` là nhánh dọc 10 phút cho ba quy tắc. Bước “ví dụ tính số” và “kiểm tra riêng” ghi `không áp dụng`: nguồn không có ví dụ optimizer, còn việc thêm một bài tính mới sẽ lấy thời gian khỏi replay, mạng mục tiêu và loss.

## Bản đồ truyền dữ kiện

- Chuyển tiếp $(O_t,A_t,R_{t+1},O_{t+1},Z_{t+1},U_{t+1})$ được định nghĩa ở `L08-12`; $O_{t+1}$ lấy từ final observation trước autoreset. Khi lấy batch, đổi tên thành $(O_i,A_i,R_i,O'_i,Z_i,U_i)$, $i=1,\ldots,b$, ở `L08-10`, `L08-17`, `L08-19`, `L08-20` và `L08-29`.
- $b,N_{\mathrm{start}},N,F,C,t,k_{\mathrm{opt}}$ đi từ miền khai báo ở `L08-13`, `L08-16`, `L08-18` vào điều kiện tối ưu và đồng bộ ở `L08-19`.
- Giao diện $\mathbf q_\theta(O)\in\mathbb R^{|\mathcal A|}$ ở `L08-07` đi vào `gather` ở `L08-19`–`L08-20` và pipeline Atari ở `L08-31`.
- Ví dụ hai mẫu ở `X01` được tóm lại ở `L08-21`; cùng dấu sai số được dùng để kiểm hướng gradient.
- Replay và mạng mục tiêu được tách ở `L08-13`–`L08-16`, hợp nhất trong công thức `L08-17`, rồi quay lại như hai cơ chế ở `L08-27`–`L08-30`.

## Từng trang chiếu

| mã | luận điểm trung tâm | bước học tập | câu nối / lý do |
|---|---|---|---|
| `L08-01` | DQN thay bảng Q bằng mạng sâu. | mở vấn đề | Nối từ Bài 07. |
| `L08-02` | Bốn sản phẩm học tập kiểm chứng được. | định hướng | Chuyển sang giới hạn của bảng. |
| `L08-03` | Tham số chung tạo khái quát và giao thoa. | vấn đề, trực giác | Chuẩn bị cập nhật Q. |
| `L08-04` | Q-learning dạng bảng khai báo mặt nạ, $\alpha_t>0$ và điều kiện biên của $\gamma$. | hình thức | Xác định đích và miền trước chính sách. |
| `L08-05` | Hành vi khám phá khác phép tối ưu Bellman; phép cực đại không cần importance sampling. | hình thức, giới hạn | Nêu nguồn lệch hành vi thứ nhất. |
| `L08-06` | Cận mẫu cần thiết lập, không chỉ chiều biểu diễn. | giới hạn | Dẫn sang giao diện mạng thay vì định lý thiếu giả thiết. |
| `L08-07` | Phản ví dụ một mạng đặt mục tiêu di động trước giải pháp hai mạng. | vấn đề, hình thức | Khởi tạo $\theta^-\leftarrow\theta$ sau khi nguyên nhân đã rõ. |
| `L08-08` | Bootstrap tạo nhãn hồi quy tạm thời từ mạng mục tiêu cố định theo đoạn. | trực giác | Dẫn tới ca kết thúc. |
| `L08-09` | Kết thúc thật loại nhánh bootstrap. | ví dụ | Chuẩn bị mặt nạ trong loss. |
| `L08-10` | Gather chọn hành động lưu; MSE chỉ truyền gradient qua mạng online. | hình thức | Dẫn tới bài tính. |
| `X01` | Tính target, TD error, MSE và gradient. | kiểm tra | Hoàn tất cụm đích DQN. |
| `L08-11` | Huấn luyện xen kẽ tương tác và tối ưu. | trực giác | Mở cụm thuật toán. |
| `L08-12` | Kết thúc, cắt ngắn và autoreset có nghĩa khác nhau. | hình thức | Chốt schema và final observation trước khi lưu. |
| `L08-13` | Replay có dung lượng, batch và hai nguồn lệch hành vi. | cơ chế | Dẫn tới giới hạn. |
| `L08-14` | Replay không tạo mẫu i.i.d. | giới hạn | Chuyển sang mạng mục tiêu. |
| `L08-15` | Đường dự đoán và đường tạo đích không nhận cùng gradient. | cơ chế | Nối hai mạng đã giới thiệu với lịch đồng bộ. |
| `L08-16` | Đồng bộ dùng $k_{\mathrm{opt}}$ sau bước cập nhật. | hình thức | Hợp nhất thành loss. |
| `L08-17` | Công thức đầy đủ dùng $(O_i,A_i,R_i,O'_i,Z_i,U_i)$, $i=1,\ldots,b$. | hình thức | Chuẩn bị giả mã. |
| `L08-18` | Thu thập lưu final observation; khai báo warmup và tần suất. | thuật toán | Chuyển sang tối ưu. |
| `L08-19` | Tối ưu sau warmup theo $F$; đồng bộ sau update theo $C$. | thuật toán | Chuyển sang tensor. |
| `L08-20` | Batch Atari truy đủ hai mạng, gather, max, cờ, dtype và thiết bị. | ứng dụng | Đặt hợp đồng tensor trước kiểm tra số. |
| `L08-21` | Dấu gradient khớp sai số của hai mẫu. | kiểm tra | Dẫn tới sửa giả mã. |
| `X02` | Sửa final observation, mask MDP, dừng gradient và gather. | kiểm tra | Hoàn tất cụm thuật toán. |
| `L08-22` | Optimizer chỉ biến gradient thành bước tham số; miền siêu tham số được khai báo. | vấn đề phụ | Trang ngang cốt lõi; đi xuống để xem chi tiết. |
| `L08-23` | SGD dùng gradient hiện tại. | hình thức phụ | Nhánh dọc linh hoạt. |
| `L08-24` | RMSprop chuẩn hóa theo moment bậc hai. | hình thức phụ | Phần linh hoạt. |
| `L08-25` | Adam kết hợp moment bậc nhất và bậc hai. | hình thức phụ | Phần linh hoạt; đã sửa dấu `\quad`. |
| `L08-26` | Chọn optimizer bằng thí nghiệm có kiểm soát. | ứng dụng, giới hạn | Trang ngang tiếp theo; quay lại bất ổn cấu trúc. |
| `L08-27` | Hai biểu hiện bất ổn được ánh xạ vào deadly triad. | vấn đề | Tách nguyên nhân khỏi biện pháp giảm nhẹ. |
| `L08-28` | Tương quan làm giảm thông tin mới trong batch. | trực giác | Nối lại replay. |
| `L08-29` | Mạng mục tiêu làm chậm, không tạo ra, mục tiêu di động. | ví dụ, hình thức | Nối đúng quan hệ nhân quả với đồng bộ. |
| `L08-30` | DQN vẫn chứa deadly triad. | giới hạn | Chuyển sang ứng dụng Atari. |
| `L08-31` | Atari có giao diện quan sát–hành động–phần thưởng tối thiểu, không phải đặc tả tái lập. | ứng dụng | Kiểm tra giả thiết Markov. |
| `L08-32` | Bốn khung không bảo đảm Markov. | kiểm tra | Chuẩn bị tổng hợp. |
| `L08-33` | Bốn câu phân biệt cơ chế và phạm vi. | kiểm tra | Dẫn tới bài phân tích loại bỏ. |
| `X03` | Thí nghiệm loại bỏ đổi đúng một thành phần và dùng cùng kế hoạch chạy cho mọi nhánh. | ứng dụng, kiểm tra | Không áp đặt một số seed cụ thể khi chưa có ngân sách. |
| `L08-34` | Sáu điều kiện tạo hợp đồng DQN đúng nghĩa. | tổng hợp | Kết thúc bằng danh sách kiểm. |
