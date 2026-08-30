# Quy trình chuyển trang chiếu Học tăng cường sang RevealJS

## Phạm vi

Tệp này áp dụng cho mọi yêu cầu chọn một bộ trang chiếu trong `RL-hk2-2025-2026/` và chuyển sang RevealJS cho học phần **Học tăng cường**, học kỳ 1 năm học 2026–2027.

Mỗi yêu cầu phải tạo hoặc cập nhật:

- `2627-1/lecture-NN-<ten-bai>.html`;
- các hình SVG trong `2627-1/img/lec-NN/`;
- ba tệp quy trình trong `2627-1/planning/lec-NN/`;
- mục tương ứng trong `2627-1/index.html`.

`NN` lấy theo số bài của tệp nguồn và luôn có hai chữ số. Ví dụ, bài 1 dùng `lecture-01-<ten-bai>.html`. Nếu số bài hoặc tên bài không xác định được từ tên tệp và nội dung nguồn, phải hỏi người dùng trước khi soạn.

Điều phối viên phải dùng nhiều tác tử theo quy trình dưới đây. Không giao toàn bộ việc phân tích, soạn, rà soát và chỉnh sửa cho một tác tử.

## Đối tượng và thời lượng

- Đối tượng mặc định là sinh viên đại học đã học học máy, học sâu và thuật toán.
- Buổi học gồm ba tiết, mỗi tiết 50 phút, tổng cộng 150 phút.
- Phần trình chiếu chính được thiết kế cho 120 phút. 30 phút còn lại dành cho chữa bài tập và trình diễn mã (code demo).
- Chỉ chuyển hoặc chuẩn bị code demo khi bản nguồn có nội dung tương ứng. Không tự tạo sổ tay mã (notebook) hoặc chương trình ngoài phạm vi nguồn nếu người dùng không yêu cầu.

## Ngôn ngữ và biên tập

- Viết thuần Việt. Chỉ giữ tiếng Anh cho tên riêng, tên phần mềm, ký hiệu chuẩn, tên thuật toán hoặc thuật ngữ chưa có cách dịch ổn định.
- Khi dùng viết tắt lần đầu, viết đầy đủ bằng tiếng Việt rồi đặt dạng viết tắt trong ngoặc.
- Viết ngắn, trực tiếp và học thuật. Dùng câu ngắn, động từ rõ và thuật ngữ nhất quán.
- Không dùng câu hỏi tu từ, câu cảm thán, lời ca tụng, khẩu hiệu hoặc cách diễn đạt quảng bá.
- Không thêm nhận định, số liệu, nguồn hoặc ví dụ không có căn cứ.
- Trong mọi tệp Markdown, chỉ dùng `$...$` cho công thức nội dòng và `$$...$$` cho công thức khối.
- Dùng `$no-ai-slop` để biên tập nội dung hiển thị và ghi chú diễn giả. Giữ ý của nguồn, cắt lời dẫn rỗng, câu tổng kết lặp, diễn đạt phô trương và nhịp câu máy móc. Tự kiểm bản cuối theo `no-ai-slop/eval.md`.
- Dùng `$quill` để rà dàn ý, thứ tự khái niệm, thuật ngữ và tính liên tục giữa các phần. Không khởi tạo `quill.json`; công việc này không phải dự án sách.

## Thứ tự ưu tiên

Khi có xung đột, tuân theo thứ tự sau:

1. Chỉ dẫn cụ thể của người dùng cho bài đang làm.
2. Bộ trang chiếu được người dùng chọn trong `RL-hk2-2025-2026/`.
3. Tài liệu bổ sung và tài sản liên quan do người dùng cung cấp.
4. `2627-1/lecture-template.html` và `2627-1/lecture-style.css` về giao diện và nền kỹ thuật.
5. Các quy ước trong tệp này.

Giữ mạch, thứ tự và ý chính của nguồn. Chỉ gộp, tách, thêm, lược hoặc sắp xếp cục bộ khi cần sửa lỗi, giảm quá tải, khôi phục tiên quyết, hoàn thiện mạch học tập hoặc bảo đảm khả năng đọc. Mọi sai khác phải có lý do trong storyboard và nhật ký rà soát.

## Tiếp nhận và kiểm kê

Sau khi người dùng chọn tệp nguồn, điều phối viên phải:

- đọc tệp nguồn và kiểm tra các tài liệu liên quan trong `RL-hk2-2025-2026/resources/`;
- bỏ qua `.DS_Store`, tệp có tiền tố `._` và tệp tạm có tiền tố `~$`;
- xác định số bài, tên bài, mục tiêu, kiến thức tiên quyết, phạm vi, số trang và các tài sản được dùng;
- đọc `2627-1/lecture-template.html`, `lecture-style.css` và `index.html` trước khi lập kế hoạch;
- kiểm kê các hình, biểu đồ, sơ đồ, bảng, công thức và đoạn code phải chuyển;
- xác định phần nào của nguồn là nội dung, bố cục, ghi chú, tài liệu tham khảo hoặc tài sản trực quan;
- chỉ hỏi người dùng về thông tin không thể suy ra từ kho và có thể làm thay đổi đáng kể kết quả.

Nếu người dùng chưa chọn tệp nguồn, dừng sau bước kiểm kê danh mục và yêu cầu tên tệp. Không tự chọn bài thay người dùng.

## Tổ chức tệp

Mỗi bài dùng cấu trúc sau:

```text
2627-1/
├── lecture-NN-<ten-bai>.html
├── img/
│   └── lec-NN/
│       └── *.svg
└── planning/
    └── lec-NN/
        ├── outline.md
        ├── storyboard.md
        └── review-log.md
```

- `outline.md` chứa mục tiêu, dàn ý, ánh xạ nguồn và bảng thuật ngữ hoặc ký hiệu cần thiết.
- `storyboard.md` chứa bản đồ hành trình khái niệm và một mục cho từng trang chiếu.
- `review-log.md` chứa các báo cáo rà soát, quyết định chỉnh sửa, sai khác so với nguồn và ngoại lệ đã được duyệt.
- Tệp HTML nằm trực tiếp trong `2627-1/`. Không đặt tệp HTML trong thư mục planning hoặc img.
- Mọi đường dẫn trong HTML phải tương đối và hợp lệ khi máy chủ được mở tại thư mục gốc của kho.

## Mẫu RevealJS bắt buộc

- Dùng `2627-1/lecture-template.html` làm nền. Chỉ kế thừa cấu trúc, giao diện và cấu hình kỹ thuật; không sao chép chủ đề, nội dung hoặc siêu dữ liệu (metadata) của bài mẫu.
- Dùng `2627-1/lecture-style.css`, màu, phông chữ, khoảng cách, thẻ, lưới và chân trang hiện có. Không tạo hệ giao diện mới.
- Tham khảo cách tổ chức bố cục trong kho [uet-iai-course/machine-learning](https://github.com/uet-iai-course/machine-learning), ưu tiên `SLIDE_STYLE_GUIDE.md` và các tệp `2526-2/lecture-*.html`. Áp dụng các nguyên tắc một luận điểm trung tâm, hình hoặc công thức đủ lớn, chú thích nêu kết luận và nhịp mở phần–trực giác–cơ chế–ví dụ–kiểm tra. Không sao chép nội dung, tài sản hoặc CSS từ kho tham khảo; `lecture-template.html`, `lecture-style.css` và các quy ước cục bộ vẫn có ưu tiên cao hơn.
- Giữ `lang="vi"`, khung `1280 × 720`, `controlsLayout: "edges"`, `slideNumber: true`, `hashOneBasedIndex: true` và `hash: true`.
- Dùng các thư viện cục bộ trong `2627-1/`: RevealJS, `RevealMath.KaTeX`, `RevealNotes` và `RevealHighlight`.
- Dùng `<section>` ngoài cho từng phần và `<section>` trong cho từng trang chiếu.
- Toàn bộ bài dùng từ 5 đến 7 mạch trình bày lớn, mỗi mạch tương ứng với một `<section>` ngoài; số này gồm mạch mở đầu và mạch kết luận. Chỉ dùng ngoài khoảng 5–7 khi nguồn hoặc yêu cầu cụ thể của người dùng đòi hỏi, và phải ghi lý do cùng ảnh hưởng đến mạch bài trong `storyboard.md` và `review-log.md`.
- Mỗi trang có `data-slide-id` duy nhất. Mã này chỉ xuất hiện trong HTML, outline, storyboard và nhật ký; không hiển thị trên mặt trang chiếu hoặc trong ghi chú diễn giả.
- Đặt chân trang ở cuối `.slides` và cập nhật đúng tên học phần, học kỳ và số bài.
- Không phụ thuộc mạng cho các thành phần cốt lõi.
- Chỉ dùng tài sản cốt lõi đã có trong `2627-1/` hoặc tài sản SVG được tạo cho bài đang làm. Không tải phông chữ, thư viện hoặc hình từ mạng.

## Chuyển và vẽ lại hình

- Mọi sơ đồ, đồ thị, hình minh họa và hình kỹ thuật phải được vẽ lại thành SVG. Không trích ảnh raster từ PDF hoặc PPTX rồi nhúng vào trang chiếu.
- Lưu SVG chính tại `2627-1/img/lec-NN/`. SVG nhỏ, chỉ dùng một lần, có thể đặt nội dòng trong HTML khi cách này giúp bố cục hoặc khả năng tiếp cận rõ hơn.
- Giữ đúng quan hệ, tỷ lệ có ý nghĩa, nhãn, chiều mũi tên, chú giải và dữ liệu của hình nguồn. Không làm hình đẹp hơn bằng cách thay đổi nội dung.
- Đồ thị phải có tên trục, đơn vị, chú giải và nguồn khi các thành phần này có trong nguồn hoặc cần để hiểu hình.
- Mỗi SVG phải có `role="img"` và mô tả thay thế cụ thể. Không dùng màu làm tín hiệu duy nhất.
- Công thức, bảng và đoạn code phải được dựng bằng KaTeX, HTML hoặc khối code; không chuyển chúng thành ảnh.
- Không dùng ảnh sinh bởi AI để thay cho dữ liệu, kết quả thực nghiệm hoặc hình mô tả bằng chứng.
- Ảnh chụp, logo hoặc ảnh chụp màn hình chỉ được giữ ở dạng điểm ảnh (raster) khi không thể tái tạo trung thực bằng SVG và người dùng đã duyệt ngoại lệ. Ghi ngoại lệ, lý do và đường dẫn trong `review-log.md`.
- Nếu ngoại lệ chưa được duyệt, dừng phần bị ảnh hưởng và hỏi người dùng. Không âm thầm giữ ảnh raster hoặc bỏ nội dung.

## Cấu trúc học tập

Mỗi khái niệm trọng tâm đi theo chu trình:

**vấn đề → trực giác → ví dụ → hình thức/thuật toán → ứng dụng → kiểm tra**

- **Vấn đề:** nêu quyết định, giới hạn hoặc bài toán cần giải quyết. Không dùng câu hỏi tu từ.
- **Trực giác:** dùng quan hệ trạng thái, hành động, phần thưởng, quỹ đạo hoặc giá trị để chuẩn bị cho ký hiệu.
- **Ví dụ:** dùng một trường hợp có thể tính, mô phỏng hoặc kiểm tra.
- **Hình thức/thuật toán:** nêu định nghĩa, công thức, giả mã, đầu vào, đầu ra và giả thiết.
- **Ứng dụng:** dùng trực tiếp kết quả vừa xây dựng trong một bài toán Học tăng cường.
- **Kiểm tra:** yêu cầu người học tính, giải thích, so sánh, chứng minh hoặc áp dụng.

Không bắt buộc sáu bước là sáu trang riêng. Có thể gộp khi trang vẫn có một luận điểm trung tâm. Với khái niệm phụ, có thể dùng chu trình rút gọn nếu storyboard ghi rõ lý do. Không đảo thứ tự hoặc bỏ ngầm một bước đối với khái niệm trọng tâm.

Storyboard phải chỉ ra cho từng cụm:

- mạch trình bày chứa cụm, chức năng của mạch, kết nối vào từ mạch trước và đầu ra cho mạch sau;
- mã trang thực hiện từng bước;
- kiến thức đầu vào và sản phẩm học tập;
- ký hiệu hoặc dữ kiện được truyền từ ví dụ sang công thức hoặc thuật toán;
- bước được gộp hoặc ghi `không áp dụng`, kèm lý do;
- câu nối giữa các bước;
- thời lượng dự kiến của cụm và tổng thời lượng 120 phút.

## Tiêu chuẩn nội dung Học tăng cường

- Phân biệt rõ tác tử, môi trường, trạng thái, quan sát, hành động, phần thưởng, chính sách, mô hình và hàm giá trị khi các khái niệm này xuất hiện.
- Nêu miền, kiểu, kích thước, chỉ số thời gian, quy ước kỳ vọng và điều kiện dừng trước khi sử dụng.
- Dùng ký hiệu nhất quán từ ví dụ sang công thức, giả mã, ứng dụng và bài tập.
- Phân biệt bài toán dự đoán với điều khiển; theo chính sách với khác chính sách; có mô hình với phi mô hình; giá trị trạng thái với giá trị hành động khi phù hợp.
- Với quy trình quyết định Markov, nêu rõ giả thiết Markov, không gian, động lực chuyển, phần thưởng và hệ số chiết khấu.
- Với phương trình Bellman hoặc quy tắc cập nhật, kiểm tra chỉ số, điều kiện hóa, dấu, hệ số chiết khấu, mục tiêu cập nhật và đại lượng được giữ cố định.
- Với thuật toán, nêu đầu vào, đầu ra, giả mã hoặc sơ đồ, tiêu chuẩn dừng, chi phí chính, điều kiện hội tụ và giới hạn thực hành khi nguồn có hoặc khi thiếu chúng sẽ gây hiểu sai.
- Với học sâu trong Học tăng cường, phân biệt mạng trực tuyến, mạng mục tiêu, bộ nhớ phát lại, mục tiêu bootstrap, hành vi thăm dò và chính sách đánh giá khi phù hợp.
- Không tuyên bố hội tụ, tối ưu, không chệch hoặc ổn định nếu thiếu giả thiết quyết định kết luận.
- Tự tính lại các ví dụ số, xác suất, kỳ vọng, cập nhật giá trị và kích thước ten-xơ (tensor) quan trọng.
- Giữ nguồn truy nguyên được theo số trang hoặc số trang chiếu của bản nguồn. Chỉ bổ sung nguồn ngoài khi cần sửa hoặc kiểm chứng một mệnh đề và phải ghi nguồn cụ thể.

## Tiêu chuẩn trang chiếu và ghi chú

- Mỗi trang chiếu có một luận điểm trung tâm. Tách phép suy diễn, giả mã hoặc bảng quá dài thay vì thu nhỏ chữ.
- Tiêu đề ngắn và gọi đúng khái niệm. Không đặt tiêu đề dưới dạng “Tại sao...?”, “Vì sao...?” hoặc câu kể tiến trình.
- Văn bản thân bài nên từ `0.75em` trở lên. Chỉ dùng dưới `0.65em` cho chú thích ngắn đã được tác tử góc nhìn sinh viên xác nhận là đọc được.
- Mỗi gạch đầu dòng không quá hai dòng ở khung 16:9. Chuyển diễn giải dài sang ghi chú diễn giả.
- Công thức trung tâm phải đủ lớn, có khoảng trắng và không bị cắt.
- Mọi lời mời tương tác trên mặt trang chiếu dùng nhãn **“Câu hỏi:”**.
- Không hiển thị mã nội bộ, nhãn quy trình, phân tuyến hoặc thời lượng trên mặt trang chiếu hay trong ghi chú diễn giả.
- Mỗi trang nội dung có `<aside class="notes">` khi cần giải thích giả thiết, công thức, lỗi dễ mắc, chuyển ý, đáp án hoặc nguồn.
- Ghi chú diễn giả viết thành mạch nói ngắn bằng tiếng Việt; không chỉ chứa metadata và không lặp nguyên văn nội dung hiển thị.
- Bộ trang chiếu phải dùng được bằng bàn phím, có tương phản đủ và không dùng màu làm tín hiệu duy nhất.

## Quy trình đa tác tử

### 1. Điều phối và lập kế hoạch

Điều phối viên kiểm kê nguồn, xác nhận đầu ra và mở dự án bền vững trong Codex Slides. Giao một tác tử lập kế hoạch riêng trước khi phân tích chi tiết hoặc sửa tệp.

Tác tử lập kế hoạch:

- xác định mục tiêu, phạm vi, đối tượng, thời lượng và tiêu chí hoàn thành;
- lập danh mục khái niệm trọng tâm và bản đồ chu trình học tập;
- chia việc thành kiểm kê, ánh xạ, soạn, rà soát, chỉnh sửa và kiểm định;
- xác định việc tuần tự, việc có thể chạy song song, đầu vào và đầu ra của từng tác tử;
- nêu rủi ro về thiếu nguồn, hình khó vẽ lại, ký hiệu, quá tải, tràn trang và code demo;
- không sửa tệp trang chiếu.

Điều phối viên phải kiểm tra và chấp nhận kế hoạch trước khi triển khai.

### 2. Phân tích nguồn và ánh xạ

Giao một tác tử chỉ đọc:

- lập bảng ánh xạ từng trang nguồn sang trang đích;
- ghi quyết định `giữ`, `sửa`, `gộp`, `tách`, `thêm` hoặc `bỏ`;
- trích mục tiêu, định nghĩa, công thức, thuật toán, ví dụ, bài tập, code và nguồn;
- kiểm kê từng hình và cách vẽ lại thành SVG;
- chỉ ra thiếu giả thiết, sai số, mâu thuẫn, ký hiệu không nhất quán và đoạn khó đọc;
- bàn giao đặc tả cho tác tử soạn, không sửa tệp.

### 3. Soạn và triển khai

Giao một tác tử soạn:

- tạo `outline.md`, `storyboard.md`, HTML và SVG theo đặc tả;
- dịch và biên tập bằng tiếng Việt theo `$no-ai-slop`;
- dùng `$quill` để kiểm tra mạch phần, chuyển ý, thuật ngữ và ký hiệu;
- giữ thứ tự nguồn trừ các thay đổi đã được phê duyệt;
- thêm ghi chú diễn giả và nguồn;
- không sửa RevealJS, tiện ích (plugin) hoặc CSS dùng chung nếu có thể giải quyết trong tệp bài giảng;
- nếu cần sửa `lecture-style.css`, phải kiểm tra các bài hiện có không bị hỏng.

### 4. Kiểm định storyboard

Giao một tác tử chỉ đọc rà từng trang và từng cụm khái niệm:

- kiểm tra lý do tồn tại của từng trang có cụ thể và kiểm chứng được;
- kiểm tra trang tạo một bước tiến trong lập luận hoặc luyện tập;
- kiểm tra chu trình sáu bước đúng thứ tự và nối được từ ví dụ sang hình thức;
- phát hiện trang trùng ý, trang trang trí, trang quá tải và khoảng trống cần bổ sung;
- kiểm tra thời lượng 120 phút, kiến thức tiên quyết và quan hệ trước–sau;
- đề xuất quyết định, bằng chứng và tác động đến trang lân cận;
- không sửa tệp.

Sau thay đổi số lượng hoặc thứ tự, phải rà lại các trang bị ảnh hưởng và hai trang lân cận mỗi phía.

### 5. Năm tác tử rà soát độc lập

Sau bản nháp đầu, chạy song song năm tác tử chỉ đọc. Mỗi báo cáo dùng các trường `mức độ`, `trang chiếu`, `vấn đề`, `bằng chứng`, `đề xuất sửa`.

- **Góc nhìn sinh viên:** kiểm tra tiên quyết, tải nhận thức, nhịp giảng, khả năng đọc, ví dụ, chuyển ý, câu hỏi kiểm tra và khả năng tự học.
- **Chuyên gia Học tăng cường:** kiểm tra độ bao phủ, chiều sâu, thuật ngữ, mạch học thuật, quan hệ với học máy và sự phù hợp với 120 phút.
- **Độ chính xác toán học và thuật toán:** kiểm tra định nghĩa, giả thiết, xác suất, kỳ vọng, chỉ số, công thức Bellman, quy tắc cập nhật, giả mã, kết quả số, hội tụ, độ phức tạp và kích thước tensor.
- **Phản biện học thuật và giảng dạy Học tăng cường–lập kế hoạch:** đóng vai chuyên gia nghiên cứu và giảng dạy để phản biện công thức, thuật toán và trình tự kiến thức; kiểm tra mỗi hình thức hóa có đủ trực giác, ví dụ và tiên quyết, mỗi thuật toán có xuất hiện đúng chỗ trong mạch học tập, và thứ tự hiện tại có hỗ trợ việc suy luận trên lớp hay không. Tác tử này phải nêu rõ khi một công thức đúng riêng lẻ nhưng được đặt sai trình tự hoặc thiếu cầu nối sư phạm.
- **Kết nối và mạch viết:** kiểm tra xương sống lập luận của toàn bài, điểm xuất phát, đích đến và sự tích lũy ý nghĩa qua từng phần; xác nhận bài có từ 5 đến 7 mạch trình bày lớn tương ứng với các `<section>` ngoài, gồm mạch mở đầu và mạch kết luận, trừ ngoại lệ đã được ghi rõ. Với mỗi phần, xác định chức năng, kết nối vào từ phần trước, đầu ra cho phần sau và đóng góp vào mục tiêu bài học; với mỗi trang, kiểm tra vai trò trong mạch cùng câu nối với trang liền trước và liền sau. Phát hiện bước nhảy lập luận, chuyển phần đột ngột, trang đứng riêng lẻ, phần lặp chức năng, tuyến không tiến triển, kết luận không thu hồi vấn đề mở đầu hoặc nhiều trang tranh cùng một luận điểm trung tâm. Vai này không thay thế kiểm định storyboard, rà độ chính xác hay rà tải nhận thức. Trong `bằng chứng` và `đề xuất sửa`, phải nêu rõ `vai trò trong mạch`, `kết nối vào` và `kết nối ra` của trang hoặc cụm trang bị ảnh hưởng.

Mức độ gồm `chặn bàn giao`, `nghiêm trọng`, `trung bình`, `nhẹ`. Mọi lỗi `chặn bàn giao` và `nghiêm trọng` phải được xử lý.

Đối với vai kết nối và mạch viết, dùng mức `chặn bàn giao` khi thiếu mạch mở đầu hoặc mạch kết luận, số mạch ngoài khoảng 5–7 mà không có ngoại lệ hợp lệ, không xác định được tuyến chính hoặc kết luận mâu thuẫn với vấn đề đã thiết lập; `nghiêm trọng` khi một phần trọng tâm bị đứt khỏi tuyến chính, lặp chức năng hoặc không tạo bước tiến; `trung bình` khi điểm vào, đầu ra hay câu chuyển giữa hai phần còn mờ; `nhẹ` khi mạch đúng nhưng tín hiệu chuyển ý hoặc thứ bậc nhấn chưa rõ. Sau khi thêm, bỏ, gộp, tách, đổi thứ tự trang hoặc sửa câu chuyển làm thay đổi mạch bài, phải giao lại vai này rà các trang bị ảnh hưởng, hai trang lân cận mỗi phía và mọi ranh giới phần liên quan. Nếu thay đổi mở bài, kết bài hoặc luận điểm trung tâm, phải rà lại toàn bộ bộ trang chiếu.

### 6. Chỉnh sửa

Giao một tác tử chỉnh sửa riêng sau khi năm báo cáo hoàn tất:

- hợp nhất vấn đề trùng lặp và ưu tiên tính đúng, khả năng học, khả năng đọc;
- sửa tuần tự HTML, SVG, outline, storyboard và ghi chú;
- ghi quyết định đối với đề xuất không áp dụng;
- không thay đổi mạch nguồn nếu lỗi có thể sửa cục bộ;
- yêu cầu rà lại độ chính xác cho mọi phần toán học hoặc thuật toán đã đổi đáng kể.
- yêu cầu tác tử kết nối và mạch viết rà lại theo phạm vi ở mục 5 sau mọi thay đổi cấu trúc, thứ tự, câu chuyển hoặc luận điểm trung tâm.

Các tác tử sửa tệp không được chạy song song.

### 7. Kiểm định cuối

Điều phối viên hoặc tác tử kiểm thử riêng phải:

- đối chiếu số trang nguồn, bảng ánh xạ, `data-slide-id` và mục tương ứng trong storyboard;
- kiểm tra HTML, cấu trúc `<section>`, KaTeX, tiện ích, ghi chú diễn giả, đường dẫn, SVG và liên kết;
- kiểm tra bài có từ 5 đến 7 `<section>` ngoài, gồm mạch mở đầu và mạch kết luận, hoặc có ngoại lệ hợp lệ đã được ghi trong storyboard và nhật ký;
- tìm mọi tham chiếu ảnh raster; chỉ chấp nhận mục có ngoại lệ đã được người dùng duyệt và ghi trong nhật ký;
- kiểm tra không có tài nguyên hỏng hoặc phụ thuộc mạng cốt lõi;
- chạy `python3 -m reloadserver 8765` tại thư mục gốc; cổng là đối số vị trí, không dùng `--port`;
- mở `http://localhost:8765/2627-1/lecture-NN-<ten-bai>.html` và duyệt mọi trang ngang, trang dọc;
- kiểm tra tràn chữ, chữ nhỏ, chồng lấn, công thức, hình, tương phản và bàn phím ở khung 16:9 và một màn hình hẹp;
- dùng Codex Slides để rà soát trực quan sau cùng và xác minh thay đổi hiển thị đúng;
- kiểm tra đủ năm báo cáo độc lập; mọi vấn đề về vai trò trong mạch, kết nối vào–ra và tuyến lập luận phải có quyết định cùng bằng chứng rà lại;
- chạy lại kiểm định sau mỗi lần sửa lỗi chặn bàn giao hoặc nghiêm trọng.

Nếu Codex Slides không khả dụng, phải báo rõ giới hạn, tiếp tục đầy đủ các kiểm tra RevealJS cục bộ và không tuyên bố đã rà bằng Codex Slides.

## Cập nhật `index.html`

- `2627-1/index.html` là danh mục riêng của học phần **Học tăng cường** cho học kỳ 1 năm học 2026–2027.
- Khi chuyển bài Học tăng cường đầu tiên, bỏ các thẻ của học phần Cơ sở toán học cho AI hiện có.
- Mỗi bài hoàn thành có một thẻ theo thứ tự số bài, gồm tên bài, mô tả một câu và liên kết duy nhất đến tệp HTML của bài giảng.
- Không đặt liên kết đến `outline.md`, `storyboard.md`, `review-log.md`, `note-for-author.md` hoặc thư mục `planning/` trên trang chỉ mục. Các tệp quy trình chỉ dùng nội bộ trong kho.
- Không thêm bài chưa hoàn thành hoặc liên kết đến tệp chưa tồn tại.
- Giữ giao diện của trang chỉ mục hiện có trừ nội dung nhận diện học phần và danh sách bài.

## Tiêu chí hoàn thành

Chỉ bàn giao khi:

- bản RevealJS giữ đúng ý chính và mạch nguồn, còn mọi sai khác đều được ghi;
- nội dung chính bằng tiếng Việt, ngắn, trực tiếp và đã qua `$no-ai-slop`;
- outline, storyboard và nhật ký nằm đúng `planning/lec-NN/`;
- mọi hình đã được vẽ lại thành SVG hoặc có ngoại lệ raster được người dùng duyệt;
- năm báo cáo độc lập đã có và mọi lỗi bắt buộc đã được xử lý;
- công thức, ví dụ số, giả mã và giả thiết đã được kiểm tra;
- bộ trang chiếu chạy tại cổng `8765`, không có lỗi hiển thị hoặc tài nguyên hỏng nghiêm trọng;
- `index.html` liên kết đúng tới tệp HTML của bài và không liên kết tới các tệp quy trình;
- nội dung trong kho khớp với bản đã rà trong Codex Slides, hoặc giới hạn công cụ đã được ghi rõ.

Khi bàn giao, nêu ngắn gọn: tệp trang chiếu, URL cục bộ, tệp nguồn, hình đã vẽ lại, các kiểm tra đã chạy, sai khác có chủ ý, ngoại lệ và giới hạn còn lại.

## Điều phối mô hình trong dự án

- Codex chính giữ vai trò điều phối viên và thực hiện kiểm định cuối.
- Người dùng cho phép các worker OpenRouter đọc và gửi nội dung các tệp trong workspace tới OpenRouter để thực hiện nhiệm vụ được giao, ngoại trừ mọi tệp `.env`. Không được đọc, đưa vào prompt, ghi log hoặc gửi nội dung `.env` và các giá trị bí mật chứa trong đó tới OpenRouter.
- Chạy worker qua các lệnh `openrouter-mcp-reader`, `openrouter-mcp-reviewer` và `openrouter-mcp-writer` trong `openrouter-mcp/`. Không dùng `collaboration.spawn_agent` cho ba vai trò này và không chuyển ngầm sang worker mặc định khi OpenRouter lỗi.
- Dùng vai trò `openrouter_reader` qua `openrouter-mcp-reader` cho kiểm kê, lập kế hoạch và phân tích nguồn chỉ đọc.
- Dùng vai trò `openrouter_reviewer` qua `openrouter-mcp-reviewer` cho các lượt rà soát độc lập chỉ đọc.
- Dùng vai trò `openrouter_writer` qua `openrouter-mcp-writer` cho một phần việc ghi đã được giới hạn bằng `--repo-root`, tệp và đầu ra cụ thể.
- Luôn truyền `--json`; dùng `requested_model`, `observed_model` và `provider` trong kết quả cầu nối làm bằng chứng runtime, không dùng lời tự khai trong nội dung worker.
- Khi cần chạy song song, khởi chạy mỗi reviewer trong một tiến trình `openrouter-mcp-reviewer` riêng và chờ tất cả hoàn tất.
- Không cho hai tác tử có quyền ghi sửa các tệp trùng nhau cùng lúc.
- Điều phối viên phải chờ các tác tử liên quan, hợp nhất kết quả và tự xác minh trước khi bàn giao.
