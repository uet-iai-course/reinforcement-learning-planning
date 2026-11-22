# Nhận xét của Codex: mạch 2 "Tính bất định của môi trường và lập kế hoạch nền", Bài 11 (2026-11-22)

- Nguồn: `codex exec` (gói ChatGPT), model mặc định của cấu hình Codex, mức suy luận high; chạy bằng `tools/deck/codex_review.py`.
- Bản được nhận xét: `2627-1/lecture-11-lap-ke-hoach-dua-tren-mo-hinh.html` tại `cdb80d4`; 17 trang (L11-2-00, L11-2-03, L11-2-06, L11-2-13, L11-2-04, L11-2-07, L11-2-16, L11-2-17, L11-2-08, L11-2-11, L11-2-12, L11-2-18, L11-2-14, L11-2-09, L11-2-10, L11-2-15, L11-2-19).
- Vòng sau chỉnh sửa; nhận xét trước: `nhan-xet-codex-mach2-2026-11-22-vong2.md`.
- Điểm: Mạch dẫn dắt 8,5; Trực quan hóa 9,0; Liên kết ví dụ–toán 9,0; Cân bằng trực giác–chứng minh 8,5; Từ lý thuyết đến thuật toán 8,5. Chưa đạt điều kiện dừng (mọi tiêu chí ≥ 9).
- Prompt:

```text
Xem phần "Tính bất định của môi trường và lập kế hoạch nền" (mạch 2) của bài giảng https://courses.iaidev.com/reinforcement-learning-planning/2627-1/lecture-11-lap-ke-hoach-dua-tren-mo-hinh.html#/2

Phần này đã được chỉnh sửa theo nhận xét lần trước (tệp `nhan-xet-truoc.md`). Hãy nhận xét bản sau chỉnh sửa: đề xuất nào đã được thực hiện và thực hiện tốt đến đâu, còn điều gì cần sửa.

Hãy phân tích dưới góc nhìn của sinh viên để gợi ý cách trình bày tốt hơn, trực quan hơn.

---
Ảnh đính kèm là 17 trang của phần này, đúng thứ tự trình chiếu (L11-2-00, L11-2-03, L11-2-06, L11-2-13, L11-2-04, L11-2-07, L11-2-16, L11-2-17, L11-2-08, L11-2-11, L11-2-12, L11-2-18, L11-2-14, L11-2-09, L11-2-10, L11-2-15, L11-2-19), chụp từ bản hiện tại, có thể mới hơn trang web. Tệp `mach.md` trong thư mục làm việc chứa văn bản, công thức (TeX) và ghi chú giảng viên của từng trang. Đọc theo ảnh; dùng `mach.md` để đọc chính xác công thức.
Khi nêu vấn đề hoặc đề xuất, ghi mã trang (ví dụ L11-2-06). Viết báo cáo bằng tiếng Việt, định dạng Markdown; hình đề xuất thì mô tả bằng lời (thành phần, số liệu, chú thích).
Cuối báo cáo, chấm điểm phần này trên thang 10 theo năm tiêu chí, ghi đúng một bảng Markdown hai cột `Tiêu chí | Điểm`, mỗi tiêu chí một dòng, điểm là một số (ví dụ 8,5): Mạch dẫn dắt; Trực quan hóa; Liên kết ví dụ–toán; Cân bằng trực giác–chứng minh; Từ lý thuyết đến thuật toán.
```

---
# Nhận xét bản chỉnh sửa mạch 2 — Tính bất định của môi trường và lập kế hoạch nền

Bản chỉnh sửa làm rõ nhất cách phần thưởng ở \(Z\) truyền ngược qua \(K\), \(F\) rồi \(B\). Từ ví dụ tính tay đến bài tập, sinh viên có thể chỉ ra ô nào được ghi, ô nào được đọc ngay sau đó và vì sao đổi thứ tự lại cho kết quả khác. Chỗ dễ mất mạch nhất là khi **cùng một mê cung chuyển từ mô hình đếm sang mô hình lưu kết cục gần nhất rồi quay lại mô hình đếm**. Ghi tên mô hình ở ngay đầu mỗi ví dụ sẽ giúp sinh viên theo dõi cả phép tính lẫn phạm vi của các kết luận. **L11-2-03, L11-2-07, L11-2-16, L11-2-12, L11-2-10.**

Tôi đánh giá theo 17 ảnh đúng thứ tự chiếu và dùng `mach.md` để đối chiếu công thức, giả thiết và ghi chú giảng viên. Trang web không tải được trong lần kiểm tra này, nên phần nhận xét về hiển thị dựa trên các ảnh đính kèm. [Nhận xét lần trước](/tmp/claude-1000/-data-tqlong-lectures/fd411c55-a86c-4518-a9f0-a6d4fde11419/scratchpad/lec11/codex-m2-v3/nhan-xet-truoc.md) · [Văn bản và ghi chú giảng viên](/tmp/claude-1000/-data-tqlong-lectures/fd411c55-a86c-4518-a9f0-a6d4fde11419/scratchpad/lec11/codex-m2-v3/mach.md)

## Các đề xuất lần trước đã được thực hiện đến đâu

- **L11-2-00, L11-2-03, L11-2-06 — Câu hỏi mở mới thực hiện một phần.** Câu hỏi về cách tăng \(Q(F,\rightarrow)\) đã xuất hiện ở trang mô hình đếm. Số thứ tự ①, ② và hai thanh \(1/2\) cho thấy tần suất được tính từ đâu. Hình “đọc \(K\), ghi \(F\)” giải thích tốt hai con số \(0{,}45\) và \(0{,}225\). Trang mở vẫn chủ yếu giới thiệu đề mục, nên sinh viên phải đợi đến L11-2-06 mới thấy đầy đủ tình huống khiến câu hỏi có ý nghĩa.
- **L11-2-13, L11-2-18 — Phạm vi của bảo đảm hội tụ đã rõ hơn.** L11-2-13 đã nêu mô hình cố định và đủ các cặp, đồng thời cho thấy \(0{,}729\) đến từ ba lần chiết khấu trước phần thưởng \(+1\). L11-2-18 đối chiếu đủ bốn giả thiết, phân biệt lần ghi đè ở lượt đầu với lần ghi lại cùng kết cục ở lượt hai, và dùng đúng chữ “chưa có bảo đảm” cho việc chọn mọi cặp vô hạn lần. Tiêu đề phụ trong hình L11-2-13 vẫn nên nói rõ điều kiện “đi đúng” chỉ áp cho các kết cục lưu **trên đường đang vẽ**, như phần văn bản bên phải đã nêu.
- **L11-2-07, L11-2-16, L11-2-17, L11-2-08 — Trình tự ví dụ, sơ đồ, giả mã đã được cải thiện.** Sơ đồ Dyna nay đứng ngay trước giả mã và dùng đúng bước thật \(A\to B\) sẽ gặp trong bài tập. Hai ô đóng khung \(0{,}5\) trên L11-2-16 đã làm được việc mà mũi tên được đề xuất lần trước cần làm. Trang này cũng ghi rõ \(0{,}225\) phụ thuộc vào thứ tự chọn cặp. Phần còn thiếu là một nhãn nổi bật cho mô hình lưu kết cục gần nhất trên L11-2-07, nơi cách lưu này xuất hiện ngay sau các trang nói về mô hình đếm.
- **L11-2-11, L11-2-12 — Bài tập kiểm tra tốt việc cập nhật tại chỗ.** Hai ô \(0{,}45\) đóng khung nối trực tiếp giá trị vừa ghi ở \(F\) với mục tiêu của cập nhật ở \(B\). Câu đảo thứ tự cho \(0{,}10125\) so với \(0{,}2025\), đủ để phát hiện sinh viên đang dùng giá trị cũ hay mới. Ảnh cho thấy cả câu hỏi và đáp số. Nếu chúng đang hiện cùng lúc khi chiếu, nên cho lớp dự đoán trước khi hiện đáp số.
- **L11-2-14, L11-2-09 — Đã xử lý tốt xác suất trượt trong ví dụ đổi cửa.** Cột “kết cục khi đi đúng” và ô “sang \(C\) với xác suất \(0{,}8\)” đã sửa đúng hai điểm được góp ý. Chuỗi \(0{,}64>0{,}6\) → chọn đi phải → quan sát thật → ghi mô hình cho thấy thưởng trong lập kế hoạch dẫn đến một lần thử thật như thế nào.
- **L11-2-04, L11-2-10, L11-2-15, L11-2-19 — Các chú thích về sai số đã được bổ sung.** L11-2-04 đã giải thích \(0{,}2828\) là độ lệch chuẩn qua nhiều nhóm hai lần thử. L11-2-15 đã đưa giá trị nhánh, giả thiết phương sai \(1\) và vai trò của \(\alpha_j=1/j\) lên trang. L11-2-19 đã ghi rõ mốc so sánh trên trục dọc, mức \(1\) giả định của đường xám và sự khác nhau giữa \(C\) và \(k\). Phần sinh viên còn phải tự suy ra là mục tiêu kỳ vọng cụ thể là số nào và vì sao chứng minh sinh ra hệ số \((b-1)/b\).

## Những chỗ nên sửa tiếp

1. **Mở bằng một bước đi và một ô giá trị chưa đổi. L11-2-00, L11-2-03, L11-2-06.** Dùng dải ba ô \(F\to K\to Z\), ghi phần thưởng \(0\) và \(+1\) trên hai mũi tên. Dưới bước \(F\to K\), ghi “lúc đọc \(K\), giá trị còn bằng \(0\)”. Dưới bước \(K\to Z\), ghi “sau bước này, \(Q(K,\rightarrow)=0{,}5\)”. Khi đó câu hỏi “Làm sao cập nhật \(F\) ngay bây giờ?” có đủ dữ kiện. L11-2-06 có thể dùng lại đúng dải này và thêm mũi tên nét đứt cho mẫu mô phỏng.

2. **Cho sinh viên thấy hai mô hình lưu gì từ cùng dữ liệu. L11-2-03, L11-2-07, L11-2-08, L11-2-10.** Ở L11-2-07, dùng hai ô cạnh nhau dưới hai quan sát ① ở lại \(A\), ② sang \(B\). Ô “mô hình đếm” giữ \(A:1,\ B:1\). Ô “kết cục gần nhất” gạch kết cục \((0,A)\) cũ và giữ \((0,B)\). Gắn nhãn “dùng kết cục gần nhất để tính tay” ở ví dụ Dyna-Q và “dùng lại mô hình đếm của L11-2-03” trên cây L11-2-10. Ở L11-2-08, viết rõ biến thể có trượt rút **cả cặp** \((R,S')\) từ một lần thử cũ của cặp trạng thái–hành động đã chọn. Sinh viên có thể chuyển ngay mô tả này thành cách cài đặt.

3. **Tách điều kiện chạy một cập nhật khỏi điều kiện hội tụ toàn bảng. L11-2-06, L11-2-07, L11-2-13, L11-2-17, L11-2-18.** Câu “Q-planning cần mô hình ở mọi cặp” trên L11-2-07 dễ khiến sinh viên thắc mắc vì ngay sau đó Dyna-Q vẫn lập kế hoạch với bốn cặp. Có thể viết “Một cập nhật cần mô hình ở cặp được chọn. Mệnh đề 11.4 xét hội tụ toàn bảng, với mô hình cố định và đủ mọi cặp hợp lệ.” Trên L11-2-17, dùng chính bước thật \(A\to B\) và đánh dấu ô \(F\) được cập nhật khi tác tử đang ở \(B\). Cách vẽ đó cũng giúp sửa câu “trước khi tác tử gặp chúng” thành “trước khi tác tử quay lại”, khớp với việc ví dụ chọn cặp đã thử.

4. **Đặt hai con số \(0{,}3\) và \(0{,}2828\) vào hai tình huống lấy dữ liệu. L11-2-04.** Dòng mở lấy kết quả của một lượt đi, còn đồ thị áp dụng khi ấn định \(C\) trước. Sinh viên có thể thấy cùng \(C=2\) và tưởng hai con số phải bằng nhau. Gắn nhãn “lượt vừa quan sát” cạnh \(|0{,}5-0{,}8|=0{,}3\), và “lặp nhiều nhóm, mỗi nhóm đúng hai lần thử” cạnh \(0{,}2828\). Có thể vẽ ba kết quả khả dĩ của mỗi nhóm là \(\hat p=0,\ 0{,}5,\ 1\). Nhắc bằng một câu rằng trong lượt mê cung, lần thử thứ hai ở \(A\) xảy ra vì lần đầu bị trượt.

5. **Cho thấy kết cục sau một lần thử lại lối mở. L11-2-14, L11-2-09.** Sau ô “thử \(\rightarrow\) ở \(B\)”, tách hình thành hai nhánh “sang \(C\), xác suất \(0{,}8\)” và “ở lại \(B\), xác suất \(0{,}2\)”. Cả hai nhánh tới bước (e) ghi kết cục vừa thấy. Ghi \(\ell(B,\rightarrow)\gets0\) ngay tại lần thử thật. Nếu sinh viên cần cài Dyna-Q+, thêm một dòng về biến thể cho phép lập kế hoạch với hành động chưa thử, khởi tạo bằng kết cục ở nguyên trạng thái và thưởng \(0\). Chi tiết này hiện chỉ có trong ghi chú. [Sutton và Barto, §8.3](https://www.andrew.cmu.edu/course/10-703/textbook/BartoSutton.pdf#page=190)

6. **Nối cây hai nhánh với công thức RMSE và quyết định theo ngân sách. L11-2-10, L11-2-15, L11-2-19.** Ghi ngay dưới cây \(\bar y=(0{,}54+0{,}36)/2=0{,}45\), rồi dùng lại \(\bar y\) trên trang chứng minh. Giải thích bằng hai bước: giữ nguyên các giá trị nhánh và rút có hoàn lại thì trung bình \(k\) mẫu có MSE \(\sigma^2/k\) quanh \(\bar y\). Lấy trung bình qua các bộ giá trị nhánh cho \(\mathbb E[\sigma^2]=1-1/b\), vì phương sai của trung bình \(b\) nhánh độc lập là \(1/b\). Trên đồ thị, ghi cạnh chấm xám “đã tính đúng mục tiêu kỳ vọng của mô hình”. Có thể chốt bằng hai mốc: với \(b=2,\ k=2\), phép tính kỳ vọng đã xong, còn RMSE của lấy mẫu theo giả thiết là \(0{,}5\). Với \(b=100,\ k=10\), lấy mẫu đã cho một ước lượng có RMSE \(0{,}3146\) trong khi phép tính đủ nhánh cần \(100\) lượt đánh giá. [Sutton và Barto, §8.5, Hình 8.7](https://www.andrew.cmu.edu/course/10-703/textbook/BartoSutton.pdf#page=196)

## Chấm điểm trên thang 10

| Tiêu chí | Điểm |
|---|---:|
| Mạch dẫn dắt | 8,5 |
| Trực quan hóa | 9 |
| Liên kết ví dụ–toán | 9 |
| Cân bằng trực giác–chứng minh | 8,5 |
| Từ lý thuyết đến thuật toán | 8,5 |
