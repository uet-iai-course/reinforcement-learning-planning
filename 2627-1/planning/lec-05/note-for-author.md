# Ghi chú cho giảng viên — Bài 05

- Tuyến lõi 108 phút. Dùng 12 phút dự phòng cho A06 và phần hiện dần về $\gamma=1$ ở B07 nếu lớp theo kịp. Không nói nhãn phân tuyến hoặc thời lượng trên mặt trang và trong ghi chú diễn giả.
- Phần 30 phút bài tập: ưu tiên X07 để kiểm tra cơ chế; dùng X03 cho phép tính ngắn và X04 cho thảo luận chệch–phương sai.
- Dạy A02 như một giao diện thuật toán: đầu vào, khởi tạo, vòng lượt, đầu ra, dừng và chi phí. Sau đó chạy đủ trung bình mẫu trên A03 trước khi đổi sang $\alpha$ hằng ở A05.
- Giá trị $11/21$ và $19/21$ ở A04 chỉ dùng đối chiếu; không đưa vào cập nhật MC hoặc TD.
- Nếu dùng A06, luôn nói đủ quy tắc lần ghé, quy tắc bước học và thứ tự xử lý. Các mẫu trong một lượt không độc lập.
- Dạy B02 theo đúng vòng chuyển. Các bảng B03–B04 dùng cập nhật tại chỗ; hàng sau đọc giá trị vừa cập nhật ở hàng trước.
- B06 là cầu nối bắt buộc: định nghĩa $T^\pi$ trước, rồi chỉ ra kỳ vọng của $\delta_t$ là sai số Bellman. Chỉ dùng tính co chuẩn vô cùng khi $\gamma<1$.
- Ở B07, $n$ là số lần cập nhật riêng của trạng thái $s$. Diễn giải Robbins–Monro bằng “học mãi nhưng bước nhỏ dần để nhiễu không tích lũy”. $\alpha=0{,}5$ trong ví dụ không phải lịch hội tụ.
- Nếu mở phần $\gamma=1$, giải thích “đúng đắn” là đi tới kết thúc với xác suất 1; “quá độ” là một trạng thái chỉ được ghé hữu hạn lần trong một lượt. Phải khởi động lại nhiều lượt để có cập nhật vô hạn lần.
- Không nói TD luôn có phương sai thấp hơn hoặc luôn nhanh hơn. Nêu cơ chế: $G_t$ tích lũy nhiều nguồn ngẫu nhiên, còn TD thay phần đuôi bằng $V_t$, thường giảm biến động nhưng có thể đưa chệch vào đích.
- C01 dùng $R_{t+4}$ với $\gamma^3$ và $R_{t+2}$ với $\gamma$; không dùng số mũ sai của PDF nguồn.
- Không mở sang điều khiển, khác chính sách hoặc Q-learning. Bài sau mới xử lý chính sách thay đổi.
- Không có code demo trong nguồn; không tự thêm notebook hoặc chương trình.
