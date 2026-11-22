# Nhận xét của Codex: mạch 2 "Tính bất định của môi trường và lập kế hoạch nền", Bài 11 (2026-11-22)

- Nguồn: `codex exec` (gói ChatGPT), model mặc định của cấu hình Codex, mức suy luận high; chạy bằng `tools/deck/codex_review.py`.
- Bản được nhận xét: `2627-1/lecture-11-lap-ke-hoach-dua-tren-mo-hinh.html` tại `2f7f616`; 17 trang (L11-2-00, L11-2-03, L11-2-06, L11-2-13, L11-2-04, L11-2-07, L11-2-16, L11-2-17, L11-2-08, L11-2-11, L11-2-12, L11-2-18, L11-2-14, L11-2-09, L11-2-10, L11-2-15, L11-2-19).
- Vòng sau chỉnh sửa; nhận xét trước: `nhan-xet-codex-mach2-2026-11-22-vong4.md`.
- Điểm: Mạch dẫn dắt 9,0; Trực quan hóa 9,5; Liên kết ví dụ–toán 9,0; Cân bằng trực giác–chứng minh 9,0; Từ lý thuyết đến thuật toán 8,5. Chưa đạt điều kiện dừng (mọi tiêu chí ≥ 9).
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

Bản sửa giúp sinh viên theo dõi được quá trình phần thưởng lan ngược qua bảng \(Q\). Ở **L11-2-03**, tác tử đã rời \(F\) khi giá trị ở \(K\) còn bằng 0. Đến **L11-2-06**, hình “đọc \(K\), ghi \(F\)” cho thấy cách dùng mẫu đã lưu để cập nhật \(Q(F,\rightarrow)\) lên \(0{,}225\). Hai bổ sung hiệu quả nhất là cặp thẻ so sánh cách lưu mô hình ở **L11-2-07** và hình tác tử đang ở \(B\) trong khi cập nhật ô \(F\) ở **L11-2-17**. Chỗ đáng sửa nhất là làm rõ mỗi lần bài chuyển sang một mô hình khác, nhất là khi đi từ giả mã Dyna-Q sang ví dụ mê cung đổi cửa.

Tôi dùng 17 ảnh làm bản chuẩn về nội dung và thứ tự trình chiếu, đối chiếu công thức và ghi chú trong `mach.md`. Trang web không tải được trong lần kiểm tra này, nên nhận xét về bố cục dựa trên ảnh tĩnh. [Nhận xét lần trước](/tmp/claude-1000/-data-tqlong-lectures/fd411c55-a86c-4518-a9f0-a6d4fde11419/scratchpad/lec11/codex-m2-v5/nhan-xet-truoc.md) · [Văn bản và ghi chú giảng viên](/tmp/claude-1000/-data-tqlong-lectures/fd411c55-a86c-4518-a9f0-a6d4fde11419/scratchpad/lec11/codex-m2-v5/mach.md)

## Các góp ý đã được thực hiện đến đâu

- **Hai cách lưu mô hình — L11-2-03, L11-2-07, L11-2-08, L11-2-10.** Góp ý tách hai cách lưu đã được thực hiện tốt. Hai thẻ ở L11-2-07 dùng chung quan sát ① \((0,A)\) và ② \((0,B)\). Thẻ đếm giữ cả hai với xác suất \(1/2\) mỗi kết cục. Thẻ tính tay gạch quan sát đầu và giữ quan sát sau. Số ① và ② xuất hiện lại trên cây ở L11-2-10, giúp sinh viên nhận ra dữ liệu cũ. Phần còn thiếu là một nhãn ngay trên cột “mô hình sau (e)” cho biết bảng đang dùng **kết cục gần nhất**. Cũng nên đưa lên trang chiếu nhận xét hiện nằm trong ghi chú L11-2-07. Hai cách lưu cho cùng phép tính ở bước 5 vì \((F,\rightarrow)\) và \((K,\rightarrow)\) đều mới được thử một lần.

- **Lập kế hoạch nền và thứ tự cập nhật — L11-2-16, L11-2-17, L11-2-12.** Hình nhỏ ở L11-2-17 thực hiện đúng góp ý lần trước. Chấm tại \(B\) cho biết tác tử đang ở đâu, còn viền cam tại \(F\) cho biết ô nào được sửa. Hai bảng tính tiếp nối hình này bằng cách đóng khung giá trị vừa ghi và giá trị được đọc ngay sau đó. Câu hỏi đảo thứ tự ở L11-2-12 kiểm tra đúng cơ chế: \(Q(B,\downarrow)\) bằng \(0{,}10125\) nếu cập nhật \(B\) trước, và \(0{,}2025\) nếu cập nhật \(F\) trước. Nên chèn một dòng ngắn giữa (d) và hai lượt (f) ở L11-2-12 với nội dung “(e) ghi lại \((A,\rightarrow)\mapsto(0,B)\)”. Sinh viên sẽ thấy đủ trình tự thuật toán ngay cả khi bước đó giữ nguyên dữ liệu đã lưu.

- **Phạm vi bảo đảm hội tụ — L11-2-06, L11-2-07, L11-2-13, L11-2-18.** Câu mở và ghi chú L11-2-07 nay phân biệt đúng một cập nhật trên cặp đã có mô hình với bảo đảm hội tụ của toàn bảng. L11-2-13 đã ghi giả định mô hình đủ các cặp và được giữ cố định. L11-2-18 đã đưa lịch \(\alpha_j=1/j\) theo số lần cập nhật **từng cặp** lên slide. Hàng “mọi cặp chọn vô hạn lần” vẫn dễ bị đọc như một giả thiết chắc chắn bị vi phạm. Nên ghi “(f) chọn trong các cặp đã thử. Độ phủ về lâu dài phụ thuộc vào việc tác tử có thử được mọi cặp và tiếp tục lập kế hoạch hay không.” Ở L11-2-13, đặt nhãn **“Mô hình kết cục gần nhất giả định, đầy đủ và cố định”** sát số \(0{,}729\), đồng thời gọi \(\hat q_*\) là giá trị tối ưu của mô hình với cả \((\hat p,\hat r)\). Như vậy sinh viên dễ phân biệt kết quả \(0{,}729\) với giá trị \(0{,}6604\) của môi trường có trượt.

- **Hai cách lấy dữ liệu ở trang bất định — L11-2-04, L11-2-19.** L11-2-04 có đủ dữ kiện và đã nêu rõ vì sao \(C=2\) trong lượt mê cung phụ thuộc vào lần trượt đầu. Góp ý đặt hai quy trình cạnh nhau vẫn chưa được thực hiện trên hình. Con số \(0{,}3\) nằm ở dòng mở, còn \(0{,}2828\) nằm dưới biểu đồ. Nên đặt hai cụm ngay trên đồ thị. Cụm trái vẽ chuỗi “trượt \(\to\) sang \(B\)” và ghi **“Sai lệch tuyệt đối của lượt này: \(0{,}3\)”**. Cụm phải dùng ba cột tại \(\hat p=0;\,0{,}5;\,1\), cao tương ứng \(0{,}04;\,0{,}32;\,0{,}64\), với nhãn **“Độ lệch chuẩn qua các nhóm có đúng hai lần thử: \(0{,}2828\)”**. Dùng câu “hai lần thử được ấn định trước” làm nhãn cho đường \(0{,}4/\sqrt C\) tại mốc \(C=2\). Dòng cuối L11-2-19 đã nối lại đúng hai vai trò của \(C\) và \(k\).

- **Mê cung đổi cửa và Dyna-Q+ — L11-2-14, L11-2-09.** Hình hai mê cung giữ cùng vị trí các ô, nên sinh viên đối chiếu được ngay cửa \(F\)–\(K\) đóng và lối \(B\)–\(C\) mở. L11-2-09 đã thể hiện rõ thưởng chỉ cộng ở (f) và cả hai kết cục thử thật đều đặt lại \(\ell\). Nên ghi \((0,C)\) ngay trên nhánh xác suất \(0{,}8\) để đối xứng với \((0,B)\) ở nhánh \(0{,}2\), và gắn nhãn **“Ví dụ dùng mô hình giữ kết cục gần nhất”**. Nhãn này quan trọng vì với bảng đếm tích lũy, một lần sang \(C\) chỉ thêm một quan sát vào lịch sử. Quy tắc Dyna-Q+ cho hành động chưa thử vẫn nằm trong ghi chú. Có thể thêm dưới sơ đồ một dòng về bước (f): tại trạng thái đã gặp, cho phép chọn cả hành động chưa thử và khởi tạo kết cục mô phỏng là ở lại trạng thái đó với thưởng 0. [Sutton và Barto, §8.3, tr. 168](https://www.andrew.cmu.edu/course/10-703/textbook/BartoSutton.pdf#page=190)

- **Từ cây hai nhánh đến chứng minh RMSE — L11-2-10, L11-2-15, L11-2-19.** L11-2-15 đã đưa \(Q_k=\frac1k\sum_j y_{S'_j}\) lên slide. Đây là bước tiến rõ so với lần trước, nhưng sinh viên vẫn gặp nhiều giả thiết mới cùng lúc. Có thể đưa ví dụ hai lần rút từ ghi chú L11-2-10 lên màn hình trước mệnh đề. Vẽ hai lượt rút có hoàn lại từ các mục tiêu \(0{,}54\) và \(0{,}36\), rồi hiện ba kết quả trung bình \(0{,}54;\,0{,}45;\,0{,}36\) với xác suất \(1/4;\,1/2;\,1/4\). Dòng \(\alpha_1=1,\ \alpha_2=1/2\) giải thích ngay vì sao lần cập nhật thứ hai lấy trung bình. Sau đó mới chuyển sang hai bước của chứng minh: giữ bộ giá trị nhánh cố định để có \(\sigma^2/k\), rồi lấy trung bình qua các bộ giá trị nhánh có phương sai 1. Ở L11-2-19, ghi ngay cạnh điểm \(b=2,\ k=2\) rằng RMSE \(0{,}5\) dùng giả thiết phương sai 1 của mệnh đề. Cạnh điểm xám \((1;0)\), dùng nhãn “đã tính đúng **mục tiêu kỳ vọng của mô hình**” để làm rõ đại lượng được tính chính xác.

## Chỉnh sửa ưu tiên để sinh viên tự triển khai được

**L11-2-08** nên phát biểu bước (f) theo đúng điều kiện có thể kiểm tra trong mã. Chọn một trạng thái có ít nhất một hành động đã lưu trong `Model`, rồi chọn một hành động đã lưu tại đó. “Trạng thái đã gặp” có thể bao gồm ô vừa đến lần đầu hoặc ô kết thúc \(Z\), nơi chưa có hành động nào để rút. Ngay dưới giả mã, cho hai dòng tương ứng với hai thẻ ở **L11-2-07**: **“Giữ kết cục gần nhất: (e) ghi đè, (f) đọc kết cục đã lưu”** và **“Đếm kết cục: (e) tăng số đếm của \((R,S')\), (f) rút cả \((R,S')\) theo tần suất”**. Khi gặp lại cây ở **L11-2-10**, sinh viên sẽ thấy ngay vì sao mô hình có hai nhánh và nhánh nào được đánh giá trong một lần cập nhật mẫu.

## Chấm điểm trên thang 10

| Tiêu chí | Điểm |
|---|---:|
| Mạch dẫn dắt | 9 |
| Trực quan hóa | 9,5 |
| Liên kết ví dụ–toán | 9 |
| Cân bằng trực giác–chứng minh | 9 |
| Từ lý thuyết đến thuật toán | 8,5 |
