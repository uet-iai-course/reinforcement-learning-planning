# Storyboard Bài 04

## Hành trình khái niệm

| Cụm | Vấn đề | Trực giác | Ví dụ | Hình thức | Ứng dụng | Kiểm tra | Đầu vào → sản phẩm | Phút |
|---|---|---|---|---|---|---|---|---:|
| Định hướng | P01 | P01 | không áp dụng: đặt phạm vi | P02 | P01 | P02 | Bài 03 → miền DP và chuẩn | 7 |
| Bellman tối ưu và $q_*$ | A02 | A02 | A02,A08 | A08,A00,A01,A03,A09 | A05–A06 | A02,A09 | phép tính tất định → $q_*,v_*,T^\pi,T_*$, greedy | 25 |
| Lặp chính sách | B00 | B00–B03 | B00–B03 | B04–B06,B08 | B03,B06 | B06 | MDP hai trạng thái → PI chính xác | 27 |
| Lặp giá trị | C00 | C01–C02 | C00–C02 | C03–C09 | C05–C07 | C05 | Gridworld → VI, phần dư, chi phí | 31 |
| Hội tụ, giới hạn, quyết định | D00 | D00–D02 | dùng lại A02, B00 và C00 | D01–D07 | D05,D08 | D05 | tính co → tồn tại → chặn dừng → phạm vi dùng | 30 |

Tổng tuyến chính: $7+25+27+31+30=120$ phút. Thời lượng này gồm các câu hỏi ngắn ở P02, B06, C05 và D05. Nhánh bài tập: X09 12 phút, X06 10 phút, X04 8 phút; X07 tự luyện.

## Truyền dữ kiện và câu nối

- P02 định nghĩa $\mathcal V$ và $\lVert\cdot\rVert_\infty$ trước A01, A03 và D01–D07.
- A02 cố định bối cảnh tất định: thưởng $2/0$, trạng thái kế tiếp $s_1/s_2$, $\gamma=0{,}9$, giá trị tiếp tục tối ưu $5/8$. A08 ép hành động đầu bằng $a\triangleright\pi$, tránh điều kiện hóa trên biến cố xác suất không; A00 dùng $v_*=\max_aq_*$.
- A01 chỉ áp dụng $T^\pi$ cho chính sách Markov dừng. D03 xử lý mọi $\pi\in\Pi$ bằng chặn chân trời hữu hạn; D06 mới dựng chính sách Markov dừng đạt cận.
- B00–B03 giữ cùng MDP và $\gamma=0{,}9$: $(10,11)\to(10,30)\to(27,30)$. B03 tính $q_{\pi_1}(s_0,b)=27$ trước khi đổi sang $\pi_2$.
- B04 dùng $\varepsilon_{\mathrm{step}}$ và trả $v_{j+1}$, nên chặn có hệ số $\gamma/(1-\gamma)$. B06–B08 chỉ nói PI chính xác; biến thể sửa đổi được bỏ khỏi tuyến chính.
- C00 nêu rõ $\gamma=0{,}9$. C04 thực hiện một lượt và tính $\Delta$; C09 tính $w=T_*v$ để kiểm phần dư. Nếu chưa dừng, $w$ trở thành bảng kế tiếp, không tính lại lượt quét.
- D04 suy $e\le\rho+\gamma e$; D07 dùng $T^{\pi_v}v=T_*v$ để suy chặn mất mát. Hai bước giải thích ngưỡng ở C09.
- D05 hợp nhất kiểm tra đầu vào tổng quát với CartPole. D08 nối $q_*$ sang điều khiển dựa trên giá trị hành động khi không biết mô hình.

## Từng trang

| Mã | Luận điểm trung tâm | Câu nối |
|---|---|---|
| P00 | Bài toán là giải MDP có mô hình. | Tách đầu vào và đầu ra. |
| P01 | DP tính kỳ vọng từ mô hình đã biết. | Chốt miền toán học. |
| P02 | Mọi toán tử cùng miền $\mathcal V$ và chuẩn vô cùng. | Bắt đầu bằng lựa chọn số. |
| A02 | Micro-example nêu rõ thưởng, trạng thái kế tiếp và tiếp diễn tối ưu. | Đặt tên giá trị hành động. |
| A08 | $q_*$ ép hành động đầu rồi tối ưu chính sách tiếp diễn. | Lấy cực đại để được $v_*$. |
| A00 | $v_*=\sup_\pi v_\pi=\max_aq_*$. | So với đánh giá chính sách cố định. |
| A01 | $T^\pi:\mathcal V\to\mathcal V$ cho chính sách Markov dừng. | Thay trung bình hành động bằng cực đại. |
| A03 | $T_*:\mathcal V\to\mathcal V$ sao lưu hành động tốt nhất. | Viết trực tiếp cho $q_*$. |
| A09 | Bellman $q_*$; câu hỏi giải thích cực đại ở trạng thái kế tiếp; dựng ứng viên tham lam. | Tổ chức các phép toán. |
| A05 | Quy hoạch động luân phiên đánh giá và cải thiện. | Tách PI khỏi VI. |
| A06 | PI và VI ghép ba phép toán khác nhau. | Theo dõi PI trên ví dụ. |
| B00 | MDP hai trạng thái cố định dữ kiện. | Đánh giá $\pi_0$. |
| B01 | $v_{\pi_0}=(10,11)$. | Cải thiện trên cùng bảng. |
| B02 | Cải thiện được $\pi_1=(a,b)$. | Đánh giá và giải thích vòng kế. |
| B03 | $q_{\pi_1}(s_0,b)=27$ dẫn tới $\pi_2=(b,b)$. | Khái quát đánh giá lặp. |
| B04 | Ngưỡng bước có chặn sai số đúng cho giá trị trả về. | So sánh lịch cập nhật. |
| B05 | Đánh giá bất đồng bộ cố định $\pi$ cần công bằng. | Đóng gói PI chính xác. |
| B06 | PI chính xác có đầu vào, phá hòa, dừng và chi phí. | Chứng minh bảo đảm. |
| B08 | Đơn điệu, co và tính hữu hạn cho PI chính xác. | Sang VI trên Gridworld. |
| C00 | Gridworld đủ mô hình và ghi rõ $\gamma=0{,}9$. | Thực hiện lượt đầu. |
| C01 | $v_1$ cho thấy tầm nhìn một bước. | Theo dõi lan truyền. |
| C02 | Giá trị lan ngược sau bốn lượt. | Khái quát VI. |
| C03 | VI lặp trực tiếp $T_*$. | Tách một lượt cập nhật. |
| C04 | Một lượt dùng $v_{\mathrm{old}}$ và có chi phí $C_{\mathrm{model}}$. | Kiểm phần dư tại bảng mới. |
| C09 | Lượt $T_*v$ vừa kiểm phần dư vừa được tái sử dụng nếu chưa dừng. | Trích chính sách từ cùng bảng. |
| C05 | $T^{\pi_v}v=T_*v$ đòi hỏi cùng $v$. | So sánh chi phí. |
| C06 | Chi phí phân biệt lượt đầu và các lượt kiểm được tái sử dụng. | Xét lịch bất đồng bộ. |
| C07 | VI bất đồng bộ dùng $T_*$ và cần công bằng. | Đặt lộ trình chứng minh. |
| C08 | Chứng minh đi từ co tới mất mát chính sách. | Bắt đầu với bất đẳng thức max. |
| D00 | Ba câu hỏi hội tụ cần một công cụ chung. | Xử lý cực đại. |
| D01 | Bất đẳng thức max chặn sai khác từng trạng thái. | Lấy chuẩn. |
| D02 | $T_*$ co nên có điểm bất động duy nhất. | Chặn mọi chính sách. |
| D03 | Chân trời hữu hạn và đuôi chiết khấu cho $v_\pi\le\bar v$. | Dựng chính sách đạt cận. |
| D06 | Chính sách tham lam theo $\bar v$ đạt đúng $\bar v=v_*$. | Quay lại phần dư. |
| D04 | Phần dư chặn sai số giá trị bằng phép suy diễn một dòng. | Chặn mất mát. |
| D07 | Greedy identity chuyển sai số thành mất mát chính sách. | Kiểm phạm vi với CartPole. |
| D05 | CartPole rời rạc vẫn thiếu hạt nhân. | Tổng kết cách chọn công cụ. |
| D08 | Bảng quyết định nối DP với điều khiển phi mô hình. | Chuyển sang bài tập. |
| X09 | Dữ kiện MDP đầy đủ; tính $V_1$, rồi sáu $Q_{V_1}$ để trích greedy. | Sang chứng minh ma trận. |
| X06 | Chứng minh đánh giá dạng ma trận. | Sang lịch cập nhật. |
| X04 | Phân tích đồng bộ và bất đồng bộ. | Sang tính đơn điệu. |
| X07 | Chứng minh tính đơn điệu. | Kết thúc. |

## Rà lân cận sau thay đổi

- Đã rà P00–A01 sau khi chuyển A02 lên trước hình thức: giả thiết và chuẩn có trước micro-example; A08, A00 mới đặt tên $q_*,v_*$; A01 mới dùng toán tử.
- Đã rà A02–A05 sau khi thêm A08/A09 và bỏ A04 cũ: không còn trang tính chất lặp; $q_*$ đi từ ví dụ → định nghĩa → Bellman → greedy.
- Đã rà P02–A00 sau khi làm chặt A08: $\Pi$ được định nghĩa trước; ký hiệu ép hành động đầu không phụ thuộc xác suất hành động của chính sách tiếp diễn; A09 chỉ gọi $\bar\pi$ là ứng viên.
- Đã rà B02–B05 sau khi thêm $q_{\pi_1}(s_0,b)=27$: dữ kiện $v_{\pi_1}$ xuất hiện cùng trang trước khi tính $q$; B04 không phụ thuộc ngược.
- Đã rà B05–C01 sau khi bỏ B07 sửa đổi: B06→B08 giữ thuật toán chính xác và bảo đảm liền nhau; C00 mở ví dụ VI.
- Đã rà C02–C07 sau khi tách C04/C09: lượt cập nhật, lượt residual, greedy và bảng chi phí dùng nhãn nhất quán; không dùng kết quả D04–D07 trước khi chứng minh, chỉ xem trước.
- Đã rà C04–C07 sau sửa tái sử dụng: khi chưa dừng, $v\leftarrow w$; C06 không còn tính hai lần cùng một lượt $T_*v$.
- Đã rà D01–D08 sau khi tách D03/D04: cận trên và đạt cận tách riêng; residual→value và value→policy tách riêng; CartPole và trang quyết định đứng sau toàn bộ bảo đảm.
