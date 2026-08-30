# Storyboard Bài 05

## Hành trình khái niệm

| Cụm | Vấn đề | Trực giác | Ví dụ | Hình thức | Ứng dụng | Kiểm tra | Đầu vào → sản phẩm | Phút lõi |
|---|---|---|---|---|---|---|---|---:|
| Định hướng | P01 | P00–P01 | không áp dụng: đặt phạm vi | P02 | P01 | P02 | Bài 04 → dự đoán phi mô hình | 7 |
| Monte Carlo | A00 | A00–A01 | A00,A03 | A01–A02 | A03–A05,A07 | A08 | lượt hoàn chỉnh → $G_t$ → thuật toán → ước lượng | 31 |
| TD(0) | B00 | B00,B05 | B00,B03–B04 | B01–B02,B06–B07 | B03–B06 | B08 | chuyển mẫu → cập nhật → kỳ vọng Bellman → hội tụ | 32 |
| So sánh | C00 | C01,C03 | C00–C02 | C03–C04 | C02–C06 | C05,C07 | quỹ đạo dài → cơ chế chệch–phương sai → lựa chọn | 25 |
| Tổng hợp | D00 | D00 | không áp dụng: tổng hợp | D00 | D01 | D01 | dự đoán cố định → cầu nối điều khiển | 13 |

Tuyến lõi: $7+31+32+25+13=108$ phút. Vùng đệm: A06 8 phút và phần hiện dần về $\gamma=1$ ở B07 4 phút. Bài tập: X07 15 phút, X03 7 phút, X04 8 phút.

## Truyền dữ kiện

- P02 cố định $v_\pi$ là đích và $V_t$ là ước lượng. Các phần sau không đổi chính sách.
- A00 cho lượt $e_1$ trước công thức A01, nêu chính sách dự định Right và xác suất đảo chiều $0{,}2$. A02 nêu đủ đầu vào, khởi tạo, vòng lượt, đầu ra, dừng, chi phí và quy tắc mỗi trạng thái tối đa một mẫu trong mỗi lượt của MC lần ghé đầu tiên.
- A03 áp dụng trọn trung bình mẫu trên $e_1,e_2$: $(1,1)$ rồi $(0,0)$. A04 mới đưa $11/21,19/21$ làm oracle. A05 giữ cùng mẫu và đổi bước học sang $\alpha=0{,}5$.
- A06 tách mọi lần ghé khỏi tuyến lõi; nhãn hàng alpha ghi rõ đây là MC mọi lần ghé, không phải TD. A07 chỉ phát biểu hội tụ chính cho lần ghé đầu tiên với các lượt khởi động lại độc lập.
- B00 cho chuyển $S\to x$ trước ký hiệu. B02 nêu đủ đầu vào, khởi tạo, vòng chuyển, đầu ra, dừng và chi phí của TD(0). B03–B04 dùng cập nhật tại chỗ.
- B06 định nghĩa $T^\pi$ rồi mới lấy kỳ vọng của $\delta_t$; mỗi $\delta_t$ là một mẫu nhiễu của sai số Bellman, một chuyển chưa xác định dấu của sai số Bellman kỳ vọng. B07 dùng $n$ là số lần cập nhật trạng thái, cho ví dụ $\alpha_n=1/n$, diễn giải Robbins–Monro bằng “học mãi nhưng nhiễu giảm dần” và định nghĩa ngay trên mặt trang $\pi$ đúng đắn là đi tới kết thúc với xác suất $1$ từ mọi trạng thái liên quan.
- C00–C01 dùng đi bộ dài; C00 không dùng hai giá trị chuẩn của nguồn vì không tái tạo nhất quán từ mô hình đã nêu. C02 báo rõ trở lại lượt ngắn, chốt $\gamma=1$, $\alpha=0{,}5$ và bảng khởi tạo bằng không; nguồn số liệu tr. 29. C03 nối số nguồn ngẫu nhiên trong $G_t$ với biến động, rồi nối phần đuôi $V_t$ với chệch.
- C01 dùng đúng $R_{t+4}$ với $\gamma^3=0{,}970299$ và $R_{t+2}$ với $-\gamma=-0{,}99$.

## Từng trang

| Mã | Luận điểm trung tâm | Câu nối |
|---|---|---|
| P00 | Từ mô hình đã biết sang quỹ đạo lấy mẫu. | Đặt bài toán dự đoán. |
| P01 | Chính sách cố định, mô hình chưa biết. | Chốt giả thiết và đối tượng học. |
| P02 | $v_\pi$ cố định còn $V_t$ thay đổi. | Xem một lượt mẫu. |
| A00 | Chính sách dự định Right, xác suất đảo chiều $0{,}2$; lượt cụ thể xuất hiện trước phần thưởng tích lũy. | Tính đích MC. |
| A01 | MC dùng toàn bộ phần còn lại sau lần ghé. | Viết thuật toán tái tạo được. |
| A02 | MC lần ghé đầu có đủ giao diện, vòng lặp, dừng, chi phí và mỗi trạng thái tối đa một mẫu trong mỗi lượt. | Chạy thuật toán trên hai lượt. |
| A03 | Trung bình mẫu cho $(1,1)$ sau $e_1$ và $(0,0)$ sau $e_2$. | Đối chiếu với giá trị thật. |
| A04 | $11/21,19/21$ chỉ là oracle đo sai số. | Tách mẫu khỏi bước học. |
| A05 | Cùng mẫu nhưng bước $1/N$ và $\alpha$ hằng cho kết quả khác. | Mở rộng quy tắc lần ghé khi còn giờ. |
| A06 | Phần đệm: mọi lần ghé cho $(1,1)$ sau $e_1$ và $(0,1/3)$ sau $e_2$ với trung bình mẫu; hàng alpha là MC mọi lần ghé. | Trở lại bảo đảm của tuyến chính. |
| A07 | Trung bình lần ghé đầu cần lượt độc lập, kỳ vọng hữu hạn và ghé vô hạn. | Kiểm tên thuật toán. |
| A08 | Tên “gia tăng” chưa xác định quy tắc mẫu và bước học; câu chuyển sang TD thay return bằng đích một bước. | Sang đích một bước. |
| B00 | Một chuyển đủ để tạo đích TD. | Phân biệt các đích. |
| B01 | $G_t$ là đích MC; $Y_t^{\mathrm{TD}}$ và $\delta_t$ thuộc TD. | Viết thuật toán tái tạo được. |
| B02 | TD(0) có đủ giao diện, vòng chuyển, dừng và chi phí. | Chạy lượt đầu. |
| B03 | Lượt đầu kết thúc tại $(0,0{,}5)$. | Tiếp tục cùng bảng. |
| B04 | Lượt hai kết thúc tại $(-0{,}375,0{,}375)$. | So thời điểm cập nhật. |
| B05 | TD cập nhật sớm; MC truyền kết quả cuối sau kết thúc. | Lấy kỳ vọng của một cập nhật. |
| B06 | Kỳ vọng sai số TD là sai số Bellman của $V_t$; mỗi $\delta_t$ là một mẫu nhiễu, chưa xác định dấu của sai số kỳ vọng. | Chọn lịch bước học. |
| B07 | Robbins–Monro dùng số lần cập nhật của từng trạng thái; nhánh $\gamma=1$ cần lượt khởi động lại và $\pi$ đúng đắn — đi tới kết thúc với xác suất $1$ từ mọi trạng thái liên quan. | Kiểm cập nhật tại chỗ. |
| B08 | Đích hàng hai dùng giá trị vừa cập nhật. | Sang quỹ đạo dài. |
| C00 | Quỹ đạo dài làm $G_t$ nhạy với đường đi; không dùng hai giá trị chuẩn không tái tạo được của nguồn. | Viết chỉ số. |
| C01 | Số mũ phụ thuộc vị trí phần thưởng. | Trở lại lượt ngắn để so phạm vi tác động. |
| C02 | Với cùng $\gamma,\alpha,V_0$, MC đổi S và x còn TD chỉ đổi x sau một lượt; nguồn số liệu tr. 29. | Giải thích chệch–phương sai. |
| C03 | MC tích lũy nhiều nguồn ngẫu nhiên; TD thay phần đuôi bằng $V_t$. | Chọn theo thiết lập. |
| C04 | Lượt, thời điểm cập nhật và mục tiêu hội tụ quyết định lựa chọn. | Kiểm số mũ. |
| C05 | $R_{t+4}$ mang $\gamma^3$. | Khóa phạm vi. |
| C06 | Không suy sang điều khiển, khác chính sách hoặc Q-learning. | Tự kiểm. |
| C07 | Ba câu hỏi phủ đích, thời điểm và bước học. | Tổng hợp. |
| D00 | Bốn phân biệt cần giữ. | Nối bài sau. |
| D01 | Điều khiển làm chính sách không còn cố định. | Sang bài tập dọc. |
| X07 | Giải thích ba kết quả đã tính với $V_0(S)=V_0(x)=0$ bằng mẫu, bước học và thời điểm cập nhật. | Chữa tổng hợp. |
| X03 | Tính đích, sai số và cập nhật TD. | Chữa ngắn. |
| X04 | Phân tích cơ chế chệch–phương sai có điều kiện. | Thảo luận. |

## Rà mạch và lân cận sau chỉnh sửa

- Đã rà P02–A04: lượt → return → thuật toán → ước lượng → oracle; không còn đặt oracle trước thao tác học.
- Đã rà A02–A07: thuật toán đầy đủ đứng trước số học; trung bình mẫu đứng trước $\alpha$ hằng; mọi lần ghé không chen vào tuyến lõi.
- Đã rà B00–B04: chuyển mẫu → phân biệt đích → thuật toán → hai lượt tại chỗ.
- Đã rà B04–B08: bảng số → thời điểm → định nghĩa $T^\pi$ → Robbins–Monro → kiểm tra tại chỗ.
- Đã rà C00–C04: đi bộ dài và chỉ số được đóng lại trước khi tiêu đề C02 báo đổi về lượt ngắn; C03–C04 không lặp B05.
- Đã rà các câu hỏi P02, C07 và D01: mỗi câu có đáp án hiện dần trên mặt trang.
