# Bài 03 — Quá trình quyết định Markov

## Phạm vi và mục tiêu

- Nguồn chính: `RL-hk2-2025-2026/lecture2-3-MDPswithKeyConcepts.pptx`, trang 28–58.
- Bài tập: `RL-hk2-2025-2026/resources/hw02.pdf`, Bài 3, 4, 7, 8.
- Tuyến chính: 35 trang, 120 phút. Bốn bài tập ở nhánh dọc, ngoài tuyến chính.
- Bài này giả sử biết mô hình. Quy hoạch động thuộc Bài 04; phương pháp phi mô hình thuộc các bài sau.
- Không dạy Bellman tối ưu, lặp giá trị hoặc lặp chính sách. Bài 9 của bài tập chuyển sang Bài 04.

Sau bài học, sinh viên có thể kiểm tra ma trận chuyển; tính phần thưởng tích lũy; lập và giải Bellman cho MRP; tạo MRP từ MDP dưới chính sách Markov dừng; liên hệ $v_\pi$, $q_\pi$ và Bellman kỳ vọng.

## Ánh xạ nguồn

| Trang nguồn | Quyết định | Trang đích | Lý do |
|---:|---|---|---|
| 28–30 | gộp, sửa | P00–P02, A00–A01 | Đặt mục tiêu; diễn đạt chính xác quan hệ kế thừa; nêu phạm vi biết mô hình. |
| 31–33 | tách, vẽ lại | A02–A05 | Đặt đồ thị trước định nghĩa; quỹ đạo và ma trận dùng cùng thứ tự, quy ước véc-tơ cột. |
| 34–35 | sửa, sắp lại | B01,B00 | Đặt véc-tơ thưởng trước định nghĩa MRP; tách $R_{t+1}$ khỏi $r(s)$. |
| 36–40 | gộp, tính lại | B02–B03 | Nêu điều kiện hữu hạn; tính lại hai phần thưởng tích lũy. |
| 39–43 | gộp, sắp lại | B04, C00, C05 | Định nghĩa giá trị, dùng một sao lưu tạm trước Bellman, chỉ đưa nghiệm sau công thức. |
| 44–48 | tách, sửa | C01–C06 | Dẫn từ phân rã một bước tới hệ; bỏ thuật ngữ ánh xạ co chưa định nghĩa; nêu điều kiện $\gamma=1$. |
| 49 | sửa | D00 | Dùng hạt nhân chung sau ví dụ; nêu miền thưởng rời rạc và quy tắc thay tổng bằng tích phân. |
| 50 | vẽ lại, sửa, sắp lại | D01, D03, D06 | Đặt Student MDP trước định nghĩa; khôi phục nút ngẫu nhiên Pub; nêu rõ dữ kiện giá trị ở D06. |
| 51 | vẽ lại, sửa | D09–D10 | Biểu diễn đủ sáu kết quả; dùng Warm–Fast nhận $-10$ rồi kết thúc. |
| 52–53 | giữ, mở rộng | D02, D05–D06 | Chính sách Markov dừng; ví dụ $q_\pi$ và quan hệ với $v_\pi$. |
| 54–55 | tính lại, gộp | D06, D10 | Dùng nghiệm Student và Racing Car đã kiểm. |
| 56–57 | tách | D07–D08 | Hai Bellman kỳ vọng đặt sau ví dụ và cầu nối MRP cảm sinh. |
| 58 | chuyển | D11–D13, `note-for-author.md` | Nối rõ quy hoạch động và phi mô hình; nguồn đọc chưa đủ thư mục để công bố. |
| hw02 Bài 3,4,7,8 | giữ phạm vi | X03,X04,X07,X08 | Nhánh dọc; phân bổ chữa lưu ngoài slide. |

## Ký hiệu và quy ước

| Ký hiệu | Nghĩa |
|---|---|
| $P_{ss'}$ | $\Pr(S_{t+1}=s'\mid S_t=s)$ trong chuỗi Markov/MRP. |
| $\mu_t$ | Phân phối trạng thái dạng véc-tơ cột; $\mu_{t+1}=P^{\mathsf T}\mu_t$. |
| $r(s)$ | $\mathbb E[R_{t+1}\mid S_t=s]$; Student MRP dùng $R_{t+1}=r(S_t)$. |
| $G_t$ | Phần thưởng tích lũy từ $R_{t+1}$. |
| $Q$ | Ma trận con của các trạng thái chưa kết thúc khi $\gamma=1$. |
| $p(s',r\mid s,a)$ | Hạt nhân chung của MDP; các tổng trong bài dùng miền rời rạc. |
| $\pi(a\mid s)$ | Chính sách Markov ngẫu nhiên dừng. |
| $P^\pi,r^\pi$ | Động lực và thưởng của MRP cảm sinh bởi chính sách cố định. |
| $v_\pi,q_\pi$ | Giá trị trạng thái và giá trị hành động dưới $\pi$. |

## Tài sản SVG

- `student-mrp.svg`: bảy trạng thái, đúng toàn bộ xác suất chuyển và Sleep hấp thụ.
- `bellman-backup.svg`: sao lưu Bellman kỳ vọng, nhãn cốt lõi từ 30 px.
- `student-mdp.svg`: đúng topology nguồn, gồm nút ngẫu nhiên sau hành động Pub.
- `racing-car.svg`: đủ sáu kết quả theo cặp trạng thái–hành động, xác suất và thưởng.
