# Ghi chú cho người soạn Bài 08

Tệp này giữ các chỉ dẫn biên tập không đưa lên mặt trang chiếu hoặc vào ghi chú diễn giả.

## Các quyết định phải giữ

- Không đưa hai cận độ phức tạp mẫu ở trang nguồn 9 và 11 trở lại phần chính. Chúng thiếu mô hình lấy mẫu, chuẩn sai số, xác suất thành công, điều kiện bao phủ và thuật toán cụ thể.
- Dùng $(O_t,A_t,R_{t+1},O_{t+1},Z_{t+1},U_{t+1})$ cho dòng thời gian tương tác. Sau khi lấy batch, đổi sang đúng một quy ước $(O_i,A_i,R_i,O'_i,Z_i,U_i)$, $i=1,\ldots,b$; không dùng $R_{i+1}$ hoặc $O_{i+1}$ trong công thức batch.
- $Z$ phải biểu diễn kết thúc của MDP đang mô hình hóa; $U$ là cắt ngắn ngoài mô hình. Với nhiệm vụ tiếp diễn bị giới hạn thu thập, reset khi $Z\lor U$ nhưng chỉ dùng $1-Z$ trong mục tiêu bootstrap.
- Với API tự reset, lưu `final_observation` hoặc `terminal_observation` làm $O_{t+1}$ trước khi dùng quan sát đầu của episode mới. Bài `X02` giả sử `final_observation` đúng là quan sát cuối của chuyển tiếp.
- Mục tiêu phải được dừng gradient bằng `detach` hoặc `no_grad`. Gradient chỉ đi qua phần tử $Q_\theta(O_i,A_i)$ đã được gather theo hành động lưu trong replay.
- DQN cơ bản nhận quan sát hoặc biểu diễn trạng thái và xuất vector cho tập hành động rời rạc hữu hạn.
- Giới thiệu mạng online $Q_\theta$, mạng mục tiêu $Q_{\theta^-}$ và phép khởi tạo $\theta^-\leftarrow\theta$ trước khi dùng $\theta^-$ trong công thức bootstrap.
- Replay giảm tương quan ngắn hạn; không tạo dữ liệu độc lập và cùng phân phối (i.i.d.) và không bảo đảm hội tụ.
- Có hai nguồn lệch hành vi: $\epsilon$-greedy khác phép cực đại Bellman, và replay chứa dữ liệu từ các phiên bản hành vi cũ. DQN cơ bản không dùng importance sampling vì đích là phép sao lưu tối ưu, không phải kỳ vọng hành động theo một chính sách đích ngẫu nhiên.
- Mạng mục tiêu giữ cố định trong $C$ bước tối ưu rồi sao chép cứng; cơ chế này không bảo đảm hội tụ.
- Dùng sai số bình phương trung bình (MSE) như lựa chọn của bài để thống nhất phép tính. Nếu nhắc Huber, chỉ nói đây là lựa chọn thực hành khác; không gán lựa chọn MSE cho một đặc tả bắt buộc của DQN.
- Với Atari, nói “bốn khung quan sát liên tiếp” hoặc “xấp xỉ trạng thái”; không khẳng định tính Markov.
- Pipeline Atari chỉ mô tả giao diện tối thiểu gồm quan sát, hành động rời rạc và phần thưởng vô hướng. Không gọi đây là đặc tả tái lập; nguồn thiếu nhiều chi tiết tiền xử lý và giao thức thực nghiệm.

## Quy ước ký hiệu

- $\epsilon_{\mathrm{exp}}$: khám phá.
- $\epsilon_{\mathrm{opt}}$: ổn định số của RMSprop/Adam.
- Nếu sau này thảo luận độ chính xác định lý, dùng $\varepsilon_{\mathrm{acc}}$; không dùng cùng một epsilon cho ba vai trò.
- Adam dùng $\sqrt{\hat v_t}+\epsilon_{\mathrm{opt}}$, không đặt epsilon bên trong căn.
- Mọi phép bình phương, căn và chia trong RMSprop/Adam thực hiện theo từng tọa độ.
- $t$ đếm bước môi trường; $k_{\mathrm{opt}}$ đếm bước tối ưu; $j$ chỉ dùng trong công thức optimizer. Không trộn ba chỉ số.
- $b,N_{\mathrm{start}},N,F,C\in\mathbb N_+$ với $b\le N_{\mathrm{start}}\le N$. Tối ưu khi đủ warmup và $t\bmod F=0$; sau cập nhật mới tăng $k_{\mathrm{opt}}$ và kiểm tra đồng bộ.
- Dùng $\gamma<1$ cho nhiệm vụ tiếp diễn. Chỉ dùng $\gamma=1$ khi episode kết thúc thích hợp và return hữu hạn.
- Ở cầu nối Q-learning dạng bảng, khai báo $\alpha_t>0$. Chỉ nói hội tụ khi dãy bước thỏa Robbins–Monro theo từng cặp trạng thái–hành động và đủ các giả thiết thăm.

## Nhịp giảng

- Giữ ví dụ terminal ở trước stop-gradient. Người học phải hiểu đích trước khi lấy gradient.
- Tách hai luồng của vòng DQN: thu thập chuyển tiếp và tối ưu từ replay.
- Dạy schema chuyển tiếp trước replay và giả mã; không để cờ kết thúc xuất hiện lần đầu trong code.
- Đặt phản ví dụ một mạng vừa đổi dự đoán vừa đổi đích trước khi giới thiệu online/target. Sau đó khởi tạo $\theta^-\leftarrow\theta$; sau replay, nhắc lại hai đường tính và đồng bộ trước loss hoàn chỉnh.
- Truy dấu giả mã qua đủ chọn hành động, lưu, lấy batch, target, update, sync và dừng.
- Phần optimizer là khái niệm phụ. Không kéo dài thành so sánh bộ tối ưu trong học sâu nói chung.
- Trang tổng quan optimizer và bảng so sánh nằm trên tuyến ngang. SGD, RMSprop và Adam nằm theo chiều dọc dưới trang tổng quan; không ép người giảng đi qua ba trang này khi thiếu thời gian.
- Đặt deadly triad sau hai cơ chế trực tiếp. Khi nói mục tiêu di động, nêu đúng nguyên nhân là bootstrap từ ước lượng đang học; mạng mục tiêu chỉ làm chậm vòng phản hồi này.
- Tuyến chính có 110 phút. Ba trang optimizer chi tiết `L08-23`–`L08-25` tạo phần linh hoạt 10 phút; rút gọn phần này trước khi cắt replay, target network hoặc loss.

## Bài tập và đáp số

- Bài mini-batch: $y=(4{,}6,-2)$; $\delta=(1{,}5,-0{,}5)$; MSE $=1{,}25$; gradient theo $(q_1,q_2)$ là $(-1{,}5,0{,}5)$.
- Bài sửa giả mã phải giữ bốn sửa đổi độc lập: lấy final observation trước autoreset, mask theo kết thúc của MDP đang mô hình hóa, `no_grad` hoặc `detach` cho đích, và gather một hành động lưu trên mỗi hàng.
- Bài ablation không yêu cầu viết code. Giữ kiến trúc, ngân sách, optimizer và lịch khám phá; đổi đúng một thành phần; đo return đánh giá, TD error, chuẩn gradient và độ phân tán qua nhiều lần chạy độc lập. Không ấn định một số seed cụ thể nếu chưa có ngân sách thí nghiệm.

## Code demo và nguồn ngoài

Nguồn không có code demo nên không tự tạo notebook hoặc chương trình. Nếu sau này thêm demo, phải ghi rõ semantics của API cho `terminated`, `truncated`, autoreset và final observation. Nếu thêm chi tiết Atari ngoài nguồn, phải trích nguồn cụ thể; không thêm tuyên bố thành tích hoặc reward clipping khi chưa có nguồn và thời lượng.

## Nội dung để dành cho bài sau

- DQN dùng cùng phép cực đại để chọn và đánh giá hành động kế tiếp nên có thể đánh giá quá cao do nhiễu. Chỉ đưa overestimation và Double DQN lên slide khi bài sau hoặc nguồn bổ sung cho phép; không chen vào mạch hiện tại.

## Kiểm tra biên tập

- Không đưa mã trang, thời lượng, nhãn tuyến hoặc chỉ dẫn cho người soạn vào slide hay notes.
- Không dùng “replay phá vỡ tương quan”, “target network bảo đảm ổn định”, “Adam hội tụ nhanh” hoặc “bốn khung là trạng thái Markov”.
- Khi sửa loss, tính lại ví dụ batch và kiểm dấu gradient.
- Khi sửa schema, cập nhật đồng thời replay, công thức, giả mã, tensor và bài sửa code; phân biệt chỉ số thời gian $t$ với chỉ số batch $i$.
- Rà câu chữ theo `no-ai-slop/eval.md`; giữ thuật ngữ và trật tự khái niệm nhất quán theo mạch Quill, không tạo `quill.json`.
