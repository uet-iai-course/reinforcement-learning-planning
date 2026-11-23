# Nhận xét của Codex: mạch 2 "Tính bất định của môi trường và lập kế hoạch nền", Bài 11 (2026-11-23)

- Nguồn: `codex exec` (gói ChatGPT), model mặc định của cấu hình Codex, mức suy luận high; chạy bằng `tools/deck/codex_review.py`.
- Bản được nhận xét: `2627-1/lecture-11-lap-ke-hoach-dua-tren-mo-hinh.html` tại `1ae5d8e`; 17 trang (L11-2-00, L11-2-03, L11-2-06, L11-2-13, L11-2-04, L11-2-07, L11-2-16, L11-2-17, L11-2-08, L11-2-11, L11-2-12, L11-2-18, L11-2-14, L11-2-09, L11-2-10, L11-2-15, L11-2-19).
- Điểm: Ý đồ của mạch 8,0; Hiểu trực quan thuật toán 8,0; Mạch dẫn dắt 7,5; Trực quan hóa 8,0; Liên kết ví dụ–toán 8,5; Cân bằng trực giác–chứng minh 7,5; Từ lý thuyết đến thuật toán 8,0. Chưa đạt điều kiện dừng (mọi tiêu chí ≥ 9).
- Prompt:

```text
Xem phần "Tính bất định của môi trường và lập kế hoạch nền" (mạch 2) của bài giảng https://courses.iaidev.com/reinforcement-learning-planning/2627-1/lecture-11-lap-ke-hoach-dua-tren-mo-hinh.html#/2

Hãy phân tích dưới góc nhìn của sinh viên để gợi ý cách trình bày tốt hơn, trực quan hơn.

Trước khi góp ý, hãy đóng vai một sinh viên lần đầu học phần này, chỉ đọc mặt trang (ảnh và chữ trên trang), và viết mục **Kể lại như sinh viên**:
1. Ý đồ của phần này: vấn đề gì, vì sao cần giải quyết, phần này đi từ đâu tới đâu (2–3 câu).
2. Với mỗi phương pháp hoặc thuật toán xuất hiện: ý tưởng trong một câu; nó làm gì, kể bằng lời từng bước, không công thức; vì sao nó giải được vấn đề đã nêu; nó khác phương pháp trước ở đâu.
Chỗ nào mặt trang (ảnh và chữ trên trang) không đủ để kể lại, ghi "không rút ra được từ trang chiếu" kèm mã trang. Đó là những chỗ cần sửa trước hết; đề xuất phải giúp sinh viên tự kể lại được ý đồ, ý tưởng và cách thuật toán chạy một cách trực quan.

---
Ảnh đính kèm là 17 trang của phần này, đúng thứ tự trình chiếu (L11-2-00, L11-2-03, L11-2-06, L11-2-13, L11-2-04, L11-2-07, L11-2-16, L11-2-17, L11-2-08, L11-2-11, L11-2-12, L11-2-18, L11-2-14, L11-2-09, L11-2-10, L11-2-15, L11-2-19), chụp từ bản hiện tại, có thể mới hơn trang web. Tệp `mach.md` trong thư mục làm việc chứa văn bản và công thức (TeX) trên mặt từng trang. Đọc theo ảnh; dùng `mach.md` để đọc chính xác công thức. Ảnh chụp trạng thái cuối của mỗi trang, khi mọi lượt bấm đã hiện; trong `mach.md`, ⟨bấm k⟩ đánh dấu phần hiện ở lượt bấm thứ k của trang.
Khi nêu vấn đề hoặc đề xuất, ghi mã trang (ví dụ L11-2-06). Viết báo cáo bằng tiếng Việt, định dạng Markdown; hình đề xuất thì mô tả bằng lời (thành phần, số liệu, chú thích).
Cuối báo cáo, chấm điểm phần này trên thang 10 theo 7 tiêu chí, ghi đúng một bảng Markdown hai cột `Tiêu chí | Điểm`, mỗi tiêu chí một dòng, điểm là một số (ví dụ 8,5): Ý đồ của mạch; Hiểu trực quan thuật toán; Mạch dẫn dắt; Trực quan hóa; Liên kết ví dụ–toán; Cân bằng trực giác–chứng minh; Từ lý thuyết đến thuật toán. "Ý đồ của mạch" và "Hiểu trực quan thuật toán" chỉ được từ 9 trở lên khi mục Kể lại như sinh viên làm được đầy đủ chỉ từ mặt trang (ảnh và chữ trên trang).
```

---
# Mạch 2 — Tính bất định của môi trường và lập kế hoạch nền

Báo cáo dựa trên 17 ảnh theo đúng thứ tự trình chiếu. Tôi dùng `mach.md` để đối chiếu công thức và thứ tự các lượt bấm. Đường dẫn bài giảng hiện không truy cập được. [mach.md](/tmp/claude-1000/-data-tqlong-lectures/fd411c55-a86c-4518-a9f0-a6d4fde11419/scratchpad/lec11/codex-m2-prompt-moi/mach.md)

## Kể lại như sinh viên

### Ý đồ của phần này

Khi vừa nhận thưởng ở đoạn từ K đến đích, em muốn dùng thông tin đó để đánh giá lại hành động đi từ F đến K ngay, vì tác tử có thể phải chờ đến lượt sau mới đi qua F. Bài chỉ cách ghi lại các bước thật thành mô hình, dùng mô hình để cập nhật thêm, rồi ghép việc đó vào mỗi bước thật bằng Dyna-Q. Cuối phần, em thấy hai câu hỏi khác nhau: làm sao biết mô hình đã lỗi thời khi mê cung đổi cửa, và nên dùng bao nhiêu lượt tính để ước lượng giá trị từ mô hình đang có. (L11-2-00, L11-2-03, L11-2-06, L11-2-17, L11-2-14, L11-2-19)

### Các phương pháp và thuật toán

**Q-learning — học từ bước vừa đi thật.** Em thực hiện một hành động, xem mình nhận thưởng gì và tới đâu, rồi đọc giá trị của hành động tốt nhất ở ô mới. Em dùng hai thông tin đó để kéo giá trị của hành động vừa làm về phía mục tiêu. Khi tới đích Z, mục tiêu chỉ còn phần thưởng vừa nhận. Nhờ vậy, em cập nhật được giá trị đi phải ở K ngay khi nhận thưởng. Giá trị đi phải ở F vẫn bằng 0 vì lần đi qua F xảy ra trước lúc K có giá trị. Đây là cách cập nhật cơ sở để so sánh với các cách dùng mô hình ở phía sau. (L11-2-03, L11-2-08, L11-2-16)

**Mô hình đếm — ghi các kết cục đã thấy và dùng tần suất để dự đoán.** Em gom bước thật theo ô xuất phát và hành động, đếm số lần tới từng ô, rồi chia cho tổng số lần thử của cặp đó. Em cũng lấy trung bình các phần thưởng đã nhận. Chẳng hạn, hai lần đi phải ở A cho một lần ở lại A và một lần sang B, nên em gán cho mỗi kết cục một nửa. Q-learning dùng bước thật để sửa giá trị, còn mô hình đếm dùng bước thật để học hành động có thể dẫn tới đâu và cho thưởng gì. **“không rút ra được từ trang chiếu” (L11-2-03, L11-2-06)** — khi một cặp có nhiều kết cục với phần thưởng khác nhau, em chưa biết cách đi từ hai thống kê trên trang mô hình đếm đến việc rút phần thưởng và ô đến cùng nhau. Quy tắc đếm theo cả kết cục xuất hiện sau ở L11-2-08.

**Q-planning — dùng một bước do mô hình sinh ra để cập nhật bảng Q.** Em chọn một cặp mà mô hình trả lời được, hỏi mô hình phần thưởng và ô đến, đọc giá trị tốt nhất hiện có tại ô đến rồi cập nhật cặp đã chọn theo cách của Q-learning. Chọn đi phải ở F thì mô hình đưa em tới K với thưởng 0. Bảng Q lúc này đã có giá trị 0,5 ở K, nên giá trị đi phải ở F tăng lên 0,225 dù tác tử đã đi qua F từ trước. Mô hình đếm cung cấp thông tin về bước đi, còn Q-planning dùng thông tin đó để sửa giá trị. Nếu mô hình được giữ cố định, có đủ cặp, mọi cặp được chọn lặp lại vô hạn và bước học thỏa điều kiện nêu trên trang, giá trị sẽ tiến về nghiệm tối ưu của mô hình. **“không rút ra được từ trang chiếu” (L11-2-13)** — em theo được cách ra 0,729 từ đường đi trong mô hình, nhưng chưa tự tính được 0,6604 của mê cung thật vì trang chưa cho đủ quy tắc chuyển trạng thái dùng để ra số đó. (L11-2-06, L11-2-13, L11-2-18)

**Dyna-Q — sau mỗi bước thật, vừa học trực tiếp, vừa sửa mô hình, vừa lập kế hoạch.** Em chọn hành động theo chính sách ε-tham lam, thực hiện và quan sát kết cục. Em dùng kết cục thật để sửa bảng Q, rồi ghi kết cục vào mô hình. Sau đó, em chọn ngẫu nhiên một trạng thái đã có trong mô hình và một hành động đã lưu ở đó, lấy một kết cục mô phỏng, cập nhật Q theo cùng quy tắc và lặp đủ số lần đã định. Khi tính tay, em giữ kết cục gần nhất của mỗi cặp. Nếu dùng mô hình đếm, em giữ số lần thấy từng kết cục và rút theo tần suất. Khác với vòng Q-planning đứng riêng, Dyna-Q xen vòng mô phỏng vào mỗi bước thật và học dần mô hình đang dùng. Em hiểu chữ **nền** khi tác tử đang ở B mà bảng Q của F vẫn được sửa. Thứ tự chọn cặp cũng có tác dụng ngay: nếu em sửa F trước, lần cập nhật B đọc được giá trị mới của F. (L11-2-07, L11-2-16, L11-2-17, L11-2-08, L11-2-11, L11-2-12)

**Dyna-Q+ — dùng thưởng trong lúc lập kế hoạch để khuyến khích thử lại hành động lâu ngày ít dùng.** Em đếm số bước thật từ lần cuối thử một cặp. Khi cặp đó được chọn để lập kế hoạch, em cộng thêm thưởng mô phỏng theo thời gian đã chờ, rồi cập nhật Q. Với cửa mới mở ở B, lần cập nhật trên trang đẩy giá trị đi phải từ 0,54 lên 0,64, vượt lựa chọn đang dẫn đầu là 0,6. Lần tới ở B, tác tử có lý do để thật sự thử đi phải. Sang C hay trượt và ở lại B, nó đều ghi kết cục quan sát được và đặt lại bộ đếm. Dyna-Q thường phải chờ một lần thăm dò để thử lại lối này. Dyna-Q+ có thể làm hành động ấy trở thành lựa chọn tham lam. **“không rút ra được từ trang chiếu” (L11-2-08, L11-2-09)** — với một hành động chưa hề được thử, em chưa biết hành động đó có được đưa vào mô hình để nhận thưởng hay không, và nếu có thì khởi tạo thế nào. (L11-2-14, L11-2-09)

**Cập nhật mẫu và cập nhật kỳ vọng — hai cách lấy mục tiêu từ cùng một mô hình.** Với cập nhật mẫu, em rút một kết cục theo tần suất của mô hình, đọc giá trị ô đến và dùng mục tiêu của nhánh đó. Với cập nhật kỳ vọng, em lấy thông tin về tất cả kết cục, tính mục tiêu từng nhánh rồi gộp theo xác suất. Ở A, một lần rút cho mục tiêu 0,54 hoặc 0,36 và cần một lần đánh giá. Xét cả hai nhánh cho mục tiêu 0,45 và cần hai lần đánh giá. Cập nhật mẫu chính là việc em đã làm trong bước lập kế hoạch của Dyna-Q. Cập nhật kỳ vọng tốn thêm lượt đánh giá để tính đúng mục tiêu theo mô hình. Em có thể rút nhiều mẫu để ước lượng mục tiêu này tốt hơn, còn muốn biết xác suất đi sang B ngoài mê cung thật chính xác hơn thì phải thử thật thêm. (L11-2-10, L11-2-15, L11-2-19)

## Đề xuất chỉnh sửa theo mức ưu tiên

### 1. Cho sinh viên theo dõi một bước thật và một lần đọc mô hình trước khi đọc định nghĩa

- **L11-2-00, L11-2-03, L11-2-06.** Giữ câu hỏi về F làm câu hỏi mở mạch và đặt nó ngay cạnh hình F–K–Z. Ở lượt bấm đầu, hiện bước thật F sang K, thưởng 0, với thẻ “lúc này giá trị ở K bằng 0”. Tiếp theo hiện K sang Z, thưởng +1, và đổi ô Q ở K lên 0,5. Cuối cùng giữ chấm tác tử ở Z, hiện mũi tên nét đứt F sang K ghi “mô hình trả thưởng 0, đến K”. Nối thẻ “đọc 0,5 ở K” với thẻ “ghi 0,225 ở F”. Đặt phép tính sau lượt bấm này để sinh viên có thể nói trước **đọc ô nào, ghi ô nào, vì sao giá trị đổi**. Sơ đồ bốn nhánh ở L11-2-00 có thể thu nhỏ để nhường chỗ cho câu hỏi mở mạch.
- **L11-2-03, L11-2-06, L11-2-07, L11-2-08, L11-2-10.** Dùng lại hai thẻ quan sát của hành động đi phải ở A xuyên suốt các trang. Thẻ 1 ghi “thưởng 0, ở lại A”, thẻ 2 ghi “thưởng 0, sang B”. Trong mô hình đếm, giữ cả hai thẻ và ghi xác suất một nửa trên mỗi thẻ. Trong mô hình giữ kết cục gần nhất, làm mờ thẻ 1 và giữ thẻ 2. Khi gọi mô hình mẫu, đưa ra một thẻ nguyên vẹn. Khi đọc mô hình phân phối để tính kỳ vọng, mở cả hai thẻ kèm xác suất. Thêm ngay ở L11-2-06 một câu nói rõ ví dụ tính tay dùng kết cục gần nhất, còn hai cách lưu tình cờ cùng trả về K cho hành động ở F vì mới có một lần quan sát cặp đó. Như vậy sinh viên có thể theo dõi chỗ đổi mô hình trước khi gặp bảng năm bước.

### 2. Đưa vòng lặp Dyna lên trước bảng tính và giữ nguyên vị trí tác tử khi mô phỏng

- **L11-2-17, L11-2-07, L11-2-16, L11-2-08.** Đưa sơ đồ kiến trúc lên trước ví dụ lượt thứ nhất. Trong mỗi hình, tách ba vùng có nhãn **Mê cung thật**, **Mô hình**, **Bảng Q**. Ở bước 5, lượt bấm đầu cho tác tử đi vào Z và cập nhật K lên 0,5. Lượt kế ghi kết cục vào mô hình. Hai lượt sau lần lượt lấy thẻ của F và K, sửa F lên 0,225 rồi sửa K lên 0,75. Giữ chấm tác tử ở Z trong cả hai lượt mô phỏng. Ghi “thứ tự chọn trong lần chạy minh họa” cạnh hai thẻ để sinh viên thấy đây là kết quả của một thứ tự cụ thể. Sau khi đã thấy một vòng chạy, sinh viên mới đọc ký hiệu (a)–(f) và công thức tổng quát ở L11-2-08.
- **L11-2-11, L11-2-12.** Giữ câu hỏi đảo thứ tự và khai thác các lượt bấm đã có. Trước khi hiện hàng cập nhật B, hỏi “B sẽ đọc giá trị nào ở F?”. Cho hiện hai cột, mỗi cột chỉ có thứ tự và số đọc được: **F trước, B đọc 0,45 và lên 0,2025**; **B trước, B đọc 0,225 và lên 0,10125**. Đánh dấu A đã đọc giá trị cũ ở B từ bước thật đầu tiên. Chi tiết đó giải thích vì sao cập nhật mô phỏng ở B chưa làm A đổi ngay.

### 3. Trình bày hội tụ bằng hai mô hình cụ thể, rồi nối với giới hạn của ví dụ

- **L11-2-13, L11-2-18.** Đặt trang hội tụ sau khi sinh viên đã thấy Dyna-Q ghi đè và chọn cặp từ mô hình. Mở bằng hai bản đồ cùng tuyến A–B–F–K–Z. Bên mô hình, gắn nhãn “luôn đi tới ô kế” và giữ dải giá trị hiện có. Bên môi trường thật, vẽ vòng lặp ở các ô có thể trượt, ghi xác suất và phần thưởng theo đúng quy tắc của mê cung, rồi chỉ ra phép tính hoặc dẫn chiếu cụ thể cho 0,6604. Khi trình bày giả thiết, đặt cạnh mỗi dòng một chi tiết từ ví dụ: mô hình mới có bốn cặp, kết cục ở A từng bị ghi đè, lịch chọn chỉ lấy cặp đã thử, bước học giữ ở 0,5. Chốt bằng hai câu riêng: **mỗi lượt cập nhật chỉ cần mô hình trả lời được cặp đang chọn**; **bảo đảm hội tụ của mệnh đề cần các điều kiện cho cả quá trình**.

### 4. Cho thấy Dyna-Q+ dẫn tới lần thử thật bằng một dòng thời gian

- **L11-2-14, L11-2-09.** Giữ hai mê cung trước và sau khi đổi cửa. Thêm một dòng thời gian dưới hình: “cửa B–C mở” → “đã 400 bước thật kể từ lần thử đi phải ở B” → “một lần lập kế hoạch cộng 0,2” → “lần tới ở B, chọn đi phải”. Ở mốc lập kế hoạch, đặt ba vạch ngang chung thang giá trị tại 0,54, 0,6 và 0,64 để thấy lúc nào thứ hạng hành động đổi. Giữ hai nhánh thử thật với xác suất 0,8 sang C và 0,2 ở lại B, rồi cho cả hai về thao tác ghi kết cục và đặt bộ đếm về 0. Ghi rõ phạm vi của biến thể trên trang: nếu chỉ xét các cặp đã lưu, nói ngay cạnh bước chọn cặp. Nếu bài muốn sinh viên cài đặt cả trường hợp hành động chưa từng thử, bổ sung quy tắc khởi tạo mô hình và bộ đếm cho các hành động đó.

### 5. Cho sinh viên phân biệt số lần thử thật với số lượt tính trên mô hình

- **L11-2-04, L11-2-19.** Trên trang bất định, đặt hai thí nghiệm cạnh nhau. Bên trái là quỹ đạo “trượt, rồi sang B” đã quan sát. Bên phải là nhiều nhóm được ấn định thử đúng hai lần, với ba kết quả ước lượng 0, 0,5 và 1 có xác suất lần lượt 0,04, 0,32 và 0,64. Sau đó mới hiện đồ thị và ghi rõ trục tung là **độ lệch chuẩn**, còn mệnh đề viết theo **phương sai**. Ở trang cuối, dùng lại hai nhãn đầy đủ ngay trên hình: “\(C\) lần thử thật để học xác suất” và “\(k\) lần rút từ mô hình để ước lượng mục tiêu”. Như vậy sinh viên thấy ngay hai thao tác đang cải thiện hai ước lượng khác nhau.
- **L11-2-10, L11-2-15, L11-2-19.** Giữ cây hai nhánh làm cầu nối sang bài toán 100 nhánh. Trước khi hiện công thức RMSE, mô tả một hình gồm 100 thẻ giá trị nhánh được giữ cố định, mười lượt rút có hoàn lại, và hai dấu chỉ “trung bình 10 lượt rút” và “trung bình đủ 100 nhánh”. Đoạn nối hai dấu là sai lệch của **một** lần làm thử. RMSE khoảng 0,3146 tóm tắt sai số qua các lần lặp dưới giả thiết của mệnh đề. Trên đồ thị ngân sách, ghi trực tiếp “10/100 lượt đánh giá” tại chấm xanh và “100/100 để tính đúng mục tiêu kỳ vọng” tại chấm xám cho ví dụ này. Đổi nhãn bậc xám trước mốc đó thành “chưa tính đủ các nhánh” hoặc giữ mức 1 kèm chú thích ngay trên đường rằng đó là mức sai số ban đầu giả định.

## Điểm đánh giá

| Tiêu chí | Điểm |
|---|---:|
| Ý đồ của mạch | 8 |
| Hiểu trực quan thuật toán | 8 |
| Mạch dẫn dắt | 7,5 |
| Trực quan hóa | 8 |
| Liên kết ví dụ–toán | 8,5 |
| Cân bằng trực giác–chứng minh | 7,5 |
| Từ lý thuyết đến thuật toán | 8 |
