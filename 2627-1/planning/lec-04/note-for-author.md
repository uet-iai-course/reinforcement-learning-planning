# Ghi chú cho giảng viên — Bài 04

1. Tuyến chính 120 phút đã gồm các tương tác ngắn. Phần chữa bài: X09 12 phút, X06 10 phút, X04 8 phút; X07 giao tự luyện. Không đưa phân bổ này vào slide hoặc ghi chú diễn giả.
2. A02 là micro-example bổ sung, không phải dữ liệu thực nghiệm. Bối cảnh phải giữ tất định: thưởng $2/0$, trạng thái kế tiếp $s_1/s_2$, $\gamma=0{,}9$, giá trị tiếp tục tối ưu $5/8$.
3. A08 ép hành động đầu bằng $a\triangleright\pi$ rồi dùng chính sách tiếp diễn từ $t=1$; không đổi lại thành điều kiện hóa trên $A_0=a$. A09 chỉ dựng ứng viên $\bar\pi$; D06 mới kết luận chính sách tối ưu.
4. A01 chỉ định nghĩa $T^\pi$ cho chính sách Markov dừng. Khi chứng minh cận trên cho mọi $\pi\in\Pi$, dùng chân trời hữu hạn ở D03; không viết $T^\pi$ cho chính sách phụ thuộc lịch sử.
5. PI trên tuyến chính là bản đánh giá chính xác. Lặp chính sách sửa đổi đã bị bỏ vì nguồn không đủ đặc tả tái lập; không trình bày bảo đảm hữu hạn của PI chính xác như bảo đảm cho bản bị cắt.
6. B04 trả về $v_{j+1}$ sau khi $\Delta_j\le\varepsilon_{\mathrm{step}}$; vì vậy chặn là $\gamma\varepsilon_{\mathrm{step}}/(1-\gamma)$.
7. C09 tính $w=T_*v$ để lấy phần dư tại cùng bảng dùng trích $\pi_v$. Nếu chưa dừng, đặt $v\leftarrow w$; không tính lại lượt quét vừa có.
8. D03 chỉ chứng minh $v_\pi\le\bar v$; D06 mới chứng minh chính sách tham lam đạt cận. D04 chỉ suy residual→value; D07 mới suy value→policy bằng $T^{\pi_v}v=T_*v$.
9. Gridworld dùng $\gamma=0{,}9$, biên trái giữ nguyên, $c_5$ hấp thụ và giá trị kết thúc bằng không. Không thay quy ước nếu không tính lại bảng C02.
10. CartPole chỉ minh họa giới hạn rời rạc hóa. Không biến phần này thành code demo vì nguồn không cung cấp mã tương ứng.
