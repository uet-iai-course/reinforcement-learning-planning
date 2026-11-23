# Nhận xét của Codex: mạch 2 "Tính bất định của môi trường và lập kế hoạch nền", Bài 11 (2026-11-23)

- Nguồn: `codex exec` (gói ChatGPT), model mặc định của cấu hình Codex, mức suy luận high; chạy bằng `tools/deck/codex_review.py`.
- Bản được nhận xét: `2627-1/lecture-11-lap-ke-hoach-dua-tren-mo-hinh.html` tại `1ae5d8e` cộng thay đổi chưa commit; 19 trang (L11-2-00, L11-2-03, L11-2-06, L11-2-04, L11-2-17, L11-2-07, L11-2-20, L11-2-16, L11-2-08, L11-2-13, L11-2-11, L11-2-12, L11-2-18, L11-2-14, L11-2-09, L11-2-10, L11-2-21, L11-2-15, L11-2-19).
- Vòng sau chỉnh sửa; nhận xét trước: `nhan-xet-codex-mach2-2026-11-23-prompt-moi.md`.
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
# Nhận xét sau chỉnh sửa · Mạch 2, Bài 11

Báo cáo dựa trên 19 ảnh của bản hiện tại theo thứ tự trình chiếu. Tôi dùng `mach.md` để đối chiếu công thức và các lớp hiện dần. Đường dẫn bài giảng không truy cập được trong phiên này, nên phần nhận xét về lượt bấm dựa trên những gì tệp mô tả. [Văn bản mặt trang](mach.md) · [Nhận xét lần trước](nhan-xet-truoc.md)

## Kể lại như sinh viên

### Ý đồ của phần này

Em vừa nhận thưởng khi đi từ K đến đích và muốn dùng ngay thông tin đó để đánh giá lại hành động đi từ F đến K, vì có thể phải đợi đến lượt sau mới quay lại F. Bài đi từ cách ghi kinh nghiệm thật thành mô hình, sang cách dùng mô hình để cập nhật thêm rồi ghép các lần cập nhật ấy vào mỗi bước thật bằng Dyna-Q. Sau đó bài xét chuyện mô hình cũ khi mê cung đổi cửa và chuyện nên rút vài mẫu hay tính hết các nhánh khi lập kế hoạch. (L11-2-00, L11-2-03, L11-2-06, L11-2-17, L11-2-14, L11-2-19)

**“không rút ra được từ trang chiếu” (L11-2-00, L11-2-04, L11-2-19)** — ở đầu mạch, em chưa thấy vì sao bài đang nói về việc cập nhật thêm lại chuyển sang đếm số lần thử thật, rồi cuối bài lại đếm số lượt rút từ mô hình. Đến trang cuối em mới biết hai số đếm phục vụ hai việc khác nhau.

### Các phương pháp và thuật toán

**Q-learning — học giá trị từ chính bước vừa đi.** Em thực hiện một hành động, xem mình nhận thưởng gì và tới ô nào. Em lấy phần thưởng cùng giá trị của hành động tốt nhất ở ô đến để đặt mục tiêu, rồi kéo giá trị của hành động vừa làm về phía mục tiêu đó. Nếu ô đến là đích thì chỉ dùng phần thưởng. Vì vậy, bước vào Z làm giá trị đi phải ở K tăng lên. Khi tác tử đi qua F ở bước trước, giá trị ở K còn bằng 0, nên cập nhật ở F lúc đó vẫn cho 0. Đây là cách cập nhật cơ sở mà các thuật toán sau dùng lại. (L11-2-03, L11-2-08, L11-2-16)

**Mô hình đếm và mô hình giữ kết cục gần nhất — hai cách ghi nhớ những gì đã xảy ra.** Với mô hình đếm, em gom các thẻ theo ô xuất phát và hành động. Mỗi thẻ ghi cả phần thưởng lẫn ô đến. Em đếm số thẻ đến từng ô để ước lượng xác suất, lấy trung bình phần thưởng khi cần, và rút nguyên một thẻ theo tần suất kết cục khi cần một mẫu. Hai lần đi phải ở A cho hai thẻ, một ở lại A và một sang B, mỗi thẻ có cơ hội được rút như nhau. Với cách giữ kết cục gần nhất, thẻ sang B ghi đè thẻ ở lại A, nên lần sau hỏi mô hình chỉ nhận thẻ sang B. Q-learning dùng bước thật để sửa bảng giá trị, còn hai cách ghi này dùng bước thật để mô hình có thể trả lời về một hành động đã thử. (L11-2-03, L11-2-06, L11-2-07, L11-2-08)

**Q-planning — lấy một bước từ mô hình để sửa bảng giá trị.** Em chọn một cặp ô và hành động, hỏi mô hình để lấy phần thưởng và ô đến, rồi cập nhật cặp đã chọn giống Q-learning. Nếu chọn đi phải ở F, mô hình trả thẻ thưởng 0, đến K. Em đọc giá trị 0,5 vừa có ở K và dùng nó để nâng giá trị đi phải ở F lên 0,225, trong khi tác tử đã ở Z. Cái mới so với Q-learning là nguồn của bước dùng để cập nhật. Khi chạy lâu trên một mô hình cố định, giá trị học được hướng tới nghiệm của mô hình đó nếu thỏa các điều kiện trên trang hội tụ. **“không rút ra được từ trang chiếu” (L11-2-13)** — em hiểu vì sao mô hình luôn đi tới cho giá trị 0,729, nhưng chưa tự dựng được phép tính cho giá trị 0,6604 của mê cung thật. Hình cho biết xác suất trượt và hệ số nhân, còn trường hợp trượt nhận thưởng gì và vì sao hệ số ấy xuất hiện thì em phải tự điền. (L11-2-06, L11-2-13, L11-2-17)

**Dyna-Q — sau mỗi bước thật, cập nhật trực tiếp, ghi mô hình rồi lập kế hoạch.** Em chọn hành động theo chính sách ε-tham lam và đi thật. Em dùng kết cục vừa thấy để sửa Q, rồi ghi nó vào mô hình. Sau đó, em chọn một trạng thái đã có trong mô hình và một hành động đã lưu ở đó, lấy kết cục mô phỏng và sửa Q theo cùng quy tắc. Em lặp phần mô phỏng đủ số lần đã định. Ở bước 5, lần đi thật nâng giá trị ở K lên 0,5. Hai lần lập kế hoạch sau đó lần lượt sửa F lên 0,225 rồi sửa K lên 0,75. Tác tử vẫn ở Z. Khác với Q-planning chạy riêng trên mô hình, Dyna-Q vừa học mô hình vừa dùng nó giữa các bước thật. **“không rút ra được từ trang chiếu” (L11-2-07, L11-2-08)** — trang thuật toán giả thiết môi trường tất định, còn ví dụ tính tay có trượt và vẫn giữ kết cục gần nhất. Em làm theo được ví dụ, nhưng chưa biết khi nào nên chọn cách lưu đó và khi nào nên giữ nhiều kết cục. (L11-2-17, L11-2-20, L11-2-16, L11-2-08)

**Dyna-Q+ — làm hành động lâu ngày chưa thử trở nên đáng thử lại.** Với một cặp đã lưu, em đếm số bước thật từ lần cuối thử nó. Khi chọn cặp đó để lập kế hoạch, em cộng thưởng vào mẫu mô phỏng rồi cập nhật Q. Trong ví dụ, giá trị đi phải ở B tăng từ 0,54 lên 0,64 và vượt hành động đang dẫn đầu ở mức 0,6. Khi trở lại B và chọn tham lam, tác tử có lý do đi phải. Dù sang C hay trượt ở lại B, tác tử ghi kết cục thật và đặt lại bộ đếm. Dyna-Q thường phải chờ một lượt thăm dò để thử lại lối ấy, còn phần thưởng của Dyna-Q+ có thể làm thay đổi lựa chọn tham lam. **“không rút ra được từ trang chiếu” (L11-2-07, L11-2-14, L11-2-09)** — em chưa thấy hành động đi phải ở B đã vào mô hình lúc nào. Lượt đầu chỉ cho em thấy hành động đi xuống ở B. (L11-2-14, L11-2-09)

**Cập nhật mẫu và cập nhật kỳ vọng — hai cách lấy mục tiêu từ cùng một mô hình.** Với cập nhật mẫu, em rút một thẻ theo xác suất, đọc giá trị ở ô đến và dùng mục tiêu của nhánh vừa rút. Ở A, một lượt rút cho mục tiêu 0,54 hoặc 0,36. Với cập nhật kỳ vọng, em mở cả hai nhánh, tính mục tiêu từng nhánh rồi gộp theo xác suất, được 0,45. Cách thứ nhất chính là kiểu cập nhật đã dùng trong Q-planning và Dyna-Q. Rút thêm và lấy trung bình giúp em ước lượng mục tiêu của mô hình tốt hơn. Cách thứ hai tính đúng mục tiêu của mô hình sau khi xét đủ các nhánh. **“không rút ra được từ trang chiếu” (L11-2-21, L11-2-19)** — em chỉ thấy khoảng cách giữa hai vạch trong hình 10 lượt rút, chưa đọc được độ lớn của sai lệch trong lần rút đó. Em cũng chưa biết đường xám ở mức 1 đang đo sai số của giá trị nào trước khi tính đủ nhánh. (L11-2-10, L11-2-21, L11-2-15, L11-2-19)

## Đối chiếu với nhận xét lần trước

1. **Mở bằng F–K–Z và dùng lại các thẻ quan sát — thực hiện tốt.** Sơ đồ tổng quan ở L11-2-00 đã thu gọn. L11-2-03 đặt câu hỏi cạnh hai bước thật và ghi rõ K còn 0 ở bước 4, lên 0,5 ở bước 5. L11-2-06 dùng nhãn **đọc** ở K, **ghi** ở F và giải thích vì sao hai cách lưu cho cùng kết cục tại F. Cặp thẻ ①–② được dùng lại ở L11-2-07 và L11-2-10. Việc rút nguyên cặp phần thưởng–ô đến đã có quy tắc ở L11-2-08. Vì hai thẻ ở A đều có thưởng 0, sinh viên vẫn khó thấy ngay lý do phải giữ hai thông tin đi cùng nhau.

2. **Đưa kiến trúc Dyna lên trước ví dụ và cho theo dõi vị trí tác tử — thực hiện rất tốt.** L11-2-17 xuất hiện trước bảng năm bước. Trang mới L11-2-20 chia rõ mê cung thật, mô hình và bảng Q, rồi minh họa thứ tự chọn cặp của một lần chạy. L11-2-16 nối hình với phép tính bằng số 0,5 đóng khung. L11-2-12 cũng đã làm đúng phần gợi ý về thứ tự cập nhật: hỏi B đọc gì ở F trước khi hiện đáp án, rồi đặt hai kết quả 0,2025 và 0,10125 cạnh nhau. Hàng của A đã ghi rõ nó đọc giá trị cũ ở B. Trên ảnh cuối của L11-2-20, số 0,5 nằm trong chú thích đọc ở K, còn ô K chỉ hiện 0,75, nên đường đi của số 0,5 vẫn rõ hơn ở bảng tính kế tiếp.

3. **Dời hội tụ xuống sau thuật toán và đối chiếu với bài tập — thực hiện tốt về thứ tự, còn thiếu một bước tính.** L11-2-13 nay đứng sau ví dụ và thuật toán Dyna-Q. Hình đã có vòng trượt 0,2, hai dải giá trị và hệ số truyền giá trị. Phần còn thiếu là quy tắc phần thưởng trên vòng trượt và cách suy ra 0,9756 ở K cùng hệ số 0,72/0,82. L11-2-18 đã đối chiếu cả bốn giả thiết, nhưng “chỉ chọn cặp đã thử” mới mô tả phạm vi lấy mẫu. Cần thêm rằng ví dụ chưa có bảo đảm mọi cặp hợp lệ cuối cùng đều được thử và được chọn vô hạn lần.

4. **Dùng dòng thời gian để giải thích Dyna-Q+ — gần như đầy đủ.** L11-2-14 giữ hai bản đồ cùng vị trí ô. L11-2-09 đã có thang chung cho 0,54, 0,6 và 0,64, hai kết cục của lần thử thật, thao tác đặt lại bộ đếm và nhãn “cặp đã lưu”. Nhãn này làm rõ phạm vi của biến thể minh họa, nên trường hợp hành động chưa bao giờ được thử chỉ cần bổ sung nếu bài muốn dạy cách cài đặt biến thể có những hành động đó. Hai chi tiết vẫn dễ bị đọc nhầm là mốc bắt đầu đếm 400 bước và điều kiện để lần sau ở B chọn đi phải.

5. **Phân biệt thử thật với rút từ mô hình — thực hiện tốt, nhất là ở hai hình mới và sửa.** L11-2-04 có hai thí nghiệm đặt cạnh nhau và trục tung ghi rõ độ lệch chuẩn. L11-2-21 đã tạo được cầu nối từ cây hai nhánh đến công thức sai số bằng 100 nhánh cố định và một lần lấy 10 mẫu. L11-2-19 ghi rõ 10/100, 100/100 và phân biệt \(k\) với \(C\) ở cuối trang. Chú thích “sai số giả định 1” đã có, nhưng bậc xám vẫn dễ được đọc như một kết quả định lượng ngang hàng với ba đường RMSE.

## Những chỉnh sửa nên ưu tiên

1. **Nối câu hỏi mở mạch với hai việc phải ước lượng. (L11-2-00, L11-2-04, L11-2-16, L11-2-19)** Dưới câu mở ở L11-2-00, cho một dòng dẫn đường gồm ba cụm: **đi thật để học mô hình → rút từ mô hình để cập nhật Q → đi thử lại khi nghi mô hình đã cũ**. Ở L11-2-04, gắn nhãn “thử thật để học xác suất” ngay trên hình. Ở L11-2-19, đưa nhãn “rút từ mô hình để ước lượng mục tiêu” vào tên trục và nhắc lại nhãn của L11-2-04. Có thể dùng một câu hỏi chuyển trang ở L11-2-16: “Nếu rút thêm từ mô hình đang gán A và B mỗi nơi một nửa, ta biết chính xác hơn mục tiêu theo mô hình hay xác suất sang B ngoài mê cung?” Câu hỏi này nối được hai đoạn bất định bằng chính hai thẻ sinh viên đã thấy.

2. **Nói rõ mô hình nào đang chạy và cho theo dõi một số qua từng thao tác. (L11-2-03, L11-2-06, L11-2-07, L11-2-20, L11-2-08)** Đặt ngay trên bảng năm bước câu “Ví dụ có trượt. Để tính tay, mỗi cặp chỉ giữ kết cục vừa thấy.” Ở trang thuật toán, gắn giả thiết tất định cạnh quy tắc ghi một kết cục và đặt quy tắc đếm theo cả phần thưởng–ô đến cạnh biến thể có trượt. Một thẻ giả định ở lề, cùng ô đến nhưng khác phần thưởng, đủ để cho thấy tác dụng của việc rút nguyên thẻ. Trong hình ba vùng, cho ô K giữ dấu vết **0 → 0,5 ở (d) → 0,75 ở (f)**, nối số 0,5 với cập nhật ở F và giữ chấm tại Z. Cũng nên ghi ngay cạnh bước chọn hành động rằng ε-tham lam thường chọn hành động có Q cao nhất và đôi lúc chọn ngẫu nhiên để thăm dò.

3. **Cho sinh viên tự dựng một phương trình hội tụ từ hình. (L11-2-13, L11-2-18)** Phóng to riêng ô K, ghi hai nhánh **0,8 tới Z, thưởng +1** và **0,2 ở lại K, thưởng 0** theo quy tắc dùng để tính ví dụ. Trước khi hiện kết quả, hỏi “Nếu trượt, ô nào sẽ được đọc lại?”. Từ hình, hiện phép tính ở K, \(v(K)=0{,}8+0{,}2\cdot0{,}9v(K)\). Dùng một ô trước K để chỉ ra phần đi tiếp có hệ số \(0{,}8\cdot0{,}9\), còn phần ở lại tạo ra mẫu số \(1-0{,}2\cdot0{,}9\). Sau hai bước đó, sinh viên có thể tự lần ngược về A. Khi giải bài tập, ghi rõ lịch chọn trong ví dụ chưa bảo đảm cập nhật vô hạn cho mọi cặp và bước học hằng 0,5 nằm ngoài giả thiết của mệnh đề.

4. **Làm rõ hai mốc thời gian của Dyna-Q+. (L11-2-14, L11-2-09)** Thêm một câu chuyển cảnh rằng đây là thời điểm sau nhiều lượt và tác tử từng thử đi phải ở B khi lối còn bị chặn, nên mô hình đã có thẻ “thưởng 0, ở lại B”. Trên dòng thời gian, đánh dấu riêng **lần thử thật cuối của cặp** và **lúc cửa mở**. Vẽ ngoặc “400 bước” từ lần thử cuối đến lần lập kế hoạch trong ví dụ. Ở mốc cuối, ghi “nhánh tham lam chọn → nếu 0,64 vẫn dẫn đầu”. Như vậy sinh viên có thể kể trọn vòng từ mô hình cũ đến lần thử thật tiếp theo.

5. **Nối sai lệch của một lượt rút với RMSE và làm rõ đường ngân sách. (L11-2-21, L11-2-15, L11-2-19)** Ghi giá trị của hai vạch trung bình trong một lần rút minh họa, kèm độ dài đoạn sai lệch. Có thể viền cam một thẻ và ghi “×2” để sinh viên nhìn thấy ý nghĩa của *có hoàn lại*. Trước chứng minh, thêm một câu bằng lời giải thích rằng mỗi lần rút 10 mẫu cho một sai lệch, rồi RMSE tổng hợp bình phương các sai lệch khi lặp thí nghiệm theo giả thiết của mệnh đề. Trên đồ thị ngân sách, thay đoạn xám ngang ở mức 1 bằng một dải ghi “chưa hoàn tất cập nhật kỳ vọng” và giữ chấm tại \(k/b=1\), RMSE bằng 0. Các đường màu khi đó có thể được đọc trực tiếp như sai số định lượng, còn chấm xám chỉ mốc đủ ngân sách để tính đúng mục tiêu của mô hình.

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
