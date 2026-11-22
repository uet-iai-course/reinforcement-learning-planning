# Nhận xét của Codex: mạch 2 "Tính bất định của môi trường và lập kế hoạch nền", Bài 11 (2026-11-22)

- Nguồn: `codex exec` (gói ChatGPT), model mặc định của cấu hình Codex, mức suy luận high; chạy bằng `tools/deck/codex_review.py`.
- Bản được nhận xét: `2627-1/lecture-11-lap-ke-hoach-dua-tren-mo-hinh.html` tại `9096f20` cộng thay đổi chưa commit; 17 trang (L11-2-00, L11-2-03, L11-2-06, L11-2-13, L11-2-04, L11-2-07, L11-2-16, L11-2-08, L11-2-17, L11-2-11, L11-2-12, L11-2-18, L11-2-14, L11-2-09, L11-2-10, L11-2-15, L11-2-19).
- Vòng sau chỉnh sửa; nhận xét trước: `nhan-xet-codex-mach2-2026-11-22.md`.
- Điểm: Mạch dẫn dắt 8,5; Trực quan hóa 9,0; Liên kết ví dụ–toán 8,5; Cân bằng trực giác–chứng minh 8,0; Từ lý thuyết đến thuật toán 8,5. Chưa đạt điều kiện dừng (mọi tiêu chí ≥ 9).
- Prompt:

```text
Xem phần "Tính bất định của môi trường và lập kế hoạch nền" (mạch 2) của bài giảng https://courses.iaidev.com/reinforcement-learning-planning/2627-1/lecture-11-lap-ke-hoach-dua-tren-mo-hinh.html#/2

Phần này đã được chỉnh sửa theo nhận xét lần trước (tệp `nhan-xet-truoc.md`). Hãy nhận xét bản sau chỉnh sửa: đề xuất nào đã được thực hiện và thực hiện tốt đến đâu, còn điều gì cần sửa.

Hãy phân tích dưới góc nhìn của sinh viên để gợi ý cách trình bày tốt hơn, trực quan hơn.

---
Ảnh đính kèm là 17 trang của phần này, đúng thứ tự trình chiếu (L11-2-00, L11-2-03, L11-2-06, L11-2-13, L11-2-04, L11-2-07, L11-2-16, L11-2-08, L11-2-17, L11-2-11, L11-2-12, L11-2-18, L11-2-14, L11-2-09, L11-2-10, L11-2-15, L11-2-19), chụp từ bản hiện tại, có thể mới hơn trang web. Tệp `mach.md` trong thư mục làm việc chứa văn bản, công thức (TeX) và ghi chú giảng viên của từng trang. Đọc theo ảnh; dùng `mach.md` để đọc chính xác công thức.
Khi nêu vấn đề hoặc đề xuất, ghi mã trang (ví dụ L11-2-06). Viết báo cáo bằng tiếng Việt, định dạng Markdown; hình đề xuất thì mô tả bằng lời (thành phần, số liệu, chú thích).
Cuối báo cáo, chấm điểm phần này trên thang 10 theo năm tiêu chí, ghi đúng một bảng Markdown hai cột `Tiêu chí | Điểm`, mỗi tiêu chí một dòng, điểm là một số (ví dụ 8,5): Mạch dẫn dắt; Trực quan hóa; Liên kết ví dụ–toán; Cân bằng trực giác–chứng minh; Từ lý thuyết đến thuật toán.
```

---
# Nhận xét bản chỉnh sửa mạch 2 — Tính bất định của môi trường và lập kế hoạch nền

Bản 17 trang cải thiện rõ nhất ở đoạn **Dyna-Q qua hai lượt đi**. Sinh viên có thể lần theo phần thưởng \(+1\) ở đích, thấy giá trị được truyền từ \(K\) về \(F\) rồi về \(B\), và tự tính vì sao thứ tự cập nhật làm kết quả thay đổi. Chỗ dễ mất mạch nhất vẫn là lúc cùng một mê cung chuyển từ **mô hình đếm** sang **mô hình lưu kết cục gần nhất**, rồi quay lại mô hình đếm. Nên ghi tên mô hình ngay tại những hình và phép tính phụ thuộc vào lựa chọn đó. **L11-2-03, L11-2-13, L11-2-07, L11-2-10.**

Tôi đánh giá bố cục theo 17 ảnh đính kèm và đối chiếu công thức, giả thiết với `mach.md`. Tôi chưa tải được bản web nên đánh giá phần hiển thị ở khung hình đã gửi. [Nhận xét lần trước](nhan-xet-truoc.md) · [Văn bản và ghi chú giảng viên](mach.md) · [Bản web Bài 11](https://courses.iaidev.com/reinforcement-learning-planning/2627-1/lecture-11-lap-ke-hoach-dua-tren-mo-hinh.html#/2)

## Các đề xuất lần trước đã được thực hiện đến đâu

- **L11-2-00, L11-2-03, L11-2-06 — Câu hỏi mở đã có và phép tính được minh họa rõ.** Câu hỏi “tăng \(Q(F,\rightarrow)\) bằng cách nào mà không đi lại qua \(F\)?” xuất hiện ở L11-2-03. Trang này đã có số thứ tự ①, ②, tổng năm bước thật, bốn cặp đã thử, nhãn \(C=0\) và hai công thức hiện trọn. L11-2-06 thực hiện tốt đề xuất “đọc \(K\), ghi \(F\)” bằng viền ô, nét mũi tên và hai dòng tính từ mục tiêu \(0{,}45\) đến giá trị mới \(0{,}225\). Trang mở L11-2-00 vẫn dành chỗ cho sơ đồ toàn bài và danh sách thuật ngữ, nên tình huống cụ thể đến muộn một trang.
- **L11-2-13, L11-2-04 — Hai hình đã làm rõ những khác biệt quan trọng.** L11-2-13 đặt \(0{,}6604\) cạnh môi trường có trượt và \(0{,}729\) cạnh mô hình lưu kết cục gần nhất. Dải bốn bước, với \(+1\) ở bước cuối, giải thích được \(\gamma^3\). Câu nối sang mục tiêu Bellman cũng đã lên trang. L11-2-04 dùng xuyên suốt biến cố sang \(B\) khi chọn phải ở \(A\), ghi rõ hai trục, hai đường và hai mốc \(C=2,50\). Lời giải thích qua trung bình Bernoulli giúp sinh viên đọc đồ thị cùng công thức.
- **L11-2-07, L11-2-16, L11-2-08, L11-2-17 — Ví dụ, thuật toán và kiến trúc đã dùng chung các nhãn (d), (e), (f).** Bảng lượt đầu cho thấy lần ghi đè ở \(A\) và ba cập nhật \(0{,}5 \rightarrow 0{,}225 \rightarrow 0{,}75\) ở các ô tương ứng. Trang mới L11-2-16 cho thấy phép tính từng hàng và đối chiếu \(n=0\) với \(n=2\) trên cùng năm bước thật. L11-2-08 đã bổ sung \(\gamma\), quy ước ở trạng thái kết thúc và cách dùng mô hình đếm khi có trượt. Trang mới L11-2-17 làm rõ hai đường dẫn vào cùng bảng \(Q\), đồng thời cho thấy mẫu thật còn được dùng để học mô hình.
- **L11-2-11, L11-2-12, L11-2-18 — Bài tập đã kiểm được cả tính toán lẫn giả thiết.** Hai ô đóng khung \(0{,}45\) cho thấy hàng sau đọc giá trị vừa ghi ở hàng trước. Câu đảo thứ tự cho \(0{,}10125\) so với \(0{,}2025\), đúng với mục tiêu kiểm tra cập nhật tại chỗ. Trang mới L11-2-18 đưa đủ bốn giả thiết lên màn chiếu, ghi rõ bước đang xét lưu lại đúng \((0,B)\), và kết luận đúng phạm vi của mệnh đề.
- **L11-2-14, L11-2-09 — Ví dụ đổi cửa đã có hình và có cơ chế giải thích.** Hai mê cung cùng bố cục cho phép nhìn ngay cửa nào đóng, lối nào mở và vì sao hai đường đều dài bốn bước. Bảng phân biệt dự đoán lạc quan ở \(F\) và bi quan ở \(B\). Chuỗi \(0{,}64>0{,}6\) → chọn phải ở \(B\) → quan sát thật → cập nhật mô hình cho thấy chính xác tiền thưởng trong bước lập kế hoạch ảnh hưởng đến hành động ra sao.
- **L11-2-10, L11-2-15, L11-2-19 — Phần ngân sách đã có ví dụ xuyên suốt, còn thiếu một bước giải thích.** Hai cây dùng lại đúng ①, ② từ mô hình đếm, ghi \(R=0\) và số lượt đánh giá. Câu hỏi \(b=100,\ k=10\) chuyển tự nhiên sang đồ thị mới, nơi điểm \((0{,}1;\,0{,}3146)\) được làm nổi. L11-2-15 đã phân biệt \(C\) với \(k\). Định nghĩa chính xác của giá trị nhánh và lý do xuất hiện hệ số \((b-1)/b\) vẫn nằm trong ghi chú. Đường xám trên đồ thị vẫn thiếu chú thích về giả định sai số ban đầu.

## Những chỗ nên sửa tiếp

1. **Đưa tình huống \(F\to K\to Z\) lên L11-2-00 và ghi tên mô hình tại chỗ chuyển.** Dùng hình ba ô, ghi \(+1\) trên mũi tên \(K\to Z\), và dưới hình ghi \(Q(K,\rightarrow)=0{,}5\), \(Q(F,\rightarrow)=0\) sau lượt đầu của Q-learning. Hỏi lớp vì sao ô \(F\) vẫn bằng \(0\), rồi để L11-2-06 trả lời. Ở **L11-2-03 và L11-2-07**, đặt cạnh nhau hai cách lưu cùng hai quan sát ở \(A\): bảng đếm giữ \(A:1,\ B:1\), còn bảng kết cục gần nhất giữ \((0,B)\) sau lần ②. Nhắc lại nhãn “mô hình đếm từ L11-2-03” trên hai cây ở **L11-2-10**. Ở **L11-2-08**, ghi rõ biến thể có trượt lấy mẫu từ các kết cục **ghép cặp** \((R,S')\) đã quan sát cho cặp đó. Như vậy sinh viên biết cách lấy cả phần thưởng và trạng thái kế từ mô hình.

2. **Gắn từng kết luận hội tụ với đúng giả thiết.** Ở **L11-2-13**, thêm ngay dưới \(0{,}729\) dòng “mô hình đã đủ các cặp, được giữ cố định, các kết cục lưu trên đường vẽ đều đi đúng”. Bốn cặp của lượt đầu ở L11-2-07 là dữ liệu của một ví dụ khác. Có thể thay đoạn “Ý nghĩa” bằng một dòng ký hiệu: kỳ vọng của mục tiêu mẫu \(R+\gamma\max_{a'}Q(S',a')\) theo mô hình bằng mục tiêu Bellman tối ưu **của mô hình đó**. Ở **L11-2-18**, ghi “chưa có bảo đảm mọi cặp sẽ được chọn vô hạn lần”. Quy tắc chọn trong các cặp đã thử mô tả tập cặp hiện tại. Độ bao phủ về lâu dài còn phụ thuộc vào những cặp tác tử sẽ thử trong môi trường thật. Dẫn lại lần ghi đè ở L11-2-07 để minh họa mô hình từng đổi, dù lần ghi đang xét cho cùng kết cục.

3. **Dùng sơ đồ Dyna để giới thiệu vòng lặp, rồi cho lớp dự đoán bước kế.** Đặt **L11-2-17** ngay trước giả mã **L11-2-08**, sau ví dụ tính tay. Trong sơ đồ, minh họa bằng bước thật \(A\to B\) của **L11-2-11**, rồi tô ô \(F\) khi (f) cập nhật cặp đã thử ở đó. Diễn đạt lập kế hoạch nền là “cập nhật giá trị ở một trạng thái khác trước lần tác tử quay lại đó” để khớp với điều kiện chọn cặp đã thử. Ở **L11-2-16**, dùng mũi tên từ \(0{,}5\) vừa ghi ở hàng (d) đến \(0{,}5\) được đọc ở hàng (f), và ghi \(0{,}225\) ứng với thứ tự lấy mẫu đã nêu. Ở **L11-2-12**, hiện câu đảo thứ tự trước khi hiện \(0{,}10125\) để lớp có thời gian dự đoán.

4. **Giữ xác suất trượt trong ví dụ đổi cửa.** Ở **L11-2-14**, đổi nhãn cột “môi trường mới” thành “kết cục khi đi đúng trong môi trường mới”. Ở **L11-2-09**, sửa ô “bước thật: sang \(C\)” thành “thử \(\rightarrow\) ở \(B\), sang \(C\) với xác suất \(0{,}8\)”, rồi ghi “(e) cập nhật theo kết cục quan sát”. Tiền thưởng làm hành động đi phải trở thành lựa chọn tham lam với bảng \(Q\) vừa tính. Việc phát hiện lối mở vẫn phụ thuộc vào lần thử thật.

5. **Nói rõ mỗi đường cong đo đại lượng gì.** Ở **L11-2-04**, ghi cạnh \(0{,}2828\) “độ lệch chuẩn của \(\hat p\) qua các nhóm hai lần thử”. Chênh lệch quan sát trong lượt minh họa là \(|0{,}5-0{,}8|=0{,}3\). Ở **L11-2-15**, đưa hai ý từ ghi chú lên trang: \(y_{s'}=\gamma\max_{a'}Q(s',a')\) là giá trị nhánh có phương sai \(1\) theo giả thiết, và \(\alpha_j=1/j\) biến \(Q_k\) thành trung bình của \(k\) mục tiêu mẫu. Ở **L11-2-19**, ghi trục dọc “RMSE so với mục tiêu kỳ vọng của mô hình”. Có thể đánh dấu phương pháp kỳ vọng bằng một chấm tại \((1;0)\) và một dải chú thích “đang tính đủ \(b\) nhánh” trước mốc đó. Nếu giữ bậc xám, ghi rõ mức \(1\) là sai số ban đầu giả định. Khi chốt hình, nhắc lại rằng \(C\) thêm dữ liệu thật để ước lượng xác suất, còn \(k\) thêm lượt rút để ước lượng mục tiêu trên mô hình đang dùng. [Sutton và Barto, §8.5, Hình 8.7](https://www.incompleteideas.net/book/bookdraft2018mar21.pdf)

## Chấm điểm trên thang 10

| Tiêu chí | Điểm |
|---|---:|
| Mạch dẫn dắt | 8,5 |
| Trực quan hóa | 9 |
| Liên kết ví dụ–toán | 8,5 |
| Cân bằng trực giác–chứng minh | 8 |
| Từ lý thuyết đến thuật toán | 8,5 |
