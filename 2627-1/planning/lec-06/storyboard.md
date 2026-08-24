# Storyboard Bài 06

## Hành trình khái niệm

| Cụm | Vấn đề | Trực giác | Ví dụ | Hình thức | Thuật toán | Ứng dụng | Kiểm tra | Hội tụ | Phút |
|---|---|---|---|---|---|---|---|---|---:|
| Định hướng | P01 | P00,P03 | không áp dụng: đặt phạm vi | P02 | không áp dụng | P03 | P03 | không áp dụng | 10 |
| Chính sách và lượt chung | A00 | A00–A01,A02 | A03–A04 | A01–A02 | không áp dụng | A03–A04 | A04 | không áp dụng | 20 |
| MC control | B00 | B00 | B00,B03–B04 | B05 | B01–B02 | B03–B04 | B04 | B06 | 23 |
| SARSA | C00 | C00 | C00 | C01 | C02 | C03 | C04 | C05 | 23 |
| Q-learning cốt lõi | D00 | D00 | D00 | D01 | D02 | D03 | D04 | D05 | 24 |
| Tổng hợp cốt lõi | E00 | E00–E01 | không áp dụng: tổng hợp | E00–E01 | không áp dụng | E03 | không áp dụng: trang tổng hợp | không áp dụng | 10 |
| Linh hoạt: dự đoán khác chính sách | D06 | D06 | D07 | D06–D07 | không áp dụng: nhánh mở rộng | D07 | không áp dụng | không áp dụng | 5 |
| Linh hoạt: chặn Hoeffding | E02 | E02 | không áp dụng: chặn tổng quát | E02 | không áp dụng | không áp dụng | không áp dụng | không áp dụng | 5 |

Tuyến cốt lõi là 110 phút và không gồm D06, D07 hoặc E02. D06–D07 là một nhánh mở rộng 5 phút về đánh giá khác chính sách; E02 là nhánh linh hoạt 5 phút về chặn Hoeffding. Tổng phần trình chiếu là 120 phút. X01–X03 dùng 5, 10 và 15 phút, tổng 30 phút.

## Truyền dữ kiện và giả thiết

- P02 định nghĩa $\mathcal X$, $\mathcal X_{\mathrm{reach}}$ và $A_{\max}$; đồng thời nêu MC cần lượt kết thúc gần chắc chắn và return hữu hạn. Điều kiện này không suy ra từ hình chuỗi.
- A03 cố định $Q_0(B)=(0,1)$, $Q_0(C)=(1,0)$, $Q_0(D)=(1,0)$; hành động 0 là trái, 1 là phải.
- A04 dùng dãy $u_t=0{,}8,0{,}6,0{,}2,0{,}4$ với $\varepsilon=0{,}25$: $u_t\le\varepsilon$ mở cổng thăm dò; số kế chọn hành động 0 khi không quá $0{,}5$. Quy tắc chỉ cố định lượt $(D,0)\to(C,0)\to(B,0)\to A$; không phải bộ lấy mẫu đúng của chính sách $\varepsilon$-tham lam.
- B00 truyền các phần thưởng tích lũy $998,999,1000$ vào B03–B04. B03 dùng trung bình mẫu; B04 dùng $\alpha=0{,}8$.
- B05 nối một bảng $Q$ còn nhiễu với định lý chỉ dùng $q_\pi$ chính xác. B06 ghép GLIE với điều kiện kết thúc, return bị chặn và trung bình mẫu hoặc bước Robbins–Monro; kết luận chỉ trên $\mathcal X_{\mathrm{reach}}$.
- C00 dùng ngay chuyển $(C,0)\to B$ và hành động kế tiếp $A'=0$ trước khi C01 đưa công thức SARSA. C03 áp dụng toàn lượt; C04 đổi đúng một hành động để kiểm tra cơ chế.
- D00 giữ cùng chuyển nhưng đổi mục tiêu sang hành động tham lam trước công thức D01. D03 áp dụng toàn lượt; D04 so trực tiếp với SARSA.
- C02 và D02 dùng $k$ cho lượt, $t$ cho chuyển và $N(s,a)$ cho số lần cập nhật riêng của cặp; bước học là $\alpha_{N(s,a)}(s,a)$.
- D05 kết thúc mạch Q-learning trên $\mathcal X_{\mathrm{reach}}$. D06–D07 mới mở rộng sang điều kiện hỗ trợ và TD(0) giá trị trạng thái khác chính sách, rồi nối về E00.
- Chính sách tham lam ban đầu có thể lặp B–C. Lượt mẫu dài ba bước không chứng minh mọi lượt đều kết thúc.

## Từng trang

| Mã | Luận điểm trung tâm | Câu nối |
|---|---|---|
| P00 | Điều khiển phi mô hình học chính sách từ trải nghiệm. | Phân biệt với dự đoán. |
| P01 | Điều khiển làm chính sách thay đổi. | Chốt miền và giả thiết. |
| P02 | MC cần kết thúc gần chắc chắn; mọi đại lượng có vai trò rõ. | Xem vòng học. |
| P03 | Chính sách, trải nghiệm và $Q$ tạo vòng phản hồi. | Cần chính sách từ $Q$. |
| A00 | $Q$ cho phép so sánh hành động. | Thêm thăm dò. |
| A01 | $\varepsilon$-tham lam có xác suất xác định. | Phân biệt hành vi và đích. |
| A02 | Theo/khác chính sách phụ thuộc quan hệ $\mu$–$\pi$. | Cố định ví dụ. |
| A03 | Một chuỗi và một bảng $Q_0$ dùng xuyên bài. | Cố định một lượt. |
| A04 | Quy tắc số chỉ tái tạo lượt, không mô phỏng phân phối. | Tính phần thưởng tích lũy. |
| B00 | MC dùng ba phần thưởng tích lũy của lượt hoàn chỉnh. | Viết giao diện. |
| B01 | MC nêu rõ kết thúc, return, đầu vào, đầu ra và dừng. | Đặt cập nhật vào vòng lượt. |
| B02 | MC lần ghé đầu cập nhật sau trạng thái kết thúc. | Chạy trung bình mẫu. |
| B03 | Mẫu đầu thay giá trị khởi tạo khi dùng $1/N$. | Đổi riêng bước học. |
| B04 | $\alpha=0{,}8$ giữ $20\%$ giá trị cũ. | Giải thích cải thiện. |
| B05 | Cải thiện trong lớp $\varepsilon$-mềm cần giả thiết đúng. | Nêu điều kiện dài hạn. |
| B06 | GLIE gồm thăm dò vô hạn và tham lam ở giới hạn; MC còn cần lượt hữu hạn. | Sang cập nhật một bước. |
| C00 | Hành động kế tiếp thật sự tại B phải đi vào đích SARSA. | Viết công thức. |
| C01 | Đích SARSA dùng $A_{t+1}$ do hành vi chọn. | Đặt vào thuật toán. |
| C02 | SARSA có vòng ngoài theo lượt, reset, chọn $A_0$, nhánh kết thúc, dừng và chi phí. | Chạy toàn lượt. |
| C03 | SARSA cho $0{,}2;-0{,}6;800$ ở ba ô. | Đổi một hành động. |
| C04 | Đổi hành động tại B làm đích ở C đổi. | Gắn với bảo đảm. |
| C05 | Hội tụ SARSA cần GLIE và Robbins–Monro theo từng cặp. | Đổi chính sách đích. |
| D00 | Cùng chuyển có hành động lấy mẫu và hành động tham lam khác nhau. | Viết công thức. |
| D01 | Q-learning dùng cực đại thay hành động kế tiếp. | Đặt vào thuật toán. |
| D02 | Q-learning có vòng ngoài theo lượt, reset, nhánh kết thúc, dừng và chi phí. | Chạy toàn lượt. |
| D03 | Q-learning cho $0{,}2;0{,}2;800$ ở ba ô. | So đích. |
| D04 | SARSA dùng quyết định thăm dò; Q-learning dùng cực đại. | Gắn với bảo đảm. |
| D05 | Hội tụ Q-learning cần độ phủ và Robbins–Monro theo từng cặp. | Mở rộng đánh giá khác chính sách. |
| D06 | Nhánh linh hoạt quay lại dự đoán $V$ và lượng hóa điều kiện hỗ trợ trên các cặp khả đạt. | Nêu cập nhật hiệu chỉnh. |
| D07 | TD(0) giá trị trạng thái dùng tỉ số từng bước, kèm ví dụ $\rho=4$. | Quay lại ba thuật toán chính. |
| E00 | Ba thuật toán khác ở đích, thời điểm và quan hệ chính sách. | Tách chi phí. |
| E01 | Chi phí tính toán không phải độ phức tạp mẫu. | Giới hạn chặn xác suất. |
| E02 | Hoeffding chỉ chặn một trung bình độc lập bị chặn. | Khóa phạm vi. |
| E03 | Bài 07 thay bảng giá trị bằng hàm xấp xỉ và xét lại bảo đảm hội tụ. | Sang bài tập dọc. |
| X01 | Phản biện quy tắc số như một bộ lấy mẫu. | Chữa phân phối và lượt. |
| X02 | Đối chiếu ba bảng và đổi riêng $A_{t+1}$ tại B để tính lại cập nhật ở C. | Chữa cơ chế đích. |
| X03 | Khôi phục miền hữu hạn, thưởng bị chặn, $\gamma<1$; tách GLIE của SARSA khỏi độ phủ và Robbins–Monro mà Q-learning vẫn cần. | Chữa điều kiện. |

## Rà lân cận sau đổi thứ tự

- Đã rà A03–B01: môi trường → quy tắc cố định lượt → return → giả thiết MC; không suy kết thúc từ chuỗi.
- Đã rà B03–B06: hai cập nhật → định lý cải thiện → GLIE và hội tụ; định lý không còn đứng trước ứng dụng.
- Đã rà B06–C02: bảo đảm MC → ví dụ nhỏ SARSA → công thức → thuật toán.
- Đã rà C03–D02: ứng dụng SARSA → kiểm tra → hội tụ → ví dụ nhỏ Q-learning → công thức → thuật toán.
- Đã rà D03–E01: ứng dụng Q-learning → so sánh → hội tụ → mở rộng khác chính sách → tổng hợp.
- E00–E02 là một nhóm ngang riêng. E03 là neo của nhóm dọc E03/X01/X02/X03; RevealJS không còn cấp lồng thứ ba.
