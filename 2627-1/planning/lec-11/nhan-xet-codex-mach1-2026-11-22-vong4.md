# Nhận xét của Codex: mạch 1 "Học tăng cường · Bài 11", Bài 11 (2026-11-22)

- Nguồn: `codex exec` (gói ChatGPT), model mặc định của cấu hình Codex, mức suy luận high; chạy bằng `tools/deck/codex_review.py`.
- Bản được nhận xét: `2627-1/lecture-11-lap-ke-hoach-dua-tren-mo-hinh.html` tại `cdb80d4` cộng thay đổi chưa commit; 8 trang (L11-1-01, L11-1-06, L11-1-09, L11-1-07, L11-1-02, L11-1-05, L11-1-03, L11-1-04).
- Vòng sau chỉnh sửa; nhận xét trước: `nhan-xet-codex-mach1-2026-11-22-vong3.md`.
- Điểm: Mạch dẫn dắt 9,0; Trực quan hóa 9,0; Liên kết ví dụ–toán 9,0; Cân bằng trực giác–chứng minh 8,5; Từ lý thuyết đến thuật toán 8,5. Chưa đạt điều kiện dừng (mọi tiêu chí ≥ 9).
- Prompt:

```text
Xem phần "Học tăng cường · Bài 11" (mạch 1) của bài giảng https://courses.iaidev.com/reinforcement-learning-planning/2627-1/lecture-11-lap-ke-hoach-dua-tren-mo-hinh.html#/1

Phần này đã được chỉnh sửa theo nhận xét lần trước (tệp `nhan-xet-truoc.md`). Hãy nhận xét bản sau chỉnh sửa: đề xuất nào đã được thực hiện và thực hiện tốt đến đâu, còn điều gì cần sửa.

Hãy phân tích dưới góc nhìn của sinh viên để gợi ý cách trình bày tốt hơn, trực quan hơn.

---
Ảnh đính kèm là 8 trang của phần này, đúng thứ tự trình chiếu (L11-1-01, L11-1-06, L11-1-09, L11-1-07, L11-1-02, L11-1-05, L11-1-03, L11-1-04), chụp từ bản hiện tại, có thể mới hơn trang web. Tệp `mach.md` trong thư mục làm việc chứa văn bản, công thức (TeX) và ghi chú giảng viên của từng trang. Đọc theo ảnh; dùng `mach.md` để đọc chính xác công thức.
Khi nêu vấn đề hoặc đề xuất, ghi mã trang (ví dụ L11-1-09). Viết báo cáo bằng tiếng Việt, định dạng Markdown; hình đề xuất thì mô tả bằng lời (thành phần, số liệu, chú thích).
Cuối báo cáo, chấm điểm phần này trên thang 10 theo năm tiêu chí, ghi đúng một bảng Markdown hai cột `Tiêu chí | Điểm`, mỗi tiêu chí một dòng, điểm là một số (ví dụ 8,5): Mạch dẫn dắt; Trực quan hóa; Liên kết ví dụ–toán; Cân bằng trực giác–chứng minh; Từ lý thuyết đến thuật toán.
```

---
# Nhận xét bản chỉnh sửa mạch 1 · Học tăng cường, Bài 11

Bản chỉnh sửa đã làm rõ lợi ích của lập kế hoạch ngay trong ví dụ mở bài. Ở **L11-1-09**, sinh viên thấy cùng một chuyển tiếp F → K có mục tiêu bằng \(0\) ở bước thật thứ tư và bằng \(0{,}45\) khi được mô hình sinh lại sau bước thứ năm. Dải ba mốc mới giúp giải thích vì sao giá trị ở F tăng dù tác tử vẫn chỉ đi năm bước thật. Hai việc nên ưu tiên là **hiện thao tác ghi vào mô hình ở L11-1-09** và **đưa câu trả lời về phạm vi hội tụ lên thẻ bên phải ở L11-1-07**.

Báo cáo lấy tám ảnh đính kèm làm chuẩn cho bản hiện tại. Trang web không truy cập được trong phiên này. Thứ tự hiện các lớp nội dung được đối chiếu theo ghi chú giảng viên. [Nhận xét lần trước](nhan-xet-truoc.md) · [Văn bản, công thức và ghi chú từng trang](mach.md)

## Từ mê cung đến câu hỏi trung tâm

- **L11-1-01 · Đã làm rõ vai trò của lịch lấy mẫu trong ghi chú.** Câu mở bài nêu đúng lợi ích mà sinh viên sắp thấy. Ghi chú đã xác định \(0{,}225\) ứng với thứ tự lấy \((\mathrm F,\rightarrow)\) rồi \((\mathrm K,\rightarrow)\), và đảo thứ tự cho \(0{,}3375\). Nên mang cụm **“với lượt lấy mẫu minh họa”** sang **L11-1-09** hoặc **L11-1-07**, ngay cạnh \(0{,}225\), để sinh viên đọc con số cùng với điều kiện tạo ra nó.

- **L11-1-06 · Đã thêm hình hai kết cục tại K theo góp ý.** Mũi tên vào Z ghi xác suất \(0{,}8\) và thưởng \(+1\), vòng lặp tại K ghi xác suất \(0{,}2\) và thưởng \(0\). Hai nhãn khớp trực tiếp với hai số hạng trong phương trình. Bước khó hơn là hiểu hệ số \(0{,}8780\). Nên gọi \(d\) là *số lần đi đúng tối thiểu để tới Z* ngay khi viết \(v(1)\), rồi dùng F để giải thích hệ số bằng \(0{,}8\gamma/(1-0{,}2\gamma)\). Khi chuyển sang **L11-1-09**, hiện một dòng ngắn **“Các số trên mê cung là \(v_*\) để đối chiếu. Bảng \(Q\) của tác tử khởi tạo bằng \(0\).”**

- **L11-1-09 · Đã có dải ba mốc và phân biệt được bước thật với mẫu mô phỏng.** Nét xanh, nét cam đứt và dòng “tổng số bước thật: 5” giúp sinh viên theo dõi hai loại cập nhật. Để dải này đọc được như một thuật toán, nên cho mỗi mốc hiện đúng thao tác và dữ liệu của nó:
  1. **Bước thật 4** ghi \(Q(\mathrm F,\rightarrow)=0\) sau cập nhật và lưu kết cục \(S'=\mathrm K,\ R=0\) cho cặp \((\mathrm F,\rightarrow)\).
  2. **Bước thật 5** ghi \(Q(\mathrm K,\rightarrow)=0{,}5\) sau cập nhật và lưu kết cục \(S'=\mathrm Z,\ R=+1\) cho cặp \((\mathrm K,\rightarrow)\).
  3. **Lượt lập kế hoạch đầu tiên sau bước 5** chọn \((\mathrm F,\rightarrow)\), nhận \(S'=\mathrm K,\ R=0\) từ mô hình, tính mục tiêu \(0{,}45\) rồi cập nhật \(Q(\mathrm F,\rightarrow)=0{,}225\).

  Nên dừng sau mốc 2 và hỏi **“Ngay sau cập nhật thật thứ năm, \(Q(\mathrm F,\rightarrow)\) bằng bao nhiêu?”** Khi hiện mốc 3, làm nổi số \(0{,}5\) tại K và số \(0{,}45\) trong phép tính. Sinh viên sẽ thấy chính giá trị tiếp nối ở K đã đổi. Lượt lập kế hoạch thứ hai có thể để lớp tự tính theo **L11-1-03**, với kết quả \(Q(\mathrm K,\rightarrow)=0{,}75\).

- **L11-1-07 · Đã đưa kết quả chọn tham lam lên màn hình, còn câu trả lời về mô hình sai nằm trong ghi chú.** Thẻ trái đã chuyển hai con số thành một quyết định cụ thể ở F. Có thể trình bày bằng hai hàng với bốn cột \(\uparrow,\downarrow,\leftarrow,\rightarrow\). Hàng Q-learning có bốn số \(0\), hàng sau lập kế hoạch tô đậm \(0{,}225\) ở cột \(\rightarrow\). Ở thẻ phải, đặt **“1 lần tới K / 1 lần thử”** cạnh xác suất thật \(0{,}8\), rồi thêm ngay dưới **“Với mô hình cố định và đủ điều kiện hội tụ, Q-planning hội tụ tới \(\hat q_*\) của mô hình.”** Trong câu dẫn dành cho Dyna-Q, thay chữ “hoặc” bằng trình tự **cập nhật \(Q\) từ bước thật → cập nhật mô hình → lập kế hoạch trên mẫu từ mô hình**.

## Từ quy ước đến mục tiêu học tập

- **L11-1-02 · Đã thực hiện tốt hai chỉnh sửa về cách lấy mẫu và giả thiết hội tụ.** Hình dùng chung đầu vào \((\mathrm K,\rightarrow)\), nói rõ mỗi lần gọi mô hình mẫu rút một kết cục và đánh dấu \((\mathrm K,0)\) là kết quả ví dụ. Dòng Q-learning đã thêm điều kiện động lực dừng. Nên làm nổi cụm **“ví dụ mô hình khớp luật mê cung”** để sinh viên liên hệ với \(\hat p=1\) ở **L11-1-07**. Hai hình đang minh họa hai mô hình cụ thể: một mô hình khớp xác suất thật và một mô hình đếm từ một lần quan sát. Dùng nhãn \(S'\) và \(R\) cạnh các giá trị cũng giúp sinh viên đọc được cả đầu ra \((S',R)\) ở đây lẫn bộ chuyển tiếp \((s,a,r,s')\) ở **L11-1-09**.

- **L11-1-05 · Đã thêm cả hai liên hệ được đề xuất.** Nhãn “bước 5 vừa xong” gọi lại Dyna-Q và “phòng trái → K” báo trước ví dụ tùy chọn. Ngoặc gom tìm kiếm theo cây và tối ưu kế hoạch theo thời điểm ra quyết định giúp đọc nhanh. Ở nhánh tối ưu, nên dùng **“tối ưu chuỗi hành động nhận giá trị thực”** để làm rõ “liên tục” là tính chất của không gian hành động.

- **L11-1-03 · Đã làm rõ cỡ mẫu và thứ tự lập kế hoạch.** Cụm “hai cỡ mẫu giả định” giúp tránh nhầm năm bước của cả lượt với năm lần thử một cặp. Tuy nhiên, hai giá trị \(0{,}1789\) và \(0{,}0566\) đang hiện cùng câu hỏi dự đoán. Nên cho lớp đoán hệ số giảm trước, rồi hiện \(\sqrt{50/5}\approx3{,}16\) và hai giá trị kiểm tra. Với mục RMSE, nên hỏi trước **“Với ngân sách 10 lần đánh giá, cách nào thực hiện được?”** Một cập nhật kỳ vọng đầy đủ trong ví dụ cần 100 lần đánh giá. Nếu muốn sinh viên tính RMSE bằng số, dẫn tới ví dụ có phân phối và các giá trị đích dùng trong phép tính.

- **L11-1-04 · Đã xuống dòng cho bài chạy MCTS và giữ trọng tâm ở thao tác.** Nên ghi **“so sánh hai hành động tại F, với \(m\) mô phỏng mỗi hành động”** ngay trong mục rollout. Nhãn này giúp sinh viên hiểu phạm vi của chặn xác suất trước khi gặp bài chọn trong cả bốn hành động. Với tùy chọn, đề xuất dải ba nút **phòng trái → K → Z**, ghi “tùy chọn phòng trái” và “tùy chọn phòng phải” trên hai mũi tên. Dưới dải, hiện lần lượt \(V_0\equiv0\), vòng 1 đưa giá trị dương tới K, vòng 2 truyền giá trị đó về A. Có thể hiện \(V_2(\mathrm A)=0{,}6604\) sau khi lớp dự đoán ô nào đổi ở vòng 2.

## Chấm điểm

| Tiêu chí | Điểm |
|---|---:|
| Mạch dẫn dắt | 9 |
| Trực quan hóa | 9 |
| Liên kết ví dụ–toán | 9 |
| Cân bằng trực giác–chứng minh | 8,5 |
| Từ lý thuyết đến thuật toán | 8,5 |
