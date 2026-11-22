# Nhận xét của Codex: mạch 2 "Tính bất định của môi trường và lập kế hoạch nền", Bài 11 (2026-11-22)

- Nguồn: `codex exec` (gói ChatGPT), model mặc định của cấu hình Codex, mức suy luận high; chạy bằng `tools/deck/codex_review.py`.
- Bản được nhận xét: `2627-1/lecture-11-lap-ke-hoach-dua-tren-mo-hinh.html` tại `cdb80d4` cộng thay đổi chưa commit; 17 trang (L11-2-00, L11-2-03, L11-2-06, L11-2-13, L11-2-04, L11-2-07, L11-2-16, L11-2-17, L11-2-08, L11-2-11, L11-2-12, L11-2-18, L11-2-14, L11-2-09, L11-2-10, L11-2-15, L11-2-19).
- Vòng sau chỉnh sửa; nhận xét trước: `nhan-xet-codex-mach2-2026-11-22-vong3.md`.
- Điểm: Mạch dẫn dắt 9,0; Trực quan hóa 9,0; Liên kết ví dụ–toán 9,0; Cân bằng trực giác–chứng minh 8,5; Từ lý thuyết đến thuật toán 8,5. Chưa đạt điều kiện dừng (mọi tiêu chí ≥ 9).
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

Bản hiện tại đã trả lời trực quan câu hỏi mở của mạch. Khi tác tử đi từ \(F\) sang \(K\), giá trị ở \(K\) còn bằng 0. Khi tác tử nhận \(+1\) ở bước kế tiếp, mô hình cho phép dùng lại mẫu \(F\to K\) để cập nhật \(Q(F,\rightarrow)\) ngay. Dải ba ô ở **L11-2-03**, hình “đọc \(K\), ghi \(F\)” ở **L11-2-06** và hai bảng tính ở **L11-2-16, L11-2-12** giúp sinh viên theo được giá trị nào vừa đổi và được đọc ở đâu. Vướng mắc lớn nhất còn lại là nhận ra **mô hình đang lưu gì** mỗi khi bài chuyển giữa mô hình đếm và mô hình lưu kết cục gần nhất.

Tôi dùng 17 ảnh đính kèm làm bản chuẩn cho thứ tự và nội dung hiển thị, rồi đối chiếu công thức và ghi chú giảng viên trong `mach.md`. Trang web không tải được trong lần kiểm tra này, nên tôi chưa xác minh cách các thành phần lần lượt xuất hiện khi chiếu. [Nhận xét lần trước](/tmp/claude-1000/-data-tqlong-lectures/fd411c55-a86c-4518-a9f0-a6d4fde11419/scratchpad/lec11/codex-m2-v4/nhan-xet-truoc.md) · [Văn bản và ghi chú giảng viên](/tmp/claude-1000/-data-tqlong-lectures/fd411c55-a86c-4518-a9f0-a6d4fde11419/scratchpad/lec11/codex-m2-v4/mach.md)

## Các đề xuất lần trước đã được thực hiện đến đâu

1. **Câu hỏi mở có đủ dữ kiện ngay ở trang nội dung đầu tiên — L11-2-00, L11-2-03, L11-2-06.** Dải \(F\to K\to Z\) đã có hai phần thưởng \(0\), \(+1\) và cho thấy giá trị ở \(K\) đổi sau bước nào. Sang L11-2-06, mũi tên nét đứt chỉ đúng mẫu mô phỏng trả về để ghi \(0{,}225\) vào ô \(F\). Trang mở L11-2-00 vẫn làm nhiệm vụ định vị mạch. Đặt dải ở L11-2-03 là một lựa chọn hợp lý vì câu hỏi được gặp ngay ở trang kế tiếp.

2. **Hai cách lưu mô hình đã xuất hiện trên cùng dữ liệu, nhưng còn dễ đọc lẫn — L11-2-07, L11-2-08, L11-2-10.** Hàng thứ hai ở L11-2-07 đã gạch \((0,A)\), giữ \((0,B)\) và ghi \(A:1,\ B:1\). Cả hai cách lưu vẫn nằm trong cùng một ô của bảng. L11-2-08 đã thực hiện rõ phần quan trọng đối với cài đặt là rút **cả cặp** \((R,S')\) từ cùng một lần thử cũ. Cây ở L11-2-10 cũng đã đánh số hai quan sát, đủ để nối lại với L11-2-03.

3. **Điều kiện để cập nhật một ô và điều kiện hội tụ toàn bảng đã được phân biệt trên trang chiếu — L11-2-06, L11-2-07, L11-2-13, L11-2-17, L11-2-18.** Câu mở mới ở L11-2-07 giải quyết đúng thắc mắc vì sao Dyna-Q có thể lập kế hoạch khi mới biết bốn cặp. L11-2-17 đã dùng bước thật \(A\to B\) để minh họa cập nhật ở \(F\), nhưng vị trí tác tử ở \(B\) vẫn chỉ có trong đoạn văn. Ghi chú L11-2-07 vẫn nói Q-planning “không chạy được trên mô hình này”, dễ làm giảng viên lặp lại cách nói mà trang chiếu đã sửa.

4. **Hai cách lấy dữ liệu ở trang bất định đã được giải thích bằng lời — L11-2-04.** Trang đã ghi “lượt vừa quan sát”, nêu ba giá trị có thể có của \(\hat p\) khi ấn định hai lần thử, và giải thích vì sao lượt mê cung có lần thử thứ hai. Điểm còn khó khi nhìn nhanh là \(0{,}3\) nằm ở dòng mở, còn \(0{,}2828\) nổi bật trên hình. Sinh viên vẫn phải tự nhận ra một số là sai lệch tuyệt đối của một lượt, số kia là độ lệch chuẩn qua nhiều nhóm thử.

5. **Ví dụ thử lại lối mở đã có đủ hai kết cục — L11-2-14, L11-2-09.** Chuỗi \(0{,}64>0{,}6\), chọn đi phải, rẽ nhánh xác suất \(0{,}8/0{,}2\), rồi ghi quan sát và đặt \(\ell\) về 0 làm rõ tác dụng của thưởng thăm dò. Đây là thay đổi hiệu quả nhất ở đoạn Dyna-Q+. Quy tắc cho phép lập kế hoạch với hành động chưa thử vẫn nằm trong ghi chú.

6. **Phần sai số đã dùng chung ký hiệu và có các mốc ngân sách cụ thể — L11-2-10, L11-2-15, L11-2-19.** Cây đã ghi \(\bar y=0{,}45\), phần chứng minh đã có hai bước, và đồ thị đánh dấu cả \((1;0)\), \(b=2,\ k=2\) lẫn \(b=100,\ k=10\). Mắt xích còn thiếu trên trang chứng minh là \(\alpha_j=1/j\) biến \(Q_k\) thành trung bình của \(k\) mục tiêu mẫu như thế nào. Công thức đó hiện có trong ghi chú.

## Những chỗ nên sửa tiếp

1. **Đặt tên mô hình ngay tại nơi sinh viên phải chọn cách đọc dữ liệu — L11-2-03, L11-2-07, L11-2-08, L11-2-10.** Ở L11-2-07, đặt hai thẻ dưới cùng hai quan sát ① \((0,A)\), ② \((0,B)\). Thẻ **“Đếm kết cục”** giữ hai dòng, mỗi dòng có số đếm 1 và xác suất \(1/2\). Thẻ **“Giữ kết cục gần nhất — dùng để tính tay”** gạch dòng ① và giữ dòng ②. Dùng lại tên và số thứ tự đó trên cây L11-2-10. Cách vẽ này cũng nối được hai công thức ở L11-2-03 với giả mã L11-2-08. \(\hat p(s'|s,a)\) tóm tắt tần suất đến trạng thái kế, \(\hat r(s,a)\) tóm tắt thưởng trung bình, còn khi sinh mẫu thì bảng đếm theo kết cục \((R,S')\) giữ thưởng đi cùng trạng thái kế của lần quan sát đó.

2. **Cho sinh viên theo dõi riêng vị trí tác tử, ô \(Q\) và phạm vi của mệnh đề — L11-2-06, L11-2-07, L11-2-13, L11-2-17, L11-2-18.** Trong sơ đồ Dyna, đặt chấm “tác tử đang ở \(B\)” sau mũi tên thật \(A\to B\), rồi tô viền ô \(F\) với nhãn “(f) ghi \(Q(F,\rightarrow)\)”. Có thể định nghĩa lập kế hoạch nền là dùng mô hình giữa các bước thật để cập nhật giá trị, kể cả ở trạng thái khác vị trí hiện tại. Ở L11-2-06, ghi ngay trong thuật toán “chọn một cặp có mô hình” và sửa ghi chú L11-2-07 cho nhất quán. Ở L11-2-13, gắn nhãn **“giả sử đã có mô hình đủ các cặp và giữ cố định”** ngay cạnh \(0{,}729\), để sinh viên biết đây là một tình huống giả định sau khi đã có đủ dữ liệu. Trong bảng L11-2-18, có thể ghi Robbins–Monro **theo số lần cập nhật từng cặp**, kèm ví dụ \(\alpha_j=1/j\), để điều kiện có thể chuyển thành một bộ đếm trong cài đặt.

3. **Đặt hai quy trình lấy dữ liệu cạnh nhau — L11-2-04, L11-2-19.** Bên trái vẽ “trượt, rồi sang \(B\)” và ghi \(\hat p=0{,}5\), sai lệch tuyệt đối \(0{,}3\). Bên phải đặt ba cột cho các nhóm **đúng hai lần thử**, tại \(\hat p=0;\ 0{,}5;\ 1\), có xác suất tương ứng \(0{,}04;\ 0{,}32;\ 0{,}64\). Ghi dưới ba cột “độ lệch chuẩn giữa các nhóm \(=0{,}2828\)”. Có thể hiện hình nhỏ này trước đồ thị theo \(C\). Khi kết mạch ở L11-2-19, nhắc lại bằng hai câu ngắn. Thêm \(C\) giúp ước lượng xác suất của môi trường. Thêm \(k\) giúp ước lượng mục tiêu của mô hình đang dùng.

4. **Đưa quy tắc Dyna-Q+ cần để cài đặt lên trang chiếu — L11-2-14, L11-2-09.** Dưới sơ đồ hai nhánh, ghi “Thưởng \(0{,}2\) chỉ cộng trong (f). Mỗi lần thử thật đặt lại \(\ell\), kể cả khi trượt.” Có thể chú thích ngay trên nhánh \(0{,}2\) rằng mô hình lưu kết cục gần nhất sẽ ghi lại \((0,B)\). Như vậy sinh viên thấy lần thử thật có thể xảy ra mà lối mới vẫn chưa được phát hiện. Thêm một dòng ở bước (f) về các hành động chưa thử tại trạng thái đã gặp, với mô hình khởi tạo trả về cùng trạng thái và thưởng 0. [Sutton và Barto, §8.3](https://www.andrew.cmu.edu/course/10-703/textbook/BartoSutton.pdf#page=190)

5. **Dùng lại cây hai nhánh để dẫn vào chứng minh RMSE — L11-2-10, L11-2-15, L11-2-19.** Trước khi hiện giả thiết phương sai 1, cho lớp rút hai lần có hoàn lại từ hai mục tiêu cố định \(0{,}54\) và \(0{,}36\). Trung bình có thể là \(0{,}54\), \(0{,}45\) hoặc \(0{,}36\). Sau đó viết ngay trên trang \(Q_k=\frac1k\sum_{j=1}^k y_{S'_j}\) do \(\alpha_j=1/j\). Với các giá trị nhánh giữ cố định, phương sai của trung bình mẫu là \(\sigma^2/k\) quanh \(\bar y\). Giả thiết phương sai 1 đi vào bước sau, khi lấy trung bình qua nhiều bộ giá trị nhánh để được \(\mathbb E[\sigma^2]=1-1/b\). Trên đồ thị, có thể rút chú thích thành hai quyết định đọc được tại chỗ. Với hai nhánh và hai lượt đánh giá, tính đủ nhánh cho đúng mục tiêu mô hình. Với 100 nhánh và ngân sách 10 lượt đánh giá, lấy mẫu đã cho một ước lượng có RMSE \(0{,}3146\) theo giả thiết của mệnh đề. [Sutton và Barto, §8.5, Hình 8.7](https://www.andrew.cmu.edu/course/10-703/textbook/BartoSutton.pdf#page=196)

## Chấm điểm trên thang 10

| Tiêu chí | Điểm |
|---|---:|
| Mạch dẫn dắt | 9 |
| Trực quan hóa | 9 |
| Liên kết ví dụ–toán | 9 |
| Cân bằng trực giác–chứng minh | 8,5 |
| Từ lý thuyết đến thuật toán | 8,5 |
