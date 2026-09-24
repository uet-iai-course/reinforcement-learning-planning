# Đối chiếu lecture note và slide Bài 04

Lecture note dành cho sinh viên tại `2627-1/materials/lec-04/lecture-note.md` được viết theo bộ 45 slide hoàn tất ngày 24-09-2026. Nguồn trực tiếp là nội dung và ghi chú diễn giả trong `lecture-04-giai-mdp-bang-quy-hoach-dong.html`; không dùng bộ số của lecture note cũ.

| Phần của note | Slide | Nội dung cần khớp |
|---|---|---|
| 1. Lập kế hoạch từ mô hình | 01–05 | Mô hình hai trạng thái, tổng dài hạn, nhìn trước một bước |
| 2. Bellman tối ưu | 06–12 | Phân biệt $Q_v,q^\pi,q_*$, tối ưu, hai toán tử |
| 3. Đánh giá chính sách | 13–18 | Giải hệ, lặp, lịch cập nhật, bảng trả về |
| 4. Lặp chính sách | 19–26 | Đánh giá lại, cải thiện, giữ hòa và dừng hữu hạn |
| 5. Lặp giá trị | 27–34 | Lưới năm ô, bảng đồng bộ, trích chính sách và phần dư |
| 6. Hội tụ và sai số | 35–41 | Tính co, điểm bất động, chặn phần dư, rời rạc hóa |
| 7. Tổng hợp và vận dụng | 42–45 | So sánh phương pháp, kiểm chứng tối ưu, bài tập |

## Quy ước cần giữ khi chỉnh tài liệu

- Hai trạng thái dùng thưởng $2,-1,5,10$ và $\gamma=0{,}5$. Giá trị chính sách lần lượt là $(4,7)$, $(4,20)$ và $(9,20)$. Số $13{,}5$ là giá trị chọn $b$ một lần tại $s_1$ rồi theo chính sách cũ; giá trị của chính sách mới tại đó là $20$.
- Lưới dùng thưởng thường $-1$, thưởng đi vào đích $24$ và $\gamma=0{,}5$. Trạng thái kết thúc có giá trị $0$; đi trái từ ô đầu giữ nguyên ô đó. Mọi cập nhật đồng bộ đọc cùng bảng cũ. Phần dư của $v_3$ là $3$; $v_5=v_4$.
- Định nghĩa $q^\pi$ ấn định hành động đầu, kể cả khi hành động đó có xác suất bằng không dưới $\pi$. Toán tử $T^\pi$ dùng chính sách Markov dừng; chứng minh cận trên cho chính sách phụ thuộc lịch sử dùng kỳ vọng theo lịch sử.
- Đánh giá chính sách trả bảng mới $w=T^\pi v$, còn lặp giá trị trả bảng $v$ đã đo phần dư cùng $\pi_v$. Hai chặn sai số tương ứng có hệ số khác nhau. Lặp chính sách khi hết ngân sách trả đúng chính sách đã đánh giá cùng giá trị của nó.
- Quy tắc giữ hành động cũ khi hòa đi cùng bảo đảm dừng hữu hạn của lặp chính sách đánh giá chính xác. Không áp dụng bảo đảm đó cho phiên bản đánh giá bị cắt.
- Chặn sai số đầu $64$ là giả định minh họa độc lập; không suy ra từ lưới. Phần dư $0{,}15$ cho chặn sai số $0{,}3$; chưa đủ bảo đảm ngưỡng $0{,}2$. Phần dư dương không tự chứng nhận chính sách tối ưu tuyệt đối.
- CartPole chỉ minh họa giới hạn biểu diễn: $3\times3\times6\times6=324$ ô chưa cung cấp mô hình và chưa bảo đảm tính Markov. Không có code demo trong phạm vi note.

Mỗi phần có một câu hỏi tự kiểm, gợi ý và lời giải. Nguồn, hình và liên kết được đọc qua `material-viewer.html`; đường dẫn tính từ `2627-1/`, theo quy ước chung của trình xem. Bản sinh viên không hiển thị mã nội bộ hoặc các chỉ dẫn trong tệp này. Kết quả rà nội dung và trình xem nằm trong `review-log.md`.
