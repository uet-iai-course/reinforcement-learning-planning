# Nhận xét của Codex: mạch 2 "Tính bất định của môi trường và lập kế hoạch nền", Bài 11 (2026-11-23)

- Nguồn: `codex exec` (gói ChatGPT), model mặc định của cấu hình Codex, mức suy luận high; chạy bằng `tools/deck/codex_review.py`.
- Bản được nhận xét: `2627-1/lecture-11-lap-ke-hoach-dua-tren-mo-hinh.html` tại `f9d58bd`; 19 trang (L11-2-00, L11-2-03, L11-2-06, L11-2-04, L11-2-17, L11-2-07, L11-2-20, L11-2-16, L11-2-08, L11-2-13, L11-2-11, L11-2-12, L11-2-18, L11-2-14, L11-2-09, L11-2-10, L11-2-21, L11-2-15, L11-2-19).
- Vòng sau chỉnh sửa; nhận xét trước: `nhan-xet-codex-mach2-2026-11-23-p2.md`.
- Điểm: Ý đồ của mạch 8,5; Hiểu trực quan thuật toán 8,5; Mạch dẫn dắt 8,5; Trực quan hóa 9,0; Liên kết ví dụ–toán 9,0; Cân bằng trực giác–chứng minh 8,5; Từ lý thuyết đến thuật toán 8,5. Chưa đạt điều kiện dừng (mọi tiêu chí ≥ 9).
- Prompt:

```text
Xem phần "Tính bất định của môi trường và lập kế hoạch nền" (mạch 2) của bài giảng https://courses.iaidev.com/reinforcement-learning-planning/2627-1/lecture-11-lap-ke-hoach-dua-tren-mo-hinh.html#/2

Phần này đã được chỉnh sửa theo nhận xét lần trước (tệp `nhan-xet-truoc.md`). Hãy nhận xét bản sau chỉnh sửa: đề xuất nào đã được thực hiện và thực hiện tốt đến đâu, còn điều gì cần sửa.

Hãy phân tích dưới góc nhìn của sinh viên để gợi ý cách trình bày tốt hơn, trực quan hơn.

Trước khi góp ý, hãy đóng vai một sinh viên lần đầu học phần này, chỉ đọc mặt trang (ảnh và chữ trên trang), và viết mục **Kể lại như sinh viên**:
1. Ý đồ của phần này: vấn đề gì, vì sao cần giải quyết, phần này đi từ đâu tới đâu (2–3 câu).
2. Với mỗi phương pháp hoặc thuật toán xuất hiện: ý tưởng trong một câu; nó làm gì, kể bằng lời từng bước, không công thức; vì sao nó giải được vấn đề đã nêu; nó khác phương pháp trước ở đâu.
Chỗ nào mặt trang (ảnh và chữ trên trang) không đủ để kể lại, ghi "không rút ra được từ trang chiếu" kèm mã trang. Đó là những chỗ cần sửa trước hết; đề xuất phải giúp sinh viên tự kể lại được ý đồ, ý tưởng và cách thuật toán chạy một cách trực quan.

---
Ảnh đính kèm là 19 trang của phần này, đúng thứ tự trình chiếu (L11-2-00, L11-2-03, L11-2-06, L11-2-04, L11-2-17, L11-2-07, L11-2-20, L11-2-16, L11-2-08, L11-2-13, L11-2-11, L11-2-12, L11-2-18, L11-2-14, L11-2-09, L11-2-10, L11-2-21, L11-2-15, L11-2-19), chụp từ bản hiện tại, có thể mới hơn trang web. Tệp `mach.md` trong thư mục làm việc chứa văn bản và công thức (TeX) trên mặt từng trang. Đọc theo ảnh; dùng `mach.md` để đọc chính xác công thức. Ảnh chụp trạng thái cuối của mỗi trang, khi mọi lượt bấm đã hiện; trong `mach.md`, ⟨bấm k⟩ đánh dấu phần hiện ở lượt bấm thứ k của trang.
Khi nêu vấn đề hoặc đề xuất, ghi mã trang (ví dụ L11-2-06). Viết báo cáo bằng tiếng Việt, định dạng Markdown; hình đề xuất thì mô tả bằng lời (thành phần, số liệu, chú thích).
Cuối báo cáo, chấm điểm phần này trên thang 10 theo 7 tiêu chí, ghi đúng một bảng Markdown hai cột `Tiêu chí | Điểm`, mỗi tiêu chí một dòng, điểm là một số (ví dụ 8,5): Ý đồ của mạch; Hiểu trực quan thuật toán; Mạch dẫn dắt; Trực quan hóa; Liên kết ví dụ–toán; Cân bằng trực giác–chứng minh; Từ lý thuyết đến thuật toán. "Ý đồ của mạch" và "Hiểu trực quan thuật toán" chỉ được từ 9 trở lên khi mục Kể lại như sinh viên làm được đầy đủ chỉ từ mặt trang (ảnh và chữ trên trang).
```

---
# Nhận xét sau chỉnh sửa — Mạch 2, Bài 11

Báo cáo dựa trên 19 ảnh theo thứ tự trình chiếu. Tôi dùng `mach.md` để kiểm tra công thức và thứ tự hiện dần. Trang web không truy cập được trong phiên này, nên nhận xét về lượt bấm dựa trên mô tả trong tệp. [Văn bản mặt trang](/tmp/claude-1000/-data-tqlong-lectures/fd411c55-a86c-4518-a9f0-a6d4fde11419/scratchpad/lec11/codex-m2-p3/mach.md)

## Kể lại như sinh viên

### Ý đồ của phần này

Khi đi từ F sang K, em chưa biết bước tiếp theo từ K sẽ được thưởng, nên lần cập nhật ở F vẫn cho giá trị 0. Đến lúc nhận thưởng ở Z, em muốn dùng lại bước F sang K đã ghi để sửa giá trị ở F ngay, khỏi chờ quay lại. Bài đi từ cách ghi các bước thật và dùng chúng để cập nhật thêm, đến cách phát hiện mô hình đã cũ và cách chọn giữa rút vài mẫu với tính đủ các nhánh. (L11-2-00, L11-2-03, L11-2-06, L11-2-17, L11-2-14, L11-2-19)

**“không rút ra được từ trang chiếu” (L11-2-00, L11-2-04, L11-2-16)** — ở lần đọc đầu, em chưa biết câu hỏi về số lần thử thật ở A sẽ gặp lại câu hỏi về số lần rút mô phỏng ở đâu. Đến trang cuối em mới thấy hai số đếm được đặt cạnh nhau và biết mỗi số dùng để ước lượng một thứ khác nhau. (L11-2-19)

### Các phương pháp và thuật toán

- **Q-learning — em dùng bước vừa đi để sửa giá trị của hành động vừa làm.** Em đi thật, xem phần thưởng và ô đến, rồi lấy phần thưởng cùng giá trị của hành động tốt nhất ở ô đến để đặt mục tiêu. Em kéo giá trị cũ về phía mục tiêu một phần. Nếu đến đích, em chỉ dùng phần thưởng. Vì vậy bước vào Z nâng giá trị đi phải ở K. Bước đi từ F xảy ra sớm hơn, khi giá trị ở K còn bằng 0. Đây là quy tắc cập nhật mà các cách lập kế hoạch bên dưới dùng lại. (L11-2-03, L11-2-08, L11-2-16)
- **Mô hình đếm và mô hình giữ kết cục gần nhất — em ghi bước đã đi để có thể hỏi lại sau.** Với mô hình đếm, mỗi lần đi em thêm một thẻ ghi chung phần thưởng và ô đến vào nhóm của ô xuất phát và hành động. Em đếm tỉ lệ đến từng ô để ước lượng xác suất, lấy trung bình các phần thưởng khi cần, hoặc rút nguyên một thẻ để mô phỏng một bước. Hai lần đi phải ở A cho một thẻ ở lại A và một thẻ sang B. Với cách giữ kết cục gần nhất, em thay thẻ ở lại A bằng thẻ sang B. Bước thật ở đây tạo dữ liệu cho mô hình, còn ở Q-learning nó trực tiếp sửa bảng giá trị. Ở A, thử thật thêm giúp em học xác suất sang B, dù từng lần thử vẫn có thể trượt. (L11-2-03, L11-2-04, L11-2-07, L11-2-08)
- **Q-planning — em hỏi mô hình để có một bước dùng cho cập nhật Q.** Em chọn ngẫu nhiên một cặp ô và hành động, lấy một kết cục từ mô hình, đọc giá trị tốt nhất ở ô đến rồi sửa giá trị tại cặp đã chọn. Chọn đi phải ở F cho thẻ thưởng 0, đến K. Em đọc 0,5 ở K và sửa giá trị đi phải ở F lên 0,225 dù tác tử đã ở Z. So với Q-learning, bước đem ra cập nhật đến từ mô hình. Nếu chạy đủ lâu dưới các điều kiện của bài, em học được giá trị tối ưu theo mô hình đang dùng. **“không rút ra được từ trang chiếu” (L11-2-03, L11-2-06, L11-2-13)** — em chạy được lần chọn F, nhưng chưa biết phải chọn từ bốn cặp đã ghi hay từ mọi cặp hợp lệ khi lặp thuật toán. Trang hội tụ cũng chưa nói rõ mô hình cố định trong hình liên hệ thế nào với bảng bốn cặp. (L11-2-06, L11-2-13)
- **Dyna-Q — em xen các lần lập kế hoạch vào sau mỗi bước thật.** Em thường chọn hành động có giá trị cao nhất và đôi lúc chọn ngẫu nhiên. Sau khi đi, em sửa Q bằng kết cục thật rồi ghi kết cục vào mô hình. Sau đó em chọn một ô đã có trong mô hình và một hành động đã lưu ở ô ấy, lấy kết cục mô phỏng, sửa Q theo cùng quy tắc và lặp đủ số lần đã định. Ở bước 5, em cập nhật K bằng bước thật, rồi chọn F và K để lập kế hoạch. F đọc giá trị 0,5 vừa ghi ở K. Tác tử vẫn ở Z trong cả hai lần mô phỏng. Khác với Q-planning trên một mô hình có sẵn, Dyna-Q vừa học mô hình vừa dùng nó. Ở lượt sau, nếu chọn F trước B thì B đọc giá trị F vừa sửa, nên thứ tự chọn ảnh hưởng đến kết quả sau hai lần cập nhật. (L11-2-17, L11-2-07, L11-2-20, L11-2-08, L11-2-12)
- **Dyna-Q+ — em tăng cơ hội thử lại một hành động đã lâu chưa đi thật.** Em đếm số bước thật từ lần cuối thử cặp đó. Khi lấy cặp đã lưu để lập kế hoạch, em cộng một khoản thưởng mô phỏng tăng theo thời gian chờ rồi sửa Q. Trong ví dụ, đi phải ở B tăng từ 0,54 lên 0,64, vượt mức 0,6 đang dẫn đầu. Nếu thứ hạng ấy còn giữ khi tác tử trở lại B và chọn tham lam, nó sẽ thử đi phải. Em ghi kết cục thật và đặt lại bộ đếm dù lần đó sang C hay trượt ở B. So với Dyna-Q, khoản thưởng có thể khiến nhánh tham lam thử lại lối mà mô hình cũ đánh giá thấp. (L11-2-14, L11-2-09)
- **Cập nhật mẫu — em rút một kết cục để lấy mục tiêu cho một lần cập nhật.** Em rút theo xác suất trong mô hình, đọc giá trị tốt nhất ở ô đến, ghép với phần thưởng trên thẻ rồi dùng mục tiêu đó để sửa Q. Với hai thẻ ở A, em nhận mục tiêu 0,54 nếu rút nhánh sang B hoặc 0,36 nếu rút nhánh ở lại A. Đây là cách Q-planning và Dyna-Q đã dùng. Khi giữ nguyên giá trị các nhánh và lấy trung bình nhiều lượt rút, em ước lượng tốt hơn mục tiêu theo mô hình. (L11-2-06, L11-2-08, L11-2-10, L11-2-15)
- **Cập nhật kỳ vọng — em tính mục tiêu bằng cách xét đủ các kết cục có thể xảy ra.** Em lấy phân phối kết cục của cặp đang xét, tính mục tiêu trên từng nhánh, gộp chúng theo xác suất rồi dùng kết quả để sửa Q. Hai nhánh ở A đồng khả năng nên em lấy trung bình hai mục tiêu và được 0,45. Cách này cho đúng mục tiêu theo mô hình sau khi đánh giá đủ nhánh. Cập nhật mẫu tốn một lần đánh giá mỗi lượt và kết quả thay đổi theo nhánh rút được. **“không rút ra được từ trang chiếu” (L11-2-21, L11-2-15, L11-2-19)** — em thấy khoảng cách giữa hai vạch của lần rút minh họa, nhưng chưa đọc được sai lệch của lần đó. Em cũng chưa rõ khi tính RMSE, bài chỉ rút lại từ cùng 100 giá trị nhánh hay còn thay cả bộ giá trị nhánh. (L11-2-10, L11-2-21, L11-2-15, L11-2-19)

## Đối chiếu với nhận xét lần trước

1. **Đường dẫn từ bước thật đến mô hình đã rõ hơn, còn thiếu một chỗ chốt.** L11-2-03 đã có câu dẫn *đi thật → rút từ mô hình → thử lại*. L11-2-04 ghi ngay trên trục rằng \(C\) đếm lần thử thật để học xác suất. L11-2-16 đã hỏi đúng câu phân biệt hai việc ước lượng, còn L11-2-19 giải nghĩa cả \(k\) và \(C\). Ở L11-2-00, sinh viên vẫn chỉ thấy danh sách chủ đề. Từ câu hỏi ở L11-2-16 đến lời chốt ở L11-2-19 còn cả đoạn thuật toán, hội tụ, bài tập và đổi cửa.
2. **Chuỗi ví dụ Dyna-Q đã thực hiện tốt phần theo dõi thao tác.** L11-2-07 nói rõ vì sao ví dụ có trượt mà vẫn giữ kết cục gần nhất. L11-2-20 giữ đủ dấu vết **0 → 0,5 → 0,75** ở K, nối 0,5 với cập nhật của F và giữ chấm ở Z. L11-2-08 giải nghĩa ε-tham lam ngay chỗ chọn hành động. L11-2-12 cho sinh viên đoán B đọc giá trị nào trước khi hiện hai kết quả theo thứ tự chọn. Phần còn thiếu là một ví dụ cho thấy lợi ích của việc rút **nguyên thẻ** khi phần thưởng thay đổi theo kết cục. (L11-2-03, L11-2-08)
3. **Phần hội tụ đã bổ sung đúng chỗ cần hỏi sinh viên.** L11-2-13 hỏi trượt ở K thì đọc lại ô nào, rồi hiện phép tính cho 0,9756. L11-2-18 đã ghi rõ cả việc chọn cặp vô hạn lần lẫn vấn đề của bước học hằng 0,5. Ở L11-2-13, cụm “ô K, thưởng 0” vẫn cần gắn riêng vào nhánh trượt vì nhánh vào Z nhận +1. Hệ số truyền từ K về các ô trước đã có, nhưng phép dựng hệ số từ hai nhánh vẫn bị lướt qua.
4. **Dòng thời gian Dyna-Q+ đã giải quyết phần lớn nhận xét.** L11-2-09 tách rõ lần thử cuối, lúc mở lối và lúc lập kế hoạch. Ngoặc 400 bước bắt đầu từ lần thử thật cuối, và ô cuối đã có điều kiện “nếu 0,64 vẫn dẫn đầu”. Còn thiếu một câu nối từ L11-2-14 để người đọc biết đây là sau nhiều lượt và cặp đi phải ở B đã được thử khi lối còn bị chặn. Lượt đầu chỉ cho thấy cặp đi xuống ở B. (L11-2-07, L11-2-14, L11-2-09)
5. **Phần ngân sách đã sửa đúng quy ước hình, còn thiếu một ví dụ sai lệch đọc được.** L11-2-21 đã có dấu ×2 cho lượt rút có hoàn lại. L11-2-15 đã có câu giải thích RMSE bằng lời. L11-2-19 dùng dải xám để chỉ ngân sách chưa đủ cho cập nhật kỳ vọng và đặt chấm sai số 0 ở mốc đủ nhánh. Hai vạch ở L11-2-21 vẫn thiếu số, còn tên trục ở L11-2-19 dùng “số lần rút” cho cả phép so sánh với cách duyệt đủ nhánh. [Nhận xét lần trước](/tmp/claude-1000/-data-tqlong-lectures/fd411c55-a86c-4518-a9f0-a6d4fde11419/scratchpad/lec11/codex-m2-p3/nhan-xet-truoc.md:66)

## Những chỉnh sửa nên ưu tiên

1. **Chốt hai vai trò của dữ liệu ngay khi hai thẻ ở A xuất hiện.** (L11-2-00, L11-2-03, L11-2-04, L11-2-16, L11-2-10) Dùng chính hai thẻ ① và ② để dẫn hai câu hỏi. “Muốn biết xác suất thật sang B?” thì đi phải ở A thêm trong mê cung. “Muốn tính mục tiêu Q với hai thẻ đang có?” thì rút từ mô hình hoặc xét cả hai nhánh. Cho hiện lời chốt ngay sau câu hỏi ở L11-2-16, rồi nhắc lại khi quay về mô hình đếm ở L11-2-10. Ở L11-2-04, đặt nhãn “hai lần thử phát sinh trong một lượt đi” bên trái và “mỗi nhóm được ấn định hai lần thử” bên phải để sinh viên biết biểu đồ ba cột thuộc thí nghiệm nào.
2. **Ghi phạm vi chọn cặp ngay cạnh bước chọn.** (L11-2-03, L11-2-06, L11-2-08, L11-2-13, L11-2-18) Ở L11-2-06, đặt cạnh hình nhãn “minh họa một cập nhật trên cặp đã có thẻ”, rồi ghi đầu vào của thuật toán 11.3 là mô hình có thể trả kết cục cho mọi cặp hợp lệ. Ở L11-2-08, viết rõ thứ tự “chọn ngẫu nhiên một trạng thái đã lưu → chọn ngẫu nhiên một hành động đã lưu tại đó” nếu đó là quy tắc bài muốn dạy. Dùng cùng nhãn *mô hình cố định* ở L11-2-13 và L11-2-18. Ở định nghĩa lập kế hoạch nền, dùng “sửa giá trị ở F khi tác tử đang ở Z” hoặc “trước khi gặp lại F” để khớp với ví dụ về cặp đã quan sát. (L11-2-17, L11-2-20)
3. **Cho sinh viên dựng một phép tính từ hai nhánh.** (L11-2-13) Trên hình ở K, gắn “0,8 → Z, thưởng +1” lên mũi tên đi tiếp và “0,2 → K, thưởng 0” lên vòng trượt. Ở lượt bấm sau, dùng cùng bố cục tại F. Nhánh đi tiếp đọc giá trị K với hệ số \(0{,}8\cdot0{,}9\), nhánh trượt đọc lại giá trị F với hệ số \(0{,}2\cdot0{,}9\). Khi chuyển phần đọc lại F sang vế trái, sinh viên sẽ thấy hệ số \(0{,}72/0{,}82\) đến từ đâu và có thể tự lần tiếp về A. Gắn nhãn “mô hình cố định giả sử luôn đi tới ô kế trên tuyến” cho dải cam để nêu rõ mô hình tạo ra 0,729.
4. **Dùng một thẻ giả định để giải thích vì sao giữ chung thưởng và ô đến, rồi nối lịch sử của B qua hai trang.** (L11-2-03, L11-2-08, L11-2-14, L11-2-09) Trong một ô nhỏ ghi rõ “ví dụ giả định”, đặt hai thẻ *thưởng 0, ở A* và *thưởng +1, sang B*. Hỏi rút nguyên thẻ có thể cho “thưởng +1, ở A” hay không. Ví dụ này làm rõ thao tác cần cài đặt trong biến thể có trượt. Ở phần đổi cửa, thêm một dòng cạnh bản đồ cũ “Trong một lượt trước khi đổi cửa, tác tử từng thử đi phải ở B và ghi thẻ thưởng 0, ở lại B”. Khi sang L11-2-09, dùng lại đúng thẻ đó làm mốc bắt đầu đếm 400 bước.
5. **Tách sai lệch của một lần rút khỏi RMSE và dùng chung đơn vị ngân sách.** (L11-2-21, L11-2-15, L11-2-19) Ghi giá trị cạnh hai vạch trung bình và độ dài đoạn nối, lấy số từ chính 100 nhánh và 10 lượt rút trong hình. Cho hiện thêm hai vạch cam mảnh từ hai lần rút lại trên cùng bộ nhánh. Sang trang mệnh đề, nói bằng lời rằng trước hết bài đo sai số khi giữ cố định bộ nhánh, rồi lấy trung bình bình phương sai số qua các bộ giá trị nhánh theo giả thiết. Gắn \(0{,}3146\) với RMSE của thí nghiệm đó. Trên đồ thị cuối, đổi nhãn trục thành “số lần đánh giá nhánh chia cho tổng số nhánh”. Khi ấy 10 lượt rút có hoàn lại và một lượt duyệt đủ 100 nhánh cùng đọc được trên một trục ngân sách.

## Điểm đánh giá

| Tiêu chí | Điểm |
|---|---:|
| Ý đồ của mạch | 8,5 |
| Hiểu trực quan thuật toán | 8,5 |
| Mạch dẫn dắt | 8,5 |
| Trực quan hóa | 9 |
| Liên kết ví dụ–toán | 9 |
| Cân bằng trực giác–chứng minh | 8,5 |
| Từ lý thuyết đến thuật toán | 8,5 |
