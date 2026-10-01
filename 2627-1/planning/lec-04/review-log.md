# Nhật ký xây dựng lại Bài 04

## Lịch sử giai đoạn lập kế hoạch — 2026-09-28

Người dùng yêu cầu bỏ toàn bộ dàn bài cũ, lập lại từ đầu theo Sutton–Barto chương 4 rồi viết lại bộ trang chiếu; tiêu đề, nội dung và ghi chú phải học thuật, thống nhất ký hiệu. Điều phối viên đã chấp nhận kế hoạch tác nghiệp 7 mạch, 45 trang, 120 phút. Lượt này thay toàn bộ `analysis.md`, `outline.md`, `storyboard.md`, `review-log.md` và loại `note-for-author.md` cũ không còn hiệu lực. Không đọc/dùng outline hoặc storyboard cũ làm khung. Tại thời điểm kết thúc giai đoạn lập kế hoạch, HTML, SVG, index và ghi chú công khai chưa được sửa; các giai đoạn triển khai và rà tiếp theo được ghi bên dưới.

Các tệp quy trình của kho đã được sửa trước lượt này được giữ nguyên: `AGENTS.md`, `prompt_lecture_note_deck.md`, `.codex/README.md`, `.codex/config.toml`, `.codex/workflow-smoke-test-prompt.md`, `openrouter-mcp/README.md`. Không dùng OpenRouter, không đọc `.env`/bí mật, không gọi mô hình qua API hoặc CLI.

## Điều phối và bằng chứng mô hình

| Tác tử | Vai trò | Cấu hình được chỉ định từ lời gọi gốc | Trạng thái ở lượt này |
|---|---|---|---|
| lec04_planner | Lập kế hoạch và kiểm chứng số chỉ đọc | `model: gpt-6-astra`, `reasoning_effort: xhigh`, `fork_turns: none` | Kế hoạch và numeric-report được điều phối viên chấp nhận |
| lec04_source_map | Ánh xạ nguồn, tài sản, bài tập, ký hiệu chỉ đọc | Cùng cấu hình trên | source-report được điều phối viên chấp nhận; đủ 38 trang |
| lec04_research | Sutton–Barto và hai bộ đại học chỉ đọc | Cùng cấu hình trên | research được điều phối viên chấp nhận |
| lec04_outline_writer | Soạn mới bốn tệp kế hoạch | Cùng cấu hình trên theo phân công của điều phối viên | Đã tự biên tập; trạng thái lịch sử trước gate chấp nhận và triển khai HTML |

Cấu hình trên là cấu hình đã chỉ định trong công cụ tác tử gốc theo hồ sơ điều phối; chưa có bằng chứng công cụ xác minh riêng mô hình thực chạy hoặc tuyến xác thực subscription. Không dùng lời tự khai của tác tử để xác nhận hai điểm đó. Không tạo tác tử con trong lượt soạn.

Codex Slides đã mở dự án bền vững `20260928103306-b-i-04-gi-i-mdp-b-ng-quy-ho-ch-ng-h-s-vi-ukmg` theo session-context. Đây là shell dự án, chưa phải bằng chứng bài mới đã dựng hoặc rà bằng Codex Slides. URL: `http://127.0.0.1:4311/?resume=20260928103306-b-i-04-gi-i-mdp-b-ng-quy-ho-ch-ng-h-s-vi-ukmg`. Không chạy tạo nội dung bằng mô hình của plugin. Việc kiểm định RevealJS và tải hiện vật vào dự án chưa diễn ra ở giai đoạn lập kế hoạch này.

## Tiếp nhận nguồn và quyết định cấu trúc

- Đã đọc đầy đủ bản trích PDF nguồn 38 trang, dữ kiện và báo cáo số. Đã đọc chương 4 bản sách hoàn chỉnh; báo cáo nguồn đại học và hình nguồn được đọc độc lập, điều phối viên chấp nhận trước khi chốt kế hoạch.
- Mạch mới: A mở đầu 5 trang/10 phút; B đánh giá 8/22; C cải thiện 7/20; D lặp chính sách 6/18; E lặp giá trị 8/22; F quy hoạch động thực hành 6/16; G tổng hợp 5/12. Tổng 45/120. Mỗi mạch có kiểm tra riêng; 30 phút chữa bài ngoài tuyến chính, không tạo code demo.
- Mở bài theo thứ tự giới thiệu → nội dung/mục tiêu → bài toán → mô hình cụ thể → kiểm tra. Bellman tối ưu được đưa sau ví dụ cải thiện và chính sách ổn định. Đây là thay thứ tự theo chỉ dẫn người dùng, không tự nhận là giữ nguyên thứ tự PDF.
- Bỏ các trang mục lục lặp 11,16,22; thay mục lục đầu tr. 3. Các ý học thuật của toàn bộ 38 trang vẫn có đích, ghi chú hoặc sửa có lý do trong ánh xạ.

## Sửa nội dung và ký hiệu

| Vấn đề nguồn | Quyết định | Bằng chứng/đích |
|---|---|---|
| $G_t$ bị gọi là hàm phần thưởng | Dùng “tổng thưởng chiết khấu”, thưởng là $R_{t+1}$ | NG1 tr. 5; L04-A05 |
| Ký hiệu giá trị không thống nhất | $v_\pi,q_\pi$ chính xác; $V_k$ ước lượng; $i,k,t$ khác vai trò; $Q_V$ được định nghĩa rõ | Ledger outline; toàn bài |
| Tr. 19 bỏ đánh giá chính sách giữa | Khôi phục $(10,30)$ trước đổi $s_0$ sang b | L04-C06–C07,D02; số hữu tỉ kiểm chứng |
| Bảo đảm PI thiếu điều kiện | Đánh giá chính xác, giữ hành động cũ khi hòa; nếu đổi chọn cực đại theo thứ tự cố định; đầu ra cùng chính sách | L04-D03–D06; SB §4.3, Ex. 4.4 |
| Delta và sai số bị lẫn | Phần dư đo trên bảng được trả; sai số bị chặn bởi phần dư chia $1-\gamma$ | L04-B05–B06,E04,E07; hệ quả tự suy đã kiểm |
| Tại chỗ và bất đồng bộ bị đồng nhất | Tách ví dụ tại chỗ và quy trình bất đồng bộ; mọi trạng thái được cập nhật vô hạn lần trong bảo đảm | L04-F02–F03; SB §4.5 |
| Lưới thiếu biên/kết thúc | Đi trái c1 ở lại, thưởng -1; nhận 10 trên chuyển vào c5, giữ giá trị c5 bằng 0 | L04-E06,E08; ghi rõ bổ sung |
| Chi phí so sánh thiếu đơn vị | Đếm chi phí mỗi lượt với mô hình đặc/thưa; không khẳng định luôn nhanh hơn | L04-F01,G02 |
| CartPole rời rạc bị xem là MDP có sẵn | 324 tổ hợp là biểu diễn; còn cần p và điều kiện Markov, có thể cần terminal riêng | L04-F05–F06 |
| hw04 thiếu yêu cầu/biên | Câu hỏi xây dựng từ dữ kiện nguồn, nêu bổ sung biên, thưởng theo chuyển thực tế | L04-G03; đáp án $V_1=(-1,-1,-1,7.8,0)$, $V_2(c_3)=4.436$ |

Hệ quả phần dư và chi phí phép tính do nhóm suy từ công thức đã kiểm, không gán nguyên văn cho một trang sách. Không thêm chặn tổn thất chính sách. Không dùng lưới sách $\gamma=1$ làm ví dụ trung tâm; chỉ đọc thêm với điều kiện kết thúc thích hợp. GPI thêm theo chương 4 để tổng hợp cơ chế, không tuyên bố mọi xấp xỉ đều hội tụ.

## Tự kiểm no-ai-slop — Edit

Đã đọc `/home/tqlong/.codex/skills/no-ai-slop/SKILL.md` và `eval.md`. Phạm vi: tiêu đề 45 trang, luận điểm, ý chính, câu hỏi, đáp án và ghi chú học thuật dự kiến; văn bản phân tích và storyboard. Đặc trưng giữ: thuật ngữ Học tăng cường, cấu trúc giả thiết–suy luận–kết luận, ký hiệu chuẩn, các phân biệt chính xác/gần đúng và đồng bộ/tại chỗ, chức năng đánh giá học tập. Văn phong học thuật theo chỉ dẫn dự án có ưu tiên hơn gợi ý giữ giọng nói của skill.

Kết quả tự đối chiếu trực tiếp eval.md:

| Nhóm kiểm | Kết quả và bằng chứng hành động |
|---|---|
| Giữ ý, chi tiết và mức chính xác | Đạt: giữ bốn chuyển tiếp, gamma, các bảng nguồn; ghi riêng mọi bổ sung; không cắt giả thiết cần cho bảo đảm. |
| Câu có chức năng và động từ cụ thể | Đạt: tiêu đề gọi khái niệm hoặc kết quả; các nhiệm vụ dùng Tính/Xác định/Giải thích; bỏ tiêu đề tu từ và câu ca ngợi nguồn tr. 30,37. |
| Lời dẫn, nhấn mạnh rỗng, metadiscourse | Đạt sau sửa: loại “ngay bây giờ” khỏi dẫn nhập; không dùng “chúng ta”, “hãy quan sát”, “điểm mấu chốt” hay lời điều hành trong ghi chú dự kiến. |
| Nhịp câu khuôn mẫu và thay từ tùy tiện | Đạt: tên đánh giá/cải thiện/chính sách/bảng giá trị được dùng cố định; giữ cấu trúc trường trong hồ sơ vì chức năng kiểm định, không chuyển các nhãn đó ra mặt trang. |
| Khẩu hiệu, kết luận kịch tính, định dạng trang trí | Đạt: kết luận bằng nghiệm có giả thiết và nhiệm vụ đọc/tính; không emoji, khẩu hiệu hoặc câu kết ẩn dụ. Tổng kết và câu hỏi được giữ vì chức năng học tập rõ. |
| Mức biên tập và tự đọc cuối | Đạt trong phạm vi kế hoạch: không suy đoán tác giả, không dùng điểm phát hiện AI; câu toán học giữ nội dung và tính điều kiện. Bản đầy đủ nằm trong bốn tệp, thay đổi được ghi ở các mục trên. |

Đây là tự kiểm của tác tử soạn, chưa thay báo cáo Detect độc lập cho bài hoàn chỉnh. Những từ như “kết nối”, “thời lượng”, “quyết định” ở tệp quy trình là metadata được phép; không đưa chúng vào notes hoặc mặt trang.

## Rà tính liên tục theo Quill

Đã đọc `/home/tqlong/.codex/skills/quill/SKILL.md` và mục Outline/Threads trong `references/workflows.md`. Chỉ áp dụng việc theo dõi khái niệm, tiên quyết và quan hệ đầu vào–đầu ra; theo yêu cầu cụ thể, không khởi tạo `quill.json`, không tạo dự án sách.

Các mạch mở được đóng theo thứ tự: giá trị dài hạn của chính sách được giải ở B; hành động tốt hơn được giải ở C; lặp tới ổn định được giải ở D; chi phí đánh giá đầy đủ được xử lý ở E; lịch và mô hình được xét ở F; nghiệm và điều kiện được kiểm ở G. Dữ kiện không đổi giữa B–E: thưởng $(1,0,2,3)$ và $\gamma=0.9$. Lưới xác định và lưới ngẫu nhiên có nhãn dữ kiện riêng. Ký hiệu $Q_V$ chỉ xuất hiện sau định nghĩa, phần dư/chuẩn trước khi được dùng trong tiêu chuẩn dừng. Kết luận không thêm thuật toán trọng tâm. Không có cờ liên tục chưa giải quyết trong kế hoạch; mối nối D04→E05 cần giữ cách phát biểu định lý và chứng minh như storyboard đã ghi.

## Kiểm định cấu trúc lượt 1

- Đếm bằng script nội bộ: 45 mã duy nhất, 7 mạch, 120 phút; đúng số trang/thời lượng từng mạch. Đủ 38 hàng ánh xạ và 7 kiểm tra riêng có đáp án; bài tập G03 là mục thứ tám có yêu cầu.
- Công thức Markdown chỉ dùng `$...$` và `$$...$$`. Chuẩn hóa prime thành chỉ số trên ký tự apostrophe trong biểu thức KaTeX; không để ký tự điều khiển sinh do xử lý chuỗi.
- Các số chính được nhận từ báo cáo tính hữu tỉ đã chấp nhận. Không tạo bài demo hay notebook. Không có tài sản raster/ngoại lệ cần người dùng duyệt.
- Chưa xác nhận HTML, KaTeX render, SVG, phông chữ, đường dẫn, tràn trang, bàn phím, màn hình hẹp hoặc trạng thái Codex Slides vì lượt này chỉ lập kế hoạch. Các báo cáo rà độc lập còn chờ; không gắn trạng thái hoàn tất cho deck.

## Các bước phụ thuộc đã dự kiến ở giai đoạn lập kế hoạch

Điều phối viên kiểm tra kế hoạch và tác tử storyboard rà chỉ đọc. Sau khi được chấp nhận, tác tử soạn mới triển khai HTML/SVG theo kế hoạch, rồi thực hiện các lượt rà nội dung, kết nối, văn phong và góc nhìn sinh viên. Ghi chú công khai được đồng bộ ký hiệu và dẫn chiếu riêng, giữ chứng minh chuyên sâu và các ví dụ bổ sung khác dữ kiện deck. Nhật ký này sẽ tiếp tục được cập nhật bằng phát hiện, quyết định sửa và kiểm định thực tế.

## Triển khai RevealJS sau gate — 2026-09-28

Tác tử lec04_deck_writer nhận thông điệp PLAN_ACCEPTED sau khi tác tử dàn bài nhả quyền ghi. Vai trò: soạn HTML/SVG và cập nhật mô tả chỉ mục; cấu hình được điều phối viên chỉ định là model gpt-6-astra, reasoning_effort xhigh, fork_turns none. Đây là bằng chứng cấu hình lời gọi, không phải tự xác nhận mô hình thực chạy. Không tạo tác tử con, không dùng OpenRouter, API/CLI mô hình hoặc .env.

Đã thay toàn bộ lecture-04-giai-mdp-bang-quy-hoach-dong.html bằng 45 trang theo 45 mã đã duyệt, chia 7 mạch. Mỗi trang có ghi chú diễn giải học thuật và nguồn theo trang/mục cụ thể. Nội dung hiển thị có 8 mục “Câu hỏi:”, gồm 7 kiểm tra mạch và bài tập lưới ngẫu nhiên. Đáp án nằm trong ghi chú; dữ kiện hai trạng thái và lưới được giữ theo báo cáo số đã chấp nhận.

Tạo 10 SVG dp04-*: chín hình dự kiến cùng dp04-roadmap.svg biểu diễn bản đồ nội dung của A02. Storyboard đã bổ sung dòng tài sản cho hình bản đồ, không đổi số trang, thứ tự hoặc thời lượng. Mỗi SVG có role="img", title, desc; mọi ảnh nhúng có mô tả thay thế. Giữ nguyên năm SVG của ghi chú chuyên sâu. Không tạo tài sản raster.

Các quyết định triển khai:

- Chỉ dùng lớp giao diện trong lecture-slide.css; không có thẻ CSS cục bộ, không sửa CSS chung, RevealJS hay tiện ích.
- B05 định nghĩa chuẩn vô cùng và phần dư trước quy trình. Giả mã B05/D03/E04/F03 dùng danh sách HTML, giữ cỡ chữ thân bài, có đầu vào, dừng/ngân sách và đầu ra nhất quán.
- E06 đặt sơ đồ/quy ước cạnh bảng 0–4; G03 tách sơ đồ nhánh khỏi dữ kiện và câu hỏi. Công thức dài của lưới ngẫu nhiên nằm trong ghi chú, không giảm chữ để nhét trang.
- F03 ghi rõ điều kiện cập nhật vô hạn lần cho các trạng thái chưa kết thúc; giá trị kết thúc giữ bằng 0. Ghi chú áp dụng quy trình vào lịch ngược của lưới và kiểm phần dư toàn bảng bằng 0.
- Meta viewport cho phép phóng to trên điện thoại; giữ khung RevealJS 1280 × 720 và các cấu hình bắt buộc.
- G05 chỉ liên kết toàn bộ “Ghi chú chuyên sâu”; không ánh xạ bảy mạch sang bảy phần ghi chú theo số thứ tự.
- Mô tả Bài 4 ở index.html được sửa theo mạch đánh giá → cải thiện → lặp chính sách/lặp giá trị → bất đồng bộ và giới hạn mô hình.

### Tự biên tập no-ai-slop và rà Quill của HTML

Đã áp dụng Edit và đối chiếu trực tiếp no-ai-slop/eval.md cho toàn bộ tiêu đề, nội dung hiển thị, chú thích SVG, ghi chú diễn giả và mô tả chỉ mục. Giữ ký hiệu, điều kiện toán học, bốn chuyển tiếp nguồn và các lời giải. Loại metadata lập kế hoạch, lời điều hành, diễn giải về công việc người soạn và phần lặp lời giải không cần thiết. Không dùng lời ca ngợi, câu hỏi tu từ, kết luận kịch tính, từ đồng nghĩa thay tùy tiện hoặc suy đoán tác giả. Các câu có chức năng định nghĩa, lập luận, điều kiện, kết luận toán học hoặc đánh giá học tập. Tự kiểm các nhóm giữ ý, câu cụ thể, mẫu diễn đạt, định dạng và tự đọc cuối: đạt trong phạm vi bản soạn. Đây chưa thay thế Detect độc lập.

Rà tính liên tục theo Quill trên tuyến HTML: A thiết lập mô hình và nhu cầu tính tổng thưởng; B tính giá trị; C dùng đúng giá trị đó để so sánh hành động; D đánh giá lại chính sách mới; E cắt ngắn đánh giá và kiểm phần dư; F thay lịch, tổng hợp GPI và xem giới hạn mô hình; G kiểm lại nghiệm và chuyển sang bài tập từ nguồn. $Q_V$ chỉ dùng sau định nghĩa E03; chỉ số $i,k,t$ được phân biệt; lưới xác định và ngẫu nhiên có quy ước riêng. Không tạo quill.json.

### Kiểm tra của tác tử soạn

- Kiểm tra cấu trúc: 45 mã duy nhất khớp thứ tự kế hoạch; 7 phần ngoài; 45 khối notes; 8 nhãn “Câu hỏi:”; footer và thư viện cục bộ đúng.
- Kiểm tra đường dẫn: không có tài nguyên cục bộ bị thiếu; không tham chiếu raster; không có mã nội bộ ngoài thuộc tính HTML.
- Phân tích XML: cả 10 SVG hợp lệ, đủ vai trò và mô tả.
- KaTeX cục bộ: phân tích 578 biểu thức từ toàn bộ HTML, kể cả notes; không có lỗi cú pháp. KaTeX có cảnh báo bảng metric cho một số ký tự tiếng Việt trong hàm text, cần kiểm hiển thị ở lượt trình duyệt toàn bài.
- Kiểm tra trực quan cục bộ ở 1280 × 720: B05, D03, E04, E06, F03, G03. Cả sáu trang không tràn đáy; đã xem ảnh để kiểm chữ và đồ thị. Đã sửa đường dẫn mũi tên lưới và dời nhãn xác suất khỏi đường nối của hình ngẫu nhiên, rồi kiểm lại.
- Không sửa ghi chú công khai hoặc năm SVG gắn với ghi chú; đối chiếu git diff xác nhận các tệp đó và CSS/thư viện không đổi trong lượt này.
- Ảnh kiểm cục bộ ở /tmp/rl04-rebuild/writer-preview/. Chưa chạy thay lượt kiểm toàn bộ 45 trang/màn hình hẹp của điều phối viên; chưa tuyên bố hoàn tất năm báo cáo độc lập hoặc kiểm Codex Slides.

## Đồng bộ ghi chú chuyên sâu — 2026-09-28

Tác tử `lec04_note_sync` nhận `WRITE_NOTE` sau khi tác tử HTML nhả quyền ghi. Vai trò: đồng bộ ghi chú công khai; cấu hình do điều phối viên chỉ định là `gpt-6-astra`, mức suy luận `xhigh`, qua cơ chế tác tử gốc. Cấu hình lời gọi không được dùng để tự xác nhận mô hình thực chạy. Không tạo tác tử con, không dùng OpenRouter, API/CLI mô hình hoặc `.env`.

Phạm vi nội dung là `materials/lec-04/lecture-note.md`. Giữ bảy phần riêng, bảy câu kiểm tra kèm gợi ý/lời giải, 50 công thức khối và các chứng minh về khả nghịch, cải thiện chính sách, tính co, Banach, tối ưu trên lớp chính sách phụ thuộc lịch sử và chặn phần dư. Giữ nguyên bộ số bổ sung: thưởng $(2,-1,5,10)$, $\gamma=0{,}5$, lưới có thưởng vào đích $24$, ví dụ chặn sai số đầu $64$. Năm SVG `two-state.svg`, `policy-evaluation.svg`, `gridworld.svg`, `convergence.svg`, `cartpole.svg` giữ nguyên nội dung và SHA-256.

Đầu ghi chú xác định đây là học liệu chuyên sâu với bộ dữ kiện độc lập với deck. Đồng bộ $v_\pi,q_\pi,T_\pi,P_\pi,r_\pi$, bảng $V,U,W$, dãy $V_k$, điểm nhìn trước $Q_V$, chính sách $\pi_V$, phần dư $b_\pi(V),b_*(V)$ và ngưỡng $\eta$. Giữ $\theta$ là góc CartPole và $\varepsilon$ là sai số yêu cầu. Phép đánh giá vẫn trả $W$ với chặn $\gamma b_\pi(V)/(1-\gamma)$; lặp giá trị vẫn trả đúng $V$ đã đo phần dư và trích $\pi_V$. Ở giai đoạn đồng bộ ban đầu chưa đổi quy tắc bảng trả; quyết định M02/P01 ở lượt sửa cuối bên dưới thay thế quy ước này.

Loại 14 dẫn số trang chiếu cũ; thay bằng tên khái niệm, mục Sutton–Barto đã được kiểm chứng, hoặc bỏ dòng dẫn trùng ý. Bổ sung tham khảo chương 3–4 của Sutton–Barto, sửa quan hệ giữa ghi chú và deck, xác định phạm vi Bài 3, 6, 7, 9 của `hw3.pdf` ở tr. 1–2 trong tài liệu bốn trang. Các ví dụ điều chỉnh không được gán là dữ kiện của Sutton–Barto hoặc của deck mới.

### Quy ước trạng thái kết thúc

Điều phối viên chấp nhận $\mathcal S$ chỉ gồm trạng thái chưa kết thúc, $n=|\mathcal S|$, còn $\mathcal S^+$ bổ sung trạng thái kết thúc khi có. Bảng giá trị mở rộng bằng $0$ tại kết thúc; hạng tiếp diễn ở đó bằng $0$ và không lấy cực đại trên tập hành động kết thúc. Phần thưởng về sau được quy ước bằng $0$ trong tổng vô hạn.

Ma trận $P_\pi$ vẫn có cỡ $n\times n$ trên $\mathcal S$, tổng hàng không vượt $1$. Chứng minh khả nghịch thay bước tổng hàng bằng $1$ thành không vượt $1$. Công thức $r_\pi$ lấy tổng trên $\mathcal S^+$ để giữ phần thưởng chuyển vào trạng thái kết thúc. Chứng minh theo lịch sử xác định khai triển hành động tại trạng thái chưa kết thúc; tại kết thúc phần thưởng và phần tiếp diễn bằng $0$. Không mở rộng kích thước ma trận hoặc thêm hành động hình thức. Đây là sửa giả thiết của ghi chú; không thay số, quỹ đạo trước kết thúc hay ý của chứng minh.

### Biên tập no-ai-slop và rà Quill

Đã đọc `no-ai-slop/SKILL.md`, `eval.md`, `quill/SKILL.md` và mục Revise/Outline trong tài liệu quy trình của Quill. Áp dụng Edit và tự đối chiếu `eval.md` cho toàn bộ tiêu đề, thân bài, gợi ý, lời giải và nguồn của ghi chú. Các mẫu đã sửa có bằng chứng gồm “hãy theo đúng trạng thái kế”, “Hai điểm thực hiện quan trọng”, “tuyệt đối không trả”, “đã có trong tay”, “Tính duy nhất quan trọng vì...” và lời dẫn lặp “Kiểm lại...”. Bản sửa nêu trực tiếp đối số, phép tính, quy tắc đầu ra hoặc hệ quả toán học. Giữ định nghĩa, nhãn định lý, câu hỏi và tổng hợp vì chức năng học tập. Các nhóm giữ ý, câu cụ thể, mẫu diễn đạt, định dạng và tự đọc cuối đều đạt trong phạm vi tự kiểm; không dùng điểm phát hiện AI hoặc suy đoán tác giả. Kết quả này không thay thế Detect độc lập.

Quill được dùng để đối chiếu mạch mô hình → điểm nhìn trước/Bellman → đánh giá → cải thiện/lặp chính sách → lặp giá trị → chứng minh/sai số → chứng nhận và bài tập. Ghi chú giữ cấu trúc riêng; bảy ID chủ đề được bảo toàn, không coi thứ tự các phần là ánh xạ một–một với bảy mạch của deck. Không tạo `quill.json` hoặc cấu trúc dự án sách.

### Kiểm tra bản đã chuẩn bị

- KaTeX cục bộ: 1.071 biểu thức trong bản đồng bộ trước bổ sung terminal dựng được với `throwOnError=true`, `strict='error'`; không lỗi. Sau sửa terminal, kiểm riêng 42 biểu thức trong các đoạn thay đổi, không lỗi; tổng bản cuối là 1.084 biểu thức, trong đó 50 công thức khối.
- So sánh theo thứ tự: 49 trong 50 công thức khối giữ nguyên nội dung qua ánh xạ ký hiệu; công thức duy nhất sửa nội dung là miền tổng của $r_\pi$ để bao gồm thưởng vào trạng thái kết thúc. Các bước chứng minh vẫn được giữ.
- Giữ đủ 7 ID duy nhất, 7 câu kiểm tra và cùng số khối gợi ý, lời giải, chứng minh; công thức Markdown chỉ dùng `$...$` và `$$...$$`.
- Tính lại bằng phân số chính xác: ba lượt đánh giá $(2,5),(3,6),(3{,}5,6{,}5)$; ba bảng cải thiện; lưới đến $V_5=V_4=(1{,}25,4{,}5,11,24,0)$; $b_*(V_3)=3$; các chặn sai số $0{,}3$ và $0{,}2$ đều khớp.
- Danh sách đường dẫn và SHA-256 của năm SVG không đổi. Không còn tham chiếu số trang chiếu cũ hoặc ký hiệu thuộc phạm vi đồng bộ.

Ngoài phạm vi ghi chú, sửa đúng một lỗi tên tệp trong `prompt_lecture_note_deck.md`: `lecture-style.css` thành `lecture-slide.css`, theo yêu cầu điều phối. Không sửa phần khác của tài liệu quy trình. Bản chuẩn bị và báo cáo chi tiết nằm trong `/tmp/rl04-rebuild/lecture-note-synced.md` và `note-sync-plan.md`; không đưa tệp tạm vào kho. Lượt này không chạy lại rà nội dung hoặc viết lại bản đã duyệt; kiểm trình duyệt và năm báo cáo độc lập thực hiện trên bản đã cố định ở giai đoạn tiếp theo.

## Sửa ký hiệu sau kiểm tra toàn bài — 2026-09-28

Điều phối viên và tác tử kiểm định storyboard phát hiện lỗi nghiêm trọng ở mặt trang L04-A03, L04-A04, L04-A05, L04-B01, L04-B02: 15 biểu thức mất tổng cộng 16 dấu gạch chéo trước lệnh TeX. Ví dụ mathcal, gamma, pi, cdot vẫn được KaTeX đọc như tích các chữ cái, nên kiểm cú pháp trước đó không phát hiện lỗi ngữ nghĩa này. Nguyên nhân là chuỗi JavaScript không giữ nguyên ký tự khi ghi khối đầu của tiện ích sinh HTML; khai báo raw ở Python không khôi phục được ký tự đã mất trước đó.

Sau gate FIX_ESCAPE, tác tử lec04_deck_writer sửa trực tiếp năm trang và các literal tương ứng trong tiện ích sinh. Các ghi chú gốc bị hỏng trong tiện ích cũng được khôi phục; bỏ lớp vá ghi chú sau khi sinh. Không chạy lại bước ghi HTML của tiện ích để tránh ghi đè các sửa đổi hiện có. Đã bổ sung kiểm lệnh TeX bị mất dấu và ký tự điều khiển trước bước xuất; chạy riêng phần tạo chuỗi trong bộ nhớ xác nhận 45 chuỗi trang khớp HTML hiện tại, không ghi tệp đầu ra.

Quét toàn bộ 578 biểu thức trên mặt trang và trong ghi chú không còn tên lệnh TeX bị viết trần; ba nhóm báo nhầm đã đối chiếu là tích jR, môi trường aligned và tích nmd trong chi phí. KaTeX vẫn kiểm cú pháp 578 biểu thức thành công. Kiểm này bổ sung cho việc đọc công thức, không thay thế rà chính xác toán học.

Điều phối viên đồng thời phát hiện CSS viết hoa tiêu đề làm đổi ký hiệu chữ thường trong bốn tiêu đề thẻ ở L04-C02 và L04-D02. Đã thay tiêu đề thẻ bằng nhãn tiếng Việt “Hành động thứ nhất/thứ hai” và “Trạng thái thứ nhất/thứ hai”, đưa $a,b,s_0,s_1,(b,b)$ xuống thân thẻ. Không sửa CSS chung, cỡ chữ, công thức, mã hoặc thứ tự trang. Các tiêu đề toán còn lại ở B02/E07 chỉ có chữ hoa $V$ và chỉ số số học, không chịu thay đổi ý nghĩa.

Kiểm lại trình duyệt 1280 × 720 trên A01–A05, B01–B04 và C02/D02; không thấy phần tử nội dung tràn khung. A03 hết tràn chú thích sau khi khôi phục lệnh TeX, không cần giảm chữ hoặc thay nội dung. Đã xem trực tiếp ảnh A03, A05, B02, C02, D02 để xác nhận ký hiệu. Ảnh tại /tmp/rl04-rebuild/writer-escape-preview/. Giữ 45 mã, 7 mạch và 45 notes. Phạm vi trang thay đổi của lượt sửa là A03, A04, A05, B01, B02, C02, D02.


## Bản cố định cho năm vai độc lập — 2026-09-28

Năm tác tử chỉ đọc rà cùng bản đã sửa lỗi escape và ký hiệu tiêu đề. Điều phối viên kiểm đủ 18 SHA-256 trước khi giao `WRITE_FINAL`; không có thay đổi giữa các lượt rà. Bảng dưới là hồ sơ bền vững của manifest, không phụ thuộc tệp tạm. Những phát hiện và trích đoạn của các báo cáo ở sau phản ánh bản này, trước lượt sửa cuối.

| Tệp | SHA-256 |
|---|---|
| `2627-1/lecture-04-giai-mdp-bang-quy-hoach-dong.html` | `9047c8619836c14ca7ed015925095c0d98da73eee1ed25c5e4b13f63cc8a387d` |
| `2627-1/materials/lec-04/lecture-note.md` | `0fe241676026a5b227f705e4e28958e496f2841482673e8c3b4e3af38682ad5d` |
| `2627-1/index.html` | `088dbcc1c7e2f00288e20f63214fe804ab60ed69a94619306a0eb9088738b9fc` |
| `2627-1/lecture-slide.css` | `fb3bfe620eb6d17722da108b1917e824a69b31f0d5806de57c62394e9f2bd217` |
| `2627-1/planning/lec-04/outline.md` | `da0fdcec579ec3df79256b72a688c4e3e784b35385cc6f1a3b2d50a8baf64877` |
| `2627-1/planning/lec-04/analysis.md` | `a2a1683dab2a090d270e6d47b6eac694aba94a2e87a841b39044e7a2ac27cd68` |
| `2627-1/planning/lec-04/review-log.md` | `4190419ebe128bddc032d0309494558250d7cf8c9ab00e3705dd9f3d6fa8c0ae` |
| `2627-1/planning/lec-04/storyboard.md` | `6b9aad86d221ddd8e35927b19b8358921843c545f5a595db340a64b917850417` |
| `2627-1/img/lec-04/dp04-expectation-backup.svg` | `7dc0c92728324ed9afce8db62d28e2210ac31b5c8e481db65e08a291d5689fbd` |
| `2627-1/img/lec-04/dp04-update-order.svg` | `ba59d8a8895bf18a34fc2bb292263a12828afbfed33c3cb53b0a44c76e7b4aa3` |
| `2627-1/img/lec-04/dp04-one-step-choice.svg` | `8f3b36be2a5ccf8958568cb675d60baa496301bdf10244216563846f13f268cc` |
| `2627-1/img/lec-04/dp04-cartpole-bins.svg` | `0f87a28bb86e2317b1acfa85455c1cdd68d0c6d3682347fe7fdb242a93b62fc8` |
| `2627-1/img/lec-04/dp04-gpi.svg` | `343207c414848903d1ed70220f56c27173fded153b22a136440d444bc5750762` |
| `2627-1/img/lec-04/dp04-policy-iteration.svg` | `17f43bcd86db0cbc29cb5d464a290700fe52cc21656253dca4a208ea0687ef4f` |
| `2627-1/img/lec-04/dp04-five-cell.svg` | `60329df8d04718cf4ee92c3b5c2bbe93854beb4da93cb648e1d314fed623f12f` |
| `2627-1/img/lec-04/dp04-roadmap.svg` | `e921df255702aec40eba65ea4cf6e4b3412494aef012a1f6ae59e4a2dd056285` |
| `2627-1/img/lec-04/dp04-two-state.svg` | `ab048bef8a45d93ce3b9b68a1bdd528d7ba0ae87a4b8a96897d8caa37ac16488` |
| `2627-1/img/lec-04/dp04-stochastic-grid.svg` | `172ec346fa11cec0b21c703b0970fb8da940b5aa7aa03f5a8330b797821b8d6a` |

### Vai trò và cấu hình tác tử

| Tác tử | Vai trò | Cấu hình được chỉ định trong hồ sơ điều phối |
|---|---|---|
| lec04_review_student | Góc nhìn sinh viên, đọc hiểu và ảnh trình chiếu | gpt-6-astra; xhigh; fork_turns: none |
| lec04_review_rl | Chuyên gia Học tăng cường | gpt-6-astra; xhigh; fork_turns: none |
| lec04_review_math | Độ chính xác toán học và thuật toán | gpt-6-astra; xhigh; fork_turns: none |
| lec04_review_pedagogy | Phản biện học thuật và giảng dạy Học tăng cường–lập kế hoạch | gpt-6-astra; xhigh; fork_turns: none |
| lec04_review_flow | Kết nối và mạch viết | gpt-6-astra; xhigh; fork_turns: none |
| lec04_final_editor | Chỉnh sửa riêng sau năm báo cáo; một tác tử ghi tại một thời điểm | gpt-6-astra; xhigh; fork_turns: none |

Cấu hình chỉ định không được coi là bằng chứng độc lập về mô hình thực chạy hoặc tuyến xác thực. Tác tử chỉnh sửa không tạo tác tử con, không dùng OpenRouter, API/CLI mô hình hoặc đọc tệp bí mật. Hai báo cáo sư phạm và mạch viết hoàn tất trước thông điệp `WRITE_FINAL`; trước thông điệp đó tác tử chỉnh sửa chỉ đọc và chuẩn bị.

### Trạng thái các phát hiện trước bản cố định

| Mã | Mức độ | Trang | Vấn đề/bằng chứng | Quyết định và trạng thái |
|---|---|---|---|---|
| R01 / storyboard escape | nghiêm trọng | A03, A04, A05, B01, B02 | 15 biểu thức mất 16 dấu gạch chéo; KaTeX đọc thành tích ký tự, kiểm cú pháp vẫn qua | Đã khôi phục trực tiếp trước bản cố định; rà mẫu lệnh và ảnh bị ảnh hưởng/lân cận, tổng 14 ảnh của lượt kiểm lại theo hồ sơ điều phối. Không chạy lại generator. |
| R02 | trung bình | A03 | Chú thích Markov vượt mép dưới khi công thức còn hỏng | Đã hết tràn sau khôi phục công thức, trước bản cố định; không giảm cỡ chữ. |
| R03 | nghiêm trọng về ký hiệu hiển thị | C02, D02 | CSS tiêu đề viết hoa biến hành động/trạng thái | Đã đổi bốn tiêu đề thẻ sang nhãn tiếng Việt, ký hiệu ở thân thẻ; kiểm ảnh trước bản cố định. |
| R04 | trung bình | D01; dp04-policy-iteration.svg | Nhãn `vπᵢ` đặt π cùng dòng cơ sở | Lượt sửa cuối dùng `tspan` chỉ số dưới cho πᵢ, giữ các quan hệ và chiều mũi tên; cần kiểm ảnh D01 sau sửa. |
| R05 | nhẹ | G03 | Caption mô tả công việc bổ sung điều kiện nguồn | Gộp với SV-05/N01; giữ nguồn ngắn, bỏ siêu diễn ngôn, giữ các quy ước mô hình. |

Kiểm định storyboard trước triển khai đã đóng các mục metadata trong notes, chuẩn/phần dư trước giả mã, tải E06 và ứng dụng sau quy trình F03. Báo cáo đối chiếu bản triển khai phát hiện R01/R02 ở hash HTML `c024d32edd0bf9c1f665fe8e10bd5ce8a81bc7d4891aa27ce688e03ea0bf14bf`; hash này là lịch sử, không phải bản cố định mà năm vai rà. Các sửa sau năm báo cáo cần rà lại riêng, không kế thừa tự động kết quả ảnh cũ.

## Hồ sơ năm báo cáo độc lập

Các báo cáo dưới được lưu đầy đủ để giữ mức độ, trang, vấn đề, bằng chứng và đề xuất của từng vai. Chúng là hồ sơ lịch sử trên bản cố định, không phải mô tả hiện trạng sau sửa. Quyết định điều phối đối với từng phát hiện nằm sau năm báo cáo; sự khác nhau giữa nhận định của các vai được giữ nguyên.


### Báo cáo 1/5 — Góc nhìn sinh viên

### Rà soát độc lập — Góc nhìn sinh viên

#### Phạm vi và bản được rà

- Tác tử: `lec04_review_student`; vai trò chỉ đọc, độc lập với bốn vai rà soát còn lại. Không đọc báo cáo của các vai khác hoặc báo cáo root-review; không sửa tệp trong kho.
- Bản cố định: `/tmp/rl04-rebuild/frozen-review.json`.
- HTML: `2627-1/lecture-04-giai-mdp-bang-quy-hoach-dong.html`.
- SHA-256 HTML đã kiểm trước và cuối lượt: `9047c8619836c14ca7ed015925095c0d98da73eee1ed25c5e4b13f63cc8a387d`.
- Đã đọc toàn bộ 45 trang và 45 ghi chú diễn giả; đối chiếu bản đồ, ký hiệu, nội dung và thời lượng từng trang trong `outline.md`, cùng toàn bộ `storyboard.md`. Hai tệp đều có 45 mục theo đúng thứ tự HTML; tổng thời lượng từng trang là 120 phút. Đã kiểm hash của HTML, hai tệp quy trình và 10 SVG `dp04-*` so với bản cố định; không có sai khác.
- Đã kiểm nội dung nhãn, mô tả thay thế và cấu trúc của 10 SVG mới. Tham khảo mở đầu, các quy trình đánh giá/lặp giá trị, phần dư và tổng hợp của `materials/lec-04/lecture-note.md`; không coi bộ số riêng với $\gamma=0{,}5$ là lỗi so với bộ trang chiếu có $\gamma=0{,}9$.
- Đã đọc `AGENTS.md`, `$no-ai-slop/SKILL.md` và `eval.md`; áp dụng Detect. Đã đọc `$quill/SKILL.md` và Outline Workflow để đối chiếu thứ tự khái niệm, thuật ngữ và đầu vào–đầu ra; không tạo dự án sách.

#### Kết luận theo vai

Không phát hiện lỗi **chặn bàn giao** hoặc **nghiêm trọng** trong phạm vi góc nhìn sinh viên. Có hai đề xuất mức trung bình và ba đề xuất mức nhẹ. Mạch chính có đủ tiên quyết đối với sinh viên đã học MDP, xác suất, đại số tuyến tính và thuật toán; các phép tính cụ thể xuất hiện trước công thức tổng quát của đánh giá, cải thiện, lặp chính sách và lặp giá trị.

Ví dụ hai trạng thái giảm việc phải học lại dữ kiện qua các phần. Sự phân biệt giữa $q_{\pi_0}(s_1,b)=12{,}9$ và giá trị sau khi đổi chính sách là $30$ được giải thích rõ ở C02/C06. D06 kiểm tra được một lỗi suy luận thực tế về chính sách ổn định theo bảng gần đúng. Các câu kiểm tra có dữ kiện và lời giải trong notes; G04 thu hồi cả việc tính và căn cứ chứng nhận nghiệm. Bảy phần phân bổ 120 phút hợp lý ở mức dự kiến; 30 phút chữa bài phù hợp với việc không có code trong nguồn.

#### Nhận xét cần xem xét

##### SV-01 — Đổi qua lại giữa hai mô hình nhưng nhãn trên mặt trang chưa đủ rõ

- **Mức độ:** trung bình.
- **Trang chiếu:** L04-E06 → L04-E07 → L04-E08.
- **Vấn đề:** E07 quay lại ví dụ hai trạng thái ngay sau lưới năm ô rồi E08 trở lại lưới. Mặt trang E07 không gọi tên mô hình đang dùng. Sinh viên phải tự nhận ra việc đổi dữ kiện từ kích thước vector và tên hành động, trong khi đang học phân biệt phần dư với sai số.
- **Bằng chứng:** E06 hiển thị bảng năm cột trạng thái với $V_1=(-1,-1,-1,10,0)$. Thẻ bên phải E07 chỉ mang tên “Bảng $V_1=(1,3)$”, tiếp theo là “Chính sách tham lam là $(b,b)$” và “Phần dư $2{,}7$; sai số giá trị $27$”. E08 lại cho $V_2=(-1{,}9;-1{,}9;8;10;0)$. Notes E07 nói “Trong mô hình hai trạng thái”, nhưng tín hiệu đó chưa có trên mặt trang. Ảnh `L04-E07-1280.png` xác nhận đây là vấn đề nhãn ngữ cảnh, không phải mất chữ.
- **Đề xuất sửa:** Gọi rõ “Mô hình hai trạng thái” ở thẻ E07 và “Lưới năm ô” trong dòng dữ kiện E08. Có thể nhắc $v_*=(27,30)$ trong notes hoặc cùng thẻ nếu còn chỗ để phép so sai số tự truy nguyên được. Không cần đổi thứ tự trang hoặc đổi ví dụ.

##### SV-02 — Cầu nối từ cập nhật tại chỗ theo chính sách sang cập nhật tối ưu còn ngắn

- **Mức độ:** trung bình.
- **Trang chiếu:** L04-F02 → L04-F03.
- **Vấn đề:** Ví dụ tính tay lớn ở F02 dùng đánh giá chính sách cố định, trong khi quy trình F03 dùng toán tử tối ưu. Cơ chế lưu một bảng được giữ nguyên nhưng bài toán và toán tử đổi. Sinh viên lần theo ví dụ vào giả mã có thể tưởng kết quả $2{,}9$ vẫn là kết quả của bước F03.
- **Bằng chứng:** F02 ghi “Đánh giá $\pi_0=(a,a)$” và $V(s_1)\leftarrow2+0{,}9\cdot1=2{,}9$. F03 chuyển sang $V(s)\leftarrow(T_*V)(s)$ và kết luận $V\to v_*$. Trên cùng mô hình, từ bảng $(1,0)$, toán tử tối ưu ở $s_1$ cho $\max\{2{,}9;3\}=3$, khác $2{,}9$. Câu cuối F02 nhắc lịch ngược trên lưới nhưng chưa nói rõ việc đổi từ đánh giá sang điều khiển. Storyboard mô tả đầu vào F03 là “Ví dụ tại chỗ được mở rộng thành lịch cập nhật không cần lượt quét đầy đủ”, nên cần nêu thêm thành phần thay đổi.
- **Đề xuất sửa:** Thêm nhãn ngắn ở F03 xác định đây là lặp giá trị bất đồng bộ, hoặc câu nối rằng cùng cách dùng bảng hiện có được áp dụng cho $T_*$ thay $T_\pi$. Notes có thể đối chiếu một phép tính $\max\{2{,}9;3\}=3$ để tách rõ thay lịch cập nhật với thay toán tử. Giữ nguyên ví dụ F02 vì nó đối chiếu tại chỗ với đồng bộ tốt.

##### SV-03 — Phần dư xuất hiện đồng thời với nhiều chi tiết của thuật toán

- **Mức độ:** nhẹ.
- **Trang chiếu:** L04-B04–L04-B06, trọng tâm L04-B05.
- **Vấn đề:** B05 đưa chuẩn vô cùng, phần dư, kiểm ngưỡng, bảng trả về và ngân sách vào cùng trang trong 3 phút. Chữ đủ lớn và giả mã rõ, nhưng lần gặp đầu tiên của phần dư chưa có một phép tính số ngắn ngay cạnh định nghĩa. Sinh viên có thể thực hiện cập nhật mà chưa gắn được đại lượng này với bảng cụ thể.
- **Bằng chứng:** Trang mở bằng “Chuẩn vô cùng: $\|U-V\|_\infty=\max_s|U(s)-V(s)|$” rồi “Phần dư: $b_\pi(V)=\|T_\pi V-V\|_\infty$”, tiếp theo bốn bước thuật toán. B02 đã có sẵn $V_1=(1,2)$ và $V_2=(1{,}9;2{,}9)$; phép tính phần dư số đầu tiên được yêu cầu ở B08.
- **Đề xuất sửa:** Bổ sung vào notes B05 hoặc phần cuối B04 một phép đối chiếu từ dữ kiện đã có: $b_{\pi_0}(V_1)=\max\{|1{,}9-1|,|2{,}9-2|\}=0{,}9$. Nêu đây là độ lệch của chính $V_1$ so với một cập nhật Bellman của nó. Không nhồi thêm một khối chữ vào mặt trang B05.

##### SV-04 — Bài lưới nên nêu tường minh tập hành động và phép lặp cần thực hiện

- **Mức độ:** nhẹ.
- **Trang chiếu:** L04-E06, L04-E08, L04-G03.
- **Vấn đề:** Dữ kiện đầy đủ có trong notes và mô tả thay thế, nhưng mặt trang chưa ghi trực tiếp rằng mỗi ô chưa kết thúc có cả hành động trái và phải. Bài tập G03 cũng chỉ yêu cầu tính $V_1,V_2$ mà chưa gọi tên lặp giá trị đồng bộ. Trong toàn bài có cả đánh giá theo chính sách và lặp giá trị, nên một nhãn sẽ giúp tự học mà không cần suy từ ngữ cảnh.
- **Bằng chứng:** Hình E06 chỉ vẽ mũi tên phải, đã ghi đúng “Mũi tên: chính sách tối ưu”; bullet có “Trái ở $c_1$: ở lại” nhưng chưa có tập hành động. Notes giải thích “Các mũi tên ... không loại bỏ hành động trái khỏi mô hình”. G03 vẽ một nhánh minh họa với “Hành động chọn: phải”, còn yêu cầu là “Từ $V_0=0$, tính $V_1$, rồi tính $V_2(c_3)$”. Notes dùng cực đại của cả hai hành động.
- **Đề xuất sửa:** Nêu ngắn “Hành động: trái hoặc phải” tại E06; tại G03 xác định yêu cầu là một lượt lặp giá trị đồng bộ và giữ cùng tập hành động của lưới. Không cần vẽ thêm toàn bộ mũi tên trái vào hình chính sách.

##### SV-05 — Chú thích bài tập còn thông tin về quá trình biên soạn

- **Mức độ:** nhẹ.
- **Trang chiếu:** L04-G03.
- **Vấn đề:** Một phần chú thích không giúp giải bài mà mô tả quyết định của người soạn. Đây là mẫu siêu diễn ngôn về biên soạn trong chế độ Detect của `$no-ai-slop`, đồng thời không phù hợp yêu cầu chỉ đưa nội dung học thuật và yêu cầu học tập lên mặt trang.
- **Bằng chứng:** “Dữ kiện: bài tập tuần 4. Quy ước biên, thưởng theo chuyển thực tế và yêu cầu tính được bổ sung.” Ảnh `L04-G03-1280.png` cho thấy câu này hiển thị công khai dưới bài tập. Phần “Dữ kiện: bài tập tuần 4” có chức năng ghi nguồn; phần sau mô tả việc bổ sung của tác giả.
- **Đề xuất sửa:** Giữ nguồn bài tập, chuyển câu về quyết định bổ sung sang storyboard/review-log. Các quy ước toán học đang có ở bullet và notes vẫn cần được giữ nguyên.

#### Kiểm tra hình ảnh và khả năng đọc

Đã thực sự mở bằng `view_image`:

- Năm contact sheet `/tmp/rl04-rebuild/contact-1.png` đến `contact-5.png`, bao phủ toàn bộ 45 trang ở ảnh 1280 × 720.
- Ảnh riêng 1280 × 720: A03, B01, B05, C02, D02, D03, E04, E06, E07, F02, F03, F05, G02, G03; đường dẫn theo mẫu `/tmp/rl04-rebuild/screens/L04-<mã>-1280.png`.
- Ảnh riêng chiều rộng 390 px: A03, B05, C02, D02, D03, E04, E06, F03, G03; đường dẫn theo mẫu `/tmp/rl04-rebuild/screens/L04-<mã>-390.png`.

Ở ảnh 1280 × 720 đã mở riêng, chữ thân bài, công thức trung tâm và số trong bảng đọc được. Các trang giả mã B05/D03/E04/F03 không chồng chữ và không có dấu hiệu thu chữ quá nhỏ; nhận xét SV-03 là về số khái niệm đồng thời, không phải kích thước chữ. Hình C02 phân biệt hành động bằng nhãn, hướng mũi tên và giá trị, không chỉ bằng màu. Bảng E06 đủ đọc ở kích thước trình chiếu và có cả chỉ số lượt lẫn trạng thái. Chú thích nhỏ hơn thân bài vẫn đọc được trong các ảnh desktop đã mở, nhưng không thể suy từ ảnh rằng hàng cuối lớp trong mọi phòng đều đọc được.

Ở 390 px, bộ trang chiếu giữ khung 16:9 nên chữ thân bài và bảng nhỏ rõ rệt khi xem toàn khung; không xác nhận rằng đọc lâu ở tỷ lệ mặc định là thoải mái. Theo phạm vi đã giao, đây là giới hạn của chế độ trình chiếu cố định và cần phóng to hoặc xem ngang. Lượt này không thử thao tác phóng to trên thiết bị thật, nên không dùng khả năng zoom trong metadata như bằng chứng đã kiểm trải nghiệm.

#### Văn phong, tự học và giới hạn của lượt rà

Ngoài SV-05, không phát hiện trong toàn bộ tiêu đề, mặt trang và notes mẫu lời dẫn rỗng, khẩu hiệu, câu hỏi tu từ, lời điều phối giảng viên hoặc nhận định khoa trương cần ghi thành finding. Các nhãn định lý, định nghĩa, câu hỏi kiểm tra và phần kết luận có chức năng học tập nên được giữ. Không chấm điểm văn bản bằng bộ phát hiện AI và không suy đoán tác giả.

Ghi chú chuyên sâu khai báo ngay đầu tệp rằng ví dụ có bộ số riêng; đó là thông tin có ích cho sinh viên tự học. Quy trình đánh giá trong ghi chú trả $W$ và có chặn tương ứng, trong khi bộ trang chiếu trả $V$ cùng phần dư của $V$; ghi chú đã nêu riêng quy ước này. Không yêu cầu ép hai tài liệu thành bản sao.

Đây là kiểm tra đọc hiểu và khả năng đọc từ nội dung cùng ảnh cố định; không thay thế rà toán độc lập, đối chiếu toàn bộ PDF nguồn, đo tương phản tự động, kiểm trình duyệt trực tiếp, kiểm bàn phím, kiểm màn chiếu thật hoặc Codex Slides. Không đọc hay dựa vào báo cáo của vai khác. Báo cáo hình học do điều phối viên nêu không được dùng thay cho việc xem ảnh trong lượt này.


### Báo cáo 2/5 — Chuyên gia Học tăng cường

### Rà soát độc lập Bài 04 — Chuyên gia Học tăng cường

Tác tử: `lec04_review_rl`. Phạm vi: toàn bộ bản bài giảng mới; rà độ bao phủ, chiều sâu, các phân biệt trong Học tăng cường, trình tự kiến thức và thời lượng. Đây là báo cáo chỉ đọc; không sửa tệp trong kho và không đọc báo cáo của bốn vai rà soát khác.

#### Bản được rà và phạm vi kiểm chứng

- Đối chiếu danh sách cố định `/tmp/rl04-rebuild/frozen-review.json`: **18/18 tệp khớp SHA-256** tại thời điểm rà.
- HTML: `2627-1/lecture-04-giai-mdp-bang-quy-hoach-dong.html`; SHA-256 `9047c8619836c14ca7ed015925095c0d98da73eee1ed25c5e4b13f63cc8a387d`. Đã đọc **45/45 trang, 45/45 khối ghi chú**, đủ bảy mạch A–G.
- Đã đọc nội dung và nhãn của cả **10 SVG `dp04-*`**, toàn bộ `analysis.md`, `outline.md`, `storyboard.md` và ghi chú chuyên sâu `materials/lec-04/lecture-note.md` (683 dòng).
- Nguồn đối chiếu: bản trích đủ 38 trang của `lecture04-solving-MDP.pdf`; `hw04.txt`; các báo cáo nguồn, nghiên cứu và số được điều phối viên cung cấp. Đọc trực tiếp các đoạn liên quan trong bản sách cục bộ `book.txt`: Sutton–Barto §4.1, §4.2–4.4, §4.5–4.8, trang in 74–89. Văn bản trích sách mất một số ký tự toán; không lấy phần ký tự lỗi làm căn cứ sửa công thức.
- Tính lại bằng phân số hữu tỉ: ba chính sách trong chuỗi PI ở cả bộ số của deck và note; các lượt VI 0–4 và lượt 55; bảng lưới xác định 0–5 ở cả hai bộ số; hai hành động tại $c_3$ trong lưới nhiễu. Kết quả khớp học liệu.
- Đã đọc và áp dụng `no-ai-slop/SKILL.md` ở chế độ Detect. Áp dụng Quill vào quan hệ tiên quyết, tính liên tục và thuật ngữ; không tạo `quill.json` hay dự án sách.

#### Kết luận

**Không phát hiện lỗi chặn bàn giao hoặc nghiêm trọng trong phạm vi chuyên môn đã rà.** Có hai vấn đề trung bình và ba vấn đề nhẹ dưới đây. Các vấn đề đều sửa được tại chỗ; không cần đổi số mạch hoặc đưa chứng minh chuyên sâu lên mặt trang chiếu.

Tuyến đánh giá → cải thiện → lặp chính sách → lặp giá trị → bất đồng bộ/GPI/giới hạn phù hợp yêu cầu viết mới theo Chương 4. Việc giữ cùng MDP hai trạng thái qua bốn cơ chế làm rõ sự thay đổi của đối tượng được giữ cố định. Dữ kiện và lời giải được dùng nhất quán.

#### Các vấn đề

##### RL-01 — Quy ước trạng thái kết thúc chưa được khai báo trong HTML

- **Mức độ:** trung bình.
- **Trang chiếu:** L04-A03, B04, B07, D05, E03, E06.
- **Vấn đề:** HTML chưa xác định $\mathcal S$ có bao gồm trạng thái kết thúc hay không và chưa khai báo $\mathcal S^+$. Điều này làm miền của bảng giá trị, miền tổng theo $s'$ và số chính sách chưa thống nhất tường minh với Sutton–Barto, outline và note. Các ví dụ hiện tại vẫn cho kết quả đúng; đây là khoảng trống về miền/ký hiệu.
- **Bằng chứng:** A03, HTML dòng 34, chỉ ghi “Tập trạng thái $\mathcal S$”; B04, dòng 75, ghi $V:\mathcal S\to\mathbb R$; D05, dòng 190, đếm $\prod_{s\in\mathcal S}|\mathcal A(s)|$. E06 lại có $V(c_5)=0$ và trạng thái kết thúc không có hành động. Trong khi đó outline dòng 40–42 và note dòng 19–21 xác định $\mathcal S$ là các trạng thái chưa kết thúc, $s'$ chạy trên $\mathcal S^+$, bảng được mở rộng bằng 0. Quy ước này chưa có trong HTML, kể cả notes.
- **Đề xuất sửa:** Bổ sung tại notes A03 một đoạn ngắn đồng bộ với note: $\mathcal S$ gồm trạng thái chưa kết thúc, $\mathcal A(s)$ hữu hạn khác rỗng; nếu có kết thúc dùng $\mathcal S^+$ trong tổng theo $s'$, mở rộng mọi bảng bằng 0 tại đích. Nhắc ở B04 hoặc B07 rằng các bảng/ma trận có $|\mathcal S|$ thành phần chưa kết thúc. Không cần đưa cả bảng ký hiệu lên mặt trang.

##### RL-02 — Ví dụ theo chính sách ngẫu nhiên của kế hoạch chưa có trong HTML

- **Mức độ:** trung bình.
- **Trang chiếu:** L04-B01–B08; liên quan C03 và G03.
- **Vấn đề:** Toàn bộ phép tính trong mạch đánh giá chỉ dùng chính sách xác định và động lực xác định. Tổng theo $\pi(a\mid s)$ được phát biểu nhưng chưa được thực hiện bằng số. Lưới nhiễu G03 minh họa ngẫu nhiên của môi trường trong điều khiển, không thay thế việc minh họa trung bình theo chính sách. Đây cũng là phần cụ thể của kế hoạch đã không đi vào sản phẩm.
- **Bằng chứng:** Outline dòng 174 dự kiến rõ: “Ví dụ phụ cho chính sách ngẫu nhiên đều: từ bảng không, $V_1(s_0)=0.5(1)+0.5(0)=0.5$, $V_1(s_1)=0.5(2)+0.5(3)=2.5$.” Notes B03 chỉ nói “Kỳ vọng bao gồm ngẫu nhiên của chính sách và môi trường” rồi quay lại hai phương trình xác định. B08 tiếp tục kiểm tra $\pi_0=(a,a)$; G03 dùng phép cực đại trên hành động.
- **Đề xuất sửa:** Khôi phục ví dụ phụ đã duyệt trong notes B03 hoặc B04, ghi rõ chính sách mới có xác suất $1/2$ cho mỗi hành động và vẫn giữ nguyên mô hình, $\gamma=0{,}9$. Có thể thay một ý của câu kiểm tra B08 bằng việc giải thích hoặc tính trung bình này. Không cần thêm MDP hay trang mới; điều chỉnh vài chục giây trong mạch B nếu dùng trên lớp.

##### RL-03 — Cơ chế bootstrapping có nhưng chưa được nhận diện bằng thuật ngữ

- **Mức độ:** nhẹ.
- **Trang chiếu:** L04-B01–B04, G01/G05; ghi chú chuyên sâu phần 3 và 7.
- **Vấn đề:** Học liệu giải thích dùng giá trị tiếp nối, nhưng không gọi tên bootstrapping hoặc phân biệt đặc điểm này với yêu cầu có mô hình. Vì vậy cầu nối từ quy hoạch động sang các phương pháp học từ trải nghiệm còn thiếu một thuật ngữ có sẵn trong nguồn.
- **Bằng chứng:** B01 ghi “Một bảng giá trị hiện có ước lượng phần thưởng về sau”. Nguồn tr. 12 ghi “backup và bootstrapping”; Sutton–Barto §4.8, tr. 89, tách việc cập nhật từ ước lượng khác với việc cần mô hình chính xác. `bootstrap` không xuất hiện trong nội dung công khai của deck hoặc note; outline dòng 729 vẫn ánh xạ nội dung này sang A03/B01/F05.
- **Đề xuất sửa:** Thêm tên thuật ngữ vào đúng cơ chế đã có ở B04: cập nhật xây mục tiêu từ ước lượng giá trị của trạng thái kế tiếp là bootstrapping. Trong notes G01 hoặc G05, nêu rằng đây là một đặc điểm riêng với yêu cầu biết mô hình. Không cần dạy trước Monte Carlo hoặc học sai phân thời gian, cũng không thêm công thức của bài sau.

##### RL-04 — Mục tiêu lựa chọn cách tính chưa có tình huống đánh giá trực tiếp

- **Mức độ:** nhẹ.
- **Trang chiếu:** L04-A02, F01–F06, G02–G04.
- **Vấn đề:** A02 yêu cầu “Chọn cách tổ chức tính toán phù hợp”, nhưng các câu kiểm tra phần cuối chủ yếu phát hiện dữ kiện/điều kiện thiếu hoặc kiểm chứng một bảng đã cho. G02 mô tả ba cơ chế và cách kiểm đầu ra, chưa yêu cầu chọn một cách dựa trên chi phí hoặc nhu cầu tính toán.
- **Bằng chứng:** F06 hỏi về lịch bỏ $s_1$ và mô hình CartPole còn thiếu; G04 yêu cầu tính $Q_V$, phần dư và nhận diện giới hạn của bộ mô phỏng. G02 có tiêu đề “Lựa chọn phương pháp và điều kiện áp dụng”, nhưng bảng chỉ có “Tổ chức cập nhật” và “Kiểm tra đầu ra”.
- **Đề xuất sửa:** Thêm một tình huống ngắn vào câu kiểm tra sẵn có hoặc 30 phút chữa bài: một lượt quét toàn bảng quá tốn nhưng vẫn có mô hình đầy đủ; yêu cầu chọn lịch cập nhật và nêu điều kiện bao phủ cùng cách kiểm phần dư. Câu trả lời dựa trực tiếp F01–F03. Nếu không muốn thêm câu, thu hẹp mục tiêu A02 thành “So sánh các cách tổ chức tính toán”. Không gán một phương pháp luôn nhanh hơn.

##### RL-05 — Thuật ngữ còn đổi từ đồng nghĩa giữa deck và note

- **Mức độ:** nhẹ.
- **Trang chiếu:** L04-A01, F01; ghi chú chuyên sâu mở đầu, phần 1, 2 và 5.
- **Vấn đề:** Detect của no-ai-slop ghi nhận mẫu **Synonym cycling — đổi từ đồng nghĩa không cần thiết** ở các tên đối tượng chuyên môn. Điều này chưa làm sai công thức nhưng không khớp câu khẳng định “Ký hiệu và thuật ngữ thống nhất với bộ trang chiếu”.
- **Bằng chứng:** A01 dùng “Quá trình quyết định Markov”, còn note dòng 5, 13, 202 dùng “quy trình quyết định Markov”. Deck F01 dùng “mô hình đặc”; note dòng 441 dùng “mô hình dày”. Note dòng 44, 109 dùng “tất định”, còn cùng note và deck dùng “xác định” ở các đoạn khác.
- **Đề xuất sửa:** Chọn một thuật ngữ cho mỗi đối tượng theo bảng thuật ngữ của học phần rồi đồng bộ deck, note và planning; giữ phân biệt giữa chính sách xác định với động lực chuyển xác định. Đây là sửa thuật ngữ, không phải lý do đổi cấu trúc hoặc giản lược chứng minh.

#### Bao phủ chuyên môn và chiều sâu

| Cụm | Phạm vi đã rà | Kết quả |
|---|---|---|
| Mô hình và vấn đề | A01–A05 | Có mô hình chung chuyển–thưởng, Markov, quan sát đầy đủ trong notes, thưởng bị chặn và chiết khấu; dữ kiện hai trạng thái khớp nguồn. Bổ sung miền theo RL-01. |
| Đánh giá | B01–B08 | Đủ vấn đề, hai lượt tay, Bellman, toán tử, thuật toán, co, phần dư và kiểm tra. Trả đúng bảng đã đo phần dư. Thiếu ví dụ chính sách ngẫu nhiên theo RL-02. |
| Cải thiện | C01–C07 | Phân biệt chọn một hành động rồi theo chính sách cũ với đổi chính sách lâu dài; giá trị 12,9 không bị gọi nhầm là 30. Định lý và phác thảo đơn điệu/co có giả thiết. |
| Lặp chính sách | D01–D06 | Có đủ chuỗi $(a,a)\to(a,b)\to(b,b)$, đánh giá chính xác, giữ hòa, ngân sách và cặp đầu ra nhất quán. Phản ví dụ ổn định theo $V=0$ bác đúng kết luận tối ưu thiếu căn cứ. |
| Lặp giá trị | E01–E08 | Ví dụ trước toán tử; $Q_V$ khác $q_\pi$; cực đại ngoài kỳ vọng; kiểm phần dư đúng bảng; giá trị đích 0; bảng lưới và chứng nhận $V_5=V_4$ đúng. |
| Bất đồng bộ, GPI, giới hạn | F01–F06 | Phân biệt tại chỗ với lịch tổng quát; bảo đảm mọi trạng thái được cập nhật vô hạn lần có giới hạn “giá trị mới nhất”; GPI không bị coi là bảo đảm cho mọi xen kẽ. Chi phí và giới hạn gộp CartPole phù hợp. |
| Kết luận và luyện tập | G01–G05 | Thu hồi nghiệm và điều kiện, bài nhiễu đúng trọng số/thưởng thực tế, phân biệt mô hình đầy đủ với bộ mô phỏng sinh mẫu. Tài liệu đọc đúng chức năng. |
| Ghi chú chuyên sâu | Phần 1–7 | Bộ số riêng đã khai báo; $(4,7)\to(4,20)\to(9,20)$ và lưới thưởng 24 đúng. Chứng minh khả nghịch, cải thiện, co/Banach và tối ưu trên lớp chính sách có lịch sử được giữ; không cần chuyển lên mặt slide. |

Mô hình đầy đủ được phân biệt với mẫu ở B01 và G04. Dự đoán/điều khiển, $v_\pi/q_\pi$, giá trị thật/bảng ước lượng, vòng chính sách/lượt cập nhật/bước tương tác đều được phân biệt đúng. Không cần đưa phân loại theo chính sách/khác chính sách vào đây vì thuật toán đang dùng kỳ vọng trực tiếp từ mô hình, không có chính sách hành vi sinh tập mẫu cần hiệu chỉnh. Các nội dung mạng mục tiêu, bộ nhớ phát lại hoặc học sâu không thuộc phạm vi nguồn.

Quan hệ với nền tảng học máy được thể hiện ở sự khác nhau giữa dự đoán giá trị và tối ưu quyết định, cùng phân biệt dữ liệu mẫu với mô hình. Bài chưa mở một thuật toán học từ dữ liệu mới; điều đó phù hợp phạm vi. RL-03 làm rõ thêm cơ chế ước lượng nối sang các bài sau mà không tăng phạm vi thuật toán.

#### Thời lượng, văn phong và giới hạn của báo cáo

Phân bổ $10+22+20+18+22+16+12=120$ phút phù hợp 45 trang có ví dụ tính tay và kiểm tra theo cụm. Tổng 150 phút giữ 30 phút chữa bài; không có căn cứ tạo code demo từ nguồn. G03 chỉ dành ba phút cho lập kỳ vọng tại ô sát đích và dành lời giải toàn bài cho phần chữa bài, như outline ghi; không nên diễn giải ba phút là đủ chữa toàn bộ lưới. Đây là đánh giá kế hoạch, chưa phải dữ liệu đo từ một buổi dạy thử.

Detect không phát hiện lời dẫn rỗng, lời ca tụng, câu hỏi tu từ hoặc chỉ dẫn điều phối cần coi là lỗi nghiêm trọng trong HTML/notes đã đọc. Câu hỏi tính toán và phần tổng hợp có chức năng học tập nên được giữ. Vấn đề thuật ngữ được ghi riêng tại RL-05; không dùng điểm phát hiện AI hay suy đoán tác giả.

Đây là rà nội dung từ mã HTML, văn bản và ngữ nghĩa SVG. Chưa duyệt toàn bộ ảnh render ở 16:9 hoặc màn hình hẹp; không chứng nhận khả năng đọc, tràn trang, KaTeX hay Codex Slides. Năm hình cũ chỉ phục vụ ghi chú chuyên sâu nằm ngoài bộ 18 tệp cố định; báo cáo không nhận là đã kiểm lại hình học/render của chúng. Không đọc báo cáo của các reviewer khác hoặc `root-review` để duy trì tính độc lập.


### Báo cáo 3/5 — Độ chính xác toán học và thuật toán

### Rà độc lập độ chính xác toán học và thuật toán — Bài 04

Tác tử: `/root/lec04_review_math`. Vai trò: chỉ đọc, rà định nghĩa, giả thiết, ký hiệu, chứng minh, thuật toán, số liệu và nhãn hình. Ngày rà: 28-09-2026. Không chỉnh tệp sản phẩm, không đọc báo cáo của bốn reviewer khác hoặc báo cáo rà của điều phối viên, không tạo tác tử, không dùng OpenRouter/API hoặc tệp môi trường.

#### Phạm vi và bản đã rà

- Đọc toàn bộ 45 trang và 45 ghi chú của `2627-1/lecture-04-giai-mdp-bang-quy-hoach-dong.html`; đọc toàn bộ `2627-1/materials/lec-04/lecture-note.md`.
- Đọc nhãn, mô tả và kiểm tra quan hệ mũi tên liên quan của 10 SVG `dp04-*.svg`. Đối chiếu bảng thuật ngữ, các mô tả toán học/thuật toán và ánh xạ liên quan trong `outline.md`, `storyboard.md`, `analysis.md`.
- Đối chiếu bản trích nguồn tại `/tmp/rl04-rebuild/source.txt`, các đoạn chương 4 trong `book.txt`, cùng hồ sơ `research.md`, `source-report.md`, `numeric-report.md`. Tự tính lại bằng `fractions.Fraction`; báo cáo số trước đó chỉ dùng để đối chiếu sau phép tính độc lập.
- Đã đọc `AGENTS.md` và `/home/tqlong/.codex/skills/no-ai-slop/SKILL.md`; áp dụng Detect cho cách diễn đạt các mệnh đề toán học. Không dùng điểm phát hiện AI hoặc suy đoán tác giả.
- SHA-256 HTML: `9047c8619836c14ca7ed015925095c0d98da73eee1ed25c5e4b13f63cc8a387d`.
- SHA-256 ghi chú: `0fe241676026a5b227f705e4e28958e496f2841482673e8c3b4e3af38682ad5d`.
- Kiểm tra đủ 18 mục trong `/tmp/rl04-rebuild/frozen-review.json` trước và sau lượt rà: không mục nào đổi hash.

Đọc bổ sung năm SVG được chính ghi chú nhúng: `two-state.svg`, `policy-evaluation.svg`, `gridworld.svg`, `convergence.svg`, `cartpole.svg`. Chúng không nằm trong danh sách đóng băng 18 tệp; chỉ xác nhận nhãn toán học tại thời điểm đọc, không coi là đã được kiểm chứng bất biến bởi manifest đó.

#### Kết luận

Không phát hiện lỗi **chặn bàn giao** hoặc **nghiêm trọng** về toán học/thuật toán. Công thức Bellman, chứng minh cải thiện, tính co, tồn tại chính sách tối ưu, phần dư, giả mã chính trên trang chiếu và toàn bộ kết quả số đã kiểm đều đúng dưới các giả thiết được trình bày.

Có **2 điểm trung bình** về tính tường minh/nhất quán giữa các học liệu và **1 điểm nhẹ** về cách phát biểu điều kiện đủ. Các điểm này không phủ nhận tính đúng của ví dụ, chứng minh hoặc từng biến thể thuật toán riêng.

#### Phát hiện

##### M01 — Miền trạng thái kế tiếp chưa được khai báo trong HTML

- **Mức độ:** trung bình.
- **Trang chiếu/vị trí:** L04-A03, HTML dòng 33–36; L04-B04 dòng 75–76; L04-B07 ghi chú dòng 99; liên quan L04-D05 dòng 190 và các bài lưới có kết thúc. Đối chiếu `outline.md` dòng 40–45 và `lecture-note.md` dòng 19–21, 202–214.
- **Vấn đề:** HTML chưa xác định rõ $\mathcal S$ chỉ gồm trạng thái chưa kết thúc và miền của tổng theo $s'$ là $\mathcal S^+$. Ghi chú bài giảng và bảng ký hiệu trong outline đã làm đúng điều này, nhưng quy ước chưa được đưa vào deck. Nếu người học dùng $s'\in\mathcal S$ theo miền của bảng $V:\mathcal S\to\mathbb R$ mà HTML đã viết, phần thưởng của chuyển vào đích có thể bị bỏ khỏi tổng. Nếu hiểu $\mathcal S$ gồm đích có tập hành động rỗng, tích đếm chính sách ở D05 lại không còn có nghĩa như dự định.
- **Bằng chứng:** A03 chỉ viết “Tập trạng thái $\mathcal S$ và tập hành động $\mathcal A(s)$ hữu hạn” và “$S_t\in\mathcal S$”; B04 định nghĩa $V:\mathcal S\to\mathbb R$ rồi dùng $\sum_{s',r}$ không chỉ miền. B07 dùng $n=|\mathcal S|$, ma trận $n\times n$ và tổng phần thưởng theo $s',r$ nhưng chưa nói hàng ma trận có tổng không vượt 1 khi loại đích. Ngược lại, ghi chú dòng 21 đã định nghĩa $\mathcal S^+$ và mở rộng $V$ bằng 0; dòng 208 tính thưởng trên $\mathcal S^+$, dòng 214 dùng tổng hàng $P_\pi\le1$.
- **Phân biệt mặt trang/ghi chú:** HTML đã giải thích đúng $V(s_{\mathrm{term}})=0$, vẫn tính thưởng khi đi vào đích, và không cực đại trên tập hành động rỗng tại B03/E03. Vì vậy đây là thiếu khai báo miền, không phải sai quy ước thưởng kết thúc trong lời giải.
- **Đề xuất sửa:** thêm ngắn vào ghi chú A03 quy ước $\mathcal S$ chưa kết thúc, $\mathcal A(s)$ hữu hạn khác rỗng, $\mathcal S^+$ có thêm đích và miền các tổng; tại B04 nhắc mở rộng $V(s_{\mathrm{term}})=0$. Ghi chú B07 có thể bổ sung $P_\pi$ chỉ chuyển giữa trạng thái chưa kết thúc, còn $r_\pi$ tính cả chuyển vào đích. Không cần thay công thức hoặc các bảng số.

##### M02 — Cùng ký hiệu ngân sách nhưng hai học liệu trả bảng ở các thời điểm khác nhau

- **Mức độ:** trung bình.
- **Trang chiếu/vị trí:** L04-B05, HTML dòng 82–85; L04-E04 dòng 228–232; `lecture-note.md` dòng 237–242 và 414–421.
- **Vấn đề:** Deck định nghĩa $K$ là số lần nhận bảng mới; ghi chú đánh giá trả $W$, còn ghi chú lặp giá trị tính $W$ nhưng có thể trả $V$ trước khi nhận nó. Những quy trình này đều có chặn đúng riêng, nhưng người đọc chưa được báo rõ rằng ghi chú đang trình bày biến thể có quy ước đếm và trả bảng khác deck. Cùng $K$ có thể cho số cập nhật đã nhận khác nhau.
- **Bằng chứng:** B05 ghi “tối đa $K$ lượt nhận bảng mới” và nếu đạt ngưỡng thì “trả $(V,b)$”; khi hết ngân sách tính lại phần dư của bảng cuối. Ghi chú dòng 240 ghi “nếu $b_\pi(V)\le\eta$, trả $W$” và dòng 242 nêu đúng chặn $\gamma b_\pi(V)/(1-\gamma)$. E04 nhận tối đa $K$ bảng rồi kiểm bảng cuối; ghi chú dòng 419 khi hết $K$ lượt lại trả “chính bảng $V$ đã kiểm”, chưa nhận $W$. Với $K=1$ và ngưỡng chưa đạt ở $V_0$, E04 trả $V_1$, còn quy trình ghi chú trả $V_0$ sau lần tính đầu.
- **Phân biệt sai toán với khác quy ước:** Không có chặn sai số sai ở dòng 242/597: chặn cho $W$ đã được chứng minh đúng. Deck cũng đo phần dư trên đúng bảng trả. Điểm cần sửa là sự khác nhau chưa được đặt tên và quy ước đếm lượt trong ghi chú chưa đủ tường minh khi đọc cùng deck.
- **Đề xuất sửa:** ưu tiên dùng chung quy ước ngân sách của deck trong các thủ tục chính. Có thể giữ nguyên chứng minh cho $W=T_\pi V$ như một biến thể trả bảng mới. Nếu giữ hai thủ tục khác nhau, thêm câu xác định rõ ở ghi chú: $K$ đếm phép áp dụng toán tử hay số lần nhận bảng, số lần cập nhật tối đa và bảng được trả khác thủ tục trên trang chiếu như thế nào. Không cần đổi bộ số $\gamma=0{,}5$.

##### M03 — Dùng “cần” ở điều kiện vốn chỉ đủ để bảo đảm sai số

- **Mức độ:** nhẹ.
- **Trang chiếu/vị trí:** `lecture-note.md` dòng 622, lời giải phần 6(b); cùng cách viết trong `outline.md` dòng 519.
- **Vấn đề:** Câu về ngưỡng có thể được đọc thành điều kiện cần của sai số thực, trong khi lập luận chỉ cho một điều kiện đủ qua chặn phần dư.
- **Bằng chứng:** “Muốn bảo đảm $e\le0{,}2$ cần $b_*(V)\le\cdots=0{,}1$, tức phải lặp thêm…” Trong chính ví dụ hai trạng thái của ghi chú, bảng $V=(9{,}15;19{,}85)$ có $e=0{,}15\le0{,}2$ nhưng $b_*(V)=0{,}225>0{,}1$; do đó không thể suy ngược từ sai số nhỏ sang ngưỡng phần dư này. Đoạn trước đã nhận xét đúng rằng sai số thực có thể nhỏ hơn chặn.
- **Đề xuất sửa:** dùng “Một điều kiện đủ để bảo đảm bằng chặn này là…”; nếu giữ yêu cầu tiếp tục lặp, ghi rõ mục đích là đạt chứng nhận theo chặn đang dùng. Không cần đưa phản ví dụ trên vào học liệu.

#### Những kiểm tra đã đạt

| Cụm | Kết quả kiểm độc lập |
|---|---|
| Mô hình và kỳ vọng | $p(s',r\mid s,a)$ là phân phối chung; công thức không tính thưởng hai lần. $R_{t+1}$ và $G_t$ nhất quán. Chính sách dừng, miền hành động và cách hiểu hành động đầu được ấn định đã có trong ghi chú. |
| $q_\pi$ và $Q_V$ | Phân biệt rõ giá trị theo chính sách với điểm nhìn trước từ bảng tùy ý. Quan hệ $Q_{v_\pi}=q_\pi$ được dùng đúng; bảng trung gian của VI không bị gọi là giá trị chính sách. |
| Đánh giá | Nghiệm chính xác $(10,11)$ và $(4,7)$; các lượt đồng bộ, tại chỗ và phần dư đều đúng. Dạng ma trận trong ghi chú xử lý đúng xác suất chuyển vào đích và tổng hàng không vượt 1. |
| Cải thiện và PI | Giá trị cũ được giữ cố định trong toàn bước cải thiện. Chứng minh đơn điệu, tăng nghiêm tại trạng thái đổi và lập luận hữu hạn có giữ hòa đều đúng. Phân biệt đánh giá chính xác với đánh giá gần đúng, và trả cặp chính sách–giá trị cùng chính sách. |
| Hai chuỗi PI | Deck: $(10,11)\to(10,30)\to(27,30)$; ghi chú: $(4,7)\to(4,20)\to(9,20)$. Đã giải cả bốn chính sách xác định của mỗi bộ số bằng khử Gauss hữu tỉ và đối chiếu các điểm hành động. |
| VI và phần dư | Deck: $V_1=(1,3)$, $V_2=(2{,}7;5{,}7)$, phần dư tại $V_1$ bằng $2{,}7$, sai số bằng $27$. $V_{55}\approx(26{,}9087024183;29{,}9087024183)$, phần dư $0{,}00912975817$, sai số $0{,}0912975817$. |
| Lưới xác định | Deck: các bảng $k=0\ldots5$, nghiệm $(4{,}58;6{,}2;8;10;0)$ và bốn điểm đi trái đều đúng. Ghi chú: các bảng $k=0\ldots5$, nghiệm $(1{,}25;4{,}5;11;24;0)$, phần dư của $V_3$ bằng 3 đều đúng. Hai lịch ngược tại chỗ đạt đúng nghiệm trong một lượt từ bảng 0 của từng ví dụ. |
| Lưới ngẫu nhiên | Xác suất mỗi hành động cộng bằng 1; thưởng gắn chuyển thực tế. $V_1=(-1;-1;-1;7{,}8;0)$; hai điểm tại $c_3$ ở lượt hai là $-1{,}108$ và $4{,}436$. Các nhãn SVG khớp ba kết quả tại $c_4$. |
| Chứng minh hội tụ | Bất đẳng thức giữa hai cực đại, tính co và chặn phần dư đúng. Ghi chú chứng minh điểm bất động chặn cả chính sách phụ thuộc lịch sử bằng kỳ vọng theo $H_t$, rồi xây chính sách Markov dừng đạt cận; không gán $T_\pi$ dừng cho một chính sách phụ thuộc lịch sử. |
| Bất đồng bộ và GPI | Điều kiện mỗi trạng thái chưa kết thúc được cập nhật vô hạn lần, bảng mới nhất và $\gamma<1$ được nêu. Phần dư cuối đo khi cố định toàn bảng. GPI không bị dùng như bảo đảm cho mọi lịch xen kẽ gần đúng. |
| Chi phí và CartPole | $O(n^2m)$, $O(nmd)$, $O(n^2)$ đánh giá xác định và $O(n^3)$ giải hệ đặc đều gắn với biểu diễn và thao tác thích hợp. Ghi chú tính thêm $O(nm)$ nếu lưu toàn bảng $Q_V$. $3\times3\times6\times6=324$ đúng; có phân biệt trạng thái gộp, tính Markov và mô hình còn thiếu. |
| Hình và nguồn | Không thấy nhãn thưởng, chiều chuyển, nhãn xác suất hoặc giá trị toán học sai trong các SVG đã đọc. Các mục đánh giá/cải thiện/PI/VI/bất đồng bộ/GPI đối chiếu được với Sutton–Barto chương 4; giữ hòa phù hợp vấn đề của Bài tập 4.4. |

#### Detect và giới hạn

Trong phạm vi các mệnh đề toán học và giải thích thuật toán, không phát hiện lời ca ngợi, khẳng định hội tụ/tối ưu thiếu điều kiện, suy đoán nguồn hoặc lời dẫn rỗng làm thay đổi nghĩa toán học. M03 là vấn đề độ chính xác của quan hệ điều kiện đủ, không phải bằng chứng về nguồn gốc văn bản.

Lượt rà này không thay kiểm tra trình duyệt, tràn trang, kích thước chữ, khả năng đọc công thức sau KaTeX hoặc rà sư phạm toàn tuyến. Không tuyên bố đã rà bằng Codex Slides. Các SVG được kiểm nhãn và cấu trúc quan hệ, chưa được duyệt trực quan ở mọi kích thước màn hình bởi vai này. Đã đọc toàn văn deck/note; không coi việc đối chiếu phần toán học của outline/storyboard là một lượt rà đầy đủ mạch viết của các hồ sơ đó.


### Báo cáo 4/5 — Phản biện học thuật và giảng dạy

### Rà độc lập: học thuật, giảng dạy và văn phong Bài 04

Vai: phản biện học thuật và giảng dạy Học tăng cường–lập kế hoạch, kết hợp `$no-ai-slop` Detect. Tác tử: `lec04_review_pedagogy`. Ngày rà: 2026-09-28.

#### Bản rà và phạm vi

- Bản cố định: `/tmp/rl04-rebuild/frozen-review.json`, 18 SHA-256. Kiểm đầu lượt khớp **18/18**. Chỉ băm byte của `review-log.md`, không đọc nội dung tệp này.
- Đã đọc toàn bộ **45 trang và 45 khối ghi chú diễn giả** trong `2627-1/lecture-04-giai-mdp-bang-quy-hoach-dong.html`, từ L04-A01 đến L04-G05; toàn bộ `2627-1/materials/lec-04/lecture-note.md`; nhãn, mô tả và nội dung văn bản của **10 SVG `dp04-*`**. Đối chiếu bản đồ khái niệm, danh mục hình thức hóa, chu trình và quyết định trong `analysis.md`, `outline.md`, `storyboard.md`.
- Đọc `AGENTS.md`, `no-ai-slop/SKILL.md`, `no-ai-slop/eval.md`, `quill/SKILL.md` và phần quy trình dàn ý/khái niệm liên quan. Áp dụng Quill để theo dõi tiên quyết, khái niệm được truyền và điểm khép lại; không khởi tạo dự án sách.
- Không đọc báo cáo của vai khác, `review-log.md` hoặc `root-review`. Không sửa sản phẩm. Báo cáo này không thay thế kiểm định bố cục trong trình duyệt.

#### Kết luận

**Không phát hiện lỗi chặn bàn giao hoặc nghiêm trọng trong phạm vi vai này.** Tuyến chính đi từ mô hình đã biết đến đánh giá, cải thiện, lặp chính sách, lặp giá trị, lịch cập nhật và kiểm chứng nghiệm. Các thuật toán chủ đạo có vấn đề, trực giác và bước tính tay trước quy trình. Những điểm còn lại là **3 mục trung bình, 3 mục nhẹ**, có thể sửa cục bộ mà không đổi sườn 45 trang.

Các phương trình được kiểm tra không có lỗi toán học đủ căn cứ để kết luận sai. Tuy nhiên, việc công thức đúng riêng lẻ không giải quyết ba vấn đề sư phạm dưới đây: hai học liệu dùng quy ước ngân sách khác nhau; bước chuyển từ đánh giá tại chỗ sang điều khiển bất đồng bộ còn ngầm; phần dư được hình thức hóa trước ví dụ định lượng của chính đại lượng đó.

#### Bảng phát hiện

Trong bảng, `HTML` là tệp trang chiếu, `note` là `materials/lec-04/lecture-note.md`; số dòng xác định vị trí trong bản cố định.

| Mã | Mức độ | Trang chiếu hoặc học liệu | Vấn đề | Bằng chứng | Đề xuất sửa |
|---|---|---|---|---|---|
| P01 | trung bình | L04-E04; note §5, dòng 414–421; liên quan L04-B05 và note §3, dòng 237–242 | Cùng ký hiệu ngân sách $K$ nhưng số lần nhận bảng và bảng trả khác nhau giữa slide và ghi chú. Hai quy trình có thể đều đúng; người học hiện phải tự phát hiện rằng chúng là hai biến thể. Đây là khác biệt có thể kiểm chứng khi thực hiện thuật toán. | E04: “tối đa $K$ lượt nhận bảng mới”; notes: “Nếu đã nhận đủ $K$ bảng mới, tính lại phần dư trên bảng cuối trước khi trả.” Note §5: “Một lượt gồm các bước sau” rồi “Nếu hết $K$ lượt: trả chính bảng $V$ đã kiểm”. Với $K=1$, ngưỡng chưa đạt và cùng bảng khởi tạo, note trả $V_0$ sau lần tính kiểm đầu; slide nhận $V_1$ rồi đo phần dư của $V_1$. Tương tự, B05 trả $V$ khi đạt ngưỡng, còn note §3 trả $W$ và sử dụng chặn có thêm hệ số $\gamma$. Note dòng 5 lại nói “Ký hiệu và thuật ngữ thống nhất với bộ trang chiếu.” | Ưu tiên thống nhất cách đếm $K$ và bảng trả với slide. Nếu giữ biến thể, nêu rõ ngay trước quy trình note rằng $K$ đếm phép tính kiểm thay vì số lần nhận bảng; phân biệt tên ngân sách và chỉ rõ biến thể trả $W$ của đánh giá. Giữ chặn tương ứng với đúng bảng; không chỉ thay tên $V/W$. |
| P02 | trung bình | L04-F02 → L04-F03; HTML dòng 270–285 | Cầu nối từ bài toán dự đoán sang điều khiển bị để ngầm. Bước tính tay được triển khai tại F02 dùng chính sách cố định, còn quy trình ở F03 dùng cực đại. Công thức F03 đúng, nhưng không phải phép tổng quát hóa trực tiếp của phép tính hai trạng thái vừa làm. | F02: “Đánh giá $\pi_0=(a,a)$ từ bảng $0$” và $V(s_1)\leftarrow2+0{,}9\cdot1=2{,}9$. F03: “Nhận $V(s)\leftarrow(T_*V)(s)$”. Câu về lưới ở cuối F02 chỉ nêu kết quả truyền trong một lượt; notes F02 chỉ cho bảng cuối $(4.58,6.2,8,10,0)$, chưa viết bước cực đại tại chỗ. | Gọi rõ ví dụ lưới ở F02 là **lặp giá trị tại chỗ**, rồi thêm một bước tay ngắn từ dữ kiện có sẵn, chẳng hạn cập nhật $c_4$ thành $10$ rồi $c_3$ thành $\max\{-1,8\}=8$. Nêu rằng lịch cập nhật là thành phần thay đổi, còn F03 chọn toán tử tối ưu để giải điều khiển. Không cần thêm trang hoặc mô hình mới. |
| P03 | trung bình | L04-B04 → L04-B06; kiểm tra L04-B08 | Phần dư và chặn sai số có công thức đúng nhưng thiếu ví dụ định lượng trước lần hình thức hóa đầu. B02 chuẩn bị hai bảng, song chưa chuyển chênh lệch giữa chúng thành đại lượng kiểm tra dừng. B05 đưa đồng thời chuẩn vô cùng, phần dư, ngưỡng và quy trình; phép tính phần dư cụ thể đầu tiên nằm trong câu kiểm tra B08. | B05: “Chuẩn vô cùng: $\|U-V\|_\infty=\max_s|U(s)-V(s)|$. Phần dư: $b_\pi(V)=\|T_\pi V-V\|_\infty$.” B06 nêu ngay chặn $b_\pi(V)/(1-\gamma)$. B02 chỉ có $V_1=(1,2)$, $V_2=(1{,}9;2{,}9)$; B08 mới yêu cầu “Tính $b_{\pi_0}(V_2)$ và chặn sai số của $V_2$.” | Dùng chính hai bảng B02 để dẫn vào B05: sau một phép cập nhật, độ lệch lớn nhất của $V_1$ là $0{,}9$; đây là độ không khớp với phương trình Bellman của bảng đang xét. Sau đó mới đặt tên chuẩn/phần dư. Nêu nhu cầu chuyển độ không khớp đo được thành sai số so với nghiệm chưa biết trước chặn B06. Có thể thay một câu hiện có; không cần đổi thứ tự toàn mạch. |
| N01 | nhẹ | L04-G03, caption HTML dòng 320; L04-E06, notes dòng 247 | **Interpretive metadiscourse / authorial metacommentary:** còn thông tin về công việc biên soạn trên sản phẩm học tập. Đây không phải chỉ dẫn điều hành lớp, nhưng không giải thích thêm mô hình cho người học. | G03: “Quy ước biên, thưởng theo chuyển thực tế và yêu cầu tính được bổ sung.” E06: “Quy ước đi trái ở $c_1$ giữ nguyên trạng thái hoàn thiện điều kiện biên chưa nêu trong nguồn.” | Giữ nguồn dẫn và quy ước toán học; đưa lời giải thích rằng người soạn đã bổ sung điều kiện vào hồ sơ quy trình. Trong notes chỉ cần giải thích tác dụng của điều kiện biên đối với chuyển tiếp. |
| N02 | nhẹ | L04-A01; note dòng 5, 13, 202, 305; các tệp kế hoạch | **Synonym cycling:** tên tiếng Việt của cùng khái niệm MDP chưa thống nhất giữa slide và học liệu. | A01: “Quá trình quyết định Markov (MDP)”; note: “quy trình quyết định Markov (MDP)”; outline và storyboard cũng dùng “quy trình”. | Chọn một tên đầy đủ theo bảng thuật ngữ học phần và dùng nhất quán. Không thay MDP hoặc ý nghĩa mô hình. |
| N03 | nhẹ | note §3, dòng 235 | **Throat-clearing opener / lời dẫn rỗng:** câu chỉ thông báo rằng danh sách sau sẽ xuất hiện, ngay dưới tiêu đề đã nêu quy trình. | “Quy trình đầy đủ gồm các thành phần sau.” | Bỏ câu; giữ nguyên danh sách đầu vào, khởi tạo, cập nhật và dừng. |

#### Kiểm tra toàn tuyến học thuật

| Phạm vi đã rà | Tiên quyết và bước chuẩn bị | Hình thức, thuật toán và kiểm tra | Kết luận của vai rà |
|---|---|---|---|
| A01–A05, 5 trang | Mô hình đã biết, mục tiêu điều khiển, trạng thái/hành động/thưởng; mô hình hai trạng thái và chính sách ban đầu; tổng thưởng là tiên quyết đã nhắc | A05 tính ba phần thưởng và phân biệt bảng thưởng với mô hình chuyển | Đầu vào đủ cho B. Không yêu cầu người học suy ra tối ưu từ phần thưởng tức thời. |
| B01–B08, 8 trang | B01 thiết lập tổng thưởng vô hạn và giá trị tiếp nối; B02 tính hai lượt trước $v_\pi,T_\pi$ | B03–B05 định nghĩa và quy trình; B06 nêu giả thiết co; B07 giải hệ; B08 kiểm cập nhật và phần dư | Đánh giá chính sách đặt đúng chỗ. Cần cầu nối riêng của phần dư theo P03; không cần đổi thuật toán. |
| C01–C07, 7 trang | Giá trị chính xác $(10,11)$ từ B; C01 phân biệt hành động đầu với chính sách tiếp nối; C02 tính $11$ và $12{,}9$ | C03 định nghĩa $q_\pi$; C04 quy tắc/định lý; C05 dùng đơn điệu và tính co đã có; C06 đánh giá lại; C07 kiểm lần chọn tiếp | Không nhầm $12{,}9$ với giá trị $30$ của chính sách mới. Chứng minh không dùng kết quả tối ưu chưa được thiết lập. |
| D01–D06, 6 trang | Chu kỳ đánh giá–cải thiện và chuỗi đủ ba chính sách xuất hiện trước giả mã | D03 có đầu vào, cặp đầu ra, giữ hòa, ngân sách; D04 chứng nhận ổn định; D05 hữu hạn có điều kiện; D06 phản ví dụ đánh giá gần đúng | Bellman tối ưu tại D04 xuất hiện để giải thích một chính sách đã ổn định, vì vậy có nhu cầu và ví dụ trước đó. Định lý được phát biểu ở đây, tính co tối ưu được chứng minh ở E05; notes đã chỉ rõ phần chứng minh sau, không giả làm chứng minh hoàn tất. |
| E01–E08, 8 trang | Giới hạn chi phí đánh giá đầy đủ; E02 thực hiện hai lượt cực đại trước $Q_V,T_*$ | E03 phân biệt $Q_V,q_\pi$; E04 quy trình; E05 co; E06 lưới; E07 phần dư; E08 terminal và bảng cũ | Cực đại đặt ngoài kỳ vọng. Quy ước giá trị terminal bằng 0 và thưởng khi vào đích nhất quán. Slide không dùng chính sách sớm ổn định làm bằng chứng bảng giá trị đã hội tụ. |
| F01–F06, 6 trang | Chi phí quét toàn mô hình, ví dụ tại chỗ, kết quả lưới ngược thứ tự | F03 quy trình từng trạng thái và điều kiện bao phủ; F04 GPI; F05 CartPole; F06 kiểm lịch/mô hình | Điều kiện dùng giá trị mới nhất và cập nhật mọi trạng thái vô hạn lần được nêu. GPI là khái niệm tổng hợp, không được dùng để bảo đảm mọi cách xen kẽ. Cần làm rõ đổi toán tử theo P02. |
| G01–G05, 5 trang | Trở lại đúng MDP mở đầu; so sánh các quy trình theo giả thiết; dùng lưới ngẫu nhiên có dữ kiện | G03 bài tập kỳ vọng; G04 kiểm bốn điểm nhìn trước, phần dư và mô hình; G05 đọc/bài tập | Kết luận thu hồi được bài toán mở đầu. Không đưa thuật toán trọng tâm mới. Ví dụ không chiết khấu được giữ ở đọc thêm với giới hạn giả thiết. |

Đếm độc lập xác nhận 45 mã duy nhất, 45 notes và 45 thời lượng trong outline khớp thứ tự HTML; tổng là **120 phút**. Khoảng 30 phút chữa bài được giữ ngoài tổng đó. Không thấy lý do học thuật phải thêm code demo.

Các phép tính đối chiếu trực tiếp gồm ba nghiệm đánh giá $(10,11)$, $(10,30)$, $(27,30)$; các lượt đầu lặp giá trị $(1,3)$, $(2{,}7;5{,}7)$, $(5{,}13;8{,}13)$; phần dư của $V_{55}$ khoảng $0{,}009129758$; và giá trị lưới nhiễu $V_2(c_3)=4{,}436$. Những kết quả này khớp nội dung đang rà. Đây là kiểm tra hỗ trợ lập luận sư phạm, không thay báo cáo toán độc lập.

#### Bao phủ ghi chú chuyên sâu và Detect

Ghi chú chuyên sâu đã được đọc đủ bảy phần, gồm các bài tập, gợi ý, lời giải và tài liệu tham khảo. Bộ số $\gamma=0{,}5$ khác bộ slide được khai báo rõ, nên không coi đó là sai số hoặc đổi nguồn ngầm. Phần 1 cho hai quỹ đạo và phép nhìn trước; phần 2 dùng kết quả ấy để giới thiệu $Q_V$ và mục tiêu tối ưu; phần 3 đánh giá; phần 4 cải thiện/lặp chính sách; phần 5 dùng bước tính lưới trước quy tắc lặp; phần 6 có ví dụ hai bảng trước chứng minh co và sau đó chứng minh điểm bất động là giá trị tối ưu; phần 7 thu hồi mô hình mở đầu. Chứng minh cải thiện trong note dùng đơn điệu và phần đuôi chiết khấu, nên không lệ thuộc vòng vào định lý Banach đặt sau. Điểm cần thống nhất với slide là P01.

Phạm vi Detect gồm tiêu đề, nội dung mặt trang, nhãn/mô tả của 10 SVG mới, 45 notes và toàn bộ ghi chú chuyên sâu. Các mẫu có bằng chứng được ghi tại N01–N03; không phát hiện khẩu hiệu, lời ca tụng, kết luận kịch tính hoặc lời hướng dẫn giảng viên kiểu “nhấn mạnh với sinh viên”. Các nhãn “Câu hỏi:”, câu lệnh tính/chứng minh và bước giả mã được giữ vì có chức năng học tập. Những câu phân biệt $V$ với $v_\pi$, thưởng terminal với giá trị terminal, chính sách với mô hình, hoặc chứng nhận chính xác với dừng gần đúng không bị coi là “binary contrasts” cần xóa: chúng bảo vệ phân biệt toán học của bài.

Tự đối chiếu yêu cầu Detect trong `eval.md`: mỗi mẫu phát hiện có tên, trích dẫn và đề xuất ngắn; không viết lại sản phẩm, không cho điểm phát hiện AI, không suy đoán tác giả. Không loại định nghĩa, giả thiết, kết quả hoặc phần tổng hợp chỉ vì cấu trúc của chúng lặp lại.

#### Tình trạng bàn giao của vai rà

Đề nghị điều phối viên quyết định xử lý P01–P03 và biên tập N01–N03. Các đề xuất dùng dữ kiện hiện có, không yêu cầu mở rộng sườn nguồn. Nếu sửa quy ước bảng trả/ngân sách, cần kiểm lại chặn sai số tương ứng; nếu sửa F02–F03 hoặc B04–B06, rà lại cụm và hai trang lân cận theo quy trình. Báo cáo này không tự chứng nhận đã hoàn tất các vai khác hoặc kiểm tra trực quan cuối.

Kiểm SHA-256 cuối lượt: **18/18 tệp khớp bản cố định**, không tệp sản phẩm nào thay đổi trong lượt rà. Chỉ tạo báo cáo `/tmp/rl04-rebuild/review-pedagogy.md`.


### Báo cáo 5/5 — Kết nối và mạch viết

### Rà độc lập 5/5 — Kết nối và mạch viết Bài 04

#### Phạm vi và phương pháp

- Tác tử: `lec04_review_flow`; vai chỉ đọc, không sửa học liệu.
- Bản rà: `2627-1/lecture-04-giai-mdp-bang-quy-hoach-dong.html`, đủ 45 trang từ L04-A01 đến L04-G05, cả nội dung hiển thị và ghi chú diễn giả. Đối chiếu `planning/lec-04/analysis.md`, `outline.md`, `storyboard.md` và quan hệ khái niệm với `materials/lec-04/lecture-note.md`.
- Đã đọc AGENTS.md, Quill SKILL.md và hai phần Outline/Threads của workflows.md; áp dụng vào chức năng phần, tuyến khái niệm, thuật ngữ và đầu vào–đầu ra. Không khởi tạo dự án sách hoặc `quill.json`.
- Đã đọc no-ai-slop SKILL.md; dùng chế độ Detect. Nhận xét dựa trên câu chữ cụ thể, không dùng điểm phát hiện AI hoặc suy đoán tác giả.
- Không đọc nội dung review-log, root-review hoặc báo cáo của các vai rà khác; không gọi mô hình ngoài, không tạo tác tử con, không đọc bí mật. Không chứng minh lại toàn bộ ghi chú, chạy trình duyệt hoặc rà bố cục thay vai sinh viên.
- SHA-256 đầu lượt: 18/18 tệp khớp `/tmp/rl04-rebuild/frozen-review.json`.

#### Kết luận

Tuyến chính xác định được và tiến triển: **mô hình đã biết → đánh giá → cải thiện → lặp chính sách → lặp giá trị → tổ chức cập nhật và giới hạn mô hình → kiểm chứng nghiệm**. Bảy mạch có chức năng khác nhau; mở đầu thiết lập bài toán, kết luận thu hồi nghiệm và các điều kiện chứng nhận. Không có phát hiện `chặn bàn giao` hoặc `nghiêm trọng` trong phạm vi mạch viết.

Có **2 phát hiện trung bình và 2 phát hiện nhẹ**. Hai điểm trung bình là tín hiệu đổi ví dụ tại E06–E07 và tín hiệu đổi toán tử tại F02–F03. Có thể sửa cục bộ, không cần thêm hoặc đổi thứ tự trang. Số trang theo mạch là 5, 8, 7, 6, 8, 6, 5; có 45 mã duy nhất; 45 mục thời lượng trong storyboard cộng đúng 120 phút.

#### Bản đồ A–G và ranh giới

| Mạch | Chức năng riêng | Đầu vào | Đầu ra cho mạch sau | Kết luận |
|---|---|---|---|---|
| A — mở đầu | Xác định bài toán điều khiển và dữ kiện dùng xuyên suốt | MDP, kỳ vọng, tổng chiết khấu | Bốn chuyển tiếp, $\pi_0=(a,a)$, $\gamma=0{,}9$; tổng hữu hạn chưa tính hết tương lai | Đủ: A03 nêu mục tiêu tối ưu; A04–A05 tạo nhu cầu đánh giá |
| B — đánh giá | Tính giá trị khi chính sách giữ cố định | Mô hình và chính sách từ A | $v_{\pi_0}=(10,11)$; phân biệt bảng lặp, nghiệm và phần dư | Đủ: giá trị này được dùng trực tiếp ở C01–C03 |
| C — cải thiện | Nối so sánh một hành động với thay đổi chính sách lâu dài | Giá trị chính xác từ B | $\pi_1=(a,b)$, $v_{\pi_1}=(10,30)$; việc đổi tiếp tại $s_0$ | Đủ: C06–C07 tạo nhu cầu lặp lại đánh giá và cải thiện |
| D — lặp chính sách | Ghép hai thao tác thành thuật toán điều khiển có điều kiện dừng | Đánh giá, cải thiện, co theo chính sách | Chuỗi chính sách, cặp tối ưu $(b,b),(27,30)$; giới hạn đánh giá gần đúng | Đủ: E01 nhận trực tiếp chi phí hoàn tất đánh giá |
| E — lặp giá trị | Gộp chọn hành động và cập nhật từ bảng bất kỳ | Cơ chế nhìn trước và giới hạn lặp chính sách | Toán tử tối ưu, phần dư, chính sách trích và lưới lan truyền | Đủ về tuyến; tín hiệu đổi mô hình ở E07 còn thiếu, xem F-01 |
| F — thực hành | Thay lịch tính, nhận diện điều kiện bao phủ và giới hạn biểu diễn | Các phép cập nhật đã học | Phân biệt đồng bộ/tại chỗ/bất đồng bộ; GPI; yêu cầu mô hình hữu hạn phù hợp | Đủ về chức năng; cần làm rõ đổi toán tử và nối tới CartPole, xem F-02/F-03 |
| G — kết luận và vận dụng | Thu hồi bài toán, đối chiếu cách kiểm chứng, vận dụng kỳ vọng | Nghiệm và các điều kiện từ B–F | Chứng nhận Bellman, bài tập lưới nhiễu, tài liệu tự học | Đủ: không mở thuật toán trọng tâm mới |

| Ranh giới | Bằng chứng đầu ra → đầu vào | Đủ/thiếu và tác động |
|---|---|---|
| A→B | A05 phân biệt tổng ba bước với tổng vô hạn; B01 mở bằng “tổng thưởng gồm vô hạn hạng” và phần tiếp nối | **Đủ.** Nhu cầu đánh giá có căn cứ từ chính quỹ đạo vừa tính |
| B→C | B07 cho $(10,11)$ và nêu dùng làm giá trị tiếp nối; C01 ghi lại đúng bảng này | **Đủ.** B08 kiểm cơ chế trước khi chuyển từ dự đoán sang điều khiển |
| C→D | C06 đánh giá chính sách mới; C07 tìm lựa chọn tiếp tại $s_0$; D01 nêu chính sách thay đổi thì giá trị tiếp nối thay đổi | **Đủ.** Chu trình lặp là nhu cầu phát sinh từ kết quả đã có |
| D→E | D03 yêu cầu đánh giá chính xác; D05–D06 giới hạn của dừng gần đúng; E01 nêu chi phí hoàn tất đánh giá rồi xây cập nhật cực đại | **Đủ.** E không dùng phản ví dụ D06 để suy ra hội tụ; E05 cung cấp bảo đảm riêng |
| E→F | E06–E08 cho phép quét đồng bộ trên lưới; F01 đếm chi phí một lượt và nêu khả năng phân bổ theo trạng thái | **Đủ.** F02 dùng lại lưới để giải thích thứ tự; thiếu tín hiệu bên trong F, không đứt ranh giới E→F |
| F→G | F06 kiểm lịch và mô hình; G01 thu hồi kết quả lập kế hoạch, G02 đặt lại các điều kiện cho từng phương pháp | **Đủ.** Giới hạn thực hành được giữ khi kết luận tối ưu |
| Mở bài→kết bài | A03 yêu cầu tối đa tổng thưởng tại mọi trạng thái; G01 trả $(b,b),(27,30)$; G04 yêu cầu kiểm $T_*V=V$ và giả thiết | **Đủ.** Kết luận trả lời bài toán mở đầu và đo khả năng kiểm chứng, không chỉ lặp mục lục |

#### Bảng phát hiện

| Mức độ | Trang chiếu/phạm vi | Vấn đề | Bằng chứng | Đề xuất sửa |
|---|---|---|---|---|
| Trung bình — F-01 | L04-E06→E07→E08; storyboard E06–E07 | Đổi từ lưới năm ô sang mô hình hai trạng thái nhưng thẻ ví dụ của E07 chỉ ghi $V_1$, làm mất tín hiệu về miền của bảng. Storyboard còn gọi đầu ra E06 là “bảng gần tối ưu” dù ghi chú E06 đã xác nhận điểm bất động. | HTML dòng 245–247 dùng $c_1,\ldots,c_5$, xác nhận $T_*V_4=V_4$ trong notes. Dòng 252 ghi “Bảng $V_1=(1,3)$” mà không nhắc mô hình; E08 quay lại bảng năm ô. Storyboard dòng 357/364: “Bảng gần tối ưu cần được kiểm chứng…”. **Vai trò:** E06 áp dụng lặp giá trị; E07 định lượng sai số. **Vào:** lưới đã đạt điểm bất động. **Ra:** bảng hai trạng thái còn sai số dù chính sách đã tối ưu. Quan hệ so sánh hai tình huống chưa hiện rõ. | Ghi rõ “Mô hình hai trạng thái: $V_1=(1,3)$” trên E07. Sửa câu nối storyboard để phân biệt lưới đạt điểm bất động với bảng xấp xỉ trong mô hình tiếp diễn. Có thể thêm một câu học thuật ngắn trong notes E07 nêu lại phép so sánh này; không cần đổi số hoặc thứ tự. **Ảnh hưởng lân cận:** giữ ví dụ lưới ở E06/E08, giữ nhu cầu phần dư từ E05; rà lại E05–E08 và F01. |
| Trung bình — F-02 | L04-F02→F03; storyboard đoạn sau bảng chu trình | Bước tính chính trên F02 là đánh giá tại chỗ theo $T_{\pi_0}$, còn quy trình F03 dùng $T_*$. Chưa nói rõ yếu tố được giữ là lịch dùng giá trị mới, còn toán tử đã đổi sang lặp giá trị. | F02 dòng 272 ghi “Đánh giá $\pi_0=(a,a)$” và kết quả $(1;2{,}9)$. F03 dòng 279 chuyển sang $V(s)\leftarrow(T_*V)(s)$. F02 có câu về lưới quét ngược nhưng không gọi đó là lặp giá trị. Storyboard dòng 39 ghi “Dữ kiện $(0,0)$, $(1,2)$ và thứ tự trạng thái được giữ trong quy trình F03”, chưa phân biệt hai toán tử. **Vai trò:** F02 tạo trực giác dùng bảng hiện có; F03 hình thức hóa thuật toán bất đồng bộ. **Vào:** cập nhật theo chính sách cố định. **Ra:** cập nhật tối ưu từng trạng thái. Thiếu cầu nối nêu chính xác thành phần thay đổi. | Gọi rõ ví dụ lưới cuối F02 là “lặp giá trị tại chỗ”; tại F03 nêu quy trình đang áp dụng cập nhật tối ưu $T_*$, còn thay bằng $T_\pi$ là đánh giá một chính sách cố định. Sửa câu về dữ kiện trong storyboard: ví dụ hai trạng thái truyền cơ chế đọc bảng mới; ví dụ lưới truyền quy tắc tối ưu và lịch $c_4,c_3,c_2,c_1$. Không đồng nhất đầu ra hai toán tử. **Ảnh hưởng lân cận:** bảo toàn F01→F02 về chi phí và F03→F04 về cách tổ chức; rà E08–F05. |
| Nhẹ — F-03 | L04-F04→F05 | Câu nối từ tổ chức cập nhật/GPI sang giới hạn mô hình CartPole có trong storyboard nhưng chưa xuất hiện trong nội dung học thuật của hai trang. | Storyboard dòng 411/418: “Khung thuật toán vẫn phụ thuộc một biểu diễn trạng thái và mô hình phù hợp.” F04 kết bằng điều kiện điểm ổn định và giới hạn GPI; F05 mở ngay với bốn biến liên tục. **Vai trò:** F04 tổng hợp thuật toán; F05 kiểm miền áp dụng. **Vào:** mọi lịch trên đã giả định mô hình hữu hạn. **Ra:** 324 ô chưa cung cấp mô hình Markov. Quan hệ vẫn suy ra được từ A03/F01, nhưng tín hiệu chuyển cấp từ thuật toán sang biểu diễn còn mờ. | Đưa quan hệ đã có trong storyboard vào câu mở F05 hoặc notes cuối F04: các cách tổ chức trên vẫn cần mô hình hữu hạn, trong khi CartPole có trạng thái liên tục. Giữ nguyên nội dung gộp trạng thái, không thêm lý thuyết rời rạc hóa. **Ảnh hưởng lân cận:** F06 tiếp tục kiểm đúng hai điều kiện độc lập; rà F02–F06/G01 và ranh giới F→G nếu sửa câu nối. |
| Nhẹ — F-04 | L04-A01/F01 và lecture-note, outline | Tên tiếng Việt của cùng đối tượng và cùng kiểu biểu diễn chưa thống nhất giữa deck và ghi chú. Đây là đổi từ đồng nghĩa không có chức năng toán học. | HTML dòng 20: “Quá trình quyết định Markov”; note dòng 5, 13, 202, 305: “quy trình quyết định Markov”. F01: “Đặc: xét mọi trạng thái kế tiếp”; note dòng 441: “mô hình dày”; outline dùng “mô hình đặc”. Note mở đầu tuyên bố “Ký hiệu và thuật ngữ thống nhất với bộ trang chiếu.” | Chọn một cách gọi xuyên bộ học liệu, chẳng hạn “quá trình quyết định Markov” và “mô hình đặc”; giữ “quy trình” cho các bước thuật toán. Không sửa dữ kiện hoặc chứng minh của ghi chú. **Ảnh hưởng lân cận:** chỉ đối chiếu các lần xuất hiện tương ứng, không cần thay cấu trúc. |

#### Chu trình học tập và các quan hệ được giữ

| Cụm | Vấn đề/trực giác | Ví dụ trước hình thức | Hình thức/quy trình | Ứng dụng và kiểm tra | Kết luận |
|---|---|---|---|---|---|
| Đánh giá | B01 từ tổng vô hạn ở A05 | B02 tính hai lượt với cùng bảng cũ | B03–B06; B05 đủ vòng lặp và phần dư | B07 giải hệ đối chiếu; B08 tính lượt tiếp và sai số | Đủ, không mở bằng toán tử |
| Cải thiện | C01 tách hành động đầu và chính sách tiếp nối | C02 so 11 với 12,9 | C03 định nghĩa; C04 quy tắc; C05 lập luận | C06 đánh giá chính sách mới; C07 cải thiện tiếp | Đủ; phân biệt 12,9 với 30 được giữ |
| Lặp chính sách | D01 cần đánh giá lại sau thay chính sách | D02 lần theo toàn chuỗi | D03 quy trình; D04–D05 dừng và tối ưu | D04 áp dụng chứng nhận; D06 phản ví dụ ổn định theo bảng sai | Đủ; D02 thêm đoạn cuối của chuỗi, không chỉ chép C06 |
| Lặp giá trị | E01 chi phí hoàn tất đánh giá | E02 hai lượt trên cùng mô hình | E03–E05; E04 quy trình | E06 lưới; E07 sai số; E08 cập nhật và kết thúc | Đủ; sửa tín hiệu mô hình theo F-01 |
| Bất đồng bộ | F01 chi phí toàn bảng; F02 cơ chế đọc giá trị mới | F02 ví dụ tại chỗ và lưới quét ngược | F03 một trạng thái, lịch, phần dư, điều kiện hội tụ | F03 notes áp dụng lịch ngược; F06 phát hiện lịch bỏ trạng thái | Các bước có mặt; cầu nối toán tử cần F-02 |
| GPI | F04 dùng các thuật toán đã thực hiện làm ví dụ | PI/VI/bất đồng bộ đã có dữ kiện ở D–F | F04 định nghĩa khuôn tương tác | Phân loại ba cách tổ chức và điểm ổn định chung | Chu trình rút gọn hợp lệ vì là khái niệm hỗ trợ, không mở thuật toán mới |
| Mô hình gộp | F05 xét biểu diễn hữu hạn cho trạng thái liên tục | Bốn biến và 324 tổ hợp | Ánh xạ chỉ số khoảng trong notes | F06 chỉ ra mô hình còn thiếu | Chu trình rút gọn có lý do; cần tín hiệu vào theo F-03 |
| Mở đầu/kết luận | A thiết lập dữ kiện; G thu hồi bài toán | A04 và G03 là ví dụ có dữ kiện | A nhắc tiên quyết; G không thêm định nghĩa trọng tâm | A05 và G04 kiểm đúng năng lực đã chuẩn bị | Đủ; bài tập ngẫu nhiên dùng kỳ vọng đã được học |

D04 dùng kết quả Bellman tối ưu trước chứng minh co tối ưu E05, nhưng ghi chú D04 nêu rõ căn cứ sẽ được thiết lập khi xét lặp giá trị; C05 chỉ sử dụng tính co theo chính sách đã có ở B06. Đây là phát biểu định lý rồi bổ sung chứng minh, không phải suy luận vòng. A03 nhắc MDP trước A04 là khôi phục tiên quyết, không phải mở khái niệm trọng tâm mới bằng ký hiệu. F02 là ví dụ dẫn nhập được AGENTS.md cho phép; phát hiện F-02 liên quan phép nối ví dụ với đúng toán tử, không phản đối thứ tự ví dụ–trực giác.

#### Bao phủ từng trang

| Trang | Bước tiến trong mạch và quan hệ lân cận | Kết luận |
|---|---|---|
| A01 | Xác định chủ đề và mô hình đã biết để A02 nêu năng lực | Đủ |
| A02 | Nối các năng lực, đặt tiên quyết cho dữ kiện A03 | Đủ |
| A03 | Từ chủ đề đến bài toán tối ưu có giả thiết; A04 cụ thể hóa | Đủ |
| A04 | Cung cấp mô hình xuyên suốt và chính sách khởi đầu cho A05 | Đủ |
| A05 | Tính tổng cắt ngắn, để lại phần thưởng về sau cho B01 | Đủ |
| B01 | Tạo cơ chế thưởng một bước và giá trị tiếp nối trước B02 | Đủ |
| B02 | Hai lượt cụ thể chuẩn bị $v_\pi$ và toán tử | Đủ |
| B03 | Phân biệt nghiệm kỳ vọng với bảng lặp trước B04 | Đủ |
| B04 | Chuyển phương trình thành phép cập nhật; B05 tổ chức vòng lặp | Đủ |
| B05 | Nêu bảng đọc/ghi và phần dư; B06 giải thích ý nghĩa sai số | Đủ |
| B06 | Bảo đảm hội tụ có điều kiện, sau đó đối chiếu nghiệm nhỏ | Đủ |
| B07 | Tính $(10,11)$ làm chuẩn kiểm B08 và đầu vào C | Đủ |
| B08 | Kiểm thao tác và phần dư trước khi cho thay chính sách | Đủ |
| C01 | Dùng giá trị đã có để định nghĩa tình huống hành động đầu | Đủ |
| C02 | Hai lựa chọn trên cùng phần tiếp nối, tạo đối tượng $q_\pi$ | Đủ |
| C03 | Định nghĩa $q_\pi$ và trung bình $v_\pi$, làm căn cứ chọn | Đủ |
| C04 | Quy tắc chọn và định lý có giả thiết; C05 giải thích bảo đảm | Đủ |
| C05 | Đơn điệu cộng co truyền cải thiện một bước sang giá trị mới | Đủ |
| C06 | Áp dụng trên hai trạng thái, đánh giá lại để C07 dùng | Đủ |
| C07 | Lựa chọn đổi vì giá trị mới, tạo nhu cầu chu trình D | Đủ |
| D01 | Ghép đúng hai thao tác vừa học, phân biệt chỉ số | Đủ |
| D02 | Hoàn tất chuỗi và kiểm ổn định; thêm bước chưa có ở C | Đủ |
| D03 | Quy trình đầy đủ và cặp đầu ra nhất quán | Đủ |
| D04 | Nối ổn định chính xác với Bellman tối ưu và nghiệm ví dụ | Đủ |
| D05 | Giải thích dừng hữu hạn và giới hạn đánh giá gần đúng | Đủ |
| D06 | Phản ví dụ kiểm điều kiện dừng; E01 đề xuất quy tắc cắt ngắn có bảo đảm riêng | Đủ |
| E01 | Chỉ ra chi phí đánh giá và cơ chế cập nhật cực đại | Đủ |
| E02 | Tính trước công thức, đối chiếu cập nhật cố định chính sách | Đủ |
| E03 | Định nghĩa $Q_V,T_*$, phân biệt với $q_\pi$ | Đủ |
| E04 | Quy trình trả đúng bảng, chính sách và phần dư | Đủ |
| E05 | Cung cấp tính co tối ưu, đặt nhu cầu tiêu chuẩn đo được | Đủ |
| E06 | Mô hình có kết thúc thể hiện đường lan truyền | Đủ chức năng; F-01 ở câu nối ra |
| E07 | Chuyển chặn thành ngưỡng, tách giá trị và chính sách | F-01: cần gọi lại mô hình hai trạng thái |
| E08 | Kiểm đồng bộ và thưởng tại kết thúc, chuẩn bị bàn chi phí | Đủ |
| F01 | Đếm công việc của một lượt, tạo nhu cầu thay lịch | Đủ |
| F02 | Minh họa giá trị mới được dùng ngay và lợi ích của thứ tự | F-02: cần phân biệt toán tử của hai ví dụ |
| F03 | Khái quát lịch từng trạng thái và điều kiện bao phủ | F-02: cần nói rõ quy trình dùng $T_*$ |
| F04 | Tổng hợp cách tổ chức dưới GPI, không trùng D01 | Đủ; F-03 ở câu nối ra |
| F05 | Thử điều kiện mô hình trên CartPole và giới hạn gộp | F-03: thiếu tín hiệu nối vào |
| F06 | Kiểm lịch và mô hình, thu hồi hai giới hạn thực hành | Đủ |
| G01 | Trả lời bài toán mở đầu bằng nghiệm và cách kiểm | Đủ; tổng kết có chức năng học tập |
| G02 | Đối chiếu cách cập nhật và chứng nhận dưới cùng giả thiết | Đủ; khác F04 ở mục tiêu lựa chọn/kiểm đầu ra |
| G03 | Dùng kỳ vọng đã học cho chuyển tiếp ngẫu nhiên | Đủ; không thêm thuật toán |
| G04 | Kiểm chứng nghiệm gắn với giả thiết và phân biệt mô hình/mẫu | Đủ; khác D02 ở yêu cầu lập luận và giới hạn mô phỏng |
| G05 | Giao tài liệu và bài tập đã có tiên quyết, đóng tuyến | Đủ |

Không thấy trang chỉ có trang trí hoặc hai phần tranh cùng chức năng. Việc lặp dữ kiện $(27,30)$ ở D, G01 và G04 có ba vai trò khác nhau: tìm nghiệm, thu hồi mục tiêu, kiểm chứng chủ động.

#### Liên kết với ghi chú chuyên sâu

Đối chiếu theo khái niệm, không ép số hoặc số phần trùng slide:

| Nội dung deck | Vị trí trong ghi chú | Quan hệ |
|---|---|---|
| Mô hình, tổng thưởng, tiên quyết A | Phần 1 | Cùng đối tượng; note khai báo rõ bộ thưởng và $\gamma=0{,}5$ riêng |
| Đánh giá B | Phần 3; bảo đảm ở phần 6 | Cùng phương trình, bảng cũ/mới và ý nghĩa phần dư |
| Giá trị hành động/cải thiện C | Phần 2 và phần 4 | Cùng phân biệt hành động đầu với chính sách tiếp nối |
| Lặp chính sách D | Phần 4; tối ưu toàn cục ở phần 6 | Cùng đánh giá chính xác, giữ hòa, cặp chính sách–giá trị |
| Lặp giá trị E | Phần 5–6 | Cùng toán tử, terminal, trích chính sách và phần dư |
| Lịch/chi phí/CartPole F | Phần 3, 5, 6 | Note bổ sung tại chỗ, chi phí và sai số mô hình; không phải bản chép đủ phần GPI/bất đồng bộ của deck |
| Kết luận G | Phần 7 | Cùng phân biệt dự đoán/điều khiển và chứng nhận trên mô hình đã cho |

G05 liên kết đúng tên tài liệu; đầu ghi chú và mục tài liệu tham khảo đều công khai cấu trúc/bộ số độc lập. Note dùng $\sup$ trước khi chứng minh cực đại đạt được, trong khi deck phát biểu $\max$ với giả thiết hữu hạn chiết khấu; hai cách trình bày tương thích. Quy trình đánh giá trong note trả $W$ và nêu chặn $\gamma b_\pi(V)/(1-\gamma)$, khác quy ước deck trả $V$ và phần dư của $V$; note đã nêu rõ sự khác nhau và chứng minh chặn tương ứng. Không coi đây là lỗi đổi dữ kiện hoặc yêu cầu đồng bộ lại thuật toán. Điểm cần sửa liên kết chỉ là thuật ngữ F-04.

#### Detect no-ai-slop

Không phát hiện lời ca tụng, kết luận kịch tính, lời dẫn điều phối kiểu “tiếp theo chúng ta”, câu hỏi tu từ thay vấn đề học tập hoặc chuỗi trang tổng kết rỗng trong 45 trang và notes. Các đối chiếu toán học như $V_k$ với $v_\pi$, mẫu với mô hình, chính sách ổn định với tối ưu là phân biệt cần thiết; không đề xuất xóa theo quy tắc chống đối lập tu từ. Các nhãn “Câu hỏi:” và phần tổng hợp có chức năng đánh giá rõ.

Mẫu phát hiện cụ thể thuộc no-ai-slop là **Synonym cycling** tại F-04: “quá trình/quy trình quyết định Markov”, “mô hình đặc/dày”. Cách sửa là thống nhất tên, không làm mất phân biệt toán học. Hai phát hiện F-01/F-02 là thiếu tín hiệu nối khái niệm, không dùng chúng làm bằng chứng về tác giả hoặc nguồn gốc văn bản.

#### Tính toàn vẹn cuối lượt

Chỉ tạo báo cáo này trong `/tmp/rl04-rebuild/`; không chỉnh tệp được rà. Kết quả SHA-256 cuối lượt được ghi sau phép kiểm độc lập bên dưới.

Kiểm cuối lượt: **18/18 SHA-256 không đổi**, khớp toàn bộ danh mục cố định; không có tệp sai khác.


## Quyết định hợp nhất và sửa cục bộ — 2026-09-28

Điều phối viên chấp nhận cả năm báo cáo và giao `WRITE_FINAL` sau khi kiểm đủ 18 hash. Không vai nào phát hiện lỗi chặn bàn giao hoặc nghiêm trọng trong bản cố định; các mức trung bình và nhẹ dưới đây được sửa hoặc gộp. Giữ 45 mã và thứ tự, bảy mạch, 120 phút; không sửa CSS hoặc thư viện, không tạo raster/code demo, không đổi bộ số riêng hay năm SVG của ghi chú.

| Phát hiện | Mức độ | Quyết định | Vị trí và bằng chứng sửa |
|---|---|---|---|
| M01; RL-01 | trung bình | Chấp nhận, gộp | Notes A03 khai báo $\mathcal S$ chưa kết thúc, $\mathcal A(s)$ hữu hạn khác rỗng, $\mathcal S^+$ và giá trị đích 0. B04 nêu miền bảng/tổng; B07 nêu ma trận trên trạng thái chưa kết thúc, tổng hàng không vượt 1, thưởng tính cả chuyển vào đích. Không thay dữ kiện hay kết quả số. |
| M02; P01 | trung bình | Chấp nhận thống nhất quy trình chính theo deck | Note §3/§5: $K\ge0$ đếm số lần nhận bảng mới; bộ đếm $k$ tăng chỉ khi nhận $V\leftarrow W$; kiểm phần dư trên bảng cuối, kể cả $K=0$. Trả $V$ đã kiểm, và VI trích $\pi_V$ từ cùng bảng. Giữ chứng minh cho $W$ ở §6 như hệ quả/biến thể riêng; PI dùng $I_{\max}$ đồng nhất D03. Bảng ký hiệu và dẫn nội bộ đã đổi. |
| M03 | nhẹ | Chấp nhận | Note câu hỏi/lời giải §6(b), outline E07 và mặt E07 dùng “điều kiện đủ”; tiếp tục lặp nhằm đạt chứng nhận theo chặn, không khẳng định ngưỡng phần dư là điều kiện cần của sai số thật. |
| RL-02 | trung bình | Chấp nhận, đặt ở notes B04 | Sau toán tử, chính sách ngẫu nhiên đều trên cùng mô hình cho $(0.5,2.5)$ từ bảng không. Outline chuyển phép tính phụ từ dự kiến B03 sang B04 để không lẫn bảng một lượt với $v_\pi$. Không thêm trang/thời lượng. |
| RL-03 | nhẹ | Chấp nhận | Notes B04 gọi tên bootstrapping tại cơ chế dùng ước lượng tiếp nối; notes G01 và note §3/§7 phân biệt đặc điểm này với yêu cầu có mô hình để tính kỳ vọng. Không thêm thuật toán bài sau. |
| RL-04 | nhẹ | Chọn thu hẹp mục tiêu | A02 dùng “So sánh các cách tổ chức tính toán”, khớp MT6 và các câu kiểm tra hiện có; không thêm tình huống lựa chọn lên trang. Đồng bộ outline và đầu ra tổng hợp trong planning. |
| RL-05; N02; F-04 | nhẹ | Chấp nhận, gộp | Dùng “quá trình quyết định Markov”, “mô hình đặc”, “xác định”; note và planning đã đồng bộ. “Quy trình” vẫn dùng cho các bước thuật toán; không thay tên nguồn trích nguyên văn. |
| SV-01; F-01 | trung bình | Chấp nhận, gộp | E07 ghi “Mô hình hai trạng thái”, đưa $V_1$ vào thân; E08 ghi “Lưới năm ô”. Notes E07 và câu nối E06–E07 trong planning phân biệt lưới $V_4$ đã là điểm bất động với $V_1=(1,3)$ còn sai số. |
| SV-02; P02; F-02 | trung bình | Chấp nhận, gộp | F02 gọi rõ lặp giá trị tại chỗ, notes tính $c_4\leftarrow10$, $c_3\leftarrow\max\{-1,8\}=8$. F03 có tiêu đề “Lặp giá trị bất đồng bộ”, notes tách $T_*$ với $T_\pi$, đối chiếu $3$ với $2.9$ từ bảng $(1,0)$. Storyboard không còn nói đầu ra đánh giá truyền nguyên sang $T_*$. |
| SV-03; P03 | nhẹ / trung bình theo từng vai | Chấp nhận, gộp; ưu tiên ví dụ trước định nghĩa | Cuối notes B04 tính độ lệch lớn nhất $0.9$ từ $V_1=(1,2)$ và $V_2=(1.9,2.9)$, trước phần dư B05. Nêu nhu cầu liên hệ độ không khớp đo được với sai số; B05 nối tới tính co B06. Không lặp ví dụ trên mặt B05. |
| SV-04 | nhẹ | Chấp nhận | E06 và G03 ghi trái/phải; câu hỏi G03 xác định lặp giá trị đồng bộ từ $V_0=0$. Giữ thưởng theo chuyển thực tế, quy ước biên và mọi đáp án. |
| SV-05; N01; R05 | nhẹ | Chấp nhận, gộp | Caption G03 chỉ giữ “Dữ kiện: bài tập tuần 4”. Notes E06 nêu chuyển trái ở $c_1$ và thưởng $-1$, bỏ bình luận hoàn thiện nguồn. Quyết định bổ sung biên/yêu cầu đã nằm trong ánh xạ và storyboard. |
| N03 | nhẹ | Chấp nhận | Bỏ “Quy trình đầy đủ gồm các thành phần sau.” khi sửa note §3; danh sách thuật toán bắt đầu bằng dữ kiện cụ thể. |
| F-03 | nhẹ | Chấp nhận | Cuối notes F04 nêu các lịch vẫn cần biểu diễn hữu hạn và mô hình đã biết; CartPole có trạng thái liên tục nên còn cần xét gộp trạng thái. Outline/storyboard F04→F05 dùng cùng quan hệ. |

Vai sinh viên và vai mạch viết không coi biến thể trả $W$ trong note là lỗi toán; điều phối viên vẫn chọn thống nhất hai quy trình chính theo M02/P01 để người học không phải tự phân biệt cách đếm cùng ký hiệu $K$. Chứng minh đúng cho $W$ được giữ nguyên. Đây là quyết định đồng bộ học liệu, không ghi lại nhận xét của hai vai đó thành phát hiện toán học.

### Tự biên tập no-ai-slop — Edit của lượt sửa cuối

Tác tử chỉnh sửa đã đọc trực tiếp `SKILL.md` và `eval.md`, đọc tiêu đề, nội dung và notes của toàn bộ deck cùng ghi chú chuyên sâu trước khi sửa. Phạm vi biên tập là các đoạn được quyết định ở bảng trên, các câu liên quan trong outline/storyboard/analysis và nhãn SVG D01. Các mẫu có bằng chứng đã loại: bình luận biên soạn ở E06/G03 (N01/SV-05), câu dẫn rỗng trước danh sách note §3 (N03), đổi từ đồng nghĩa trong thuật ngữ (RL-05/N02/F-04). Không đổi giả thiết, dữ kiện, chứng minh đúng hoặc các phân biệt có chức năng toán học.

Tự đối chiếu trực tiếp toàn bộ nhóm kiểm trong `eval.md`:

| Nhóm kiểm | Kết quả của lượt sửa |
|---|---|
| 11 nguyên tắc biên tập: giữ ý, chi tiết, cấu trúc, mức cắt và câu cụ thể | Đạt: mọi thay đổi có finding/quyết định; dữ kiện hai bộ số được giữ; chỉ đổi quy tắc trả bảng ở hai quy trình đã duyệt. Câu trực tiếp dùng đối tượng, phép tính và điều kiện. Không ép cấu trúc câu đồng dạng. |
| Từ ngữ rỗng, nhấn mạnh thiếu căn cứ | Đạt: bỏ câu chỉ báo danh sách và bình luận biên soạn; không thêm khẩu hiệu, lời ca ngợi hoặc khẳng định hội tụ vượt giả thiết. |
| 9 mẫu diễn đạt và định dạng | Đạt: thuật ngữ ổn định, không lời dẫn tu từ/kết luận kịch tính, không bình luận cách đọc hay điều phối. Giữ đối chiếu $V/W$, $T_\pi/T_*$, chính sách/mô hình vì chức năng toán học; giữ nhãn định nghĩa, kết quả và Câu hỏi vì chức năng học tập. |
| Tự đọc cuối và sản phẩm bàn giao | Đạt trong phạm vi sửa: câu học thuật ngắn, có dữ kiện kiểm chứng; các bản sửa đầy đủ được ghi trực tiếp vào tệp, thay đổi được liệt kê trong bảng quyết định. Không dùng điểm bộ phát hiện AI hoặc suy đoán tác giả. |

Kết quả là tự kiểm của tác tử sửa, không thay báo cáo độc lập hoặc lượt kiểm ảnh sau sửa. Các trích đoạn chưa biên tập ở hồ sơ năm báo cáo được giữ như bằng chứng lịch sử, không phải nội dung công khai của bài.

### Rà Quill của lượt sửa cuối

Đã đọc Quill `SKILL.md`, Outline Workflow và Threads Workflow; chỉ áp dụng kiểm tiên quyết, khái niệm, thuật ngữ và quan hệ đầu vào–đầu ra, không tạo `quill.json`. Chuỗi A→B→C→D→E→F→G và các mục tiêu vẫn giữ nguyên. Những mối nối được làm rõ: B04 độ lệch số → B05 phần dư → B06 chặn sai số; E06 điểm bất động trên lưới → E07 sai số của mô hình tiếp diễn → E08 kiểm lưới; F02 cơ chế tại chỗ và ví dụ tối ưu → F03 lặp giá trị bất đồng bộ; F04 tổ chức tính toán → F05 điều kiện mô hình. Mô hình hai trạng thái, lưới xác định, lưới ngẫu nhiên và bộ số riêng của note đều có nhãn; không truyền lẫn bảng giữa các ví dụ.

### Phạm vi cần rà lại sau sửa

- Toán/thuật toán: notes A03/B04/B07 và lân cận; hai quy trình note §3/§5, ledger $K/I_{\max}$, chứng minh và câu hỏi/lời giải §6; đối chiếu B05/E04/D03. Kiểm $K=0$, $K=1$, dừng sớm và hết ngân sách để xác nhận đúng bảng trả.
- Mạch viết/sư phạm: B02–B08; E04–E08/F01; E08–F06/G01–G02, cùng bản đồ A–G. Số trang, thứ tự và thời lượng không đổi; câu nối và nhãn mô hình/toán tử có thay đổi nên cần rà lại ranh giới tương ứng.
- Trực quan: các mặt trang A02, E06, E07, E08, F02, F03, G03; D01 do nhãn SVG; các công thức mới trong notes và ghi chú cần kiểm KaTeX.
- Codex Slides: tác tử chỉnh sửa chưa thực hiện kiểm định. Browser tích hợp Codex không có trong phiên theo điều phối viên; việc kiểm trạng thái dự án, ảnh lưu và ứng dụng bằng Chromium cục bộ thuộc lượt điều phối tiếp theo, phải được ghi đúng phạm vi khi có bằng chứng.

Danh sách tệp sửa của lượt này: HTML Bài 04; `img/lec-04/dp04-policy-iteration.svg`; `materials/lec-04/lecture-note.md`; bốn tệp `planning/lec-04/{analysis,outline,storyboard,review-log}.md`. HTML đổi trực tiếp tại A02, A03, B04, B05, B07, E06, E07, E08, F02, F03, F04, G01, G03; D01 đổi tài sản hình. Không chạy lại tiện ích sinh HTML.


### Kiểm cơ bản trước nhả quyền ghi — 2026-09-28

- Đối chiếu bản trước sửa: đúng bảy tệp thay đổi trong manifest 18 tệp, gồm HTML, note, một SVG và bốn tệp planning. Index/CSS giữ nguyên hash; năm SVG cũ của note giữ nguyên hash. Các thư viện không thuộc phạm vi ghi của tác tử.
- HTML có 45 mã duy nhất, đúng thứ tự bản cố định, bảy section ngoài, 45 notes; không có đường dẫn cục bộ thiếu. Outline và storyboard khớp đủ 45 ID/thứ tự, mỗi tệp có 45 thời lượng cộng 120 phút. Mười SVG mới phân tích XML được và có role img.
- KaTeX cục bộ dựng 626 biểu thức HTML và 1.108 biểu thức note, không lỗi cú pháp. Có cảnh báo metric chữ Việt trong hàm text như lượt trước; việc duyệt hình/render thuộc lượt điều phối. Phép kiểm cú pháp không thay kiểm ngữ nghĩa toán học.
- Note giữ nguyên toàn bộ 50 công thức khối của bản cố định; bảy topic ID và số khối câu hỏi/gợi ý/lời giải/chứng minh không đổi. Chỉ các mô tả thuật toán, ký hiệu ngân sách và công thức nội dòng liên quan đã thay theo quyết định. Markdown dùng đúng dấu dollar cho công thức.
- Rà diff không thấy thay đổi ngoài phạm vi đã duyệt. Một lần viết hoa “Mô hình chuyển dày” còn sót được sửa thành “Mô hình chuyển đặc” sau thông báo PRODUCT_FROZEN và báo trước cho điều phối viên; không đổi toán. `git diff --check` không báo lỗi khoảng trắng.
- Sản phẩm đã cố định cho các lượt đọc sau sửa; chưa tự kết luận các báo cáo rà lại hoặc kiểm định trực quan cuối đã hoàn tất.

HTML SHA-256 sau sửa: `d9ebe94b97e63530e6b8cae8ae63102458f4392b217b621885f1ed9e00aff5b3`. Note SHA-256 cuối: `ff2077f17aa9ea3d081640f56de6422f08273abaef39a012f24d228806762838`. SVG chu trình lặp chính sách SHA-256: `2dba0580245918311cf12df6d32aa5edd2e7fbccee2d0341a6344f7ce92ec41c`.


### Sửa bố cục E06 sau kiểm ảnh — 2026-09-28

Điều phối viên phát hiện caption E06 ở khoảng y=669–700 trên ảnh 1280 × 720, chạm chân trang và mũi tên xuống dù còn nằm trong viewport. Theo `WRITE_LOCAL_LAYOUT`, tác tử chỉnh sửa chuyển nguyên đoạn caption từ cuối section vào cột phải, ngay sau bảng. Giữ nguyên chữ, công thức, notes, cỡ chữ, CSS, 45 ID/thứ tự và thời lượng; storyboard chỉ bổ sung vị trí caption. Kiểm so sánh xác nhận chuỗi nội dung sau bỏ thẻ/khoảng trắng và toàn bộ notes E06 không đổi; `git diff --check` sạch. Điều phối viên kiểm lại E06 ở hai viewport sau khi nhả quyền; tác tử sửa không tự ghi kết quả ảnh chưa thực hiện.


## Kết quả rà lại và kiểm định cuối — 2026-09-28

Điều phối viên đã chấp nhận năm báo cáo độc lập và bản sửa của tác tử chỉnh sửa riêng. Sau khi tác tử nhả quyền ghi, hai lượt chỉ đọc kiểm lại phần bị ảnh hưởng. Không coi các lượt có phạm vi này là một lượt rà mới toàn bộ bài.

| Tác tử | Cấu hình được chỉ định | Phạm vi và bằng chứng | Kết luận |
|---|---|---|---|
| lec04_recheck_math | gpt-6-astra, xhigh, fork_turns: none; công cụ tác tử gốc | A01–A05, B01–B08; B05/D03/E03–E04 đối chiếu note §3–§6; F01–F05 và lưới E06–E08; SVG D01. Kiểm bằng phân số hữu tỉ 140 trường hợp ngân sách/ngưỡng, hai trường hợp $\gamma=0$, sáu trường hợp ngân sách lặp chính sách. | Đóng M01–M03, P01–P03 trong phạm vi toán học; không phát hiện vấn đề toán mới còn mở. |
| lec04_review_flow — lượt rà lại | Cấu hình Astra/xhigh của lượt gốc được giữ khi tiếp tục nhiệm vụ | A01–A04, B01–B07 và ranh giới B08/C01, E04–G05; đối chiếu chức năng, đầu vào–đầu ra, câu nối trong outline/storyboard và quan hệ khái niệm với note. | Đóng F-01–F-04; không phát hiện lỗi mạch viết mới. 45 mã, 7 mạch, 120 phút và thứ tự không đổi. |

Bằng chứng đóng các điểm chính:

- Miền $\mathcal S$ chưa kết thúc, $\mathcal S^+$ gồm đích và giá trị đích bằng 0 đã nhất quán giữa deck, note và ma trận đánh giá. Thưởng chuyển vào đích vẫn được tính.
- Đánh giá và lặp giá trị trả $V$ đã đo phần dư. Với $K=0$, trả bảng khởi tạo; với $K=1$, nhận tối đa một bảng rồi kiểm bảng đó. Chính sách trích dùng cùng bảng trả. Kiểm đạt ngưỡng được ưu tiên khi phần dư bằng ngưỡng, kể cả ở lần nhận bảng cuối.
- Với bộ số deck và $K=1$, đánh giá trả $(1,2)$ với phần dư $0{,}9$; lặp giá trị trả $(1,3)$ với phần dư $2{,}7$ và chính sách $(b,b)$ khi ngưỡng là $0{,}01$. Hệ quả có hệ số $\gamma$ cho $W=T_\pi V$ được giữ riêng, không gán cho bảng $V$ của quy trình chính.
- Ví dụ chính sách ngẫu nhiên đều nằm tại notes B04, đúng vị trí đã đồng bộ trong kế hoạch. Ví dụ độ lệch $0{,}9$ xuất hiện trước định nghĩa phần dư B05. F02 phân biệt đánh giá hai trạng thái với lặp giá trị tại chỗ trên lưới; F03 kế thừa đúng toán tử tối ưu.
- E07 gọi lại mô hình hai trạng thái; E08 gọi lại lưới. F04 nối tới F05 bằng điều kiện biểu diễn hữu hạn và mô hình đã biết. Các câu nối nêu quan hệ học thuật, không điều phối trình chiếu.

Hai báo cáo rà lại tại thời điểm kiểm là /tmp/rl04-rebuild/recheck-math.md và recheck-flow.md; kết luận, phạm vi và bằng chứng quyết định đã được lưu bền vững ở đây. Không có đề xuất bắt buộc còn mở.

### RevealJS, học liệu và tài sản

| Kiểm tra thực tế | Kết quả |
|---|---|
| Cấu trúc và kế hoạch | 45 trang, 7 section ngoài, 45 notes, mã duy nhất, đúng thứ tự outline/storyboard, tổng 120 phút. |
| KaTeX | 626 biểu thức HTML gồm notes không lỗi cú pháp; trình đọc note dựng 1.108 biểu thức không báo lỗi. Lỗi ngữ nghĩa do mất dấu gạch chéo trước bản cố định đã được rà riêng; không suy độ đúng từ kiểm cú pháp. |
| Hai kích thước | Duyệt 45 trang ở 1280 × 720 và 390 × 844: 90 lượt đúng trang, không tràn ngoài viewport, không ảnh hỏng, không lỗi JavaScript/HTTP. Bàn phím hoạt động theo các trục/chế độ cuộn tương ứng. |
| Rà ảnh sau biên tập | Xem trực tiếp A02, D01, E06–E08, F02–F03, G03. Caption E06 được chuyển xuống dưới bảng ở cột phải; kiểm lại hai kích thước và xem ảnh xác nhận không còn chạm chân trang. Không giảm chữ hoặc đổi nội dung. |
| Học liệu | Trình đọc note chạy ở hai kích thước, không tràn ngang, không ảnh hoặc liên kết mục lục hỏng; liên kết về deck đúng. Sửa thuật ngữ “dày” thành “đặc” sau lượt kiểm không đổi công thức/cấu trúc. |
| SVG và phụ thuộc | 10 SVG mới hợp lệ, có vai trò/mô tả thay thế; không raster hoặc tài nguyên mạng cốt lõi trong deck. Năm SVG cũ của note không đổi. |
| CSS và phạm vi | Cả 13 tệp bài giảng/mẫu liên kết lecture-slide.css. CSS chung, RevealJS, tiện ích và các bài khác không bị sửa. git diff --check đạt. |

Ở chiều rộng 390 px, toàn khung 16:9 có chữ nhỏ; cần phóng to hoặc xem ngang để đọc lâu. Chưa kiểm màn chiếu trong phòng học hoặc thao tác zoom trên thiết bị thật. Học liệu dạng trang văn bản phù hợp hơn để đọc trên màn hình hẹp.

### Codex Slides và tính bền vững

Dự án 20260928103306-b-i-04-gi-i-mdp-b-ng-quy-ho-ch-ng-h-s-vi-ukmg, tên **Bài 04 — Giải MDP bằng quy hoạch động**. Đã lưu dàn ý 45 trang bằng danh sách tường minh, tải 45 ảnh PNG chụp từ RevealJS đã kiểm và ghi đúng 45 notes. PNG chỉ là ảnh xem trước/kiểm định trong dự án Codex Slides, không phải tài sản nhúng thay SVG của bài giảng.

Kiểm trạng thái và các điểm truy cập ảnh đã lưu: 45/45 trang có trạng thái rendered; cả 45 ảnh khớp SHA-256 với ảnh đã kiểm; tiêu đề và notes khớp HTML. Phiên bản cuối tại lượt kiểm là **48**, mã 19eaff44-0c03-4324-955f-fa340863ef8e. Không chạy tạo hoặc vẽ lại nội dung bằng mô hình của plugin.

Thao tác tải ảnh không tự đổi checkpoint outline. Đã đọc tuyến lưu của ứng dụng rồi cập nhật riêng trạng thái giao diện sang deck/canvas qua API cục bộ của Codex Slides; thao tác này không gọi mô hình. Sau đó mở đúng liên kết bàn giao [Play tại trang 32](http://127.0.0.1:4311/project/20260928103306-b-i-04-gi-i-mdp-b-ng-quy-ho-ch-ng-h-s-vi-ukmg?slide=32&mode=play&checkpoint=deck), xem ảnh E06 bằng Chromium và xác nhận tải lại vẫn giữ trang 32/45, ảnh tải đủ, không lỗi JavaScript.

Browser tích hợp trong Codex không có công cụ khả dụng ở phiên này. Kết quả trên là kiểm trạng thái lưu, ảnh lưu và ứng dụng bằng Chromium cục bộ; **chưa kiểm trực quan trong Browser tích hợp**.

Các tệp phân tích, outline, storyboard, nhật ký, HTML và lecture note được đồng bộ vào Design Files sau khi đóng kiểm định. Bản chính để giảng vẫn là HTML/SVG trong kho.

### Trạng thái bàn giao

Đạt phạm vi nội dung và kiểm định cục bộ đã yêu cầu, với giới hạn Browser tích hợp và màn hình hẹp nêu trên. Đủ năm báo cáo độc lập; các sửa toán và mạch viết đã được kiểm lại. Đã tự biên tập theo no-ai-slop/Edit và kiểm bằng eval.md; Detect độc lập đã có bằng chứng và quyết định. Không còn văn nói mô phỏng, chỉ dẫn biên soạn/điều phối hoặc thuật ngữ thay tùy tiện được ghi nhận là vấn đề mở trong sản phẩm.

Điều phối viên sửa 13 lần thiếu dấu gạch chéo trong công thức của bảng quyết định ở nhật ký sau hợp nhất; đây chỉ là sửa ký hiệu trong hồ sơ, không đổi HTML, note, SVG, lập luận hoặc quyết định.

Hash sản phẩm cuối: HTML 7955b78ca08d9efab4965b8ffa1b0ade3a392d491092dc67dac034f0cda82aba; note ff2077f17aa9ea3d081640f56de6422f08273abaef39a012f24d228806762838; SVG chu trình 2dba0580245918311cf12df6d32aa5edd2e7fbccee2d0341a6344f7ce92ec41c.

## Rà soát từng trang theo yêu cầu ngày 2026-10-01

Yêu cầu của người dùng: duyệt lần lượt từng trang, xác định trang muốn nói gì, vấn đề còn tồn tại và đề xuất sửa; chỉnh sửa để tiêu đề ngắn gọn, học thuật, mạch lập luận chặt chẽ và khái niệm không xuất hiện đột ngột; commit và push sau mỗi trang.

Tác tử: điều phối viên là phiên Claude Code chính. Bốn tác tử rà soát chỉ đọc (dải A01–B08, dải C01–D06, dải E01–G05, kết nối và mạch viết toàn bài) và các tác tử chỉnh sửa tuần tự đều tạo bằng công cụ `Agent` loại `fork`, kế thừa mô hình Claude Opus 5.5 của phiên điều phối. Mô hình ghi theo lời gọi công cụ, không theo lời tự khai của tác tử. Các tác tử rà dùng `no-ai-slop` chế độ Detect; tác tử chỉnh sửa dùng chế độ Edit và tự kiểm theo `eval.md`; tác tử mạch viết dùng `quill` làm danh mục kiểm tra, không tạo `quill.json`.

Kiểm tra trực quan: Playwright Chromium ở 1600 × 900 và 390 × 844, máy chủ `python3 -m reloadserver 8766` tại thư mục gốc. Cổng 8765 đang do một phiên khác chiếm để phục vụ kho `ds-foundation-algorithms`; tiến trình đó không bị dừng. Mỗi trang được kiểm tràn dọc ở khung 1280 × 720, tràn ngang, lỗi KaTeX, ảnh hỏng, cỡ chữ nhỏ nhất, lỗi JavaScript và yêu cầu thất bại.

### Quyết định chung

- Ký hiệu phần dư đổi từ $b_\pi(V)$, $b_*(V)$ thành $\Delta_\pi(V)$, $\Delta_*(V)$; biến cục bộ trong giả mã đổi thành $\Delta$. Lý do: chữ $b$ trùng tên hành động $b$ của MDP hai trạng thái, ví dụ câu hỏi G04 đặt “chính sách tham lam” $(b,b)$ cạnh $b_*(V)$. Đồng bộ trong HTML, outline, storyboard và ghi chú bài giảng; các mục nhật ký cũ giữ nguyên ký hiệu lịch sử.
- Thuật ngữ “giá trị nhìn trước” thay “điểm nhìn trước” và “điểm” cho đại lượng $\sum_{s',r}p(s',r\mid s,a)[r+\gamma V(s')]$; “lượt” chỉ một lần cập nhật mọi trạng thái chưa kết thúc, “vòng” chỉ vòng ngoài của lặp chính sách.
- Đề xuất đổi thứ tự E05→E07→E06 bị bác: giữ thứ tự nguồn đã duyệt; câu nêu nhu cầu đại lượng dừng tính được chuyển lên đầu E07.
- Kiểm trực quan sau đổi ký hiệu: B05, B06, B08, E04, E07, F03, G04 đạt ở hai kích thước, không lỗi.

### L04-A01 — Giải MDP bằng quy hoạch động

- Trang muốn nói: bài 04 tính giá trị và chọn chính sách từ mô hình môi trường đã biết.
- Vấn đề: nhẹ, dòng “Quá trình quyết định Markov (MDP)” đứng như phụ đề rời; dòng này viết đầy đủ chữ viết tắt của tiêu đề nên vẫn có chức năng.
- Quyết định: giữ nguyên. Không có vấn đề vượt mức nhẹ.
- Kiểm tra: không đổi nội dung; trang đạt ở lượt kiểm toàn bài trước đó.

### L04-A02 — Nội dung và mục tiêu

- Trang muốn nói: bản đồ năm thành phần của bài, các mục tiêu học tập và kiến thức tiên quyết.
- Vấn đề: trung bình, mục tiêu không đo được: “Thực hiện cập nhật và cải thiện chính sách.” không nói cập nhật đại lượng nào; “Kiểm tra hội tụ, sai số và điều kiện dừng.” không gắn với phép tính cụ thể. Nhẹ, câu đầu notes “Các thuật toán sau dùng lại…” là lời dẫn rỗng.
- Quyết định: sửa. Bốn mục tiêu một dòng: đánh giá và cải thiện chính sách; thực hiện lặp chính sách, lặp giá trị; chặn sai số bằng phần dư; so sánh cập nhật đồng bộ và bất đồng bộ. Bản đề xuất ba mục dài làm trang cao 705/720 nên được tách thành bốn mục ngắn. Notes nêu ánh xạ mục tiêu sang các mạch. Đồng bộ outline.
- Kiểm tra: 665/720 ở 16:9; hai kích thước đạt, không lỗi; đã xem ảnh.

### L04-A03 — Lập kế hoạch với mô hình đã biết

- Trang muốn nói: dữ kiện của MDP hữu hạn có mô hình đã biết và bài toán tìm chính sách tối ưu tại mọi trạng thái.
- Vấn đề: trung bình, thuật ngữ “quy hoạch động” trong tên bài chưa được định nghĩa trên mặt trang nào. Nhẹ, tiêu đề có từ thừa “Bài toán”. Nhẹ, “Đánh giá chính sách hiện tại cung cấp căn cứ để thay đổi lựa chọn.” dùng động từ mạnh giả tạo.
- Quyết định: sửa. Tiêu đề “Lập kế hoạch với mô hình đã biết”. Thay câu trên bằng định nghĩa “Quy hoạch động: nhóm thuật toán tính chính sách tối ưu từ mô hình MDP đầy đủ.” theo Sutton–Barto chương 4, tr. 73, nguồn đã có trong notes. Ý “giá trị của chính sách là căn cứ để đổi lựa chọn” chuyển xuống notes. Đồng bộ tiêu đề và ý chính ở outline, storyboard.
- Kiểm tra: 665/720; hai kích thước đạt, không lỗi; đã xem ảnh.

### L04-A04 — MDP hai trạng thái

- Trang muốn nói: bốn chuyển tiếp xác định và chính sách ban đầu $\pi_0$ là dữ kiện dùng xuyên suốt bài.
- Vấn đề: trung bình, tiêu đề “Mô hình hai trạng thái” trùng nghĩa với “mô hình $p$”. Trung bình, $\pi_0=(a,a)$ chưa được nói là chính sách xác định, nên $\pi(a\mid s)$ ở B03 xuất hiện đột ngột. Trung bình, lý do cần ví dụ (thưởng trước mắt chưa đủ để chọn) chỉ có trong notes.
- Quyết định: sửa. Tiêu đề “MDP hai trạng thái”. Box nêu “Chính sách xác định $\pi_0=(a,a)$: chọn $a$ tại $s_0$ và tại $s_1$, tức $\pi_0(a\mid s)=1$.” Thêm chú thích nêu vấn đề: tại $s_0$, $a$ cho thưởng tức thời lớn hơn, nhưng chỉ $b$ dẫn tới $s_1$ có thưởng $2$ và $3$; dữ kiện đã kiểm theo bảng. Notes giữ thứ tự $(s_0,s_1)$ và giải thích vì sao cần tính phần thưởng sau bước đầu. Đồng bộ tiêu đề ở outline, storyboard.
- Kiểm tra: 665/720; hai kích thước đạt, không lỗi; đã xem ảnh.

### L04-A05 — Kiểm tra tổng thưởng chiết khấu

- Trang muốn nói: tính tổng chiết khấu cắt ngắn ba bước theo $\pi_0$ và chỉ ra rằng chỉ biết phần thưởng của từng hành động thì chưa đủ.
- Vấn đề: trung bình, công thức $G_t$ đặt sau câu hỏi, dữ kiện đứng sau yêu cầu. Nhẹ, tiêu đề tám từ. Nhẹ, notes dùng dấu chấm thập phân. Lời giải đã kiểm: thưởng $2$, $1$, $1$; tổng $3{,}71$.
- Quyết định: sửa. Tiêu đề “Kiểm tra tổng thưởng chiết khấu”. Công thức $G_t$ đặt trước câu hỏi, dạng nội dòng trong khối công thức lớn; dạng hiển thị làm trang cao 713/720 và tiêu đề chạm nút điều hướng. Sửa dấu phẩy thập phân trong notes và alt hình. Đồng bộ tiêu đề ở outline, storyboard.
- Kiểm tra: 602/720; hai kích thước đạt, không lỗi; đã xem ảnh.

### L04-B01 — Bài toán đánh giá chính sách

- Trang muốn nói: đánh giá chính sách là tính tổng thưởng kỳ vọng của một chính sách cố định; phần tiếp nối của tổng lại là cùng bài toán, xuất phát từ trạng thái kế tiếp.
- Vấn đề: nghiêm trọng, thuật ngữ “đánh giá chính sách” chưa được gọi tên dù B04 dùng ngay trong tiêu đề. Nghiêm trọng, ý thay phần tiếp nối bằng bảng hiện có chỉ được nói mờ (“Một bảng giá trị hiện có ước lượng phần thưởng về sau.”). Trung bình, hệ thức $G_t=R_{t+1}+\gamma G_{t+1}$ chỉ có trong notes B03. Trung bình, “giá trị tiếp nối” là thuật ngữ xương sống nhưng chưa có định nghĩa trên mặt trang. Trung bình, tiêu đề dùng “Dự đoán” trong khi cả mạch dùng “đánh giá”.
- Quyết định: sửa. Tiêu đề “Bài toán đánh giá chính sách”. Mặt trang gọi tên “Đánh giá chính sách (bài toán dự đoán)”, đưa hệ thức $G_t=R_{t+1}+\gamma G_{t+1}$ lên và định nghĩa giá trị tiếp nối $V(s')$ trong box. Câu “chính sách được giữ cố định” và cách suy hệ thức chuyển xuống notes. Hình dùng lớp có sẵn `figure short` để không tràn; nhãn hình vẫn đọc được. Đồng bộ tiêu đề ở outline, storyboard và mục hình thức hóa trong outline.
- Kiểm tra: lần đầu 726/720 (tràn), sau khi rút câu và dùng `figure short` còn 692/720; hai kích thước đạt, không lỗi; đã xem ảnh.

### L04-B02 — Hai lượt đánh giá đồng bộ

- Trang muốn nói: một lượt đồng bộ tính mọi ô từ cùng bảng cũ theo quy tắc thưởng một bước cộng giá trị cũ chiết khấu của trạng thái kế tiếp.
- Vấn đề: trung bình, phép tính không ghi ô nào của bảng cũ được đọc (“$V_1(s_1)=2+0{,}9\cdot0=2$”), nên ký hiệu $V_k(s')$ không truyền sang công thức ở B03–B04. Trung bình, chưa có câu trực giác cho quy tắc tính. Nhẹ, “cập nhật đồng bộ” dùng ở dòng đầu nhưng chỉ được giải thích ở box. Nhẹ, tiêu đề chín từ. Nhẹ, notes dùng dấu chấm thập phân.
- Quyết định: sửa. Tiêu đề “Hai lượt đánh giá đồng bộ”. Dòng đầu nêu quy tắc bằng lời. Bốn phép tính viết $V_{k+1}(s)=r+0{,}9\,V_k(s_0)$; số liệu đã kiểm: $V_1=(1,2)$, $V_2=(1{,}9;2{,}9)$. Box định nghĩa cập nhật đồng bộ và “lượt” (cập nhật mỗi trạng thái một lần). Notes giải thích vì sao cả hai ô đọc $s_0$ và gọi tên cập nhật tại chỗ cho phép tính $2+0{,}9\cdot1{,}9=3{,}71$. Đồng bộ tiêu đề ở outline, storyboard.
- Kiểm tra: 670/720; hai kích thước đạt, không lỗi; đã xem ảnh.

### L04-B03 — Phương trình Bellman kỳ vọng

- Trang muốn nói: $v_\pi$ là kỳ vọng của tổng thưởng và thỏa quan hệ một bước, với cùng ẩn $v_\pi$ ở hai vế.
- Vấn đề: trung bình, chưa có cầu nối với phép tính tay ở B02; mặt trang không nói phương trình là phép tính đó với $V_k$, $V_{k+1}$ thay bằng cùng $v_\pi$. Trung bình, $\pi(a\mid s)$ và tổng theo $a$, $s'$, $r$ xuất hiện trong khi ví dụ là xác định. Nhẹ, tiêu đề tám từ.
- Quyết định: sửa. Tiêu đề “Phương trình Bellman kỳ vọng” (giữ “kỳ vọng” để đối lập với “tối ưu” ở D04, E03). Dòng đầu nối các bảng $V_k$ với hàm giá trị $v_\pi$. Thêm chú thích: phép tính hai lượt với $V_k$, $V_{k+1}$ thay bằng cùng $v_{\pi_0}$, mỗi tổng còn một hạng. Notes giải thích $\pi(a\mid s)$ cho chính sách xác định (A04 đã nêu $\pi_0(a\mid s)=1$). Đồng bộ tiêu đề ở outline, storyboard.
- Kiểm tra: 656/720; hai kích thước đạt, không lỗi; đã xem ảnh.

### L04-B04 — Toán tử đánh giá chính sách

- Trang muốn nói: thay $v_\pi$ ở vế phải bằng một bảng bất kỳ cho toán tử $T_\pi$; lặp toán tử này là phép tính ở B02, và $v_\pi$ là điểm bất động của nó.
- Vấn đề: trung bình, $T_\pi$ được đưa ra mà mặt trang không nêu thao tác sinh ra nó (“Toán tử $T_\pi$ biến bảng … thành bảng mới”). Trung bình, mặt trang không chỉ ra hai lượt ở B02 chính là $V_1=T_\pi V_0$, $V_2=T_\pi V_1$. Nhẹ, “điểm bất động” chỉ được nêu tên. Trung bình, notes quá tải: đoạn về độ lệch $0{,}9$ phục vụ nhu cầu tiêu chuẩn dừng của B05.
- Quyết định: sửa. Tiêu đề giữ. Dòng đầu: “Thay $v_\pi$ ở vế phải phương trình Bellman bằng một bảng $V$ bất kỳ; $p$ và $\pi$ giữ cố định.” Thẻ quy tắc lặp ghi hai lượt đã tính; thẻ nghiệm ghi “$v_\pi$ là điểm bất động của $T_\pi$”, notes thêm rằng tính duy nhất cần $\gamma<1$. Đoạn notes về độ lệch $0{,}9$ chuyển sang notes B05. “Lượt cập nhật toàn bảng” đổi thành “lượt”.
- Kiểm tra: 689/720; dòng “Hai lượt đã tính” tách khỏi công thức để KaTeX không ngắt giữa đẳng thức; hai kích thước đạt, không lỗi; đã xem ảnh.

### L04-B05 — Thuật toán đánh giá chính sách đồng bộ

- Trang muốn nói: quy trình hai bảng với phép dừng theo phần dư tính được từ bảng hiện có.
- Vấn đề: nghiêm trọng, bốn ký hiệu mới ($\|\cdot\|_\infty$, phần dư, $\eta$, $K$) xuất hiện cùng lúc, không có nhu cầu đi trước; mặt trang không nói vì sao cần đại lượng dừng. Trung bình, bước 3–4 dài và lặp ý (“Khi hết $K$ lượt, tính lại … trên bảng cuối; trả … cùng kết quả kiểm tra ngưỡng.”).
- Quyết định: sửa. Tiêu đề giữ. Mở bằng nhu cầu: sau hữu hạn lượt, bảng chỉ xấp xỉ $v_\pi$. Định nghĩa phần dư kèm ví dụ $\Delta_{\pi_0}(V_1)=\max\{0{,}9;0{,}9\}=0{,}9$ (đã kiểm: $T_{\pi_0}V_1=(1{,}9;2{,}9)$). Quy trình ba bước; ngữ nghĩa giữ nguyên: kiểm ngưỡng ưu tiên, trả $V$ không trả $W$, sau lần nhận bảng thứ $K$ bước 2 đo phần dư của bảng cuối, $K=0$ trả bảng khởi tạo. Notes cập nhật theo bước mới và nhận đoạn ví dụ chuyển từ B04. Đồng bộ outline, storyboard.
- Kiểm tra: 648/720; hai kích thước đạt, không lỗi; đã xem ảnh.

### L04-B06 — Hội tụ của đánh giá lặp

- Trang muốn nói: khi $\gamma<1$, $T_\pi$ là ánh xạ co; vì vậy đánh giá lặp hội tụ tới $v_\pi$ duy nhất và phần dư chặn được sai số.
- Vấn đề: trung bình, mặt trang không gọi tên “tính co” dù C05 (“$T_{\pi'}$ co”) và E05 dùng lại thuật ngữ này. Nhẹ, thiếu nhãn tính chất và hệ quả. Nhẹ, tiêu đề chưa song song với E05.
- Quyết định: sửa. Tiêu đề “Hội tụ của đánh giá lặp”. Giả thiết nêu thành một dòng riêng, kèm điều kiện không áp dụng khi $\gamma=1$. Thêm nhãn “Tính co.” với diễn giải bằng lời trước bất đẳng thức và nhãn “Hệ quả.” trước chặn sai số. Box cũ bỏ để tránh đè chân trang (bản đầu cao 711/720); ý “phần dư đo trên bảng trả về” chuyển xuống notes. Đồng bộ tiêu đề ở outline, storyboard.
- Kiểm tra: 659/720 sau khi sửa câu diễn giải tính co; hai kích thước đạt, không lỗi; đã xem ảnh.

### L04-B07 — Giá trị chính xác của chính sách ban đầu

- Trang muốn nói: giải hệ Bellman cho $v_{\pi_0}=(10,11)$ và đối chiếu với các bảng lặp; giá trị này là giá trị tiếp nối để so sánh hành động ở mạch sau. Số liệu đã kiểm: $x=1/0{,}1=10$, $y=2+0{,}9\cdot10=11$.
- Vấn đề: nhẹ, tiêu đề “Nghiệm đánh giá của chính sách ban đầu” vòng. Nhẹ, hộp kết quả ngắt dòng giữa đẳng thức $v_{\pi_0}=(10,11)$.
- Quyết định: sửa tiêu đề thành “Giá trị chính xác của chính sách ban đầu” (dùng chữ, không đưa $\pi_0$ vào tiêu đề). Hộp kết quả tách hai dòng. Nội dung khác giữ. Đồng bộ tiêu đề ở outline, storyboard.
- Kiểm tra: 578/720; hai kích thước đạt, không lỗi; đã xem ảnh.

### L04-B08 — Kiểm tra đánh giá chính sách

- Trang muốn nói: người học tự tính $V_3$, phần dư và chặn sai số, rồi phân biệt bảng ước lượng với nghiệm chính xác.
- Vấn đề: nhẹ, câu 3 diễn đạt vụng (“Giải thích vì sao chưa được gọi $V_3$ là $v_{\pi_0}$.”). Nhẹ, lời giải trong notes dùng dấu chấm thập phân. Nhẹ, tiêu đề chưa theo mẫu “Kiểm tra” + tên khái niệm của mạch.
- Quyết định: sửa. Tiêu đề “Kiểm tra đánh giá chính sách”. Câu 3: “Giải thích vì sao $V_3$ chưa phải là $v_{\pi_0}$.” Lời giải đã kiểm: $V_3=(2{,}71;3{,}71)$, $\Delta_{\pi_0}(V_2)=0{,}81$, chặn $8{,}1$; notes thêm rằng sai số thật của $V_2$ cũng bằng $8{,}1$. Đồng bộ tiêu đề ở outline, storyboard.
- Kiểm tra: 548/720; hai kích thước đạt, không lỗi; đã xem ảnh.

### L04-C01 — Đổi hành động ở bước đầu

- Trang muốn nói: khi đã biết $v_{\pi_0}$, có thể đánh giá việc đổi hành động ở bước đầu rồi tiếp tục theo $\pi_0$; đại lượng so sánh là giá trị nhìn trước.
- Vấn đề: trung bình, trang chưa nêu bài toán cần giải (“Đã biết giá trị của chính sách hiện tại: $v_{\pi_0}=(10,11)$.”). Trung bình (Detect, mục đích mơ hồ, thiếu $\gamma$): “So sánh phần thưởng trước mắt cộng giá trị tiếp nối chuẩn bị cho việc thay đổi chính sách.” Trung bình, thuật ngữ “giá trị nhìn trước” được dùng từ C02 nhưng chưa định nghĩa trên mặt trang. Nhẹ, tiêu đề dài.
- Quyết định: sửa. Tiêu đề “Đổi hành động ở bước đầu”. Dòng đầu nêu bài toán điều khiển: xác định có nên đổi hành động của $\pi_0$ tại một trạng thái. Hộp cuối định nghĩa giá trị nhìn trước $r+\gamma\,v_{\pi_0}(s')$. Notes thêm kỳ vọng theo $p$ khi chuyển tiếp ngẫu nhiên và việc giữ $v_{\pi_0}$ cố định. Đồng bộ tiêu đề và ý chính ở outline, storyboard.
- Kiểm tra: 650/720; hai kích thước đạt, không lỗi; đã xem ảnh.

### L04-C02 — So sánh hai nhánh hành động

- Trang muốn nói: tại $s_1$, chọn $b$ một bước rồi theo $\pi_0$ cho giá trị nhìn trước $12{,}9$, lớn hơn $v_{\pi_0}(s_1)=11$ của hành động cũ.
- Vấn đề: trung bình, trang không nói nhánh $a$ là hành động của $\pi_0$, nên không thấy $12{,}9$ vượt giá trị hiện tại. Nhẹ, thẻ “Hành động thứ nhất” và “Chọn $a$ tại $s_1$” lặp ý. Nhẹ, notes dùng dấu chấm thập phân (“Số 12.9”).
- Quyết định: sửa. Đề xuất tiêu đề “So sánh hai hành động tại $s_1$” (quyết định chung) KHÔNG áp dụng: CSS chung đặt tiêu đề `h2`/`h3` chữ hoa, nên KaTeX hiển thị $s_1$ thành $S_1$ và $a$ thành $A$, làm sai ký hiệu (biến ngẫu nhiên $S_t$ khác trạng thái $s$). Tiêu đề chọn “So sánh hai nhánh hành động”; thẻ đặt tên “Giữ hành động cũ”, “Đổi hành động”, ký hiệu chuyển xuống dòng thân. Hộp cuối: “Giá trị nhìn trước của $b$ vượt $v_{\pi_0}(s_1)=11$.” Notes đổi $12{,}9$. Đồng bộ tiêu đề ở outline, storyboard.
- Kiểm tra: bản có thêm mệnh đề trong hộp cao 714/720, đã rút còn 671/720; hai kích thước đạt, không lỗi; đã xem ảnh.

### L04-C03 — Hàm giá trị hành động

- Trang muốn nói: $q_\pi(s,a)$ cố định hành động đầu rồi theo $\pi$; tách bước đầu cho dạng tính được, và hai giá trị nhìn trước ở trang trước chính là $q_{\pi_0}(s_1,\cdot)$.
- Vấn đề: trung bình, mặt trang không phân biệt định nghĩa với tính chất; định nghĩa bằng kỳ vọng chỉ có trong notes nên công thức tổng một bước trông như định nghĩa. Nhẹ, hộp cuối không nói hai số là giá trị nhìn trước vừa tính. Nhẹ, tiêu đề chưa song song với “Phương trình Bellman kỳ vọng”/“Hàm giá trị” ở mạch B.
- Quyết định: sửa. Tiêu đề “Hàm giá trị hành động”. Dòng đầu gắn nhãn “Định nghĩa.” với $q_\pi(s,a)=\mathbb E_\pi[G_t\mid S_t=s,A_t=a]$ và câu “Tách bước đầu cho dạng tính được:”. Hộp cuối: “Hai giá trị nhìn trước tại $s_1$ là …”. Notes bỏ câu lặp định nghĩa, giữ quy ước $\pi(a\mid s)=0$. Đồng bộ tiêu đề ở outline, storyboard.
- Kiểm tra: 613/720; hai kích thước đạt, không lỗi; đã xem ảnh.

### L04-C04 — Cải thiện chính sách tham lam

- Trang muốn nói: chọn hành động cực đại theo $q_\pi$ (với $v_\pi$ chính xác cố định) cho chính sách không kém $\pi$ tại mọi trạng thái; quy tắc phá hòa giữ hành động cũ khi hòa.
- Vấn đề: trung bình, định lý xuất hiện chưa có nhu cầu trên mặt trang (lý do “$12{,}9$ giả định tiếp nối theo $\pi_0$” chỉ có trong notes C02). Trung bình, “tham lam” và $\arg\max$ chưa giải thích trên mặt trang. Trung bình, lý do chính sách tham lam thỏa giả thiết định lý chỉ có trong notes. Trung bình, quy tắc phá hòa chưa có tên dù D05 gọi “phá hòa ổn định”. Nhẹ, câu khó đọc “Với giá trị chính xác $v_\pi$, giữ nguyên bảng này khi chọn hành động ở mọi trạng thái.”
- Quyết định: sửa. Tiêu đề “Cải thiện chính sách tham lam”. Thêm câu nhu cầu nối với $12{,}9$. Định nghĩa chính sách tham lam nội dòng; câu “$\arg\max$ là tập hành động đạt cực đại” và nhãn “Phá hòa:”. Hộp định lý thêm câu “Chính sách tham lam thỏa giả thiết vì $\max_a q_\pi(s,a)\ge\sum_a\pi(a\mid s)q_\pi(s,a)=v_\pi(s)$.” Notes tách trường hợp chính sách cũ xác định và ngẫu nhiên, đổi “phá hòa ổn định” thành “quy tắc phá hòa”. Đồng bộ tiêu đề ở outline, storyboard.
- Kiểm tra: bản giữ công thức $\arg\max$ dạng khối cao 767/720 (tràn); chuyển công thức thành nội dòng, còn 626/720. Hai kích thước đạt, không lỗi; đã xem ảnh.

### L04-C05 — Chứng minh định lý cải thiện

- Trang muốn nói: từ $v_\pi\le T_{\pi'}v_\pi$, tính đơn điệu và tính co của $T_{\pi'}$ cho $v_\pi\le v_{\pi'}$.
- Vấn đề: nghiêm trọng, bước đầu của chứng minh thiếu căn cứ trên mặt trang; đẳng thức $(T_{\pi'}v_\pi)(s)=q_\pi(s,\pi'(s))$ chỉ có trong notes, còn mặt trang ghi “Từ điều kiện cải thiện: $v_\pi\le T_{\pi'}v_\pi$”. Trung bình, không nói dãy là đánh giá lặp $\pi'$ đã học ở mạch B và thiếu câu kết luận. Nhẹ, thẻ “Bảo toàn thứ tự” lệch tên “đơn điệu” trong notes, storyboard. Nhẹ (Detect, metadiscourse) trong notes: “Phép tính số minh họa điều kiện; lập luận này cung cấp kết quả cho toàn bộ lớp MDP đã nêu.”
- Quyết định: sửa. Tiêu đề “Chứng minh định lý cải thiện”. Dòng đầu đưa đẳng thức cầu nối lên mặt trang. Thẻ “Tính đơn điệu”. Thẻ giới hạn: dãy là đánh giá lặp $\pi'$ xuất phát từ $v_\pi$; do tính co, dãy hội tụ về $v_{\pi'}$; vậy $v_\pi\le v_{\pi'}$. Notes giải thích vì sao đẳng thức đúng (tổng theo hành động còn một hạng) và bỏ câu metadiscourse. Đồng bộ tiêu đề ở outline, storyboard.
- Kiểm tra: tách câu kết luận để KaTeX không ngắt giữa bất đẳng thức; 635/720; hai kích thước đạt, không lỗi; đã xem ảnh.

### L04-C06 — Lần cải thiện thứ nhất

- Trang muốn nói: cải thiện từ $\pi_0$ chỉ đổi hành động tại $s_1$, cho $\pi_1=(a,b)$ với $v_{\pi_1}=(10,30)\ge v_{\pi_0}=(10,11)$; giá trị tiếp nối tại $s_1$ tăng nên lựa chọn ở $s_0$ có thể đổi. Số liệu đã kiểm: $q_{\pi_0}(s_0,a)=10$, $q_{\pi_0}(s_0,b)=9{,}9$; $x=1/0{,}1=10$, $y=3/0{,}1=30$.
- Vấn đề: trung bình, hệ quả chính (đối chiếu định lý, giá trị tiếp nối 11 → 30) chỉ có trong notes, trong khi đó là ý nối sang C07. Nhẹ, “$x=1+0{,}9x$; $y=3+0{,}9y$” không nói đây là hệ Bellman của $\pi_1$. Nhẹ, notes dùng “Điểm $12{,}9$”.
- Quyết định: sửa. Tiêu đề “Lần cải thiện thứ nhất”. Thẻ phải: “Hệ Bellman của $\pi_1$: …”. Thêm hộp “$v_{\pi_1}\ge v_{\pi_0}$ theo từng trạng thái; giá trị tiếp nối tại $s_1$ tăng từ 11 lên 30.” Notes nêu $x,y$ và đổi sang “giá trị nhìn trước”. Đồng bộ tiêu đề ở outline, storyboard.
- Kiểm tra: 658/720; hai kích thước đạt, không lỗi; đã xem ảnh.

### L04-C07 — Kiểm tra cải thiện chính sách

- Trang muốn nói: lần cải thiện thứ hai phải dùng $v_{\pi_1}=(10,30)$; với giá trị này, tại $s_0$ chọn $b$ vì $27>10$.
- Vấn đề: nhẹ, tiêu đề “Kiểm tra lựa chọn theo giá trị chính sách” mơ hồ, chưa theo mẫu “Kiểm tra” + tên khái niệm của mạch. Nhẹ, câu 3 “Giải thích sự khác biệt so với cải thiện từ $\pi_0$.” chưa nói khác biệt ở đâu.
- Quyết định: sửa. Tiêu đề “Kiểm tra cải thiện chính sách” (dùng chữ, không đưa $\pi_1$ vào tiêu đề; tiêu đề chữ hoa làm sai ký hiệu toán viết thường). Câu 3: “Giải thích vì sao lựa chọn tại $s_0$ khác lần cải thiện từ $\pi_0$.” Lời giải ghi phép tính $1+0{,}9\cdot10=10$ và $0+0{,}9\cdot30=27$. Đồng bộ tiêu đề ở outline, storyboard.
- Kiểm tra: 518/720; hai kích thước đạt, không lỗi; đã xem ảnh.

### L04-D01 — Chu trình lặp chính sách

- Trang muốn nói: đổi chính sách làm đổi giá trị tiếp nối, nên phải xen kẽ đánh giá và cải thiện; chu trình này là lặp chính sách.
- Vấn đề: trung bình, thuật ngữ “lặp chính sách” chưa được gọi tên trên mặt trang (chỉ có trong notes và alt của hình) nhưng D02 dùng ngay. Trung bình, câu mở chung chung (“Chính sách thay đổi làm thay đổi giá trị tiếp nối. Vì vậy chính sách mới phải được đánh giá lại.”), không dùng bằng chứng từ C06–C07. Nhẹ, tiêu đề kể hai thao tác thay vì gọi tên khái niệm.
- Quyết định: sửa. Tiêu đề “Chu trình lặp chính sách”. Câu mở dùng bằng chứng 11 → 30 và lựa chọn tại $s_0$ đổi theo, rồi định nghĩa “Lặp chính sách (policy iteration) xen kẽ đánh giá và cải thiện cho đến khi chính sách không đổi.” Câu chung cũ chuyển xuống notes. Hình giữ nguyên. Đồng bộ tiêu đề ở outline, storyboard.
- Kiểm tra: 631/720; hai kích thước đạt, không lỗi; đã xem ảnh.

### L04-D02 — Lặp chính sách trên MDP hai trạng thái

- Trang muốn nói: hai lần đổi chính sách đưa $(a,a)$ tới $(b,b)$; chính sách này không đổi khi cải thiện theo giá trị chính xác của nó, nên là chính sách ổn định. Số liệu đã kiểm: $(b,b)$ có $x=0{,}9y$, $y=3+0{,}9y$ nên $(27,30)$; $q_{\pi_2}=(25{,}3;\,27;\,26{,}3;\,30)$.
- Vấn đề: trung bình, “quỹ đạo” là thuật ngữ RL chỉ chuỗi trạng thái–hành động–phần thưởng, dùng cho dãy kết quả thuật toán gây nhầm. Trung bình, “chính sách ổn định” dùng ở D03, D04 mà chưa định nghĩa. Nhẹ, chỉ số $i$ giới thiệu ở D01 nhưng bảng không có cột $i$. Nhẹ, thẻ “Trạng thái thứ nhất” và “Tại $s_0$, theo $(b,b)$:” lặp ý; các số chưa được gọi là $q_{\pi_2}$.
- Quyết định: sửa. Tiêu đề “Lặp chính sách trên MDP hai trạng thái”. Bảng thêm cột $i$ (0, 1, 2). Thẻ ghi $q_{\pi_2}(s,\cdot)$ trên một dòng; giữ tên thẻ bằng chữ (không đưa $s_0$ vào `h3` vì chữ hoa làm sai ký hiệu). Câu cuối định nghĩa “Chính sách ổn định” và nêu $\pi_2=(b,b)$ ổn định. Notes dùng $v_{\pi_1}$, $\pi_2$. Đồng bộ tiêu đề ở outline, storyboard.
- Kiểm tra: bản đầu cao 689/720, tiêu đề chạm mũi tên điều hướng dọc; gộp hai dòng $q$ mỗi thẻ, còn 617/720. Hai kích thước đạt, không lỗi; đã xem ảnh.

### L04-D03 — Thuật toán lặp chính sách

- Trang muốn nói: quy trình đầy đủ gồm đầu vào, đánh giá chính xác, cải thiện tham lam có quy tắc phá hòa, dừng khi chính sách ổn định hoặc hết ngân sách.
- Vấn đề: trung bình (xung đột thuật ngữ), bước 4 “trả $(\pi,v_\pi)$ với trạng thái ổn định”, chữ “trạng thái” trùng với trạng thái MDP. Nhẹ, bước 5 không nêu kết luận khi hết ngân sách, không đối xứng với bước 4. Nhẹ, bước 3 diễn đạt lại quy tắc phá hòa thay vì dùng tên đã đặt ở C04.
- Quyết định: sửa. Tiêu đề giữ. Bước 3 “áp dụng quy tắc phá hòa”. Bước 4 “trả $(\pi,v_\pi)$ và kết luận chính sách ổn định”. Bước 5 “trả $(\pi,v_\pi)$ và kết luận chưa ổn định”; “lặp từ bước 2”. Notes giữ (đã nêu cặp trả về khi hết ngân sách chưa được chứng nhận tối ưu).
- Kiểm tra: 521/720; hai kích thước đạt, không lỗi; đã xem ảnh.

### L04-D04 — Chính sách ổn định là tối ưu

- Trang muốn nói: chính sách ổn định thỏa phương trình Bellman tối ưu; trong MDP hữu hạn chiết khấu phương trình này có nghiệm duy nhất $v_*$, nên chính sách ổn định là tối ưu. Với ví dụ: $\pi_*=(b,b)$, $v_*=(27,30)$.
- Vấn đề: trung bình, $v_*$ xuất hiện đột ngột (“Giá trị tối ưu: $v_*(s)=\max_\pi v_\pi(s)$.”), không nối với mục tiêu “lớn nhất tại mọi trạng thái” ở A03. Trung bình, bước $v_\pi(s)=q_\pi(s,\pi(s))=\max_a q_\pi(s,a)$ chỉ có trong notes. Trung bình, công thức khối chưa có nhãn “phương trình Bellman tối ưu” trên mặt trang. Nhẹ, tính duy nhất được chứng minh ở mạch E; notes đã ghi.
- Quyết định: sửa. Tiêu đề “Chính sách ổn định là tối ưu”. Dòng đầu nêu mục tiêu điều khiển là giá trị tối ưu tại mọi $s$. Dòng hai đưa chuỗi $v_\pi(s)=q_\pi(s,\pi(s))=\max_a q_\pi(s,a)$ lên mặt trang và gọi tên phương trình Bellman tối ưu. Hộp: “phương trình này có nghiệm duy nhất $v_*$, nên $v_\pi=v_*$.” “Mô hình hai trạng thái” → “MDP hai trạng thái”. Notes giải thích vì sao chính sách ổn định thỏa $\pi(s)\in\arg\max_a q_\pi(s,a)$ (quy tắc phá hòa). Đồng bộ tiêu đề ở outline, storyboard.
- Kiểm tra: 658/720; hai kích thước đạt, không lỗi; đã xem ảnh.

### L04-D05 — Dừng hữu hạn và đánh giá gần đúng

- Trang muốn nói: với đánh giá chính xác và quy tắc phá hòa, lặp chính sách dừng sau hữu hạn vòng; đánh giá gần đúng không có bảo đảm này.
- Vấn đề: trung bình, thiếu mắt xích “không chính sách nào lặp lại” trên mặt trang (chỉ có trong notes); mặt trang chỉ có số chính sách hữu hạn và “cải thiện nghiêm ở ít nhất một trạng thái”. Trung bình, “phá hòa ổn định” và “quy tắc giữ hòa” (notes) là hai tên khác cho quy tắc đã đặt tên ở C04.
- Quyết định: sửa. Tiêu đề giữ. Dòng cuối thẻ trái: “Mỗi lần đổi, giá trị không giảm và tăng nghiêm ở ít nhất một trạng thái, nên không chính sách nào lặp lại.” Hộp: “Đánh giá chính xác cùng quy tắc phá hòa bảo đảm dừng sau hữu hạn vòng.” Notes thống nhất “quy tắc phá hòa”.
- Kiểm tra: rút hộp để không còn một chữ rơi xuống dòng riêng; 612/720; hai kích thước đạt, không lỗi; đã xem ảnh.

### L04-D06 — Kiểm tra điều kiện dừng

- Trang muốn nói: chính sách không đổi khi cải thiện theo một bảng sai chưa phải tối ưu; định lý dừng chỉ áp dụng khi bảng là giá trị chính xác của chính sách đang giữ. Lời giải đã kiểm: bốn giá trị nhìn trước từ $V=(0,0)$ là $1,0,2,3$; $(a,b)$ tham lam theo $V$; $v_{(a,b)}=(10,30)$ kém $(27,30)$ của $(b,b)$.
- Vấn đề: nhẹ, tiêu đề dài (“Kiểm tra điều kiện dừng của lặp chính sách”). Thuật ngữ “giá trị nhìn trước” đã khớp định nghĩa ở C01 sau commit thống nhất thuật ngữ.
- Quyết định: sửa tiêu đề thành “Kiểm tra điều kiện dừng”; nội dung và notes giữ. Đồng bộ tiêu đề ở outline, storyboard.
- Kiểm tra: 556/720; hai kích thước đạt, không lỗi; đã xem ảnh.

### L04-E01 — Cắt ngắn bước đánh giá

- Trang muốn nói: cắt bước đánh giá của lặp chính sách còn một lượt rồi gộp với lựa chọn tham lam cho quy tắc lặp giá trị; bảng trung gian không là giá trị của chính sách nào, nên điều kiện dừng đổi sang phần dư.
- Vấn đề: trung bình, nhu cầu cắt ngắn chỉ nêu chung (“Đánh giá có thể cần nhiều lượt tính.”), không dùng số liệu của mạch B. Trung bình (báo cáo mạch), D05–D06 vừa kết luận đánh giá gần đúng không chứng nhận tối ưu, E01 lại cắt đánh giá mà không nêu tiêu chuẩn dừng mới. Nhẹ, tiêu đề dài, cụm “trong bài toán điều khiển” thừa.
- Quyết định: sửa. Tiêu đề “Cắt ngắn bước đánh giá”. Câu mở nêu sai số $10\cdot0{,}9^k$ và 44 lượt (đã kiểm: $V_k(s_0)=10(1-0{,}9^k)$, $V_k(s_1)=11-10\cdot0{,}9^k$; $0{,}9^{43}\approx0{,}0108$, $0{,}9^{44}\approx0{,}0097$). Hộp thêm điều kiện dừng theo phần dư của toán tử tối ưu. Notes thêm phép tính 44 lượt và cầu nối “tham lam + một lượt đánh giá = cực đại”. Đồng bộ tiêu đề và quyết định ở outline, storyboard.
- Kiểm tra: 630/720; hai kích thước đạt, không lỗi KaTeX/JS/tài nguyên; đã xem ảnh.

### L04-E02 — Hai lượt lặp giá trị đồng bộ

- Trang muốn nói: tính tay hai lượt lặp giá trị đồng bộ trên MDP hai trạng thái; khác đánh giá chính sách ở phép cực đại trên các hành động. Số đã kiểm: $V_1=(1,3)$, $V_2=(2{,}7;5{,}7)$.
- Vấn đề: nhẹ, cụm “trên cùng mô hình” trong tiêu đề mơ hồ. Nhẹ, hành động đạt cực đại không ghi trên mặt trang, trong khi trang thuật toán trích $\pi_V$ và trang phần dư dùng “chính sách tham lam là $(b,b)$”.
- Quyết định: sửa. Tiêu đề “Hai lượt lặp giá trị đồng bộ” (song song “Hai lượt đánh giá đồng bộ”). Hộp thêm “Ở lượt hai, cực đại đạt tại $(b,b)$.” (báo cáo gốc viết “cả hai lượt”, sai vì lượt một cực đại tại $(a,b)$; dùng bản đã sửa). Notes ghi hành động cực đại của từng lượt. Bỏ câu dẫn “Mỗi ô lấy giá trị nhìn trước lớn nhất…” vì làm trang tràn (727/720) và trùng thẻ ở trang trước. Đồng bộ tiêu đề ở outline, storyboard.
- Kiểm tra: 678/720; hai kích thước đạt, không lỗi; đã xem ảnh.

### L04-E03 — Toán tử Bellman tối ưu

- Trang muốn nói: ký hiệu hóa phép tính tay của lặp giá trị thành giá trị nhìn trước $Q_V$ và toán tử $T_*$; $v_*$ là điểm bất động của $T_*$.
- Vấn đề: trung bình, mặt trang dùng $q_*$ (“$V=v_*\Rightarrow Q_V=q_*$”) trong khi $q_*$ chỉ được định nghĩa trong notes trang chính sách ổn định. Trung bình, không nối với bảng tính tay ở trang trước. Nhẹ, “Điểm bất động tối ưu thỏa $v_*=T_*v_*$” không gợi lại phương trình Bellman tối ưu đã có.
- Quyết định: sửa. Tiêu đề giữ. Câu mở: “Mỗi ô của bảng lượt hai là một giá trị nhìn trước từ $V_1$.” Dòng cuối: “Với $V=v_\pi$, $Q_V=q_\pi$. Phương trình Bellman tối ưu, đã gặp khi xét chính sách ổn định, viết gọn là $v_*=T_*v_*$.” Chuyển $q_*$ và $V=v_*\Rightarrow Q_V=q_*$ vào notes cùng định nghĩa $q_*$.
- Kiểm tra: 634/720; hai kích thước đạt, không lỗi; đã xem ảnh.

### L04-E04 — Thuật toán lặp giá trị đồng bộ

- Trang muốn nói: quy trình đầy đủ của lặp giá trị đồng bộ gồm đầu vào, phần dư tối ưu, điều kiện dừng và đầu ra kèm chính sách trích từ bảng trả về.
- Vấn đề: nhẹ, $\Delta_*$ được định nghĩa như ký hiệu mới, không gợi lại $\Delta_\pi$ của thuật toán đánh giá. Nhẹ, $\pi_V$ trong hộp không có tên gọi. Trung bình (báo cáo lượt 1), khuôn bốn bước khác khuôn ba bước của thuật toán đánh giá đã sửa, làm mất ký hiệu chung để so sánh.
- Quyết định: sửa. Tiêu đề giữ. Định nghĩa “Phần dư tối ưu, thay $T_\pi$ bằng $T_*$ trong $\Delta_\pi$”. Quy trình ba bước cùng khuôn: kiểm ngưỡng hoặc đủ $K$ bảng mới thì trả $(V,\Delta)$ và kết quả so ngưỡng, ngược lại $V\leftarrow W$. Hộp gọi tên chính sách tham lam trích từ chính bảng trả về. Notes thay câu cũ về hết ngân sách bằng mô tả lần nhận bảng thứ $K$, trường hợp $K=0$ và ví dụ $K=1$ trên MDP hai trạng thái ($V_1=(1,3)$, $\Delta_*(V_1)=2{,}7$, chính sách $(b,b)$; đã kiểm: $T_*V_1=(2{,}7;5{,}7)$, phần dư $\max\{1{,}7;2{,}7\}=2{,}7$). Đồng bộ ý chính ở outline và quyết định ở storyboard.
- Kiểm tra: 620/720; hai kích thước đạt, không lỗi; đã xem ảnh.

### L04-E05 — Hội tụ của lặp giá trị

- Trang muốn nói: $T_*$ co với hệ số $\gamma$ như $T_\pi$, nên có điểm bất động duy nhất $v_*$ và lặp giá trị hội tụ với tốc độ $\gamma^k$; chặn này chứa $v_*$ nên chưa là điều kiện dừng.
- Vấn đề: trung bình, hộp cũ nêu nhu cầu “phép kiểm thực hành cần đại lượng tính được” nhưng trang lưới chen giữa trước khi phần dư được dùng. Nhẹ, không gợi lại tính co của $T_\pi$ đã có, làm tính co của $T_*$ trông như kết quả mới tách rời. Nhẹ, tiêu đề dài.
- Quyết định: sửa. Tiêu đề “Hội tụ của lặp giá trị”. Câu mở nối với $T_\pi$ (cùng giả thiết, $T_*$ cũng co). Câu giữa “Do đó $T_*$ có điểm bất động duy nhất…”. Hộp nêu đúng kết luận của trang: chặn theo $\gamma^k$ chứa $v_*$ chưa biết nên chưa là điều kiện dừng; câu nhu cầu đại lượng tính được chuyển lên đầu trang phần dư (giữ thứ tự E05–E07, bác đề xuất đổi thứ tự). Notes thêm chặn $30\cdot0{,}9^k$ cho MDP hai trạng thái (đã kiểm: $\|V_0-v_*\|_\infty=30$; sai số thật $27\cdot0{,}9^{k-1}=30\cdot0{,}9^k$ với $k\ge1$). Đồng bộ tiêu đề ở outline, storyboard.
- Kiểm tra: lần đầu “$0\le\gamma<1$” bị ngắt dòng giữa công thức; viết lại câu mở, 635/720; hai kích thước đạt, không lỗi; đã xem ảnh.

### L04-E06 — Lan truyền giá trị trên lưới năm ô

- Trang muốn nói: lặp giá trị đồng bộ trên mô hình có trạng thái kết thúc; mỗi lượt truyền giá trị thêm một ô và bảng đạt điểm bất động $V_4$. Bảng số đã kiểm.
- Vấn đề: nhẹ, mặt trang không ghi $V_4$ là điểm bất động, trong khi trang phần dư và câu hỏi kiểm tra trên lưới dùng điều này. Nhẹ, notes liệt kê sẵn mọi giá trị nhìn trước từ $V_4$, trùng đáp án câu hỏi kiểm tra mới trên lưới.
- Quyết định: sửa. Tiêu đề giữ. Chú thích thêm “$V_5=V_4$”. Notes ghi $V_4=v_*$ và kết luận chính sách đi phải, bỏ danh sách số (chuyển sang lời giải của trang kiểm tra lưới). Thuật ngữ “giá trị nhìn trước” đã thống nhất từ commit 0.
- Kiểm tra: 666/720; hai kích thước đạt, không lỗi; đã xem ảnh.

### L04-E07 — Phần dư và điều kiện dừng

- Trang muốn nói: phần dư tính được từ bảng hiện tại chặn sai số so với $v_*$, nên dùng làm điều kiện dừng; chính sách trích có thể đã tối ưu khi bảng còn xa nghiệm.
- Vấn đề: trung bình, trang mở bằng công thức, nhu cầu nằm ở trang hội tụ cách hai trang. Nhẹ, “sai số giá trị 27” mơ hồ giữa chặn và sai số thật (cả hai bằng 27: $2{,}7/0{,}1=27$; $\|V_1-v_*\|_\infty=\max\{26;27\}=27$). Nhẹ, tiêu đề nên nêu chức năng. Nhẹ, thẻ “Mô hình hai trạng thái” lệch tên “MDP hai trạng thái”.
- Quyết định: sửa. Tiêu đề “Phần dư và điều kiện dừng”. Thêm câu mở nêu nhu cầu và nối với $\Delta_\pi$. Thẻ phải: “MDP hai trạng thái”; “$\Delta_*(V_1)=2{,}7$; chặn và sai số thật đều bằng $27$”; “Chính sách tham lam $(b,b)$ đã tối ưu.” Thẻ trái rút còn “sai số không quá $0{,}1$ khi $\Delta_*(V)\le0{,}01$”. Notes bỏ câu về lưới (đã chuyển sang trang lưới), đổi “mô hình hai trạng thái” thành “MDP hai trạng thái”. Đồng bộ tiêu đề và quyết định ở outline, storyboard.
- Kiểm tra: bản đầu tràn (748/720); rút hai thẻ, 694/720; hai kích thước đạt, không lỗi; đã xem ảnh.

### L04-E08 — Kiểm tra lặp giá trị trên lưới

- Trang muốn nói: kiểm tra cập nhật tối ưu, phần dư và quy ước trạng thái kết thúc trên lưới.
- Vấn đề: trung bình, câu 1 cũ yêu cầu tính $V_3(c_1)$, $V_3(c_2)$, nhưng đáp án $-2{,}71$ và $6{,}2$ đã in ở hàng $k=3$ của bảng lan truyền; câu hỏi không đo được năng lực. Nhẹ, chưa kiểm phần dư vừa học. Nhẹ, tiêu đề dài.
- Quyết định: sửa. Tiêu đề “Kiểm tra lặp giá trị trên lưới”. Dữ kiện $V_4=(4{,}58;6{,}2;8;10;0)$. Câu 1: tính hai giá trị nhìn trước tại $c_1$ và $c_3$, xác định $\Delta_*(V_4)$ và chính sách trích. Câu 2 giữ, đổi chỉ số thành $V_4(c_5)$. Lời giải đã kiểm: $c_1$ trái $3{,}122$, phải $4{,}58$; $c_3$ trái $4{,}58$, phải $8$; $c_2$: $\max\{3{,}122;6{,}2\}$; $c_4$: $\max\{6{,}2;10\}$; $T_*V_4=V_4$, $\Delta_*(V_4)=0$, chính sách đi phải. Đồng bộ outline (luận điểm, ý chính, yêu cầu, đáp án, tiêu chí) và storyboard.
- Kiểm tra: 560/720; hai kích thước đạt, không lỗi; đã xem ảnh.

### L04-F01 — Chi phí một lượt quét

- Trang muốn nói: một lượt quét toàn bảng tốn $O(n^2m)$ với mô hình đặc hoặc $O(nmd)$ với mô hình thưa; vì vậy cần cách phân bổ công việc khác lượt đồng bộ.
- Vấn đề: trung bình, trang mở mạch F mà không có điểm vào từ mạch E (“Đặt $n=|\mathcal S|$…” ngay dòng đầu). Trung bình, “Thay lịch cập nhật” trong hộp xuất hiện đột ngột vì khái niệm lịch chưa có. Nhẹ, giả thiết “đã gộp phần thưởng thành kỳ vọng” đứng sau bảng dù bảng dựa vào nó.
- Quyết định: sửa. Tiêu đề “Chi phí một lượt quét”. Câu mở nối với lượt đồng bộ của đánh giá và lặp giá trị, đưa giả thiết gộp thưởng lên trước bảng. Hộp nêu hai hướng thay đổi cụ thể: dùng ngay giá trị mới trong cùng lượt (trang tại chỗ) và chọn trạng thái cần cập nhật (trang bất đồng bộ). Notes giữ. Đồng bộ tiêu đề ở outline, storyboard.
- Kiểm tra: 636/720; hai kích thước đạt, không lỗi; đã xem ảnh.

### L04-F02 — Cập nhật tại chỗ và thứ tự trạng thái

- Trang muốn nói: dùng ngay giá trị mới trong cùng lượt làm thay đổi kết quả, và thứ tự quét quyết định tốc độ lan truyền. Số đã kiểm: tại chỗ $(1;2{,}9)$ so với đồng bộ $(1,2)$; lưới ngược thứ tự cho $(4{,}58;6{,}2;8;10;0)$ trong một lượt.
- Vấn đề: trung bình, “tại chỗ” không được định nghĩa trên mặt trang. Trung bình, ví dụ lưới chỉ là mệnh đề không có số, và dùng $T_*$ trong khi ví dụ bên trái dùng $T_{\pi_0}$ mà không nói rõ.
- Quyết định: sửa. Tiêu đề giữ. Thêm định nghĩa “Tại chỗ: giá trị mới ghi đè ngay và được dùng cho các ô sau trong cùng lượt.” Phép tính hai trạng thái gộp thành một dòng (kết quả ở hộp). Dòng lưới ghi rõ $T_*$ và kết quả “một lượt cho $(4{,}58;6{,}2;8;10;0)$, bằng $V_4$ của bốn lượt đồng bộ”. Notes đổi dấu thập phân và thêm hai bước $c_2$, $c_1$.
- Kiểm tra: bản đầu tràn (744/720), rồi công thức bị ngắt dòng; rút phép tính, 626/720; hai kích thước đạt, không lỗi; đã xem ảnh.

### L04-F03 — Thuật toán lặp giá trị bất đồng bộ

- Trang muốn nói: cập nhật từng trạng thái theo một lịch, dùng giá trị mới nhất; hội tụ khi mọi trạng thái chưa kết thúc được cập nhật vô hạn lần.
- Vấn đề: nhẹ, ý “quét tại chỗ là một lịch cụ thể; bất đồng bộ tổng quát không cần quét đủ lượt” chỉ có trong notes, trong khi đây là cầu nối từ trang tại chỗ. Nhẹ, tiêu đề không cho biết trang là quy trình; notes còn “mô hình hai trạng thái”.
- Quyết định: sửa. Tiêu đề “Thuật toán lặp giá trị bất đồng bộ”. Thêm câu mở “Mỗi bước cập nhật một trạng thái do lịch chọn; quét tại chỗ là một lịch cụ thể.” Gộp câu đầu ra vào bước 3 để giữ trang trong khung. Notes: “MDP hai trạng thái”. Đồng bộ tiêu đề ở outline, storyboard.
- Kiểm tra: bản đầu tràn (743/720); gộp đầu ra vào bước 3, 612/720; hai kích thước đạt, không lỗi; đã xem ảnh.

### L04-F04 — Lặp chính sách tổng quát

- Trang muốn nói: lặp chính sách, lặp giá trị và lịch bất đồng bộ là các cách xen kẽ đánh giá và cải thiện; khi cả hai quá trình cùng ổn định thì đạt tối ưu.
- Vấn đề: trung bình, mặt trang chỉ mô tả, chưa nêu kết quả; phát biểu “ổn định chung ⇒ $V=v_*$” chỉ có trong notes. Nhẹ, câu “GPI mô tả tương tác…” chưa nói GPI gọi chung điều gì.
- Quyết định: sửa. Tiêu đề giữ. Câu mở “Lặp chính sách tổng quát (GPI) gọi chung sự xen kẽ giữa đánh giá và cải thiện.” Thêm hộp “Khi cả hai cùng ổn định, $V=v_\pi$ và $\pi$ tham lam theo $V$, nên $V=T_*V=v_*$.” Rút chữ ba thẻ để giữ trang trong khung; ý “khác nhau ở mức hoàn tất đánh giá” chuyển vào notes. Câu nối sang CartPole đặt ở trang rời rạc hóa (theo báo cáo E–G).
- Kiểm tra: bản đầu tràn (779/720), rút thẻ còn 727, rút câu mở còn 683/720; hai kích thước đạt, không lỗi; đã xem ảnh.

### L04-F05 — Rời rạc hóa trạng thái CartPole

- Trang muốn nói: áp dụng quy hoạch động cho trạng thái liên tục cần rời rạc hóa (ở đây $3\cdot3\cdot6\cdot6=324$ ô, đã kiểm) và vẫn cần mô hình chuyển–thưởng.
- Vấn đề: trung bình, rời rạc hóa xuất hiện đột ngột; mặt trang không nêu nhu cầu “các quy trình trên cần tập trạng thái hữu hạn và mô hình $p$ đã biết” (câu nối chỉ có trong notes trang GPI). Nhẹ, tiêu đề gộp hai ý.
- Quyết định: sửa. Tiêu đề “Rời rạc hóa trạng thái CartPole”. Thêm câu mở “Các quy trình trên cần trạng thái hữu hạn và $p$ đã biết; CartPole có trạng thái liên tục.” Gộp “Trạng thái $(x,\dot x,\theta,\dot\theta)$; chia lần lượt $3,3,6,6$ khoảng” thành một dòng để tránh lặp “liên tục”. Giữ kích thước hình để nhãn hình đọc được (đã thử lớp `figure short`, nhãn còn khoảng 0,56em nên bỏ). Đồng bộ tiêu đề ở outline, storyboard.
- Kiểm tra: bản đầu 703/720 với hộp chạm chân trang; rút câu mở, 656/720; hai kích thước đạt, không lỗi; đã xem ảnh.

### L04-F06 — Kiểm tra lịch cập nhật và mô hình

- Trang muốn nói: kiểm tra hai điều kiện áp dụng: lịch phải bao phủ mọi trạng thái chưa kết thúc và mô hình phải được biết.
- Vấn đề: trung bình, câu 1 “giá trị không được khôi phục” mơ hồ; lời giải chỉ nêu $V(s_1)=0$, bỏ qua hệ quả $V(s_0)\to10$ thay vì $27$ (đã kiểm: $x=\max\{1+0{,}9x;0\}$ có nghiệm $x=10$). Nhẹ, notes có câu khuyên răn “Phải kiểm tra điều kiện của thuật toán trước khi diễn giải đầu ra.” Nhẹ, tiêu đề dài.
- Quyết định: sửa. Tiêu đề “Kiểm tra lịch cập nhật và mô hình”. Câu 1 yêu cầu giới hạn của $V(s_0)$, giá trị $V(s_1)$, so sánh với $v_*=(27,30)$ và nêu điều kiện bị vi phạm. Lời giải thêm phép tính $V(s_0)\to10$. Xóa câu khuyên răn trong notes. Đồng bộ tiêu đề, yêu cầu và đáp án ở outline, storyboard.
- Kiểm tra: 583/720; hai kích thước đạt, không lỗi; đã xem ảnh.
