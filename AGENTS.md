# Quy trình chuyển trang chiếu Học tăng cường sang RevealJS

## Phạm vi

Tệp này áp dụng cho mọi yêu cầu chọn một bộ trang chiếu trong `RL-hk2-2025-2026/` và chuyển sang RevealJS cho học phần **Học tăng cường**, học kỳ 1 năm học 2026–2027.

Mỗi yêu cầu phải tạo hoặc cập nhật:

- `2627-1/lecture-NN-<ten-bai>.html`;
- các hình SVG trong `2627-1/img/lec-NN/`;
- ba tệp quy trình trong `2627-1/planning/lec-NN/`;
- học liệu công khai trong `2627-1/materials/lec-NN/`: ghi chú bài giảng `lecture-note.md` (theo quy trình hai giai đoạn trong `prompt_lecture_note_deck.md`), bộ bài tập `exercises.md` và bài thực hành `thuc-hanh-<chu-de>.ipynb` khi người dùng yêu cầu;
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
- Tiêu đề, nội dung trang chiếu, chú thích hình, ghi chú diễn giả, ghi chú bài giảng và lời giải phải dùng văn phong trang trọng, học thuật. Viết trực tiếp, chính xác; ưu tiên câu ngắn, động từ rõ và thuật ngữ nhất quán.
- Không dùng văn nói mô phỏng hoặc lời hướng dẫn giảng viên, người soạn trên sản phẩm công khai và trong ghi chú diễn giả, chẳng hạn “chúng ta hãy nhìn”, “nhấn mạnh với sinh viên”, “đến đây chuyển sang trang sau”. Diễn đạt bằng đối tượng, giả thiết, phép suy luận và kết luận. Các yêu cầu học tập như “Tính”, “Xác định”, “Chứng minh” và các bước thuật toán vẫn được dùng khi đúng chức năng.
- Không dùng câu hỏi tu từ, câu cảm thán, lời ca tụng, khẩu hiệu hoặc cách diễn đạt quảng bá. Trong ghi chú bài giảng, được phép mở một mục bằng câu hỏi nghiên cứu thật mà mục đó trả lời ngay sau ("Ước lượng này tốt đến mức nào? Định lý sau cho biết…"); câu hỏi không có câu trả lời trong cùng mục là câu hỏi tu từ và bị cấm.
- Không thêm nhận định, số liệu, nguồn hoặc ví dụ không có căn cứ.
- Trong mọi tệp Markdown, chỉ dùng `$...$` cho công thức nội dòng và `$$...$$` cho công thức khối.
- **Giọng kể của ghi chú bài giảng** (yêu cầu người dùng 2026-10-11, theo giáo trình *Học máy thống kê* của tác giả, bản nguồn tại `../SML-textbook-main.zip`, chương `chapters/06_reinforcement_learning/`): ghi chú được viết bằng giọng kể đi cùng người đọc. Dùng "chúng ta" cho câu nêu kế hoạch, nhu cầu, lựa chọn phương pháp và giới hạn ("Để giải quyết vấn đề phụ thuộc lẫn nhau giữa các trạng thái, chúng ta có thể dùng phương pháp lặp giá trị"); dùng "ta" trong tính toán ("Thế vào (2.3), ta được…", "Như vậy, ta vừa chứng minh…"). Chủ ngữ của câu dẫn dắt là người viết cùng người đọc hoặc chính đối tượng toán học, không phải tài liệu ("Mục này định nghĩa…", "Phần này giới thiệu…" bị cấm). Bên trong khối định nghĩa, định lý, mệnh đề, bổ đề, hệ quả, thuật toán giữ câu khách quan. Vẫn cấm mệnh lệnh dẫn dắt ("hãy", trừ đề bài tập), câu hỏi tu từ, lời giảng viên, lời khen và câu dẫn rỗng.
- **Thuật ngữ và định nghĩa trước khi dùng** (đợt rà soát 2026-10-12 của học phần Cơ sở toán học cho AI, áp dụng cho học phần này): thuật ngữ tiếng Anh đặt trong ngoặc ở lần xuất hiện đầu tiên của mỗi tài liệu ("lợi tức (return)", "mục tiêu bootstrap (bootstrap target)"); khi một khái niệm có hai cách gọi, viết "X (còn gọi là Y)" ở lần đầu rồi chỉ dùng X. Mọi ký hiệu, giả thiết hoặc kết quả được dùng trên một trang chiếu hoặc trong một mục phải được định nghĩa hoặc nhắc lại trước lần dùng đầu, bằng dòng "Nhắc lại:" hoặc một trang nhắc lại riêng khi kết quả đến từ bài trước; không dựa vào trí nhớ của người đọc. Dùng "Lời giải" cho lời giải bài tập, không dùng "Đáp án". Bảng thuật ngữ Việt–Anh của bài nằm trong `outline.md` và phải thống nhất với các bài đã có.
- Bắt buộc dùng kỹ năng `no-ai-slop` của Claude Code (`~/.claude/skills/no-ai-slop/`, nạp bằng công cụ `Skill`) khi soạn, sửa hoặc rà tiêu đề, nội dung trang chiếu, ghi chú và học liệu. Đọc `SKILL.md` trước khi áp dụng. Tác tử soạn hoặc chỉnh sửa dùng chế độ Edit, biên tập rồi tự đối chiếu `eval.md` và sửa các mục chưa đạt trước khi bàn giao. Tác tử rà soát chỉ đọc dùng chế độ Detect, nêu mẫu diễn đạt có vấn đề, trích đoạn làm bằng chứng và đề xuất sửa; không chỉnh tệp. Loại lời dẫn rỗng, lời nhấn mạnh thiếu căn cứ, câu lặp, đổi từ đồng nghĩa tùy tiện, nhịp câu khuôn mẫu và kết luận kịch tính. Ghi phạm vi cùng kết quả kiểm tra trong `review-log.md`; không dùng điểm từ bộ phát hiện AI hoặc suy đoán tác giả làm bằng chứng.
- Khi áp dụng `no-ai-slop`, giữ nguyên ý nguồn, giả thiết, ký hiệu, phép suy luận và các phân biệt toán học, thuật toán cần thiết. Văn phong học thuật của học phần được ưu tiên hơn gợi ý của kỹ năng về giữ giọng nói, hài hước hoặc câu rời. Giữ định nghĩa, nhãn kết quả, câu hỏi đánh giá và phần tổng kết khi chúng có chức năng học tập rõ.
- Dùng kỹ năng `quill` của Claude Code (`~/.claude/skills/quill/`) để rà dàn ý, thứ tự khái niệm, thuật ngữ và tính liên tục giữa các phần. Không khởi tạo `quill.json`; công việc này không phải dự án sách.

## Thứ tự ưu tiên

Khi có xung đột, tuân theo thứ tự sau:

1. Chỉ dẫn cụ thể của người dùng cho bài đang làm.
2. Bộ trang chiếu được người dùng chọn trong `RL-hk2-2025-2026/`.
3. Tài liệu bổ sung và tài sản liên quan do người dùng cung cấp.
4. Mẫu văn phong, dẫn dắt và cách đặt vấn đề của tác giả: các trang chiếu MAT1101 tại `../MAT1101/` cho mặt trang chiếu, chương Học tăng cường và các chương khác của giáo trình *Học máy thống kê* tại `../SML-textbook-main.zip` cho ghi chú bài giảng. Hai nguồn này chỉ làm mẫu cách trình bày; không lấy nội dung, số liệu hay thứ tự chủ đề từ chúng thay cho nguồn ở mục 2.
5. `2627-1/lecture-template.html` và `2627-1/lecture-slide.css` về giao diện và nền kỹ thuật.
6. Các quy ước trong tệp này.

Giữ mạch, thứ tự và ý chính của nguồn. Chỉ gộp, tách, thêm, lược hoặc sắp xếp cục bộ khi cần sửa lỗi, giảm quá tải, khôi phục tiên quyết, hoàn thiện mạch học tập hoặc bảo đảm khả năng đọc. Mọi sai khác phải có lý do trong storyboard và nhật ký rà soát.

## Tiếp nhận và kiểm kê

Sau khi người dùng chọn tệp nguồn, điều phối viên phải:

- đọc tệp nguồn và kiểm tra các tài liệu liên quan trong `RL-hk2-2025-2026/resources/`;
- bỏ qua `.DS_Store`, tệp có tiền tố `._` và tệp tạm có tiền tố `~$`;
- xác định số bài, tên bài, mục tiêu, kiến thức tiên quyết, phạm vi, số trang và các tài sản được dùng;
- đọc `2627-1/lecture-template.html`, `lecture-slide.css` và `index.html` trước khi lập kế hoạch;
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
├── materials/
│   ├── _templates/            # lecture-note.md, exercises.md
│   └── lec-NN/
│       ├── lecture-note.md
│       ├── exercises.md
│       └── thuc-hanh-<chu-de>.ipynb
└── planning/
    └── lec-NN/
        ├── outline.md
        ├── storyboard.md
        └── review-log.md
```

- `outline.md` chứa mục tiêu, dàn ý, ánh xạ nguồn, sườn lý thuyết chung của bài (bài toán trung tâm, đối tượng và ký hiệu chung, giả thiết, chuỗi định nghĩa–kết quả–phương pháp, giới hạn áp dụng) và bảng thuật ngữ hoặc ký hiệu cần thiết.
- `storyboard.md` chứa bản đồ hành trình khái niệm và một mục cho từng trang chiếu.
- `review-log.md` chứa các báo cáo rà soát, quyết định chỉnh sửa, sai khác so với nguồn và ngoại lệ đã được duyệt.
- Tệp HTML nằm trực tiếp trong `2627-1/`. Không đặt tệp HTML trong thư mục planning hoặc img.
- Mọi đường dẫn trong HTML phải tương đối và hợp lệ khi máy chủ được mở tại thư mục gốc của kho.

## Mẫu RevealJS bắt buộc

- Dùng `2627-1/lecture-template.html` làm nền. Chỉ kế thừa cấu trúc, giao diện và cấu hình kỹ thuật; không sao chép chủ đề, nội dung hoặc siêu dữ liệu (metadata) của bài mẫu.
- Mọi bộ trang chiếu RevealJS trong `2627-1/`, kể cả `lecture-template.html`, phải dùng chung tệp `2627-1/lecture-slide.css` và liên kết bằng đường dẫn tương đối `href="lecture-slide.css"`. Đây là tệp CSS dùng chung cho giao diện bài giảng; không sao chép CSS thành tệp riêng cho từng bài hoặc tạo hệ giao diện mới. Kế thừa màu, phông chữ, khoảng cách, thẻ, lưới và chân trang từ tệp này.
- Các quy tắc giao diện có thể tái sử dụng phải đặt trong `lecture-slide.css`. Chỉ dùng CSS cục bộ trong HTML cho nhu cầu riêng của một trang mà CSS chung chưa đáp ứng; không ghi đè hệ giao diện chung. Các tệp CSS của RevealJS và tiện ích vẫn dùng theo mẫu kỹ thuật.
- Tham khảo cách tổ chức bố cục trong kho [uet-iai-course/machine-learning](https://github.com/uet-iai-course/machine-learning), ưu tiên `SLIDE_STYLE_GUIDE.md` và các tệp `2526-2/lecture-*.html`. Áp dụng các nguyên tắc một luận điểm trung tâm, hình hoặc công thức đủ lớn, chú thích nêu kết luận và nhịp mở phần–trực giác–cơ chế–ví dụ–kiểm tra. Không sao chép nội dung, tài sản hoặc CSS từ kho tham khảo; `lecture-template.html`, `lecture-slide.css` và các quy ước cục bộ vẫn có ưu tiên cao hơn.
- Giữ `lang="vi"`, khung `1280 × 720`, `controlsLayout: "edges"`, `slideNumber: true`, `hashOneBasedIndex: true` và `hash: true`.
- Dùng các thư viện cục bộ trong `2627-1/`: RevealJS, `RevealMath.KaTeX`, `RevealNotes` và `RevealHighlight`.
- Dùng `<section>` ngoài cho từng phần và `<section>` trong cho từng trang chiếu.
- Toàn bộ bài dùng từ 5 đến 7 mạch trình bày lớn, mỗi mạch tương ứng với một `<section>` ngoài; số này gồm mạch mở đầu và mạch kết luận. Chỉ dùng ngoài khoảng 5–7 khi nguồn hoặc yêu cầu cụ thể của người dùng đòi hỏi, và phải ghi lý do cùng ảnh hưởng đến mạch bài trong `storyboard.md` và `review-log.md`.
- Mạch mở đầu gồm, theo thứ tự: trang bìa (tên học phần, số bài, chủ đề, đơn vị, và một câu luận đề của bài: một câu trần thuật nêu kết quả hoặc cơ chế trung tâm, như "Chứng nhận nghiệm tối ưu bằng cận dưới." ở deck 03 hay "Ba cơ sở của bước lặp: …" ở deck 04 của học phần Cơ sở toán học cho AI); trang **Tiên quyết và quy ước** với dòng "Nhắc lại:" nêu các kết quả của bài trước được dùng và dòng "Ký hiệu:" nêu miền, kiểu và quy ước của bài (miền trạng thái, miền hành động, chính sách, chỉ số thời gian, kỳ vọng); mục tiêu học tập quan sát hoặc đánh giá được, mỗi mục tiêu ứng với một sản phẩm kiểm tra được; trang **Nội dung** liệt kê đánh số mọi mạch của bài, kể cả mạch mở đầu và mạch kết luận, số và tên trùng với trang tiêu đề mạch tương ứng, có thể thêm một dòng tài liệu đọc trước (giáo trình, chương, mục, như MAT1101 làm ở trang "Sách"); trang **Vấn đề trung tâm** nêu bài toán của bài trong một dòng và câu trả lời có điều kiện của từng mạch trong một dòng mỗi mạch, kèm hình khi có (có thể thay bằng một trang gộp "Nhắc lại: <kết quả bài trước>" + "Ví dụ. <trường hợp công cụ cũ còn giải được>" + "Nhu cầu: <giới hạn dẫn tới bài này>", như deck 04 làm với tính đủ của KKT); khi bài có khung chung cho mọi phương pháp (cấu trúc một bước lặp, cấu trúc một quy tắc cập nhật), một trang nêu khung đó bằng ba đến bốn dòng trước mạch nội dung đầu tiên; trang **Ngữ cảnh** khi bài dùng một khung chung (đối tượng, ký hiệu, giả thiết chung, tối đa bốn dòng) có thể gộp với trang tiên quyết. Mỗi mạch còn lại bắt đầu bằng một trang tiêu đề mạch theo mục "Trang tiêu đề mạch".
- Mạch kết luận cũng mở bằng trang tiêu đề mạch ("Tổng kết và chuyển tiếp" hoặc "Tổng hợp và vận dụng") và gồm: bảng tổng kết `Kết quả | Giả thiết không được bỏ | Công thức hoặc thuật toán`, mỗi kết quả chính của bài một hàng (MAT1101 kết bài bằng trang "Tóm tắt" liệt kê các công thức); khi bài có nhiều thuật toán, thêm bảng khung chung `Phương pháp | Quy tắc cập nhật | Dữ liệu dùng | Điều kiện dừng` và bảng `Phương pháp | Giả thiết không được bỏ | Kết luận` cho các định lý hội tụ (deck 04 dùng ba bảng như vậy cho bốn phương pháp Newton); một bài tập tổng hợp dùng nhiều kết quả của bài trên một bài toán Học tăng cường cụ thể, có lời giải trên mặt trang; một trang trả lời vấn đề trung tâm bằng kết luận có điều kiện, nêu giả thiết nào cho phép thay tập phương án hay chuỗi quyết định bằng cấu trúc nào, kèm dòng "Nguồn:" tổng hợp; trang **Câu hỏi tự kiểm tra** mở bằng "Câu hỏi: trả lời và nêu kết quả đã dùng." với hai đến bốn câu ngắn, mỗi câu kiểm một giả thiết hoặc một phân biệt; trang **Bài tập về nhà và tài liệu đọc** với bảng `Mạch | Bài tập` ánh xạ các bài trong `exercises.md` tới từng mạch (khi tệp bài tập đã có), dòng "Tài liệu đọc:" ghi tác giả, năm, mục, và dòng liên kết "Ghi chú bài giảng · Bài tập" trỏ tới viewer; một dòng nối sang bài kế tiếp khi có căn cứ từ nguồn. Không đưa khái niệm mới vào mạch kết luận.
- Mỗi trang có `data-slide-id` duy nhất. Mã này chỉ xuất hiện trong HTML, outline, storyboard và nhật ký; không hiển thị trên mặt trang chiếu hoặc trong ghi chú diễn giả.
- Đặt chân trang ở cuối `.slides` và cập nhật đúng tên học phần, học kỳ và số bài.
- Liên kết giữa các trang thể hiện quan hệ học thuật: kết quả nào được kế thừa, giả thiết nào được bổ sung hoặc thay đổi, giới hạn nào dẫn tới nhu cầu tiếp theo. Không dùng lời chỉ đường ("tiếp theo chúng ta…") thay cho quan hệ suy luận.
- Không phụ thuộc mạng cho các thành phần cốt lõi.
- Chỉ dùng tài sản cốt lõi đã có trong `2627-1/` hoặc tài sản SVG được tạo cho bài đang làm. Không tải phông chữ, thư viện hoặc hình từ mạng.

### Trang tiêu đề mạch

Mỗi mạch, trừ mạch mở đầu, bắt đầu bằng một trang tiêu đề mạch (yêu cầu người dùng 2026-10-12 cho học phần Cơ sở toán học cho AI, áp dụng cho học phần này). Trang bìa là trang tiêu đề của mạch mở đầu; không thêm trang "Mở đầu" riêng. Trang tiêu đề mạch là `<section>` trong đầu tiên của `<section>` ngoài tương ứng, mang lớp `strand-title`, và gồm:

- số thứ tự của mạch viết bằng chữ số ("2.", "3.", …), trùng với số trên trang "Nội dung" và với chỉ số ngang của RevealJS (`hashOneBasedIndex: true` nên mạch 3 mở tại `#/3`);
- tên mạch là cụm danh từ gọi tên khái niệm, bài toán hay kết quả, không dạng câu hỏi, không kể tiến trình; tên không trùng tiêu đề của trang nội dung đầu tiên trong mạch;
- một dòng dẫn, tối đa 25 âm tiết, nêu nhu cầu hoặc nhiệm vụ mà mạch giải quyết, mở bằng "Muốn …" hoặc nhãn "Nhu cầu:", là câu trần thuật, không kết thúc bằng dấu hỏi; dạng thường dùng là "Muốn <đích của mạch>, (trước hết) phải <việc mạch làm>" ("Muốn tìm tập ứng viên hữu hạn, phải mô tả toàn bộ miền khả thi và tính được các đỉnh bằng đại số"; trong Học tăng cường: "Muốn đánh giá một chính sách khi không có mô hình, phải ước lượng giá trị từ các lượt đã quan sát");
- tùy chọn một dòng từ khóa, tối đa năm cụm danh từ ngăn bằng " · ".

Cấu trúc HTML: khối `div.strand-title-body` chứa `<h2>` với số thứ tự trong `span.strand-number` đứng trước tên mạch, rồi `p.strand-lead` cho dòng dẫn và `p.strand-keys` cho dòng từ khóa. Kiểu của các lớp này nằm trong `lecture-slide.css`, không viết lại theo bài.

Không đặt định nghĩa, công thức trung tâm, hình hay bài tập trên trang tiêu đề mạch; không ghi "Mạch", "Đầu vào", "Đầu ra" hay mã trang trên mặt trang. Ghi chú diễn giả của trang này dài khoảng 40–100 âm tiết và nêu: kết quả hoặc ký hiệu kế thừa từ mạch trước, nhiệm vụ của mạch, và kết quả mạch giao cho mạch sau. Trang tiêu đề mạch không tính là một mạch và không đổi số mạch của bài. Nếu dòng dẫn nêu đúng nhu cầu của khái niệm đầu tiên trong mạch, storyboard có thể ghi trang này là bước `vấn đề` của khái niệm đó; nếu không, ghi "ngoài hành trình khái niệm". Nhãn phần bằng chữ cái `A`, `B`, `C` vẫn được dùng trong storyboard, dàn ý, học liệu và mã trang, nhưng không đặt trên mặt trang tiêu đề mạch.

Mã trang theo quy ước `<tiền tố mạch>00` (ví dụ `L05-B00`); nếu mã này đã có, dùng `<tiền tố>T` và ghi trong storyboard. Thuộc tính `id` của trang tiêu đề mạch là `mach-N`. Không đổi `id` của trang đã được học liệu liên kết tới. Các bộ trang chiếu đã phát hành trước quy định này được bổ sung trang tiêu đề mạch theo từng đợt sửa có nhật ký riêng; không sửa hàng loạt ngoài yêu cầu của người dùng.

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

### Các loại phần chính trong bộ trang chiếu

Mỗi `<section>` ngoài là một mạch trình bày có chức năng riêng đối với vấn đề trung tâm của bài. Mỗi mạch phải có điểm vào nhận kiến thức, kết quả hoặc vấn đề còn lại từ mạch trước và đầu ra đủ rõ để mạch sau sử dụng. Giữ quy mô 5–7 mạch theo mục “Mẫu RevealJS bắt buộc”; không chia một mạch liền lạc hoặc tạo phần trang trí chỉ để đạt số lượng.

Tổ chức các phần theo vai trò sau, đồng thời giữ thứ tự và ý chính của nguồn:

- **Mở đầu:** giới thiệu tên học phần, số bài, chủ đề và đơn vị theo thông tin đã xác minh; nêu mục tiêu có thể quan sát hoặc đánh giá, kiến thức tiên quyết, bản đồ nội dung và vấn đề trung tâm cần giải quyết. Viết vấn đề dưới dạng quyết định, bài toán hoặc giới hạn cụ thể, không dùng câu hỏi tu từ. Đầu ra của phần này là nhu cầu học khái niệm đầu tiên; không chỉ liệt kê mục lục.
- **Phát triển kiến thức:** mỗi phần giải quyết một khía cạnh của vấn đề trung tâm theo chu trình học tập bên dưới. Mở phần bằng nhu cầu chưa được giải quyết hoặc giới hạn của kết quả trước; xây dựng trực giác và ví dụ trước khi đưa định nghĩa, công thức hay thuật toán. Kết phần bằng kết quả có thể dùng tiếp và một câu nối nêu rõ nhu cầu của phần sau. Có thể có nhiều phần loại này, nhưng mỗi phần phải tạo một bước tiến riêng.
- **Ứng dụng và luyện tập:** dùng trực tiếp khái niệm, công thức hoặc thuật toán vừa xây dựng để tính, giải thích, so sánh hoặc ra quyết định trong một bài toán Học tăng cường. Nêu dữ kiện, yêu cầu và sản phẩm cần đạt; không đòi hỏi kỹ thuật hay giả thiết chưa được chuẩn bị. Gợi ý hoặc đáp án đặt trong ghi chú diễn giả. Mặc định đặt ứng dụng và câu hỏi kiểm tra ngay sau cụm khái niệm liên quan; chỉ tách thành phần riêng khi cần tổng hợp nhiều kết quả và nguồn cho phép. Phần tổng hợp không thay thế bước ứng dụng và kiểm tra của từng khái niệm trọng tâm. Mọi lời mời tương tác vẫn dùng nhãn **“Câu hỏi:”**.
- **Kết luận:** trở lại vấn đề mở đầu, đối chiếu kết quả đã đạt với mục tiêu học tập và nêu điều kiện áp dụng hoặc giới hạn cần nhớ. Có câu hỏi tự kiểm tra, bài tập và tài liệu đọc khi có căn cứ từ nguồn. Đầu ra là những việc người học có thể thực hiện sau bài và kiến thức cần mang sang bài tiếp theo nếu xác định được từ nguồn. Không chỉ lặp lại mục lục, không đưa khái niệm trọng tâm mới vào phần kết luận.

Các vai trò trên không tương ứng cứng với bốn `<section>` ngoài. Ứng dụng và luyện tập có thể nằm trong các phần phát triển kiến thức; mạch mở đầu và mạch kết luận luôn phải có. Phân bổ phần trình chiếu chính trong 120 phút; giữ 30 phút chữa bài tập và trình diễn mã theo phạm vi đã quy định, không tự bổ sung code demo.

Nếu nguồn có nội dung lịch sử, trình bày theo quan hệ **vấn đề hoặc giới hạn trước đó → nhu cầu mới → ý tưởng được đưa ra → hệ quả còn dùng hiện nay**. Chỉ giữ mốc thời gian, tên người và thuật toán khi chúng giải thích sự thay đổi phương pháp. Đặt nội dung này vào mạch khái niệm liên quan; chỉ tách thành phần riêng khi có chức năng rõ đối với vấn đề trung tâm. Không dùng danh sách niên đại tách rời lập luận hoặc lời ca tụng.

### Chu trình cho từng khái niệm

Mỗi khái niệm trọng tâm đi theo chu trình:

**vấn đề → trực giác → ví dụ → hình thức/thuật toán → ứng dụng → kiểm tra**

- **Vấn đề:** nêu quyết định, giới hạn hoặc bài toán cần giải quyết. Không dùng câu hỏi tu từ.
- **Trực giác:** dùng quan hệ trạng thái, hành động, phần thưởng, quỹ đạo hoặc giá trị để chuẩn bị cho ký hiệu.
- **Ví dụ:** dùng một trường hợp có thể tính, mô phỏng hoặc kiểm tra.
- **Hình thức/thuật toán:** nêu định nghĩa, công thức, giả mã, đầu vào, đầu ra và giả thiết.
- **Ứng dụng:** dùng trực tiếp kết quả vừa xây dựng trong một bài toán Học tăng cường.
- **Kiểm tra:** yêu cầu người học tính, giải thích, so sánh, chứng minh hoặc áp dụng.

Ví dụ dẫn nhập có thể đặt cùng hoặc ngay sau vấn đề, trước trực giác, theo chuỗi **vấn đề + ví dụ dẫn nhập → trực giác → hình thức/thuật toán → ứng dụng → kiểm tra**. Storyboard phải ghi rõ ví dụ làm cụ thể vấn đề nào và dữ kiện nào được dùng tiếp. Không mở đầu khái niệm trọng tâm bằng định nghĩa hoặc ký hiệu khi vấn đề, đại lượng và trực giác chưa được thiết lập.

Không bắt buộc sáu bước là sáu trang riêng. Có thể gộp khi trang vẫn có một luận điểm trung tâm. Với khái niệm phụ, có thể dùng chu trình rút gọn nếu storyboard ghi rõ lý do. Ngoài cách đặt ví dụ dẫn nhập đã nêu, không đảo thứ tự hoặc bỏ ngầm một bước đối với khái niệm trọng tâm.

### Phần về khái niệm

Phần về khái niệm phải giúp người học nhận diện đúng đối tượng, giải thích ý nghĩa và dùng được khái niệm trong bài toán đang học. Đây là một dạng phần phát triển kiến thức; không bắt buộc mỗi khái niệm có một `<section>` ngoài riêng.

Trình bày theo chu trình đã quy định, với các yêu cầu cụ thể:

1. **Vấn đề:** chỉ ra điều chưa mô tả, phân biệt hoặc tính được bằng kiến thức đã có; nêu vai trò của khái niệm mới trong việc giải quyết thiếu hụt đó.
2. **Trực giác:** giải thích đối tượng và quan hệ bằng lời hoặc hình trước khi đưa ký hiệu. Phân biệt rõ diễn giải trực giác với định nghĩa chính thức.
3. **Ví dụ:** dùng một trường hợp nhỏ có thể tính hoặc kiểm tra; xác định rõ dữ kiện và đại lượng đang xét. Khi phù hợp, thêm phản ví dụ hoặc trường hợp biên có căn cứ để làm rõ ranh giới của khái niệm.
4. **Hình thức:** phát biểu định nghĩa với miền xác định, kiểu đại lượng, ký hiệu và giả thiết cần thiết. Dùng lại dữ kiện và ký hiệu của ví dụ, hoặc nêu ánh xạ rõ ràng. Phân biệt định nghĩa, tính chất, định lý và nhận xét; với công thức, giải thích từng thành phần và ý nghĩa trong bài toán. Nếu cần chứng minh, nêu mục tiêu, ý tưởng, bước then chốt và điểm dùng giả thiết; tách suy diễn dài sang trang kế tiếp hoặc ghi chú.
5. **Ứng dụng:** dùng định nghĩa hoặc tính chất vừa xây dựng để giải quyết vấn đề đã nêu. Chỉ rõ kết quả nào được dùng tiếp trong khái niệm hoặc thuật toán sau.
6. **Kiểm tra:** yêu cầu người học nhận diện trường hợp thỏa định nghĩa, phân biệt khái niệm dễ nhầm, tính một đại lượng hoặc giải thích tác động khi thay giả thiết. Gợi ý và đáp án phải dựa trên kiến thức đã trình bày.

Không coi việc nêu tên, chép định nghĩa và liệt kê tính chất là đã hoàn thành phần khái niệm. Đầu ra phải là một năng lực có thể kiểm tra, chẳng hạn phân biệt trạng thái với quan sát hoặc tính giá trị từ một mô hình đã cho, khi phù hợp với nguồn.

### Phần về thuật toán

Phần về thuật toán phải giúp người học giải thích cơ chế, thực hiện được một bước hoặc một lượt lặp và xác định điều kiện sử dụng. Chỉ giới thiệu thuật toán sau các khái niệm và mục tiêu mà nó cần; không dùng giả mã để đưa ngầm kiến thức tiên quyết mới.

Trình bày theo chu trình đã quy định, với các yêu cầu cụ thể:

1. **Vấn đề:** nêu bài toán cần giải, đại lượng cần tìm và giới hạn của cách làm đã biết. Xác định đây là dự đoán hay điều khiển, có mô hình hay phi mô hình, theo chính sách hay khác chính sách khi các phân biệt này phù hợp.
2. **Trực giác:** giải thích thông tin thuật toán dùng, đại lượng nó thay đổi và cơ chế tạo ra thay đổi. Với quy tắc cập nhật, làm rõ ước lượng hiện tại, mục tiêu cập nhật và sai lệch giữa chúng trước khi viết công thức tổng quát.
3. **Ví dụ:** thực hiện bằng tay một bước hoặc một lượt lặp trên dữ kiện nhỏ, có giá trị khởi tạo và kết quả trung gian kiểm tra được. Giải thích phép tính bằng cơ chế vừa nêu, rồi dùng chính ví dụ này để chuẩn bị ký hiệu cho công thức và giả mã.
4. **Hình thức và quy trình:** nêu đầu vào, đầu ra, giả thiết, khởi tạo, tham số, công thức cập nhật, thứ tự thao tác và điều kiện dừng hoặc ngân sách chạy. Giả mã hay sơ đồ phải đủ rõ để lần theo ví dụ; phân biệt đại lượng cũ, mới và được giữ cố định. Với dữ liệu lấy mẫu, chỉ rõ nguồn mẫu và chính sách sinh dữ liệu khi phù hợp; xử lý trạng thái kết thúc và phân biệt kết thúc một lượt tương tác với dừng toàn bộ thuật toán.
5. **Ứng dụng và đánh giá:** dùng quy trình đầy đủ cho bài toán đã đặt, đối chiếu với bước tính tay và nêu cách đánh giá đầu ra. Trình bày chi phí tính toán, bộ nhớ, điều kiện hội tụ và giới hạn thực hành khi nguồn có hoặc khi thiếu sẽ gây hiểu sai. Phân biệt bảo đảm lý thuyết với tiêu chuẩn dừng thực hành; không coi hết ngân sách chạy hoặc một ví dụ thành công là bằng chứng hội tụ.
6. **Kiểm tra:** yêu cầu người học thực hiện bước tiếp theo, tìm lỗi trong cập nhật, giải thích vai trò của tham số hoặc chọn thuật toán dựa trên giả thiết đã học. Bài kiểm tra phải đo hiểu cơ chế và điều kiện áp dụng, không chỉ nhớ tên hay chép giả mã.

Nếu giới thiệu biến thể, nêu rõ giới hạn cần khắc phục, thành phần thay đổi và hệ quả đối với dữ liệu, mục tiêu cập nhật hoặc chi phí. Giữ ký hiệu chung để so sánh; không trình bày một danh sách thuật toán rời rạc. Ví dụ tính tay, công thức và giả mã phải cho kết quả nhất quán. Không tự bổ sung chương trình hoặc notebook để thay cho giải thích thuật toán.

Hai dạng phần trên vẫn tuân theo quy định về nguồn, cách đặt ví dụ dẫn nhập và việc gộp bước. Mọi bổ sung để khôi phục tiên quyết hoặc sửa thiếu sót của nguồn phải được truy nguyên và ghi lý do trong storyboard cùng nhật ký rà soát.

### Ghi nhận trong storyboard

Storyboard phải có bản đồ các phần, ghi loại phần, chức năng riêng, kiến thức đầu vào, kết quả đầu ra và đóng góp cho vấn đề trung tâm. Với từng trang, ghi lý do tồn tại, nhu cầu học tập được giải quyết, quan hệ với trang trước và sau, mục tiêu hoặc sản phẩm học tập được hỗ trợ, cùng quyết định `giữ`, `sửa`, `gộp`, `tách`, `thêm` hoặc `bỏ` và lý do. Không thêm trang chỉ để trang trí hoặc lặp kết luận; mọi thay đổi so với nguồn phải tuân theo thứ tự ưu tiên và được ghi trong nhật ký rà soát.

Storyboard phải chỉ ra cho từng cụm:

- mạch trình bày chứa cụm, chức năng của mạch, kết nối vào từ mạch trước và đầu ra cho mạch sau;
- mã trang thực hiện từng bước; nếu ví dụ dẫn nhập đứng trước trực giác, nêu rõ vấn đề mà ví dụ làm cụ thể;
- kiến thức đầu vào và sản phẩm học tập;
- dạng nội dung `khái niệm`, `thuật toán` hoặc kết hợp; với khái niệm, chỉ rõ năng lực nhận diện và sử dụng cần kiểm tra; với thuật toán, chỉ rõ tiên quyết, bước tính tay và trang chứa quy trình đầy đủ;
- ký hiệu hoặc dữ kiện được truyền từ ví dụ sang công thức hoặc thuật toán;
- bước được gộp hoặc ghi `không áp dụng`, kèm lý do;
- câu nối giữa các bước;
- thời lượng dự kiến của cụm và tổng thời lượng 120 phút.

Trang tiêu đề mạch có một mục riêng trong storyboard với đủ các trường trên; trường vị trí ghi "điểm vào mạch N". Bản đồ các phần ghi mã trang tiêu đề của từng mạch. Với mỗi trang vượt trần mật độ (mục "Văn phong và mật độ mặt trang chiếu") trước khi sửa, storyboard ghi số âm tiết trước và sau cùng quyết định `tách` hoặc `sửa`; với trang được phép vượt trần, storyboard ghi ngoại lệ kèm lý do.

## Tiêu chuẩn nội dung Học tăng cường

- Phân biệt rõ tác tử, môi trường, trạng thái, quan sát, hành động, phần thưởng, chính sách, mô hình và hàm giá trị khi các khái niệm này xuất hiện.
- Nêu miền, kiểu, kích thước, chỉ số thời gian, quy ước kỳ vọng và điều kiện dừng trước khi sử dụng.
- Dùng ký hiệu nhất quán từ ví dụ sang công thức, giả mã, ứng dụng và bài tập.
- Phân biệt bài toán dự đoán với điều khiển; theo chính sách với khác chính sách; có mô hình với phi mô hình; giá trị trạng thái với giá trị hành động khi phù hợp.
- Với quá trình quyết định Markov, nêu rõ giả thiết Markov, không gian, động lực chuyển, phần thưởng và hệ số chiết khấu.
- Với phương trình Bellman hoặc quy tắc cập nhật, kiểm tra chỉ số, điều kiện hóa, dấu, hệ số chiết khấu, mục tiêu cập nhật và đại lượng được giữ cố định.
- Với thuật toán, nêu đầu vào, đầu ra, giả mã hoặc sơ đồ, tiêu chuẩn dừng, chi phí chính, điều kiện hội tụ và giới hạn thực hành khi nguồn có hoặc khi thiếu chúng sẽ gây hiểu sai.
- Với học sâu trong Học tăng cường, phân biệt mạng trực tuyến, mạng mục tiêu, bộ nhớ phát lại, mục tiêu bootstrap, hành vi thăm dò và chính sách đánh giá khi phù hợp.
- Không tuyên bố hội tụ, tối ưu, không chệch hoặc ổn định nếu thiếu giả thiết quyết định kết luận.
- Tự tính lại các ví dụ số, xác suất, kỳ vọng, cập nhật giá trị và kích thước ten-xơ (tensor) quan trọng.
- Giữ nguồn truy nguyên được theo số trang hoặc số trang chiếu của bản nguồn. Chỉ bổ sung nguồn ngoài khi cần sửa hoặc kiểm chứng một mệnh đề và phải ghi nguồn cụ thể.

## Văn phong và mật độ mặt trang chiếu

Mặt trang chiếu là văn bản toán học ngắn gồm tiêu đề, vài dòng mệnh đề, công thức và nhãn. Diễn giải, động cơ chi tiết, đối chiếu ký hiệu và nguồn nằm trong ghi chú diễn giả; diễn giải dài hơn mức cần cho buổi giảng thuộc về ghi chú bài giảng. Các chuẩn trong mục này lấy từ bài giảng MAT1101 (Xác suất thống kê) của cùng tác giả tại `../MAT1101/` (13 bộ, 532 trang; trung vị 20 âm tiết chữ mỗi trang, 3 dòng, 6 âm tiết mỗi dòng; số đo và quyết định ghi tại `../math-4-AI/2627-1/planning/style-revision-2026-10-12.md`), và áp dụng cho mọi bộ trang chiếu của học phần.

### Mật độ chữ

Âm tiết được đếm bằng số từ tách theo khoảng trắng, không tính tiêu đề, công thức KaTeX, ô số của bảng, nhãn trong hình và ghi chú diễn giả.

- Mỗi trang nội dung nhắm tới không quá 40 âm tiết chữ; trần cứng 60 âm tiết. Trang mục tiêu, nội dung, tổng kết và bảng so sánh có trần 80 âm tiết.
- Không quá sáu dòng nội dung, không tính tiêu đề; mỗi gạch đầu dòng, câu, dòng nhãn hoặc khối công thức hiển thị tính là một dòng.
- Mỗi dòng chữ không quá 20 âm tiết. Câu dài hơn được tách, rút thành mệnh đề, hoặc chuyển sang ghi chú.
- Không quá ba khối công thức hiển thị; một hệ `aligned` tính là một khối. Giả mã dài hơn tám dòng tách sang trang riêng.
- Mỗi trang có nhiều nhất một khung nhấn chứa câu văn (`.question-box`, `.panel` hoặc tương đương); khung không chứa quá hai câu.
- Không dùng lớp hay thuộc tính thu nhỏ chữ để đạt các trần trên. Trang vượt trần phải được tách hoặc chuyển phần diễn giải sang ghi chú, và storyboard ghi quyết định `tách` hoặc `sửa`.
- Trang được phép vượt trần chỉ khi có ngoại lệ ghi trong `storyboard.md` kèm lý do. Tác tử rà soát xếp trang vượt trần không có ngoại lệ ở mức `trung bình`, trang vượt quá 1,5 lần trần ở mức `nghiêm trọng`.

### Câu trên mặt trang

- Viết mệnh đề toán học ngắn theo lối văn bản toán: "Đặt …", "Suy ra …", "Thế vào được …", "Do … nên …", "Với mỗi mẫu chuyển, cập nhật …". Không dùng "ta thấy", "rõ ràng", "chúng ta", lời chỉ đường hay câu hỏi tu từ trên mặt trang; "ta" chỉ xuất hiện trong dòng tính toán ("ta được …") khi không bỏ được.
- Định nghĩa viết bằng "là" hoặc "gọi là"; không dùng dấu "=" thay cho động từ.
- Một trang có nhiều nhất một câu kết luận cuối trang. Câu đó phải là một kết luận có điều kiện hoặc một con số ("Với $\alpha = 0{,}1$, $V(s_1)$ tăng từ $0$ lên $0{,}3$"); không dùng khẩu hiệu, ẩn dụ hay chuỗi mũi tên tóm tắt.

### Mở một khái niệm

Trang vấn đề mở bằng một câu "Muốn …" hoặc nhãn "Nhu cầu:", tiếp theo là một đến ba ví dụ dẫn nhập cụ thể, có số liệu hoặc đối tượng đếm được, theo đúng cách MAT1101 mở "Khái niệm xác suất có điều kiện" bằng "Muốn đánh giá xác suất khi có một phần thông tin" rồi ba ví dụ (hai xúc sắc, xét nghiệm dương tính, từ ghép). Trong Học tăng cường, ví dụ dẫn nhập là một môi trường nhỏ tính tay được (dãy ô, mê cung vài trạng thái, một lượt tương tác ghi rõ phần thưởng). Trang hình thức kế tiếp có thể giữ cùng tiêu đề với trang vấn đề. Bước trực giác đứng trước phát biểu hình thức; nhãn "Ý nghĩa:" sau một kết quả là diễn giải bổ sung, không thay cho bước trực giác.

Khi một phương pháp mới được đưa ra, mặt trang nêu giới hạn của phương pháp trước thành một dòng cụ thể (giáo trình của tác giả: "hàm chuyển và hàm phần thưởng thường không được biết trước nên hai thuật toán quy hoạch động không áp dụng được") rồi mới nêu ý tưởng mới. Không mở một thuật toán bằng tên hoặc giả mã.

### Trang phát biểu kết quả

Một trang định lý, mệnh đề hoặc bất đẳng thức gồm:
1. Phát biểu có giả thiết và kết luận.
2. Tùy chọn một dòng "Ý nghĩa:" đọc kết quả bằng lời (MAT1101: "Nếu phương sai nhỏ thì biến không quá xa khỏi kỳ vọng của nó").
3. Tùy chọn một dòng "Chứng minh." nêu ý chính khi chứng minh gói trong một đến hai dòng ("Áp dụng bất đẳng thức Markov cho $(X-\mu)^2$").

Chứng minh dài hơn đặt ở trang riêng có tiêu đề "Chứng minh: <tên kết quả>", chia bước, mỗi trang một kết quả. Không đặt định lý, chứng minh nhiều bước, ví dụ và nhận xét phạm vi trên cùng một trang. Với kết quả hội tụ, phát biểu nêu rõ giả thiết quyết định (tập hữu hạn, $\gamma<1$, điều kiện bước học, độ phủ) ngay trên mặt trang.

### Trang ví dụ

Tiêu đề có dạng "Ví dụ: <đối tượng>", trong đó đối tượng là cụm danh từ ("Ví dụ: dãy bốn ô", "Ví dụ: một lượt trên mê cung"). Trang theo thứ tự:
1. Dữ kiện có số: môi trường, chính sách, giá trị khởi tạo, tham số, mẫu chuyển hoặc lượt.
2. Yêu cầu bằng động từ học tập ("Tính …", "Xác định …").
3. Các bước, mỗi bước một dòng; với quy tắc cập nhật ghi rõ mục tiêu cập nhật, sai lệch và giá trị mới.
4. Kết quả kèm "Diễn giải:" hoặc dòng kiểm tra.

Khi một ví dụ kéo dài nhiều trang, mỗi trang thêm tên bước sau dấu phẩy, ví dụ "Ví dụ: dãy bốn ô, lượt thứ hai".

### Trang bài tập

Tiêu đề có dạng "Bài tập: <chủ đề>"; nhiều phần thì thêm "(a)", "(b)". Đề bài mở bằng nhãn "Câu hỏi:", được gõ bằng chữ và KaTeX, không chụp ảnh từ sách; dữ kiện dạng bảng dùng cùng khuôn bảng với ví dụ dẫn nhập để sinh viên nhận ra cấu trúc chung. Ghi chú diễn giả của trang đề bài nêu bài tập kiểm tra năng lực nào và một dòng "Gợi ý:" về bước mở đầu.
- **Bài tập có lời giải mẫu:** lời giải trình bày trên mặt trang dưới nhãn "Lời giải:", hiện bằng `fragment` hoặc ở trang kế tiếp cùng tiêu đề, mỗi dòng một bước lập luận, kết thúc bằng một kết luận ngắn (MAT1101: "Alice đúng", "Khi $\epsilon$ giảm còn một nửa thì $n$ cần tăng 4 lần").
- **Bài tập để người học tự làm:** gợi ý và lời giải đặt trong ghi chú diễn giả.

Mỗi cụm khái niệm lớn có ít nhất một bài tập có lời giải mẫu trên mặt trang. Storyboard ghi bài tập thuộc loại nào. Tiêu đề "Bài tập: …" là nhãn nội dung, không phải badge quy trình. Khi tệp `exercises.md` của bài có bài trùng với bài tập trên trang chiếu, hai lời giải phải cho cùng kết quả; tệp bài tập dẫn tới cả trang đề bài và trang lời giải.

### Ví dụ xuyên suốt

Mỗi bài chọn một đến hai môi trường hoặc tình huống nhỏ, tính tay được, và dùng lại qua nhiều khái niệm. Mỗi lần dùng lại phải trả lời một câu hỏi mới hoặc so sánh hai công cụ trên cùng số liệu (MAT1101 so cận Chebyshev với định lý giới hạn trung tâm trên cùng bài khảo sát ý kiến; trong Học tăng cường: Monte Carlo và TD(0) trên cùng một lượt, Sarsa và Q-learning trên cùng một chuyển). Gọi ví dụ bằng tên đối tượng ("dãy bốn ô", "mê cung ba phòng"), không bằng mã ("VD1"). Dữ kiện được nêu lại trên trang dùng lại. Khi bài có bài thực hành, ví dụ xuyên suốt nên là phiên bản thu nhỏ của môi trường trong bài thực hành (CartPole, LunarLander, Flappy Bird) để kết quả tính tay đối chiếu được với kết quả chạy.

### Bảng

Dùng bảng so sánh khi hai đến bốn phương pháp được đối chiếu theo cùng tiêu chí (dự đoán và điều khiển; theo chính sách và khác chính sách; Monte Carlo, TD(0) và quy hoạch động). Một phép tính lặp lại nhiều lần (bảng lặp giá trị, bảng cập nhật theo bước) dùng một khuôn bảng cố định với cùng tên cột trong toàn bài.

### Nhãn dẫn dắt

Chỉ dùng các nhãn sau, viết đậm:
- **Môi trường hình thức, kết thúc bằng dấu chấm:** "Định nghĩa.", "Định lý.", "Mệnh đề.", "Bổ đề.", "Hệ quả.", "Nhận xét.", "Thuật toán.", "Chứng minh.", "Trực quan.", "Ví dụ.".
- **Nhãn dẫn, kết thúc bằng dấu hai chấm:** "Nhu cầu:", "Ý nghĩa:", "Diễn giải:", "Lưu ý:", "Nhắc lại:", "Cách khác:", "Dạng khác:", "Ký hiệu:", "Giả thiết:", "Kết luận:", "Đầu vào:", "Đầu ra:", "Câu hỏi:", "Gợi ý:", "Lời giải:".

Không dùng nhãn quy trình, nhãn cảm thán hay nhãn quảng bá.

### Mã nội bộ của bài khác

Mặt trang phát biểu giả thiết và kết quả bằng lời, và gọi ví dụ bằng tên đối tượng. Mã nội bộ kiểu "T7", "H2", "VD1" không xuất hiện trên mặt trang. Sau phát biểu bằng lời được kèm số hiệu kết quả của ghi chú bài giảng, dạng "(Định lý 04.3)", tối đa một lần mỗi trang.

### Những điểm của MAT1101 không áp dụng

Không bắt chước: dấu cách trước dấu hỏi; câu hỏi không có nhãn; tiêu đề "Bài tập" không có chủ đề; đề bài dạng ảnh; dấu "=" thay cho "là"; thuật ngữ tiếng Anh hay viết tắt chưa giải thích; địa chỉ web trên mặt trang; lịch sử dạng danh sách năm–tên; trang thiếu ghi chú diễn giả.

## Tiêu chuẩn trang chiếu và ghi chú

- Mỗi trang chiếu có một luận điểm trung tâm. Tách phép suy diễn, giả mã hoặc bảng quá dài thay vì thu nhỏ chữ.
- Tiêu đề ngắn, có văn phong học thuật và gọi đúng khái niệm, bài toán hoặc kết quả. Không đặt tiêu đề dưới dạng “Tại sao...?”, “Vì sao...?”, “Từ ... đến ...”, lời kêu gọi, khẩu hiệu hoặc câu kể tiến trình giảng bài. Được dùng tiền tố chức năng trước cụm danh từ: `Ví dụ: <đối tượng>`, `Bài tập: <chủ đề>`, `Chứng minh: <tên kết quả>`; tiền tố không đứng một mình. Tiêu đề được lặp qua nhiều trang khi một khái niệm hay ví dụ kéo dài.
- Văn bản thân bài nên từ `0.75em` trở lên. Chỉ dùng dưới `0.65em` cho chú thích ngắn đã được tác tử góc nhìn sinh viên xác nhận là đọc được.
- Mỗi gạch đầu dòng không quá hai dòng ở khung 16:9. Chuyển diễn giải dài sang ghi chú diễn giả.
- Công thức trung tâm phải đủ lớn, có khoảng trắng và không bị cắt.
- Mọi lời mời tương tác trên mặt trang chiếu dùng nhãn **“Câu hỏi:”**.
- Mặt trang chiếu chỉ chứa nội dung học thuật và yêu cầu học tập. Không hiển thị chỉ dẫn biên soạn, điều hành lớp, thao tác trình chiếu hoặc lời dẫn như “hãy quan sát”, “ghi nhớ điểm này”, “chuyển sang phần tiếp theo”. Câu nối phải nêu quan hệ giữa các khái niệm hoặc kết quả; chỉ dẫn điều phối và thời lượng chỉ ghi trong tệp quy trình. Câu hỏi, bài tập và giả mã vẫn giữ yêu cầu thực hiện cần thiết.
- Không hiển thị mã nội bộ, nhãn quy trình, phân tuyến hoặc thời lượng trên mặt trang chiếu hay trong ghi chú diễn giả.
- Mỗi trang nội dung có `<aside class="notes">` khi cần giải thích giả thiết, công thức, lỗi dễ mắc, chuyển ý, đáp án hoặc nguồn.
- Ghi chú diễn giả là phần diễn giải học thuật ngắn bằng tiếng Việt: giả thiết, giải thích công thức hoặc hình, phân biệt dễ nhầm, quan hệ với nội dung kế tiếp và gợi ý hoặc lời giải. Gợi ý phải nêu cách lập luận hoặc bước tính; không chỉ dẫn giảng viên phải nói, nhấn mạnh hay điều phối lớp thế nào. Không chỉ chứa siêu dữ liệu và không lặp nguyên văn nội dung hiển thị.
- Ghi chú diễn giả nên dài khoảng 40–150 âm tiết; trang chứng minh hoặc lời giải có thể tới khoảng 250 âm tiết. Khoảng này là khuyến nghị: ghi chú dài hơn chỉ bị xếp mức `nhẹ`, và mọi ghi chú vẫn phải có đủ giả thiết, diễn giải, phân biệt dễ nhầm và lời giải khi trang có bài tập. Không mở ghi chú bằng “Trang này …”, “Slide này …” hoặc câu lấy tài liệu làm chủ ngữ; mở bằng đối tượng toán học hoặc kết quả kế thừa.
- Nguồn của trang (số trang hoặc trang chiếu của bản nguồn, mục của giáo trình) ghi trong ghi chú diễn giả hoặc trang tài liệu tham khảo, không ghi ở chân từng trang.
- Bộ trang chiếu phải dùng được bằng bàn phím, có tương phản đủ và không dùng màu làm tín hiệu duy nhất.

## Ghi chú bài giảng, bài tập và bài thực hành

- Ghi chú bài giảng và bài tập công khai của mỗi bài đặt tại `2627-1/materials/lec-NN/lecture-note.md` và `2627-1/materials/lec-NN/exercises.md`; mẫu tại `materials/_templates/`. Markdown là nguồn phát hành; hình dùng chung `img/lec-NN/`. Không dùng Node.js, trình sinh trang hoặc bước build; tệp được tải khi chạy bởi `2627-1/material-viewer.html` với JavaScript và CSS cục bộ.
- URL viewer chỉ nhận hai tham số cùng bài: `doc=materials/lec-NN/lecture-note.md` hoặc `doc=materials/lec-NN/exercises.md`, và `deck=lecture-NN-<ten-bai>.html`. Viewer từ chối đường dẫn ngoài quy ước, số bài không khớp và tài nguyên khác nguồn.
- Thứ tự xử lý bắt buộc là bảo toàn công thức → chuyển Markdown bằng Marked → làm sạch HTML bằng DOMPurify → khôi phục công thức dưới dạng nút văn bản → render bằng KaTeX. Chỉ dùng `$...$` và `$$...$$`.
- Viewer hỗ trợ mười bốn loại khối không lồng nhau bằng cú pháp `::: <loại> Tiêu đề tùy chọn` … `:::`: `definition`, `theorem`, `proposition`, `lemma`, `corollary`, `remark`, `algorithm`, `example`, `application`, `derivation`, `proof`, `exercise`, `hint` và `solution`. Tiêu đề thay cho nhãn mặc định của loại khối. Danh sách loại khối và nhãn tiếng Việt nằm ở một chỗ duy nhất, hằng `DIRECTIVE_LABELS` trong `material-viewer.js`. `proof`, `hint` và `solution` gập mặc định, dùng được bằng bàn phím và được mở khi in; các khối còn lại luôn mở.
- Mỗi tệp Markdown bắt đầu bằng một heading cấp một. Hình phải có văn bản thay thế; bảng phải có hàng tiêu đề; nguồn truy nguyên được theo cùng tiêu chuẩn của bộ trang chiếu.
- **Ghi chú bài giảng** là chương giáo trình tự chứa theo mục "Tiêu chuẩn giáo trình cho ghi chú bài giảng". Bộ trang chiếu là bản tóm lược của ghi chú, không phải ngược lại; khi hai bên mâu thuẫn, ghi chú là bản đầy đủ và được sửa trước. Không sao chép ghi chú diễn giả thành ghi chú bài giảng.
- **Tệp bài tập** `exercises.md` chứa bộ bài giao chính thức của buổi học theo ba mức: nhận biết; tính toán hoặc chứng minh; vận dụng vào một bài toán Học tăng cường cụ thể. Mỗi bài có `hint` và `solution` đầy đủ, dữ kiện nêu lại trong khối, số hiệu `Bài tập NN.k` dùng chung một bộ đếm với ghi chú bài giảng. Tệp mở bằng một đoạn nêu quan hệ với ghi chú (bài nào giữ số hiệu và lời giải của ghi chú, bài nào chỉ có ở tệp này) và một bảng `Mạch | Mở phần | Bài tập` dẫn tới trang tiêu đề mạch của bộ trang chiếu (`lecture-NN-<ten-bai>.html#/N/1`). Bài trùng với bài tập trên trang chiếu ghi dòng "Trùng trang chiếu" kèm liên kết, và lời giải trong tệp cho cùng kết quả với lời giải trên trang. Hai tệp không lặp đề bài của mục "Bài tập củng cố" trong ghi chú. Bài tập "[Lập trình]" và "[Tìm hiểu]" theo cách gọi của giáo trình *Học máy thống kê* được phép khi có nguồn hoặc bài thực hành tương ứng.
- **Bài thực hành** (yêu cầu người dùng 2026-10-03, Bài 04) là một notebook Jupyter `thuc-hanh-<chu-de>.ipynb` cho mỗi bài khi người dùng yêu cầu, nối tiếp kiến thức của bài giảng: dựng môi trường → thiết lập đánh giá qua nhiều lượt (cùng tập hạt giống; trung bình, độ lệch chuẩn, sai số chuẩn; so sánh ghép cặp) → thuật toán của bài, mỗi thuật toán có bước tính tay với `assert` trước bản đầy đủ → đánh giá trong môi trường thật → các gợi mở để sinh viên tự cải tiến. Notebook tự cài gói ở ô đầu (`%pip install -q …`), chạy được trên Jupyter cục bộ và Colab, không phụ thuộc tệp trong kho, được kiểm thử trong môi trường ảo rỗng. Trước mỗi ô mã chính có ô Markdown giải thích bằng ký hiệu của ghi chú bài giảng và ánh xạ ký hiệu → biến kèm kích thước mảng; mã có chú thích bước thuật toán. Trực quan hóa chính sách tham chiếu và chính sách học được ngay trên notebook bằng trình phát `<canvas>` nhẹ vẽ từ mảng trạng thái, kèm đồ thị tĩnh và dải ảnh hiển thị được khi không có JavaScript. Không dùng `assert` so với số liệu phụ thuộc phiên bản gói. Công khai mọi thử nghiệm sơ bộ dùng để chọn cấu hình; không khẳng định kết quả chạy ngoài notebook mà không nhúng dữ liệu. Quy trình: soạn → ba rà soát độc lập chỉ đọc (Học tăng cường và toán; góc nhìn sinh viên kèm kiểm thử độc lập; sư phạm và văn phong `no-ai-slop` Detect) → sửa → rà lại → kiểm tra cuối; nhật ký trong `planning/lec-NN/review-log.md`.
- Khi trang chiếu thay đổi ký hiệu, giả thiết, ví dụ, kết luận hoặc thứ tự khái niệm, phải rà lại ghi chú bài giảng, bài tập và bài thực hành của cùng bài. Tài liệu chỉ được công bố trên chỉ mục sau khi nguồn, công thức, liên kết, màn hình rộng, màn hình hẹp và bàn phím đã được kiểm tra.

## Tiêu chuẩn giáo trình cho ghi chú bài giảng

Mục này quy định `materials/lec-NN/lecture-note.md`. Ghi chú bài giảng là một chương giáo trình tự chứa: sinh viên đọc được trọn vẹn mà không cần mở bộ trang chiếu, không cần nghe giảng và không cần công cụ hỗ trợ bên ngoài.

### Tiêu chuẩn thứ nhất: trình bày theo ngữ cảnh để hiểu được bằng cách đọc

Phép thử duy nhất: một sinh viên có đủ kiến thức tiên quyết, đọc tệp từ đầu đến cuối theo thứ tự, không mở trang chiếu, không tra cứu ngoài và không dùng công cụ hỗ trợ, phải hiểu được từng câu tại chỗ câu đó xuất hiện. Mọi quy tắc dưới đây phục vụ phép thử này.

- **Vấn đề đi trước công cụ.** Mỗi mục `##` mở bằng một đoạn nêu bài toán cụ thể (môi trường, dữ kiện, số liệu khi được) mà công cụ hiện có chưa giải được, và nêu điều mục này sẽ làm rõ, viết như câu hỏi mà người đọc cùng tác giả đặt ra ("Để trả lời câu hỏi này, chúng ta cần…"). Giáo trình của tác giả mở mục Q-learning bằng giới hạn của quy hoạch động: hàm chuyển và phần thưởng không biết trước, nên hai thuật toán trước không áp dụng được; ghi chú làm theo cách đó. Không mở mục bằng định nghĩa, công thức hay danh sách.
- **Mỗi công thức được bao bởi lời.** Trước công thức có câu nói công thức tính gì và vì sao cần nó; sau công thức có câu đọc công thức bằng lời, nêu từng thành phần nghĩa là gì và đại lượng thu được dùng vào đâu. Không để hai công thức đứng liền nhau mà không có câu nối.
- **Ký hiệu được gọi tên khi xuất hiện.** Lần đầu một ký hiệu xuất hiện, câu chứa nó nêu tên gọi, kiểu và miền ("chính sách $\pi(a\mid s)$ là phân phối trên $\mathcal A$ với mỗi trạng thái $s$"). Bảng ký hiệu ở đầu chương là chỗ tra lại, không thay cho câu giới thiệu tại chỗ. Khi ký hiệu của học phần khác ký hiệu của giáo trình *Học máy thống kê* ($v_\pi$ so với $V^\pi$, $p(s',r\mid s,a)$ so với $T(s,a,s')$ và $R(s,a,s')$), bảng ký hiệu nêu tương ứng một lần.
- **Mỗi bước suy diễn nêu lý do.** Trong suy diễn và chứng minh, mỗi dấu bằng hoặc bất đẳng thức đi kèm căn cứ: định nghĩa nào, giả thiết nào, kết quả số hiệu nào, phép biến đổi nào (giáo trình của tác giả ghi "[do ERM]" bên cạnh dòng biến đổi và giải thích từng dòng của chứng minh toán tử co). Không có bước "dễ thấy", "suy ra ngay" hoặc dấu ba chấm.
- **Phát biểu toán học có bản đọc bằng lời.** Sau mỗi định nghĩa và định lý có một đoạn nói lại nội dung bằng tiếng Việt thường, nêu vai trò từng giả thiết và điều xảy ra khi bỏ một giả thiết, kèm ít nhất một ví dụ và một phản ví dụ hoặc trường hợp giới hạn (giáo trình của tác giả sau định lý PAC: đọc kết quả với $\epsilon = 1\%$, $n = 100\,000$, rồi hỏi giả thiết hữu hạn có thực tế không và trả lời bằng mô hình 64 bit). Dạng đã dùng cho ghi chú Bài 07 của học phần Cơ sở toán học cho AI: câu mở "Hai giả thiết của định lý có vai trò riêng, và mỗi giả thiết bị bỏ đều có phản ví dụ", rồi một danh sách "Bỏ <giả thiết>: <phản ví dụ cụ thể>" cho từng giả thiết, rồi một câu chỉ ra bước nào của chứng minh dùng giả thiết nào.
- **Ví dụ cụ thể trước phát biểu tổng quát.** Mỗi khái niệm trọng tâm có một ví dụ với số liệu được tính tay xuất hiện trước định nghĩa hoặc định lý tổng quát, rồi được nhắc lại sau phát biểu để chỉ ra phát biểu tổng quát bao hàm ví dụ này ở chỗ nào.
- **Nối mục bằng kết quả, không bằng lời dẫn.** Cuối mỗi mục có đoạn kết nêu ba điều: đã thu được kết quả gì (dẫn số hiệu), kết quả đó còn thiếu gì hoặc giả thiết nào còn hạn chế, và mục kế tiếp giải quyết thiếu hụt đó như thế nào. Ba điều này được kể trong một hoặc hai đoạn văn xuôi liền mạch ("Như vậy, chúng ta đã…", "Tuy nhiên, …", "Trong Mục N+1, chúng ta…"), không dùng nhãn "Kết mục", "Đích của mục" hay danh sách. Ở mỗi ranh giới mục, câu nối chỉ đặt ở một phía. Không dùng câu dẫn rỗng kiểu "tiếp theo ta xét".
- **Không tham chiếu ra ngoài tệp mà không đủ nội dung.** Cấm "như trên trang chiếu", "đã nói trong bài", "xem bài giảng". Kết quả của bài trước được dẫn bằng số hiệu và được phát biểu lại trong một câu đủ để dùng ngay. Tham chiếu tiến phải nêu rõ điều đang được tạm chấp nhận.
- **Câu đủ thành phần, đoạn có luận điểm.** Không chép câu mảnh kiểu gạch đầu dòng của trang chiếu thành văn ghi chú. Mỗi đoạn có một câu luận điểm. Danh sách chỉ dùng cho các mục thực sự song song (các bước thuật toán, các giả thiết, các trường hợp).
- **Nhầm lẫn thường gặp được nói thẳng.** Ở mỗi khái niệm, nêu cách hiểu sai phổ biến và lý do nó sai, bằng phản ví dụ hoặc chỉ ra giả thiết bị vi phạm.
- **Hình được đọc trong văn bản.** Mỗi hình có đoạn văn trước hoặc sau nói cần nhìn điều gì trên hình và điều đó ứng với công thức hay kết quả nào; `alt` mô tả đủ nội dung toán học.
- **Độ dài phục vụ việc đọc hiểu.** Ghi chú viết cho người đọc lần đầu, ưu tiên rõ ràng hơn ngắn gọn, và dài hơn phần ghi chú diễn giả của cùng bài. Một chương thường dài 8 000 đến 20 000 từ; dưới 6 000 từ cần lý do ghi trong `review-log.md`.

### Các nguyên tắc còn lại

- **Tự chứa.** Mọi ký hiệu, giả thiết, đối tượng và kết quả được dùng phải được định nghĩa hoặc phát biểu trong cùng tệp, hoặc dẫn tới số hiệu cụ thể trong ghi chú của bài trước (`Định lý 03.2`) kèm phát biểu lại.
- **Đầy đủ, không cắt cụt.** Mỗi lập luận được viết hết các bước; mỗi ví dụ tính đến kết quả số và kiểm tra lại; mỗi bài tập có lời giải.
- **Ví dụ và bài tập tự chứa tại chỗ** (yêu cầu người dùng 2026-10-10). Mỗi khối `example`, `application`, `exercise` nêu lại đầy đủ dữ kiện ngay trong khối: môi trường, chính sách, giá trị khởi tạo, tham số, mẫu chuyển, kết quả của bước trước mà khối dùng tới. Không viết "với dữ liệu của Ví dụ 04.2" rồi để sinh viên tua lại; nếu ví dụ nối tiếp một ví dụ trước, mở bằng một đoạn "Dữ kiện" chép lại các giá trị cần dùng kèm số hiệu nguồn trong ngoặc.
- **Hình thức.** Kiến thức được trình bày theo các môi trường có nhãn và số hiệu: Định nghĩa, Định lý, Mệnh đề, Bổ đề, Hệ quả, Ví dụ, Nhận xét, Chứng minh, Thuật toán, Bài tập, Tình huống áp dụng. Không trộn định nghĩa vào giữa đoạn văn giải thích; không phát biểu kết quả bằng lời rồi bỏ qua dạng toán học.
- **Giữ hành trình khái niệm.** Chu trình của bộ trang chiếu (vấn đề → trực giác → ví dụ → hình thức/thuật toán → ứng dụng → kiểm tra) được giữ đầy đủ trong ghi chú với mức chi tiết của giáo trình; với thuật toán, giữ thêm các yêu cầu ở mục "Phần về thuật toán".

### Tham khảo cách diễn giải của giáo trình

Khi soạn hoặc sửa một ghi chú, tác tử soạn phải đối chiếu với cách các giáo trình chuẩn trình bày cùng chủ đề và ghi vào `review-log.md` giáo trình nào, mục nào đã được tham khảo cho từng mục của chương. Giáo trình chuẩn của học phần: Sutton và Barto (2018) *Reinforcement Learning: An Introduction* cho toàn bộ học phần; Puterman (1994) *Markov Decision Processes* và Bertsekas (2019) *Reinforcement Learning and Optimal Control* cho quá trình quyết định Markov và quy hoạch động; Szepesvári (2010) *Algorithms for Reinforcement Learning* cho phát biểu gọn các thuật toán và điều kiện hội tụ; Bertsekas và Tsitsiklis (1996) *Neuro-Dynamic Programming* cho xấp xỉ hàm; Goodfellow, Bengio và Courville (2016) *Deep Learning* cho phần mạng trong Học tăng cường sâu; chương Học tăng cường của giáo trình *Học máy thống kê* của tác giả (`../SML-textbook-main.zip`, `chapters/06_reinforcement_learning/`) cho giọng kể, cách dẫn dắt và thuật ngữ tiếng Việt. Bộ trang chiếu nguồn trong `RL-hk2-2025-2026/` vẫn quyết định phạm vi và thứ tự.

Những điều cần học từ giáo trình và chuyển vào ghi chú:

- **Thứ tự dẫn dắt**: giáo trình đưa khái niệm nào trước, nêu nhu cầu bằng ví dụ nào, chỗ nào dừng lại giải thích trước khi phát biểu tổng quát. Khi ghi chú đổi thứ tự so với giáo trình, ghi lý do.
- **Cách đọc một định nghĩa hoặc định lý bằng lời**: câu diễn giải sau phát biểu, vai trò từng giả thiết, trường hợp đặc biệt và phản ví dụ mà giáo trình chọn. Ưu tiên các ví dụ kinh điển (dãy ô ngẫu nhiên, mê cung lưới, bài toán đánh bạc, CartPole) hơn là bịa ví dụ mới, trừ khi ví dụ mới là phiên bản thu nhỏ của môi trường trong bài thực hành.
- **Hình vẽ chuẩn**: sơ đồ dự phòng (backup diagram), lưới trạng thái, đồ thị giá trị theo bước, so sánh phương sai. Vẽ lại bằng SVG cục bộ với số liệu của chương, không sao chép hình.
- **Thuật ngữ và ký hiệu**: dùng thuật ngữ tiếng Việt đã quy ước trong học phần, ghi thuật ngữ gốc trong ngoặc ở lần đầu, giữ ký hiệu của Sutton và Barto khi không xung đột với bài.
- **Nhận xét và cảnh báo**: những điểm giáo trình nêu dưới dạng nhận xét, chú thích hoặc bài tập có lời giải mà sinh viên hay hiểu sai (mục tiêu cập nhật không phải giá trị thật; kết thúc lượt khác dừng thuật toán; chính sách hành vi khác chính sách đích).
- **Mức chặt chẽ**: theo mức giáo trình chọn cho đối tượng đại học; khi giáo trình bỏ qua một chứng minh, ghi chú hoặc bổ sung chứng minh ở mức đó hoặc dẫn nguồn có số trang, không phát biểu như thể đã chứng minh.

Giới hạn: tham khảo cách diễn giải, không dịch hoặc chép đoạn văn của giáo trình. Trích dẫn nguồn theo tác giả, năm, mục và trang trong "Hướng dẫn đọc thêm và tài liệu tham khảo", và dẫn tại chỗ khi một lập luận, ví dụ hay hình lấy ý từ giáo trình.

### Đoạn văn móc nối: quan hệ giữa khái niệm, kết quả và thực hành

Ghi chú không phải danh mục các định nghĩa và định lý đứng cạnh nhau. Mỗi đối tượng mới phải được gắn vào mạng kiến thức đã có bằng những đoạn văn móc nối viết rõ, có tên quan hệ và có số hiệu:

- **Khái niệm với khái niệm.** Ngay sau một định nghĩa mới có đoạn nêu quan hệ của nó với các khái niệm đã định nghĩa: là trường hợp đặc biệt của gì, tổng quát hóa gì, bổ sung cho gì, khác gì với khái niệm dễ nhầm ($q_\pi$ với $v_\pi$; mẫu chuyển với mô hình; kết thúc lượt với dừng thuật toán). Quan hệ được phát biểu bằng toán học khi có thể và được dẫn số hiệu.
- **Kết quả với kết quả.** Trước mỗi định lý có câu nêu định lý này cần kết quả nào trước đó; sau định lý có đoạn nêu nó mạnh hơn, yếu hơn hay mở rộng kết quả nào đã có, đổi giả thiết nào và trả giá bằng gì. Khi một định lý là hệ quả hay trường hợp riêng của định lý khác, viết thành `corollary` và chỉ ra bước suy ra.
- **Thuật toán với thuật toán.** Khi giới thiệu biến thể, nêu giới hạn cần khắc phục, thành phần thay đổi (mục tiêu cập nhật, chính sách hành vi, bộ nhớ, mạng mục tiêu) và hệ quả đối với dữ liệu, độ chệch, phương sai hoặc chi phí; giữ ký hiệu chung để so sánh.
- **Chuỗi suy luận của chương.** Mỗi mục `##` kể lại chuỗi định nghĩa → kết quả → thuật toán của mục bằng văn xuôi trong đoạn kết mục, dẫn số hiệu. Tóm tắt chương kể lại chuỗi này cho toàn bài trong một đoạn văn 5–8 câu đặt trước danh mục số hiệu.
- **Kết quả với thực hành.** Ngay sau mỗi định lý hoặc thuật toán chính có đoạn "Trong thực hành" (cách gọi của giáo trình *Học máy thống kê*) nêu cụ thể: đối tượng của kết quả ứng với gì khi cài đặt (bảng giá trị, bộ xấp xỉ tuyến tính hay mạng, bộ nhớ phát lại, chính sách hành vi); giả thiết của kết quả được bảo đảm hay vi phạm ra sao trong môi trường thật hoặc với xấp xỉ hàm (quan sát không Markov, chính sách thay đổi trong khi học, dữ liệu khác chính sách); kết luận cho phép làm gì hoặc giải thích hiện tượng gì đã quan sát (phân kỳ của bộ ba bất ổn, phương sai của Monte Carlo). Đoạn này dẫn tới tình huống áp dụng ở cuối chương, bài thực hành của bài hoặc bài khác của học phần. Không viết câu chung chung kiểu "kết quả này rất quan trọng trong thực tế".
- **Ứng dụng ngược về lý thuyết.** Mỗi tình huống áp dụng ở cuối chương dẫn ngược số hiệu của các định nghĩa, định lý và thuật toán mà nó dùng, và nêu bước nào của tình huống tương ứng với giả thiết nào.
- **Móc nối với bài trước và bài sau.** Mở chương nêu kết quả cụ thể của bài trước mà chương này xây tiếp (số hiệu, phát biểu lại một câu) và giới hạn của kết quả đó mà chương này vượt qua. Kết chương nêu giới hạn còn lại và bài nào của học phần xử lý tiếp. Chỉ dẫn tới bài đã có trong kho.

Mỗi đoạn móc nối là văn xuôi có luận điểm, không phải một dòng "Liên hệ: …".

### Cấu trúc bắt buộc của một chương

1. **Tiêu đề** cấp một: `# Bài NN — Tên bài`.
2. **Giới thiệu chương**: tối đa một đoạn ngắn, hoặc bỏ hẳn. Bài toán trung tâm được nêu ở đầu mục nội dung thứ nhất.
3. **Mục tiêu học tập**: danh sách kết quả quan sát được.
4. **Kiến thức tiên quyết**: mỗi mục là một gạch đầu dòng mở bằng tên nhóm kiến thức in đậm kèm số hiệu trong ngoặc ("**Phương trình Bellman kỳ vọng** (Định lý 03.4, Hệ quả 03.5).") rồi phát biểu lại kết quả trong một đến hai câu đủ để dùng ngay; mở mục bằng một câu quy ước cách đọc số hiệu ("Số hiệu `03.k` chỉ ghi chú Bài 03").
5. **Bảng ký hiệu**: bảng ba cột `Ký hiệu | Ý nghĩa | Miền hoặc kiểu`, khoảng 20 dòng, chỉ gồm ký hiệu dùng xuyên suốt chương; nêu miền trạng thái, miền hành động, chính sách, hệ số chiết khấu, chỉ số thời gian và quy ước kỳ vọng. Trước bảng một câu nêu phạm vi của bảng và quy tắc "mỗi chữ giữ một nghĩa trong cả chương"; sau bảng một đoạn nêu các quy ước đọc (bất đẳng thức theo thành phần, chỉ số thời gian của phần thưởng, số liệu sư phạm tự xây dựng).
6. **Bản đồ chủ đề** bốn nhóm `cốt lõi`, `cầu nối`, `bổ sung`, `đọc thêm` theo `prompt_lecture_note_deck.md`, mỗi chủ đề ghi mục tương ứng.
7. **Các mục nội dung** đánh số `## 1.`, `## 2.`, …; mỗi mục ứng với một mạch của bộ trang chiếu và tuân thủ mẫu ở phần "Mẫu trình bày một khái niệm". Mỗi chủ đề mang một `note-topic-id` duy nhất. Mục 1 mở bằng: kết quả của bài trước mà chương xây tiếp (số hiệu, một câu phát biểu lại), bài toán cụ thể có số liệu mà công cụ cũ chưa giải được, điều chương này chứng minh hoặc xây dựng, và hình minh họa cấu trúc của chương có đoạn đọc hình. Mỗi mục sau mở bằng một đoạn nhắc lại thiếu hụt của mục trước trên chính ví dụ xuyên suốt rồi nêu việc của mục.
8. **Tình huống áp dụng và ứng dụng**: mục riêng ở cuối phần nội dung (xem dưới).
9. **Tóm tắt chương**: mở bằng một đoạn văn 5–8 câu kể lại câu chuyện của chương (câu hỏi xuất phát, các bước đã đi, kết quả đích, giới hạn còn lại), dẫn số hiệu ngay trong câu; rồi đến **Định nghĩa và kết quả theo mục** (một gạch đầu dòng mỗi mục, mỗi kết quả một mệnh đề ngắn kèm số hiệu), **Công thức cần nhớ** trên dòng hiển thị, và **Giả thiết hay bị bỏ quên**.
10. **Bài tập củng cố**: ít nhất một bài cho mỗi mục tiêu học tập, chia ba tiểu mục `### Mức nhận biết`, `### Mức tính toán hoặc chứng minh`, `### Mức vận dụng`; mỗi bài có `hint` và `solution`. Tệp `exercises.md` chứa bộ bài giao chính thức; hai tệp không lặp đề bài.
11. **Hướng dẫn đọc thêm và tài liệu tham khảo**: tác giả, năm, tên, chương hoặc mục, trang hoặc trang chiếu của bản nguồn; nêu mục nào của chương dựa trên nguồn nào.

### Môi trường và đánh số

- Số hiệu theo bài và thứ tự xuất hiện trong bài, dùng chung một bộ đếm cho Định nghĩa, Định lý, Mệnh đề, Bổ đề, Hệ quả, Nhận xét và Thuật toán (`Định nghĩa 05.1`, `Định lý 05.2`, `Thuật toán 05.3`), một bộ đếm riêng cho Ví dụ (`Ví dụ 05.1`) và một bộ đếm riêng cho Bài tập (`Bài tập 05.1`). Mọi tham chiếu chéo dùng số hiệu, không dùng "định lý ở trên".
- Nhãn và số hiệu đặt ở tiêu đề khối: `::: theorem Định lý 04.2 (Toán tử Bellman là ánh xạ co)`. Tên gọi quen thuộc đặt trong ngoặc sau số hiệu.
- Khối `proof` đi ngay sau kết quả mà nó chứng minh và kết thúc bằng dấu $\square$. Chứng minh dài hơn một trang được tách bổ đề. Khối `algorithm` ghi đầu vào, đầu ra, giả thiết, khởi tạo, tham số, các bước đánh số, điều kiện dừng và chi phí mỗi bước.

### Mẫu trình bày một khái niệm

Mỗi khái niệm trọng tâm đi qua đủ các bước sau, theo thứ tự này, trong một hoặc nhiều tiểu mục `###`:

1. **Vấn đề**: quyết định, giới hạn hoặc bài toán chưa trả lời được bằng công cụ trước đó, nêu bằng ví dụ cụ thể có số liệu khi có thể.
2. **Trực giác**: mô tả bằng quan hệ trạng thái, hành động, phần thưởng, quỹ đạo hoặc giá trị (lời hoặc hình SVG có `alt`) điều khái niệm nắm bắt; mở bằng "Một cách trực quan", "Về mặt ý tưởng" và có một câu nói rõ đây chưa phải định nghĩa.
3. **Định nghĩa**: môi trường `definition`, ghi đủ miền, kiểu và chiều của mọi đối tượng, chỉ số thời gian, quy ước kỳ vọng, các giả thiết, ký hiệu được đưa vào. Ngay sau đó là một đoạn diễn giải từng thành phần và một hoặc hai ví dụ, phản ví dụ.
4. **Kết quả hoặc thuật toán**: môi trường `theorem`, `proposition` hoặc `lemma` theo mẫu bốn phần: giả thiết, kết luận, điều kiện áp dụng, phạm vi hoặc giới hạn; phân biệt $=$, $\approx$, $\propto$, hội tụ và tương đương. Với thuật toán, dùng `algorithm` và trước đó một ví dụ thực hiện bằng tay một bước hoặc một lượt theo mục "Phần về thuật toán".
5. **Chứng minh**: môi trường `proof` viết đủ các bước; khi chứng minh vượt phạm vi học phần, ghi rõ "Chứng minh nằm ngoài phạm vi học phần" kèm nguồn có số trang và nêu ý tưởng chính trong một đoạn.
6. **Ví dụ có lời giải**: môi trường `example` với dữ kiện đầy đủ, tính toán từng bước, kết quả số và một dòng kiểm tra lại. Ít nhất một ví dụ tính được bằng tay và, khi bài có bài thực hành, một ví dụ nối với môi trường của bài thực hành cho mỗi kết quả chính.
7. **Nhận xét**: môi trường `remark` cho giới hạn áp dụng, nhầm lẫn thường gặp, quan hệ với kết quả trước, điều gì thay đổi khi bỏ một giả thiết.
8. **Bài tập ngay sau mục**: một đến ba bài `exercise` kiểm tra đúng mục tiêu của tiểu mục, kèm `hint` và `solution` đầy đủ.

Các bước có thể gộp trong một tiểu mục nhưng không được đổi thứ tự và không được bỏ bước. Không mở một khái niệm bằng định nghĩa khi chưa có vấn đề và trực giác.

### Tình huống áp dụng và ứng dụng

- **Tình huống áp dụng** (`application`) là một bài toán Học tăng cường cụ thể được giải trọn vẹn bằng công cụ của chương: nêu bài toán và môi trường, mô hình hóa thành đối tượng của chương, xác minh các giả thiết của kết quả được dùng, áp dụng kết quả hoặc thuật toán, diễn giải kết luận trở lại bài toán ban đầu, nêu giới hạn. Mỗi chương có ít nhất hai tình huống, trong đó một tình huống nêu trường hợp giả thiết không thỏa và hậu quả. Khi bài có bài thực hành, một tình huống đối chiếu với kết quả của bài thực hành.
- **Ứng dụng** là danh mục ngắn các chỗ khái niệm xuất hiện trong các bài sau của học phần, trong Học tăng cường sâu hoặc trong bài thực hành, mỗi mục một hoặc hai câu nêu khái niệm nào của chương được dùng và dẫn tới bài hoặc nguồn tương ứng. Không liệt kê suông tên lĩnh vực.

### Trình bày sáng sủa: chứng minh và diễn giải

Chứng minh và đoạn diễn giải phải đọc được từng ý một (yêu cầu người dùng 2026-10-09):

- **Một ý một đoạn.** Đoạn văn diễn giải chỉ chứa một luận điểm và tối đa khoảng bốn câu. Không nối hai ý bằng dấu chấm phẩy hoặc "và" để tiết kiệm dòng.
- **Chứng minh theo bước.** Mỗi chứng minh dài hơn ba câu được chia thành các bước có nhãn in đậm trên dòng riêng (`**Bước 1 (toán tử co).**`): câu đầu nêu điều bước này thiết lập, các câu sau là lập luận, câu cuối nêu căn cứ. Chuỗi biến đổi nhiều hơn hai dấu bằng hoặc bất đẳng thức đặt trong `$$...$$` với `\begin{aligned}`, mỗi dấu một dòng, căn cứ ghi ở cột phải bằng `&&\text{(...)}` hoặc ở câu ngay sau công thức.
- **Trường hợp và điều kiện thành danh sách.** Phân chia trường hợp, kiểm tra nhiều điều kiện, hoặc nhiều kết luận (a), (b), (c) viết thành danh sách, mỗi mục một dòng.
- **Công thức quan trọng trên dòng riêng.** Công thức dài hơn nửa dòng, công thức được tham chiếu về sau (đánh số `\tag{3.4}` theo số mục) và kết luận của một bước luôn đặt ở `$$...$$`.
- **Tách phần của phát biểu.** Trong định lý, bốn phần Giả thiết, Kết luận, Điều kiện áp dụng, Phạm vi mỗi phần là một đoạn riêng; trong định nghĩa, các đối tượng được định nghĩa liên tiếp tách dòng.
- **Ví dụ và lời giải.** Các giai đoạn (lập mô hình, kiểm giả thiết, tính, diễn giải, kiểm tra lại) mở bằng nhãn in đậm trên dòng riêng. Mỗi phép tính có kết quả trung gian được ghi; với quy tắc cập nhật ghi mục tiêu, sai lệch và giá trị mới trên ba dòng.
- **Hạn chế ngoặc đơn lồng.** Không quá một ngoặc đơn trong một câu; chú thích dài chuyển thành câu riêng.

Tác tử rà mạch viết kiểm tiêu chí này ở mọi khối `proof`, `derivation`, `solution` và mọi đoạn diễn giải; chỗ không đạt ghi mức `trung bình`.

### Kiểm định ghi chú bài giảng

Trước khi công bố trên chỉ mục, tác tử rà soát lập bảng đối chiếu theo các mục sau, ghi kết quả vào `review-log.md`:

- mỗi mục tiêu học tập có ít nhất một kết quả hoặc ví dụ và một bài tập tương ứng;
- mỗi khái niệm trọng tâm của `storyboard.md` đi đủ tám bước của mẫu trình bày; mỗi thuật toán có bước tính tay trước giả mã và hai bản cho kết quả nhất quán;
- mỗi ký hiệu dùng trong chương có mặt trong bảng ký hiệu; miền, chỉ số thời gian và quy ước kỳ vọng được nêu trước khi dùng;
- mỗi định lý có đủ bốn phần và có chứng minh hoặc nguồn có số trang; không có tuyên bố hội tụ, tối ưu, không chệch hoặc ổn định thiếu giả thiết quyết định;
- mỗi ví dụ có kết quả số và dòng kiểm tra lại; các con số được tính lại độc lập bởi tác tử rà toán;
- mỗi bài tập có `hint` và `solution` đầy đủ;
- không có tham chiếu "xem trang chiếu", không có câu mảnh, không có bước suy diễn bị bỏ;
- chứng minh chia bước có nhãn, chuỗi biến đổi trong `aligned` mỗi dấu một dòng, trường hợp thành danh sách, đoạn diễn giải một ý một đoạn;
- số hiệu liên tục, tham chiếu chéo trỏ đúng, các khối không lồng nhau và render đúng ở màn rộng, màn hẹp;
- mỗi định nghĩa có đoạn nêu quan hệ với khái niệm đã có; mỗi kết quả có đoạn nêu quan hệ với kết quả trước và đoạn "Trong thực hành" nêu đúng đối tượng, giả thiết và kết luận; mỗi mục kể được chuỗi suy luận bằng văn xuôi ở đoạn kết mục; mở và kết chương có móc nối với bài trước và bài sau;
- mỗi công thức có câu dẫn trước và câu đọc sau; mỗi ký hiệu được gọi tên tại lần xuất hiện đầu; giọng kể "chúng ta/ta" đúng quy định và tài liệu không làm chủ ngữ;
- mỗi mục có ghi trong `review-log.md` giáo trình và mục đã tham khảo cách diễn giải; không có đoạn dịch hoặc chép;
- nội dung, ký hiệu và giả thiết nhất quán với bộ trang chiếu và bài thực hành cùng bài; chỗ lệch được ghi và sửa ở bộ trang chiếu.

Tiêu chuẩn này áp dụng cho ghi chú mới và là đích rà soát lại cho các ghi chú đã công bố. Việc nâng cấp một ghi chú đã có đi qua quy trình đa tác tử rút gọn: tác tử soạn viết lại theo mẫu, tác tử rà toán tính lại toàn bộ số liệu, tác tử rà mạch viết kiểm tra tám bước và liên kết mục, điều phối viên duyệt rồi mới cập nhật chỉ mục.

## Quy trình đa tác tử

### 1. Điều phối và lập kế hoạch

Điều phối viên kiểm kê nguồn và xác nhận đầu ra. Giao một tác tử lập kế hoạch riêng trước khi phân tích chi tiết hoặc sửa tệp.

Tác tử lập kế hoạch:

- xác định mục tiêu, phạm vi, đối tượng, thời lượng và tiêu chí hoàn thành;
- xác định sườn lý thuyết chung và quan hệ phụ thuộc giữa các kết quả; lập danh mục khái niệm trọng tâm và bản đồ chu trình học tập;
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
- viết tiêu đề, nội dung và ghi chú bằng tiếng Việt theo văn phong học thuật; biên tập bằng `no-ai-slop` và tự kiểm theo `eval.md`;
- dùng `quill` để kiểm tra mạch phần, chuyển ý, thuật ngữ và ký hiệu;
- giữ thứ tự nguồn trừ các thay đổi đã được phê duyệt;
- thêm ghi chú diễn giả và nguồn;
- không sửa RevealJS, tiện ích (plugin) hoặc CSS dùng chung nếu có thể giải quyết trong tệp bài giảng;
- nếu cần sửa `lecture-slide.css`, phải kiểm tra mẫu và tất cả các bài hiện có sử dụng tệp này không bị hỏng bố cục hoặc khả năng đọc.

### 4. Kiểm định storyboard

Giao một tác tử chỉ đọc rà từng trang và từng cụm khái niệm:

- kiểm tra lý do tồn tại của từng trang có cụ thể và kiểm chứng được;
- kiểm tra trang tạo một bước tiến trong lập luận hoặc luyện tập;
- kiểm tra chức năng từng loại phần theo mục “Các loại phần chính trong bộ trang chiếu”, đầu vào–đầu ra giữa các phần và việc kết luận giải quyết vấn đề mở đầu;
- kiểm tra chu trình sáu bước đúng thứ tự, kể cả cách đặt ví dụ dẫn nhập được phép, và nối được từ ví dụ sang hình thức;
- đối chiếu phần khái niệm và phần thuật toán với yêu cầu riêng tương ứng; kiểm tra ranh giới trực giác–định nghĩa, tiên quyết trước thuật toán và sự nhất quán giữa ví dụ tính tay, công thức, giả mã và câu hỏi kiểm tra;
- phát hiện trang trùng ý, trang trang trí, trang quá tải và khoảng trống cần bổ sung;
- kiểm tra mỗi mạch trừ mạch mở đầu có trang tiêu đề mạch đúng mục "Trang tiêu đề mạch", số và tên khớp trang "Nội dung", và trang nội dung đầu mạch không trùng tiêu đề với tên mạch;
- kiểm tra thời lượng 120 phút, kiến thức tiên quyết và quan hệ trước–sau;
- đề xuất quyết định, bằng chứng và tác động đến trang lân cận;
- không sửa tệp.

Sau thay đổi số lượng hoặc thứ tự, phải rà lại các trang bị ảnh hưởng và hai trang lân cận mỗi phía.

### 5. Năm tác tử rà soát độc lập

Sau bản nháp đầu, giao đủ năm vai cho năm tác tử chỉ đọc độc lập; chạy song song trong giới hạn số tác tử khả dụng, chia lượt khi cần. Các tác tử phải rà cùng một bản đã cố định. Mỗi báo cáo dùng các trường `mức độ`, `trang chiếu`, `vấn đề`, `bằng chứng`, `đề xuất sửa`.

- **Góc nhìn sinh viên:** kiểm tra tiên quyết, tải nhận thức, nhịp giảng, khả năng đọc, ví dụ, chuyển ý, câu hỏi kiểm tra và khả năng tự học. Đo số âm tiết chữ của từng trang theo mục "Văn phong và mật độ mặt trang chiếu"; trang vượt trần mà không có ngoại lệ ghi trong storyboard xếp mức `trung bình`, trang vượt quá 1,5 lần trần xếp mức `nghiêm trọng`.
- **Chuyên gia Học tăng cường:** kiểm tra độ bao phủ, chiều sâu, thuật ngữ, mạch học thuật, quan hệ với học máy và sự phù hợp với 120 phút.
- **Độ chính xác toán học và thuật toán:** kiểm tra định nghĩa, giả thiết, xác suất, kỳ vọng, chỉ số, công thức Bellman, quy tắc cập nhật, giả mã, kết quả số, hội tụ, độ phức tạp và kích thước tensor.
- **Phản biện học thuật và giảng dạy Học tăng cường–lập kế hoạch:** đóng vai chuyên gia nghiên cứu và giảng dạy để phản biện công thức, thuật toán và trình tự kiến thức; kiểm tra mỗi hình thức hóa có đủ trực giác, ví dụ và tiên quyết, mỗi thuật toán có xuất hiện đúng chỗ trong mạch học tập, và thứ tự hiện tại có hỗ trợ việc suy luận trên lớp hay không. Tác tử này phải nêu rõ khi một công thức đúng riêng lẻ nhưng được đặt sai trình tự hoặc thiếu cầu nối sư phạm.
- **Kết nối và mạch viết:** kiểm tra xương sống lập luận của toàn bài, điểm xuất phát, đích đến và sự tích lũy ý nghĩa qua từng phần; xác nhận bài có từ 5 đến 7 mạch trình bày lớn tương ứng với các `<section>` ngoài, gồm mạch mở đầu và mạch kết luận, trừ ngoại lệ đã được ghi rõ. Với mỗi phần, xác định chức năng, kết nối vào từ phần trước, đầu ra cho phần sau và đóng góp vào mục tiêu bài học; với mỗi trang, kiểm tra vai trò trong mạch cùng câu nối với trang liền trước và liền sau. Phát hiện bước nhảy lập luận, chuyển phần đột ngột, trang đứng riêng lẻ, phần lặp chức năng, tuyến không tiến triển, kết luận không thu hồi vấn đề mở đầu hoặc nhiều trang tranh cùng một luận điểm trung tâm. Vai này không thay thế kiểm định storyboard, rà độ chính xác hay rà tải nhận thức. Trong `bằng chứng` và `đề xuất sửa`, phải nêu rõ `vai trò trong mạch`, `kết nối vào` và `kết nối ra` của trang hoặc cụm trang bị ảnh hưởng.

Mức độ gồm `chặn bàn giao`, `nghiêm trọng`, `trung bình`, `nhẹ`. Mọi lỗi `chặn bàn giao` và `nghiêm trọng` phải được xử lý.

Vai phản biện học thuật và giảng dạy đồng thời rà văn phong của tiêu đề, nội dung và ghi chú bằng chế độ Detect của `no-ai-slop`. Báo cáo phải trích dẫn cụ thể văn nói, lời dẫn rỗng hoặc chỉ dẫn điều phối còn xuất hiện; đề xuất sửa phải giữ nguyên điều kiện toán học và ý nghĩa thuật toán.

Đối với vai kết nối và mạch viết, dùng mức `chặn bàn giao` khi thiếu mạch mở đầu hoặc mạch kết luận, số mạch ngoài khoảng 5–7 mà không có ngoại lệ hợp lệ, không xác định được tuyến chính hoặc kết luận mâu thuẫn với vấn đề đã thiết lập; `nghiêm trọng` khi một phần trọng tâm bị đứt khỏi tuyến chính, lặp chức năng hoặc không tạo bước tiến; `trung bình` khi điểm vào, đầu ra hay câu chuyển giữa hai phần còn mờ; `nhẹ` khi mạch đúng nhưng tín hiệu chuyển ý hoặc thứ bậc nhấn chưa rõ. Sau khi thêm, bỏ, gộp, tách, đổi thứ tự trang hoặc sửa câu chuyển làm thay đổi mạch bài, phải giao lại vai này rà các trang bị ảnh hưởng, hai trang lân cận mỗi phía và mọi ranh giới phần liên quan. Nếu thay đổi mở bài, kết bài hoặc luận điểm trung tâm, phải rà lại toàn bộ bộ trang chiếu.

### 6. Chỉnh sửa

Giao một tác tử chỉnh sửa riêng sau khi năm báo cáo hoàn tất:

- hợp nhất vấn đề trùng lặp và ưu tiên tính đúng, khả năng học, khả năng đọc;
- sửa tuần tự HTML, SVG, outline, storyboard và ghi chú;
- ghi quyết định đối với đề xuất không áp dụng;
- không thay đổi mạch nguồn nếu lỗi có thể sửa cục bộ;
- yêu cầu rà lại độ chính xác cho mọi phần toán học hoặc thuật toán đã đổi đáng kể.
- yêu cầu tác tử kết nối và mạch viết rà lại theo phạm vi ở mục 5 sau mọi thay đổi cấu trúc, thứ tự, câu chuyển hoặc luận điểm trung tâm.

Các tác tử sửa tệp không được chạy song song. Sau mỗi lần sửa, điều phối viên đọc diff và ghi quyết định `chấp nhận | yêu cầu sửa | bác bỏ` theo mục "Điều phối mô hình trong dự án".

### 7. Kiểm định cuối

Điều phối viên hoặc tác tử kiểm thử riêng phải:

- đối chiếu số trang nguồn, bảng ánh xạ, `data-slide-id` và mục tương ứng trong storyboard;
- kiểm tra HTML, cấu trúc `<section>`, KaTeX, tiện ích, ghi chú diễn giả, đường dẫn, SVG và liên kết;
- kiểm tra mọi bộ trang chiếu và mẫu liên kết đúng tới CSS dùng chung `lecture-slide.css`; không có bản sao CSS giao diện riêng cho từng bài hoặc liên kết tới tên CSS cũ;
- kiểm tra bài có từ 5 đến 7 `<section>` ngoài, gồm mạch mở đầu và mạch kết luận, hoặc có ngoại lệ hợp lệ đã được ghi trong storyboard và nhật ký;
- đối chiếu loại phần, chức năng, đầu vào, đầu ra và đóng góp cho vấn đề trung tâm giữa storyboard và HTML; kiểm tra mở đầu thiết lập nhu cầu, các phần kiến thức tạo bước tiến và kết luận thu hồi mục tiêu đã nêu;
- tìm mọi tham chiếu ảnh raster; chỉ chấp nhận mục có ngoại lệ đã được người dùng duyệt và ghi trong nhật ký;
- chạy phép đếm mật độ (âm tiết chữ, số dòng, âm tiết mỗi dòng) cho mọi trang và đính kèm kết quả; xác nhận không trang nào vượt trần mà không có ngoại lệ ghi trong storyboard, và không trang nào dùng lớp thu nhỏ chữ để đạt trần;
- kiểm tra mọi trang tiêu đề mạch hiển thị đúng ở 1600×900 và 390×844, số mạch khớp `#/N` và trang "Nội dung";
- khi bài có ghi chú, bài tập hoặc bài thực hành, kiểm tra ký hiệu, giả thiết, ví dụ và thứ tự khái niệm nhất quán với bộ trang chiếu, và viewer mở được cả `lecture-note.md` lẫn `exercises.md` không lỗi KaTeX;
- kiểm tra không có tài nguyên hỏng hoặc phụ thuộc mạng cốt lõi;
- chạy `python3 -m reloadserver 8765` tại thư mục gốc; cổng là đối số vị trí, không dùng `--port`;
- mở `http://localhost:8765/2627-1/lecture-NN-<ten-bai>.html` và duyệt mọi trang ngang, trang dọc;
- kiểm tra tràn chữ, chữ nhỏ, chồng lấn, công thức, hình, tương phản và bàn phím ở khung 16:9 và một màn hình hẹp;
- rà soát trực quan sau cùng bằng trình duyệt (Chromium không giao diện qua Playwright), lưu ảnh chụp ở khung 16:9 và màn hình hẹp làm bằng chứng cho các trang bị ảnh hưởng, và xác minh thay đổi đã lưu trong tệp của kho hiển thị đúng;
- kiểm tra đủ năm báo cáo độc lập; mọi vấn đề về vai trò trong mạch, kết nối vào–ra và tuyến lập luận phải có quyết định cùng bằng chứng rà lại;
- kiểm tra tiêu đề, nội dung, ghi chú và học liệu có văn phong trang trọng, học thuật; không còn văn nói mô phỏng hoặc chỉ dẫn điều phối trên trang chiếu và trong ghi chú; xác nhận phạm vi biên tập cùng kết quả tự kiểm `no-ai-slop` trong nhật ký;
- chạy lại kiểm định sau mỗi lần sửa lỗi chặn bàn giao hoặc nghiêm trọng.

Nếu không mở được trình duyệt để rà soát trực quan, phải báo rõ giới hạn, tiếp tục đầy đủ các kiểm tra tĩnh còn lại và không tuyên bố đã kiểm tra trực quan.

## Cập nhật `index.html`

- `2627-1/index.html` là danh mục riêng của học phần **Học tăng cường** cho học kỳ 1 năm học 2026–2027.
- Khi chuyển bài Học tăng cường đầu tiên, bỏ các thẻ của học phần Cơ sở toán học cho AI hiện có.
- Mỗi bài hoàn thành có một thẻ theo thứ tự số bài, gồm nhãn `Bài N`, tên bài, mô tả một câu và một hàng tài nguyên gồm bốn nhóm: **Bài giảng** (liên kết tới `lecture-NN-<ten-bai>.html`), **Ghi chú bài giảng** và **Bài tập** (liên kết qua `material-viewer.html?doc=materials/lec-NN/{lecture-note,exercises}.md&deck=lecture-NN-<ten-bai>.html`, chỉ khi Markdown đích đã vượt kiểm định) và **Thực hành** (liên kết "Mở trên Colab" tới `https://colab.research.google.com/github/uet-iai-course/reinforcement-learning-planning/blob/main/2627-1/materials/lec-NN/<file>.ipynb` và liên kết tải `.ipynb`; một bài có nhiều notebook thì nhiều nút đặt tên theo môi trường). Tài liệu chưa có hiển thị `Chưa có` dưới dạng trạng thái, không phải liên kết giả. Quy định này thay cho quy tắc một liên kết duy nhất trước đây.
- Không đặt liên kết đến `outline.md`, `storyboard.md`, `review-log.md`, `note-for-author.md` hoặc thư mục `planning/` trên trang chỉ mục. Các tệp quy trình chỉ dùng nội bộ trong kho.
- Không thêm bài chưa hoàn thành hoặc liên kết đến tệp chưa tồn tại.
- Giữ giao diện của trang chỉ mục hiện có trừ nội dung nhận diện học phần và danh sách bài.

## Tiêu chí hoàn thành

Chỉ bàn giao khi:

- bản RevealJS giữ đúng ý chính và mạch nguồn, còn mọi sai khác đều được ghi;
- tiêu đề, nội dung, ghi chú diễn giả và học liệu bằng tiếng Việt, có văn phong trang trọng, học thuật; đã biên tập và tự kiểm theo `no-ai-slop`, không còn văn nói mô phỏng hoặc chỉ dẫn điều phối trong sản phẩm;
- outline, storyboard và nhật ký nằm đúng `planning/lec-NN/`; mỗi mạch trừ mạch mở đầu có trang tiêu đề mạch; không trang nào vượt trần mật độ mà không có ngoại lệ trong storyboard;
- ghi chú bài giảng, bài tập và bài thực hành của bài (nếu có) nhất quán với bộ trang chiếu và đạt các tiêu chuẩn tương ứng;
- mọi hình đã được vẽ lại thành SVG hoặc có ngoại lệ raster được người dùng duyệt;
- năm báo cáo độc lập đã có và mọi lỗi bắt buộc đã được xử lý;
- công thức, ví dụ số, giả mã và giả thiết đã được kiểm tra;
- bộ trang chiếu chạy tại cổng `8765`, không có lỗi hiển thị hoặc tài nguyên hỏng nghiêm trọng;
- `index.html` liên kết đúng tới tệp HTML của bài và không liên kết tới các tệp quy trình;
- bản RevealJS trong kho là đúng phiên bản đã được rà soát trực quan trên trình duyệt, hoặc giới hạn công cụ đã được ghi rõ.

Khi bàn giao, nêu ngắn gọn: tệp trang chiếu, URL cục bộ, tệp nguồn, hình đã vẽ lại, các kiểm tra đã chạy, sai khác có chủ ý, ngoại lệ và giới hạn còn lại.

## Điều phối mô hình trong dự án

- Phiên Claude Code chính giữ vai trò điều phối viên và kiểm soát chất lượng, chạy **Claude Opus 5.5** (`claude-opus-5-5`) (yêu cầu người dùng 2026-10-22, thay quy định dùng Claude Fable 5.1 trước đó): phân rã công việc, viết giao việc, hợp nhất kết quả và chấp nhận hoặc bác bỏ mọi đầu ra của tác tử con. Điều phối viên không tự đảm nhận vai soạn, rà soát hay chỉnh sửa trong quy trình. Nếu phiên đang chạy mô hình khác, báo rõ trước khi giao việc và đề nghị người dùng chuyển mô hình; không tự coi phiên đó là điều phối viên hợp lệ.
- Mọi tác tử con, kể cả tác tử do tác tử con tạo tiếp, phải dùng **Claude Opus 5.5** (`claude-opus-5-5`) với mức suy luận `high` qua cơ chế tác tử gốc của Claude Code. Tạo tác tử bằng công cụ `Agent` với `model: "opus"` và `effort: "high"`, loại `general-purpose` hoặc loại có định nghĩa trong `.claude/agents/` khai báo mô hình `claude-opus-5-5` và mức suy luận `high`. Không dùng loại `fork`, vì tác tử `fork` kế thừa mô hình của điều phối viên và bỏ qua tham số mô hình. Không giao vai trong quy trình cho loại tác tử cố định mô hình hoặc mức suy luận khác. Tiếp tục nhiệm vụ của tác tử đã tạo bằng `SendMessage`; lời gọi `Agent` mới tạo một tác tử mới.
- Mọi đầu ra của tác tử con phải được điều phối viên rà trước khi chuyển sang giai đoạn sau, ghi vào tệp của kho hoặc gửi người dùng. Với kế hoạch và báo cáo: đối chiếu từng phát hiện với tệp và dòng được dẫn, tự kiểm lại phép tính và hằng số. Với tệp đã ghi: đọc diff và chạy các bước kiểm tra kỹ thuật, trực quan và đồng bộ học liệu. Ghi quyết định `chấp nhận | yêu cầu sửa | bác bỏ` kèm lý do trong `review-log.md`; yêu cầu sửa được gửi lại đúng tác tử bằng `SendMessage` và kết quả sửa được rà lại. Việc một tác tử con rà kết quả của tác tử con khác không thay thế bước duyệt của điều phối viên.
- Không dùng OpenRouter, cầu nối trong `openrouter-mcp/`, các script OpenRouter, `codex-orchestrator` hoặc lời gọi mô hình qua API/CLI để thay cơ chế tác tử gốc của Claude Code. Các ủy quyền OpenRouter, GPT-6-Astra và cấu hình trong hồ sơ lịch sử (kể cả `.codex/`) không áp dụng cho quy trình hiện hành.
- Không đọc, nạp hoặc gửi `.env`, `.env.*` ở bất kỳ thư mục nào; không dùng khóa API hay bí mật để tạo hoặc xác thực tác tử. Không đưa bí mật, kể cả trong tệp có tên thông thường, vào lời nhắc, tệp đính kèm, kết quả công cụ hoặc nhật ký.
- Mỗi nhiệm vụ phải có vai trò, đầu vào, đầu ra, phạm vi tệp và điều kiện hoàn thành cụ thể. Tác tử chỉ đọc có thể chạy song song trong giới hạn khả dụng; chỉ một tác tử được ghi tệp tại một thời điểm. Điều phối viên phải chấp nhận hoặc bác bỏ kết quả trước giai đoạn phụ thuộc.
- Ghi tên tác tử, vai trò, loại tác tử, mô hình và mức suy luận đã chỉ định từ lời gọi công cụ hoặc định nghĩa tác tử trong nhật ký, cùng quyết định rà của điều phối viên cho từng đầu ra. Chỉ ghi mô hình thực chạy hoặc tuyến xác thực khi công cụ cung cấp bằng chứng; không coi lời tự khai của tác tử là bằng chứng thực thi.
- Nếu không tạo được tác tử Claude Opus 5.5 với mức suy luận `high` qua cơ chế gốc, báo rõ giới hạn và dừng phần việc phụ thuộc. Tiếp tục các việc độc lập đã được phép; điều phối viên không tự làm thay phần việc phụ thuộc và không chuyển ngầm sang mô hình khác, OpenRouter hoặc script gọi mô hình.

### Chọn phạm vi rà soát

- Trước mỗi lượt rà, xác định phạm vi: tiêu đề hoặc câu chữ; một lỗi vừa sửa; một cụm khái niệm, công thức hoặc thuật toán; toàn bài khi có bản nháp mới hoặc thay đổi luận điểm, mở bài, kết bài.
- Với thay đổi cục bộ, cung cấp phần đã sửa, hai trang lân cận mỗi phía và bản đồ các phần nếu liên quan mạch viết. Trích đoạn phải có đường dẫn và mã trang hoặc số dòng truy nguyên; tác tử chỉ đọc thêm trong phạm vi đã giao.
- Rà toán phải giữ đủ ký hiệu, giả thiết, ví dụ và nguồn của cụm; không rút đầu vào chỉ còn công thức cuối. Nếu cần chia bài thành nhiều gói, lập bảng bao phủ; vai mạch viết vẫn phải rà toàn tuyến bằng bản đồ các phần.
- Khi tác tử thất bại do phạm vi quá lớn, thu hẹp hoặc chia gói trước khi thử lại bằng cùng mô hình. Ghi rõ phần chưa rà nếu vẫn thất bại; không chuyển sang OpenRouter hoặc mô hình khác.
- Năm vai vẫn độc lập; rà lại đúng phần bị ảnh hưởng và các ranh giới liên quan. Không coi rà trích đoạn là đã rà toàn bài.
