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

## Rà soát từng trang và biên tập lại — 01-10-2026

Yêu cầu của người dùng: duyệt lần lượt từng trang, xác định trang muốn nói gì, đề xuất và sửa để tiêu đề ngắn gọn, học thuật; mạch lập luận chặt; khái niệm không xuất hiện đột ngột hoặc khiên cưỡng; sau mỗi trang sửa mục ghi chú bài giảng tương ứng. Bảng rà soát do điều phối (phiên chính, Opus 5.5) lập sau khi đọc deck, ghi chú, PDF nguồn 33 trang và HW05. Biên tập: Agent fork, Opus 5.5 (kế thừa phiên), effort theo phiên; là tác tử duy nhất ghi tệp trong lượt này.

Không đổi: 45 trang, thứ tự trang, năm mạch, phân bổ 120 phút, mọi `data-slide-id` và `data-note-topic-id`, SVG, `lecture-slide.css`, `index.html`. CSS cục bộ thêm một dòng giới hạn hình L05-D06 (200px) và bỏ quy tắc `.card` của L05-D06 không còn dùng.

### Bảng từng trang

| Mã trang | Trang muốn nói gì | Vấn đề | Đề xuất | Quyết định | Thay đổi ghi chú |
|---|---|---|---|---|---|
| L05-A01 | Tên bài, phạm vi MC/TD | Không | Giữ | giữ | Không |
| L05-A02 | Lộ trình và mục tiêu | Ba thẻ không khớp mạch B–D; "So sánh có điều kiện" mơ hồ | Ba thẻ theo ba mạch | sửa | Đoạn mở đầu nêu ba phần của bài |
| L05-A03 | Cùng đầu ra $v_\pi$, đầu vào đổi từ mô hình sang mẫu | Câu mở cụt, chưa nêu bài toán | Tiêu đề "Đánh giá chính sách khi chưa biết mô hình"; câu mở nêu bài toán dự đoán | sửa | topic-01 mở bằng phát biểu bài toán dự đoán |
| L05-A04 | Mẫu chuyển và đại lượng $v_\pi$ | Quá nhiều ký hiệu ($T$, $\mathcal S^+$, quy ước kết thúc, $\gamma$) trước ví dụ | Tiêu đề "Mẫu chuyển và giá trị cần ước lượng"; chuyển $T$, $\mathcal S^+$ sang B03 | sửa | topic-01 đổi tiêu đề mục; đoạn quy ước kết thúc chuyển sang topic-02 |
| L05-A05 | Phân biệt một mẫu với mô hình | Dùng $S$, $X$ trước khi giới thiệu chuỗi ngắn | Câu hỏi bằng ký hiệu chung $s\to s'$ | sửa | Câu hỏi và lời giải topic-01 dùng $(s,a,0,s')$ |
| L05-B01 | Ví dụ xuyên suốt và nhiệm vụ | Ý tưởng MC (nguồn tr.17) và khái niệm lượt chưa có trên mặt trang | Định nghĩa lượt; hộp ý tưởng MC; tiêu đề "Chuỗi ngắn và ý tưởng Monte Carlo" | sửa | topic-02 thêm định nghĩa lượt và đoạn ý tưởng MC; tiêu đề mục "Lượt và lợi tức" |
| L05-B02 | Lợi tức +1/−1 của hai lượt | Không | Giữ | giữ | Không |
| L05-B03 | Định nghĩa lợi tức sau ví dụ | Tiêu đề tả công thức | "Lợi tức chiết khấu"; nhận $T$, $\gamma$ từ A04; $\mathcal S^+$ vào ghi chú diễn giả | sửa | topic-02 nhận đoạn $\mathcal S$, $\mathcal S^+$ và quy ước kết thúc |
| L05-B04 | Hai quy tắc chọn mẫu | Thiếu lý do cần quy tắc | Câu mở: một trạng thái có thể xuất hiện nhiều lần | sửa | topic-04 thêm câu lý do |
| L05-B05 | Trung bình mẫu | Không | Giữ | giữ | topic-04 đổi tiêu đề mục thành "Ước lượng Monte Carlo" |
| L05-B06 | Cập nhật trung bình không lưu mẫu cũ | Nhu cầu chỉ có trong ghi chú | "Cập nhật trung bình khi có mẫu mới"; câu "Yêu cầu:" | sửa | topic-06 thêm câu nêu nhu cầu bộ nhớ |
| L05-B07 | Dạng gia tăng tổng quát | Tiêu đề dài | "Trung bình gia tăng" | sửa | Không |
| L05-B08 | Thay $1/n$ bằng $\alpha$ | Bước hằng xuất hiện không có động cơ | "Bước học hằng"; câu mở theo nguồn tr.21 | sửa | topic-06 thêm lý do dùng bước hằng (nguồn tr.21) |
| L05-B09 | Hai lựa chọn độc lập | Viết tắt trong tiêu đề | "Hai lựa chọn của Monte Carlo" | sửa | Không |
| L05-B10 | Thuật toán MC | "Quy trình" không thống nhất | "Thuật toán dự đoán Monte Carlo" | sửa | topic-03 đổi tiêu đề mục |
| L05-B11 | MC trên $e_2$ | Viết tắt trong tiêu đề | "Monte Carlo trên lượt thứ hai" | sửa | Không |
| L05-B12 | Tính chất thống kê | Tiêu đề "giả thiết" nhưng nội dung là kết quả; câu mở nặng | "Tính không chệch và hội tụ của Monte Carlo"; ba thẻ; chú thích giả thiết | sửa | topic-11 đổi tiêu đề "Tính không chệch và điều kiện hội tụ", thêm câu mở và đoạn bước hằng |
| L05-B13 | Kiểm tra chọn mẫu | Viết tắt trong tiêu đề | "Kiểm tra chọn mẫu Monte Carlo" | sửa | Không |
| L05-C01 | Hạn chế MC tạo nhu cầu TD | Câu chữ tiêu đề | "Cập nhật khi lượt chưa kết thúc" | sửa | topic-07 câu mở nêu MC chỉ cập nhật khi lượt kết thúc |
| L05-C02 | Thay $G_{t+1}$ bằng $V(S_{t+1})$ | Phép thay và tên bootstrap chỉ có trong ghi chú | "Mục tiêu một bước"; hiển thị $G_t\approx R_{t+1}+\gamma V(S_{t+1})$; gọi tên bootstrap | sửa | topic-07 đặt công thức xấp xỉ trước ví dụ, theo đúng thứ tự trang |
| L05-C03 | Tính tay một bước | Tiêu đề dài | "Một bước cập nhật TD" | sửa | Không |
| L05-C04 | Công thức TD(0) | Tên "sai phân thời gian" chưa giải thích | Chú thích về hiệu hai dự đoán liên tiếp | sửa | topic-07 thêm câu giải thích tên gọi |
| L05-C05 | Thuật toán TD(0) | Tiêu đề | "Thuật toán TD(0)" | sửa | topic-08 đổi tiêu đề "Thuật toán TD(0) và các trường hợp biên" |
| L05-C06 | Hai trường hợp biên | Tự chuyển khiên cưỡng | Câu mở gắn tự chuyển với việc đứng yên ở HW05 bài 6 | sửa | topic-08 thêm cùng liên hệ |
| L05-C07 | TD(0) trên $e_1$ | Không | Giữ | giữ | Không |
| L05-C08 | TD(0) trên $e_2$ | Không | Giữ | giữ | Không |
| L05-C09 | Chi phí hai thuật toán | Tiêu đề không nêu nội dung bảng | "Chi phí bộ nhớ và tính toán" | sửa | Không |
| L05-C10 | Kiểm tra một bước TD(0) | Không | Giữ | giữ | Không |
| L05-D01 | Hai bảng khác nhau | Câu nối sang giá trị chuẩn chỉ trong ghi chú | "Monte Carlo và TD(0) trên cùng dữ liệu"; hộp nêu nhu cầu giá trị chuẩn | sửa | topic-05 câu mở nối từ hai bảng |
| L05-D02 | Giá trị chuẩn | Thiếu câu nêu vì sao tính được $v_\pi$ | Câu mở: mô hình đã biết trong ví dụ | sửa | topic-05 cùng câu |
| L05-D03 | Chuỗi dài | Lý do đưa chuỗi dài chưa rõ | "Chuỗi dài với thưởng thưa"; chú thích nêu lý do | sửa | topic-12 câu mở; tiêu đề "Chuỗi dài và biến thiên của lợi tức" |
| L05-D04 | Hai lợi tức cùng $S$ khác xa nhau | Tiêu đề nhấn chi tiết số mũ | "Biến thiên của lợi tức" | sửa | Không |
| L05-D05 | Kỳ vọng mục tiêu TD lệch $v_\pi$ | Thuật ngữ độ chệch (nguồn tr.26) không được gọi tên | "Độ chệch của mục tiêu TD"; gọi tên độ chệch sau ví dụ số | sửa | topic-10 đổi tiêu đề; định nghĩa độ chệch sau ví dụ số; độ chệch của $G_t$ bằng 0 |
| L05-D06 | So sánh phương sai | Kết quả dương chỉ trong ghi chú | "Phương sai của mục tiêu"; hiển thị bất đẳng thức và giới hạn | sửa | topic-13 đổi tiêu đề "Phương sai của mục tiêu" |
| L05-D07 | Điều kiện hội tụ TD(0) | Tiêu đề không gọi tên kết quả | "Điều kiện hội tụ của TD(0)"; "với xác suất 1" | sửa | Không (đã có trong topic-11) |
| L05-D08 | Chuyển sang dùng lại dữ liệu | Bước chuyển từ D07 đột ngột | "Dự đoán trên dữ liệu cố định"; câu mở nối (Sutton–Barto §6.3) | sửa | topic-16 đổi tiêu đề, thêm câu nối từ mẫu mới |
| L05-D09 | Cập nhật theo lô | Tiêu đề dài | "Cập nhật theo lô" | sửa | Không |
| L05-D10 | Nghiệm MC theo lô | Tiêu đề không thống nhất với D09 | "Nghiệm Monte Carlo theo lô" | sửa | Không |
| L05-D11 | Nghiệm TD theo lô | Như trên | "Nghiệm TD theo lô" | sửa | Không |
| L05-D12 | Kiểm tra kết luận | Không | Giữ | giữ | Không |
| L05-E01 | Lựa chọn phương pháp | Không | Giữ | giữ | Không |
| L05-E02 | Năng lực sau bài | Trùng chức năng A02/E04; thiếu bảng tổng kết nguồn tr.31, 33 | "Tổng kết Monte Carlo và TD(0)"; bảng sáu tiêu chí có điều kiện; câu nối Bài 06 | sửa | topic-15 đổi tiêu đề "Tổng kết, bài tập và tài liệu đọc"; thay đoạn năng lực bằng bảng tổng kết và câu nối Bài 06 |
| L05-E03 | Bài tập tuần 5 | Tiêu đề dài | "Bài tập tuần 5" | sửa | Không |
| L05-E04 | Kiểm tra lựa chọn | Không | Giữ | giữ | Không |
| L05-E05 | Tài liệu đọc | Tiêu đề dài | "Tài liệu đọc" | sửa | Không |

Đề xuất bị điều chỉnh: L05-D05 ban đầu đặt định nghĩa độ chệch đầu trang; biên tập chuyển xuống sau ví dụ số để không mở khái niệm bằng định nghĩa. L05-B01 bỏ dòng "Ước lượng $v_\pi(S)$ và $v_\pi(X)$ từ các lượt" vì hộp ý tưởng MC đã nêu nhiệm vụ và trang cần vừa khung. L05-D06 gộp hai thẻ nguồn ngẫu nhiên thành một câu để có chỗ cho bất đẳng thức. L05-D08 bỏ hộp cuối, chuyển nhiệm vụ dự đoán $A$ lên dòng dữ kiện. Không có đề xuất bị từ chối.

### Sai lệch so với nguồn

- L05-E02 khôi phục bảng so sánh nguồn tr.31 và tổng kết tr.33 ở dạng có điều kiện; các nhận định không điều kiện của nguồn (TD phương sai thấp hơn, học nhanh hơn với thưởng thưa) không được giữ, lý do đã ghi ở các mục trước của nhật ký.
- L05-E02 thêm câu nối Bài 06 theo câu hỏi mở nguồn tr.32 về cải thiện chính sách.
- L05-B01 đưa ý tưởng MC nguồn tr.17 lên mặt trang; L05-B08 đưa lý do bước hằng nguồn tr.21 lên mặt trang; L05-C02 đưa thuật ngữ bootstrap nguồn tr.24 lên mặt trang.
- L05-D05 dùng thuật ngữ độ chệch theo nguồn tr.26, kèm điều kiện để độ chệch bằng 0.

### Kiểm tra

- `git diff --check` đạt; 50 thẻ `<section>` mở và đóng; 45 `data-slide-id` duy nhất; 45 `data-note-topic-id`.
- Số tính lại: $0.2(-1)+0.8(0.5)=0.2$; $1/5-11/21=-34/105$; các số khác giữ nguyên từ bản đã kiểm.
- Playwright Chromium, server `python3 -m reloadserver 8766` tại gốc kho (cổng 8765 đang do dự án khác dùng): cả 45 trang ở 1600×900 và 390×844, tắt hiệu ứng chuyển trang, mở bằng `Reveal.slide(h, v, 99)`. Không có lỗi console hoặc trang, không có `.katex-error`, không có yêu cầu mạng ngoài, không tràn ngang; chiều cao nội dung mọi trang ≤ 720; cỡ chữ thân nhỏ nhất 0.82em. Ảnh đã xem: A04, B01, B12, D02, D05, D06, D08, E02.
- Trình xem học liệu: 642 công thức KaTeX, không có `.katex-error`, không có yêu cầu mạng ngoài. Lỗi CSP về script nội dòng xuất hiện ở mọi ghi chú, kể cả Bài 04, do script tự nạp lại của reloadserver; không liên quan thay đổi.

### Tự kiểm no-ai-slop Edit

Phạm vi: mọi tiêu đề, câu và chú thích mới trên mặt trang; ghi chú diễn giả đã sửa (A02, A04, A05, B01, B03, B12, C02, D05, E02); các đoạn mới hoặc sửa trong lecture-note.md (đoạn mở đầu, topic-01, 02, 04, 06, 07, 08, 05, 12, 10, 13, 11, 16, 15); các mục hiệu chỉnh trong outline.md và storyboard.md. Đối chiếu eval.md: giữ ý và không thêm khẳng định ngoài nguồn (mục nguyên tắc 1, 7, 8); không dùng từ cấm hoặc trạng từ rỗng; không có tương phản nhị phân, câu hỏi tu từ, kết thúc tóm tắt, câu "sâu sắc" cuối đoạn; không có gạch ngang dài mới; dấu hai chấm chỉ dùng cho nhãn ("Lượt:", "Yêu cầu:", "Ý tưởng Monte Carlo:", "Câu hỏi:") và danh sách; chữ đậm chỉ cho thuật ngữ được định nghĩa. Hai câu dẫn bảng trong ghi chú ("Bảng dưới thu gọn…", "Các kết quả dưới đây cho biết…") được giữ vì có chức năng định hướng nội dung học. Văn phong học thuật và độ chính xác toán học được ưu tiên hơn lời khuyên về giọng cá nhân của kỹ năng.

Quill (Outline, Threads, Concept, chỉ dùng như danh sách kiểm): thứ tự khái niệm lượt → lợi tức → chọn mẫu → trung bình → bước học → thuật toán → tính chất; mục tiêu một bước → bootstrap → sai số TD; độ chệch → phương sai → hội tụ → dữ liệu cố định → tổng kết. Thuật ngữ "độ chệch", "bootstrap", "lượt", "bước học hằng" được khai báo trước lần dùng trong cả deck và ghi chú. Không tạo quill.json.

Chưa commit, chưa push. Cần rà toán học và mạch lập luận trên các trang đã đổi nội dung trước khi commit.

### Rà soát độc lập và vòng sửa — 01-10-2026

Ba người rà soát độc lập, chỉ đọc, trên bản nháp đã đóng băng sau lượt biên tập ở trên: (1) toán học và RL; (2) mạch lập luận và góc nhìn sinh viên; (3) phê bình học thuật kèm no-ai-slop Detect. Theo thông tin điều phối chuyển cho biên tập, cả ba là Agent fork, Opus 5.5. Biên tập ghi vai trò theo thông báo của điều phối, không tự kiểm được lệnh gọi công cụ. Không có phát hiện mức chặn bàn giao hoặc nghiêm trọng. Điều phối chuyển các phát hiện dưới dạng danh sách đã hợp nhất, không kèm mức độ từng mục. Vì vậy cột mức độ ghi "≤ trung bình" cho mọi mục; riêng mục cỡ chữ giả mã được đánh dấu theo bằng chứng đo.

| Mức độ | Trang | Vấn đề | Quyết định | Trạng thái |
|---|---|---|---|---|
| ≤ trung bình (cỡ chữ dưới ngưỡng 0.75em) | L05-B10, L05-C05 | Chữ giả mã 0.82em so với nền trang (người rà đo được khoảng 23px) | Nâng CSS cục bộ `.algorithm` lên 0.92em (30.9px theo tọa độ trang 1280×720); trang cao 633 và 643 | đã sửa |
| ≤ trung bình | L05-B07; L05-C02 | Chưa gọi tên "mục tiêu cập nhật"; C02 cần nêu mục tiêu $G_t$ của MC bị thay | B07 thêm câu về mục tiêu cập nhật; C02 nêu mục tiêu một bước thay $G_t$; topic-06, topic-07 đồng bộ | đã sửa |
| ≤ trung bình | L05-C02, topic-07 | Dấu ≈ giữa $G_t$ và mục tiêu TD dễ hiểu sai | Bỏ ≈; viết $G_t=R_{t+1}+\gamma G_{t+1}$, thay $G_{t+1}$ bằng $V(S_{t+1})$, ước lượng của $v_\pi(S_{t+1})=\mathbb E_\pi[G_{t+1}\mid S_{t+1}]$ | đã sửa |
| ≤ trung bình | L05-C04 | Giải thích $\delta_t$ chưa khớp topic-07 | Hiệu giữa mục tiêu dựa trên dự đoán tại $t+1$ và dự đoán tại $t$, cả hai nơi | đã sửa |
| ≤ trung bình | L05-B12, topic-11 | Thiếu định nghĩa không chệch; chú thích giả thiết ngắt dòng gượng; ghi chú diễn giả có câu thừa | Thêm định nghĩa; chú thích một câu liền với các giả thiết; ghi chú nêu tính Markov cho thời điểm ghé ngẫu nhiên; bỏ hai câu thừa | đã sửa |
| ≤ trung bình | L05-B08, topic-06 | Lý do bước hằng dựa vào môi trường không dừng, ngoài giả thiết của bài | Nêu rõ ngoài giả thiết; $\alpha=0.5$ để đối chiếu ví dụ nguồn và thấy trọng số theo thời gian; không dùng dấu hai chấm tiết lộ | đã sửa |
| nhẹ | L05-B03 | Câu mở thiếu quy ước giá trị trạng thái kết thúc | Thêm "giá trị ở trạng thái kết thúc bằng $0$" | đã sửa |
| nhẹ | L05-A05, topic-01 | "robot" không thống nhất thuật ngữ tác tử | "Tác tử"; "chính sách luôn chọn hành động sang phải, ký hiệu $a$" | đã sửa |
| nhẹ | L05-C03 | Bảng cho trước không rõ xuất xứ | Chú thích nêu đây là kết quả TD(0) sau $e_1$, được tính lại ở lượt thứ nhất; topic-07 đồng bộ | đã sửa |
| nhẹ | L05-C06, topic-08 | Dẫn chiếu bài tập trên mặt trang dài | Mặt trang chỉ nêu tự chuyển khi đứng yên; HW05 bài 6 và "số liệu minh họa" vào ghi chú | đã sửa |
| nhẹ | L05-D01, topic-05 | Câu hộp thiếu cấu trúc mục đích | "Để xác định bảng nào gần $v_\pi$ hơn, cần giá trị chuẩn của môi trường." | đã sửa |
| ≤ trung bình | L05-D02, D03, D04 | Thiếu câu nối ra sang độ chệch và phương sai; lý do chuỗi dài nằm ở chú thích; thứ tự xét chưa nêu | D02 chú thích nối ra; D03 câu lý do làm câu mở; D04 chú thích nêu thứ tự kỳ vọng rồi phương sai; topic-05, topic-12 đồng bộ | đã sửa |
| ≤ trung bình | L05-D06, topic-13 | Bất đẳng thức thiếu giả thiết trên mặt trang; gộp nguồn ngẫu nhiên với sai số tất định của $V$ | Thêm giả thiết Markov và mômen bậc hai hữu hạn; tách hai nguồn | đã sửa |
| nhẹ | L05-D09 | Ký hiệu $k$, $\Delta_k$, $\varepsilon$, $K$ được khai báo sau khi dùng; thẻ dày | Khai báo $k$, $\Delta_k(s)$ đầu thẻ; $\varepsilon$, $K$ ở bước 1; bỏ hai dòng thừa | đã sửa |
| ≤ trung bình | L05-E02, topic-15 | Ô hội tụ chỉ liệt kê điều kiện, chưa nêu kết quả; ô phương sai MC không so sánh được; thiếu giả thiết; ghi chú có câu bình luận quy trình về nguồn | Ô hội tụ "về $v_\pi$ khi …"; MC "có thể lớn khi lượt dài"; chú thích giả thiết; bỏ câu bình luận nguồn (giữ ở đây: bài giảng gốc tr.26–28, 31 so sánh MC/TD bằng nhận định không kèm điều kiện; bảng chỉ giữ nhận định đã chứng minh hoặc dẫn nguồn) | đã sửa |
| nhẹ | topic-10 | "**có thể** chệch, không bắt buộc luôn chệch" vừa rào đón vừa in đậm trang trí | "Mục tiêu TD chệch khi sai số ở các trạng thái kế tiếp không triệt tiêu trong kỳ vọng." | đã sửa |
| nhẹ | topic-11; topic-03 | Câu mở siêu ngôn ngữ; ghi chú thiếu dẫn chiếu khớp vị trí B12 | Bỏ câu "Các kết quả dưới đây…"; cuối topic-03 dẫn chiếu mục tính không chệch và điều kiện hội tụ | đã sửa |
| nhẹ | L05-A04 (ghi chú diễn giả) | Câu kể tiến trình | "…được định nghĩa cùng ví dụ chuỗi ngắn" | đã sửa |
| nhẹ | L05-B12, D06, D07, E02 | Lặp cụm "không có bảo đảm…" | Mỗi trang nêu điều kiện một lần dưới dạng khẳng định có điều kiện; mặt trang D06, D07, E02 còn 0 lần, B12 còn 1 lần trong ghi chú diễn giả | đã sửa |
| nhẹ | L05-E01/E02 | Đề xuất đổi thứ tự hai trang kết luận | Từ chối. E01 trả lời trực tiếp bài toán mở đầu; E02 tổng kết tính chất và nối sang Bài 06, phù hợp làm trang khép bài trước bài tập | từ chối |

Để giữ các trang vừa khung sau khi thêm chữ: C02 và D03 dùng hình cỡ ngắn; D02 (150px) và D06 (170px) có giới hạn hình cục bộ; thẻ thứ ba của B12 và hai thẻ của D03 được rút gọn. Không thu nhỏ chữ.

Kiểm tra sau vòng sửa: `git diff --check` đạt; 50 thẻ `<section>` mở và đóng; 45 `data-slide-id` duy nhất. Playwright trên cổng 8766 với `wait_until="load"`, tắt hiệu ứng chuyển trang, kiểm tra các trang đã đổi ở 1600×900 và 390×844: không có lỗi console hoặc trang, không có `.katex-error`, không có yêu cầu mạng ngoài, không tràn ngang; chiều cao nội dung ≤ 720. Ảnh đã xem: B12, C02, D09, E02. Tự kiểm no-ai-slop Edit trên các câu mới theo eval.md: không có tương phản nhị phân, câu rào đón lặp, dấu hai chấm tiết lộ hay chữ đậm trang trí; dấu hai chấm chỉ dùng cho nhãn và khai báo ký hiệu. Chưa commit, chưa push.

### Rà lại sau vòng sửa — 01-10-2026

Người rà toán học và người rà mạch lập luận rà lại các trang đã đổi. Theo thông báo của điều phối, kết quả là **đạt**, kèm ba phát hiện nhẹ. Người rà mạch xác nhận lý do từ chối đổi thứ tự E01/E02 là hợp lệ; lý do được ghi thêm vào storyboard.

| Mức độ | Trang | Vấn đề | Quyết định | Trạng thái |
|---|---|---|---|---|
| nhẹ (toán) | L05-B12, topic-11 | Danh sách giả thiết hội tụ thiếu "quá trình hữu hạn" | Thêm vào đầu danh sách trên chú thích B12; topic-11 đã có "quá trình phần thưởng Markov hữu hạn" | đã sửa |
| nhẹ (mạch) | L05-B12, topic-11 | "Mỗi mẫu giữ trọng số $\alpha$" sai với bước hằng | Mẫu mới nhất có trọng số $\alpha$, mẫu cũ hơn giảm theo $(1-\alpha)$; ghi chú diễn giả nêu trọng số $\alpha(1-\alpha)^j$; topic-11 đồng bộ | đã sửa |
| nhẹ (toán) | L05-D02, topic-05 | Câu nối ra ngụ ý độ chệch và phương sai giải thích toàn bộ độ lệch | "Một phần độ lệch…; phần còn lại phụ thuộc bước học, khởi tạo và số mẫu" | đã sửa |

Để B12 vừa khung sau câu trọng số mới, ba thẻ được rút gọn; ý "khởi tạo còn ảnh hưởng" của bước hằng chuyển khỏi thẻ, vẫn nằm ở chú thích L05-B08 và ghi chú diễn giả. Chú thích B12 nêu đích hội tụ $v_\pi(s)$ một lần cho cả hai kết quả. Kiểm tra: `git diff --check` đạt; Playwright cổng 8766, `wait_until="load"`, B12 (cao 679) và D02 (cao 654) ở 1600×900 và 390×844: không lỗi, không `.katex-error`, không yêu cầu mạng ngoài, không tràn. Chưa commit, chưa push.

Phát hiện của điều phối khi kiểm trình duyệt ở 1600×900 (nhẹ, bố cục): đáy nội dung đè hoặc chạm đỉnh dòng chân trang (863px) ở B03, C02, D06, E02, B01, B07, D01. Đã sửa bằng CSS cục bộ chỉ cho bảy trang này: thu khoảng cách dưới tiêu đề, quanh `.math-large`, `.box` và `.caption`; thu lề công thức hiển thị ở B03 và B07. Không đổi chữ, không giảm cỡ chữ, không sửa `lecture-slide.css`. Sau sửa, `footer_check.py` không còn trang nào đè ngoài mạch A, nơi chân trang bị ẩn. Playwright ở 1600×900 và 390×844 không có lỗi và không tràn. Trạng thái: đã sửa.

### Kiểm định cuối của điều phối — 01-10-2026

Bằng chứng vai trò theo lệnh gọi công cụ của phiên chính: một tác tử biên tập (Agent, `subagent_type: fork`, kế thừa Opus 5.5 của phiên; được tiếp tục bằng SendMessage cho ba vòng sửa) và ba tác tử rà soát chỉ đọc chạy song song (Agent, `fork`): toán học và RL; mạch lập luận và góc nhìn sinh viên; phê bình học thuật kèm no-ai-slop Detect. Rà lại sau sửa dùng lại hai tác tử toán học và mạch lập luận qua SendMessage. Mức effort của phiên không xác nhận được từ trong phiên. Ghi chú: trong bảng rà lại, nguồn của hai phát hiện đã được điều phối hiệu chỉnh (trọng số bước hằng ở B12 do người rà mạch nêu; câu nối D02 do người rà toán nêu).

Kiểm trình duyệt do điều phối tự chạy (Playwright Chromium, server `reloadserver` cổng 8766 vì cổng 8765 đang phục vụ dự án khác; tắt hiệu ứng chuyển trang): cả 45 trang ở 1600×900 và 390×844 không có lỗi console hoặc trang, không có `.katex-error`, không có tài nguyên hỏng hay yêu cầu mạng ngoài, không cuộn ngang; không trang nào có nội dung vượt khung 720 hoặc đè chân trang; chữ giả mã B10, C05 nay ≥ 0.75em. Ảnh đã xem: A04, B03, B10, B12, C02, D06, D09 (hẹp), E02. Ở 390px Reveal chuyển sang chế độ cuộn dọc. Trình xem ghi chú: không `.katex-error`, không yêu cầu mạng ngoài; lỗi CSP về script nội dòng có sẵn ở trình xem (tái hiện trên ghi chú Bài 04), không do thay đổi này. `git diff --check` đạt.

## Rà soát và trình bày lại L05-B02–L05-B06 — 06-10-2026

### Yêu cầu và phạm vi

Người dùng hỏi trang L05-B04 muốn nói gì và quy tắc chọn lợi tức làm mẫu là gì; mặt trang khi đó nêu nhu cầu có quy tắc nhưng không phát biểu quy tắc. Yêu cầu tiếp theo: chạy quy trình sửa cho L05-B02–L05-B06, xác định ý trung tâm của từng trang và tìm cách thể hiện tốt hơn. Yêu cầu bổ sung: đưa vào ý "mỗi mẫu mọi lần ghé có kỳ vọng $v_\pi(s)$ nhờ tính Markov".

Không đổi số trang, thứ tự trang, năm mạch, thời lượng, `data-slide-id` hay `data-note-topic-id`. Không sửa `lecture-slide.css` hay `index.html`.

### Tác tử

Bằng chứng là các lệnh gọi công cụ Agent/SendMessage của phiên điều phối.

| Vai trò | Loại | Mô hình | Effort | Ghi file |
|---|---|---|---|---|
| Điều phối, kiểm cuối, nhật ký | phiên chính | claude-opus-5-5 | theo cấu hình phiên | `review-log.md` |
| Phân tích ý trung tâm và đề xuất trình bày B02–B06 | fork (Agent tool) | claude-opus-5-5 (kế thừa) | kế thừa | không |
| Biên tập, ba vòng (tiếp tục bằng SendMessage) | fork | claude-opus-5-5 (kế thừa) | kế thừa | deck, hai SVG, outline, storyboard, lecture-note |
| Rà lại toán/thuật toán và RL, hai vòng | fork | claude-opus-5-5 (kế thừa) | kế thừa | không |
| Rà lại mạch, góc nhìn sinh viên, văn phong (no-ai-slop Detect), hai vòng | fork | claude-opus-5-5 (kế thừa) | kế thừa | không |

Chỉ một tác tử ghi file tại mỗi thời điểm; hai tác tử rà lại chạy song song, chỉ đọc.

### Ý trung tâm và thay đổi theo trang

| Trang | Ý trung tâm | Vấn đề trước khi sửa | Thay đổi | Quyết định |
|---|---|---|---|---|
| L05-B02 | Mỗi lần ghé là một thời điểm $t$ có $S_t=s$, có lợi tức riêng bằng tổng thưởng phần đuôi | "Lần ghé" chưa được định nghĩa; phép cộng phần đuôi chỉ có trong ghi chú | Câu định nghĩa lần ghé; `episode-one.svg`, `episode-two.svg` thêm hàng $G_t$, ngoặc nét đứt "phần đuôi sau t = 1", viewBox 1080×222, chữ 32; hộp ví dụ $0+0+1=1$ và $-1$; `max-height` cục bộ 182px | sửa |
| L05-B03 | $G_t$ có hệ số $\gamma^{k-t}$ và tính ngược từ $G_T=0$ | Công thức truy hồi chưa được dùng; không nối về B02 | Gộp tổng và truy hồi một dòng; bảng tính ngược trên $e_1$; chú thích $\gamma=1$ thu lại B02; bỏ bốn quy tắc CSS cục bộ | sửa |
| L05-B04 | Hai quy tắc chọn mẫu; mỗi mẫu có kỳ vọng $v_\pi(s)$ nhờ tính Markov; hai quy tắc khác nhau ở số mẫu mỗi lượt | Không phát biểu quy tắc; hộp cuối không mang thông tin | Hai dòng quy tắc có nhãn; cột "Thời điểm ghé"; câu trọng số $2/3$ của $e_1$ tại $X$; hộp tính Markov. Ghi chú: thời điểm dừng, tính Markov mạnh, phụ thuộc trong lượt, nguồn gây chệch của trung bình mọi lần ghé | sửa |
| L05-B05 | Ước lượng MC là trung bình các mẫu đã chọn, $n=N(s)$ | Ví dụ lặp ô bảng B04 | Bảng theo dõi $g_n$, $n$, tổng, $V_n(X)$; ghi chú nêu dạng bộ đếm và tổng của nguồn tr. 18, đổi tên $S(s)$ thành "tổng" để tránh trùng trạng thái $S$ | sửa |
| L05-B06 | Trung bình mới bằng trung bình cũ cộng $1/n$ sai lệch, dịch về phía mẫu mới | Hai cách tính không được gọi tên; lý do bộ nhớ nửa đúng | Câu yêu cầu; hai thẻ "Tính lại từ tổng", "Sửa trung bình cũ"; trục số SVG inline (`role="img"`, hình dạng chấm khác nhau); ghi chú: tổng và bộ đếm cũng không cần lịch sử, dạng sửa trung bình được dùng lại ở bước học hằng và TD(0) | sửa |
| L05-B12 | Không đổi ý | Câu mở chưa nêu lý do | "Theo tính Markov, lợi tức sau mỗi lần ghé…" | sửa |

Đồng bộ: `outline.md`, `storyboard.md` (B02–B06, B12, chu trình khái niệm cụm B, chu trình phụ bước học), `lecture-note.md` topic-02, topic-04, topic-06 và alt hai hình. Topic-11 không đổi, đã đối chiếu nhất quán.

### Phát hiện và quyết định

| mức độ | trang chiếu / vị trí | vấn đề | quyết định | trạng thái |
|---|---|---|---|---|
| trung bình (mạch, vòng 1) | L05-B04 | Bảng cho $0$ và $1/3$ tại $X$ cạnh hộp "mỗi mẫu có kỳ vọng $v_\pi(s)$", lời giải chỉ ở ghi chú | Thay thẻ quy tắc bằng hai dòng; thêm câu trọng số $2/3$ trên mặt trang | đã sửa |
| trung bình (mạch, vòng 1) | L05-B06, storyboard | Mất bước vấn đề của chu trình phụ | Câu "Yêu cầu: …"; sửa dòng chu trình phụ | đã sửa |
| trung bình (mạch, vòng 1) | L05-B02 | Chữ trong SVG khoảng 0,5em | Thu viewBox, chữ 32; đo 0,78em ở 1600×900 | đã sửa |
| trung bình (toán, vòng 1) | lecture-note topic-04 | Câu sau bảng bị marked đưa vào bảng | Chèn dòng trống; rà toàn ghi chú | đã sửa |
| trung bình (toán, vòng 1) | L05-B04 ghi chú, topic-06 | Lý do trùng trung bình tại $S$ nêu thiếu | "mỗi lượt cho hai mẫu bằng nhau" | đã sửa |
| nhẹ (toán + mạch) | L05-B04 ghi chú, topic-06 | Gán tính thời điểm dừng cho giả thiết Markov | Tách: $t_k$ là thời điểm dừng theo định nghĩa; Markov dùng cho bước Markov mạnh | đã sửa |
| nhẹ (toán) | L05-B03 ghi chú, topic-02 | "cách bốn chuyển" dễ hiểu thành $\gamma^4$ | "chuyển thứ tư … $\gamma^{4-1}=\gamma^3$" | đã sửa |
| nhẹ (mạch) | L05-B04 ghi chú | Tham chiếu mơ hồ | Ghi tên trang "Tính không chệch và hội tụ của Monte Carlo" | đã sửa |
| nhẹ (mạch) | L05-B04 | Cột thời điểm ghé khó đọc | "$e_1$: … · $e_2$: …" | đã sửa |
| nhẹ (mạch) | L05-B06 | Nhãn trục số nhỏ | Chữ 30, đo 0,77em | đã sửa |
| nhẹ (mạch) | L05-B05/L05-B06 | Hàng 3 bảng B05 và thẻ "Tính lại từ tổng" là cùng phép tính | Từ chối: B06 cần đặt hai cách tính cạnh nhau để so thông tin mỗi cách dùng | không sửa |
| nhẹ (toán, vòng 2) | L05-B04 ghi chú, topic-06 | Ngụ ý phụ thuộc trong lượt gây chệch | Ghi chú: phụ thuộc không tự gây chệch; số mẫu mỗi lượt ngẫu nhiên, tương quan với lợi tức cho dạng tỉ số; mặt trang bỏ "phụ thuộc nhau" | đã sửa |
| nhẹ (toán, vòng 2) | L05-B06 SVG | Chân chữ dòng cuối sát mép viewBox | viewBox cao 192, `max-height` 166px | đã sửa |
| nhẹ (mạch, vòng 2) | L05-B04, L05-B06 | Viết hoa sau dấu hai chấm khác quy ước deck | Viết thường | đã sửa |

Vòng 2: rà lại toán đạt; rà lại mạch đạt; không còn phát hiện chặn, nghiêm trọng hay trung bình. Các sửa vòng 3 chỉ thuộc các mục nhẹ trên, điều phối kiểm lại bằng diff và trình duyệt.

### no-ai-slop và Quill

Biên tập dùng chế độ Edit trên mặt trang, ghi chú diễn giả B02–B06, B12, mục outline/storyboard và topic-02/04/06, tự đối chiếu `eval.md` sau mỗi vòng: đạt. Rà mạch dùng Detect trên cùng phạm vi; mẫu còn lại (tham chiếu mơ hồ, viết hoa sau dấu hai chấm) đã sửa. Thứ tự chu trình khái niệm cụm B được kiểm theo danh mục Revise/Threads của Quill, không tạo `quill.json`.

### Kiểm tra

- Playwright Chromium, server gốc repo cổng 8766, 1600×900 và 390×844: toàn bộ 45 trang không `.katex-error`, không phần tử tràn, không cuộn ngang, không lỗi console, không tải từ ngoài, không tài nguyên lõi hỏng (chỉ yêu cầu long-poll `api-reloadserver/wait-for-reload` của server phát triển bị hủy khi đóng trang); cỡ chữ nhỏ nhất ≥0,82em. Điều phối đã xem ảnh B02–B06.
- Chiều cao trang sau sửa: B02 680, B03 603, B04 637, B05 548, B06 689 trên 720. B06 nằm trong mức của các trang không sửa (E02 696, C02 691); mũi tên điều hướng trên chạm vùng tiêu đề ở các trang cao này là giới hạn chung của deck.
- Viewer ghi chú: 0 `.katex-error`, hai SVG tải được, bảng topic-04 đúng. Lỗi CSP về inline script và việc hình `img/lec-*` bị cắt/cuộn ngang do `min-width: 900px` trong `material-viewer.css` có từ trước, áp cho mọi bài; không sửa trong phạm vi này.
- `git diff --check` đạt.

## Bài thực hành: dự đoán Monte Carlo và TD(0) trên LunarLander không gió (2026-10-03)

### Phạm vi và quyết định

- Yêu cầu của người dùng: "tiếp tục làm thực hành cho bài 5, Monte Carlo và TD(0), phi mô hình, dùng Lunar Lander (không có gió)", cùng các yêu cầu chung đã nêu cho thực hành Bài 04: notebook standalone tự cài gói, các bước chi tiết có tính sư phạm, đánh giá qua nhiều lượt, ô Markdown giải thích bằng công thức trong bài, chú thích code, trực quan hóa trực tiếp các chính sách sau khi đánh giá (kể cả baseline), gợi mở cuối bài, cột Thực hành trong `2627-1/index.html`. Đây là yêu cầu trực tiếp nên ngoại lệ "không tự tạo notebook" của AGENTS.md được áp dụng.
- Sản phẩm: `2627-1/materials/lec-05/thuc-hanh-lunarlander-du-doan-phi-mo-hinh.ipynb` (73 ô, 0,65 MB, lưu kèm output; ô code đầu `%pip install -q "gymnasium[box2d]>=1.0" numpy matplotlib`).
- Nguồn: bài giảng gốc `lecture-05-du-doan-phi-mo-hinh.pdf` tr. 17–18, 21–28 (đã đối chiếu nguyên văn tr. 26–28); ký hiệu và quy trình theo `materials/lec-05/lecture-note.md` (MC 6 bước, TD(0) 6 bước, điều kiện bước học, cập nhật theo lô 5 bước, ví dụ A, B); Sutton–Barto ấn bản 2 §5.1 tr. 92–93, §6.1–6.3 tr. 119–128 (Ví dụ 6.4); các mục xem trước §6.4–6.5, §7.1, §9.3 và Tsitsiklis & Van Roy (1997), IEEE TAC 42(5):674–690 chỉ dẫn ở mức gợi mở, số trang chưa đối chiếu bản in. Bài giảng gốc không có ví dụ LunarLander; môi trường là lựa chọn của người dùng.
- Thiết kế: `LunarLander-v3`, `enable_wind=False`; chính sách cần đánh giá $\pi$ là hàm `heuristic` của gymnasium trộn hành động ngẫu nhiên với $\varepsilon=0{,}1$, đối chứng heuristic thuần và chính sách ngẫu nhiên; $\gamma=0{,}99$; rời rạc hóa 8 biến thành 9216 ô theo ý nghĩa vật lý; 2000 lượt huấn luyện, 500 lượt kiểm tra với dãy hạt giống tách biệt; thước đo không cần mô hình $J(V)$ trên tập kiểm tra (nêu rõ thước đo ưu tiên đích của MC mọi lần ghé) và $V(S_0)$ so với $\mathbb E_\pi[G_0]$ (kiểm tra thô); MC theo lô và TD theo lô (bước $\alpha/N(s)$, đối chiếu nghiệm $(I-\gamma\hat P)V=\hat r$, nối thực hành Bài 04). Cách chia ô có nhìn vào tập kiểm tra; điều này được công khai trong notebook.
- Index: thẻ Bài 5 có link Colab và link tải `.ipynb` trong nhóm **Thực hành**.

### Tác tử

| Vai trò | Loại | Mô hình | Effort | Ghi file |
|---|---|---|---|---|
| Điều phối, kiểm tra cuối, index, nhật ký | phiên chính | claude-opus-5-5 | high | `index.html`, nhật ký này |
| Soạn thảo, sau đó biên tập hai lượt | fork (Agent tool) | claude-opus-5-5 (kế thừa) | high | notebook |
| Rà soát học tăng cường và toán/thuật toán | fork | claude-opus-5-5 | high | không |
| Rà soát góc nhìn sinh viên, kiểm thử standalone | fork | claude-opus-5-5 | high | không |
| Rà soát sư phạm, mạch, văn phong (no-ai-slop Detect) | fork | claude-opus-5-5 | high | không |
| Rà soát lại (gộp toán và mạch/văn phong) | fork | claude-opus-5-5 | high | không |

### Phát hiện và quyết định (vòng rà soát 1)

Không có phát hiện chặn bàn giao hay nghiêm trọng.

| mức độ | vị trí | vấn đề | quyết định | trạng thái |
|---|---|---|---|---|
| trung bình | mục 2 | Câu "bước đầu chỉ có chi phí nhiên liệu" sai: `reset()` gọi `step(0)` nên `prev_shaping` đã đặt | Bỏ câu, nêu cơ chế, kiểm công thức thưởng trên mọi bước | đã sửa |
| trung bình | phần 8 | Giải thích TD với $\alpha_n=1/n$ sai trọng tâm | Cơ chế tự chuyển: sai số còn lại $\approx n^{-(1-\gamma)}$, tỉ số đo được $\approx0{,}09$; Robbins–Monro là bảo đảm tiệm cận và giả thiết Markov | đã sửa |
| trung bình | phần 8 | Chênh lệch MC lần ghé đầu/mọi lần ghé gán cho một nguyên nhân | Hai nguyên nhân, in số mẫu | đã sửa |
| trung bình | phần 8 | Điểm xuất phát đường học TD và đường bảng hằng chưa giải thích; chưa nối độ chệch–phương sai tr. 26–28 | In $J(\mathbf 0)$, diễn giải, nối tr. 26–28 và ghi chú; nhiệm vụ khởi tạo bằng trung bình lợi tức | đã sửa |
| trung bình | phần 8–9 | $\mathbb E_\pi[G_0]$ thực ra trên 493/500 lượt; TD theo lô và MC theo lô không cùng dữ liệu (7,7% số chuyển) | $G_0$ trên 500 lượt với chặn đuôi tiên nghiệm; TD theo lô cùng dữ liệu với MC, báo cả hai | đã sửa |
| trung bình | mục 7 | TD(0) thiếu câu hỏi kiểm tra | Câu hỏi tự chuyển, bảng ký hiệu → biến | đã sửa |
| trung bình | ô 10, phần 10 | $v_\pi$ dễ bị hiểu là mức "tốt" của vị trí | Nêu $v_\pi$ là phần thưởng còn lại, đẳng thức $G_t$ với $\gamma=1$, câu hỏi; diễn giải bản đồ có điều kiện; mục 10.1 kiểm hai giả thuyết bằng số đo | đã sửa |
| trung bình | mục 3.1 | Thiếu trực quan hóa baseline heuristic thuần | Ba chính sách cùng hạt giống trong đồ thị và trình phát | đã sửa |
| trung bình | nhiệm vụ gió | Lẫn quan sát không Markov với môi trường không dừng | Tách hai ý, chỉ dùng tr. 21 cho trường hợp đổi `wind_power` trong lúc học | đã sửa |
| trung bình | ô 31 | Trỏ tới phép đo không có | Sửa tham chiếu, bỏ metadiscourse | đã sửa |
| nhẹ | nhiều ô | Tính tay có thưởng định hình; histogram chung bins; `paired_difference`; chú thích JavaScript; $\hat P$ so với $P_\pi$; `prediction_pipeline`; khung TD n bước; cảnh báo pygame/pygame-ce trên Colab; "vector one-hot"; nhãn "π (ε = 0,1)"; cơ chế chưa đo viết "có thể"; Markdown trước ô hình; dòng nguồn mỗi mục | Sửa theo đề xuất | đã sửa |

### Rà soát lại

Không có phát hiện chặn, nghiêm trọng hay trung bình. Bốn mục nhẹ đã sửa: chặn đuôi $G_0$ dựa trên khoảng tiên nghiệm của $\Phi$ thay vì cực đại mẫu (đuôi $\le0{,}21$ so với $1{,}96\,\mathrm{SE}=2{,}70$); mục 10.1 chỉ dùng lượt kết thúc và in $\overline{\gamma^{T-1-t}}$; "$G_t$ không chệch đối với $\mu$ trên ô gộp"; nhãn đường bảng hằng. Trích dẫn tr. 28 ("Thường hiệu quả mẫu tốt hơn MC") đã đối chiếu nguyên văn.

### Kiểm tra

- `no-ai-slop`: tác tử soạn dùng Edit và tự kiểm `eval.md` sau mỗi lượt (đạt); hai vai rà soát dùng Detect trên toàn bộ ô Markdown, lời giải `<details>` và chú thích code; các mẫu còn lại đã sửa.
- Chạy: nbclient chạy hết 73 ô không lỗi, khoảng 72 giây; hai lần chạy cho văn bản, HTML trình phát và PNG trùng nhau (trừ số giây). Kiểm thử standalone trong venv mới chỉ có ipykernel/nbclient/nbformat: ô `%pip` cài gymnasium 1.3.0, Box2D 2.3.10 (wheel), pygame-ce; không cần khởi động lại kernel; 0 lỗi, không stderr. Chưa chạy trên Colab.
- Kiểm của điều phối: `nbformat.validate` đạt; không ô lỗi, không ô chưa chạy, không URL ngoài trong output, không stderr; công thức Markdown chỉ dùng `$...$`/`$$...$$`; đã xem hình quỹ đạo ba chính sách, histogram, đường học, $G_t$ so với $V$ dọc lượt và khung trình phát.
- Index: Playwright Chromium 1600×900 và 390×844 trên server cổng 8766 (gốc repo): không lỗi console, không tài nguyên hỏng, không cuộn ngang; `.ipynb` trả HTTP 200.
- Kết quả chính (gymnasium 1.3.0): $\mathbb E_\pi[G_0]=56{,}04\pm2{,}70$; $J$: MC theo lô 1627, TD theo lô cùng dữ liệu 1803, TD(0) $\alpha=0{,}5$ 2101, TD(0) $1/n$ 5158, mốc bảng hằng 3021, $J(\mathbf 0)=5797$.

## Đợt sửa 2026-10-12 — Giai đoạn I: ghi chú bài giảng

### Tác tử

| Vai trò | Loại | Mô hình | Effort | Ghi file |
|---|---|---|---|---|
| Soạn ghi chú bài giảng Bài 05 (giai đoạn I) | general-purpose (theo brief của điều phối viên) | claude-opus-5-5 | high | `materials/lec-05/lecture-note.md`, `img/lec-05/variance-decomposition.svg`, nhật ký này |

Không commit. Không sửa deck, `outline.md`, `storyboard.md`, notebook, index, CSS hay SVG đã có.

### Phạm vi

Viết lại toàn bộ `lecture-note.md` theo `AGENTS.md` §"Tiêu chuẩn giáo trình cho ghi chú bài giảng", mẫu `materials/_templates/lecture-note.md`, quyết định chung `planning/quyet-dinh-chuan-2026-10-12.md` (mục 1–4, 6, 8 Bài 05) và mục B của `revision-plan-2026-10-12.md`. Đủ 11 thành phần: tiêu đề, giới thiệu một đoạn, mục tiêu MT1–MT6, kiến thức tiên quyết (dẫn "ghi chú Bài 0N, Mục k" kèm phát biểu lại), bảng ký hiệu, bản đồ chủ đề bốn nhóm (23 `note-topic-id`), năm mục nội dung ứng với mạch 1–5, tình huống áp dụng và ứng dụng (mạch 6), tóm tắt chương, bài tập củng cố ba mức, hướng dẫn đọc thêm. Khoảng 32 600 từ theo `wc -w` (tính cả LaTeX và bảng).

Ví dụ xuyên suốt "dãy bốn ô" được gọi là "tàu đổ bộ thu nhỏ" ($\mathrm L$ là "rơi", $\mathrm G$ là "nằm yên"), giữ nguyên số liệu và hai lượt $e_1$, $e_2$; "chuỗi dài" thành "dãy bảy ô", giữ số liệu. Tên ô chữ đứng; hành động $\mathrm{tien}$. Dấu thập phân phẩy. Ngưỡng dừng $\theta$; $\Delta_k(s)$ được gọi tên "tổng gia số của lượt quét $k$". Bỏ mọi liên kết PDF nguồn, thay bằng "Bài giảng gốc (2025–2026), trang N" và "Bài tập tuần 5 (2025–2026), bài k". Ba lời giải HW05 bài 5–7 của ghi chú cũ chuyển ra khỏi ghi chú (chờ `exercises.md`, giai đoạn III); số liệu bài 7 vẫn có trong Ví dụ 05.7, 05.12, 05.13, 05.16.

### Giáo trình đã tham khảo theo mục

Sutton và Barto (2018) đọc trực tiếp trên bản PDF `/data/tqlong/qa/sources/sutton-barto-rl2020` (trang in = trang PDF − 22); chỉ tham khảo cách dẫn dắt và phát biểu, không dịch, không chép.

| Mục ghi chú | Giáo trình và mục | Điều đã học |
|---|---|---|
| Mục 1 | S&B §5.1 tr. 92 (đoạn mở), §6.1 tr. 119; mở đầu chương 6 tr. 119 | Mở bằng giới hạn của quy hoạch động: cần mô hình; dự đoán trước điều khiển |
| 1.2, 2.4–2.5 | S&B §2.4 tr. 30–31 (dạng NewEstimate = OldEstimate + StepSize[Target − OldEstimate], (2.4)); §2.5 tr. 32–33 ((2.6), (2.7)) | Khung cập nhật chung; trọng số bước hằng; điều kiện bước học |
| 2.1 | S&B §3.3–3.4 tr. 54–57 | Lượt, lợi tức, quy ước kết thúc và $\gamma=1$ |
| 2.2–2.3, 2.6 | S&B §5.1 tr. 92–93 (lần ghé, hộp giả mã first-visit duyệt lùi) | Định nghĩa hai quy tắc; ghi chú giữ thuật toán hai pha (lùi tính $G$, xuôi chọn lần ghé) như deck, lý do: tách hai việc cho người học |
| 2.7–2.8 | S&B §5.1 tr. 93 (hội tụ, không chệch, $1/\sqrt n$; dẫn Singh và Sutton 1996); chú dẫn chương 5 tr. 116 | Phát biểu hai kết quả; chứng minh mọi lần ghé bằng luật số lớn theo lượt là bổ sung của tác tử soạn (đủ bước) |
| 3.1–3.2 | S&B §6.1 tr. 119–121 (TD(0), hộp giả mã, sai số TD (6.5), (6.6), so sánh mục tiêu MC/DP/TD) | Mục tiêu TD là kết hợp lấy mẫu và bootstrap; thứ tự đọc–ghi |
| 4.3–4.5 | S&B §6.1 tr. 120 ((6.3)–(6.4)); §6.2 tr. 124 | Độ chệch qua Bellman kỳ vọng; phương sai: chỉ phát biểu cho mục tiêu lý tưởng (luật phương sai toàn phần) |
| 4.6 | S&B §6.2 tr. 124 (phát biểu hội tụ với (2.7)); chú dẫn chương 6 tr. 139 (Dayan 1992; Jaakkola, Jordan, Singh 1994; Tsitsiklis 1994) | Định lý 05.29 dẫn nguồn có mục và trang; chứng minh ngoài phạm vi, nêu ý tưởng |
| 5 | S&B §6.3 tr. 126–128 (cập nhật theo lô, Ví dụ 6.4, ước lượng tương đương chắc chắn, chi phí $n^2$, $n^3$) | Hai nghiệm theo lô; chứng minh hội tụ TD theo lô với $\alpha N(s)\le1$ là bổ sung của tác tử soạn |
| Hướng dẫn đọc thêm | S&B §7.1 tr. 142–145 | Chủ đề đọc thêm TD $n$ bước |

Không đọc trực tiếp trong đợt này: giáo trình *Học máy thống kê* (giọng kể theo `AGENTS.md` và bộ mẫu Bài 07 của math-4-AI), Szepesvári (2010), Bertsekas và Tsitsiklis (1996). Bertsekas và Tsitsiklis (1996) chỉ được dẫn ở mức chương trong mục đọc thêm, theo danh mục tài liệu của S&B; thông tin xuất bản của Dayan (1992), Jaakkola và cộng sự (1994), Tsitsiklis (1994), Singh và Sutton (1996), Tsitsiklis và Van Roy (1997) đối chiếu với danh mục tài liệu của S&B.

### Số hiệu cuối cùng

- Bộ đếm chung: 05.1 Định nghĩa (bài toán dự đoán phi mô hình); 05.2 Nhận xét; 05.3 Định nghĩa (lượt, lợi tức); 05.4 Mệnh đề (truy hồi); 05.5 Bổ đề (đuôi hình học của $T$); 05.6 Định nghĩa (lần ghé); 05.7 Mệnh đề (kỳ vọng sau lần ghé thứ $k$); 05.8 Định nghĩa (ước lượng MC); 05.9 Mệnh đề (trung bình gia tăng); 05.10 Định nghĩa (mục tiêu cập nhật, bước học); 05.11 Mệnh đề (trọng số bước hằng); 05.12 Nhận xét (hai trục); 05.13 Thuật toán (dự đoán MC); 05.14 Nhận xét; 05.15 Định nghĩa (không chệch, hội tụ h.c.c.); 05.16 Định lý (MC lần ghé đầu tiên); 05.17 Định lý (MC mọi lần ghé); 05.18 Nhận xét (bước hằng không hội tụ); 05.19 Định nghĩa (mục tiêu TD, sai số TD); 05.20 Thuật toán (TD(0)); 05.21 Nhận xét (kết thúc, tự chuyển, cắt ngắn); 05.22 Nhận xét (chi phí); 05.23 Định nghĩa (độ chệch của mục tiêu); 05.24 Mệnh đề (độ chệch mục tiêu TD); 05.25 Hệ quả; 05.26 Mệnh đề (kỳ vọng sai số TD là phần dư Bellman); 05.27 Định lý (phương sai mục tiêu lý tưởng); 05.28 Nhận xét; 05.29 Định lý (hội tụ TD(0)); 05.30 Nhận xét; 05.31 Thuật toán (cập nhật theo lô); 05.32 Mệnh đề (nghiệm MC theo lô); 05.33 Mệnh đề (nghiệm TD theo lô); 05.34 Nhận xét.
- Ví dụ 05.1–05.25; Tình huống 05.1–05.2; Bài tập 05.1–05.22 (05.1–05.16 trong mục, 05.17–05.22 củng cố). `exercises.md` bắt đầu từ Bài tập 05.23.
- Bài tập trùng trang chiếu theo kế hoạch C: B13 ↔ Bài tập 05.5; C10 ↔ Bài tập 05.9. Bài tập 05.20 (lượt thứ ba $e_3$) là bài "E06" của kế hoạch A2; `exercises.md` không lặp đề này (bỏ mục tùy chọn 05.32 của kế hoạch C).

### Sai khác so với kế hoạch B và lý do

- Năm mục nội dung thay bốn mục của B1, theo lưu ý riêng Bài 05 của điều phối viên: Mục 1 (mạch 1: bài toán, ví dụ xuyên suốt, khung cập nhật), Mục 2–5 (mạch 2–5), mạch 6 thành tình huống và tóm tắt.
- Số hiệu lệch B2 từ 05.5: thêm Bổ đề 05.5 (đuôi hình học) để Mệnh đề 05.7, Định lý 05.16–05.17 có giả thiết khả tích đủ; thêm Định nghĩa 05.15 (không chệch, hội tụ h.c.c.) và Nhận xét 05.18 (phương sai giới hạn $\alpha\sigma^2/(2-\alpha)$ của bước hằng) thay Nhận xét 05.14 của B2; thêm Nhận xét 05.14 về hai chiều duyệt. Định lý mọi lần ghé (05.17) có chứng minh đủ bằng luật số lớn theo lượt thay vì "ngoài phạm vi".
- Ví dụ thêm: 05.9 (phân phối mẫu tại $\mathrm S$, $\operatorname{Var}=320/441$), 05.10 (ô chờ: mọi lần ghé chệch $-1/2$ ở một lượt; số liệu sư phạm tự xây dựng), 05.14 (hai chuyển thật của notebook thay số liệu tự chuyển giả định), 05.15 (điểm cố định $r/(1-\gamma)$), 05.22 (ba lịch bước học). Ví dụ 05.19 của B2 (ô tự chuyển Lunar Lander) thành Ví dụ 05.14–05.15.
- Chủ đề mới: `lec-05-topic-17` (khung chung), `-18` (trung bình gia tăng và bước hằng), `-19` (không chệch và hội tụ MC), `-20` (cầu nối tiên quyết), `-21` (bổ sung: chệch của mọi lần ghé), `-22` (bổ sung: tự chuyển), `-23` (đọc thêm: sai số MC là tổng sai số TD). Các mã `-01`…`-16` giữ cho chủ đề còn tồn tại; `-06` nay chỉ "lần ghé", `-11` nay chỉ hội tụ TD(0).
- Bài tập củng cố "chứng minh 05.9 bằng quy nạp" của B4 không dùng vì Mệnh đề 05.11 đã chứng minh bằng quy nạp trong mục; thay bằng Bài tập 05.19 (sai số MC bằng tổng sai số TD, S&B (6.6)).
- Tình huống 05.2 chọn "coi điểm cắt là trạng thái kết thúc" (tính trên tàu đổ bộ thu nhỏ với cắt sau hai chuyển: độ chệch $-0{,}16\cdot11/21\approx-0{,}084$) cùng số liệu notebook; phần "ô gộp không Markov" nằm trong Tình huống 05.1.
- SVG: dùng `design-grid.svg` (Mục 2.5). Không dùng `mc-td-timeline.svg` vì nhãn "S₁=x" (chữ thường) lệch tên ô $\mathrm X$; đề nghị giai đoạn deck xóa hoặc sửa nhãn rồi ghi lại. Thêm `variance-decomposition.svg` (thanh xếp chồng phân rã phương sai, có `<title>`, `<desc>`, gạch chéo phân biệt hai phần không chỉ bằng màu, dấu thập phân phẩy).

### Số liệu đã tính lại

$v_\pi(\mathrm S)=11/21$, $v_\pi(\mathrm X)=19/21$; $\Pr(G_0=1\mid\mathrm S)=16/21$; $\operatorname{Var}(G_t\mid\mathrm S)=320/441$, $\operatorname{Var}(Y^*\mid\mathrm S)=256/441$, hiệu $64/441$ (20%); tại $\mathrm X$: $80/441$, $16/441$; độ chệch mục tiêu TD tại $\mathrm S$ với $V(\mathrm X)=0{,}5$: $-34/105$; với $V=(1,1)$: $8/105$ tại $\mathrm S$, $2/21$ tại $\mathrm X$; bảng độ lệch (sau $e_1$: $-1/42$, $-17/42$, $-11/21$; sau $e_2$: $-65/84$, $-97/84$, $-151/168$, $-89/168$; MC mọi lần ghé $-365/336$, $-173/168$; sau $e_3$: $-25/168$, $-89/168$, $-73/336$); dãy bảy ô (phân số chính xác, $\gamma=99/100$): $u\approx(0{,}4567;\ 0{,}8292;\ 0{,}9328;\ 0{,}9705;\ 0{,}9922)$, $m(\mathrm S)\approx0{,}9051$, $\operatorname{Var}(G_t)\approx0{,}2175$, $\operatorname{Var}(Y^*)\approx0{,}0355$, tỉ lệ đuôi $0{,}837$; bốn cấu hình MC, TD(0) trên $e_1,e_2,e_3$; $\varepsilon_0=0{,}84$ cho Bổ đề 05.5; ô chờ $\mathbb E[N]=2$, $\mathbb E[N^2]=6$; phương sai giới hạn bước hằng $0{,}242$ ($\alpha=0{,}5$), $0{,}038$ ($\alpha=0{,}1$); $n=291$ lượt cho độ lệch chuẩn $\le0{,}05$; tích $\prod(1-1/(k+1)^2)\to1/2$; A–B: $V_2(\mathrm A)=3/32$, $V_3(\mathrm A)=45/256$, $V_k(\mathrm A)=\tfrac34[1-(7/8)^{k-1}]$, dừng với $\theta=0{,}01$ ở $k=18$, sai số $0{,}068$; $0{,}995^{100}\approx0{,}606$, $0{,}995^{460}\approx0{,}0997$; Ví dụ 05.14 tính lại từ output notebook ($44{,}3715$, $0{,}5215$, $67{,}168$). Các con số của notebook (J, $V(S_0)$, số lượt cắt ngắn, tỉ lệ tự chuyển) chép từ output đã nhúng, gymnasium 1.3.0.

### Giới hạn còn lại

- Tham chiếu chéo tới Bài 03, 04 dùng "ghi chú Bài 0N, Mục k" theo kế hoạch sửa của hai bài đó (Bài 03: Mục 1–4; Bài 04: Mục 1); cần đồng bộ sang số hiệu `0N.k` ở đợt sau. Bài 06, 07, 08 được dẫn theo bài, không theo mục.
- Viewer ở 390×844 báo `scrollWidth > clientWidth` (510 so với 390): nguồn là các phần tử `.katex-mathml` (đặt `position:absolute`) nằm trong bảng cuộn ngang; nội dung nhìn thấy không tràn, bảng và công thức khối cuộn trong khung. Hiện tượng giống ghi chú Bài 07; sửa cần một luật trong `material-viewer.css` (ví dụ `position:relative` cho ô bảng), ngoài phạm vi tác tử này.
- Các SVG cũ của Bài 05 dùng dấu chấm thập phân (`0.8`, `0.2`) và nhãn `x₁` chữ thường; việc sửa thuộc giai đoạn deck.
- Notebook dẫn ghi chú theo tên mục cũ ("mục Thuật toán TD(0) và các trường hợp biên", "mục Độ chệch…", "quy trình sáu bước"); ánh xạ mới: Mục 3.2 / Thuật toán 05.20, Mục 4.3 / Mệnh đề 05.24, Mục 4.5 / Định lý 05.27, Mục 5 / Thuật toán 05.31, Thuật toán 05.13. Sửa ở giai đoạn III.
- Các chỗ đề nghị tác tử rà toán soi kỹ: chứng minh Định lý 05.17 (đổi thứ tự tổng–kỳ vọng, khả tích $Z_e$); Bước 2 của Bổ đề 05.5 (tính Markov tại thời điểm cố định $jn$); Bước 2–4 của chứng minh Mệnh đề 05.33 (ma trận không âm, trường hợp $\gamma=1$); phát biểu giả thiết $\gamma=1$ của Định lý 05.29; diễn giải "Bước 1, 2, 4 của Định lý 05.17 không cần Markov" trong Tình huống 05.1.

### Tự kiểm `no-ai-slop` (Edit) và `quill`

- Phạm vi: toàn bộ `lecture-note.md`. Đã đọc `SKILL.md` và đối chiếu `eval.md` sau khi soạn. Đạt: không từ cấm hay trạng từ rỗng; không câu hỏi tu từ, không mở mục bằng định nghĩa; không "rõ ràng", "dễ thấy", "suy ra ngay"; một gạch dài duy nhất ở tiêu đề theo mẫu; không đoạn tóm tắt lặp lại cuối mục ngoài đoạn kết mục ba ý bắt buộc. Đã sửa trong lúc tự kiểm: "suy ra ngay", "thực chất là", "chính là", hai chỗ nhắc "trang chiếu" trong bản đồ chủ đề, một câu cơ chế chưa có căn cứ về ô 3426 (thay bằng phát biểu theo notebook), một ví dụ bù trừ độ chệch dùng $V(\mathrm L)\ne0$ (thay bằng ví dụ trên dãy bảy ô). Còn lại có chủ đích: câu "Mô tả này chưa phải định nghĩa/định lý" lặp lại vì `AGENTS.md` bắt buộc; đoạn kết mục mở bằng "Như vậy," theo mẫu.
- `quill` (Outline, Threads, Concept, Revise dùng làm bảng kiểm, không tạo `quill.json`): mỗi khái niệm trọng tâm đi đủ vấn đề → trực giác → ví dụ → hình thức → kết quả/thuật toán → ứng dụng ("Trong thực hành", tình huống) → kiểm tra (bài tập); ba thuật toán đều có ví dụ tính tay trước khối `algorithm` (05.8 → 05.13; 05.11–05.12 → 05.20; 05.23–05.24 → 05.31). Sợi chỉ mở ở Mục 1 (bốn câu hỏi) đóng ở Mục 2 (mục tiêu, hội tụ MC), Mục 3 (cập nhật sớm), Mục 4 (độ chệch, phương sai, hội tụ TD), Mục 5 (dữ liệu cố định). Thuật ngữ thống nhất: lợi tức, lượt, lần ghé, mục tiêu cập nhật, mục tiêu bootstrap, sai số TD, độ chệch, phần dư Bellman (khớp Bài 04), cập nhật theo lô, lượt quét.

### Kiểm tra

- `note_check.py`: 34 số hiệu chung liên tục (không khuyết, không trùng), 25 ví dụ, 22 bài tập; không khối lạ, không khối chưa đánh số, không mẫu câu cấm; không `\(`/`\[`.
- `check_note.py 05 lecture-05-du-doan-phi-mo-hinh.html` (server cổng 8766): 0 lỗi KaTeX, 140 khối, 0 lỗi console, không yêu cầu ra ngoài, không tài nguyên hỏng ở 1600×900 và 390×844; `overflow` false ở 1600, true ở 390 do `.katex-mathml` trong bảng cuộn (xem Giới hạn).
- Đã xem ảnh chụp: Ví dụ 05.8 và chứng minh Định lý 05.27 ở 1600; Ví dụ 05.21 ở 390; `variance-decomposition.svg` hiển thị độc lập. Công thức khối duy nhất bị cắt ở 1600 (chứng minh Mệnh đề 05.24, Bước 3 của Định lý 05.27) đã rút gọn bằng ký hiệu $\mathbb E_s$; kiểm lại không còn công thức khối nào vượt khung ở 1600.

## Đợt sửa 2026-10-12 — Giai đoạn I, vòng sửa sau rà soát vai A và vai B

### Tác tử và phạm vi

Cùng tác tử soạn của mục trên (general-purpose theo brief, claude-opus-5-5, effort high), sửa theo quyết định của điều phối viên trên hai báo cáo `review-05-A.md` (vai toán) và `review-05-B.md` (vai mạch viết). Chỉ ghi `materials/lec-05/lecture-note.md` và nhật ký này; không tạo SVG mới trong vòng này. Không commit.

### Số từ

Trước: 32 643 (`wc -w`). Sau: 28 304 (`wc -w`); 27 887 khi tính mỗi công thức nội dòng là một từ và bỏ công thức khối.

Chưa đạt đích dưới 25 000. Lý do: đã làm toàn bộ mức A (A1–A20), mức B trừ B3, C2–C5 và C6 trên đúng các đoạn được liệt kê; không làm mức D và không mở rộng C6 ra các đoạn khác theo quyết định. Phần sửa bắt buộc của vai A và vai B thêm khoảng 900 từ: Nhận xét 05.18 thay Mục 2.8, đoạn ý tưởng của Bổ đề 05.5, đoạn trường hợp $\gamma=1$ sau chứng minh Mệnh đề 05.34, câu về $\gamma=1$ cho Định lý 05.30, quy ước đọc dạng danh sách, thuật ngữ gốc ở lần đầu, tách câu trong đoạn mở. Bảng Bản đồ chủ đề còn 1 128 từ, cao hơn ước lượng 900 của vai B vì giữ cột Nguồn có số trang. Muốn xuống dưới 25 000 cần thêm mức D hoặc C6 trên toàn tệp; đề nghị điều phối viên chọn. Phần vượt 20 000: chương có năm mục nội dung, 35 môi trường đánh số có chứng minh đủ bước, hai tình huống và bảng số liệu notebook; các phần này đều là thành phần bắt buộc.

### Phát hiện và xử lý

Cột "Dòng mới" ghi số dòng trong `lecture-note.md` sau vòng sửa; "—" là phần bị cắt hoặc chuyển.

| Mã | Mức | Xử lý | Trạng thái | Dòng mới |
|---|---|---|---|---|
| A-1 | nghiêm trọng | Viết lại: phần dao động quanh lợi tức kỳ vọng theo ô không vượt $J$ nhỏ nhất (khoảng 1627); 3021 là $J$ của bảng hằng. Ở Tình huống 05.1, câu về bảng hằng tách khỏi câu phân rã | đã sửa | 1404, 1732 |
| A-2 | trung bình | Đoạn mở và dòng đầu bảng của mục Tình huống: hội tụ về trung bình lợi tức theo lần ghé qua Bước 1 và 4 của chứng minh Định lý 05.17; bằng $v_\pi$ chỉ khi Markov | đã sửa | 1710, 1714 |
| A-3 | trung bình | Tình huống 05.2: mục tiêu trên chuyển tại điểm cắt lệch $-11/21$ so với mục tiêu lý tưởng; nêu không cùng loại với $-0{,}084$; bỏ dẫn Mệnh đề 05.25 | đã sửa | 1772 |
| A-4 | trung bình | "Bước 1 và 4 không dùng Markov; khả tích ở Bước 2 suy từ $T\le1000$; lượt giữ lại vẫn độc lập cùng phân phối"; sửa Dẫn ngược | đã sửa | 1748, 1754 |
| A-5 | nhẹ | Bước 2 Định lý 05.17: chặn $\sum_k\lvert G_{t_k}\rvert\mathbf 1\{N\ge k\}\le R_{\max}T_e^2$; câu về $k$ có xác suất $0$ | đã sửa | 780, 792 |
| A-6 | nhẹ | Nhận xét 05.19: thêm lập luận không hội tụ h.c.c. | đã sửa | 810 |
| A-7 | nhẹ | Ý tưởng chứng minh Định lý 05.30: thêm trường hợp $\gamma=1$ (chuẩn có trọng số, Dayan 1992) | đã sửa | 1470 |
| A-8 | nhẹ | Bài tập 05.15 cũ (giá trị khi $\gamma=1$) | bỏ cùng bài tập theo quyết định 3 | — |
| A-9 | nhẹ | Thực hành Mục 4.2: $v_\pi$ của ô không định nghĩa; dùng lợi tức kỳ vọng theo ô, "theo nghĩa gần đúng" | đã sửa | 1248 |
| A-10 | nhẹ | "trong cả 2000 lượt của lần chạy" | đã sửa | 1404 |
| A-11 | nhẹ | Ghi "trung bình qua năm thứ tự lượt" ở thực hành Mục 2.6, 4.2, 4.4; câu giải thích 2101 so 2085 trong Tình huống 05.1 | đã sửa | 813, 1248, 1483, 1734 |
| A-12 | nhẹ | Ví dụ 05.11: ghi số chữ số thập phân in ra và việc dùng giá trị đã làm tròn | đã sửa | 988 |
| A-13 | nhẹ | Thuật toán 05.32: Monte Carlo theo lô dùng mọi lần ghé; Mục 5.3: $N(s)$ là số lần ghé, cũng là số chuyển rời $s$ | đã sửa | 1545, 1591 |
| B-1 | nghiêm trọng | Cắt theo mức A, B (trừ B3), C2–C5, C6 có giới hạn; 32 643 → 28 304 | sửa một phần; còn vượt đích, xem mục Số từ | — |
| B-2 | trung bình | Bỏ 05.4, 05.10, 05.13, 05.15, 05.8(b), 05.16(b)(c); chuyển 05.5, 05.9, 05.6(b), 05.11, ô chờ, 05.22 sang danh sách dưới | đã sửa | — |
| B-3 | trung bình | Gộp 2.3 vào trung bình gia tăng (Mục 2.3), Ví dụ 05.3 làm ví dụ trước Định nghĩa 05.8; thêm câu trực giác cho bước hằng | đã sửa | 443, 534 |
| B-4 | trung bình | Thay lời quy trình bằng câu quy ước dẫn mục | đã sửa | 19 |
| B-5 | trung bình | $n\to\lvert\mathcal S\rvert$ trong Bổ đề 05.5; $H\to\mathcal H$ cho tập đã ghé; ma trận $M$ biến mất cùng chứng minh rút gọn của Mệnh đề 05.34 (không cần $A_\beta$); $Z\to I_1$ trong chứng minh Định lý 05.28; giữ $Z_e$ ở Định lý 05.17 | đã sửa | 300, 623, 652, 1360 |
| B-6 | trung bình | Thuật ngữ gốc ở lần đầu: prediction, episode, return, update target, bias, batch updating (đoạn mở); truncated episode, visit, first-visit, every-visit, step size, terminal state, self-transition, variance (Mục tiêu); MDP, Bellman residual, almost surely (Tiên quyết); sweep (Bảng ký hiệu); Markov reward process (Mục 5.3). Bỏ bản lặp ở định nghĩa sau | đã sửa | 3–13, 21–26, 54, 1626 |
| B-7 | trung bình | Định nghĩa ngắn $J$ ở lần dùng đầu (thực hành Mục 2.6) | đã sửa | 813 |
| B-8 | trung bình | Như A-11 | đã sửa | 1734 |
| B-9 | trung bình | Quy ước đọc thành danh sách | đã sửa | 60–66 |
| B-10 | trung bình | Chứng minh Mệnh đề 05.34 rút gọn: Bước 1, ánh xạ co khi $\gamma<1$, Banach; $\gamma=1$ thành đoạn ý tưởng | đã sửa | 1647 |
| B-11 | trung bình | $\hat r$, $\hat P$, $\hat T$ đưa vào Giả thiết của Mệnh đề 05.34 | đã sửa | 1628 |
| B-12 | trung bình | Tách đoạn mở Mục 4.4 (bài toán / trực giác) | đã sửa | 1433 |
| B-13 | trung bình | Ví dụ 05.21, 05.22, Bài tập 05.9, 05.10 nêu lại dữ liệu tám lượt; 05.10 cũ, 05.7(c) cũ bỏ | đã sửa | 1512, 1569, 1689, 1847 |
| B-14 | trung bình | Tiên quyết nêu cả phần dư Bellman tại $s$ và chuẩn cực đại của nó | đã sửa | 25 |
| B-15 | trung bình | Ghi mục "Sửa kế hoạch C" dưới đây | đã sửa | — |
| B-16 | trung bình | Kết mục 2, 3, 4 rút còn một câu nối; giữ đoạn mở mục sau | đã sửa | 835, 1059, 1487 |
| B-17 | nhẹ | Gạch "Bỏ dùng $v_\pi$" dẫn Nhận xét 05.29 | đã sửa | 1390 |
| B-18 | nhẹ | Đoạn mở Mục 5 không liệt kê lại dữ liệu; bỏ "Hai cách đọc" trong Ví dụ 05.20 | đã sửa | 1491 |
| B-19 | nhẹ | Ví dụ bù trừ thành một câu, bỏ tham chiếu tiến | đã sửa | 1214 |
| B-20 | nhẹ | Bước nhận xét ngoài khối `remark` ở 2.1, 2.2 | chấp nhận, không sửa: các đoạn "Bỏ giả thiết" theo mẫu `AGENTS.md` cho bản đọc định lý | — |
| B-21 | nhẹ | Bỏ hai câu nhãn rỗng | đã sửa | 616, 924 |
| B-22 | nhẹ | Lời giải cập nhật ba dòng ở Bài tập 05.13; hai bài còn lại đã chuyển | đã sửa | 1940 |
| B-23 | nhẹ | Tách câu nhiều ngoặc ở đoạn mở và Ví dụ 05.1 | đã sửa | 3, 124 |
| B-24 | nhẹ | $\varepsilon_0\to\rho$ | đã sửa | 297, 312 |
| B-25 | nhẹ | $G_{\max}$ | bỏ cùng đoạn "Trên Lunar Lander" (C3) | — |
| B-26 | nhẹ | Câu về tệp bài tập viết ở dạng tồn tại độc lập, không dẫn liên kết | đã sửa | 1843 |
| B-27 | nhẹ | Xấp xỉ $n^{-(1-\gamma)}$ bỏ cùng B5; thực hành Mục 4.4 nêu hệ số $1-(1-\gamma)/n$ có lý do trực tiếp | đã sửa | 1483 |
| B-28 | nhẹ | Nhiều ngoặc dẫn số hiệu | chấp nhận theo đề xuất | — |
| slop 374 | — | "Một phép tính nhỏ cho thấy cơ chế." | bỏ cả đoạn (A3) | — |
| slop 372 | — | "Bài toán dự đoán đã đặt xong;" | viết lại | 197 |
| slop 1639 | — | "Độ chệch là một nửa của bức tranh." | thay câu nối thường | 1272 |
| slop 1375, 1835 | — | "Ví dụ X cho thấy hai điều." | bỏ, nêu thẳng | 1039, 1447 |
| slop 2119 | — | "Chương còn lại một việc:" | câu thường | 1705 |
| slop 751 | — | "Cấu trúc này đáng được đặt tên riêng" | "Ta đặt tên cho cấu trúc này vì…" | 518 |

Mức cắt đã làm: A1 (Bản đồ chủ đề thành bảng `Chủ đề (note-topic-id) | Nhóm | Mục | Vai trò | Vào → Ra | Nguồn`; sai khác so với mẫu dạng danh sách, được điều phối viên cho phép), A2–A20; B1, B2, B4–B10 (B9: chuyển Bài tập 05.22 cũ); C2 (tự chuyển gộp vào Mục 3.2 sau Nhận xét 05.22), C3, C4, C5 (2.3→2.4 cũ, 4.1→4.2 cũ, 4.4→4.5 cũ; Nhận xét 05.14 chỉ giữ ý trạng thái kết thúc và lượt dừng giữa chừng; rút gạch "Bỏ tính Markov" ở 2.2), C6 trên đoạn 1191, 1526, 1613, 1727, 2093, 2124, 2147 cũ. Không làm: B3 (giữ chứng minh Định lý 05.17, vai A xác nhận đúng), C1, mức D.

### Cấu trúc và số hiệu mới

Mục: 1.1–1.2; 2.1 Lượt và lợi tức, 2.2 Lần ghé, 2.3 Ước lượng Monte Carlo và trung bình gia tăng, 2.4 Bước học hằng và bốn cấu hình, 2.5 Thuật toán, 2.6 Không chệch và hội tụ (Nhận xét 05.18 thay Mục 2.8); 3.1, 3.2 (gồm phần tự chuyển); 4.1 Hai bảng và giá trị chuẩn, 4.2 Độ chệch, 4.3 Biến thiên và phương sai, 4.4 Hội tụ TD(0); 5.1–5.3. Giữ đủ 23 `note-topic-id`.

- Bộ đếm chung 05.1–05.35: 05.1–05.17 giữ số; mới 05.18 Nhận xét (mọi lần ghé chệch ở số lượt hữu hạn); cũ 05.18–05.34 thành 05.19–05.35 (Định nghĩa TD 05.20, Thuật toán TD(0) 05.21, Nhận xét 05.22, 05.23, Định nghĩa 05.24, Mệnh đề 05.25, Hệ quả 05.26, Mệnh đề 05.27, Định lý 05.28, Nhận xét 05.29, Định lý 05.30, Nhận xét 05.31, Thuật toán 05.32, Mệnh đề 05.33, 05.34, Nhận xét 05.35). Trong bảng "Phát hiện và xử lý" ở trên, số hiệu viết theo đánh số mới.
- Ví dụ 05.1–05.22. Ánh xạ cũ → mới: 1, 2, 3 giữ; 4 bỏ; 5→4; 6 gộp vào 7→5; 8→6; 9→7; 10 chuyển; 11→8; 12→9; 13→10; 14→11; 15→12; 16→13; 17→14; 18→15; 19→16; 20→17; 21→18; 22→19; 23→20; 24→21; 25→22.
- Bài tập 05.1–05.14. Ánh xạ cũ → mới: 1, 2, 3 giữ; 6→4 (bỏ câu b); 7→5 (bỏ câu c); 8→6 (bỏ câu b); 12→7; 14→8; 16→9 (chỉ câu a); 17→10; 18→11; 19→12; 20→13; 21→14. Bỏ: 4, 10, 13, 15. Chuyển: 5, 9, 11, 22. `exercises.md` tiếp theo từ Bài tập 05.15.
- Bài tập trùng trang chiếu: B13 và C10 nay không còn trong ghi chú (05.5 và 05.9 cũ đã chuyển).

### Chuyển cho exercises.md

Đề, gợi ý và lời giải giữ nguyên văn từ bản trước vòng sửa (số hiệu cũ), để giai đoạn III đánh số lại từ 05.15:

- Bài tập 05.5 cũ: trùng trang B13; gộp với C 05.24 nhưng bỏ phần chứng minh lại Mệnh đề 05.11.
- Bài tập 05.6 cũ, chỉ câu (b): giả thiết độc lập cùng phân phối của mẫu lần ghé đầu tiên.
- Bài tập 05.9 cũ: trùng trang C10; lời giải khớp Ví dụ 05.10 mới.
- Bài tập 05.11 cũ: gộp với C 05.25 (HW05 bài 7), thêm câu về mọi lần ghé.
- Ví dụ 05.10 cũ (ô chờ) và Bài tập 05.7 cũ câu (c): một bài mức chứng minh về độ chệch của mọi lần ghé; ghi chú giữ tóm tắt ở Nhận xét 05.18.
- Bài tập 05.22 cũ: tự chuyển trên Lunar Lander; gộp với C 05.26, chỉ giữ một bài.

```markdown
::: exercise Bài tập 05.5
Dữ kiện: hai lượt $e_1:\mathrm S\to\mathrm X\to\mathrm S\to\mathrm X\to\mathrm G$ với phần thưởng $(0,0,0,1)$ và $e_2:\mathrm S\to\mathrm X\to\mathrm S\to\mathrm L$ với phần thưởng $(0,0,-1)$; $\gamma=1$; bảng ban đầu bằng $0$.

(a) Tại $\mathrm X$, lập dãy lợi tức theo lần ghé đầu tiên và theo mọi lần ghé; tính hai trung bình.
(b) Dùng lần ghé đầu tiên với bước hằng $\alpha=0{,}5$: tính $V(\mathrm X)$ sau mỗi lượt và giải thích vì sao kết quả khác trung bình ở (a), dù tập mẫu giống nhau.
:::

::: hint
$\mathrm X$ xuất hiện hai lần trong $e_1$ và một lần trong $e_2$. Ở câu (b), dùng Mệnh đề 05.11 để viết kết quả thành tổng có trọng số.
:::

::: solution
(a) Lần ghé đầu tiên chọn $(1,-1)$, trung bình $0$. Mọi lần ghé chọn $(1,1,-1)$, trung bình $1/3$.

(b) Sau $e_1$: $0+0{,}5\cdot(1-0)=0{,}5$. Sau $e_2$: $0{,}5+0{,}5\cdot(-1-0{,}5)=-0{,}25$. Theo Mệnh đề 05.11, $-0{,}25=0{,}25\cdot0+0{,}25\cdot1+0{,}5\cdot(-1)$: giá trị khởi tạo còn trọng số $0{,}25$, và mẫu mới $-1$ có trọng số $0{,}5$ lớn hơn mẫu cũ. Trung bình mẫu đặt trọng số $0{,}5$ cho mỗi mẫu và $0$ cho giá trị khởi tạo.

**Kiểm tra lại.** Hàng thứ ba của Ví dụ 05.7 ghi $V(\mathrm X)=0{,}5$ sau $e_1$ và $-0{,}25$ sau $e_2$.
:::


::: exercise Bài tập 05.6
Dữ kiện: lượt $e_1:\mathrm S\to\mathrm X\to\mathrm S\to\mathrm X\to\mathrm G$ của tàu đổ bộ thu nhỏ.

(a) Mỗi trạng thái $\mathrm S$, $\mathrm X$ cung cấp bao nhiêu mẫu theo lần ghé đầu tiên và theo mọi lần ghé.
(b) Nêu giả thiết cho phép coi các mẫu lần ghé đầu tiên từ những lượt khác nhau là độc lập cùng phân phối.
(c) Giải thích vì sao bước 4 của Thuật toán 05.13 duyệt xuôi chứ không duyệt lùi.
:::

::: hint
Lần ghé đầu tiên được xác định riêng trong từng lượt. Ở câu (c), xét thứ tự các thời điểm ghé $\mathrm S$ trong $e_1$.
:::

::: solution
(a) Mỗi trạng thái cho một mẫu theo lần ghé đầu tiên và hai mẫu theo mọi lần ghé.

(b) Các lượt được sinh độc lập, cùng phân phối trạng thái đầu, dưới cùng chính sách cố định và môi trường dừng. Khi đó mẫu lần ghé đầu tiên của mỗi lượt là một hàm của riêng lượt đó, nên các mẫu từ những lượt khác nhau độc lập cùng phân phối. Các mẫu trong cùng một lượt thì có thể phụ thuộc nhau.

(c) Lần ghé đầu tiên của $\mathrm S$ là $t=0$. Duyệt lùi gặp $t=2$ trước; nếu đánh dấu $\mathrm S$ ở đó và bỏ qua $t=0$, mẫu được giữ là $G_2$, tức lần ghé cuối cùng. Với $\gamma<1$, $G_2=\gamma$ khác $G_0=\gamma^3$ (Ví dụ 05.2).

**Kiểm tra lại.** Với $\gamma=0{,}9$: $G_0=0{,}729$, $G_2=0{,}9$; hai quy tắc cho hai mẫu khác nhau.
:::


::: exercise Bài tập 05.9
Dữ kiện: tàu đổ bộ thu nhỏ, $\gamma=1$, $\alpha=0{,}5$; bảng ban đầu $V(\mathrm S)=0{,}25$, $V(\mathrm X)=0{,}5$, $V(\mathrm L)=0$. Xét riêng hai trường hợp, mỗi trường hợp bắt đầu từ cùng bảng ban đầu:

(a) chuyển $\mathrm S\to\mathrm X$ với phần thưởng $0$;
(b) chuyển $\mathrm S\to\mathrm L$ với phần thưởng $-1$.

Với mỗi trường hợp, tính mục tiêu, sai số TD, giá trị mới tại $\mathrm S$, và nêu các phần tử giữ nguyên.
:::

::: hint
Trong trường hợp (b), trạng thái sau là trạng thái kết thúc. Trường hợp (b) không dùng kết quả của trường hợp (a).
:::

::: solution
(a) $Y=0+0{,}5=0{,}5$; $\delta=0{,}5-0{,}25=0{,}25$; $V(\mathrm S)=0{,}25+0{,}5\cdot0{,}25=0{,}375$.

(b) $Y=-1+0=-1$; $\delta=-1-0{,}25=-1{,}25$; $V(\mathrm S)=0{,}25+0{,}5\cdot(-1{,}25)=-0{,}375$.

Trong cả hai trường hợp, $V(\mathrm X)=0{,}5$ và $V(\mathrm L)=0$ giữ nguyên.

**Kiểm tra lại.** Ở (b), phần thưởng $-1$ xuất hiện một lần trong mục tiêu; giá trị tiếp nối $V(\mathrm L)=0$.
:::


::: exercise Bài tập 05.11
Dữ kiện: tàu đổ bộ thu nhỏ với giá trị chuẩn $v_\pi(\mathrm S)=11/21$, $v_\pi(\mathrm X)=19/21$. Monte Carlo mọi lần ghé với $\alpha=0{,}5$, khởi tạo $0$, cho $(V(\mathrm S),V(\mathrm X))=(-0{,}5625;\ -0{,}125)$ sau hai lượt $e_1$, $e_2$ (Ví dụ 05.7).

(a) Tính độ lệch tại hai trạng thái.
(b) So với Monte Carlo lần ghé đầu tiên cùng bước học, sau $e_2$ (Ví dụ 05.18), và giải thích chênh lệch bằng Mệnh đề 05.11.
:::

::: hint
Tại $\mathrm S$, mọi lần ghé thực hiện hai cập nhật với mục tiêu $-1$ trong $e_2$.
:::

::: solution
(a) $-0{,}5625-11/21=-365/336\approx-1{,}086$ tại $\mathrm S$; $-0{,}125-19/21=-173/168\approx-1{,}030$ tại $\mathrm X$.

(b) Lần ghé đầu tiên cho độ lệch $-0{,}774$ và $-1{,}155$. Tại $\mathrm S$, mọi lần ghé lệch xa hơn vì hai mẫu $-1$ cuối cùng nhận trọng số $0{,}5$ và $0{,}25$ theo Mệnh đề 05.11, tổng $0{,}75$ cho kết cục rơi. Tại $\mathrm X$, mọi lần ghé gần hơn vì $e_1$ góp hai mẫu $1$, kéo giá trị lên $0{,}75$ trước khi gặp mẫu $-1$.

**Kiểm tra lại.** Theo Mệnh đề 05.11 với bốn mẫu $(1,1,-1,-1)$ và $\alpha=0{,}5$: $V_4=0{,}0625\cdot0+0{,}0625\cdot1+0{,}125\cdot1+0{,}25\cdot(-1)+0{,}5\cdot(-1)=-0{,}5625$.
:::


::: exercise Bài tập 05.7
(a) Với tàu đổ bộ thu nhỏ của Ví dụ 05.9 ($v_\pi(\mathrm S)=11/21$, $\operatorname{Var}(G_0)=320/441$), tìm số lượt nhỏ nhất để độ lệch chuẩn của trung bình lần ghé đầu tiên tại $\mathrm S$ không vượt $0{,}05$.

(b) Với cùng phương sai mẫu, tính độ lệch chuẩn giới hạn của Monte Carlo lần ghé đầu tiên với bước hằng $\alpha=0{,}1$, và so với kết quả (a).

(c) Trong ô chờ của Ví dụ 05.10, một lượt có $N=4$ lần ghé. Tính ước lượng lần ghé đầu tiên và ước lượng mọi lần ghé từ riêng lượt này.
:::

::: hint
(a) Giải $\sqrt{(320/441)/n}\le0{,}05$. (b) Dùng Nhận xét 05.18. (c) Tại lần ghé thứ $k$, lợi tức là $N-k$.
:::

::: solution
(a) Điều kiện là $n\ge(320/441)/0{,}0025\approx290{,}2$, nên cần $n=291$ lượt.

(b) Phương sai giới hạn là $\alpha\sigma^2/(2-\alpha)=0{,}1\cdot0{,}7256/1{,}9\approx0{,}0382$, độ lệch chuẩn khoảng $0{,}195$. Trung bình mẫu đạt độ lệch chuẩn $0{,}05$ sau $291$ lượt và tiếp tục giảm; bước hằng $0{,}1$ dừng ở khoảng $0{,}195$ dù chạy bao lâu.

(c) Các lợi tức là $3,2,1,0$. Lần ghé đầu tiên cho $3$; mọi lần ghé cho trung bình $(3+2+1+0)/4=1{,}5=(N-1)/2$.

**Kiểm tra lại.** Ở (a), $\sqrt{0{,}7256/291}\approx0{,}0499\le0{,}05$, còn $\sqrt{0{,}7256/290}\approx0{,}05002>0{,}05$.
:::


::: exercise Bài tập 05.22
Dữ kiện: một ô của Lunar Lander trong đó tàu chỉ tự chuyển, với cùng phần thưởng $r$ mỗi bước; $\gamma=0{,}99$; TD(0) (Ví dụ 05.15).

(a) Với bước hằng $\alpha=0{,}5$, tìm số tự chuyển nhỏ nhất để khoảng cách tới điểm cố định $r/(1-\gamma)$ còn không quá $10\%$ khoảng cách ban đầu.
(b) Với bước $\alpha_n=1/n$ và xấp xỉ hệ số thu hẹp bằng $n^{-(1-\gamma)}$, ước lượng số tự chuyển cần cho cùng yêu cầu.
(c) Giải thích vì sao Monte Carlo không gặp vấn đề này.
:::

::: hint
(a) Giải $0{,}995^k\le0{,}1$. (b) Giải $n^{-0{,}01}\le0{,}1$.
:::

::: solution
(a) $k\ge\ln0{,}1/\ln0{,}995\approx(-2{,}3026)/(-0{,}0050125)\approx459{,}4$, nên cần $460$ tự chuyển, tức $9{,}2$ giây mô phỏng với bước $0{,}02$ giây.

(b) $n^{-0{,}01}\le0{,}1$ tương đương $n\ge10^{100}$: lịch $1/n$ thỏa điều kiện Robbins–Monro nhưng không thu hẹp được khoảng cách trong bất kỳ số lần cập nhật thực tế nào.

(c) Mục tiêu Monte Carlo là $G_t$, đã chứa mọi phần thưởng về sau, kể cả phần thưởng $\pm100$ ở cuối lượt, nên không phụ thuộc giá trị của ô kế tiếp và không bị chuỗi tự chuyển làm chậm.

**Kiểm tra lại.** $0{,}995^{460}=e^{460\ln0{,}995}\approx e^{-2{,}306}\approx0{,}0997\le0{,}1$, còn $0{,}995^{459}\approx0{,}1002$.
:::


::: example Ví dụ 05.10 (Ô chờ: mọi lần ghé chệch, lần ghé đầu tiên không chệch)
**Mô hình.** Một trạng thái không kết thúc $\mathrm C$ và một trạng thái kết thúc. Từ $\mathrm C$, với xác suất $1/2$ tàu ở lại $\mathrm C$ và nhận phần thưởng $1$; với xác suất $1/2$ lượt kết thúc với phần thưởng $0$. Hệ số $\gamma=1$; mọi lượt bắt đầu ở $\mathrm C$.

**Giá trị chuẩn.** Phương trình Bellman kỳ vọng: $v=\tfrac12(1+v)+\tfrac12\cdot0$, nên $v_\pi(\mathrm C)=1$.

**Số lần ghé và lợi tức.** Gọi $N$ là số lần ghé $\mathrm C$ trong một lượt. Lượt gồm $N-1$ lần ở lại rồi một lần kết thúc, nên $\Pr(N=m)=(1/2)^m$ với $m\ge1$, và $\mathbb E[N]=2$, $\mathbb E[N^2]=6$. Tại lần ghé thứ $k$, còn $N-k$ lần ở lại, nên $G_{t_k}=N-k$.

**Lần ghé đầu tiên, một lượt.** Mẫu là $G_{t_1}=N-1$, kỳ vọng $\mathbb E[N]-1=1=v_\pi(\mathrm C)$: không chệch.

**Mọi lần ghé, một lượt.** Ước lượng là trung bình của $N$ mẫu:

$$
\hat v=\frac1N\sum_{k=1}^{N}(N-k)=\frac{N-1}{2},\qquad\mathbb E[\hat v]=\frac{\mathbb E[N]-1}{2}=\frac12\ne1 .
$$

**Giới hạn khi số lượt tăng.** Theo Bước 4 của chứng minh Định lý 05.17, giới hạn là $\mathbb E[Z]/\mathbb E[N]$ với $Z=\sum_k(N-k)=N(N-1)/2$, nên giới hạn bằng $\dfrac{(\mathbb E[N^2]-\mathbb E[N])/2}{\mathbb E[N]}=\dfrac{(6-2)/2}{2}=1$.

**Kiểm tra lại.** Với một lượt có $N=3$: các mẫu mọi lần ghé là $2,1,0$, trung bình $1$; mẫu lần ghé đầu tiên là $2$. Hai con số đều là mẫu; chỉ kỳ vọng qua mọi lượt mới cho thấy độ chệch $-1/2$.
:::
```

### Sửa kế hoạch C (theo B-15)

- C 05.24: bỏ phần chứng minh lại Mệnh đề 05.11 (ghi chú đã chứng minh); giữ bốn cấu hình và gộp với Bài tập 05.5 cũ.
- C 05.25 (HW05 bài 7): kết quả đã giải ở Ví dụ 05.5, 05.6, 05.9, 05.10 mới; đặt câu hỏi khác, ví dụ mọi lần ghé hoặc $\gamma=0{,}9$, và gộp Bài tập 05.11 cũ.
- C 05.26 [Lập trình]: chỉ giữ phần lập trình; phần tính tay tự chuyển dùng Bài tập 05.22 cũ ở trên, không lặp hai lần.
- C 05.28: phản ví dụ $V(\mathrm X)=10$, phương sai $19{,}36$ đã có ở Nhận xét 05.29; đổi số liệu phản ví dụ.
- C 05.29: trùng Bài tập 05.14 của ghi chú (lượt dài, thưởng thưa); đổi biến thể, ví dụ thêm điều kiện cắt ngắn, hoặc bỏ.
- Mục tùy chọn 05.32 (lượt thứ ba $e_3$): đã là Bài tập 05.13 của ghi chú; bỏ khỏi `exercises.md`.
- Số hiệu `exercises.md` bắt đầu từ Bài tập 05.15 (sửa thành 05.14 ở vòng cắt độ dài, rồi 05.16 ở vòng rà lại 2).

### Kiểm tra sau vòng sửa

- `note_check.py`: 35 số hiệu chung liên tục, 22 ví dụ, 14 bài tập; không khuyết, không trùng; không khối lạ, không khối chưa đánh số, không mẫu câu cấm; không `\(`/`\[`.
- `check_note.py 05 lecture-05-du-doan-phi-mo-hinh.html`: 0 lỗi KaTeX, 113 khối, 0 lỗi console, không yêu cầu ra ngoài, không tài nguyên hỏng; `overflow` false ở cả 1600×900 và 390×844.
- `no-ai-slop` (Edit, tự kiểm `eval.md`) trên mọi đoạn đã sửa: các mẫu vai B nêu đã xử lý; không thêm câu mở rỗng, câu kết kịch tính hay lời nhấn mạnh mới.

## Đợt sửa 2026-10-12 — Giai đoạn I, vòng cắt độ dài theo quyết định thứ hai của điều phối viên

Tác tử: cùng tác tử soạn (general-purpose theo brief, claude-opus-5-5, effort high); `no-ai-slop` Edit, tự kiểm `eval.md` trên mọi đoạn đã viết lại. Không commit.

### Số từ

Trước: 28 304 (`wc -w`). Sau: 24 980. Bản đồ chủ đề: 1 128 → 592 từ.

Phần vượt 20 000: chương có năm mục nội dung, 35 môi trường đánh số có chứng minh hoặc dẫn nguồn, 22 ví dụ tính tay, hai tình huống áp dụng và bảng số liệu notebook. Mọi thành phần này đều bắt buộc theo `AGENTS.md`, và tám bước của mỗi khái niệm trọng tâm được giữ nguyên.

### Bản đồ chủ đề (quyết định 3)

Bảng còn bốn cột `Chủ đề (note-topic-id) | Nhóm | Mục | Vai trò → sản phẩm dùng tiếp`, mỗi chủ đề một dòng. Đã bỏ cột Nguồn có số trang; số trang có ở mục Hướng dẫn đọc thêm và trong nhật ký này. Giữ đủ 23 mã.

### Mức D (quyết định 1)

Báo cáo `review-05-B.md` chỉ ghi nhãn "D1–D5", không ghi nội dung. Tác tử soạn hiểu mức D là các phép cắt có mất chi tiết nhưng không đụng chứng minh đã rút, không đụng tình huống và không bỏ bước nào trong tám bước. Các phép cắt đã làm:

- **D-a.** Nhận xét 05.23 (chi phí): bỏ bảng bốn dòng, giữ cùng các bậc chi phí trong hai câu.
- **D-b.** Nhận xét 05.19 (bước hằng): bỏ độ lệch chuẩn $0{,}49$ và phép tính chi tiết; giữ hai phương sai giới hạn $\approx0{,}242$ và $\approx0{,}038$ cùng lập luận không hội tụ hầu chắc chắn.
- **D-c.** Nhận xét 05.29: bỏ phép tính chi tiết của sai số bình phương trung bình; giữ hai kết quả $\approx0{,}465$ và $\approx72{,}3$.
- **D-d.** Kiểm lại sau Mệnh đề 05.25: rút còn một biểu thức.
- **D-e.** Tình huống 05.1: rút hai gạch Diễn giải và đoạn Giới hạn. Nội dung toán của vai A (Bước 1, 4; $T\le1000$; $\mu$) giữ nguyên.
- **D-f.** Ví dụ 05.1: bỏ câu kiểm về xác suất $0{,}2$ của chuyển lùi. Ví dụ 05.7: rút dòng Kiểm tra lại.
- **D-g.** Tiên quyết: bỏ câu "Cả hai cách tính đều cần mô hình", vì Mục 1 nêu lại ý này.

### C6 mở rộng (quyết định 2)

Biên tập gọn văn xuôi trên toàn tệp, theo nguyên tắc một ý một đoạn và bỏ câu lặp hoặc câu dẫn. Các đoạn đã viết lại:

- **Mục 1:** đoạn mở, đoạn lộ trình và đọc hình; Mục 1.1: trực giác, đọc hình, các đoạn sau Định nghĩa 05.1, Nhận xét 05.2, Bài tập 05.1(c); Mục 1.2: đoạn mở và kết mục.
- **Mục 2:** đoạn mở; 2.1: trực giác, đọc hình, diễn giải định nghĩa, trường hợp giới hạn, đoạn trước và sau Mệnh đề 05.4, ví dụ $\rho$, thực hành; 2.2: trực giác, diễn giải định nghĩa, sau Mệnh đề 05.7, thực hành, kiểm tra Bài tập 05.3; 2.3–2.4: đoạn mở, sau Mệnh đề 05.11; 2.6: đoạn mở, Nhận xét 05.18 (ô chờ), thực hành, kết mục.
- **Mục 3:** đoạn mở, trực giác, sau Định nghĩa 05.20, nhầm lẫn thường gặp, sau Thuật toán 05.21, phần tự chuyển, thực hành, kết mục.
- **Mục 4:** đoạn mở; 4.1: sau hai ví dụ; 4.2: đoạn mở, sau Định nghĩa 05.24, thực hành; 4.3: đoạn mở, sau Ví dụ 05.17, trước Ví dụ 05.18, đọc hình, sau Định lý 05.28, gạch "Bỏ tính Markov", thực hành; 4.4: đoạn mở, sau Ví dụ 05.19, ý tưởng chứng minh Định lý 05.30 (giữ đủ nguồn và trường hợp $\gamma=1$), so sánh với Monte Carlo, thực hành, kết mục.
- **Mục 5:** đoạn mở, trực giác 5.1, Ví dụ 05.21, đoạn trước và sau Thuật toán 05.32, sau Ví dụ 05.22, đoạn mở 5.3, đọc hình, thực hành, kết mục.
- **Phần sau Mục 5:** đoạn mở của mục Tình huống áp dụng và ứng dụng; Tóm tắt chương (đoạn kể chuyện còn bảy câu, danh sách Mục 2 và Mục 4 gọn hơn, đoạn giới hạn); lời giải Bài tập 05.13; đoạn đọc thêm `topic-23`; câu mở Bảng ký hiệu và Bản đồ chủ đề.

Không viết lại: các chứng minh (Mệnh đề 05.4, 05.7, 05.9, 05.11, 05.25, 05.27, 05.33, 05.34; Định lý 05.16, 05.17, 05.28; Hệ quả 05.26) và đoạn ý tưởng của Bổ đề 05.5 và Mệnh đề 05.34 khi $\gamma=1$.

### Bài tập chuyển thêm (quyết định 4)

Chuyển Bài tập 05.13 (lượt thứ ba $e_3$, mức tính toán, cùng cách tính với Ví dụ 05.5 và 05.9) sang danh sách cho `exercises.md`. Đây cũng là mục tùy chọn E06/05.32 của kế hoạch C. Bài tập 05.14 cũ (vận dụng) đổi số thành 05.13. Ghi chú còn Bài tập 05.1–05.13, và `exercises.md` bắt đầu từ Bài tập 05.14 (sửa dòng tương ứng ở mục "Sửa kế hoạch C" phía trên). Bảng ánh xạ mục tiêu ở đầu mục Bài tập củng cố đã cập nhật.

```markdown
::: exercise Bài tập 05.13
Dữ kiện: tàu đổ bộ thu nhỏ, $\gamma=1$, $\alpha=0{,}5$, giá trị chuẩn $v_\pi(\mathrm S)=11/21$, $v_\pi(\mathrm X)=19/21$. Sau hai lượt $e_1$, $e_2$, Monte Carlo lần ghé đầu tiên với bước hằng cho $(V(\mathrm S),V(\mathrm X))=(-0{,}25;\ -0{,}25)$, còn TD(0) cho $(-0{,}375;\ 0{,}375)$. Lượt thứ ba là $e_3:\mathrm S\to\mathrm X\to\mathrm G$ với phần thưởng $(0,1)$.

(a) Tiếp tục mỗi phương pháp trên $e_3$.
(b) Tính độ lệch của hai bảng so với giá trị chuẩn và so với Ví dụ 05.15.
:::

::: hint
Monte Carlo: hai lợi tức của $e_3$ đều bằng $1$. TD(0): chuyển thứ hai đọc bảng sau chuyển thứ nhất.
:::

::: solution
(a) Monte Carlo: $V(\mathrm S)=-0{,}25+0{,}5\cdot(1+0{,}25)=0{,}375$ và $V(\mathrm X)=0{,}375$ theo cùng phép tính.

TD(0), chuyển $\mathrm S\to\mathrm X$:

$$
\begin{aligned}
Y&=0+0{,}375=0{,}375,\\
\delta&=0{,}375-(-0{,}375)=0{,}75,\\
V(\mathrm S)&=-0{,}375+0{,}5\cdot0{,}75=0 .
\end{aligned}
$$

Chuyển $\mathrm X\to\mathrm G$:

$$
\begin{aligned}
Y&=1+0=1,\\
\delta&=1-0{,}375=0{,}625,\\
V(\mathrm X)&=0{,}375+0{,}5\cdot0{,}625=0{,}6875 .
\end{aligned}
$$

(b) Monte Carlo: $0{,}375-11/21=-25/168\approx-0{,}149$ tại $\mathrm S$; $0{,}375-19/21=-89/168\approx-0{,}530$ tại $\mathrm X$. TD(0): $0-11/21\approx-0{,}524$ tại $\mathrm S$; $0{,}6875-19/21=-73/336\approx-0{,}217$ tại $\mathrm X$. So với sau $e_2$, cả hai bảng gần giá trị chuẩn hơn ở cả hai trạng thái, và mỗi phương pháp vẫn gần hơn ở một trạng thái, như trong Ví dụ 05.15.

**Kiểm tra lại.** Ở TD(0), $V(\mathrm S)$ mới bằng $0$ vì $\delta=0{,}75$ nhân $\alpha=0{,}5$ bù đúng $-0{,}375$.
:::

```

### Số hiệu và phần toán đã đổi trong vòng này

- Số hiệu: chỉ Bài tập 05.14 → 05.13; bộ đếm chung (05.1–05.35) và Ví dụ (05.1–05.22) không đổi.
- Phần toán đã viết lại câu chữ, cần rà lại:
  - Nhận xét 05.18 (ô chờ), Nhận xét 05.19, Nhận xét 05.23 (chi phí), Nhận xét 05.29 (sai số bình phương trung bình);
  - dòng kiểm sau Mệnh đề 05.25;
  - đoạn ý tưởng chứng minh Định lý 05.30 và đoạn so sánh với Định lý 05.16, 05.17 ("Monte Carlo cần đúng $1/N(s)$, một lịch Robbins–Monro");
  - thực hành Mục 4.4 (hệ số $1-(1-\gamma)/n$);
  - ví dụ $\rho=0{,}84$ sau Bổ đề 05.5;
  - đoạn thực hành Mục 4.3 (3021 và 1627);
  - gạch Diễn giải của Tình huống 05.1.

### Kiểm tra

- `note_check.py`: 35 số hiệu chung, 22 ví dụ, 13 bài tập, liên tục, không trùng; không khối lạ, không khối chưa đánh số, không mẫu câu cấm.
- `check_note.py 05 lecture-05-du-doan-phi-mo-hinh.html`: 0 lỗi KaTeX, 110 khối, 0 lỗi console, không yêu cầu ra ngoài, `overflow` false ở 1600×900 và 390×844.

## Đợt sửa 2026-10-12 — Giai đoạn I, rà lại vòng 2

Hai tác tử rà soát chỉ đọc (Opus 5.5, effort high, theo điều phối viên): vai A (`recheck-05-A.md`, P-1…P-9) và vai B (`recheck-05-B.md`, N-1…N-17). Tác tử soạn sửa theo quyết định của điều phối viên, dùng `no-ai-slop` Edit và tự kiểm `eval.md` trên mọi đoạn đã sửa. Không commit.

### Số từ

Trước: 24 980. Sau: 25 291 (`wc -w`), dưới trần mới 25 300.

Lý do vượt 25 000: N-1 (nghiêm trọng) đưa lại hai bài tập vào Mục 3.2 và 4.1, khoảng +400 từ, để khôi phục bước 8 (bài tập ngay sau mục) và phủ mục tiêu 3–4. Phần bù gồm:
- N-7 (bỏ câu lặp bốn lần);
- rút hai đoạn "Trong thực hành" của Mục 4.3 và 4.4;
- bỏ câu thứ hai ở đoạn mở mục Tình huống áp dụng;
- rút lời giải các bài đưa về.

### Rà lại vòng 2

Cột "Dòng" ghi số dòng trong `lecture-note.md` sau vòng sửa này.

| Mã | Mức | Xử lý | Trạng thái | Dòng |
|---|---|---|---|---|
| P-1 / N-15(b) | trung bình | "Định lý 05.16, 05.17 được chứng minh cho $1/N(s)$, lịch tái tạo đúng trung bình mẫu; Định lý 05.30 cho TD(0) chấp nhận mọi lịch Robbins–Monro" | đã sửa | 1530 |
| P-2 / N-3 | trung bình | Tình huống 05.1: "Bảng dưới…", so $5157{,}9$ với $5086$ cùng cấu hình; Mục 4.4 thêm câu: $5086$ là trung bình qua năm thứ tự lượt, $5157{,}9$ là một thứ tự | đã sửa | 1806, 1533 |
| P-3 / N-4 | trung bình | Nhận xét 05.18 tách ba gạch; nêu $\mathbb E[N]=2$, $\mathbb E[N^2]=6$, $\frac1N\sum(N-k)=(N-1)/2$, giới hạn $\frac{(6-2)/2}{2}$ | đã sửa | 801–805 |
| P-4 | nhẹ | Nhận xét 05.19: "độc lập cùng phân phối" | đã sửa | 809 |
| P-5 | nhẹ | Ý tưởng Mệnh đề 05.34 khi $\gamma=1$: "sau khi bỏ các vòng lặp", "$\Phi^{\lvert\mathcal S_{\mathcal D}\rvert}$ là ánh xạ co" | đã sửa | 1742 |
| P-6 | nhẹ | Mệnh đề 05.34, Điều kiện áp dụng: khi $\gamma<1$ không cần giả thiết lượt kết thúc | đã sửa | 1714 |
| P-7 / N-11 | nhẹ | Tiên quyết: ánh xạ co có đúng một điểm bất động, phép lặp hội tụ về nó | đã sửa | 25 |
| P-8 | nhẹ | Đoạn mở mục Tình huống: "khi trạng thái không Markov và độ dài lượt bị chặn, xem Diễn giải"; ô bảng rút gọn | đã sửa | 1782, 1786 |
| P-9 | nhẹ | Ý tưởng Định lý 05.30: phương sai có điều kiện không vượt $A+B\lVert V_t\rVert_\infty^2$ | đã sửa | 1519 |
| N-1 | nghiêm trọng | (a) lượt $e_3$ về cuối Mục 4.1 (Bài tập 05.8); (c) câu (a) của bài tự chuyển cũ về cuối Mục 3.2 (Bài tập 05.7); (d) bài lịch Robbins–Monro lên cuối Mục 4.4 (Bài tập 05.11). Không làm (b) | đã sửa | 1052, 1137, 1535 |
| N-2 | trung bình | "Sau kỳ vọng (Mục 4.2), chúng ta xét dao động…" | đã sửa | 1321 |
| N-5 | trung bình | Tình huống 05.2: thêm "Xử lý đúng và giới hạn" | đã sửa | 1846 |
| N-6 | nhẹ | Bỏ vế lặp ở đoạn mở Mục 5 | đã sửa | 1563 |
| N-7 | nhẹ | Bỏ câu thứ hai ở đoạn mở mục Tình huống; rút ô bảng; giữ ở Diễn giải và Dẫn ngược | đã sửa | 1782, 1786 |
| N-8 | nhẹ | $n\to\lvert\mathcal S_{\mathcal D}\rvert$ | đã sửa | 1757 |
| N-9 | nhẹ | Thuật ngữ gốc dời về lần đầu: variance (dòng 3), TD error (48), transition sample (77), unbiased (84), on-policy (153); bỏ bản sau | đã sửa | 3, 48, 77, 84, 153 |
| N-10 | nhẹ | Mục tiêu 1: ", theo Mục 2.1" | đã sửa | 9 |
| N-12 | nhẹ | "tiền đề tuyệt đối của bài 4" | đã sửa | 2001 |
| N-13 | nhẹ | Nhận xét 05.23 hai câu; Nhận xét 05.31 hai gạch cho hai điều kiện bước học | đã sửa | 1046, 1524 |
| N-14 | nhẹ | Kết mục 5: khi trạng thái không Markov, không nghiệm nào được bảo đảm gần $v_\pi$ | đã sửa | 1777 |
| N-15(a) | nhẹ | Bỏ cấu trúc "không… mà…" ở đoạn đọc hình phương sai | đã sửa | 1388 |
| N-16 | nhẹ | "Chứng minh nằm ngoài phạm vi học phần", dẫn Bertsekas và Tsitsiklis (1996, chương 2). Chưa xác minh được mục cụ thể nên giữ mức chương | đã sửa | 310 |
| N-17 | nhẹ | "(Ví dụ 05.14, Mục 4.1)" | đã sửa | 104 |
| rút thực hành Mục 4.3, 4.4 | — | Bù độ dài theo quyết định | đã sửa | 1453, 1533 |
| A2-1 | nhẹ | Bài tập 05.8, lời giải (b): "So với sau $e_2$ (Ví dụ 05.15), cả hai bảng gần giá trị chuẩn hơn ở cả hai trạng thái; Monte Carlo vẫn gần hơn tại $\mathrm S$, TD(0) gần hơn tại $\mathrm X$." | đã sửa | 1171 |
| A2-2 | nhẹ | Tình huống 05.2: "chỉ học từ các lượt kết thúc trước điểm cắt, nên ước lượng có điều kiện trên sự kiện đó" | đã sửa | 1846 |

### Ánh xạ số hiệu bài tập vòng này

Cũ → mới:
- giữ số: 05.1, 05.2, 05.3, 05.4, 05.5, 05.6;
- 05.7 → 05.9; 05.8 → 05.10; 05.9 → 05.12; 05.10 → 05.13; 05.11 (Robbins–Monro, chuyển lên Mục 4.4) giữ 05.11; 05.12 → 05.14; 05.13 → 05.15;
- mới đưa về: Bài tập 05.7 (tự chuyển, Mục 3.2), Bài tập 05.8 (lượt $e_3$, Mục 4.1).

Ghi chú có Bài tập 05.1–05.15; `exercises.md` bắt đầu từ Bài tập 05.16. Bảng mục tiêu ↔ bài tập ở dòng 1917 đã cập nhật.

### Cập nhật danh sách chuyển cho exercises.md

- Bỏ khỏi danh sách: Bài tập $e_3$ (nay là Bài tập 05.8 của ghi chú) và câu (a) của bài tự chuyển cũ (nay là Bài tập 05.7). `exercises.md` không lặp hai đề này.
- Còn trong danh sách: 05.5, 05.6(b), 05.9, 05.11 cũ của vòng đầu; ô chờ cùng 05.7(c) cũ; câu (b) và (c) của bài tự chuyển cũ (lịch $1/n$, so với Monte Carlo).
- Kế hoạch C: mục tùy chọn E06/05.32 vẫn bỏ khỏi `exercises.md`, vì là Bài tập 05.8 của ghi chú.

### Kiểm tra

- `note_check.py`: 35 số hiệu chung, 22 ví dụ, 15 bài tập liên tục; không khối lạ, không mẫu câu cấm.
- `check_note.py 05 lecture-05-du-doan-phi-mo-hinh.html`: 0 lỗi KaTeX, 116 khối, 0 lỗi console, không yêu cầu ra ngoài, `overflow` false ở 1600×900 và 390×844.

## Đợt sửa 2026-10-12 — Giai đoạn II: bộ trang chiếu

### Tác tử

| Vai trò | Loại | Mô hình | Effort | Ghi file |
|---|---|---|---|---|
| Tác tử soạn sửa deck Bài 05 (giai đoạn II) | general-purpose (theo brief `brief_deck_writer.md` của điều phối viên) | claude-opus-5-5 | high | `lecture-05-du-doan-phi-mo-hinh.html`, `img/lec-05/{short-walk,long-walk,long-returns,learning-route,target-randomness}.svg`, xóa `img/lec-05/mc-td-timeline.svg`, `planning/lec-05/{outline,storyboard}.md` (viết lại), mục này |

Không commit, không push. Không sửa `lecture-note.md`, `lecture-slide.css`, `index.html`, `material-viewer.*`, notebook, mẫu, `AGENTS.md`, `CLAUDE.md` hay tệp của bài khác. Một lần lỡ chạy `git rm --cached` trên `mc-td-timeline.svg` đã được hoàn tác ngay bằng `git restore --staged`; chỉ mục git không chứa thay đổi nào của tác tử.

### Phạm vi và kết quả

- Deck dựng lại theo chuẩn 2026-10-12 và theo ghi chú bài giảng đã commit `e251162`: 45 → 70 trang, 5 → 6 mạch; năm trang tiêu đề mạch (`L05-B00`, `L05-C00`, `L05-D00`, `L05-DT`, `L05-E00`, `id="mach-2"`…`"mach-6"`); mạch mở đầu đủ bìa, "Tiên quyết và quy ước", "Mục tiêu học tập", "Nội dung", "Vấn đề trung tâm", "Khung chung của quy tắc cập nhật"; mạch kết luận đủ hai trang bảng tổng kết ba cột, bảng khung cập nhật, bảng điều kiện hội tụ, bài tập tổng hợp có lời giải, trang trả lời bài toán trung tâm có dòng "Nguồn:" và câu nối sang Bài 06, "Câu hỏi tự kiểm tra", "Bài tập về nhà và tài liệu đọc".
- Bỏ toàn bộ khối `<style>` cục bộ (thu chữ `.92em`, `.9em`, `.math-large` 1em, chỉnh lề). Còn sáu thuộc tính `style="max-height:…"` trên ảnh (bố cục, không đổi cỡ chữ).
- Số hiệu kết quả của ghi chú dẫn tối đa một lần mỗi trang, sau phát biểu bằng lời; các số còn lại nằm trong ghi chú diễn giả.
- Ví dụ xuyên suốt: tàu đổ bộ thu nhỏ trên dãy bốn ô với $e_1$, $e_2$, $e_3$; dãy bảy ô; tám lượt $\mathrm A$, $\mathrm B$; hai chuyển Lunar Lander của notebook. Tên ô chữ đứng, dấu thập phân phẩy, ngưỡng $\theta$, thuật ngữ theo `quyet-dinh-chuan-2026-10-12.md`.
- Bỏ liên kết PDF `../RL-hk2-2025-2026/...` trên L05-E03; nguồn ghi "Bài giảng gốc (2025–2026), trang N" và "Bài tập tuần 5 (2025–2026), bài k".
- Đồng bộ kế hoạch với commit `bc95338` (thứ tự D05 trước D03, bảng $\operatorname{Var}=320/441$): `outline.md`, `storyboard.md` viết lại theo deck mới; bỏ câu "không tạo notebook".

### Bảng mã trang cũ → mới

| Cũ | Mới | Quyết định |
|---|---|---|
| A01, A02, A03, A04 | A01, A02 (Nội dung), A03 (Vấn đề trung tâm), A04 (Tiên quyết và quy ước) | sửa |
| A05 | — | gộp (Bài tập 05.1 của ghi chú; ý chính vào ghi chú diễn giả B01) |
| — | A06, A07 | thêm |
| B01–B03, B05–B09 | cùng mã | sửa |
| B04 | B04, B04c | tách |
| B10 | B10, B10b | tách |
| B11 | — | gộp vào B09 |
| B12 | B12, B12c, B12d | tách |
| B13 | B13, B13b | sửa, thêm lời giải |
| — | B00, B09c | thêm |
| C01 | — | gộp vào C02 |
| C02–C04, C07, C08, C10 | cùng mã | sửa (C07 đặt trước C05) |
| C05 | C05, C05b | tách |
| C06 | C06, C06c | sửa, thêm |
| C09 | — | bỏ (ghi chú diễn giả C05, Nhận xét 05.23) |
| — | C00, C10b | thêm |
| D01–D04, D07, D08, D10, D11 | cùng mã | sửa |
| D05 | D05, D05b | tách |
| D06 | D06, D06b | tách |
| D09 | D09, D09b, D09c | tách |
| D12 | D12, D12b, D13, D13b | tách |
| — | D00, DT, D04b, D07a | thêm |
| E01, E04 | cùng mã | sửa |
| E02 | E02, E02b, E02c, E02d | tách |
| E03 | E03 | sửa, gộp E05 |
| E05 | — | gộp vào E03 |
| — | E00, E06, E06b | thêm |

Không có liên kết `#/N/M` hay `data-slide-id` nào từ học liệu khác trỏ vào deck Bài 05 (đã tìm trong `2627-1/`).

### Mật độ trước và sau (`density.py`)

| | Trang | Dòng `VƯỢT` | Trang > 40 âm tiết | Trang > 60 âm tiết | Trang > 90 âm tiết |
|---|---:|---:|---:|---:|---:|
| Trước | 45 | 36 | 33 | 22 | 5 |
| Sau | 70 | 8 (đều có ngoại lệ trong storyboard) | 56 | 3 (A06, E02b, E02d; trần 80) | 0 |

Tám dòng còn lại: L05-A06 (trang mục tiêu, 80), bốn trang tiêu đề mạch (dòng dẫn 21–22 âm tiết, quy định riêng ≤ 25), L05-E02b (66), L05-E02d (76), L05-E03 (7 dòng). Bảng từng trang trước/sau nằm trong `storyboard.md`, mục "Ngoại lệ mật độ". Đích 40 âm tiết chưa đạt ở 56 trang; trần 60 đạt ở mọi trang nội dung không thuộc diện trần 80.

### SVG

- `short-walk.svg`: dấu thập phân phẩy (`0,8`, `0,2`); tiêu đề "Tàu đổ bộ thu nhỏ trên dãy bốn ô"; mô tả nêu "rơi", "nằm yên".
- `long-walk.svg`: dấu thập phân phẩy; tiêu đề "Dãy bảy ô".
- `long-returns.svg`: dấu trừ `−1` thay gạch nối.
- `learning-route.svg`: nhãn "Lợi tức MC" thành hai dòng "Lợi tức / Monte Carlo" (bỏ viết tắt chưa giải thích).
- `target-randomness.svg`: "MC dùng đuôi đã xảy ra" thành "Monte Carlo dùng đuôi đã xảy ra".
- Xóa `mc-td-timeline.svg` (không dùng ở deck lẫn ghi chú; nhãn "S₁=x" lệch tên ô), theo quyết định chung mục 8. Bản sao nằm trong thư mục tạm của phiên.
- Deck dùng `short-walk`, `episode-one`, `episode-two`, `mc-td-targets`, `long-walk`, `long-returns`, `target-randomness`, `ab-empirical`, `learning-route`; `unfinished-episode.svg`, `design-grid.svg`, `variance-decomposition.svg` chỉ còn dùng trong ghi chú. Không xóa SVG nào mà ghi chú dùng. Không có ảnh raster.

### Sai lệch so với kế hoạch A và lý do

1. 70 trang thay vì khoảng 69; phân bổ 8/34/22/26/14/16 phút (kế hoạch 10/32/24/24/14/16) vì mạch 2 nhận thêm ví dụ tính tay Monte Carlo và ví dụ sai số.
2. B01 không tách thành B01/B01b: trực giác Monte Carlo là một dòng "Trực quan." trên B01; Định nghĩa 05.1 nằm ở dòng Ký hiệu/Giả thiết của A04 và ghi chú diễn giả.
3. B02 thành trang ví dụ hai hình lượt; B03 gộp Định nghĩa 05.3 với Mệnh đề 05.4 (bảng tính ngược vào ghi chú diễn giả), chỉ dẫn số hiệu trong ghi chú diễn giả.
4. B08 không tách B08/B08b: ví dụ bảng và Mệnh đề 05.11 cùng trang, dưới trần.
5. B11 gộp vào B09 (bảng bốn cấu hình có cột sau $e_2$, theo Ví dụ 05.5 của ghi chú); Nhận xét 05.12 là một dòng trên B09, `design-grid.svg` chỉ còn trong ghi chú.
6. Thêm B09c (Ví dụ 05.6, một lượt Monte Carlo lần ghé đầu tiên) để có bước tính tay trước giả mã đúng thứ tự Mục 2.5 của ghi chú.
7. B12 tách theo ghi chú: ví dụ sai số (Ví dụ 05.7), Định lý 05.16, Định lý 05.17; Nhận xét 05.19 (bước hằng) thành "Lưu ý:" trên B12d thay vì chuyển sang B08b.
8. C01 gộp vào C02 để giữ tổng số trang; `unfinished-episode.svg` không còn trên deck.
9. C06 dùng hai chuyển thật của Lunar Lander (Ví dụ 05.11) cho cả tự chuyển và trạng thái kết thúc; chuyển $\mathrm X\to\mathrm G$ đã có ở hàng cuối C07. Thêm C06c (Nhận xét 05.22).
10. C07 (TD(0) trên $e_1$) đặt trước C05 theo thứ tự Ví dụ 05.9 → Thuật toán 05.21 của ghi chú.
11. C09 bỏ thay vì giữ; nội dung chi phí nằm trong ghi chú diễn giả C05 và Nhận xét 05.23.
12. Thêm D04b (trực giác $Y^*$) và D07a (Ví dụ 05.19) để cụm phương sai và cụm hội tụ TD(0) có đủ bước; thêm D09c (Ví dụ 05.22, ngưỡng $\theta$).
13. D13 dùng ba nhận định có số liệu của ghi chú (bảng $V(\mathrm X)=10$, bước hằng $0{,}5$, lịch $n^{-0{,}6}$) thay cho đúng câu 2–4 của D12 cũ; câu "hai lượt không xếp hạng" nằm ở Diễn giải của D02.
14. D12 thêm câu (a) $V_3(\mathrm A)$ (Bài tập 05.12 của ghi chú).
15. E04 câu 4 hỏi hai lựa chọn của Monte Carlo (Nhận xét 05.12) thay cho câu về hai nghiệm theo lô, vì D12 (b) đã kiểm câu đó.
16. Dòng "Tài liệu đọc trước" của A02 nằm trong ghi chú diễn giả để trang giữ ≤ 6 dòng.
17. Câu nối sang Bài 06 đặt ở cuối L05-E01, không ở L05-E03, để E03 không vượt thêm dòng.

### Bài tập trên deck và tệp bài tập

L05-E03 ghi số hiệu dự kiến của `exercises.md` theo danh sách "chuyển cho exercises.md" ở các mục trên: mạch 2 → 05.16–05.18 (Bài tập 05.5 cũ trùng B13, 05.6(b) cũ, ô chờ); mạch 3 → 05.19–05.21 (Bài tập 05.9 cũ trùng C10, 05.11 cũ theo bài 7 tuần 5, tự chuyển (b)(c)); mạch 4 → 05.22–05.24 (bài 6, bài chứng minh phương sai, bài 4 của tuần 5); mạch 5 → 05.25–05.26 (ba lượt theo lô, bài lập trình). Giai đoạn III phải đối chiếu lại số hiệu, sửa cột phải của L05-E03 và thay "Bài tập: chưa có" bằng liên kết viewer. Lời giải trên B13b và C10b là lời giải chuẩn cho hai bài trùng.

### Đề nghị sửa ghi chú

- Mô tả thay thế của `learning-route.svg` trong ghi chú (dòng 110) ghi "Lợi tức MC"; hình nay ghi "Lợi tức / Monte Carlo". Đề nghị đổi alt thành "Lợi tức Monte Carlo" ở đợt sửa ghi chú sau. Không phát hiện mâu thuẫn số liệu nào giữa deck và ghi chú.

### Đề nghị cho `lecture-slide.css`

- Thêm một lớp chung cho hình thấp, ví dụ `.figure.compact { max-height: 150px; }`, để thay sáu thuộc tính `style="max-height:…"` trên ảnh của deck (B02, B06, C02, D04, D11). Không sửa CSS trong đợt này.

### Ngoài phạm vi, đề nghị điều phối viên

- `planning/lec-05/analysis.md` cần dòng đầu "Hồ sơ lịch sử trước đợt sửa 2026-10-12; không còn phản ánh deck hiện tại." theo quyết định chung mục 5; tệp không thuộc phạm vi ghi của brief.

### Số liệu đã tính lại

$v_\pi=(11/21;\ 19/21)$; $\operatorname{Var}(G_0\mid\mathrm S)=320/441$, độ lệch chuẩn $0{,}852/\sqrt n$ ($0{,}602$, $0{,}085$); bốn cấu hình Monte Carlo trên $e_1$, $e_2$; TD(0) trên $e_1$, $e_2$, $e_3$; độ lệch $(-0{,}774;\ -1{,}155)$, $(-0{,}899;\ -0{,}530)$ sau $e_2$ và $(-0{,}149;\ -0{,}530)$, $(-0{,}524;\ -0{,}217)$ sau $e_3$; độ chệch $-34/105$; $V(\mathrm X)=10$: phương sai $19{,}36$, độ chệch $\approx7{,}28$; phương sai giới hạn $0{,}5\cdot(320/441)/1{,}5\approx0{,}242$; Lunar Lander $44{,}3715$, $0{,}5215$, $43{,}90$ và $36{,}48$, $67{,}17$; lượt quét: $V_2(\mathrm A)=3/32$, $V_3(\mathrm A)=45/256$, thay đổi $0{,}0111$ ($k=17$) và $0{,}0097$ ($k=18$), $V_{19}(\mathrm A)\approx0{,}682$; ba lịch bước học. Mọi số khớp ghi chú bài giảng.

### Tự kiểm `no-ai-slop` (Edit) và `quill`

- Phạm vi: mặt trang và ghi chú diễn giả của cả 70 trang, tiêu đề, alt text. Đã đọc `SKILL.md`, soạn ở chế độ Edit rồi đối chiếu `eval.md`. Đạt: không từ cấm, không câu hỏi tu từ (dấu hỏi chỉ ở bốn câu tự kiểm tra có nhãn "Câu hỏi:"), không lời giảng viên, không "chúng ta", "ta thấy", "rõ ràng", "hãy", "Trang này"; không kết luận kịch tính hay chuỗi mũi tên; không gạch dài trang trí. Đã sửa trong lúc tự kiểm: viết tắt "MC" trên hai hình và alt; câu "đó là dao động, không phải độ chệch" (đối lập nhị phân) thành câu khẳng định; dấu chấm đứng một mình sau công thức trên D03. Giữ có chủ đích: nhãn "Lưu ý:" lặp ở trang thuật toán và trang kết quả vì có chức năng tách phạm vi; "không phải $v_\pi(\mathrm S)$" ở B05 vì nêu nhầm lẫn thường gặp.
- `quill` (Outline, Threads, Concept, Revise làm bảng kiểm; không tạo `quill.json`): mười một cụm trong `storyboard.md` có đủ sáu bước hoặc ghi rõ bước gộp; ba thuật toán có tính tay trước giả mã (B09c → B10; C03, C07 → C05; D09 → D09b). Sợi chỉ "lượt bị cắt ngắn" đi qua B03, B10b, C05b, C06c, E04; sợi "bảng cố định khi lấy kỳ vọng" qua D05, D05b, E02b; sợi "giả thiết Markov" qua A04, B04c, D06b, D07, E01. Thuật ngữ thống nhất với bảng Việt–Anh của `outline.md`.

### Kiểm trình duyệt

- Script Playwright Chromium duyệt cả 70 trang (`Reveal.slide(h,v,99)`), ở 1600×900 và 390×844, trên máy chủ tĩnh `http.server` cổng 8799 (gốc kho) để tránh tải lại tự động của `reloadserver` trong lúc chụp; cùng kết quả trên cổng 8766: 0 lỗi console và lỗi trang, 0 `.katex-error`, 0 yêu cầu ra ngoài máy cục bộ, 0 phản hồi lỗi, không cuộn ngang, không phần tử nào vượt khung 1280×720 hay sát chân trang (ngưỡng 28 px), số trên năm trang tiêu đề mạch khớp `#/2`…`#/6`; phím mũi tên chuyển trang.
- Đã xem ảnh chụp: năm trang tiêu đề mạch, A01, A03, A06, B01, B04, B12c, C02, C06, D03, D04b, D07, E02, E02b, E02d, E03 ở 1600×900; L05-DT, L05-E02d ở 390×844 (chế độ cuộn của RevealJS).
- `git diff --check` sạch trên deck, SVG và planning.

## Rà soát năm vai và biên tập (giai đoạn II)

### Tác tử

| Vai trò | Loại | Mô hình | Effort | Ghi file |
|---|---|---|---|---|
| Rà soát sinh viên (SV), chuyên gia Học tăng cường (RL), toán và thuật toán (TOAN), phản biện sư phạm + `no-ai-slop` Detect (PB), kết nối và mạch (MACH) | general-purpose, chỉ đọc (theo `brief_deck_reviewers.md`; mô hình và mức do điều phối viên ghi theo lệnh gọi) | claude-opus-5-5 | high | không |
| Biên tập viên deck Bài 05 (tiếp quản tác tử soạn đã dừng; một lần bị ngắt giữa chừng rồi tiếp tục cùng phạm vi) | general-purpose (theo `brief_deck_writer.md`, `brief_deck_editor.md`) | claude-opus-5-5 | high | `lecture-05-du-doan-phi-mo-hinh.html`, `img/lec-05/mc-td-targets.svg`, `outline.md`, `storyboard.md`, mục này |

Không commit. Không sửa `lecture-note.md`, `lecture-slide.css`, `index.html`, notebook hay tệp của bài khác. Kết quả rà: 0 chặn bàn giao; 1 nghiêm trọng (TOAN); nhiều trung bình trùng nhau giữa các vai.

### Bảng phát hiện và xử lý

Mã theo vai và số thứ tự trong báo cáo (`deckrev-05-{SV,RL,TOAN,PB,MACH}.md`). Trạng thái: đã sửa, sửa một phần, từ chối (kèm lý do).

| Mã | Trang | Mức | Trạng thái và cách sửa |
|---|---|---|---|
| TOAN-1 | B10b (B10) | nghiêm trọng | Đã sửa: đánh số bước như Thuật toán 05.13; bước 5 gói tăng $N(s)$, phép cập nhật và thêm $s$ vào $\mathcal H$ trong cùng điều kiện; ghi chú diễn giả nêu trường hợp lần ghé thứ hai tại $\mathrm S$ của $e_2$ |
| TOAN-2 | D11, D09b | trung bình | Đã sửa: D11 tách "Ký hiệu:" và "Giả thiết: $0<\alpha N(s)\le1$; mọi lượt của $\mathcal D$ kết thúc hoặc $\gamma<1$"; D09b "tập cố định $\mathcal D$ các lượt đã kết thúc", "(mọi lần ghé)" |
| TOAN-3 | E02d | trung bình | Đã sửa: dòng chung "Markov, dữ liệu theo $\pi$, phần thưởng bị chặn"; Monte Carlo "lượt độc lập cùng phân phối, kết thúc; ghé $s$ với xác suất dương; $1/N(s)$ → về $v_\pi(s)$ hầu chắc chắn"; TD(0) "$\gamma<1$ hoặc lượt kết thúc; mỗi $s$ vô hạn lần; Robbins–Monro"; TD theo lô "mọi lượt kết thúc hoặc $\gamma<1$; $0<\alpha N(s)\le1$ (đủ)". Hai hàng Monte Carlo $1/N(s)$ gộp làm một để giữ trần 80; "không chệch / có thể chệch" chuyển vào ghi chú diễn giả |
| TOAN-4 | B12c | nhẹ | Đã sửa: "lượt độc lập cùng phân phối, kết thúc hầu chắc chắn"; "phần thưởng bị chặn"; nhãn Định nghĩa/Định lý; cùng chỉ số $n$ |
| TOAN-5 | B04c | nhẹ | Đã sửa: Giả thiết thêm "$\mathcal S$ hữu hạn", "phần thưởng bị chặn"; dòng chứng minh (có $H_t$) chuyển vào ghi chú diễn giả, nơi $H_t$ được định nghĩa |
| TOAN-6 | B12d | nhẹ | Đã sửa: "với mẫu độc lập cùng phân phối, phương sai $\sigma^2$" trước công thức $\operatorname{Var}(V_n)\to\alpha\sigma^2/(2-\alpha)$ |
| TOAN-7 | D05b | nhẹ | Đã sửa: "Lưu ý: mục tiêu Monte Carlo không chệch khi trạng thái Markov và $\pi$ cố định" |
| TOAN-8 | C05b | nhẹ | Đã sửa: bước 6 "mở lượt mới, gán $S$ bằng trạng thái đầu" |
| TOAN-9 | E06b | nhẹ | Đã sửa: "$0{,}375-(-0{,}375)=0{,}75$" |
| TOAN-10 | B08 | nhẹ | Đã sửa: cột "Mẫu lần ghé đầu tiên tại $\mathrm X$" |
| TOAN-11 | D07 | nhẹ | Đã sửa: $\alpha_n(s)\in[0,1]$ trong công thức hiển thị |
| TOAN-12 | E04 (ghi chú) | nhẹ | Đã sửa: "(Hệ quả 05.26)" |
| TOAN-13 | B05, B07, B12d, C04, D05b, D06b, D10 (+ B10, C05) | nhẹ | Đã sửa: số hiệu đặt sau phát biểu (dòng tiếp sau công thức, dòng Kết luận/Ý nghĩa, hoặc cuối bước cuối của thuật toán) |
| TOAN-14 | C06c (ghi chú) | nhẹ | Đã sửa: "bước của TD(0) trong notebook" |
| SV-1 | C08 | trung bình | Đã sửa: dòng dữ kiện rút gọn, Diễn giải vào ghi chú diễn giả, ô có phép tính và cột Chuyển gói trong ngoặc nhọn KaTeX để không ngắt dòng; đo lại: nội dung y 116–604 trên 720 |
| SV-2 | A03, C02, D11 (B02, D04) | trung bình | Đã sửa: A03 bỏ hình; vẽ lại `mc-td-targets.svg` (nhãn 30–36 đơn vị, viewBox 1110×360, hiển thị 250 px, nhãn khoảng 0,7em); D11 hình 140 → 190 px; D04 230 → 255 px; B02 giữ (nhãn khoảng 0,64em, đo trên ảnh) |
| SV-3 | B04c, B12d, E02d, A03 | trung bình | Đã sửa: $H_t$ chỉ còn trong ghi chú diễn giả và được định nghĩa; $\sigma^2$ định nghĩa ở B12d; A03 "bước học giảm dần"; B12d "Giả thiết như lần ghé đầu tiên, dùng mọi lần ghé" |
| SV-4 | D03, D06, B01 | trung bình | Đã sửa: B01 "Tàu đổ bộ thu nhỏ (còn gọi là dãy bốn ô)"; D03 "kéo dài thành bảy ô"; D06 cột "Tàu đổ bộ thu nhỏ (bốn ô)" |
| SV-5 | B10/B10b, C05/C05b | trung bình | Đã sửa: bước con thụt lề bằng `style="margin-left"` trên danh sách con (danh sách lồng nhau trong CSS chung thu chữ còn 0,72em nên không dùng); trang hai mở bằng "Trong vòng lặp của bước 1:"; "Giả thiết:" lên trang đầu |
| SV-6 | D09b, D10 | trung bình | Đã sửa: chỉ số $j$ cho mẫu chuyển trong $\mathcal D$; ghi chú diễn giả phân biệt với $i$ của mạch 2 |
| SV-7 | C06 | trung bình | Đã sửa: Nhu cầu và dòng "trạng thái gộp thành $9216$ ô" |
| SV-8 | E03 | trung bình | Đã sửa: bảng `Mạch \| Bài tập` (hai cặp cột) với số hiệu của ghi chú; "Tệp bài tập: chưa có" |
| SV-9 | toàn deck | trung bình | Đã sửa: `scrollActivationWidth:null` |
| SV-10 | C03 | nhẹ | Đã sửa: khuôn bảng TD cố định, nhãn tiếng Việt ngoài KaTeX; console 0 cảnh báo |
| SV-11 | B12d | nhẹ | Đã sửa: "hầu chắc chắn" ngoài công thức |
| SV-12 | D09c, D13, D06b, B01, E02, C10b, E06b | nhẹ | Đã sửa: dấu chấm mồ côi (D09c, D13) và ngắt "$\gamma=$ / $0{,}99$" (D03, C06) bằng ngoặc nhọn KaTeX; ô bảng C10b, E06b để ngắt sau dấu bằng vì bảng không được rộng hơn khung |
| SV-13 | E06b | nhẹ | Đã sửa (như TOAN-9) |
| SV-14 | B12c | nhẹ | Đã sửa (như TOAN-4) |
| SV-15 | B01 | nhẹ | Đã sửa: "(mô hình chỉ để kiểm tra)", "xuất phát ở $\mathrm S$" |
| SV-16 | D05 | nhẹ | Đã sửa: dòng "Hiệu với giá trị chuẩn: …" thay công thức hiển thị không nhãn; thêm dấu chấm |
| SV-17 | D07a | nhẹ | Đã sửa: "Nhu cầu: với bảng sau nhiều bước, chọn lịch bước học vừa tới đích vừa tắt nhiễu" |
| SV-18 | E02/E02b | nhẹ | Đã sửa: tiêu đề "Kết quả và giả thiết không được bỏ" |
| SV-19 | E06 | nhẹ | Đã sửa: (a), (b) trong cùng một khung "Câu hỏi:" |
| SV-20 | ghi chú B01, B12c, D07, E01 | nhẹ | Đã sửa: rút từng ghi chú |
| SV-21 | các trang sát nút điều hướng | nhẹ | Sửa một phần: đo lại sau sửa, không trang nào vượt 720; C02 từ y=4 xuống 19, D03 từ 0 xuống 19, D04 từ 4 xuống 16. Còn D11 (y=5), B07 (9), D09c (11) có tiêu đề không chạm mũi tên lên trên ảnh |
| SV-22 | thời lượng | nhẹ | Từ chối phần "rút E02b/E02d về chỉ còn tên giả thiết": trái quyết định 7 và TOAN-3 (giả thiết đủ trên bảng). Thêm B04c vào danh sách có thể bỏ khi thiếu giờ; khối 30 phút ghi trong storyboard |
| RL-1 | B12d, D07, E01 (ghi chú) | trung bình | Đã sửa: định nghĩa $J$ ở ghi chú B12d; ghi chú E01 nêu $J$ nhỏ nhất tại lợi tức kỳ vọng theo ô nên nghiêng về Monte Carlo, ô gộp không Markov |
| RL-2 | B08 | trung bình | Đã sửa: "Nhu cầu: theo kịp môi trường thay đổi; …" |
| RL-3 | E02b, E02d | trung bình | Đã sửa (như TOAN-3; E02b thêm "$\gamma<1$ hoặc lượt kết thúc") |
| RL-4 | E01, D06b | trung bình | Đã sửa: ghi chú diễn giả D06b nêu có điều kiện tốc độ học (chưa có chứng minh; thực nghiệm thường cho TD nhanh hơn Monte Carlo bước hằng, Sutton và Barto §6.2, tr. 124–125) và độ nhạy với khởi tạo (bài giảng gốc tr. 28, 33). Không đặt trên mặt E01 vì trang đã ở trần |
| RL-5 | B12c, E02, E02d | nhẹ | Đã sửa: "cùng phân phối" |
| RL-6 | D05b | nhẹ | Đã sửa (như TOAN-7) |
| RL-7 | B12d | nhẹ | Đã sửa (như TOAN-6) |
| RL-8 | A07 | nhẹ | Đã sửa: "TD một bước, ký hiệu TD(0)" |
| RL-9 | toàn deck | nhẹ | Đã sửa: batch updating (A07), incremental mean (B07), terminal state (A04), stochastic approximation (ghi chú D07), step-size schedule (B10); bảng thuật ngữ trong `outline.md` |
| RL-10 | DT, D11, ghi chú E01 | nhẹ | Đã sửa: "quá trình phần thưởng Markov thực nghiệm"; ghi chú D11 nhắc Bài 03 |
| RL-11 | A03 | nhẹ | Đã sửa: bỏ hình, bỏ câu đọc hình trong ghi chú |
| RL-12 | D09b | nhẹ | Đã sửa (như TOAN-2) |
| RL-13 | C06 (ghi chú) | nhẹ | Đã sửa: "ngắn so với kích thước một ô gộp" |
| RL-14 | A07 (ghi chú) | nhẹ | Đã sửa: một câu gradient ngẫu nhiên, nối bán gradient Bài 07, dẫn §9.3 |
| RL-15 | thời lượng | nhẹ | Đã sửa: thêm B04c vào danh sách tự đọc |
| RL-16 | E06b | nhẹ | Đã sửa (như TOAN-9) |
| RL-17 | C06 | nhẹ | Đã sửa: khuôn bảng TD cố định; giá trị cũ nằm trong cột sai số TD |
| RL-18 | D11 | nhẹ | Đã sửa (như TOAN-2) |
| MACH-1 | A03 | trung bình | Đã sửa: chọn phương án bỏ hình (ít chữ hơn, danh sách 2–6 là bản đồ duy nhất); `learning-route.svg` giữ nguyên cho ghi chú bài giảng |
| MACH-2 | A03, E01 | trung bình | Đã sửa: A03 dòng 4 có vế "bỏ dao động đuôi"; E01 năm dòng 2–6 song song A03, dòng 4 có $-0{,}324$, dòng 5 nêu hai nghiệm $0$ và $3/4$ |
| MACH-3 | C02 → C03 | trung bình | Đã sửa: Nhu cầu ở chuyển đầu của $e_2$; C03 ghi "bảng sau $e_1$", ghi chú diễn giả chỉ nguồn của bảng |
| MACH-4 | B12, B01 | trung bình | Đã sửa: B12 "(giải từ mô hình, chỉ để đo sai số)"; ghi chú B01 "đo sai số ở mạch 2 và so hai bảng ở mạch 4"; D02 "Nhắc lại: giá trị chuẩn giải từ Bellman kỳ vọng …" |
| MACH-5 | B13, B13b | trung bình | Đã sửa: dữ kiện mới tại $\mathrm S$ với $\gamma=0{,}9$; lời giải $-0{,}0405$, $-0{,}04525$, $-0{,}22275$ (tính lại, kiểm bằng tổng trọng số $0{,}25\cdot0+0{,}25\cdot0{,}729+0{,}5\cdot(-0{,}81)$) |
| MACH-6 | C06 | trung bình | Đã sửa (như SV-7) |
| MACH-7 | D06, D03, B01 | trung bình | Đã sửa (như SV-4) |
| MACH-8 | E03 | trung bình | Đã sửa (như SV-8); Bài tập 05.1 ở hàng mạch 1; mạch 5 và 6 tách |
| MACH-9 | D05b → D03 | nhẹ | Đã sửa: Nhu cầu D03 nêu mục tiêu Monte Carlo chứa mọi chuyển còn lại |
| MACH-10 | D06b → D07a | nhẹ | Đã sửa: Nhu cầu D07a "với bảng sau nhiều bước" |
| MACH-11 | DT, D08 | nhẹ | Đã sửa: ghi chú DT nêu các lượt Lunar Lander đã thu trong bài thực hành |
| MACH-12 | ghi chú D02, B04, B05, C05b | nhẹ | Đã sửa: gọi theo đối tượng |
| MACH-13 | A07 | nhẹ | Đã sửa: bốn dòng |
| MACH-14 | E00/E02 | nhẹ | Đã sửa (như SV-18) |
| MACH-15 | DT, D11, ghi chú E01 | nhẹ | Đã sửa (như RL-10) |
| MACH-16 | D00 (ghi chú) | nhẹ | Đã sửa: rút còn khoảng 85 âm tiết |
| MACH ngoài vai | E04 câu 1; B12c | nhẹ | Đã sửa: "vì giới hạn số bước"; nhãn "Định nghĩa." |
| PB-1 | B13 | trung bình | Đã sửa (như MACH-5) |
| PB-2 | D07a | trung bình | Đã sửa: Nhu cầu mới; Diễn giải phương sai giới hạn của bước hằng; hàng "$\alpha$ hằng" của bảng chuyển vào Diễn giải để giữ 6 dòng |
| PB-3 | D03 → D04b | trung bình | Đã sửa: D04b thêm dòng "Mục tiêu TD đọc bảng đang sai; để tách dao động khỏi độ chệch, thay bảng bằng $v_\pi$" |
| PB-4 | D07 | trung bình | Đã sửa: "Trực quan. $v_\pi$ là điểm bất động của $T_\pi$ (Bài 04); trung bình mỗi bước TD(0) đi theo $T_\pi V-V$" |
| PB-5 | B12 | trung bình | Đã sửa (như MACH-4) |
| PB-6 | C06 và ghi chú có $J$ | trung bình | Đã sửa (như SV-7, RL-1) |
| PB-7 | B12d, B04c | trung bình | Đã sửa (như SV-3) |
| PB-8 | D05b | trung bình | Đã sửa (như TOAN-7). Số hiệu "(Mệnh đề 05.7)" do điều phối viên đề xuất không đặt trên mặt trang vì D05b đã mang "(Mệnh đề 05.25)" (tối đa một số hiệu mỗi trang); tên mệnh đề kỳ vọng sau lần ghé nằm trong ghi chú diễn giả |
| PB-9 | E02, E02b, E02d | trung bình | Đã sửa (như TOAN-3, RL-3) |
| PB-10 | B08 | trung bình | Đã sửa (như RL-2) |
| PB-11 | D11 | trung bình | Đã sửa (như TOAN-2) |
| PB-12 | trang ví dụ | trung bình | Sửa một phần: thêm "Tính …" ở B09c, B12, C03, C07, C08, D01, D05, D06, D09 và Diễn giải ở C06, D07a. B09, B09c, D03 không thêm Diễn giải vì trang đã đủ 6 dòng; C07 và C08 được thêm Diễn giải ở vòng rà lại 2 (lý do cũ "đủ 6 dòng" không đúng với hai trang này, xem MACH-N1) |
| PB-13 | E03, ghi chú B13 | trung bình | Đã sửa: bỏ cột dự kiến; bỏ câu "sẽ có trong tệp bài tập"; ghi chú E03 không mô tả tệp chưa có |
| PB-14 | ghi chú B04, B05, B08, B12c, B13, C03, C05b, D02, D03, D06b | trung bình | Đã sửa: bỏ chỉ đường theo vị trí, gọi tên đối tượng |
| PB-15 | ghi chú C00, D00, E00, A02, A01, E02, E02b (và B00, DT) | nhẹ | Đã sửa: mở bằng đối tượng hoặc kết quả kế thừa |
| PB-16 | A06 (ghi chú) | nhẹ | Đã sửa: thêm câu về sản phẩm kiểm tra |
| PB-17 | ghi chú B08, B10b, C07 | nhẹ | Đã sửa |
| PB-18 | B06 (ghi chú) | nhẹ | Đã sửa: "mẫu mới nhỏ hơn trung bình cũ thì trung bình giảm" |
| PB-19 | D02 và các trang dùng "độ lệch"/"sai số thật" | nhẹ | Sửa một phần: D02 ghi quy ước "độ lệch $V-v_\pi$" ở tiêu đề cột, E06 dùng cùng cụm. C04 giữ "sai số thật $v_\pi-V$" như ghi chú bài giảng; đề nghị thống nhất ở ghi chú (dưới đây) |
| PB-20 | D13b, D13 | nhẹ | Đã sửa: "Nhận định (a), (b) sai vì…"; (c) có ngoặc kép |
| PB-21 | D06, D08 | nhẹ | Đã sửa: "Tàu đổ bộ thu nhỏ (bốn ô)"; D08 "tám lượt $\mathrm A$, $\mathrm B$" |
| PB-22 | DT, D11, ghi chú E01 | nhẹ | Đã sửa (như RL-10) |
| PB-23 | B10, C05, B10b, C05b, C06c | nhẹ | Đã sửa (như SV-5, TOAN-13); C06c bỏ nhãn lặp |
| PB-24 | C05 | nhẹ | Đã sửa: ghi chú diễn giả nêu quy ước $S$ nghiêng là biến, $\mathrm S$ đứng là tên ô |
| PB-25 | A03, E01 | nhẹ | Đã sửa (như MACH-2) |
| PB-26 | C10 | nhẹ | Từ chối: đổi dòng 2 sang $\mathrm X\to\mathrm G$ phá khuôn cột "$V(\mathrm S)$ sau bước"; dòng $\mathrm S\to\mathrm L$ giữ chức năng kiểm trạng thái kết thúc khi xuất phát từ cùng bảng |
| PB-27 | các cụm hội tụ, độ chệch | nhẹ | Sửa một phần: cụm độ chệch có bước ứng dụng trên mặt D07 (điểm bất động $T_\pi$); các cụm khác giữ ứng dụng trong ghi chú diễn giả vì trang ở trần |
| PB-28 | E00 | nhẹ | Đã sửa: "Giả thiết không được bỏ · Lựa chọn phương pháp · Điều khiển phi mô hình" |

### Trang đã đổi trong vòng này

A01 (ghi chú), A02 (ghi chú), A03, A04, A06 (ghi chú), A07, B00 (ghi chú), B01, B04 (ghi chú), B04c, B05, B06 (ghi chú), B07, B08, B09c, B10, B10b, B12, B12c, B12d, B13, B13b, C00 (ghi chú), C02, C03, C04, C07, C05, C05b, C08, C06, C06c, C10b (ô bảng), D00 (ghi chú), D01, D02, D05, D05b, D03, D04 (cỡ hình), D04b, D06, D06b, D07a, D07, D13, D13b, DT, D08, D09, D09b, D09c, D10, D11, E00, E02, E02b, E02d, E06, E06b, E01, E04, E03; cấu hình `scrollActivationWidth:null`. Không thêm, bỏ hay dời trang; vẫn 70 trang, 6 mạch.

### SVG

- Vẽ lại `mc-td-targets.svg`: cùng hai hàng, cùng nhãn và chiều mũi tên; chữ 30–36 đơn vị thay 22–31, viewBox 1110×360, hộp "Giá trị ước lượng / ở trạng thái sau" hai dòng; mô tả `desc` giữ nguyên nên alt của ghi chú bài giảng vẫn đúng.
- `learning-route.svg` không còn trên deck; tệp giữ nguyên cho ghi chú bài giảng.

### Đề nghị cho `lecture-slide.css`

- Thêm lớp chung cho bước con của giả mã, ví dụ `.reveal.lecture-deck ol.substeps { margin-left: 2em; }` và `ol.substeps2 { margin-left: 4em; }`, để thay bốn thuộc tính `style="margin-left:…"` trên B10, B10b, C05, C05b. Danh sách lồng nhau không dùng được vì quy tắc `ol ol { font-size: .9em }` cho chữ 0,72em.
- Lớp `.figure.compact` như đề nghị ở mục trước, thay các `style="max-height:…"` trên ảnh.

### Đề nghị sửa ghi chú (sau giai đoạn II)

| Vị trí trong ghi chú | Nội dung sửa | Nguồn |
|---|---|---|
| Mục 1, dòng 110 (alt và đoạn đọc hình `learning-route.svg`) | Alt ghi "Lợi tức MC"; hình nay ghi "Lợi tức / Monte Carlo". Đổi alt thành "Lợi tức Monte Carlo". Deck không còn dùng hình này | tác tử soạn, MACH-1, RL-11 |
| Mục 4.4 hoặc Nhận xét 05.35 | Thêm câu có điều kiện về tốc độ học (chưa có chứng minh; thực nghiệm thường cho TD nhanh hơn Monte Carlo bước hằng trên bài toán ngẫu nhiên, Sutton và Barto 2018, §6.2, tr. 124–125) và về độ nhạy với khởi tạo | RL-4 |
| Ví dụ 05.11 và Tình huống (dòng khoảng 1025, 1822) | "mỗi bước mô phỏng dài 0,02 giây, nên 70%…" thành "…ngắn so với kích thước một ô gộp, nên…" | RL-13 |
| Dòng khoảng 1821, 1938 | Thống nhất "quá trình phần thưởng Markov thực nghiệm" | RL-10 |
| Mục 1.2 (tùy chọn) | Một câu nối quy tắc cập nhật với bước gradient ngẫu nhiên, cầu sang bán gradient ở Bài 07 | RL-14 |
| Mục 5, đoạn mở | Một căn cứ cụ thể cho dữ liệu cố định (bài thực hành quét lại các lượt đã thu) | MACH-11 |
| Mục 3.1 (khoảng dòng 904) và Ví dụ 05.15 | Thống nhất tên và dấu: "sai số thật $v_\pi-V$" và "độ lệch $V-v_\pi$" | PB-19 |
| Mục 2.6, Ví dụ 05.7 | Nêu rằng giá trị chuẩn $11/21$ giải từ mô hình chỉ để đo sai số, dùng ở cả Mục 2.6 và Mục 4 | PB-5 |

Lệch tạm thời deck–ghi chú: B13/B13b dùng dữ kiện mới ($\gamma=0{,}9$ tại $\mathrm S$), không có bài tương ứng trong ghi chú; mọi số liệu khác khớp ghi chú.

### Số dự kiến của `exercises.md` (cho giai đoạn III)

Danh sách cũ (mạch 2 → 05.16–05.18; mạch 3 → 05.19–05.21; mạch 4 → 05.22–05.24; mạch 5 → 05.25–05.26) giữ làm dự kiến, chỉ ghi ở đây. Bài trùng trang chiếu nay là B13/B13b (dữ kiện $\gamma=0{,}9$, thay Bài tập 05.5 cũ tại $\mathrm X$) và C10/C10b. Giai đoạn III thay dòng "Tệp bài tập: chưa có" trên L05-E03 bằng liên kết viewer.

### Tự kiểm `no-ai-slop` (Edit) và `quill`

- Phạm vi: mặt trang và ghi chú diễn giả của mọi trang đổi trong vòng này. Soạn ở chế độ Edit, đối chiếu `eval.md`. Quét toàn deck: 0 "chúng ta", "ta thấy", "rõ ràng", "hãy", "Trang này", "Mạch này", "Bài này", "trang trước/sau", "ở trên"; dấu hỏi chỉ ở bốn câu có nhãn "Câu hỏi:" của E04; 0 chữ Việt có dấu trong `\text{}`. Đã sửa: dấu hai chấm "tiết lộ" và câu mệnh lệnh trong ghi chú B08, B10b; siêu bình luận "Khuôn bảng này được giữ…" ở C07.
- `quill` (Outline, Threads, Concept, Revise làm bảng kiểm; không tạo `quill.json`): sợi "giá trị chuẩn" có một điểm vào (B12, giải từ mô hình) và "Nhắc lại:" ở D02; sợi tên ví dụ "tàu đổ bộ thu nhỏ (bốn ô)" → "kéo dài thành bảy ô"; sợi "bảng TD sau $e_1$" đi C07 → C03 (ghi chú) → C08 → D05; A03 và E01 song song từng dòng 2–6.

### Kiểm sau sửa

- `density.py`: mười dòng `<-- VƯỢT`, đều có ngoại lệ trong `storyboard.md` (A06, bốn trang tiêu đề mạch, E02, E02b, E02d, E01); mọi trang nội dung khác ≤ 60 âm tiết, ≤ 6 dòng, ≤ 20 âm tiết mỗi dòng.
- `deck_check.py` (cổng 8799, gốc kho), 1600×900 và 390×844: 70 trang, 0 lỗi và 0 cảnh báo console (gồm KaTeX), 0 `.katex-error`, 0 yêu cầu ra ngoài máy cục bộ, 0 yêu cầu lỗi, không cuộn ngang; năm trang tiêu đề mạch B00, C00, D00, DT, E00. Ở 390×844 deck không còn chế độ cuộn.
- Đo khung bằng script riêng (chuyển trang không hiệu ứng, so đáy nội dung với 720): không trang nào vượt khung; C08 nay 116–604. Cỡ chữ nhỏ nhất 0,752em (ô bảng).
- Đã xem ảnh 1600×900: A03, B02, B10, B10b, B13b, C02, C03, C06, C08, C10b, D03, D04, D06b, D09c, D11, D13, E01, E02, E02d, E03, E06b; 390×844: năm trang tiêu đề mạch (DT đã xem).
- `git diff --check` sạch.

## Rà lại vòng 2 và sửa (giai đoạn II)

### Tác tử

| Vai trò | Loại | Mô hình | Effort | Ghi file |
|---|---|---|---|---|
| Rà lại toán và thuật toán (`deckrecheck-05-TOAN.md`) | general-purpose, chỉ đọc (theo lệnh gọi của điều phối viên) | claude-opus-5-5 | high | không |
| Rà lại kết nối và mạch (`deckrecheck-05-MACH.md`) | general-purpose, chỉ đọc (theo lệnh gọi của điều phối viên) | claude-opus-5-5 | high | không |
| Biên tập viên deck Bài 05 (cùng tác tử vòng trước) | general-purpose | claude-opus-5-5 | high | deck, `outline.md`, `storyboard.md`, mục này |

Kết quả rà lại: 0 chặn, 0 nghiêm trọng; TOAN 7 nhẹ; MACH 2 trung bình, 10 nhẹ. Lỗi nghiêm trọng TOAN-1 (B10b) và các trung bình cũ được xác nhận đã sửa. Không commit.

### Bảng mã và trạng thái

| Mã | Trang | Mức | Trạng thái |
|---|---|---|---|
| MACH-T1 (gộp TOAN-2 rà lại) | E01, A03 | trung bình | Đã sửa: E01 dòng 4 "Bảng cố định: mục tiêu TD chệch $-0{,}324$ tại $\mathrm S$; $Y^*$ bỏ $20\%$ phương sai; hội tụ cần Robbins–Monro" (dùng $Y^*$, đã định nghĩa ở D04b, thay "mục tiêu lý tưởng" để giữ trần 80); dòng 6 "Chọn theo dữ liệu và giả thiết; Bài 06 cải thiện chính sách". "Lần ghé đầu tiên" cho $0{,}852/\sqrt n$ và "bảng TD(0) sau $e_1$" cho $-0{,}324$ đặt trong ghi chú E01 vì mặt trang ở trần (78/80). A03 dòng 4 "Bảng cố định: TD chệch, mục tiêu lý tưởng ít dao động; hội tụ khi bước giảm" |
| MACH-T2 | D07 | trung bình | Đã sửa: "Trực quan. Với $T_\pi V=r_\pi+\gamma P_\pi V$ (Bài 04), $v_\pi$ là điểm bất động; …" (58 âm tiết). Phát hiện thêm khi xem ảnh: công thức Robbins–Monro tràn mép phải từ vòng trước (thêm $\alpha_n(s)\in[0,1]$); sửa bằng dòng "Lịch bước học Robbins–Monro:" và bỏ nhãn trong công thức |
| TOAN-1 | A03 dòng 2 | nhẹ | Đã sửa: "mẫu lợi tức không chệch, trung bình hội tụ về $v_\pi$" |
| TOAN-2 | E01 | nhẹ | Đã sửa (ghi chú diễn giả, như MACH-T1) |
| TOAN-3 | E02b | nhẹ | Đã sửa: "lượt của $\mathcal D$ kết thúc (TD: hoặc $\gamma<1$); $\alpha N(s)<2$ (Monte Carlo), $\le1$ (TD)" |
| TOAN-4 | E02 | nhẹ | Đã sửa: "Hàng 2 và 4 còn cần: $\pi$ cố định, trạng thái Markov, phần thưởng bị chặn" (cách viết ngắn để dòng không ngắt và bảng không chạm chân trang) |
| TOAN-5 | D05b | nhẹ | Đã sửa: số hiệu trên dòng Ý nghĩa đổi thành "(Hệ quả 05.26)" |
| TOAN-6, MACH-N2 | C03 | nhẹ | Đã sửa: "bảng TD(0) sau $e_1$" |
| TOAN-7 | B12d (ghi chú) | nhẹ | Đã sửa: "với $\gamma=1$, $v_\pi(\mathrm C)=1$" |
| MACH-N1 | C07, C08 | nhẹ | Đã sửa: Diễn giải trên mặt trang; lý do PB-12 trong mục trước được sửa |
| MACH-N3 | B08 | nhẹ | Đã sửa: "Nhu cầu: theo kịp môi trường thay đổi (ngoài giả thiết dừng); bước $1/n$ cho mẫu thứ $1000$ trọng số $1/1000$" |
| MACH-N4 | A03 | nhẹ | Đã sửa (như MACH-T1) |
| MACH-N5 | D04b | nhẹ | Đã sửa: "Nhu cầu: tách dao động khỏi độ chệch khi mục tiêu TD đọc bảng đang sai; thay bảng bằng $v_\pi$" |
| MACH-N6 | E03, ghi chú A06 | nhẹ | Đã sửa: Bài tập 05.8 chuyển sang hàng mạch 6 (bài tổng hợp E06), hàng mạch 4 còn 05.9–05.11, 05.14; ghi chú E03 nêu 05.8 nằm ở Mục 4.1 của ghi chú bài giảng; ghi chú A06 thêm 05.8 cho mục tiêu 3 và 4 |
| MACH-N7 | B03, A03, A06 | nhẹ | Sửa một phần: "(truncated episode)" lên mặt B03 (dòng Lưu ý tách hai dòng). A03 (60) và A06 (80) đã ở trần nên không thêm tên tiếng Anh; quy ước "tên tiếng Anh ở trang định nghĩa khi trang dùng đầu đã ở trần" ghi vào bảng thuật ngữ của `outline.md` |
| MACH-N8 | ghi chú C03, C07, A03 | nhẹ | Đã sửa: bỏ "ngay sau định nghĩa", "trước đó", "của trang tiên quyết" |
| MACH-N9 | `storyboard.md`, `outline.md` | nhẹ | Đã sửa: câu tóm tắt và bảng trước/sau theo số đo 2026-10-14 (A03 60, E01 78, E03 54 với 6 dòng; 10 dòng vượt có ngoại lệ; 5 trang trên 60 đều trần 80); outline ghi cập nhật 2026-10-14 |
| MACH-N10 | D07a | nhẹ | Đã sửa: "$Y_n=1$; khi đó $1-V_n=\prod…$" (công thức gói ngoặc nhọn, không ngắt dòng); "${\sigma^2,}$" không để dấu phẩy mồ côi |

### Đề nghị sửa ghi chú bài giảng (bổ sung)

| Vị trí trong ghi chú | Nội dung sửa | Nguồn |
|---|---|---|
| §1, đoạn đọc hình `learning-route.svg` (sau dòng 110) | Đoạn đọc hình gán khối "Lựa chọn" cho Mục 5, nhưng Mục 5 là dữ liệu cố định và cập nhật theo lô; hình không có khối cho Mục 5. Vẽ lại hình theo năm mục hoặc sửa đoạn đọc hình | MACH rà lại |
| Giai đoạn III (`exercises.md`) | Đưa bài chọn mẫu tại $\mathrm S$ với $\gamma=0{,}9$ của L05-B13/B13b vào tệp bài tập làm bài trùng trang chiếu, cùng lời giải $-0{,}0405$, $-0{,}04525$, $-0{,}22275$ | điều phối viên |

### Trang đổi trong vòng này và âm tiết (`density.py`)

A03 60, A06 (chỉ ghi chú) 80, B03 52 (5 dòng), B08 54, B12d (chỉ ghi chú) 59, C03 60, C07 34, C08 35, D04b 52, D05b 56, D07 58 (5 dòng), D07a 51, E01 78, E02 72, E02b 80, E03 54. Ghi chú diễn giả đổi thêm ở A03, C03, C07, E01, E03.

### Kiểm sau sửa

- `density.py`: mười dòng `<-- VƯỢT`, đều có ngoại lệ trong `storyboard.md` (A06, B00, C00, D00, E00, E02, E02b, E02d, E01).
- `deck_check.py` (cổng 8799), 1600×900 và 390×844: 70 trang, 0 lỗi và cảnh báo console, 0 `.katex-error`, 0 yêu cầu ra ngoài, 0 yêu cầu lỗi, không cuộn ngang, năm trang tiêu đề mạch.
- Đo khung: không trang nào vượt 720. Thêm phép đo mép phải của mọi phần tử KaTeX: không công thức nào vượt mép phải, trừ hai đường SVG của căn bậc hai ở B12, E01 (báo giả đã biết, ảnh không tràn).
- Đã xem ảnh 1600×900: A03, B03, B08, C03, C07, C08, D04b, D05b, D07, D07a, E01, E02, E02b, E03. D04b sát mũi tên trên nên hình `target-randomness.svg` giảm từ 260 xuống 225 px.
- `git diff --check` sạch.

### Quyết định của điều phối viên (2026-10-14, giai đoạn II, deck)

- Tác tử: tác tử soạn kiêm biên tập (general-purpose, claude-opus-5-5, high) hai vòng, bị dừng một lần theo yêu cầu người dùng và nối lại sau khi rà trạng thái đĩa; rà lại toán và rà lại mạch (general-purpose, claude-opus-5-5, high, chỉ đọc); điều phối viên Claude Fable 5.1 (medium).
- Kiểm độc lập sau vòng 2: `density.py` chỉ gắn cờ các trang có ngoại lệ trong `storyboard.md`; Playwright 1600×900 và 390×844: 0 lỗi console, 0 `.katex-error`, 0 yêu cầu ngoài, không cuộn ngang, đủ trang tiêu đề mạch; ảnh các trang đổi chính xem trực tiếp; `git diff --check` sạch.
- `img/lec-05/mc-td-timeline.svg` không còn được deck hay ghi chú dùng (xem đề nghị ở giai đoạn I, dòng "Không dùng `mc-td-timeline.svg`"); chấp nhận xóa trong commit này. Bốn thuộc tính `style="margin-left"` cho bước con của giả mã được chấp nhận tạm; đề nghị lớp `ol.substeps` chuyển sang đợt đồng bộ chéo CSS chung.
- Quyết định: **chấp nhận**; commit `fix(lecture-05)`.
