# Nhận xét của Codex: mạch 2 "Tính bất định của môi trường và lập kế hoạch nền", Bài 11 (2026-11-22)

- Nguồn: `codex exec` (gói ChatGPT), model mặc định của cấu hình Codex, mức suy luận high; chạy bằng `tools/deck/codex_review.py`.
- Bản được nhận xét: `2627-1/lecture-11-lap-ke-hoach-dua-tren-mo-hinh.html` tại `9096f20` cộng thay đổi chưa commit; 13 trang (L11-2-00, L11-2-03, L11-2-06, L11-2-13, L11-2-04, L11-2-07, L11-2-08, L11-2-11, L11-2-12, L11-2-14, L11-2-09, L11-2-10, L11-2-15).
- Điểm: Mạch dẫn dắt 7,5; Trực quan hóa 7,5; Liên kết ví dụ–toán 8,0; Cân bằng trực giác–chứng minh 7,0; Từ lý thuyết đến thuật toán 8,0. Chưa đạt điều kiện dừng (mọi tiêu chí ≥ 9).
- Prompt:

```text
Xem phần "Tính bất định của môi trường và lập kế hoạch nền" (mạch 2) của bài giảng https://courses.iaidev.com/reinforcement-learning-planning/2627-1/lecture-11-lap-ke-hoach-dua-tren-mo-hinh.html#/2

Hãy phân tích dưới góc nhìn của sinh viên để gợi ý cách trình bày tốt hơn, trực quan hơn.

---
Ảnh đính kèm là 13 trang của phần này, đúng thứ tự trình chiếu (L11-2-00, L11-2-03, L11-2-06, L11-2-13, L11-2-04, L11-2-07, L11-2-08, L11-2-11, L11-2-12, L11-2-14, L11-2-09, L11-2-10, L11-2-15), chụp từ bản hiện tại, có thể mới hơn trang web. Tệp `mach.md` trong thư mục làm việc chứa văn bản, công thức (TeX) và ghi chú giảng viên của từng trang. Đọc theo ảnh; dùng `mach.md` để đọc chính xác công thức.
Khi nêu vấn đề hoặc đề xuất, ghi mã trang (ví dụ L11-2-06). Viết báo cáo bằng tiếng Việt, định dạng Markdown; hình đề xuất thì mô tả bằng lời (thành phần, số liệu, chú thích).
Cuối báo cáo, chấm điểm phần này trên thang 10 theo năm tiêu chí, ghi đúng một bảng Markdown hai cột `Tiêu chí | Điểm`, mỗi tiêu chí một dòng, điểm là một số (ví dụ 8,5): Mạch dẫn dắt; Trực quan hóa; Liên kết ví dụ–toán; Cân bằng trực giác–chứng minh; Từ lý thuyết đến thuật toán.
```

---
# Góp ý mạch 2 — Tính bất định của môi trường và lập kế hoạch nền

Ở góc nhìn sinh viên, phần dễ theo nhất là lúc một bước thật tới đích làm \(Q(K,\rightarrow)\) tăng, rồi một bước mô phỏng truyền giá trị về \(F\). Mê cung chung giúp nối được phép tính với đường đi. Chỗ dễ mất mạch nhất là khi cùng mê cung ấy lần lượt dùng mô hình đếm, mô hình lưu kết cục gần nhất và mô hình cũ sau khi đổi cửa. Tôi ưu tiên ghi rõ mô hình đang dùng ngay trên hình, cho thấy bảng \(Q\) thay đổi theo từng bước, và đưa những kết luận đang bị khuất trở lại vùng trình chiếu.

Báo cáo theo đúng thứ tự 13 ảnh, dùng `mach.md` để đối chiếu công thức và ghi chú giảng viên. Đường dẫn Bài 11 chưa tải được khi kiểm tra, nên nhận xét về bố cục dựa trên ảnh đính kèm. [Văn bản và ghi chú giảng viên](mach.md) · [Bản web Bài 11](https://courses.iaidev.com/reinforcement-learning-planning/2627-1/lecture-11-lap-ke-hoach-dua-tren-mo-hinh.html#/2)

## Từ năm bước thật đến một cập nhật mô phỏng

- **L11-2-00 — Mở bằng một câu hỏi trên mê cung.** Danh sách thuật ngữ mở đầu khó định hướng cho người mới. Có thể dùng hình nhỏ \(F\to K\to Z\), đánh dấu \(Z\) là đích và chỉ ghi \(Q(K,\rightarrow)=0{,}5\), \(Q(F,\rightarrow)=0\) sau lượt đầu của Q-learning. Hỏi lớp: “Tác tử đã đi qua \(F\). Sau khi nhận \(+1\) ở đích, làm sao cập nhật \(F\) ngay trong lượt này?” Giữ phép tính \(0{,}225\) để mở ở L11-2-06.
- **L11-2-03 — Cho sinh viên thấy một bước thật trở thành một lượt đếm.** Giữ mê cung và số thứ tự năm bước. Dùng cùng ký hiệu ①, ② trên hai nhánh của \((A,\rightarrow)\), ghi mỗi nhánh có số đếm \(1\), rồi hiện phép chia \(1/2\) ngay dưới hai nhánh. Ghi nhỏ “5 bước thật, 4 cặp đã thử” và “\(C=0\): chưa có ước lượng”. Đặt hai công thức \(\hat p\), \(\hat r\) cạnh ví dụ số tương ứng. Trong ảnh, công thức \(\hat r\) bị cắt ở mép dưới.
- **L11-2-06 — Làm rõ nguồn mẫu và ô được sửa.** Giữ mũi tên liền \(K\to Z\) cho bước thật, mũi tên đứt \(F\to K\) cho mẫu từ mô hình. Khi hiện mũi tên đứt, làm nổi \(Q(K,\rightarrow)=0{,}5\) là giá trị **được đọc**, rồi đổi \(Q(F,\rightarrow)\) từ \(0\) thành \(0{,}225\) để chỉ ô **được ghi**. Đặt ngay cạnh hình hai phép tính \(y=0+0{,}9\cdot0{,}5=0{,}45\) và \(Q_{\text{mới}}=0+0{,}5(0{,}45-0)=0{,}225\). Có thể dùng hai dòng này thay cho bảng một hàng để đủ chỗ hiện trọn thuật toán.

## Hội tụ và hai loại bất định

- **L11-2-13 — Ghi giả định ngay cạnh giá trị mà nó tạo ra.** Sơ đồ hai hàng giúp sinh viên thấy mỗi nguồn mẫu dẫn đến một giá trị giới hạn riêng. Hàng mô hình cần ghi rõ “mô hình lưu kết cục gần nhất, đường minh họa luôn đi đúng” cạnh \(0{,}729\). Thêm bốn mũi tên \(A\to B\to F\to K\to Z\), đặt \(+1\) ở mũi tên thứ tư để giải thích \(\gamma^3\). Hàng môi trường giữ \(0{,}6604\) với chú thích “mê cung có trượt”. Sửa nhãn giữa hai hàng thành “giá trị tối ưu có thể khác khi mô hình khác môi trường”. Sau ví dụ, thêm một câu nối với chứng minh: khi giữ mô hình cố định, kỳ vọng của mục tiêu mẫu chính là mục tiêu Bellman tối ưu **của mô hình đó**.
- **L11-2-04 — Dùng cùng một biến cố từ ví dụ đến đồ thị.** Dòng mở đầu dùng \((A,\rightarrow)\), còn ghi chú hình dùng \((F,\rightarrow)\). Đề xuất dùng xuyên suốt biến cố “đi sang \(B\) khi chọn phải ở \(A\)”, với \(p=0{,}8\) và \(\hat p=1/2\) từ hai lần thử. Đặt tên trục ngang là “số lần thử thật **của cặp này** \(C\)”, trục dọc là “độ lệch chuẩn”. Ghi trực tiếp trên hai đường “một lần thử: \(0{,}4\)” và “ước lượng qua \(C\) lần thử: \(0{,}4/\sqrt C\)”, làm nổi hai mốc \(C=2\) và \(C=50\). Ngay dưới hình, giải thích một dòng rằng \(\hat p\) là trung bình của \(C\) biến Bernoulli độc lập, với \(C\) ấn định trước. Sinh viên sẽ thấy vì sao độ phân tán của **ước lượng** giảm dù xác suất trượt mỗi lần giữ nguyên.

## Dyna-Q qua hai lượt đi

- **L11-2-07 — Cho xem hai cột “Mô hình” và “Bảng \(Q\)” ngay trong dòng thời gian.** Ở bước thật ① và ②, cột mô hình lần lượt hiện \((A,\rightarrow)\mapsto(0,A)\) rồi \((A,\rightarrow)\mapsto(0,B)\). Gắn nhãn “lưu kết cục gần nhất” từ lần ghi đầu tiên để báo rõ chuyển đổi từ L11-2-03. Đến bước ⑤, hiện lần lượt ba giá trị mới \(Q(K,\rightarrow)=0{,}5\), \(Q(F,\rightarrow)=0{,}225\), \(Q(K,\rightarrow)=0{,}75\), theo đúng thứ tự trực tiếp, lập kế hoạch, lập kế hoạch. Chốt bằng hai giá trị của \(F\) ngay sau bước này: \(0\) với \(n=0\), \(0{,}225\) với \(n=2\). Đây là kết quả của hai cặp lập kế hoạch được chọn trong ví dụ.
- **L11-2-08 — Gắn sơ đồ kiến trúc với đúng thao tác ở ví dụ.** Dùng lại các nhãn (d), (e), (f) và màu từ dòng thời gian. Trên hình, ghi đích cập nhật của từng mũi tên: (d) sửa \(Q\), (e) ghi `Model`, (f) đọc `Model` rồi sửa \(Q\) \(n\) lần. Đặt \(\gamma\) vào danh sách đầu vào và ghi giá trị tiếp nối tại đích \(Z\) bằng \(0\). Cạnh (e), thêm một dòng về phạm vi áp dụng: với môi trường tất định, lưu một kết cục cho mỗi cặp; với mê cung có trượt, có thể cập nhật bảng đếm rồi rút một cặp \((R,S')\) ở (f). Quy tắc cập nhật \(Q\) dùng chung cho cả hai.
- **L11-2-11 và L11-2-12 — Cho sinh viên dự đoán hàng cuối trước khi hiện lời giải.** Nối hai hàng lập kế hoạch bằng một mũi tên từ \(Q(F,\rightarrow)=0{,}45\) **vừa ghi** ở hàng trước đến mục tiêu \(0{,}9\cdot0{,}45=0{,}405\) của hàng sau. Khi đảo thứ tự, \(Q(B,\downarrow)\) sẽ là \(0{,}10125\), thay vì \(0{,}2025\). Có thể dùng phép đối chiếu này làm câu hỏi nhanh. Ở câu (b), đưa lên trang lời giải cả điều kiện chọn mỗi cặp vô hạn lần và bước học Robbins–Monro. Đối chiếu lần lượt với bốn cặp đã biết, mô hình được cập nhật trong quá trình chạy và \(\alpha=0{,}5\) hằng. Riêng ở bước thật đang xét, (e) ghi lại đúng kết cục đã lưu. Kết luận cần chốt là ví dụ nằm ngoài phạm vi bảo đảm của Mệnh đề 11.4.

## Khi môi trường đổi và khi ngân sách tính toán có hạn

- **L11-2-14 — Đặt hai mê cung trước và sau cạnh nhau.** Dùng cùng vị trí ô, tô hai cạnh \(F\!-\!K\) và \(B\!-\!C\), vẽ đường cũ \(A\to B\to F\to K\to Z\) và đường mới \(A\to B\to C\to D\to Z\). Cả hai dài bốn bước. Dưới hình sau, ghi kết quả thật cạnh dự đoán còn lưu: “\(F,\rightarrow\): dự đoán sang \(K\), thực tế ở \(F\)” và “\(B,\rightarrow\): dự đoán ở \(B\), thực tế sang \(C\)”. Gắn nhận xét về việc tránh thử lại với **lựa chọn tham lam**. Khi dùng \(\varepsilon\)-tham lam, nhánh thăm dò vẫn có thể thử lại.
- **L11-2-09 — Vẽ đường từ tiền thưởng mô phỏng đến lần thử thật.** Dùng hai hàng cùng bắt đầu ở \(Q(B,\rightarrow)=0{,}54\). Hàng Dyna-Q có mục tiêu \(0{,}54\) và giữ nguyên \(Q\). Hàng Dyna-Q+ ghi “400 bước thật kể từ lần thử gần nhất”, cộng \(0{,}2\) vào mục tiêu mô phỏng \(0{,}54\), rồi cho \(Q_{\text{mới}}=0{,}64>0{,}6\). Từ đó vẽ mũi tên tới “lần tới ở \(B\), đi phải là lựa chọn tham lam”, rồi tới “quan sát thật và cập nhật mô hình”. Chuỗi này giải thích được vì sao thưởng ở (f) giúp tác tử phát hiện cửa đã mở.
- **L11-2-10 — Quay lại đúng hai nhánh từ bảng đếm.** Giữ hai cây đang có, gắn mỗi xác suất \(0{,}5\) với một lần quan sát ở L11-2-03, và ghi \(R=0\) ở cả hai nhánh. Đặt kết quả ngay dưới mỗi cây: duyệt cả hai nhánh cho \(0{,}45\) với hai lần tính \(\max Q\); rút một nhánh cho \(0{,}54\) hoặc \(0{,}36\) với một lần tính. Dùng câu hỏi chuyển trang “Nếu chỉ có ngân sách đánh giá 10 trong 100 trạng thái kế, mục tiêu mẫu chính xác đến đâu?” để dẫn vào L11-2-15.
- **L11-2-15 — Ghi rõ sai số so với đại lượng nào.** Đổi nhãn trục dọc thành “RMSE so với mục tiêu kỳ vọng của mô hình” và chú thích \(k/b\) là tỷ lệ ngân sách, vì mỗi mẫu dùng một lần đánh giá. Làm nổi điểm \(b=100,\ k=10\) tại \((0{,}1;\,0{,}3146)\), cùng mốc \(k/b=1\) nơi phép tính kỳ vọng dùng đủ 100 nhánh và cho sai số \(0\). Có thể thay đoạn ngang ở độ cao \(1\) bằng chú thích “cần đủ \(b\) lượt đánh giá để tính kỳ vọng chính xác”, vì mức sai số trước đó phụ thuộc vào giá trị đang dùng làm ước lượng. Giữ hai ý chứng minh trên trang: với \(\alpha_j=1/j\), \(Q_k\) là trung bình mẫu; với \(b\) mục tiêu từng nhánh có phương sai \(1\) theo giả thiết, RMSE là \(\sqrt{(b-1)/(bk)}\). Ghi rõ phương sai \(1\) áp cho mục tiêu nhánh \(y_{s'}\) đã gồm chiết khấu. Nhắc lại L11-2-04 bằng hai nhãn cụ thể: \(C\) đếm **lần thử thật để ước lượng xác suất**, còn \(k\) đếm **lần rút từ mô hình để ước lượng mục tiêu cập nhật**.

Về bố cục, ưu tiên rà lại **L11-2-03, L11-2-06, L11-2-08, L11-2-10, L11-2-13 và L11-2-15** ở kích thước trình chiếu trong ảnh. Công thức, bước thuật toán hoặc kết quả cuối đang sát hay vượt vùng hiển thị. Hiện nội dung theo từng bước sẽ cho lớp thời gian dự đoán và giúp giữ phép tính đang giảng cùng hình minh họa trong một khung.

## Chấm điểm trên thang 10

| Tiêu chí | Điểm |
|---|---:|
| Mạch dẫn dắt | 7,5 |
| Trực quan hóa | 7,5 |
| Liên kết ví dụ–toán | 8 |
| Cân bằng trực giác–chứng minh | 7 |
| Từ lý thuyết đến thuật toán | 8 |
