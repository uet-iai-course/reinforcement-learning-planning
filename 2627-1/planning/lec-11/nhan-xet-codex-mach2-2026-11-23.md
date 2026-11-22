# Nhận xét của Codex: mạch 2 "Tính bất định của môi trường và lập kế hoạch nền", Bài 11 (2026-11-23)

- Nguồn: `codex exec` (gói ChatGPT), model mặc định của cấu hình Codex, mức suy luận high; chạy bằng `tools/deck/codex_review.py`.
- Bản được nhận xét: `2627-1/lecture-11-lap-ke-hoach-dua-tren-mo-hinh.html` tại `2f7f616` cộng thay đổi chưa commit; 17 trang (L11-2-00, L11-2-03, L11-2-06, L11-2-13, L11-2-04, L11-2-07, L11-2-16, L11-2-17, L11-2-08, L11-2-11, L11-2-12, L11-2-18, L11-2-14, L11-2-09, L11-2-10, L11-2-15, L11-2-19).
- Vòng sau chỉnh sửa; nhận xét trước: `nhan-xet-codex-mach2-2026-11-22-vong5.md`.
- Điểm: Mạch dẫn dắt 9,0; Trực quan hóa 9,5; Liên kết ví dụ–toán 9,0; Cân bằng trực giác–chứng minh 9,0; Từ lý thuyết đến thuật toán 9,0. Đạt điều kiện dừng (mọi tiêu chí ≥ 9).
- Prompt:

```text
Xem phần "Tính bất định của môi trường và lập kế hoạch nền" (mạch 2) của bài giảng https://courses.iaidev.com/reinforcement-learning-planning/2627-1/lecture-11-lap-ke-hoach-dua-tren-mo-hinh.html#/2

Phần này đã được chỉnh sửa theo nhận xét lần trước (tệp `nhan-xet-truoc.md`). Hãy nhận xét bản sau chỉnh sửa: đề xuất nào đã được thực hiện và thực hiện tốt đến đâu, còn điều gì cần sửa.

Hãy phân tích dưới góc nhìn của sinh viên để gợi ý cách trình bày tốt hơn, trực quan hơn.

---
Ảnh đính kèm là 17 trang của phần này, đúng thứ tự trình chiếu (L11-2-00, L11-2-03, L11-2-06, L11-2-13, L11-2-04, L11-2-07, L11-2-16, L11-2-17, L11-2-08, L11-2-11, L11-2-12, L11-2-18, L11-2-14, L11-2-09, L11-2-10, L11-2-15, L11-2-19), chụp từ bản hiện tại, có thể mới hơn trang web. Tệp `mach.md` trong thư mục làm việc chứa văn bản, công thức (TeX) và ghi chú giảng viên của từng trang. Đọc theo ảnh; dùng `mach.md` để đọc chính xác công thức. Ảnh chụp trạng thái cuối của mỗi trang, khi mọi lượt bấm đã hiện; trong `mach.md`, ⟨bấm k⟩ đánh dấu phần hiện ở lượt bấm thứ k của trang.
Khi nêu vấn đề hoặc đề xuất, ghi mã trang (ví dụ L11-2-06). Viết báo cáo bằng tiếng Việt, định dạng Markdown; hình đề xuất thì mô tả bằng lời (thành phần, số liệu, chú thích).
Cuối báo cáo, chấm điểm phần này trên thang 10 theo năm tiêu chí, ghi đúng một bảng Markdown hai cột `Tiêu chí | Điểm`, mỗi tiêu chí một dòng, điểm là một số (ví dụ 8,5): Mạch dẫn dắt; Trực quan hóa; Liên kết ví dụ–toán; Cân bằng trực giác–chứng minh; Từ lý thuyết đến thuật toán.
```

---
# Nhận xét mạch 2 — Tính bất định của môi trường và lập kế hoạch nền

Bản sửa đã xử lý tốt góp ý quan trọng nhất của vòng trước. Ở **L11-2-08**, sinh viên có thể đọc giả mã và xác định cặp nào được dùng để lập kế hoạch, mô hình lưu gì ở bước (e), và bước (f) lấy mẫu ra sao. Điểm còn vướng là khi rời trang thuật toán, sinh viên vẫn phải tự suy ra ví dụ đang dùng cách lưu nào. Hai chỉnh sửa có tác động lớn nhất là **gắn tên mô hình ngay tại chỗ tính** và **hiện bước (e) giữa cập nhật thật và cập nhật mô phỏng**.

Tôi lấy 17 ảnh theo thứ tự đính kèm làm bản chuẩn, dùng `mach.md` để kiểm tra công thức, ghi chú và các lượt bấm. Trang bài giảng trực tuyến không tải được trong lần kiểm tra này. [Nhận xét lần trước](/tmp/claude-1000/-data-tqlong-lectures/fd411c55-a86c-4518-a9f0-a6d4fde11419/scratchpad/lec11/codex-m2-v6/nhan-xet-truoc.md) · [Văn bản và ghi chú giảng viên](/tmp/claude-1000/-data-tqlong-lectures/fd411c55-a86c-4518-a9f0-a6d4fde11419/scratchpad/lec11/codex-m2-v6/mach.md)

## Từ quan sát đến một vòng Dyna-Q

**L11-2-00, L11-2-03, L11-2-06 — Câu hỏi mở được trả lời bằng một phép tính nhìn thấy được.** Dải \(F\to K\to Z\) cho sinh viên thấy vì sao lần đi qua \(F\) chưa làm \(Q(F,\rightarrow)\) tăng. Trang kế tiếp dùng nét đứt cho mẫu mô phỏng, đánh dấu ô \(K\) được đọc và ô \(F\) được ghi. Nhờ vậy, mục tiêu \(0{,}45\) và giá trị mới \(0{,}225\) có vai trò rõ ràng. Vướng mắc nằm ở cuối **L11-2-06**, khi hình vừa dùng một mô hình học được từ bốn cặp, còn Thuật toán 11.3 nói mô hình xác định ở mọi cặp. Nên đặt câu nối ngay trên trang này: “Để làm phép cập nhật vừa rồi, ta chỉ cần mô hình tại \((F,\rightarrow)\). Mệnh đề hội tụ ở trang sau xét toàn bộ bảng \(Q\).” Hiện sinh viên phải chờ đến **L11-2-07** mới thấy lời giải thích đó.

**L11-2-07, L11-2-08, L11-2-10 — Đã sửa tốt giả mã, còn thiếu nhãn ở bảng tính tay.** **L11-2-08** đã thực hiện cả hai đề xuất cụ thể của vòng trước. Bước (f) chọn trạng thái có cặp trong `Model`, rồi chọn hành động đã lưu tại đó. Hai dòng cuối chỉ rõ cách ghi đè và cách tăng số đếm, đồng thời nói rõ mô hình đếm rút cả \((R,S')\) theo tần suất. Cách viết này đủ để sinh viên biết ô vừa đến lần đầu hay ô kết thúc \(Z\) chưa có cặp để chọn. Ở **L11-2-07**, hai thẻ đã phân biệt rất rõ quan sát ① \((0,A)\) và ② \((0,B)\), nhưng tiêu đề cột vẫn chỉ ghi “mô hình sau (e)”. Nên đổi thành **“Kết cục gần nhất sau (e)”** và chốt ở lượt bấm 3 rằng hai cách lưu cho cùng hai phép tính tại bước 5 vì \((F,\rightarrow)\) và \((K,\rightarrow)\) đều mới được thử một lần. Khi hai quan sát ① và ② xuất hiện lại thành hai nhánh ở **L11-2-10**, sinh viên sẽ hiểu vì sao lần này cả hai được giữ.

**L11-2-16, L11-2-17, L11-2-12 — Hình đã giải thích được “lập kế hoạch nền”, còn thiếu một thao tác trong lời giải.** Chấm ở \(B\) và viền cam ở \(F\) trên **L11-2-17** là cách diễn đạt tốt nhất của phần này về vị trí tác tử và vị trí cập nhật. Hai ô đóng khung trên **L11-2-16** và **L11-2-12** cho thấy giá trị vừa ghi được đọc ngay ở hàng sau. Đặc biệt, **L11-2-12** dành lượt bấm 5 cho câu hỏi đảo thứ tự và lượt bấm 6 cho đáp án \(0{,}10125\), tạo đủ khoảng dừng để sinh viên tự tính. Góp ý hiện bước (e) vẫn chưa được đưa vào bảng lời giải. Ngay sau hàng (d), thêm một dòng nền trung tính **“(e) Ghi lại \(\mathrm{Model}(A,\rightarrow)=(0,B)\)”**, rồi mới hiện hai hàng (f). Có thể làm tương tự trên **L11-2-16**, nơi \((K,\rightarrow)\mapsto(+1,Z)\) được thêm vào mô hình và được gọi lại ở lượt (f) thứ hai.

## Hội tụ, bất định và môi trường đổi cửa

**L11-2-13, L11-2-18 — Đã trình bày được phạm vi bảo đảm, còn một điều kiện dễ bị đọc sai.** Hình hai hàng trên **L11-2-13** đặt \(0{,}6604\) cạnh môi trường có trượt và \(0{,}729\) cạnh mô hình. Đường \(A\to B\to F\to K\to Z\) cho thấy ba lần chiết khấu đến phần thưởng \(+1\). Điều kiện mô hình đầy đủ và cố định đã có dưới hình. Góp ý còn lại là đưa cụm **“Mô hình giả định giữ kết cục gần nhất, đầy đủ và cố định”** sát số \(0{,}729\), đồng thời gọi \(\hat q_*\) là hàm giá trị hành động tối ưu của mô hình \((\hat p,\hat r)\). Như vậy sinh viên dễ thấy số này đến từ một mô hình giả định, trong khi lượt thật đầu tiên mới cung cấp bốn cặp. Ở **L11-2-18**, lịch \(\alpha_j=1/j\) theo từng cặp và ví dụ ghi đè đã đủ cụ thể. Hàng “mọi cặp chọn vô hạn lần” nên ghi **“Chưa được bảo đảm chỉ từ bước (f). Còn cần tác tử thử được mọi cặp và tiếp tục lập kế hoạch.”** Cách diễn đạt này phân biệt phạm vi của định lý với những gì có thể kết luận từ một lượt chạy hữu hạn.

**L11-2-04 — Góp ý đặt hai quy trình lấy dữ liệu cạnh nhau vẫn chưa được thực hiện.** Đồ thị đã làm rõ đường ngang \(0{,}4\) và đường giảm \(0{,}4/\sqrt C\). Tuy nhiên, sinh viên thấy \(C=2\) ở cả lượt mê cung và đồ thị nên dễ áp độ lệch chuẩn \(0{,}2828\) cho chính lượt có sai lệch \(0{,}3\). Nên dùng hai ô nhỏ ngay cạnh mốc \(C=2\). Ô thứ nhất vẽ “trượt → thử lại → sang \(B\)”, ghi \(\hat p=0{,}5\) và **“Sai lệch tuyệt đối của lượt này \(=0{,}3\)”**. Ô thứ hai ghi **“Ấn định trước đúng hai lần thử”**, dùng ba cột tại \(\hat p=0;\,0{,}5;\,1\) với xác suất \(0{,}04;\,0{,}32;\,0{,}64\), rồi nối ô này với điểm **“Độ lệch chuẩn \(=0{,}2828\)”** trên đường cong. Giữ dòng chứng minh Bernoulli và thêm một nhãn nhỏ cho biết trục tung vẽ căn bậc hai của phương sai trong công thức.

**L11-2-14, L11-2-09 — Hình đổi cửa và phép tính thưởng đã rõ, quy tắc triển khai Dyna-Q+ vẫn thiếu trên màn hình.** Hai mê cung cùng bố cục làm nổi bật việc lối cũ đóng và lối mới mở. Ngay sau đó, phép tính \(0{,}54\to0{,}64>0{,}6\) giải thích vì sao hành động tham lam tại \(B\) có thể đổi. Sơ đồ cũng đã cho thấy cả lần đi đúng lẫn lần trượt đều đặt lại \(\ell\). Các đề xuất còn mở đều có thể xử lý trên **L11-2-09**. Gắn nhãn **“Ví dụ dùng mô hình giữ kết cục gần nhất”**, viết **“sang \(C\), \(0{,}8\), ghi \((0,C)\)”** trên nhánh trên để đối xứng với nhánh trượt, và cho sơ đồ xuất hiện cùng hoặc sau lượt bấm hiện \(0{,}64\). Nếu dùng trang này để sinh viên tự cài Dyna-Q+, đưa thêm một dòng từ ghi chú lên màn hình. Ở trạng thái đã gặp, bước (f) được xét cả hành động chưa thử, với kết cục khởi tạo là ở lại trạng thái đó và thưởng \(0\). [Sutton và Barto, §8.3, tr. 168](https://www.andrew.cmu.edu/course/10-703/textbook/BartoSutton.pdf#page=190)

## Từ cây hai nhánh đến sai số theo ngân sách

**L11-2-10, L11-2-15 — Đã có công thức trung bình mẫu, còn thiếu một bước đệm trước chứng minh.** Hai cây ở **L11-2-10** cho thấy ngay sự đánh đổi giữa hai lần đánh giá để tính được \(0{,}45\) và một lần đánh giá để lấy \(0{,}54\) hoặc \(0{,}36\). **L11-2-15** đã hiện \(Q_k=\frac1k\sum_j y_{S'_j}\), nhưng ví dụ hai lần rút vẫn nằm trong ghi chú. Nên thêm một lượt bấm ở cuối **L11-2-10**. Giữ hai mục tiêu nhánh cố định, rút hai lần có hoàn lại, rồi hiện ba kết quả \(0{,}36;\,0{,}45;\,0{,}54\) với xác suất \(1/4;\,1/2;\,1/4\). Ghi \(\alpha_1=1,\ \alpha_2=1/2\) để sinh viên thấy vì sao \(Q_2\) là trung bình. Nhãn “giữ cố định hai mục tiêu nhánh” quan trọng vì nhánh quay lại \(A\) có thể đọc chính bảng \(Q\) đang được cập nhật trong một lần chạy Dyna-Q thực. Sang **L11-2-15**, tách lời chứng minh thành hai lượt bấm. Trước hết giữ bộ giá trị nhánh cố định để có \(\sigma^2/k\), sau đó lấy kỳ vọng qua các bộ giá trị nhánh có phương sai \(1\).

**L11-2-19 — Đồ thị đã gọi đúng đại lượng trên trục tung, còn hai chú thích cần chính xác hơn.** Trục tung ghi RMSE so với mục tiêu kỳ vọng **của mô hình**, và dòng cuối đã phân biệt đúng \(k\) lượt rút mô phỏng với \(C\) lần thử thật. Nên ghi thêm **“theo giả thiết phương sai \(1\) của Mệnh đề 11.15(b)”** cạnh điểm \(b=2,\ k=2,\ \mathrm{RMSE}=0{,}5\), vì sinh viên vừa thấy một cây hai nhánh cụ thể với hai mục tiêu chỉ cách nhau \(0{,}18\). Cạnh điểm xám \((1;0)\), ghi **“Tính chính xác mục tiêu kỳ vọng sau \(b\) lần đánh giá nhánh”**. Cụm “cho giá trị mới” hiện tại dễ làm sinh viên đồng nhất mục tiêu chính xác với giá trị \(Q\) sau cập nhật, vốn còn phụ thuộc vào bước học. Khi chốt hình, có thể quay lại một câu hỏi từ **L11-2-04**: “Nếu mô hình vẫn cho \(\hat p=0{,}5\), rút thêm nhiều lần có đưa xác suất đó về \(0{,}8\) không?” Đây là cách kiểm tra trực tiếp xem sinh viên đã hiểu hai nguồn sai số hay chưa.

## Chấm điểm trên thang 10

| Tiêu chí | Điểm |
|---|---:|
| Mạch dẫn dắt | 9 |
| Trực quan hóa | 9,5 |
| Liên kết ví dụ–toán | 9 |
| Cân bằng trực giác–chứng minh | 9 |
| Từ lý thuyết đến thuật toán | 9 |
