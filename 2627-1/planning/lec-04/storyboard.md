# Storyboard Bài 04

## Hành trình khái niệm

| Cụm | Vấn đề | Trực giác | Ví dụ | Hình thức | Ứng dụng | Kiểm tra | Đầu vào → sản phẩm | Phút |
|---|---|---|---|---|---|---|---|---:|
| Định hướng | P01 | P01 | không áp dụng: đặt phạm vi | P02 | P01 | P02 | Bài 03 → miền DP và chuẩn | 7 |
| Bellman tối ưu và $q_*$ | A02 | A02 | A02,A08 | A08,A00,A01,A03,A09 | A05–A06 | A09 | phép tính tất định → $q_*,v_*,T^\pi,T_*$, greedy | 25 |
| Lặp chính sách | B00 | B00–B03 | B00–B03 | B04–B06,B08 | B03,B06 | B06 | MDP hai trạng thái → PI chính xác | 27 |
| Lặp giá trị | C00 | C01–C02 | C00–C02 | C03–C09 | C05–C07 | C05 | Gridworld → VI, phần dư, chi phí | 31 |
| Hội tụ, giới hạn, quyết định | D00 | D00–D02 | dùng lại A02, B00 và C00 | D01–D07 | D05,D08 | D05 | tính co → tồn tại → chặn dừng → phạm vi dùng | 30 |

Tổng tuyến chính: $7+25+27+31+30=120$ phút. Thời lượng này gồm các câu hỏi ngắn ở P02, B06, C05 và D05. Nhánh bài tập: X09 12 phút, X06 10 phút, X04 8 phút; X07 tự luyện.

## Truyền dữ kiện và câu nối

- P02 định nghĩa $\mathcal V$ và $\lVert\cdot\rVert_\infty$ trước A01, A03 và D01–D07.
- A02 cố định bối cảnh tất định tại $s_0$: $a$ cho $(1,s_0)$, $b$ cho $(0,s_1)$, $\gamma=0{,}9$, giá trị tiếp tục tối ưu $10/11$. A08 dùng hai giá trị hành động $10/9{,}9$ và phép ép hành động đầu $a\triangleright\pi$; A00 lấy cực đại được $v_*(s_0)=10$. Câu hỏi ở A02 đổi phần thưởng của $b$ thành 2 và cho nghiệm tự nhất quán $v_*(s_0)=v_*(s_1)=20$.
- A01 chỉ áp dụng $T^\pi$ cho chính sách Markov dừng. D03 xử lý mọi $\pi\in\Pi$ bằng chặn chân trời hữu hạn; D06 mới dựng chính sách Markov dừng đạt cận.
- B00–B03 giữ cùng MDP và $\gamma=0{,}9$: $(10,11)\to(10,30)\to(27,30)$. B03 tính $q_{\pi_1}(s_0,b)=27$ trước khi đổi sang $\pi_2$.
- B04 dùng $\varepsilon_{\mathrm{step}}$ và trả $v_{j+1}$, nên chặn có hệ số $\gamma/(1-\gamma)$. B06–B08 chỉ nói PI chính xác; biến thể sửa đổi được bỏ khỏi tuyến chính.
- C00 nêu rõ $\gamma=0{,}9$. C04 thực hiện một lượt và tính $\Delta$; C09 tính $w=T_*v$ để kiểm phần dư. Nếu chưa dừng, $w$ trở thành bảng kế tiếp, không tính lại lượt quét.
- D04 suy $e\le\rho+\gamma e$; D07 dùng đẳng thức tham lam $T^{\pi_v}v=T_*v$ để suy chặn mất mát. Hai bước giải thích ngưỡng ở C09.
- D05 hợp nhất kiểm tra đầu vào tổng quát với CartPole. D08 nối $q_*$ sang điều khiển dựa trên giá trị hành động khi không biết mô hình.

## Ánh xạ lecture note sang trang chiếu

| `note-topic-id` | `data-slide-id` |
|---|---|
| `lec-04-topic-01` | P00–P02, A05–A06 |
| `lec-04-topic-02` | A02, A08, A00 |
| `lec-04-topic-03` | A00, A03, A09 |
| `lec-04-topic-04` | P02, A01, A03 |
| `lec-04-topic-05` | B00–B03 |
| `lec-04-topic-06` | B04–B05 |
| `lec-04-topic-07` | B06, B08 |
| `lec-04-topic-08` | C00–C02 |
| `lec-04-topic-09` | C03, C04, C05, C09 |
| `lec-04-topic-10` | B05, C06, C07 |
| `lec-04-topic-11` | C08, D00–D02 |
| `lec-04-topic-12` | D03, D06 |
| `lec-04-topic-13` | C09, D04, D07 |
| `lec-04-topic-14` | D05 |
| `lec-04-topic-15` | D08, X09, X06, X04, X07 |

Mọi trang trong 42 `data-slide-id` có ít nhất một ánh xạ. Một trang có thể nối hai chủ đề khi nó thực hiện cầu chuyển, như P02, A00, A03, B05 và C09.

## Từng trang

| Mã | Luận điểm trung tâm | Câu nối |
|---|---|---|
| P00 | Bài toán là giải MDP có mô hình. | Tách đầu vào và đầu ra. |
| P01 | DP tính kỳ vọng từ mô hình đã biết. | Chốt miền toán học. |
| P02 | Mọi toán tử cùng miền $\mathcal V$ và chuẩn vô cùng. | Bắt đầu bằng lựa chọn số. |
| A02 | Micro-example cho $q_*(s_0,a)=10$, $q_*(s_0,b)=9{,}9$; giá trị tiếp tục $10/11$ nêu ngay đầu; câu hỏi đổi thưởng $b$ thành 2 và fragment chọn $b$ với giá trị tối ưu $20$ ở cả hai trạng thái. | Đặt tên giá trị hành động. |
| A08 | $q_*$ dùng can thiệp $a\triangleright\pi$ buộc hành động đầu (không phải điều kiện hóa theo $\pi$), rồi tối ưu chính sách tiếp diễn; nối lại hai giá trị $10/9{,}9$. | Lấy cực đại để được $v_*$. |
| A00 | $v_*=\sup_\pi v_\pi=\max_aq_*$; trong ví dụ $v_*(s_0)=10$. | So với đánh giá chính sách cố định. |
| A01 | $T^\pi:\mathcal V\to\mathcal V$ cho chính sách Markov dừng; đơn điệu/co chỉ cho lớp này, $\Pi$ đầy đủ xử lý bằng chặn chân trời ở phần bảo đảm. | Thay trung bình hành động bằng cực đại. |
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
| B08 | Đơn điệu, co và $\prod_s|\mathcal A(s)|$ hữu hạn cho PI chính xác. | Sang VI trên Gridworld. |
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
| D01 | Bất đẳng thức max chặn sai khác; kỳ vọng và phép max bảo toàn thứ tự cho tính đơn điệu. | Lấy chuẩn. |
| D02 | $T_*$ co nên có điểm bất động duy nhất; ví dụ sai số đầu 100, $\gamma=0{,}9$ cần 44 lượt để nhỏ hơn 1. | Chặn mọi chính sách. |
| D03 | Chân trời hữu hạn và đuôi chiết khấu cho $v_\pi\le\bar v$. | Dựng chính sách đạt cận. |
| D06 | Chính sách tham lam theo $\bar v$ đạt đúng $\bar v=v_*$. | Quay lại phần dư. |
| D04 | Phần dư chặn sai số giá trị bằng phép suy diễn một dòng. | Chặn mất mát. |
| D07 | Greedy identity chuyển sai số thành mất mát chính sách. | Kiểm phạm vi với CartPole. |
| D05 | CartPole rời rạc vẫn thiếu hạt nhân. | Tổng kết cách chọn công cụ. |
| D08 | Bảng quyết định thu hồi P01 và nối DP với điều khiển phi mô hình; tín hiệu bài tập dọc. | Chuyển sang bài tập. |
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
- Cần rà lại A02±2 và A08–A03 sau đồng bộ micro-example; B06–C00 sau khi thêm công thức đếm ở B08; C08–D03 sau khi thêm đơn điệu và ví dụ 44 lượt ở D01–D02. Số trang, thứ tự và thời lượng không đổi.
