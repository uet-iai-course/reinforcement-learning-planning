# Nhật ký xây dựng lại Bài 05

## Yêu cầu và trạng thái

Ngày 28-09-2026, người dùng yêu cầu bỏ toàn bộ dàn bài hiện hành, lập lại bằng `$build-slide-deck-outline`, rồi viết lại bộ trang chiếu dự đoán phi mô hình. Sutton–Barto là cơ sở tổ chức nội dung; PDF Bài 05 và bài tập tuần 5 là nguồn đối chiếu phạm vi và ví dụ. Tiêu đề, nội dung, chú thích và ghi chú dùng văn phong học thuật tiếng Việt, ký hiệu nhất quán; biên tập bằng `$no-ai-slop` và kiểm tra liên tục theo `$quill`.

Dàn bài, storyboard và ghi chú biên soạn cũ đã được loại khỏi thư mục quy trình. Lịch sử trước lần viết lại nằm trong Git tại commit `b81c183881e56f6bfbeff13e4d0b85163b38b24f`. Nhật ký này chỉ ghi quy trình xây dựng lại; không kế thừa kết luận rà soát hoặc ủy quyền dùng mô hình từ hồ sơ cũ.

**Trạng thái hiện tại:** hoàn thành xây dựng lại Bài 05 với 45 trang, năm phần, 120 phút trình chiếu và 30 phút chữa bài. Đã xử lý các phát hiện của năm báo cáo độc lập; các lượt rà lại toán học, góc nhìn sinh viên, toàn tuyến mạch viết và kiểm định kỹ thuật cuối đều đạt. Các mục theo giai đoạn bên dưới là lịch sử; kết luận bàn giao và giới hạn công cụ nằm ở mục cuối.

## Căn cứ tiếp nhận

- Nguồn chính của học phần: `RL-hk2-2025-2026/lecture-05-du-doan-phi-mo-hinh.pdf`, 33 trang.
- Bài tập: `RL-hk2-2025-2026/resources/hw05-model-free-prediction.pdf`, 2 trang.
- Giáo trình: Sutton–Barto, *Reinforcement Learning: An Introduction*, ấn bản 2; dự kiến §5.1 và §6.1–6.3, cần đối chiếu chi tiết trong báo cáo phân tích.
- Đầu ra: `2627-1/lecture-05-du-doan-phi-mo-hinh.html`, SVG của bài, `analysis.md`, `outline.md`, `storyboard.md`, nhật ký này và mục Bài 05 trong `index.html`.
- Phần trình chiếu chính: 120 phút, khoảng 45 trang, từ 5 đến 7 mạch; 30 phút chữa bài tập riêng theo quy định học phần. Không tự tạo code demo.
- Ghi chú bài giảng hiện có sẽ được đối chiếu về ký hiệu, thuật ngữ và liên kết sau khi dàn bài mới được chốt.

## Điều phối

Chỉ sử dụng tác tử gốc của Codex qua `collaboration`, chỉ định `gpt-6-astra` với `reasoning_effort: xhigh`. Không gọi OpenRouter, script mô hình, API mô hình, hoặc đọc tệp `.env`. Mô hình dưới đây là cấu hình đã chỉ định trong lời gọi công cụ, không phải khẳng định về tuyến thực thi không được công cụ xác minh.

| Tác tử | Vai trò | Mô hình và mức suy luận được chỉ định | Phạm vi |
|---|---|---|---|
| `lec05_rebuild_planner` | Lập kế hoạch chỉ đọc | GPT-6-Astra, xhigh | Quy trình và phạm vi; không kế thừa dàn bài cũ |
| `lec05_source_analysis` | Phân tích nguồn chỉ đọc | GPT-6-Astra, xhigh | Toàn bộ nguồn 33 trang, bài tập và phần sách liên quan |
| `lec05_academic_research` | Đối chiếu đại học chỉ đọc | GPT-6-Astra, xhigh | Bộ slide gốc, trình tự khái niệm, ví dụ và hình thức hóa |

Điều phối viên đã chấp nhận phạm vi MC và TD(0), không mở rộng sang n-step, TD(λ), điều khiển hoặc khác chính sách. Số mạch, số trang và thời lượng từng phần sẽ được chốt sau phân tích. Chỉ một tác tử được ghi tệp trong kho tại một thời điểm.

## Các cổng kiểm định

Đã hoàn tất dàn bài/ánh xạ, kiểm định storyboard, triển khai, năm báo cáo độc lập trên cùng bản cố định, chỉnh sửa và rà lại. Kiểm định cuối bao phủ RevealJS, KaTeX, SVG, đường dẫn, bàn phím, bố cục rộng/hẹp, trạng thái và hình ảnh Codex Slides. Bằng chứng từng giai đoạn cùng giới hạn Browser tích hợp được ghi dưới đây.

Dự án Codex Slides được mở lại: `20260824165326-chuy-n-lecture-5-d-o-n-phi-m-h-nh-monte--cp0p`. Phiên hiện tại không có công cụ Browser tích hợp; giao diện ứng dụng cục bộ được kiểm tra bằng Chromium. Giới hạn này sẽ được ghi cùng bằng chứng kiểm định cuối.

## Dàn bài mới và cổng kiểm định storyboard

Tác tử `lec05_outline_writer` soạn mới `analysis.md`, `outline.md`, `storyboard.md` ngày 28-09-2026 trong phạm vi ghi tệp được điều phối giao. Tác tử không đọc hoặc kế thừa dàn bài/HTML cũ; không sửa HTML, SVG, CSS, chỉ mục hay học liệu công khai ở giai đoạn này. Cấu hình mô hình do điều phối viên ghi theo lời gọi tác tử gốc; tác tử soạn không tự xác nhận mô hình thực chạy hoặc tuyến xác thực.

Đầu vào đã dùng: kế hoạch, phân tích nguồn, đối chiếu đại học và kiểm toán số trong `/tmp/rl05-rebuild/`; HW05 và nội dung sách đã được các báo cáo kiểm chứng. Đã đọc `AGENTS.md`, `$build-slide-deck-outline` cùng `references/output-template.md`, `$no-ai-slop` cùng `eval.md`, `$quill` cùng mục Outline Workflow. Áp dụng Quill chỉ cho dàn ý, thứ tự, thuật ngữ và tính liên tục theo yêu cầu kho; không khởi tạo `quill.json`.

### Quyết định nội dung đã cụ thể hóa

| Quyết định | Căn cứ và ảnh hưởng |
|---|---|
| Năm mạch A/B/C/D/E, 45 trang | Mở đầu 5 trang/12 phút; MC 13/35; TD(0) 10/27; so sánh 12/34; kết luận 5/12. Tổng 120 phút, đủ năm trang kiểm tra riêng. Không tách cập nhật gia tăng thành mạch chỉ để tăng số phần |
| Sườn SB thay phần ôn dài của L05 | Theo yêu cầu người dùng hiện tại. L05 tr.4–14 về điều khiển, lặp giá trị, phép co và mục lục lặp được lược có ánh xạ; các tiên quyết cần thiết ở L05-A03–L05-A04 |
| Giữ chuỗi ngắn và dài nguồn | Chuỗi ngắn dùng xuyên MC/TD; chuỗi dài cho số mũ và biến thiên lợi tức. Các số L05 tr.19 và 30 đúng sau làm tròn, không sửa số đúng |
| Thêm tám lượt A–B của SB Ví dụ 6.4 | L05-D08–L05-D12 phân biệt khớp lợi tức và khớp quan hệ Markov thực nghiệm trên dữ liệu cố định. Đã có quy trình giữ V cố định trong lượt quét, bước học đủ nhỏ, ngưỡng và ngân sách |
| Giới hạn tải L05-D09 | Mặt trang gồm một phép quét đầu từ bảng 0 và sơ đồ quy trình; bước thứ hai ở L05-D11. Công thức gia số, điều kiện riêng $0<\alpha<1/4$ và chi phí ở ghi chú. Cùng gamma 1, alpha 1/8 trong các bước A–B |
| Không thêm ví dụ trùng chức năng | Blackjack, Driving Home, chuỗi A–E năm trạng thái không dùng vì chuỗi nguồn đã đáp ứng dẫn nhập, tính tay và đối chiếu. Không thêm bề mặt/đường học thực nghiệm thiếu dữ liệu số gốc |
| Hiệu chỉnh nguồn và HW05 | L05 tr.20 phải ghi lần ghé đầu tiên và alpha 0.5; tr.31 sửa số mũ 4/2 thành 3/1. Bài HW4 giới hạn tiền đề hiệu quả mẫu; bài HW5 tách lần ghé/bước học, bỏ khẳng định bước hằng luôn hội tụ đúng; bài HW7 chỉ định rõ quy tắc lần ghé |
| Ký hiệu và thuật ngữ | $v_\pi$ là giá trị thật, V là ước lượng, $V_t$ trước cập nhật; T là thời điểm kết thúc; không cần toán tử mới. Thống nhất “sai phân thời gian (TD)”, “lần ghé đầu tiên/mọi lần ghé”, “bước học” |
| Giả thiết và điều kiện | Dữ liệu theo chính sách Markov cố định, môi trường dừng. Phân biệt terminal với cắt dữ liệu; phần thưởng ở cạnh với giá trị terminal 0. Không suy điều kiện phương sai lý tưởng sang mọi bảng V đang học |
| 30 phút chữa bài, không mã | Bảy bài HW05 có ánh xạ, đề sửa và đáp án; phân bổ 1+1+2+3+4+9+10=30 phút. Không tạo chương trình/notebook; không thêm trang chính để chứa trọn đề bài tập |
| Tài liệu truy nguyên | SB có trang nhà xuất bản MIT Press đã được điều phối xác minh; trang nội dung theo PDF 2020 đã đọc. L05 chưa xác minh tác giả nên không gán tên tác giả |

### Kiểm tra cơ học và số học của tài liệu quy trình

Đã chạy kiểm tra cấu trúc từ dữ liệu từng trang: outline có 45 mã duy nhất và storyboard có đúng 45 mã cùng thứ tự; tổng thời gian 120 phút; nhóm A=5/12, B=13/35, C=10/27, D=12/34, E=5/12. Outline có năm khối câu hỏi riêng với đáp án, tiêu chí và thời gian. Bảng ánh xạ có đủ trang 1–33; bảng HW05 có đủ bài 1–7. Analysis có đủ tám mục theo kỹ năng. Không có mã lặp tiền tố hoặc cú pháp công thức Markdown dạng dấu gạch chéo và ngoặc tròn/vuông.

Các số được đối chiếu báo cáo nguồn và kiểm toán độc lập: chuỗi ngắn $11/21,19/21$; chuỗi dài tại S/x5 là 0.829218798/0.992155697; hai lợi tức 0.970299 và −0.99; MC/TD sau hai lượt theo từng quy tắc; nghiệm HW05 bài 6; A–B MC (0,0.75) và TD (0.75,0.75). Bước tự chuyển được kiểm trực tiếp: $2+0.5(0+0.9\times2-2)=1.9$. Bước A–B thứ hai của TD dùng bảng (0,0.75) và alpha 1/8 cho A=0.09375, B=0.75. Không có dữ liệu thực nghiệm mới được tạo.

### Biên tập no-ai-slop chế độ Edit

Phạm vi: toàn bộ tiêu đề dự kiến, luận điểm, nội dung và ghi chú học thuật trong outline; các giải thích và quyết định của analysis/storyboard. Đây là biên tập bản mới từ nguồn và đặc tả đã duyệt, không rà hoặc chấm tác giả của bản cũ. Văn phong học thuật của học phần được ưu tiên; định nghĩa, câu kiểm tra, điều kiện và kết luận có chức năng học tập được giữ.

Các thay đổi biên tập: dùng tên đối tượng hoặc kết quả làm tiêu đề; bỏ câu hỏi tu từ và lời nhấn mạnh của nguồn; gộp giải thích phương sai bị lặp; thay phát biểu “TD có phương sai thấp hơn MC rất nhiều” bằng cơ chế và điều kiện; tách câu chứa nhiều điều kiện sang ghi chú; thống nhất thuật ngữ và ký hiệu. Chỉ dẫn dựng trang, mã và thời lượng được đặt trong trường quy trình, không là văn bản ghi chú diễn giả để chép nguyên.

Tác tử soạn tự đối chiếu từng mục `eval.md` sau khi viết; không dùng điểm phát hiện AI, suy đoán tác giả hoặc tác tử đánh giá thay cho tự kiểm:

| Mục eval | Kết quả | Căn cứ |
|---|---|---|
| Nguyên tắc 1: giữ ý, không thêm khẳng định vô căn cứ | đạt | Giữ nguồn, các thêm mới có mã SB hoặc nhãn ví dụ kiểm quy tắc tự xây dựng |
| Nguyên tắc 2: giữ từ vựng và mức văn phong | đạt | Thuật ngữ học thuật Việt và quy ước của người dùng chi phối toàn bộ bản mới |
| Nguyên tắc 3: không viết lại câu rõ chỉ vì đồng nhất | đạt | Giữ các phát biểu định nghĩa và phép tính cần thiết; sửa chỗ thiếu điều kiện |
| Nguyên tắc 4: mức cắt phù hợp | đạt | Lược phần ngoài phạm vi, không nén mất giả thiết hoặc phép suy luận của MC/TD |
| Nguyên tắc 5: mở bằng điều người đọc cần | đạt | Nhu cầu dự đoán và dữ liệu xuất hiện trước thuật toán |
| Nguyên tắc 6: nêu luận điểm sớm khi hữu ích | đạt | Mỗi trang có một luận điểm và dữ kiện tương ứng; khái niệm mới vẫn theo chu trình |
| Nguyên tắc 7: câu có chức năng | đạt | Mỗi trang có lý do học tập, nguồn và sản phẩm; không có trang trang trí |
| Nguyên tắc 8: loại câu chung có thể chuyển sang chủ đề khác | đạt | Câu nối nêu lợi tức, bước cập nhật hoặc tiêu chuẩn cụ thể |
| Nguyên tắc 9: động từ trực tiếp | đạt | Dùng tính, chọn, cập nhật, giữ bảng, khớp dữ liệu; không dùng lời kêu gọi |
| Nguyên tắc 10: giữ cấu trúc hữu ích | đạt | MC trước TD và cùng ví dụ; thay phần ôn theo chỉ dẫn rõ của người dùng |
| Nguyên tắc 11: sửa câu rối, giữ phân biệt | đạt | Tách mẫu/bước học, mục tiêu/ước lượng, mẫu mới/theo lô thành các đối tượng rõ |
| Từ cần bỏ 1 | đạt | Không có từ quảng bá, thổi phồng hoặc lời dẫn rỗng trong nội dung dự kiến |
| Mẫu cần bỏ 1: dẫn rỗng, tương phản giả, tu từ | đạt | Tiêu đề gọi khái niệm; câu hỏi chỉ dùng khi thực hiện đánh giá |
| Mẫu cần bỏ 2: nhịp kịch tính, từ đồng nghĩa luân phiên | đạt | Thuật ngữ cố định; mẫu trường metadata lặp chỉ phục vụ truy nguyên |
| Mẫu cần bỏ 3: nhấn mạnh thiếu căn cứ | đạt | Đã bỏ mức độ “rất nhiều”; các nguồn và giả thiết được chỉ rõ |
| Mẫu cần bỏ 4: lời dẫn người đọc và điều phối | đạt | Ghi chú học thuật giải thích đại lượng và lỗi; chỉ dẫn triển khai nằm ở trường quy trình |
| Mẫu cần bỏ 5: kết câu kịch tính | đạt | Kết thúc bằng nhiệm vụ đọc và bài tập cụ thể |
| Mẫu cần bỏ 6: tổng kết thừa | đạt | E01 lựa chọn, E02 đối chiếu năng lực, E03 bài tập, E04 kiểm tra, E05 đọc; mỗi trang có chức năng riêng |
| Mẫu cần bỏ 7: trang trí định dạng | đạt | Bảng dùng cho đối chiếu; nhãn đậm là trường quy trình; không có biểu tượng trang trí |
| Mẫu cần bỏ 8: dấu hai chấm và viết hoa | đạt | Dấu hai chấm dùng cho nhãn trường, dữ kiện và Câu hỏi |
| Mẫu cần bỏ 9: lạm dụng gạch dài | đạt | Không dùng gạch dài tạo nhịp câu; dấu gạch trong khoảng trang và tên riêng có chức năng |
| Đọc cuối 1: tự đối chiếu eval | đạt | Tác tử viết thực hiện kiểm tra này trước bàn giao |
| Đọc cuối 2: nhịp câu máy móc | đạt | Các trường lặp phục vụ cấu trúc; phần giải thích dùng quan hệ cụ thể theo từng nội dung |
| Đọc cuối 3: đúng giọng yêu cầu | đạt | Giọng trang trọng, học thuật, không giả văn nói |
| Đọc cuối 4: đọc rõ với đồng nghiệp | đạt | Từng phép tính có dữ kiện và kết quả; giả thiết gần kết luận |
| Đọc cuối 5: bản đầy đủ và phần thay đổi | đạt | Ba tệp đầy đủ đã lưu; mục “Các thay đổi biên tập” ghi ở trên |
| Đọc cuối 6: quy tắc báo cáo Detect | đạt trong phạm vi | Giai đoạn này dùng Edit; không đưa điểm số hoặc phỏng đoán nguồn gốc văn bản. Báo cáo Detect độc lập thuộc giai đoạn rà |

### Rà tính liên tục theo Quill

Đã kiểm mục đích và đầu vào/đầu ra của năm mạch; lợi tức có ví dụ trước ký hiệu; cách chọn mẫu trước bước học; bước tính TD trước giả mã; bảng C03 được cho như dữ kiện rồi đối chiếu C07; mẫu mới và dữ liệu cố định được phân biệt trước A–B. Cụm MC truyền cùng hai lượt sang TD và so sánh. Kết luận thu hồi vấn đề thiếu mô hình, không mở trọng tâm mới. Không tạo tệp hoặc công cụ của dự án sách.

Trạng thái sau bàn giao dàn bài: đủ ba tệp mới và kiểm tra nội bộ; đang chờ kết quả kiểm định storyboard chỉ đọc và chấp nhận của điều phối viên. Chưa bắt đầu HTML/SVG/index, chưa coi năm báo cáo độc lập hoặc kiểm định hiển thị là hoàn tất.

Phản hồi kiểm định storyboard về L05-B12 đã được tiếp nhận: đổi “cần phương sai hữu hạn ... để dùng luật số lớn” thành “Trong khung đang xét, giả sử lợi tức có phương sai hữu hạn và số mẫu tăng vô hạn để áp dụng luật số lớn.” Câu sửa nêu điều kiện đủ đang dùng, không gán phương sai hữu hạn thành điều kiện cần của mọi luật số lớn. Đã đối chiếu analysis và storyboard: analysis đã dùng dạng “Với các ...”, storyboard không có phát biểu gây nhầm; không đổi cấu trúc hoặc thời lượng.

## Triển khai HTML và SVG theo dàn đã duyệt — 28-09-2026

Tác tử `lec05_deck_writer`, vai trò soạn và triển khai. Mô hình được điều phối viên chỉ định trong tác vụ là GPT-6-Astra, mức suy luận xhigh; không suy diễn bằng chứng thực thi từ lời tự khai. Tác tử không gọi mô hình qua API/CLI, OpenRouter, tệp `.env` hoặc tác tử con. Phạm vi ghi gồm HTML Bài 05, SVG của bài, mô tả thẻ Bài 05 trong danh mục và mục nhật ký này. Không sửa CSS dùng chung, RevealJS, tiện ích hoặc `lecture-note.md`.

### Cổng duyệt và quyết định biên tập

Điều phối viên đã đọc, chấp nhận báo cáo kiểm định storyboard và cho phép triển khai cấu trúc 45 trang, năm mạch, 120 phút. Bản HTML được viết mới từ `analysis.md`, `outline.md` và `storyboard.md` mới; không dùng HTML hoặc dàn cũ làm sườn. Toàn bộ mã trang và thứ tự giữ nguyên. Các bổ sung A–B, tự chuyển, quy trình đầy đủ và năm trang kiểm tra đều thuộc dàn đã duyệt.

- R1 của kiểm định storyboard đã được xử lý trước triển khai: phương sai hữu hạn là giả thiết đủ đang chọn để phát biểu kết quả luật số lớn.
- R2 được xử lý bằng cách viết lại toàn bộ 45 ghi chú diễn giả theo chức năng học thuật. Ghi chú chỉ chứa giả thiết, suy luận, phân biệt, phép tính, đáp án và nguồn. Không sao chép chỉ dẫn biên soạn, nơi đặt nội dung, mã trang, thời lượng hoặc lời điều phối từ trường ghi chú trong outline.
- R3 được xử lý đối với sản phẩm công khai: không sử dụng khung lặp “Người học cần giải thích hoặc thực hiện được kết luận” trên trang hoặc trong ghi chú. Cấu trúc nội bộ của storyboard đã được duyệt được giữ nguyên trong giai đoạn triển khai; không thay đổi mục tiêu hoặc sản phẩm học tập.
- Giữ thuật ngữ “sai phân thời gian”, “lần ghé đầu tiên/mọi lần ghé”, “bước học”; dùng $v_\pi$ cho giá trị thật và $V$ cho ước lượng. $V_t$ chỉ bảng trước cập nhật TD; $V_k$ chỉ bảng đầu lượt quét theo lô.
- B10 tính lùi toàn bộ $G_t$, rồi chọn lần ghé và cập nhật theo chiều xuôi; C05 đọc cả hai giá trị từ cùng bảng trước phép ghi. D09 cộng gia số từ $V_k$ được giữ cố định và ghi đồng thời; chỉ có lượt quét đầu ở D09, lượt thứ hai ở D11.
- Mỗi trang có `data-note-topic-id` theo bảng 45 dòng đã bàn giao. Chủ đề 16 của dữ liệu A–B sẽ được tác tử học liệu bổ sung; tại thời điểm triển khai đây là phụ thuộc đã được điều phối phân công, không phải liên kết bị lược.

### Tệp và tài sản

Đã thay toàn bộ nội dung `2627-1/lecture-05-du-doan-phi-mo-hinh.html`, giữ nền kỹ thuật cục bộ của mẫu và lớp `reveal lecture-deck`. Mọi CSS cục bộ đều định phạm vi theo mã trang; không có tệp CSS giao diện riêng. Chân trang nhận diện đúng Học tăng cường, học kỳ 1, 2026–2027, Bài 05. Chỉ thay một câu mô tả thẻ Bài 05 tại `index.html`; hai liên kết bài giảng và ghi chú được giữ hợp lệ.

Đã vẽ lại `short-walk.svg`, `long-walk.svg`; tạo tám SVG mới: `learning-route.svg`, `episode-one.svg`, `episode-two.svg`, `unfinished-episode.svg`, `mc-td-targets.svg`, `long-returns.svg`, `target-randomness.svg`, `ab-empirical.svg`. Cả mười SVG được deck tham chiếu đều có `role="img"`, `title`, `desc` và nhãn có nội dung cụ thể. Không dùng raster, tài sản sinh bằng AI, đồ thị thực nghiệm hoặc hình tải mạng. Giữ hai SVG cũ chưa dùng trong deck để không làm hỏng học liệu đang chờ đồng bộ.

### Kiểm nội bộ và sửa theo bằng chứng trình duyệt

Kiểm tĩnh đã xác nhận 45 trang có mã duy nhất, đúng thứ tự outline, năm phần ngoài, mọi trang nằm ở lớp section thứ hai, 45 ghi chú, 45 thuộc tính chủ đề, CSS chung hợp lệ, không tài nguyên hỏng, không ảnh raster hoặc tài nguyên mạng. XML của các SVG hợp lệ. Bộ dò câu điều phối không tìm thấy mẫu vi phạm trong nội dung công khai. Các kiểm tra cơ học không thay thế đọc học thuật.

Tự tính lại bằng phân số trong `/tmp/rl05-rebuild/deck-numeric-check.json`: cả bốn cấu hình MC trên hai lượt; toàn bộ bảy bước TD; tự chuyển cho $1.9$; lợi tức chuỗi dài $0.970299$ và $-0.99$; hai lượt quét TD A–B cho $(0,3/4)$ rồi $(3/32,3/4)$. Kết quả khớp nội dung HTML và báo cáo số học đã được duyệt. Hệ giá trị chuẩn chuỗi ngắn/dài và bài tập 6 dùng các nghiệm đã được kiểm độc lập ở giai đoạn nguồn.

Điều phối viên chạy trình duyệt lần đầu trên 90 lượt rộng/hẹp và gửi bằng chứng ảnh. Tác tử đã xem ảnh B03, B12, C02, D06, D07, D11 rồi sửa:

- B08/B09: sửa hai chuỗi đầu bảng trong tệp dựng tạm thành chuỗi thô Python, loại ký tự điều khiển làm hỏng lệnh alpha; kiểm lại HTML không còn ký tự điều khiển bất hợp lệ.
- B03: bỏ chú thích lặp đã có trong công thức và ghi chú; B12: chuyển ba thẻ xếp dọc thành hai cột sau dòng định nghĩa, giữ nguyên giả thiết.
- C02/D06: rút câu kết về cơ chế hoặc giới hạn cụ thể; chứng minh phương sai lý tưởng vẫn đầy đủ trong ghi chú.
- D07: chuyển hai tổng sang công thức nội dòng để giảm chiều cao, giữ giới hạn chỉ số và điều kiện; rút câu kết mà không bỏ giả thiết.
- D11: rút phép tính lượt quét thứ hai, giảm khoảng trắng đoạn trong thẻ. Cỡ chữ thân bài giữ nguyên; không thu nhỏ để ép nội dung.
- SVG mục tiêu: chỉ số $T$ của trạng thái kết thúc dùng `tspan`; SVG A–B viết đầy đủ “Kết thúc”. Tiêu đề phụ tự chuyển bỏ ký hiệu thường để CSS viết hoa không làm sai biến.

B10, C05 và D09 đã được điều phối viên xem và xác nhận đọc được trong vòng kiểm đầu. Sáu trang sửa bố cục cần được xác minh lại bằng trình duyệt. Kiểm học liệu, năm vai rà độc lập và đồng bộ Codex Slides cuối cùng còn thuộc các giai đoạn tiếp theo; nhật ký này không xác nhận các giai đoạn ấy đã hoàn tất.

### No-ai-slop Edit: phạm vi và tự đối chiếu eval.md

Đã đọc SKILL và `eval.md` trước khi soạn. Phạm vi là 45 tiêu đề, thân trang, chú thích, ghi chú diễn giả, nhãn SVG và mô tả danh mục. Văn phong học thuật và các phân biệt toán học được ưu tiên theo AGENTS.md. Bản đầy đủ nằm trong HTML/SVG; những thay đổi biên tập được ghi ở các mục trên. Không dùng điểm phát hiện AI hoặc suy đoán tác giả.

| Mục eval | Kết quả | Bằng chứng áp dụng |
|---|---|---|
| Nguyên tắc 1: giữ ý và nguồn | Đạt | Không thêm môi trường hoặc số liệu ngoài dàn; các ví dụ đều truy nguyên |
| Nguyên tắc 2: giữ từ vựng và văn phong | Đạt | Thuật ngữ Việt và ký hiệu theo quyết định điều phối |
| Nguyên tắc 3: giữ câu đã rõ | Đạt | Giữ định nghĩa, phép tính và yêu cầu học tập có chức năng |
| Nguyên tắc 4: cắt đúng mức | Đạt | Chỉ bỏ chú thích trùng; giả thiết và suy luận còn đủ trong nội dung/ghi chú |
| Nguyên tắc 5: mở bằng nhu cầu | Đạt | Dữ liệu trước định nghĩa MC; tiền tố trước công thức TD |
| Nguyên tắc 6: nêu điểm chính đúng vị trí | Đạt | Tiêu đề và đối tượng chính phù hợp chức năng từng trang |
| Nguyên tắc 7: câu có chức năng | Đạt | Câu giải thích chỉ số, phép cập nhật, giả thiết hoặc kết luận có phạm vi |
| Nguyên tắc 8: loại câu chung | Đạt | Câu nối nêu lợi tức, bảng giá trị, nguồn mẫu hoặc tiêu chuẩn |
| Nguyên tắc 9: động từ trực tiếp | Đạt | Dùng tính, chọn, đọc, ghi, giữ, cộng, khớp; không lời kêu gọi |
| Nguyên tắc 10: giữ cấu trúc hữu ích | Đạt | Giữ toàn bộ năm mạch và thứ tự 45 trang được duyệt |
| Nguyên tắc 11: sửa câu rối | Đạt | Phân tách mục tiêu/sai số/bảng mới và dữ liệu cố định/mẫu mới |
| Từ cần bỏ 1 | Đạt | Không có lời ca tụng, quảng bá hoặc nhấn mạnh rỗng |
| Mẫu 1: dẫn rỗng và tu từ | Đạt | Câu hỏi dùng đúng chức năng đánh giá; tiêu đề gọi đối tượng |
| Mẫu 2: nhịp và đồng nghĩa tùy tiện | Đạt | Thuật ngữ nhất quán; loại khung câu chỉ dẫn của outline khỏi sản phẩm |
| Mẫu 3: khẳng định thiếu căn cứ | Đạt | Kết luận thống kê kèm giả thiết; không tuyên bố TD luôn tốt hơn |
| Mẫu 4: lời dẫn người đọc/điều phối | Đạt | R2 được lọc ở toàn bộ notes; không mã trang hoặc thời lượng hiển thị |
| Mẫu 5: kết câu kịch tính | Đạt | Kết bài bằng vị trí đọc và nhiệm vụ có nguồn |
| Mẫu 6: tổng kết thừa | Đạt | Mỗi trang kết luận có chức năng đã duyệt: chọn, đối chiếu, bài tập, kiểm tra, đọc |
| Mẫu 7: trang trí định dạng | Đạt | Bảng để so sánh, thẻ để nhóm đối tượng; không biểu tượng trang trí |
| Mẫu 8: dấu hai chấm | Đạt | Chỉ dùng nhãn, dữ kiện, đầu vào/đầu ra và “Câu hỏi:” |
| Mẫu 9: gạch dài | Đạt | Không dùng dấu gạch dài làm nhịp kịch tính |
| Đọc cuối 1: tự kiểm trực tiếp | Đạt | Tác tử soạn tự đối chiếu đầy đủ danh mục này |
| Đọc cuối 2: tránh nhịp khuôn mẫu | Đạt | Diễn giải theo phép tính, thuật toán hoặc giả thiết riêng của trang |
| Đọc cuối 3: đúng giọng yêu cầu | Đạt | Trang trọng, học thuật; không mô phỏng lời nói của giảng viên |
| Đọc cuối 4: câu rõ khi đọc | Đạt | Nguồn, chỉ số và đối tượng được nêu trước kết luận |
| Đọc cuối 5: bản đầy đủ và thay đổi | Đạt | HTML/SVG đầy đủ đã lưu; nhật ký và handoff nêu thay đổi |
| Đọc cuối 6: Detect | Không áp dụng cho lượt Edit | Không dùng điểm hoặc suy đoán tác giả; rà Detect độc lập thuộc giai đoạn sau |

### Rà liên tục theo Quill

Đã đọc Quill và workflow rà dàn; chỉ dùng mục đích phần, phụ thuộc khái niệm, thuật ngữ và tính liên tục. Không khởi tạo `quill.json` hoặc cấu trúc sách. Đã đối chiếu: bài toán cùng chính sách từ A sang B; hai lượt và số đếm được giữ qua MC; ví dụ số trước công thức TD; chuẩn giá trị chỉ xuất hiện sau ước lượng; sai lệch trước phương sai; điều kiện mẫu mới trước dữ liệu A–B cố định. Mạch kết luận thu hồi việc chọn mục tiêu, dữ liệu và tiêu chuẩn, không đưa thuật toán mới.

### Xác minh sau sửa bố cục

Điều phối viên báo vòng trình duyệt thứ hai đã đạt đủ 90 lượt trên hai kích thước: không tràn trang, không chồng chân trang, không ảnh hỏng, thiếu alt, lỗi HTTP hoặc lỗi trang; 596 biểu thức thô gồm cả ghi chú không có lỗi KaTeX, điều hướng hoạt động. Đã xem trực tiếp lại B12, D07, D11 và xác nhận đọc được. Bằng chứng là `/tmp/rl05-rebuild/browser-report.json` và ảnh trong `/tmp/rl05-rebuild/screens/`.

Theo phản hồi câu chữ cuối, B12 đổi “Giả sử phương sai hữu hạn và $n\to\infty$: áp dụng luật số lớn” thành “Với phương sai hữu hạn, trung bình mẫu hội tụ theo luật số lớn.” Ghi chú bổ sung rõ giới hạn $n\to\infty$ và kết quả $v_\pi(s)$ trong khung độc lập, cùng phân phối. Đây là sửa phát biểu kết quả để bỏ dấu hai chấm mang sắc thái chỉ dẫn; không đổi giả thiết, ví dụ, bố cục hoặc cấu trúc bài. B12 được điều phối viên kiểm lại riêng sau thay đổi này.

Điều phối viên đã kiểm lại B12 cùng hai trang lân cận mỗi phía: đủ 10 lượt trên hai kích thước, không lỗi hiển thị. Toàn bộ 597 công thức thô của bản cuối hợp lệ. `/tmp/rl05-rebuild/browser-report-targeted.json` ghi SHA của bản HTML và `stableDuringCheck` để xác nhận bản được kiểm không thay đổi trong lượt chạy. Tác tử soạn dừng ghi kho sau mục nhật ký này và bàn giao phạm vi học liệu cho tác tử tiếp theo.

## Đồng bộ học liệu công khai — 28-09-2026

Tác tử `lec05_source_analysis` nhận vai trò biên tập học liệu sau khi điều phối viên chấp nhận `deck-handoff.md` và `note-edit-plan.md`, xác nhận tác tử triển khai đã dừng ghi repo. Tác tử hiện hữu được điều phối chỉ định GPT-6-Astra, xhigh; thông tin này ghi cấu hình phân công, không tự xác nhận mô hình thực thi. Phạm vi ghi chỉ gồm `materials/lec-05/lecture-note.md` và mục nhật ký này. Không sửa HTML, SVG, CSS, chỉ mục hoặc ba tệp dàn bài; không tạo chương trình, notebook, `quill.json`, tác tử con hoặc commit. Không dùng API mô hình, OpenRouter hoặc tệp `.env`.

### Nội dung đã thay đổi

Học liệu được tổ chức thành năm phần theo bản trình chiếu mới. Giữ 15 comment `note-topic-id` đã có và thêm `lec-05-topic-16` cho dữ liệu A–B; thứ tự đọc là 01,02,04,06,03,07,08,09,05,12,10,13,11,16,14,15. Số ID là dữ liệu tương thích viewer, không hiển thị trên trang đọc. Đã bỏ toàn bộ bảng vai trò/kết nối, nhãn phân tuyến, mã slide cũ, thời lượng và cầu nối sang điều khiển khỏi học liệu công khai.

Giữ và sửa tương ứng 15 bộ bài tập–gợi ý–lời giải, thêm một bộ A–B thành 16. Ví dụ MC có trước giả mã; ví dụ số TD có trước quy tắc tổng quát. Quy trình MC tính lùi lợi tức rồi chọn/cập nhật xuôi; TD đọc cùng bảng trước khi ghi; quy trình theo lô giữ bảng cố định trong từng lượt quét. Các nguồn và mục đọc được dẫn bằng tên, trang và đường dẫn có thể truy nguyên.

Đã xử lý các phát hiện của `note-audit.md`: sửa câu hỏi có một đáp án nhưng yêu cầu hai cấu hình; bỏ khẳng định các mẫu trong lượt luôn phụ thuộc; phân biệt trọng số với tính phụ thuộc mẫu khi xét ảnh hưởng thứ tự; không hứa sai số giảm sau mọi mẫu mới; sửa thời điểm quan sát và câu hỏi TD thiếu dữ kiện. Phần phương sai giải thích rõ bảng cố định không làm giá trị tại trạng thái kế tiếp ngẫu nhiên thành hằng số. Chỉ mục tiêu lý tưởng dùng $v_\pi$ được áp dụng bất đẳng thức từ luật phương sai toàn phần; không suy thứ tự phương sai phổ quát cho mọi bảng $V$.

Thống nhất thuật ngữ “sai phân thời gian”, “lần ghé đầu tiên/mọi lần ghé”, “bước học”, “tác tử”; định nghĩa tổng phần thưởng chiết khấu rồi dùng “lợi tức”. Dùng $v_\pi$ cho giá trị thật, $V$ cho bảng ước lượng, $V_t$ trước cập nhật TD, $V_k$ đầu lượt quét theo lô; $n$ đếm mẫu/cập nhật của riêng trạng thái. Toán tử nếu sử dụng là $T_\pi$, tách khỏi thời điểm kết thúc $T$. Chuỗi ngắn dùng $X$ nhất quán với HTML.

Bổ sung đầy đủ dữ liệu tám lượt A–B, quy trình theo lô, quét đầu $(0,3/4)$, quét TD thứ hai $(3/32,3/4)$, nghiệm MC $(0,3/4)$ và TD $(3/4,3/4)$. Phân biệt bước học hằng trên tập cố định với mẫu mới. Phần tự luyện ghi các hiệu chỉnh HW05 bài 4, 5, 7; bài 6 có đủ dữ kiện, hệ Bellman, hệ tuyến tính, nghiệm bốn trạng thái và giải thích thứ tự giá trị trong đúng mô hình.

### Tài sản và quy ước URL

Học liệu dùng tám SVG đã có trong bản trình chiếu: `short-walk.svg`, `episode-one.svg`, `episode-two.svg`, `mc-td-targets.svg`, `long-walk.svg`, `long-returns.svg`, `target-randomness.svg`, `ab-empirical.svg`. Không tạo tài sản khác hoặc raster.

Sau khi kiểm mã viewer và học liệu Bài 02–04, điều phối viên xác nhận URL trong Markdown được phân giải từ trang đọc tại `2627-1/`. Theo quyết định mới này, ảnh dùng `img/lec-05/...`, PDF dùng `../RL-hk2-2025-2026/...`; chúng thay đường dẫn theo vị trí tệp Markdown dự kiến trước đó. Không sửa viewer. Mọi đường dẫn cục bộ tồn tại khi giải từ thư mục trang đọc; điều phối viên tiếp tục kiểm tải thực tế trong trình duyệt.

### Tự kiểm no-ai-slop Edit và Quill

Đã đọc SKILL và `eval.md`; áp dụng Edit cho toàn bộ tiêu đề, nội dung, chú thích ảnh, yêu cầu học tập, gợi ý và lời giải. Tự đối chiếu các nhóm kiểm tra:

| Nhóm kiểm trong eval | Kết quả và bằng chứng |
|---|---|
| Nguyên tắc biên tập 1–11 | Đạt trong phạm vi văn phong học thuật được yêu cầu: giữ giả thiết, dữ kiện và ý nghĩa toán học; ví dụ mới chỉ là A–B và phép tự chuyển đã có trong dàn được duyệt; không rút mất quy trình hoặc lời giải. Giọng văn học thuật của học phần ưu tiên hơn gợi ý giữ giọng nói, hài hước của kỹ năng |
| Từ/cụm rỗng | Đạt: bỏ lời nhắc người dạy, “lưu ý”, lời dẫn điều phối, nhãn “vai trò/kết nối” và cách gọi phân tuyến công khai |
| Mẫu diễn đạt 1–6 | Đạt: không dùng câu hỏi tu từ ngoài bài tập, lời nhấn mạnh thiếu bằng chứng, kết luận ưu thế phổ quát hoặc kết câu kịch tính; các phân biệt MC/TD có chức năng học thuật được giữ |
| Mẫu diễn đạt 7–9 | Đạt: bảng phục vụ so sánh dữ liệu và cấu hình; không định dạng trang trí; các công thức dùng dấu đô la đúng quy ước; dấu hai chấm dùng cho nhãn/yêu cầu học tập |
| Đọc cuối 1–5 | Đạt: tác tử biên tập tự kiểm sau sửa; văn bản đầy đủ nằm trong tệp học liệu; thay đổi được ghi tại mục này. Giữ phần tổng hợp vì nó kiểm tra năng lực đã đặt, không chỉ lặp mục lục |
| Quy tắc Detect | Không phải chế độ của bước sửa; báo cáo Detect trước đó được dùng làm đầu vào. Không dùng điểm phát hiện AI hoặc suy đoán tác giả |

Quill được dùng theo phạm vi dự án: kiểm thứ tự, tiên quyết, thuật ngữ và liên tục giữa các phần, không khởi tạo sách. Quy tắc lần ghé đầu tiên được khai báo ngay tại ví dụ trước khi mở rộng sang mọi lần ghé; một bước TD dùng bảng cho trước nên không phụ thuộc vòng vào kết quả lượt sau. Giá trị chuẩn xuất hiện sau ước lượng; kỳ vọng trước phương sai; giả thiết mẫu mới trước dữ liệu A–B cố định. Kết luận không giới thiệu điều khiển hoặc khái niệm trọng tâm mới. Không còn tham chiếu số topic cũ trong văn bản hiển thị.

### Kiểm định của tác tử học liệu

- Năm phần cấp hai; 16 comment ID duy nhất, đủ 01–16. Cả 45 `data-note-topic-id` của HTML đều có đích tương ứng.
- Mỗi chủ đề có đúng một `exercise`, một `hint`, một `solution`: tổng 16 bộ, không khối lồng hoặc dấu đóng thiếu.
- 568 biểu thức được phân tích bằng KaTeX cục bộ với `throwOnError: true`, `strict: error`; không lỗi. Hai chuỗi tiếng Việt trong công thức ban đầu được chuyển thành ký hiệu có định nghĩa bên ngoài để tránh cảnh báo Unicode của chế độ strict.
- Không còn mã nội bộ công khai, $T^\pi$, biến thể mục tiêu TD cũ hoặc delimiter toán ngoài `$...$`/`$$...$$`. Tám SVG đều thuộc tập tài sản HTML đang sử dụng; đường dẫn cục bộ tồn tại.
- Đã tính lại bằng phân số bốn cấu hình MC, bảy bước TD, tự chuyển, hai lợi tức dài, hai lượt quét A–B và kiểm chính xác hệ HW05 bài 6. Các kết quả khớp HTML và báo cáo số được điều phối chấp nhận.
- Bằng chứng tạm: `/tmp/rl05-rebuild/note-static-report.json`, `note-katex-report.json`, `note-numeric-report.json`, `note-handoff.md`. Kiểm viewer, đọc rộng/hẹp và năm vai rà độc lập thuộc bước điều phối tiếp theo; mục này không tuyên bố thay cho những kiểm tra đó.

## Năm báo cáo độc lập và chỉnh sửa sau rà — 28-09-2026

Điều phối viên đã đọc và chấp nhận đủ năm báo cáo của cùng revision `d0fa07fbf2016cf83ea6db1e168196c950486016235cad202aa18a7426115284`. Mỗi báo cáo kiểm SHA trước/sau: 19/19 tệp khớp `/tmp/rl05-rebuild/review-freeze.json`. SHA của HTML trước sửa là `aa6c43e07c745994dabf1af587e64acccd8ed778f4cde45342be037b24ecd885`; SHA học liệu là `6760dc92f0b820ec61e3a1d1a48915d12ac8588d3d933b8d48d3f69573f905e5`. Cả năm vai đều không phát hiện lỗi chặn bàn giao hoặc nghiêm trọng; các đề xuất trung bình và nhẹ vẫn được xử lý.

| Tác tử, vai độc lập | Cấu hình được chỉ định | Phạm vi và giới hạn | Báo cáo đầy đủ |
|---|---|---|---|
| `lec05_review_student`, góc nhìn sinh viên | GPT-6-Astra, xhigh, `fork_turns: none` | Đọc 45 trang/45 notes, 16 topic, bản đồ/thời lượng; xem đủ ảnh 1280 qua contact sheet, mở riêng A05/B10/C05/D11; xem 12 ảnh hẹp. Chưa diễn tập hoặc kiểm viewer trong vai này | `/tmp/rl05-rebuild/review-student.md` |
| `lec05_review_rl`, chuyên gia Học tăng cường | GPT-6-Astra, xhigh, `fork_turns: none` | 45 trang/notes, 16 topic, 33 trang nguồn, 7 bài HW05, phần sách liên quan, dữ kiện SVG; tính lại MC/TD/Bellman/A–B. Không thay kiểm trình duyệt | `/tmp/rl05-rebuild/review-rl.md` |
| `lec05_review_math`, toán học và thuật toán | GPT-6-Astra, xhigh, `fork_turns: none` | 45 trang/notes, 16 topic, 10 SVG được tham chiếu; kiểm số hữu tỷ, hệ Bellman, chỉ số, giả thiết, giả mã và hội tụ. Không rà ảnh/trình duyệt | `/tmp/rl05-rebuild/review-math.md` |
| `lec05_review_academic`, học thuật, giảng dạy và Detect | GPT-6-Astra, xhigh, `fork_turns: none` | 45 trang/notes/alt, 16 topic, 12 SVG, bản đồ phụ thuộc; xem B08/D05/D09 ở 1280. Không thay kiểm ảnh toàn bài hoặc kiểm toán số độc lập | `/tmp/rl05-rebuild/review-academic.md` |
| `lec05_review_flow`, kết nối và mạch viết | GPT-6-Astra, xhigh, `fork_turns: none` | Toàn tuyến 45 trang/notes, 16 topic, năm mạch và các ranh giới, chữ của 10 SVG. Không xác nhận toán hoặc hiển thị | `/tmp/rl05-rebuild/review-flow.md` |
| `lec05_final_editor`, chỉnh sửa riêng sau đủ năm báo cáo | GPT-6-Astra, xhigh, `fork_turns: none` | HTML, SVG lec-05, học liệu và planning lec-05; một tác tử ghi kho, không sinh tác tử phụ | `/tmp/rl05-rebuild/editor-handoff.md` |

Các cấu hình trong bảng do điều phối viên xác nhận từ lời gọi `collaboration.spawn_agent`; công cụ không cung cấp metadata riêng về mô hình thực chạy hoặc tuyến xác thực. Không dùng lời tự khai làm bằng chứng. Bước chỉnh sửa không dùng OpenRouter, API/CLI mô hình, bí mật, commit hoặc push.

### Quyết định cho từng phát hiện

Các vấn đề trùng được sửa chung nhưng giữ mã của từng vai để truy nguyên. “Đã sửa” bên dưới chỉ xác nhận thao tác của tác tử chỉnh sửa; rà lại độc lập và xác nhận trình duyệt thuộc cổng tiếp theo.

| Mã và mức trong báo cáo | Bằng chứng trước sửa, đề xuất | Quyết định và nội dung đã sửa | Vị trí |
|---|---|---|---|
| RL-01, trung bình | A03 ghi “Phân phối phần thưởng”; A05/topic-01 nói quy hoạch động cần phân phối chuyển và thưởng. Đề nghị chỉ rõ thông tin đủ cho kỳ vọng | Chấp nhận: mô hình chuyển và phần thưởng kỳ vọng. Notes/lời giải nói phân phối chung cũng đủ nhưng không phải thông tin tối thiểu | A03/A05; topic-01; analysis/outline |
| M01 và RL-02, trung bình | B12/D07/topic-11 chỉ cảnh báo phụ thuộc trong lượt hoặc “giả thiết thích hợp”. Đề nghị phát biểu tích cực kèm bộ điều kiện đủ | Chấp nhận: quá trình phần thưởng Markov hữu hạn dưới chính sách Markov dừng cố định; thưởng bị chặn; kết thúc hầu chắc chắn từ mọi trạng thái đang xét; lượt độc lập cùng phân phối khởi tạo; xác suất ghé $s$ dương; $0\le\gamma\le1$ và bước học $1/N(s)$. Trung bình mọi lần ghé hội tụ hầu chắc chắn khi số lượt hoàn chỉnh tăng vô hạn. Giữ giới hạn không chệch hữu hạn mẫu và bước hằng; hoàn thiện đáp án HW5 | B12 notes, D07 notes; topic-11/topic-15; HT2 và mục tương ứng trong outline/storyboard |
| M02/RL-03, nhẹ; ACA-01, trung bình | B08 cho $0<\alpha\le1$ nhưng nói bước hằng luôn còn ảnh hưởng khởi tạo; B12 lặp. Đề nghị tách biên $\alpha=1$ | Chấp nhận chung: với $0<\alpha<1$, khởi tạo còn ảnh hưởng và mẫu gần đây có trọng số lớn hơn; với $\alpha=1$, $V_n=g_n$ từ mẫu đầu. Giữ các phép tính $\alpha=0.5$ | B08/B12; topic-06/topic-15; analysis/outline/storyboard |
| SV-01, trung bình | D09 chỉ ghi “Quét $\mathcal D$, cộng các gia số”, dù notes/học liệu đã có công thức. Đề nghị hiển thị thao tác để tự lần theo | Chấp nhận: khai báo $k,\Delta_k(s),y,\varepsilon,K$; hiển thị $\Delta_k(s)\leftarrow\Delta_k(s)+\alpha[y-V_k(s)]$ và $V_{k+1}(s)=V_k(s)+\Delta_k(s)$. Giữ bảng tới hết lượt quét; ví dụ có gia số $0,6/8$ | D09; topic-16; ba tệp kế hoạch |
| SV-02, nhẹ | A05 nhãn “Câu hỏi:” nằm ngang câu 3 do `strong` đứng cạnh `ol`. Đề nghị nhãn thành khối | Chấp nhận: khối nhãn riêng trước danh sách, không sửa CSS chung | A05; outline |
| SV-03, nhẹ | D11 cung trên trong `ab-empirical.svg` đi qua vùng nhãn “p = 6/8; thưởng 1”. Đề nghị dời nhãn hoặc lót nền | Chấp nhận: dời nhãn từ y=75 xuống y=116 trong khoảng trống giữa hai cung, giữ cung, mũi tên và dữ liệu | `img/lec-05/ab-empirical.svg`, dùng ở D11/topic-16 |
| SV-04, nhẹ | C07 dấu chấm sau $G$ xuống một dòng riêng. Đề nghị rút câu, giữ khởi tạo 0 | Chấp nhận: “Trong lượt đầu từ bảng $0$, thưởng cuối trực tiếp cập nhật $X$ ngay trước $G$.” | C07 |
| SV-05, nhẹ; ACA-03, nhẹ | B09 notes tự thuật “Phân loại này sửa việc đặt…”; E04/topic-15 dùng “cần chốt” | Chấp nhận: bỏ câu tự thuật B09 vì quan hệ chọn mẫu/trọng số đã được phát biểu; dùng “cần xác định” ở câu hỏi/đáp án và kế hoạch | B09/E04; topic-15; outline |
| ACA-02 và FLOW-01, trung bình | D04 có hai lợi tức nhưng chưa nối rõ với giá trị chuẩn; D05 vào công thức trước phép kỳ vọng số. Đề nghị ví dụ dùng lại chuỗi ngắn | Chấp nhận: D04 đối chiếu hai lợi tức từ $S$ với $v_\pi(S)\approx0.829$ của chuỗi dài. D05 quay về chuỗi ngắn đã biết, giữ $\gamma=1,V(X)=0.5,V(L)=0$; mục tiêu $-1/0.5$ có xác suất $0.2/0.8$, kỳ vọng $0.2$ trước công thức. Sai lệch $-34/105$ trong notes/học liệu. Không suy phương sai từ hai đường | D04/D05; topic-12/topic-10; KN4/HT5, outline/storyboard |
| ACA-04 và FLOW-02, nhẹ | Notes có “số học đã kiểm độc lập”, “Các số làm tròn trong nguồn đúng”, “Hai giá trị in trong nguồn đúng sau làm tròn”. Đề nghị đưa trạng thái kiểm vào nhật ký | Chấp nhận: bỏ lời xác nhận biên tập/kiểm định, giữ nguồn và phép tính. Giữ hiệu chỉnh số mũ D04 và tiền đề HW4–5 vì cần để đối chiếu PDF | B09/B11/C07/C08/D02/D03/D11 notes |
| ACA-05 và FLOW-03, nhẹ | C05/C06/D02/D03 xen “terminal” với “trạng thái kết thúc”. Đề nghị thống nhất tên đối tượng | Chấp nhận: dùng “trạng thái kết thúc” trong notes/alt và ba tệp kế hoạch. Giữ tên tệp, ID, tên tài liệu riêng; bootstrap được giữ do đã giải nghĩa | C05/C06/D02/D03; analysis/outline/storyboard |

Với FLOW-01, vai trò D04 là ví dụ lợi tức mẫu, kết nối vào là giá trị chuẩn của D03 và kết nối ra là nhu cầu phân tích kỳ vọng ở D05. Vai trò D05 là tính kỳ vọng qua các chuyển khi bảng cố định, rồi tổng quát sai lệch; đầu ra cho D06 là phân biệt kỳ vọng với biến thiên. Với FLOW-02, bỏ tự thuật không đổi đầu vào/đầu ra B09 (tập mẫu và trọng số → cấu hình thuật toán) hoặc D02/D03 (bảng mẫu → chuẩn → lợi tức mẫu). Với FLOW-03, cùng quy ước kết thúc được truyền từ MC qua TD đến các hệ Bellman. Rà lại mạch viết phải kiểm các quan hệ này và toàn tuyến theo yêu cầu điều phối.

Các xác nhận số học được chuyển vào nhật ký: năm báo cáo đã đối chiếu các bảng MC/TD, nghiệm ngắn $11/21,19/21$, nghiệm dài làm tròn $0.829,0.992$, số mũ 3/1, HW6 và A–B. Tác tử chỉnh sửa tính riêng kỳ vọng mới $1/5$ và sai lệch $-34/105$, kiểm gia số theo lô $0,3/4$; không tạo dữ liệu thực nghiệm.

### Nguy cơ, giới hạn và đề xuất không mở rộng phạm vi

| Mã | Quyết định |
|---|---|
| SV-R1, nguy cơ trung bình về màn hình hẹp | RevealJS co khung 1280 trên điện thoại; không ghi thành lỗi tràn. Giữ thiết kế trình chiếu, dùng học liệu đọc làm đường tự học. Điều phối đã kiểm viewer rộng/hẹp: biểu thức, tám hình, 32 khối mở gợi ý/lời giải và liên kết; bản sau chỉnh được kiểm lại. Không mở một dự án thiết kế di động hoặc sửa shared viewer trong bước này |
| SV-R2, nguy cơ trung bình về nhịp D05–D07 | Chưa có diễn tập. Giữ D05/D06/D07 mỗi trang 3 phút; D05 có phép kỳ vọng số ngắn, phép trừ/suy diễn dài nằm ở notes/học liệu. D06 trình bày cơ chế và giới hạn; chứng minh trường thông tin và phương sai toàn phần là phần đọc phụ trợ, được ghi trong planning. Không thêm chỉ dẫn điều phối vào sản phẩm |
| R3 trước đó, câu khuôn mẫu trong storyboard | Chỉ sửa hai mục mở đầu A01/A02 thành đầu ra cụ thể; các mục khác đã nêu sản phẩm toán học hoặc thao tác kiểm chứng nên không viết lại cơ học toàn bộ |

Không thêm/bỏ/đổi thứ tự trang, mạch, thuật toán, dữ liệu, nguồn ngoài, demo hoặc notebook. Giữ 45 ID, năm mạch với 5/13/10/12/5 trang, 120 phút chính và 30 phút chữa bảy bài tập. Không sửa thư viện, CSS chung, shared viewer, chỉ mục hoặc tạo `quill.json`. URL hình trong học liệu vẫn theo viewer: `img/lec-05/...`; nguồn PDF dùng `../RL-hk2-2025-2026/...`.

### Tự kiểm no-ai-slop Edit và liên tục Quill

Đã đọc `no-ai-slop/SKILL.md`, `eval.md` và `quill/SKILL.md` cùng các workflow Revise/Outline/Threads/Concept. Phạm vi biên tập là các tiêu đề, thân trang, notes, alt, câu hỏi/lời giải chịu ảnh hưởng trong HTML và 16 topic; đọc toàn bản công khai trước sửa, kiểm lại các đoạn thay đổi cùng ngữ cảnh. Ba tệp kế hoạch được đồng bộ về thuật ngữ, thứ tự và điều kiện. Nhật ký giữ nguyên trích đoạn báo cáo làm bằng chứng, không coi các trích đoạn ấy là văn bản công khai còn lỗi.

| Nhóm kiểm trực tiếp theo eval.md | Kết quả sau sửa và căn cứ |
|---|---|
| Nguyên tắc 1–4: ý nghĩa, giọng, câu đã đúng, mức cắt | Đạt: sửa theo các findings đã được điều phối chấp nhận; ví dụ mới chỉ tái dùng dữ kiện; không cắt giả thiết, quy trình hoặc phân biệt toán học. Giữ văn phong học thuật theo AGENTS |
| Nguyên tắc 5–8: thứ tự, ý chính, tính cụ thể, câu chung | Đạt: D05 có phép kỳ vọng số trước hệ quả; D09 có thao tác đọc/cộng/ghi cụ thể. Bỏ lời tự thuật không tạo sản phẩm học tập; hai mục mở đầu storyboard có đầu ra kiểm chứng |
| Nguyên tắc 9–11: động từ, cấu trúc, câu dài | Đạt: giữ thứ tự 45 trang; câu hỏi dùng động từ nhiệm vụ; rút C07 và chia diễn giải D04/D05 khi cần, không đồng đều hóa nhịp toàn bài |
| Từ/cụm rỗng | Đạt: bỏ “cần chốt”, “đã kiểm” trong notes và câu bình về phân loại; không thêm lời nhấn mạnh hoặc ca tụng |
| Mẫu 1–3: đối lập rỗng, khuôn câu, nhấn mạnh/nguồn mơ hồ | Đạt: giữ đối chiếu toán học có điều kiện; nguồn cụ thể vẫn còn. Không xoay từ đồng nghĩa để tạo phong cách |
| Mẫu 4–6: lời dẫn người đọc, kết kịch tính, tổng kết thừa | Đạt: B12 phát biểu quan hệ học thuật, không chỉ người đọc tới “giả thiết trong ghi chú”; D04 nối bằng quan hệ mẫu/kỳ vọng. Giữ E01–E05 vì mỗi trang có chức năng học tập |
| Mẫu 7–9: định dạng, dấu hai chấm, gạch dài | Đạt: nhãn A05 thành khối; bảng/công thức giữ chức năng. Dấu hai chấm dùng cho dữ kiện, nguồn, bài tập. Không thêm trang trí hoặc nhịp câu kịch tính |
| Đọc cuối 1–4: tự kiểm, nhịp, giọng, câu rõ | Đạt: tác tử chỉnh sửa tự đối chiếu trực tiếp; đọc lại cả đoạn trước/sau, giữ số liệu và các điều kiện quyết định kết luận |
| Đọc cuối 5: bản đầy đủ và thay đổi | Đạt: bản đầy đủ nằm trong HTML/SVG/học liệu; bảng quyết định tại đây và handoff ghi thay đổi, giới hạn, SHA |
| Đọc cuối 6: Detect | Không áp dụng cho lượt Edit; báo cáo Detect độc lập được lưu riêng. Không dùng điểm phát hiện AI hoặc suy đoán tác giả |

Quill xác nhận tuyến khái niệm giữ nguyên: dữ liệu → lợi tức → chọn mẫu/trọng số → MC → mục tiêu TD → TD đầy đủ → giá trị chuẩn → mẫu/kỳ vọng/biến thiên → hội tụ với mẫu mới → tiêu chuẩn dữ liệu cố định → lựa chọn. Ví dụ kỳ vọng D05 có đủ dữ kiện từ B01/C03/D02; giữ phân biệt chuỗi dài ở D04 với chuỗi ngắn ở D05. $t$ là thời gian tương tác, $n$ là số mẫu riêng trạng thái, $k$ là lượt quét; $T$ và $T_\pi$ không bị trộn. Mọi lần ghé được nối từ cấu hình B09 tới điều kiện B12/topic-11 và đáp án HW5. Không xuất hiện vòng tiên quyết hoặc đối tượng mới ở kết bài.

### Kiểm hiển thị trong lúc chỉnh sửa và phạm vi rà lại

Sau lần sửa nội dung đầu, điều phối chạy đủ 90 lượt 1280/hẹp và kiểm viewer. Phát hiện duy nhất là D09 có chú thích hai dòng chồng chân trang ở 1280; D05/B12 và các trang khác không lỗi. Điều phối đã xem D05, xác nhận phép kỳ vọng và công thức đọc được; 642 biểu thức HTML và 599 biểu thức học liệu render, viewer tám hình và các khối mở/đường dẫn/bàn phím đạt trong lần kiểm đó. Đây là báo cáo của điều phối, không phải tuyên bố tác tử chỉnh sửa đã chạy trình duyệt.

Theo phản hồi, tác tử chỉnh sửa chuyển định nghĩa $\varepsilon,K$ của D09 sang cột trái để chú thích còn một dòng, không giảm chữ. B12 đổi câu chỉ tới ghi chú thành phát biểu về tính nhất quán dựa trên các lượt độc lập; bộ điều kiện đủ vẫn giữ trong notes. SHA HTML sau hai sửa là `d8be74b4d336a0ef607932672d0aa79c7dc673c73ce5a7dd1aa17cff9cfd2227`. Đã dừng ghi nội dung công khai để điều phối kiểm mục tiêu B12/D09 và hai trang lân cận mỗi phía.

Rà lại độc lập được yêu cầu, chưa tự đánh dấu hoàn tất:

- Toán/RL: A03/A05; B08/B12/D07 và topic-06/topic-11/topic-15; D05/topic-10; D09/topic-16, giữ đủ dữ kiện, giả thiết và hai trang lân cận mỗi phía.
- Mạch viết: toàn tuyến 45 trang vì A03/A05/E04 có sửa; chú ý D01–D07 và ranh giới D/E, đối chiếu bản đồ năm mạch và 16 topic.
- Góc nhìn sinh viên: A05/B08/B12/C07/D04/D05/D09/D11/E04 và SVG A–B trong viewer; các thay đổi cỡ chữ không có.
- Kiểm kỹ thuật: đối chiếu ID/thời lượng/notes/topic, KaTeX, SVG/alt, liên kết, CSS chung; kiểm lại B12/D09 sau hai sửa cuối và ghi SHA bản được kiểm. Codex Slides và giới hạn công cụ do điều phối xác minh riêng.

### Phản hồi tiếp theo và tự kiểm tĩnh

Vòng trình duyệt tiếp theo xác định D09 hết tràn khung nhưng chú thích vẫn chồng chân trang. Theo đề nghị điều phối, rút định nghĩa ở cột trái thành “$\varepsilon$: ngưỡng; $K$: số quét tối đa.” và dòng dẫn bước cộng thành “Với mỗi mẫu tại $s$, tính $y$ và cộng:”. Công thức, thứ tự giữ bảng/cộng/ghi và cỡ chữ không đổi. HTML ổn định sau sửa có SHA `22aedc6b66db8d0bc46430ae2516162843dcc3d294c0564e2d95a60d7ed387dd`.

Báo cáo `/tmp/rl05-rebuild/recheck-math.md` chấp nhận các sửa A03/A05, B08/B12/D07, D05, D09, SVG A–B và topic-01/06/10/11/15/16; đóng M01/M02, không phát hiện lỗi toán mới. Phạm vi đọc gồm 25 trang được giao và D12 làm ngữ cảnh, không thay lượt rà toàn bài trước đó. Báo cáo tính lại hai vế sai lệch D05 cùng cho $-34/105$ và phân biệt gia số đã nhân bước học với tổng sai số ở D09.

Detect trong lượt rà toán chỉ ra câu mở topic-01 lặp “đánh giá chính sách” ở đầu/cuối. Chấp nhận sửa thành “Đánh giá chính sách bằng quy hoạch động cần mô hình chuyển trạng thái và phần thưởng kỳ vọng.” Học liệu ổn định có SHA `4d1c0d1afc18608f8084bb203f42a045448f4d4e4cae4794d101b923ce9bf391`; các công thức không đổi. Tác tử chỉnh sửa đã dừng ghi HTML/SVG/học liệu; điều phối xác nhận các SHA cuối ở lượt rà tiếp theo.

Tự kiểm tĩnh của tác tử chỉnh sửa: 45 ID duy nhất, đúng thứ tự trong outline/storyboard, 45 notes, năm mạch, 120 phút theo từng trang trong cả hai tệp kế hoạch; 16 ID topic, đủ 16 khối câu hỏi, 16 gợi ý, 16 lời giải; mọi liên kết topic có đích. Mười SVG được HTML tham chiếu có vai trò ảnh và mô tả; không có tài nguyên hỏng, raster hoặc phụ thuộc mạng cốt lõi. Các deck và mẫu đều trỏ CSS chung. Không có ký tự điều khiển ngoài dòng/tab hoặc delimiter toán Markdown sai. Đã đồng bộ tiêu đề B02/D04 của kế hoạch với HTML. Bằng chứng: `editor-static-report.json`, `editor-consistency-report.json`, `editor-change-scope.json` trong `/tmp/rl05-rebuild/`.

Điều phối xác nhận HTML SHA `22aedc6b66db8d0bc46430ae2516162843dcc3d294c0564e2d95a60d7ed387dd` đã qua đủ 90 lượt rộng/hẹp sau lần sửa cuối: không tràn, chồng chân trang, ảnh hỏng, lỗi KaTeX, HTTP hoặc lỗi trang; 641 biểu thức hợp lệ. B12/D09 và hai trang lân cận mỗi phía nằm trong phạm vi này. Báo cáo `browser-report.json` lưu SHA cùng `stableDuringCheck`. A05/C07/D11 được điều phối xem trực tiếp và chấp nhận; D05 cũng đã được xác nhận đọc rõ.

Ba tệp analysis/outline/storyboard đã dừng ghi và được giao lại cho vai mạch viết; HTML/SVG/học liệu đã dừng ghi theo manifest công khai. Rà lại flow toàn tuyến và ảnh từ góc nhìn sinh viên còn do điều phối hoàn tất; tác tử chỉnh sửa không tự đóng các cổng ấy. Báo cáo bàn giao ghi đủ phạm vi, quyết định, kiểm tra và SHA trong `/tmp/rl05-rebuild/editor-handoff.md`; tệp `editor-final-sha.json` lưu manifest cuối của bảy tệp đã đổi. Tác tử `lec05_final_editor` dừng ghi repo sau mục nhật ký này.


## Chấp nhận bản cuối và bàn giao — 28-09-2026

Điều phối viên đã đọc bàn giao của tác tử chỉnh sửa và ba báo cáo rà lại. Không còn phát hiện cần sửa trong các phạm vi đã giao. Các tác tử đã dừng ghi trước khi điều phối cập nhật trạng thái ba tệp kế hoạch và nhật ký; các cập nhật này không thay nội dung học thuật, tiêu đề, thứ tự hoặc thời lượng.

### Các lượt rà lại được chấp nhận

| Vai | Phạm vi và kết luận | Bằng chứng |
|---|---|---|
| `lec05_review_math` | 25 trang được giao cùng D12 làm ngữ cảnh, sáu chủ đề học liệu và SVG A–B. Chấp nhận điều kiện mọi lần ghé, biên bước học bằng 1, kỳ vọng số D05 và gia số D09; đóng M01/M02 và các phát hiện RL tương ứng. Đọc lại D09 và câu đầu topic-01 sau hai sửa cuối; không còn phát hiện toán hoặc câu lặp chưa xử lý | `/tmp/rl05-rebuild/recheck-math.md`; manifest SHA trước/sau bổ sung |
| `lec05_review_student` | Xem trực tiếp chín trang đã sửa ở 1280 × 720 và ba ảnh hẹp D05/D09/D11; đọc nội dung, notes và ngữ cảnh liên quan. Đóng SV-01–SV-05; công thức theo lô đủ thao tác, nhãn A–B không giao đường cong, nội dung không cắt/chồng. Đây là rà lại cục bộ, không thay lượt đọc toàn bài ban đầu | `/tmp/rl05-rebuild/recheck-student.md`; ba SHA công khai khớp |
| `lec05_review_flow` | Đọc lại đủ 45 trang/45 notes, 16 chủ đề, năm phần, các chu trình và chữ của SVG. Đóng FLOW-01–FLOW-03; D04 nối chuẩn với lợi tức mẫu, D05 tính kỳ vọng trước tổng quát, D09 phân biệt giữ bảng/cộng/ghi. Mở đầu và kết luận giữ cùng bài toán đánh giá chính sách. Sáu nhóm, 17 tệp không đổi trong lượt rà | `/tmp/rl05-rebuild/recheck-flow.md`; `recheck-flow-sha-before.json` và `recheck-flow-sha-after.json` |

Các lượt tiếp tục dùng chính tác tử gốc GPT-6-Astra, mức xhigh đã được chỉ định. Điều phối chấp nhận phạm vi rà toán và sinh viên là cục bộ, phạm vi rà mạch là toàn bài. Không suy từ một lượt cục bộ rằng toàn bộ bài đã được kiểm lại theo mọi vai.

### Phiên bản công khai và kiểm định kỹ thuật

| Tệp | SHA-256 của bản được rà và bàn giao |
|---|---|
| `2627-1/lecture-05-du-doan-phi-mo-hinh.html` | `22aedc6b66db8d0bc46430ae2516162843dcc3d294c0564e2d95a60d7ed387dd` |
| `2627-1/materials/lec-05/lecture-note.md` | `4d1c0d1afc18608f8084bb203f42a045448f4d4e4cae4794d101b923ce9bf391` |
| `2627-1/img/lec-05/ab-empirical.svg` | `c5df4406ce268a06172b17f450e6fc671ba043ea8b4086977dc142fff33ce444` |

- `check_static.py`: 45 ID duy nhất, năm section ngoài, 45 notes và 45 liên kết tới chủ đề hợp lệ; thứ tự khớp kế hoạch. Mười SVG được tham chiếu có vai trò và mô tả. Không có đường dẫn thiếu, ảnh raster hoặc tài nguyên ngoài cho thành phần cốt lõi. Cả 13 bộ trang chiếu/mẫu dùng CSS chung. Chỉ mục giữ liên kết Bài 05 và cập nhật mô tả; không thêm liên kết planning.
- `browser-report.json`: 90 lượt duyệt đủ 45 trang ở 1280 × 720 và 390 × 844; SHA HTML khớp bảng trên và không đổi trong kiểm định. Không có tràn khung, chồng chân trang, ảnh hỏng, thiếu alt, lỗi KaTeX, HTTP hoặc lỗi trang. Kiểm bàn phím và cấu hình RevealJS đạt; 641 biểu thức gồm nội dung và notes hợp lệ.
- `note-browser-report.json`: 599 biểu thức hợp lệ ở cả hai kích thước, tám hình tải được, 32 khối gợi ý/lời giải mở bằng bàn phím, liên kết nội bộ hợp lệ, không tràn ngang hoặc lỗi tài nguyên. Học liệu có năm phần và 16 chủ đề, mỗi chủ đề có câu hỏi, gợi ý, lời giải. Thông báo tải còn trong DOM nhưng được ẩn khi tải thành công.
- Các giá trị MC/TD, hệ Bellman ngắn/dài, HW6 và ví dụ A–B đã được hai vai RL/toán tính độc lập; lượt rà lại xác nhận kỳ vọng D05 bằng $1/5$, sai lệch $-34/105$ và gia số đầu tại B bằng $3/4$. Không dùng kết quả hiển thị công thức để thay kiểm đúng toán học.
- `git diff --check` đạt. CSS chung, thư viện, viewer, Bài 04 và các bài khác không bị sửa. Không tạo notebook, demo, dự án Quill hoặc ảnh sinh bằng AI.

### Đồng bộ Codex Slides

Dự án `20260824165326-chuy-n-lecture-5-d-o-n-phi-m-h-nh-monte--cp0p` có 45 trang đã dựng, giai đoạn `deck`, vùng làm việc `canvas`. Đã đối chiếu đủ 45 tiêu đề và 45 ghi chú với HTML cuối; 45 tệp ảnh của dự án khớp SHA ảnh chụp RevealJS cuối. `draft` là trạng thái dự án chưa xuất bản, không phải kết quả của cổng rà nội dung.

Năm Design Files chính `uploaded/analysis.md`, `uploaded/outline.md`, `uploaded/storyboard.md`, `uploaded/lecture-05-du-doan-phi-mo-hinh.html` và `uploaded/lecture-note.md` khớp từng byte với tệp trong kho. Nhật ký này là tệp thứ sáu của hồ sơ bàn giao. Các bản có hậu tố số trong dự án là lịch sử; kế hoạch hiện hành là ba tệp không hậu tố nêu trên. Bằng chứng lưu trong `design-files-final-check.json`, `project-images-final-check.json` và `project-metadata-final-check.json` tại `/tmp/rl05-rebuild/`.

Điều phối đã mở đúng liên kết Play trang 37, xem ảnh D09 sau sửa và kiểm tải lại vẫn giữ đúng trang, ảnh và tiêu đề; không có lỗi trang. Ảnh `/tmp/rl05-rebuild/codex-final.png` và báo cáo `codex-final-report.json` ghi nhận kết quả. Liên kết bàn giao: [Codex Slides, trang 37](http://127.0.0.1:4311/project/20260824165326-chuy-n-lecture-5-d-o-n-phi-m-h-nh-monte--cp0p?slide=37&mode=play&checkpoint=deck).

Phiên này không có công cụ Browser tích hợp trong trình soạn thảo. Việc xác minh trực quan dùng Chromium cục bộ; chưa xác minh bằng Browser tích hợp. Theo nhánh giới hạn công cụ của kỹ năng Codex Slides Verification, kết quả gồm trạng thái dự án, ảnh đã lưu, liên kết chính xác và giới hạn nêu trên. Không tuyên bố đã kiểm bằng Browser tích hợp.

### Biên tập, phạm vi và giới hạn bàn giao

Tiêu đề, nội dung, notes, chú thích và học liệu đã qua no-ai-slop Edit, tự đối chiếu eval và Detect độc lập; phần sửa cuối cùng được kiểm lại trong ngữ cảnh. Các đoạn trạng thái kế hoạch và kết luận nhật ký được điều phối biên tập trực tiếp theo cùng tiêu chí: giữ sự kiện đã kiểm, dùng thuật ngữ nhất quán, bỏ lời nhấn mạnh và không thêm nhận định về tác giả. Quill đã kiểm thứ tự, tiên quyết và liên tục thuật ngữ; không tạo cấu trúc dự án sách.

Bài mới dùng Sutton–Barto §5.1, §6.1–6.3 cùng §2.4–2.5 làm sườn. Giữ hai chuỗi của PDF nguồn, thu gọn phần ôn điều khiển/quy hoạch động, bổ sung ví dụ A–B theo Ví dụ 6.4, sửa số mũ chiết khấu và tiền đề thiếu điều kiện. Bảng ánh xạ bao phủ 33 trang nguồn và bảy bài tập. Mỗi phần có một trang kiểm tra riêng; tổng thời lượng dự kiến là 120 phút và 30 phút chữa bài nguồn.

Bộ trang chiếu dùng khung trình chiếu 1280 × 720; trên điện thoại, toàn khung co nhỏ. Học liệu cung cấp đường đọc riêng đã được kiểm trên màn hình hẹp. Chưa có diễn tập lớp học để đo thời lượng thực tế; chứng minh phương sai trong notes là phần đọc phụ trợ. Không có ngoại lệ raster. Bản PDF xuất từ lần trước không thuộc lần bàn giao này; các tệp hiện tại chưa được commit hoặc push.

Bản RevealJS: [mở tại cổng 8765](http://localhost:8765/2627-1/lecture-05-du-doan-phi-mo-hinh.html). Học liệu: [ghi chú Bài 05](http://localhost:8765/2627-1/material-viewer.html?doc=materials/lec-05/lecture-note.md&deck=lecture-05-du-doan-phi-mo-hinh.html).
