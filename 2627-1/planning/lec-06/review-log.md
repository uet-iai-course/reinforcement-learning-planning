# Nhật ký xây dựng lại Bài 06

## Yêu cầu và trạng thái

Ngày 29-09-2026. Người dùng yêu cầu loại toàn bộ dàn bài Bài 06 hiện hành, lập mới bằng `$build-slide-deck-outline`, rồi viết lại RevealJS theo Sutton–Barto với hệ ký hiệu thống nhất. Tiêu đề, nội dung, chú thích, notes và học liệu dùng tiếng Việt trang trọng, học thuật; áp dụng `$no-ai-slop` và kiểm mạch bằng Quill. Không tạo dự án sách hoặc `quill.json`.

Trạng thái khi mở nhật ký: đã chấp nhận phân tích nguồn, đối chiếu học thuật và kiểm chứng toán; mở giai đoạn viết dàn bài mới, chưa thay HTML/học liệu ở thời điểm đó. Các mục sau ghi diễn tiến; kết quả nghiệm thu cuối ở cuối tệp. Dàn bài, storyboard, ghi chú biên soạn và nhật ký cũ đã được loại khỏi thư mục quy trình; bản lưu tạm nằm tại `/tmp/rl06-rebuild/old-planning/`, chỉ phục vụ khôi phục, không dùng làm đầu vào soạn. Không kế thừa kết luận rà soát hoặc ủy quyền mô hình của lần dựng trước.

## Nguồn và đầu ra

- Nguồn học phần: `RL-hk2-2025-2026/lecture-06-model-free-control.pdf`, 30 trang; tên và tác giả Tạ Việt Cường được xác nhận trên trang 1. Chủ đề gồm điều khiển Monte Carlo, Sarsa, Q-learning và điều kiện hội tụ.
- Sườn học thuật: Sutton–Barto, *Reinforcement Learning: An Introduction*, ấn bản 2; sách đã có tại `/tmp/rl04-rebuild/RLbook2020.pdf`. Vị trí dùng cụ thể phải được phân tích và xác nhận trước soạn.
- `resources/` không có hw06 riêng. Bài tập và phần chữa 30 phút lấy theo nội dung tương ứng đã kiểm trong nguồn; không mặc định chuyển bài tập của tuần khác. Chưa xác nhận có code demo.
- Đầu ra: HTML `2627-1/lecture-06-dieu-khien-phi-mo-hinh.html`; SVG trong `img/lec-06/`; bốn tệp `analysis.md`, `outline.md`, `storyboard.md`, `review-log.md` trong thư mục này; học liệu `materials/lec-06/lecture-note.md`; mô tả Bài 06 trong index.
- Dự kiến bảy mạch, khoảng 45 trang và 120 phút trình chiếu; 30 phút chữa bài riêng. Mỗi mạch có trang kiểm tra riêng. Số trang chỉ được chốt sau phân tích nguồn.

## Điều phối và chấp nhận kế hoạch

Chỉ dùng `collaboration` gốc của Codex với cấu hình `model: gpt-6-astra`, `reasoning_effort: xhigh`, `fork_turns: none`. Các tên dưới đây là cấu hình được chỉ định trong lời gọi; không tự suy diễn mô hình thực chạy hoặc tuyến xác thực từ lời tự khai. Không gọi OpenRouter, script/API/CLI mô hình, không đọc hoặc nạp `.env`, `.env.*` hay bí mật. Quy định điều phối đã được đối chiếu với `../math-4-AI/AGENTS.md`.

| Tác tử | Vai trò và quyền | Bàn giao | Cấu hình được chỉ định |
|---|---|---|---|
| `lec06_rebuild_planner` | Lập kế hoạch; chỉ đọc kho | `/tmp/rl06-rebuild/plan.md` | GPT-6-Astra, xhigh, native |
| `lec06_source_analysis` | Đọc toàn bộ nguồn, ánh xạ và kiểm kê; không sửa kho | `/tmp/rl06-rebuild/source-analysis.md` | GPT-6-Astra, xhigh, native |
| `lec06_academic_research` | Đối chiếu slide đại học và mạch học; không sửa kho | `/tmp/rl06-rebuild/research.md` | GPT-6-Astra, xhigh, native |
| `lec06_theory_audit` | Kiểm chứng mệnh đề trọng điểm về cải thiện, hội tụ, hiệu chỉnh khác chính sách và chặn mẫu; không sửa kho | `/tmp/rl06-rebuild/theory-audit.md` | GPT-6-Astra, xhigh, native |

Điều phối viên đã đọc và chấp nhận kế hoạch riêng trước khi giao phân tích chi tiết. Bảy mạch là phương án dự kiến, không là giới hạn cứng ép nội dung. Chuỗi dự đoán → giá trị hành động/thăm dò → MC → Sarsa → Q-learning → điều kiện bảo đảm → kết luận sẽ được xác nhận theo nguồn. Các điều kiện vận hành phải có trước thuật toán; mạch bảo đảm hệ thống hóa thay vì bổ sung ngầm tiên quyết.

Các cổng tiếp theo: chấp nhận đủ phân tích nguồn/nghiên cứu/toán; một tác tử viết dàn mới; kiểm định storyboard độc lập trước HTML và đối chiếu sau triển khai; hoàn thiện notes/học liệu; năm vai độc lập đọc cùng bản cố định; editor riêng; rà lại đúng phạm vi; kiểm tĩnh, số học, SVG, KaTeX, rộng/hẹp, bàn phím, liên kết và Codex Slides. Chỉ một tác tử được ghi kho tại một thời điểm.

## Kiểm kê kỹ thuật ban đầu

Đã đọc cấu trúc/cấu hình của template, hệ lớp CSS chung và mục Bài 06 trong index. Chỉ kế thừa kỹ thuật, không dùng nội dung hay CSS nội dòng của template. Thư viện RevealJS, KaTeX, Notes và Highlight dùng cục bộ; chưa sửa CSS chung. `pdfimages -list` không có ảnh raster trong nguồn. Bản trích văn bản có 30 trang; các hình và công thức cần được kiểm trực tiếp ở bước phân tích.

Dự án Codex Slides đã mở: `20260824175305-chuy-n-lecture-6-i-u-khi-n-phi-m-h-nh-mo-c905`, trạng thái clarify, 0 trang. Điều phối đã xem giao diện cục bộ bằng Chromium, không có lỗi trang. Liên kết chính xác trả về từ công cụ mở dự án được giữ trong `/tmp/rl06-rebuild/codex-initial-report.json`; ứng dụng chuyển trang chưa có outline tới trang tiếp tục yêu cầu. Chưa dựng hoặc xác nhận nội dung mới.

Phiên không có công cụ Browser tích hợp. Kiểm bằng Chromium cục bộ và thao tác dự án xác định được ghi đúng phạm vi; không gọi các chức năng sinh nội dung hoặc ảnh qua mô hình của plugin. Giới hạn Browser sẽ được ghi trong bàn giao.

Các thay đổi chưa commit của Bài 05 và tệp dùng chung được lưu dấu SHA trong `/tmp/rl06-rebuild/unrelated-baseline-sha.json`; phạm vi Bài 06 không sửa các tệp này. Script kiểm kỹ thuật được chuẩn bị ở `/tmp/rl06-rebuild/`, chưa dùng kết quả của Bài 05 làm bằng chứng cho Bài 06.

## Chấp nhận đầu vào nghiên cứu và toán học

Điều phối viên đã đọc đủ ba báo cáo source-analysis, research và theory-audit; công cụ collaboration xác nhận ba tác tử đã hoàn tất. Nguồn được ánh xạ đủ30/30trang. Đã đối chiếu trực tiếp UCL/Silver và StanfordCS234; giới hạn truy cập nguồn phụ Stanford2023 phải được giữ trong analysis. Nguồn không có mã hoặc hình raster cần chuyển. Quyết định nội dung được chốt trong `/tmp/rl06-rebuild/accepted-inputs.md` để bàn giao tác tử dàn bài; nội dung và nguồn phải được tổng hợp vào analysis/storyboard mới.

Giữ chuỗiA–E xuyên suốt, hai bảng khởi tạo nguồn cho hai bài MC; Sarsa và Q-learning dùng cùng bảngI và năm chuyển đã xác định. Giới hạn ba bước của nguồn được làm rõ là độ dài lượt minh họa; trạng thái kết thúc thật làA/E. MC dùng lần ghé đầu theo Sutton–Barto, đếm mẫu riêng cho từng cặp. Định lý cải thiện với q_pi chính xác tách khỏi cập nhật Q theo mẫu; GLIE tách bao phủ khỏi giảm epsilon; Robbins–Monro theo số cập nhật từng cặp. Định lý Sarsa/Q-learning dùng miền gamma<1, không suy từ ví dụ gamma1/bước học0.8. Công thức V ở nguồn19 được sửa nhãn trong học liệu; chặn nguồn29 dành cho đánh giá chính sách cố định và đưa sang đọc thêm. Không thêm slide chứng minh riêng cho hai nội dung này.

Các phép tính chuỗiA–E đã được điều phối viên kiểm bằng phân số trong `/tmp/rl06-rebuild/check_numbers.py`; dữ liệu đầu vào và kết quả phải xuất hiện đầy đủ trong storyboard/học liệu. Báo cáo Detect của ba tác tử là phân tích nguồn, chưa thay cho năm báo cáo độc lập của bản nháp mới.


## 2026-09-29 — Xây dựng lại dàn bài từ nguồn, giai đoạn soạn

### Vai trò, đầu vào và phạm vi

Tác tử `/root/lec06_outline_writer` nhận vai soạn dàn bài mới, sau khi điều phối viên chấp nhận kế hoạch, phân tích nguồn, nghiên cứu đối chiếu, kiểm toán toán học và kết quả tính số. Mô hình được điều phối chỉ định trong giao nhiệm vụ là `gpt-6-astra`, mức suy luận `xhigh`, qua cơ chế tác tử gốc của Codex. Mục này ghi nhận chỉ định; không dùng lời tự khai làm bằng chứng mô hình thực chạy hoặc tuyến xác thực. Không tạo tác tử con, không dùng OpenRouter, API/CLI gọi mô hình, không đọc `.env` hoặc bí mật.

Tác tử giữ quyền ghi duy nhất trong giai đoạn này: tạo mới `analysis.md`, thay toàn bộ `outline.md` và `storyboard.md` bằng dàn mới, chỉ nối thêm nhật ký. Không đọc hoặc kế thừa dàn bài, HTML hay học liệu Bài 06 cũ; không đọc bản sao lưu cũ. Không sửa HTML, SVG, materials, index, CSS hoặc Bài 05; không commit/push. Phạm vi giao cho tác tử ở giai đoạn này dừng ở dàn bài, nên tác tử chưa triển khai slide hoặc tài sản. Mục tiêu chung của người dùng vẫn bao gồm viết lại bộ trang chiếu theo dàn mới.

Đã đọc AGENTS.md, [build-slide-deck-outline](/home/tqlong/.codex/skills/build-slide-deck-outline/SKILL.md) và output-template.md, [no-ai-slop](/home/tqlong/.codex/skills/no-ai-slop/SKILL.md) và eval.md, [quill](/home/tqlong/.codex/skills/quill/SKILL.md) cùng Outline Workflow. Áp dụng no-ai-slop chế độ Edit; Quill chỉ rà mạch khái niệm, thuật ngữ và tính liên tục, không tạo `quill.json`.

Đầu vào được chấp nhận gồm kế hoạch, phân tích đủ 30 trang, báo cáo UCL/Stanford, kiểm toán sáu cụm lý thuyết và bảng số hữu tỉ. Danh mục nguồn, tác giả, URL, vị trí đọc, giới hạn truy cập và các quyết định học thuật được tổng hợp đầy đủ trong analysis.md; các tệp tạm không là nguồn học thuật duy nhất. Đã đọc nguồn trích đủ 30 trang, mẫu RevealJS, CSS dùng chung và index để xác định nền kỹ thuật. Không sao chép chủ đề hoặc metadata Cơ sở toán học cho AI từ mẫu.

### Kết quả dàn mới và thay đổi có chủ ý

Dàn có 45 trang, bảy mạch, 120 phút gồm thời gian bảy kiểm tra riêng: A05, B07, C08, D08, E08, F05, G03. Phân bổ số trang/phút là A:5/10, B:7/18, C:8/22, D:8/22, E:8/22, F:5/16, G:4/10. Chữa bài riêng 30 phút dùng bài nguồn và H03 phần bảng tra; không có demo mới. Mở đầu theo thứ tự giới thiệu → nội dung → động lực; kết luận trở lại quyết định tại D và giới hạn của bảng sau hữu hạn mẫu.

Sườn Sutton–Barto được dùng qua quan hệ phụ thuộc: giá trị hành động (§5.2), vòng đánh giá–cải thiện (§5.3), thăm dò và MC theo chính sách (§5.4), Sarsa (§6.4), Q-learning (§6.5). UCL và Stanford được dùng để đối chiếu mạch, cách dùng chung dữ kiện, hình và kiểm tra; không sao chép CSS hoặc tài sản. Đưa ví dụ số trước quy tắc tổng quát, đặt phép tính tại cụm khái niệm, tách giả mã dài qua hai trang liền nhau.

| Quyết định đã áp dụng | Căn cứ và tác động |
|---|---|
| Chuỗi A–E xuyên bài; đưa dữ kiện nguồn 15 lên động lực | Giảm số môi trường phải học; mọi thuật toán nhận mẫu, dù mô hình được công bố để kiểm số. |
| Sửa giới hạn ba bước | A/E là kết thúc thật; ba bước chỉ là độ dài lượt MC minh họa. Mẫu 5 dừng ở C vẫn có giá trị tiếp nối. |
| MC lần ghé đầu theo cặp, N0=0, chính sách giữ trong lượt | Xác định biến thể còn mơ hồ ở nguồn 10–11; đúng SB tr.101 và H03. Quỹ đạo/f được đặt lại mỗi lượt, Q/N tích lũy. |
| Hoàn thiện dãy số nguồn 17 | Dùng u_j, quy tắc tiêu thụ số phụ và đầu mút rõ. Dãy tất định chỉ phục vụ thao tác, không gọi là mẫu đều độc lập hoặc bằng chứng GLIE. |
| Sarsa/Q-learning dùng chung năm mẫu và hai bản sao bảng I | Hoàn thiện đề thiếu dữ kiện, đổi bảng đầu của Q-learning nguồn 21; chỉ thay cách tạo mục tiêu khi so sánh. |
| Phân biệt q đúng/Q ước lượng và ký hiệu liên bài | Giữ “lợi tức”, S/S^+, R_{t+1}, v/V, q/Q, b/π như Bài05; t là tương tác, k là lượt MC, n là cập nhật riêng của cặp. |
| Cải thiện mềm đặt cạnh cơ chế chọn hành động | Cùng ε, qπ chính xác, miền γ<1; phép chứng minh dài vào ghi chú, không gán cho từng cập nhật Q từ mẫu. |
| Sửa GLIE, bước học và bảo đảm hội tụ | Hai yêu cầu riêng, tập cực đại xử lý đồng hạng, bước học đếm theo cặp; γ=1/α=.8 của ví dụ tách khỏi miền định lý. Không giữ định lý MC tổng quát thiếu giả thiết nguồn 26. |
| Nguồn19 và29 chuyển đọc thêm | Nguồn19 sửa đúng đối tượng V và ngoặc hệ số nhân mục tiêu; nguồn 29 là đánh giá π,d0 cố định bằng các lợi tức độc lập bị chặn. Không mở thêm trang chứng minh hoặc làm tiên quyết Q-learning. |
| Lược bảng thuật toán sâu nguồn 23 | Ánh xạ đủ các tên bị lược trong outline; chưa có tiên quyết cho ma trận ấy và không phục vụ bước tính bảng trong 120 phút. |
| Kiểm tra C08 có cặp lặp, E08 dùng bảng chung | Ví dụ sư phạm suy từ đúng môi trường/bảng đã học, ghi rõ phần bổ sung. Không tạo dữ liệu thực nghiệm hoặc môi trường chính thứ hai. |

Bổ sung chính sách tiếp nối riêng $\pi_L$ luôn chọn trái tại B,C,D để nối ví dụ với định nghĩa giá trị hành động. Khi đó $q_{\pi_L}(D,0)=998$ và $q_{\pi_L}(D,1)=10$; cả hai có cùng chính sách tiếp nối và lợi tức hữu hạn. Ví dụ này không đổi bảng I, chính sách tham lam bảng I hoặc các dữ liệu MC/Sarsa/Q-learning. Vòng B↔C của chính sách tham lam vẫn được giữ để phân biệt miền có giá trị hữu hạn.

### Quyết định với kiểm định độc lập trong lúc soạn

Điều phối viên cung cấp hai báo cáo chỉ đọc của vai `lec06_storyboard_gate`: giai đoạn1 đọc A–B và bản đồ toàn tuyến; giai đoạn2 đọc C–G cùng các ranh giới. Các báo cáo không phát hiện lỗi mức chặn bàn giao hoặc nghiêm trọng trong phạm vi đã đọc, nhưng yêu cầu xác nhận bản sửa cuối trước mở gate HTML. Tác tử soạn đã tiếp nhận các đề xuất được điều phối viên chấp nhận; không coi việc tự sửa là lượt xác nhận độc lập.

| Mã | Quyết định, vị trí và bằng chứng xử lý |
|---|---|
| SG1 | Áp dụng ở B01–B02: chính sách tiếp nối cụ thể π_L trước định nghĩa; hai qπL đã được root tính lại. Đồng bộ HT1, bản đồ khái niệm và outline. |
| SG2 | Áp dụng ở B02: t, T, R_{j+1}, miền0≤t<T, tổng rỗng và T khác ngân sách được giải thích trong ghi chú. |
| SG3 | Áp dụng ở B07: đề hỏi trực tiếp bảng khởi tạo đã đủ căn cứ cải thiện hay chưa; đáp án/tiêu chí nêu Q chưa là qπ chính xác và miền γ của mệnh đề. Giữ3 phút. |
| SG4 | Áp dụng ở A01/B06 và rà rộng mọi phiếu: đổi lời biên soạn thành phát biểu học thuật; chuyển chỉ dẫn bố cục ra khỏi ghi chú. |
| SG5 | Áp dụng ở A01/A04: mở rộng Monte Carlo(MC), quá trình quyết định Markov(MDP), sai phân thời gian(TD) ở lần đầu. |
| SG2-01 | Áp dụng C05/C06: K nguyên dương, k=1; đầu lượt đặt lại quỹ đạo/f, t=0, lấy trạng thái đầu; giữ Q/N. Vòng lấy hành động và chuyển tiếp rõ; sau cập nhật chỉ tăng k và quay về đầu lượt. |
| SG2-02 | Đổi D07 thành “Cập nhật khi chuyển vào trạng thái kết thúc”; luận điểm xác định trạng thái kế tiếp kết thúc, ô cập nhật vẫn là cặp trước chuyển. Đồng bộ outline. |
| SG2-03 | Sửa luận điểm E06: giá trị tiếp nối tại B tạo hai mục tiêu cho cập nhật(C,0); giá trị tại C sau đó dùng cho cập nhật(D,0). Không gọi là mục tiêu tại B. |
| SG2-04 | D08 hỏi trực tiếp thời điểm lấy A', có lấy lại sau cập nhật hay không và tác động của dừng ngân sách. Lời giải giữA' nếu tiếp tục, không buộc thực hiện khi đã dừng; giữ3 phút. |
| Biên tập do root phát hiện | Đã viết lại các đoạnD/G có từ dính, thay “counter” bằng “bộ đếm”, “ratio” bằng “tỉ số”, dùng tiếng Việt cho kết thúc/lần ghé. Loại mã trang nội bộ khỏi mọi trường mặt trang/ghi chú; G04 chỉ giữ nội dung học thuật, lịch chữa và tham chiếu planning chuyển sang trường bố cục. |
| Ký hiệu đọc thêm | DT2 dùng $G^{(i)}$ cho lợi tức ngẫu nhiên của lượt độc lập i; n được khai báo lại là số lượt, khác số cập nhật theo cặp trong tuyến chính. |

### no-ai-slop Edit và tự đối chiếu eval.md

Phạm vi: toàn bộ analysis, outline, 45 phiếu storyboard, đặc biệt tiêu đề, nội dung mặt trang và ghi chú dự kiến. Văn phong học thuật và các phân biệt toán học được ưu tiên; định nghĩa, nhãn kết quả, tổng hợp có chức năng và câu hỏi đánh giá được giữ. Không dùng điểm bộ phát hiện AI hoặc suy đoán tác giả.

| Nhóm kiểm trong eval.md | Kết quả sau sửa |
|---|---|
| Editing1: giữ ý, không thêm nhận định thiếu căn cứ | Đạt: ví dụ bổ sung được đánh dấu và kiểm số; không gán cho nguồn. |
| Editing2: giữ từ vựng và mức trau chuốt phù hợp | Đạt: thống nhất thuật ngữ Học tăng cường, giữ giọng học thuật. |
| Editing3: không sửa câu rõ chỉ để đồng dạng | Đạt: thay ở chỗ mơ hồ, dính chữ hoặc sai quy chiếu; giữ các định nghĩa rõ. |
| Editing4: không cắt quá mức | Đạt: đủ giả thiết, dữ kiện, quy trình, đáp án; lời giải dài chuyển vào ghi chú. |
| Editing5: đặt điều người học cần ở đầu | Đạt: vấn đề và ví dụ trước hình thức, mỗi phiếu có luận điểm cụ thể. |
| Editing6: đưa ý chính lên trước có chọn lọc | Đạt: tiêu đề/luận điểm phục vụ chức năng trang; không ép mọi bước thành cùng kiểu câu. |
| Editing7: câu có dữ kiện và động từ rõ | Đạt: bỏ lời nhấn mạnh không có nội dung; giữ các bước tính và yêu cầu thực hiện. |
| Editing8: loại câu chung có thể chuyển sang mọi bài | Đạt: câu nối nêu đối tượng cụ thể Q, lợi tức, hành động hoặc điều kiện. |
| Editing9: chủ thể và động từ rõ | Đạt: tác tử chọn hành động; bảng được cập nhật theo cặp; không nhân hóa sơ đồ. |
| Editing10: giữ cấu trúc có chức năng | Đạt: bảy mạch và ví dụ nguồn; thay thứ tự được ghi rõ lý do. |
| Editing11: sửa câu rối, giữ độ chính xác | Đạt: chia phần giả mã và lời giải; không bỏ lượng từ/giả thiết để rút câu. |
| Words1: từ cấm và lời nhấn mạnh rỗng | Đạt: không có khẩu hiệu, quảng bá, “điểm đáng chú ý” hoặc lời ca tụng. |
| Patterns1: dẫn rỗng, câu hỏi tu từ, đối lập giả | Đạt: các đối chiếu còn lại là phân biệt toán học cần thiết; câu hỏi đều có nhiệm vụ. |
| Patterns2: câu khuôn, kết luận giả sâu, đổi đồng nghĩa | Đạt: dùng nhất quán lợi tức, bước học, thăm dò, mục tiêu, Sarsa. |
| Patterns3: nguồn mơ hồ hoặc lời đánh giá thiếu căn cứ | Đạt: nguồn/trang/URL và phạm vi đọc đã ghi; không suy ưu thế mẫu chung. |
| Patterns4: siêu diễn ngôn/chỉ dẫn người soạn trong sản phẩm | Đạt: các chỉ dẫn chuyển ra trường bố cục/quan hệ; ghi chú là giải thích học thuật. |
| Patterns5: kết luận kịch tính | Đạt: kết ở năng lực, giới hạn, bài tập và nguồn đọc có căn cứ. |
| Patterns6: tổng kết rỗng | Đạt: G02 thu hồi quyết định tại D, G03 kiểm chọn phương pháp; không lặp mục lục. |
| Patterns7: trang trí định dạng | Đạt: bảng dùng để ánh xạ/so sánh; không emoji, ảnh trang trí hoặc nhãn nội bộ trên nội dung. |
| Patterns8: nhãn và dấu hai chấm | Đạt: dùng cho trường kỹ thuật, nhãn câu hỏi và tiêu đề thuật toán, không gây kịch tính. |
| Patterns9: gạch ngang | Đạt: gạch dùng cho khoảng trang, tên riêng và chuỗi; không dùng làm nhịp câu lặp. |
| Final1: tự đối chiếu trực tiếp eval | Đạt: tác tử soạn tự đọc và sửa trước bàn giao; không giao việc tự kiểm cho reviewer. |
| Final2: nhịp câu và đối xứng máy móc | Đạt: khung phiếu lặp để kiểm định, nội dung và quan hệ cụ thể theo từng trang. |
| Final3: giữ giọng phù hợp người dùng | Đạt trong phạm vi học liệu học thuật; không thêm giọng hội thoại/hài hước. |
| Final4: đọc lại tự nhiên và chính xác | Đạt sau lượt sửa khoảng trắng, thuật ngữ và quy chiếu; giữ đủ các phân biệt toán học. |
| Final5: bản đầy đủ và thay đổi | Đạt: bản đầy đủ nằm trong ba tệp mới; mục thay đổi và quyết định tại nhật ký này. |
| Final6: yêu cầu Detect khi được giao Detect | Không áp dụng cho tác tử soạn chế độ Edit; báo cáo độc lập đã nêu mẫu, trích bằng chứng và đề xuất, không chấm điểm tác giả. |

Quill được dùng để đối chiếu đầu vào–đầu ra và các mạch khái niệm: A nêu thiếu dữ liệu hành động; B xác định giá trị/thăm dò; C cần lợi tức hoàn chỉnh; D tạo mục tiêu theo hành động thật; E tách hành vi/đích; F giới hạn bảo đảm; G thu hồi quyết định tại D. Ví dụ và ký hiệu đi xuyên từ bước tính sang công thức/giả mã; chính sách π_L minh họa giá trị được tách khỏi bảng I và các lần chạy thuật toán. Không có phần trọng tâm mới ở kết luận; hai nội dung đọc thêm không trở thành tiên quyết ngầm.

### Kiểm tra đã thực hiện và giới hạn còn lại

- Đếm bằng script:45 heading duy nhất,7 mạch;45 hàng outline khớp thứ tự/tiêu đề của storyboard; thời lượng từng phiếu khớp outline; tổng120 phút. Ánh xạ đủ30 trang nguồn.
- Xác nhận bảy trang kiểm tra riêng có mặt trang, đáp án, tiêu chí và thời gian suy nghĩ/trả lời/chữa; không dùng câu hỏi rải rác thay kiểm tra của phần.
- Kiểm số từ bảng đã được root/auditor chấp nhận; tự tính lại C08 bằng số hữu tỉ cho 996/998→996 hoặc 997, kiểm xác suất 1/8,7/8 và đồng hạng, E08 cho 0/799. Các kết quả năm mẫu, H03 và π_L đã được điều phối viên kiểm độc lập.
- Quét các trường mặt trang/ghi chú:không có data-slide-id hoặc mã A01–G04, tham chiếu analysis/outline/storyboard, từcounter/terminal/ratio hoặc lời dẫn biên soạn đã phát hiện. Kiểm liên kết nội bộ của ba tệp hợp lệ; công thức Markdown không dùng dấu phân cách bị cấm.
- Chưa triển khai HTML/SVG hoặc học liệu công khai; chưa chạy kiểm trực quan, KaTeX, bàn phím, tràn trang hoặc Codex Slides cho bản mới. B06,C04,D02,F04,G01 và các cặp trang giả mã là vị trí cần kiểm mật độ khi dựng.
- Gate độc lập cuối vẫn cần đọc bản đã sửa và xác nhận SG1–SG5/SG2-01–04 cùng các ranh giới. Điều phối viên quyết định mở bước HTML; tác tử soạn dừng sau bàn giao dàn bài.


## Chấp nhận storyboard trước triển khai HTML — 29-09-2026

Điều phối viên đã đọc báo cáo cuối của `/root/lec06_storyboard_gate`, hai báo cáo giai đoạn trước và các thay đổi của dàn cuối. Tác tử rà được tạo bằng cơ chế `collaboration` gốc với mô hình chỉ định `gpt-6-astra`, mức suy luận `xhigh`; thông số lời gọi là bằng chứng cấu hình, không là xác nhận độc lập tuyến xác thực thực chạy. Vai rà chỉ đọc, dùng Quill và no-ai-slop Detect. Không dùng OpenRouter hoặc đọc tệp bí mật.

- SG1–SG5 và SG2-01–04 đã được reviewer xác nhận giải quyết; 45 phiếu, bảy mạch, 120 phút, bảy kiểm tra riêng và các ranh giới đều được rà. Không còn lỗi chặn bàn giao hoặc nghiêm trọng của dàn bài.
- GF1: khôi phục chính xác tên bài báo Tsitsiklis, thuộc tính `viewBox` và nhãn các tệp bài tập. Không đổi URL hoặc nguồn học thuật.
- GF2: đồng bộ chỉ dẫn bố cục B02 với chính sách tiếp nối $\pi_L$; không gán hai giá trị 998 và 10 cho chính sách tham lam của bảng I.
- GF3: D05 dùng “có thể khác” khi mô tả hệ quả lấy lại hành động, giữ nguyên thứ tự Sarsa.
- GF4: F02 thay lời chỉ dẫn ký hiệu bằng định nghĩa trực tiếp thời điểm của hai bảng.
- GF5: tách từ dính ở E06/F03/F05/G01, khôi phục cách ghi tổng và ký hiệu; số liệu, công thức và thứ tự không đổi.
- GF6: nhật ký xác định đúng phạm vi giao tác tử dàn bài, không thu hẹp mục tiêu chung của người dùng.

Điều phối viên đã kiểm các chuỗi sửa và thứ tự 45 mã giữa outline/storyboard. Ba diff nhỏ đầu được reviewer đọc lại; ba lỗi khoảng trắng cuối ở E06 được điều phối viên kiểm đúng theo đề xuất. Các sửa này thuộc biên tập cục bộ, không thay luận điểm, mục tiêu hoặc thuật toán. Chế độ Edit giữ nguyên giả thiết, ký hiệu, mức chắc chắn và phân biệt toán học; tự đối chiếu các mục bảo toàn ý, độ chính xác, diễn ngôn biên soạn và câu chữ của eval.md.

**Chấp nhận dàn mới để triển khai HTML/SVG và học liệu.** Báo cáo cuối nằm tại `/tmp/rl06-rebuild/storyboard-gate-final-report.md`; hai báo cáo bao phủ chi tiết tại `storyboard-gate-stage1-report.md` và `storyboard-gate-stage2-report.md` cùng thư mục. Nhật ký này lưu các quyết định để truy nguyên ngay trong kho. Gate chỉ áp dụng cho dàn bài; chưa xác nhận chất lượng hiển thị hoặc hoàn thành bộ trang chiếu. Năm báo cáo độc lập trên bản nháp, chỉnh sửa riêng, kiểm toán học, kiểm trực quan và đồng bộ Codex Slides vẫn phải thực hiện.

## Triển khai HTML và SVG mới — 29-09-2026

Tác tử `/root/lec06_deck_writer` thực hiện vai soạn HTML/SVG sau gate. Cấu hình được điều phối viên giao từ lời gọi tác tử gốc: `model: gpt-6-astra`, `reasoning_effort: xhigh`, `fork_turns: none`. Đây là thông tin cấu hình; không tự xác nhận mô hình thực chạy hoặc tuyến xác thực. Không dùng OpenRouter, API/CLI mô hình, tệp bí mật hoặc tác tử phụ.

Đầu vào là analysis, outline, storyboard mới, manifest được chấp nhận, các báo cáo kiểm số và mẫu kỹ thuật. Không đọc hoặc nối tiếp nội dung HTML, SVG hay học liệu Bài 06 cũ. Tệp HTML được tạo lại từ đầu. Không thay analysis/outline/storyboard; SHA của ba tệp vẫn khớp manifest gate. Không sửa học liệu, index, CSS chung, thư viện, viewer hoặc bài khác.

### Sản phẩm và quyết định cục bộ

- `lecture-06-dieu-khien-phi-mo-hinh.html`: 45 trang đúng thứ tự, bảy section ngoài, 45 ghi chú học thuật có nguồn; bảy chủ đề `lec-06-topic-01` đến `lec-06-topic-07` đúng từng mạch. Liên kết học liệu dùng material-viewer hiện có. Chân trang, tên học phần, học kỳ và cấu hình RevealJS được thay đúng bài.
- Vẽ mới bảy SVG: `chain-five-states.svg`, `greedy-chain.svg`, `control-loop.svg`, `episode-return.svg`, `sarsa-target.svg`, `q-learning-target.svg`, `behavior-target.svg`. Mỗi hình có role, title, desc, viewBox và văn bản thay thế khi nhúng; tín hiệu có thêm nhãn, kiểu nét hoặc viền kép. Công thức, bảng và quy trình vẫn là KaTeX/HTML.
- C07 chuyển câu giải thích chính sách sau cập nhật vào notes và thu gọn khoảng cách dọc của sơ đồ lợi tức; giữ bảng, ba lợi tức và bộ đếm. E01 dùng một câu xác định hai vai chính sách để dành diện tích cho sơ đồ. E07 gộp ba yêu cầu dữ liệu thành một câu, giữ đủ ba yêu cầu và phóng lớn sơ đồ. F03 đặt miền bước học cùng câu định nghĩa bộ đếm để tránh chạm chân trang. Các chỉnh bố cục không đổi luận điểm, thứ tự hoặc thời lượng.
- D05 nêu tường minh trạng thái đầu lấy từ phân phối đầu, hành động đầu lấy theo chính sách mềm; bảng khởi tạo bằng $Q_0$, chỉ các bộ đếm bắt đầu ở 0. Các lịch theo cặp dùng lần cập nhật kế tiếp $n+1$ từ thông tin có trước mẫu.
- B05/C04 được sửa lỗi escape của bộ sinh HTML: dùng chuỗi raw cho $\varepsilon$ và $\tfrac14$, không xóa ký tự để che lỗi. Thêm CSS cục bộ chỉ tại B05/F03 để KaTeX trong tiêu đề giữ nguyên chữ thường, vì chữ hoa của giao diện đã làm biến đổi $\varepsilon$ và $\alpha_n$ khi hiển thị. Không đổi cỡ chữ hoặc CSS chung.
- Chưa xóa bốn SVG cũ không được HTML mới tham chiếu: `five-state-chain.svg`, `greedy-induced-mrp.svg`, `shared-trace.svg`, `target-comparison.svg`. Điều phối viên chỉ xóa sau khi học liệu mới đồng bộ và đã kiểm hết tham chiếu. Chỉ kiểm tên tệp, không lấy nội dung hình cũ để soạn.

### Biên tập no-ai-slop và rà mạch bằng Quill

Đã đọc no-ai-slop SKILL.md và eval.md, dùng chế độ Edit cho toàn bộ 45 tiêu đề, nội dung, chú thích, văn bản thay thế SVG và notes. Ý chính được giữ từ dàn được duyệt; văn phong học thuật, ký hiệu và giả thiết có ưu tiên theo AGENTS.md. Quill được dùng để kiểm tiên quyết, thuật ngữ và đầu vào–đầu ra giữa các mạch; không khởi tạo quill.json hoặc dự án sách.

| Nhóm tự kiểm eval.md | Kết quả và phạm vi |
|---|---|
| Nguyên tắc biên tập 1–11 | Đạt: giữ dữ kiện/giả thiết, không thêm mệnh đề thực nghiệm, không nén mất phân biệt toán học; câu trực tiếp và thuật ngữ thống nhất. Dàn được triển khai thành câu hoàn chỉnh thay cho nhãn nội bộ. |
| Từ cần loại 1 | Đạt: không có lời ca tụng, nhấn mạnh thiếu căn cứ hoặc lời dẫn rỗng. Các mức chắc chắn giữ đúng miền bảo đảm. |
| Mẫu cần loại 1–9 | Đạt: không có câu hỏi tu từ, chỉ dẫn giảng viên, đối lập kịch tính, đổi từ đồng nghĩa tùy tiện hoặc kết luận khẩu hiệu. Định nghĩa, nhãn Câu hỏi: và tổng hợp G01–G04 được giữ vì chức năng học tập đã xác định. |
| Đọc cuối 1–4 | Đạt qua tự đọc và quét văn bản công khai: giữ giọng học thuật, mạch câu và kết nối có nội dung; không dùng điểm phát hiện AI hoặc suy đoán tác giả. |
| Đọc cuối 5 | Bản đầy đủ nằm trong HTML/SVG; các chỉnh so với đặc tả và lý do ghi tại mục này. |
| Đọc cuối 6 | Không áp dụng cho vai soạn Edit; năm vai Detect/kiểm định độc lập chưa được thay thế bởi tự kiểm. |

Quill xác nhận chuỗi A→B đưa thiếu dữ liệu về hành động tới đối tượng $q_\pi/Q$ và thăm dò; B→C chuyển nhu cầu ước lượng thành lợi tức hoàn chỉnh; C→D dùng giới hạn tiền tố để cần giá trị tiếp nối; D→E thay hành động lấy mẫu bằng cực đại; E→F tách phép tính hữu hạn khỏi bảo đảm; F→G quay lại quyết định tại D và lựa chọn có điều kiện. Chính sách $\pi_L$ có lợi tức hữu hạn được tách khỏi chính sách tham lam bảng I. MC giữ $Q,N$ qua lượt và đặt lại quỹ đạo/$f$; Sarsa và Q-learning dùng hai bảng riêng, cùng năm mẫu. Không đưa khái niệm trọng tâm mới vào kết luận.

### Kiểm đã chạy và giới hạn

- Phân tích HTML bằng thư viện chuẩn: 45 mã duy nhất, đúng thứ tự storyboard, bảy section ngoài, 45 notes và đủ bảy chủ đề; mọi đường dẫn nội bộ của HTML tồn tại. Bảy SVG mới phân tích XML được, có mô tả và role. Không có ký tự điều khiển ngoài xuống dòng, ảnh raster hoặc nguồn mạng cốt lõi. Báo cáo tại `/tmp/rl06-rebuild/writer-static.json`.
- Tự tính bằng Fraction: năm cập nhật của Sarsa là $0,-3/5,800,41/5,-32/25$; Q-learning là $0,1/5,800,41/5,-16/25$. Kiểm C08 cho dãy $996,997,998,999,1000$ và hai đáp án 996/997; xác suất thăm dò 1/8 và 7/8; E08 cho mục tiêu 0/799. Kết quả khớp numeric-results.json; báo cáo tại `/tmp/rl06-rebuild/writer-numbers.json`.
- Chromium kiểm 26 trang ở 1280×720 và 390×844, tổng 52 lượt; phát hiện F03 chạm chân trang rồi sửa. Chạy lại ba trang D05/E07/F03 ở hai khung, sáu lượt sạch; sau sửa chữ toán trong tiêu đề và ký hiệu dấu phẩy, chạy lại B05/D02/F03/G01, tám lượt sạch trên HTML ổn định. Báo cáo cuối tại `/tmp/rl06-rebuild/writerchecks/browser-report-targeted.json`; ảnh các lượt tại thư mục `writerchecks/screens/`.
- Bản kiểm cuối thử đủ 521 biểu thức raw của cả HTML và notes bằng KaTeX: không lỗi. Các trang được duyệt không còn dấu toán chưa render, ảnh hỏng, lỗi HTTP, lỗi JavaScript, yêu cầu mạng ngoài localhost, tràn viewport hoặc chạm chân trang; kiểm máy không phát hiện văn bản dưới 0.75 lần cỡ chữ của section. Phím xuống/phải hoạt động; khung hẹp dùng chế độ cuộn mặc định của RevealJS.
- Tác tử đã xem trực tiếp ảnh rộng C07, D03, D05, E01, E04, E07, F03, F04, F05, G01 và B05; các lỗi bố cục/biến đổi chữ toán vừa nêu được sửa và xem lại. Không coi kiểm máy hoặc số ảnh này là rà trực quan đủ 45 trang. Điều phối viên vẫn phải chạy toàn bộ 45 trang trên bản cố định, kiểm năm vai độc lập, đồng bộ học liệu/index và kiểm Codex Slides. Tác tử chưa kiểm học liệu mới hoặc liên kết chủ đề trong nội dung học liệu vì ngoài phạm vi ghi.

SHA-256 HTML lúc bàn giao: `9748857620c2efa2aa331da198989c5a576d7fcde7150b7a6f169e87d7e53dc1`. Bản này là bản nháp hoàn chỉnh để rà độc lập, chưa là chứng nhận hoàn thành toàn bộ yêu cầu của người dùng.


### Điều phối chấp nhận bản dựng để đồng bộ học liệu

Điều phối viên đã đọc báo cáo bàn giao, nhật ký và đối chiếu SHA của HTML cùng bảy SVG với writer-final-manifest.json; tất cả khớp. Trạng thái tác tử soạn được công cụ collaboration xác nhận completed trước khi chuyển quyền ghi. Chấp nhận bản dựng 45 trang làm đầu vào cho học liệu mới và lượt rà bản nháp, chưa chấp nhận hoàn thành toàn bài. Tác tử học liệu chỉ sửa Markdown, mô tả index Bài06 và nhật ký; HTML/SVG được giữ ổn định cho kiểm hiển thị toàn bộ song song.

## 29-09-2026 — Soạn lại học liệu tự học theo bản dựng đã chấp nhận

**Tác tử và phạm vi:** `/root/lec06_note_writer`, vai soạn học liệu và tự kiểm. Cấu hình được điều phối viên giao từ lời gọi là `model: gpt-6-astra`, `reasoning_effort: xhigh`, `fork_turns: none`. Đây là ghi nhận cấu hình chỉ định; không tự xác nhận mô hình thực chạy hoặc tuyến xác thực. Tác tử không tạo tác tử khác, không dùng OpenRouter hay lời gọi mô hình qua API/CLI và không đọc tệp bí mật.

**Đầu vào thực sự dùng:** `analysis.md`, `outline.md`, `storyboard.md` mới; HTML mới có SHA-256 `9748857620c2efa2aa331da198989c5a576d7fcde7150b7a6f169e87d7e53dc1`; danh mục bảy SVG mới; các bàn giao nội dung, kiểm toán lý thuyết và kiểm số được điều phối viên chấp nhận. Đã đọc trực tiếp phần Bài 10 trong `RL-hk2-2025-2026/resources/hw3.pdf` qua văn bản trích xuất để xác nhận dữ kiện sáu trạng thái. Không đọc học liệu Bài 06 cũ, SVG cũ hoặc dàn cũ làm đầu vào. Các nguồn ngoài được dẫn theo hồ sơ nghiên cứu đã chấp nhận, không ghi rằng lượt soạn này đã tải hoặc rà lại toàn bộ các nguồn ấy.

**Tệp đã ghi:** thay toàn bộ `materials/lec-06/lecture-note.md`; thay duy nhất câu mô tả của thẻ Bài 06 trong `index.html`; nối mục nhật ký này. Không sửa HTML, SVG, CSS, trình đọc, Bài 05 hoặc bài khác. Không thêm trang chứng minh, chương trình, notebook, `quill.json`, commit hoặc push.

### Nội dung và sự nhất quán với dàn đã duyệt

Học liệu có đúng bảy chủ đề, mỗi chủ đề có một comment ánh xạ từ `lec-06-topic-01` tới `lec-06-topic-07`. Bảy câu kiểm tra chính có dữ kiện, gợi ý lập luận và lời giải riêng. Bài 10 có thêm một khối bài tập, gợi ý và lời giải. Tổng cộng có 8 khối exercise, 8 hint, 8 solution, 2 example, 3 proof và 1 derivation; các khối không lồng nhau.

- Giữ chuỗi A–E, thưởng trên chuyển tiếp, hai bảng khởi tạo I/II và chính sách tiếp nối riêng $\pi_L$. Tách $q_\pi$ khỏi $Q$ và miền ví dụ $\gamma=1$ khỏi miền định lý $\gamma<1$.
- Từ xác suất $1/8,7/8$ đưa tới phân phối có tập cực đại. Chứng minh cải thiện chính sách mềm gồm trọng số dư, bất đẳng thức một bước, tính đơn điệu và tính co Bellman; xử lý riêng $\varepsilon=1$ và giữ giả thiết $q_\pi$ chính xác.
- MC dùng lần ghé đầu theo cặp, $N_0=0$, chính sách cố định trong lượt; giữ $Q,N$ qua các lượt và đặt lại quỹ đạo cùng chỉ số ghé đầu. Nêu giả thiết kết thúc, lợi tức, ngân sách và chi phí; bổ sung rõ giả thiết tra cứu hằng cho chi phí xử lý $O(T)$.
- Sarsa và Q-learning chạy từ hai bản sao bảng I, có đủ năm mẫu, mục tiêu, sai lệch và hai bảng đầy đủ sau từng mẫu. Hành động kế tiếp của Sarsa được chọn trước cập nhật và giữ khi tiếp tục; ngân sách dừng tại C không tạo nhánh kết thúc.
- Các bảo đảm có miền hữu hạn, dừng, thưởng chặn, $Q_0$ hữu hạn, đúng động lực có điều kiện, cập nhật vô hạn theo cặp và bước học có trước mẫu. Sarsa bổ sung GLIE; hành vi Q-learning không phải trở nên tham lam. Không đưa lại định lý MC tổng quát thiếu căn cứ.
- Bài 10 dùng lại đầy đủ môi trường sáu trạng thái, nhiễu tại B, $\gamma=1/2$, bảng riêng và hai lượt đã cho; giải phần MC lần ghé đầu cùng Q-learning bảng tra. Không nhập phần xấp xỉ hàm. Cặp $(B,0)$ có lợi tức lần đầu 4, mọi lần ghé trung bình 7.
- Hai mục đọc thêm ở chủ đề 07 thực hiện đủ đặc tả: dự đoán TD(0) khác chính sách với tỉ số nhân riêng mục tiêu của $V$ và chứng minh kỳ vọng có điều kiện; chặn Hoeffding cho chính sách, phân phối đầu và số lượt độc lập cố định. Phân biệt hai cách đặt tỉ số, sai lệch Bellman với giá trị thật, số lượt với số cập nhật theo cặp và độ rộng lợi tức khi thưởng có dấu.

### Biên tập no-ai-slop — Edit và tự đối chiếu eval.md

Đã đọc `no-ai-slop/SKILL.md`, `eval.md`, đọc lại toàn bộ bản học liệu mới sau khi viết và biên tập trước bàn giao. Phạm vi gồm tiêu đề, thân bài, chú thích thay thế, câu hỏi, gợi ý, lời giải, chứng minh, phần đọc thêm và câu mô tả thẻ Bài 06. Quy định văn phong học thuật của học phần được ưu tiên so với gợi ý về giọng hội thoại trong kỹ năng.

| Nhóm kiểm trong eval.md | Kết quả tự kiểm và xử lý |
|---|---|
| Editing principles 1–4 | Đạt: bảo toàn dữ kiện và giả thiết đã duyệt; không nén mất phân biệt toán học. Giữ từ vựng học thuật, các bảng số và chức năng của định nghĩa, chứng minh, bài kiểm tra. |
| Editing principles 5–8 | Đạt: mở đầu trực tiếp bằng đối tượng điều khiển; thay lời giới thiệu về bản học liệu bằng nội dung học thuật. Mỗi diễn giải gắn với dữ liệu, cơ chế hoặc phạm vi một kết quả. |
| Editing principles 9–11 | Đạt: dùng câu trực tiếp và chủ thể toán học thích hợp; tách các câu dài ở quy trình và phần chặn sai số, giữ trình tự đã duyệt. |
| Words to cut | Đạt: không có từ quảng bá, lời ca tụng hoặc lời nhấn mạnh rỗng. Từ “quan trọng” chỉ xuất hiện trong thuật ngữ “lấy mẫu quan trọng”. |
| Patterns to cut 1–4 | Đạt: không dùng câu hỏi tu từ, lời dẫn diễn giảng, chỉ dẫn giảng viên, đổi thuật ngữ để tránh lặp hoặc quy kết nguồn mơ hồ. Các phép đối chiếu theo/khác chính sách và $q/Q$ được giữ vì có chức năng khái niệm. |
| Patterns to cut 5–9 | Đạt: không có kết luận kịch tính, khẩu hiệu, biểu tượng trang trí hoặc chuỗi câu rời. Bảng và danh sách phục vụ dữ kiện, quy trình và yêu cầu học tập. Phần tổng hợp được giữ đúng chức năng thu hồi quyết định tại D. |
| Final read 1–5 | Đạt trong phạm vi tự đọc: đã trực tiếp đối chiếu eval, đọc lại cả bảy chủ đề và sửa lỗi phát hiện. Bản đầy đủ nằm trong tệp học liệu; các thay đổi cùng giới hạn tự kiểm được ghi tại đây. |
| Final read 6 | Không áp dụng: lượt này là Edit, không phải Detect; không chấm điểm bộ phát hiện AI hoặc suy đoán tác giả. |

Các chỉnh sửa sau tự đọc gồm bổ sung nghĩa $\pi(a\mid s)$ và miền $d_0$, viết đủ đối số $(s)$ của toán tử Bellman, khai báo hai hàm dùng trong bất đẳng thức co, sửa hai dấu cách TeX bị thiếu dấu gạch chéo trong dữ kiện H03 và chuyển vài nhãn tiếng Việt ra khỏi toán để KaTeX không phát cảnh báo Unicode. Không thay kết quả toán của bản trình chiếu.

### Rà bằng Quill

Đã đọc `quill/SKILL.md` và phần quy trình liên quan để rà vai trò khái niệm, tiên quyết và sự liên tục. Theo chỉ dẫn của kho, không khởi tạo dự án sách hoặc tệp Quill. Kết quả rà:

| Chủ đề | Kết nối vào, đầu ra và liên hệ tiếp |
|---|---|
| 01 | Quyết định tại D xác lập thiếu dữ liệu cho hành động chưa thử; tạo nhu cầu bảng giá trị hành động. |
| 02 | Từ hai ô tại D tới $q_\pi/Q$, thăm dò và cải thiện chính xác; tạo nhu cầu ước lượng các ô từ lượt. |
| 03 | Dùng lợi tức hoàn chỉnh để xây dựng MC nhiều lượt; giới hạn chờ hết lượt tạo nhu cầu mục tiêu một bước. |
| 04 | Từ tiền tố D–C tới giá trị hành động kế tiếp và Sarsa; hành động thăm dò trong mục tiêu tạo cơ sở tách hành vi/đích. |
| 05 | Q-learning giữ dữ liệu và đổi mục tiêu; hai bảng hữu hạn dẫn tới nhu cầu kiểm điều kiện dài hạn. |
| 06 | Tách phép tính hữu hạn khỏi hội tụ; GLIE và bước học theo cặp cung cấp điều kiện chọn phương pháp ở kết luận. |
| 07 | Thu hồi quyết định tại D, kiểm lựa chọn, luyện môi trường riêng H03; DT1/DT2 xác định đúng đối tượng của hai kết quả mở rộng. |

Thuật ngữ dùng nhất quán: lợi tức, phần thưởng, trạng thái kết thúc, bộ đếm, lần ghé đầu, tỉ số, bước học, mục tiêu cập nhật, Sarsa. Phân biệt $t$ theo tương tác, $k$ theo lượt và $n$ theo cập nhật của cặp; đọc thêm Hoeffding khai báo lại $n$ là số lượt và $i$ là chỉ số lượt. Giữ $\pi_L$ riêng với chính sách tham lam bảng I; không trộn dữ kiện A–E và A–F.

### Kiểm tra thực sự đã chạy và giới hạn

- Kiểm cấu trúc Markdown: 7 đề mục chính và 7 comment chủ đề duy nhất đúng thứ tự; 7 đề mục câu kiểm tra chính; các khối đóng/mở cân bằng, không lồng; không có công thức dùng dấu phân cách ngoài `$` và `$$`, mã trang hoặc đường dẫn tạm trong học liệu công khai.
- Dùng KaTeX cục bộ với `renderToString` và `throwOnError: true` kiểm **668 biểu thức**, gồm 48 khối và 620 nội dòng: không lỗi, không cảnh báo và không còn dấu đô la lẻ. Đây là kiểm cú pháp, chưa thay kiểm trình đọc trên trình duyệt.
- Tính lại bằng số hữu tỉ: xác suất thăm dò/đồng hạng; lợi tức 998/999/1000; bài kiểm tra lần ghé đầu 996 so với mọi lần 997; tất cả mục tiêu, sai lệch và kết quả qua năm mẫu Sarsa/Q-learning; toàn bộ hai lượt H03. Kết quả H03 khớp báo cáo kiểm số độc lập được bàn giao. Mục tiêu của câu kiểm tra so sánh là 0 và 799.
- Kiểm đủ bảy ảnh tham chiếu tới SVG mới, có văn bản thay thế; các đường dẫn ảnh và PDF cục bộ tồn tại khi giải từ `2627-1`. Không tham chiếu bốn SVG cũ hoặc ảnh raster.
- So sánh `index.html` với snapshot đầu vào: đúng một dòng mô tả Bài 06 thay đổi, giữ nguyên đường dẫn và các thẻ khác. Đối chiếu SHA với manifest bản dựng xác nhận tác tử không thay HTML hoặc bảy SVG.
- Báo cáo kỹ thuật tạm ở `/tmp/rl06-rebuild/note-writer-static.json`, `note-writer-katex.json`, `note-writer-numeric.json`; mã tính số tại `note-writer-number-check.py`. Các tệp này là bằng chứng tự kiểm, không phải nguồn học thuật công khai.
- Chưa tự kiểm hiển thị trình đọc ở 1280 × 720 hoặc màn hình hẹp, bàn phím của mọi khối mở rộng hoặc Codex Slides. Điều phối viên thực hiện các kiểm này và cố định bản cho năm vai rà độc lập. Tự kiểm của tác tử soạn không thay các lượt rà đó.

## Đồng bộ bản nháp vào Codex Slides và sửa trạng thái giao diện

Điều phối viên đồng bộ ảnh chụp của đủ 45 trang RevealJS, tiêu đề và ghi chú diễn giả vào dự án hiện có `20260824175305-chuy-n-lecture-6-i-u-khi-n-phi-m-h-nh-mo-c905`. Dùng các công cụ ghi xác định, không yêu cầu sinh ảnh hoặc gọi mô hình trong plugin. HTML tại Design Files đã được thay bằng bản mới. Get_project xác nhận 45 trang có trạng thái rendered, tiêu đề và ghi chú khớp từng trang. SHA-256 của 45 ảnh trong dự án khớp tuyệt đối ảnh chụp cục bộ. Bản HTML tương ứng có SHA `9748857620c2efa2aa331da198989c5a576d7fcde7150b7a6f169e87d7e53dc1`.

Áp dụng kỹ năng codex-slides-known-errors khi giao diện còn dừng ở outline dù 45 ảnh đã lưu. Đã đọc mã endpoint PATCH của dự án và xác minh nó chỉ lưu metadata trong trường hợp này. Sửa workflow.stage từ outline sang deck, giữ workspaceMode canvas và đánh dấu bỏ bước chọn cảm hứng; không đổi pages hoặc gọi render. Báo cáo codex-workflow-repair.json xác nhận toàn bộ pages giữ nguyên. Sau đó get_project trả stage deck; Chromium mở đúng URL handoff trang35 ở chế độ play, ảnh hiển thị đúng E07 và giữ vị trí sau reload. Không tạo dự án mới để né trạng thái cũ.

Bằng chứng tại /tmp/rl06-rebuild/: project-sync.json, codex-draft-image-hashes.json, codex-workflow-repair.json, codex-draft-slide35-fixed.png và báo cáo tương ứng. Đây là kiểm bản nháp, phải đồng bộ lại các trang thay đổi sau biên tập. Công cụ Browser trong trình biên tập không được cung cấp trong phiên; việc xem giao diện thực hiện bằng Chromium cục bộ. Không tuyên bố đã kiểm bằng Browser nội bộ.

## 29-09-2026 — Tiếp nhận học liệu và sửa bố cục trước khi cố định bản nháp

Điều phối viên xác nhận tác tử học liệu đã kết thúc, đối chiếu ba SHA trong note-writer-final-manifest.json và kiểm diff index: chỉ một câu mô tả Bài 06 thay đổi. Chấp nhận học liệu làm đầu vào kiểm trình đọc và năm lượt rà độc lập; chưa coi tự kiểm của người soạn là chứng cứ hoàn tất.

Kiểm toàn bộ 45 trang ở hai khung phát hiện câu cuối C02 chạm vùng chân trang. Đã giảm margin của hai dòng trong card riêng C02 xuống .2em, giữ nội dung và cỡ chữ. Cần kiểm lại ảnh sau sửa. Đã rà mọi HTML công khai và Markdown học liệu, bỏ qua các tệp ._ và ~$: không còn tham chiếu bốn SVG cũ, nên xóa five-state-chain.svg, greedy-induced-mrp.svg, shared-trace.svg và target-comparison.svg. Bảy SVG mới là tài sản của bản dựng. Các tệp Bài 05 và tệp dùng chung được đối chiếu 21 SHA bảo vệ; không thay đổi.

## 29-09-2026 — Kiểm kỹ thuật trước năm lượt rà bản nháp

Bản HTML sau sửa C02 được kiểm đủ 45 trang tại 1280 × 720 và 390 × 844, tổng 90 lượt. Không phát hiện tràn viewport, giao chân trang, ảnh hỏng, thiếu alt, công thức thô còn sót, lỗi KaTeX, JavaScript/HTTP hoặc yêu cầu mạng ngoài. Kiểm 521 biểu thức thô gồm notes đạt; điều hướng bàn phím hoạt động. SHA HTML ổn định trong kiểm. Root đã xem ảnh C02 sau sửa và xác nhận câu cuối tách rõ chân trang.

Trình đọc học liệu hiển thị bảy chủ đề, bảy SVG và 668 công thức; không lỗi toán, ảnh hoặc liên kết nội bộ. Mở gợi ý bằng bàn phím hoạt động; đã mở toàn bộ 16 khối ẩn để kiểm dư dấu Markdown. Đã chụp đầu bảy chủ đề và 19 bảng ở hai khung. Các SVG nằm trong vùng cuộn ngang theo CSS dùng chung, không phải ảnh bị mất nội dung. Sau mở tất cả lời giải ở khung hẹp, chiều rộng tài liệu 399 so với viewport 390 cần rà thêm; chưa coi kiểm hình học là xác nhận đầy đủ khả năng đọc.

Bằng chứng: static-report.json, browser-report.json, note-browser-report.json, screens/ và note-screens/ trong thư mục làm việc tạm. Bản này được cố định cho năm vai độc lập; những kiểm trên không thay kiểm học thuật, toán hoặc mạch viết.

## 29-09-2026 — Chấp nhận năm báo cáo độc lập và mở bước biên tập

Cả năm vai rà cùng bản cố định frozen-draft, gồm 15 tệp với manifest SHA-256 1a6fe4127d79df1d9caf97b4728c83b6d8081ecbf4297b572a70c28c3653c4c8. Mỗi vai tự xác nhận đủ15 SHA khớp. Điều phối viên đã đọc báo cáo và chấp nhận bằng chứng/phạm vi; không dùng kết luận của một vai để thay các vai khác. Các tác tử được tạo bằng collaboration.spawn_agent với model gpt-6-astra, reasoning_effort xhigh, fork_turns none; đây là cấu hình đã chỉ định, không xác nhận tuyến xác thực ngoài bằng chứng công cụ.

| Tác tử | Vai và bằng chứng chính | Chặn / nghiêm trọng / trung bình / nhẹ | Báo cáo tạm |
|---|---|---|---|
| lec06_review_student | Đọc45 trang/notes và học liệu; xem90 ảnh slide,52 ảnh học liệu; kiểm bàn phím và vùng cuộn | 0 / 0 / 1 / 1 | review-student.md |
| lec06_review_rl_expert | Đối chiếu30/30 nguồn,45 trang/notes,7 chủ đề; kiểm sườn Sutton–Barto thực trong mạch | 0 / 0 / 1 / 1 | review-rl-expert.md |
| lec06_review_math | Đọc45 trang/7 chủ đề; tự tính bằng Fraction đủ MC/Sarsa/QL/C08/E08/H03 và rà giả thiết/suy diễn | 0 / 0 / 1 / 1 | review-math.md |
| lec06_review_academic | Rà45 trang/notes,7 SVG, toàn học liệu; Detect toàn bộ văn phong và trình tự hình thức hóa | 0 / 0 / 0 / 2 | review-academic.md |
| lec06_review_flow | Quill toàn tuyến45 trang/notes,7 phần và học liệu; kiểm các kết nối thực và mở–kết | 0 / 0 / 0 / 1 | review-flow.md |

Các báo cáo nằm trong /tmp/rl06-rebuild; tác tử biên tập phải lưu các phát hiện và quyết định đủ rõ trong nhật ký bền vững. M01 và RL-01 trùng một lỗi chỉ số ở notes C05. SV-01 yêu cầu làm rõ điều kiện tái khởi đầu; các lỗi nhẹ còn lại thuộc nhãn câu hỏi, thứ tự notes B06, thuật ngữ động lực không đổi, phạm vi gia số DT1, giới hạn tổng quát hóa bảng tra và một câu biên soạn trong desc SVG. Hai gợi ý tùy chọn của vai học thuật không được tính thành lỗi; biên tập viên quyết định có căn cứ. Root R02/R03 về chú giải và trạng thái planning cũng được chuyển biên tập. R01 đã sửa trước bản cố định; R04 chỉ là vùng cuộn của MathML ẩn, giữ khả năng tiếp cận.

Chỉ giao một tác tử biên tập riêng sau khi đủ năm báo cáo hoàn tất; các báo cáo độc lập không tự chỉnh repo. Cần rà lại thuật toán và các đoạn mạch bị ảnh hưởng sau sửa, rồi kiểm hiển thị và đồng bộ Codex Slides. Chưa chấp nhận bàn giao cuối.

## 29-09-2026 — Biên tập sau năm báo cáo độc lập

### Trạng thái và quyền ghi

Tác tử `/root/lec06_final_editor` được giao quyền ghi duy nhất sau khi điều phối viên xác nhận cả năm báo cáo đã hoàn tất và được chấp nhận. Cấu hình được giao: GPT-6-Astra, xhigh, qua tác tử gốc; chỉ ghi nhận chỉ định của điều phối viên, không tự xác nhận mô hình thực chạy hoặc tuyến xác thực. Đã đọc toàn bộ năm báo cáo, root-draft-findings, bàn giao editor, AGENTS.md, no-ai-slop SKILL/eval và Quill SKILL/Revise Workflow. Không tạo tác tử khác, không dùng API/CLI mô hình, OpenRouter, tệp môi trường hoặc bí mật.

Đầu vào đối chiếu đủ 15 mục của manifest bản cố định: 14 tệp trong kho khớp, riêng nhật ký có thêm mục điều phối viên chấp nhận năm báo cáo như bàn giao đã nêu. Bản trước sửa được lưu tại `/tmp/rl06-rebuild/editor-before/`; `editor-input-manifest.json` ghi SHA thực nhận. Các mốc lịch sử phía trên được giữ nguyên theo trạng thái ở từng giai đoạn.

Trạng thái sau lượt này: đã biên tập HTML, hai SVG có phát hiện, học liệu và ba tệp planning hiện hành; thêm quyết định cùng bằng chứng vào nhật ký. Giữ 45 trang, bảy mạch, thứ tự A–G, 120 phút chính và 30 phút chữa bài. Chưa xác nhận hoàn tất mục tiêu: còn tái kiểm toán/thuật toán và mạch viết đúng phạm vi, kiểm hiển thị bản mới và đồng bộ Codex Slides do điều phối viên thực hiện.

### Phiên bản và phạm vi của năm báo cáo đã nhận

M0 là manifest đầu vào chung, SHA-256 `1a6fe4127d79df1d9caf97b4728c83b6d8081ecbf4297b572a70c28c3653c4c8`. Cả năm vai báo cáo đã tự đối chiếu đủ 15/15 tệp. HTML đầu vào có SHA `ed9efc8106080a2f7b659665c0e1b16675a556c39d64d34b2fc1bbece784433b`; học liệu có SHA `b5590952f811a23d9619c6d1f4c84615deb9d180fdfb67b577b0a1f25fb0eb18`. Bảng dưới ghi phạm vi thực báo cáo, không biến việc biên tập viên đọc báo cáo thành kiểm độc lập của chính biên tập viên.

| Tác tử | Vai | Cấu hình chỉ định | SHA đầu vào | Phạm vi và giới hạn chính |
|---|---|---|---|---|
| `lec06_review_student` | Góc nhìn sinh viên | GPT-6-Astra, xhigh, native | M0; HTML và học liệu nêu trên | Đọc 45 trang/notes, toàn học liệu; xem 90 ảnh slide và 52 ảnh học liệu; thử bàn phím/vùng cuộn. Không xác nhận máy chiếu thực, trình đọc màn hình hoặc diễn tập 120 phút. Slide thu nhỏ ở 390 px khó dùng làm bề mặt tự học, học liệu có vùng cuộn riêng. |
| `lec06_review_rl_expert` | Chuyên gia Học tăng cường | GPT-6-Astra, xhigh, native | M0; HTML và học liệu nêu trên | Đối chiếu 30/30 trang nguồn, 45 trang/notes, bảy chủ đề, SVG và sườn Sutton–Barto; tự kiểm các phép tính phân biệt cơ chế. Không thay kiểm toán số toàn bộ hoặc kiểm hiển thị. |
| `lec06_review_math` | Toán và thuật toán | GPT-6-Astra, xhigh, native | M0; HTML và học liệu nêu trên | Đọc 45 trang/notes, bảy chủ đề và bảy SVG; tính Fraction độc lập MC/Sarsa/Q-learning, C08/E08/H03; rà giả thiết, DT1/DT2. Không kiểm trình duyệt; báo rõ giới hạn đọc ảnh bài Hoeffding và không xác nhận mọi biến thể MC. |
| `lec06_review_academic` | Học thuật, giảng dạy, Detect | GPT-6-Astra, xhigh, native | M0; HTML và học liệu nêu trên | Đọc 45 trang/notes, toàn học liệu, bảy SVG và planning; xem riêng bốn ảnh rộng B01/B02/B06/F03. Rà trực giác, tiên quyết và thứ tự hình thức hóa; không thay rà trực quan toàn bài hoặc kiểm định lý từ mọi nguồn gốc. |
| `lec06_review_flow` | Kết nối và mạch viết, Quill | GPT-6-Astra, xhigh, native | M0; HTML và học liệu nêu trên | Đọc toàn tuyến 45 trang/notes, bảy chủ đề, planning và chữ SVG; kiểm bảy mạch, sáu ranh giới cùng mở–kết. Không xem ảnh/trình duyệt hoặc tự kiểm toán toàn bộ số. |

Năm báo cáo có tổng chín phát hiện, trong đó M01/RL-01 trùng nhau: sau hợp nhất là hai lỗi trung bình và sáu lỗi nhẹ, không có lỗi chặn bàn giao/nghiêm trọng. Các giới hạn của từng vai được giữ; không dùng điểm phát hiện AI hoặc suy đoán tác giả.

### Quyết định biên tập theo từng phát hiện

| Mã, mức độ | Bằng chứng ở bản đầu vào | Quyết định và vị trí sau sửa |
|---|---|---|
| M01 / RL-01, trung bình | Notes C05 ghi “lưu chuyển và tăng $t$” trước khi xét $(S_t,A_t)$ trong $f$, có thể trỏ sang hành động chưa chọn hoặc $A_T$ không tồn tại. | Sửa notes C05: lưu chuyển, nếu chưa có cặp thì đặt $f(S_t,A_t)=t$, sau đó mới tăng $t$. Giữ $f$ của lần đầu khi gặp lại cặp, giữ toàn bộ công thức/mẫu số. Đồng bộ HT4, outline và phiếu C05; học liệu §3.4 vốn đúng nên không sửa quy trình đó. |
| SV-01, trung bình | Bước 5 ở D06/E05 chỉ viết “Nếu còn ngân sách, bắt đầu lượt mới”, cùng cấp với nhánh kết thúc. | Ghi đủ “Nếu $S'$ kết thúc và còn ngân sách” trên cả hai mặt trang; đồng bộ notes D06, HT5/HT6 và hai phiếu. Nhánh hết ngân sách vẫn áp dụng cho cả kết thúc lẫn chưa kết thúc; giữ mục tiêu tiếp nối ở mẫu cuối. Học liệu §§4.4/5.4 vốn phân nhánh đúng. |
| SV-02, nhẹ | Nhãn “Câu hỏi:” ở A05/C08 có thể nằm cạnh mục cuối vì danh sách nội dòng theo bố cục Reveal. | Đặt nhãn vào một `div` khối trước `ol` ở đúng hai trang. Câu hỏi, đáp án, cỡ chữ và CSS không đổi. Bổ sung quyết định vào hai phiếu; chờ kiểm ảnh rộng/hẹp sau sửa. |
| RL-02, nhẹ | Nguồn tr. 7 có “khó tổng quát hóa giữa các trạng thái tương tự”; B01 và học liệu §2.1 chưa phát biểu rõ ý này. | Thêm câu trong notes B01 và §2.1: cập nhật một cặp không trực tiếp thay đổi ước lượng các cặp khác, dù trạng thái tương tự. Từ “trực tiếp” giữ phân biệt với truyền giá trị qua các mục tiêu TD về sau. Đồng bộ HT1, mapping nguồn 7 và phiếu B01; không thêm xấp xỉ hàm. |
| AC-01, nhẹ | Notes B06 đặt tách trọng số/Bellman trước phép kiểm số, khác thứ tự trong storyboard. | Đưa nguyên đoạn $q=(3,3,-1)$ và hai kỳ vọng $0.2,2.6$ lên đầu notes. Giữ đủ hai đoạn lập luận, mẫu số $1-\varepsilon$, nhánh $\varepsilon=1$ và giới hạn dùng $q_\pi$ chính xác. Không thêm trang chứng minh hoặc ví dụ mới. |
| AC-02, nhẹ | “MDP hữu hạn, dừng” ở F04/F05 và học liệu §§7.2/7.4 dễ nhầm với kết thúc. | Thống nhất “có động lực không đổi theo thời gian” ở các vị trí đó; đồng bộ cả B06/F01, notes F04/G03, học liệu §§2.5/6.1/6.5 và planning hiện hành. Giữ đầy đủ thưởng chặn, chiết khấu, độ phủ, bước học và kết luận. |
| M02, nhẹ | DT1 đã chứng minh kỳ vọng gia số chưa nhân bước học nhưng kết luận “Hai dạng có cùng kỳ vọng cập nhật”. | Sửa đúng câu §7.4 thành “Hai gia số chưa nhân bước học có cùng kỳ vọng có điều kiện”; đồng bộ đặc tả DT1 và mapping nguồn 19. Không thêm giả thiết về bước học, không đổi tỉ số nhân riêng mục tiêu, hỗ trợ hành động hoặc điều kiện hóa. |
| FL-01, nhẹ | Desc `greedy-chain.svg` có “Vòng B–C được giữ nguyên.”, nói về thao tác biên soạn. | Bỏ riêng câu này. Giữ mô tả B→C, C→B, D→E, thưởng và hệ quả A không đạt từ D dưới chính sách ấy. Hình học, màu, nhãn hiển thị, alt và notes C02 giữ nguyên; đồng bộ phiếu C02. |
| R02, nhẹ | Chú giải nét đứt chỉ nói “tính mục tiêu từ bảng”, trong khi có cả cạnh mục tiêu→Q. | Sửa chú giải và desc `behavior-target.svg` thành tạo mục tiêu và cập nhật bảng. Giữ mọi cạnh, nhãn giá trị, kích thước và cỡ chữ; E01/E07 và học liệu §5.1 dùng chung SVG. Alt/notes đã mô tả đúng hai thao tác nên không viết lại. Đồng bộ đặc tả hình và hai phiếu. |
| R03, nhẹ | Analysis/outline/storyboard còn mô tả “chưa tạo”, “chưa triển khai”, “trước HTML”. | Cập nhật trạng thái đã dựng và đã nhận năm báo cáo; trỏ DT1/DT2 tới học liệu §§7.4–7.5, cập nhật danh mục SVG đã có và việc kiểm còn lại. Giữ nguyên các mốc lịch sử trong nhật ký; không tuyên bố kiểm định cuối đã xong. |
| R01, đã sửa trước bản cố định | Câu cuối C02 từng giao vùng chân trang. | Giữ margin .2em của card riêng C02 và phân biệt $N_0=0$. Không sửa lại; root đã kiểm trước freeze. |
| R04, giới hạn đo đã chẩn đoán | Ở 390 px sau mở lời giải, tài liệu có scrollWidth 399; root xác định 9 px đến từ MathML ẩn trong bảng. | Không sửa nội dung, MathML, viewer hoặc CSS chung. Bằng chứng root không thấy phần tử hiển thị bị mất ngoài vùng cuộn; giữ khả năng tiếp cận. Đây là giới hạn đo còn ghi nhận, không khai đã làm chiều rộng về 390. |
| O1, tùy chọn | Đưa phép cộng 998 lên mặt trang sớm hơn ở B01/B02. | Không áp dụng. B01 đã có bảng và chính sách tiếp nối trong notes, B02 có hai giá trị; học liệu đã dùng ví dụ trước định nghĩa. Reviewer không coi đây là lỗi tiên quyết; giữ diện tích cho bảng và phân biệt $q/Q$. |
| O2, tùy chọn | Đưa lời giải thích vai trò hai tổng lên trước công thức ở học liệu §6.3. | Không áp dụng. F03 đã có hai lịch số trước điều kiện; học liệu giải thích ngay sau công thức và có trường hợp đếm theo cặp. Không có thiếu hụt học tập bắt buộc cần đổi thứ tự ở lượt sửa này. |

### Tự kiểm no-ai-slop ở chế độ Edit

Đã đọc đầy đủ HTML/notes, học liệu và các tệp planning cần chỉnh; đọc lại từng phần sửa cùng ngữ cảnh sau biên tập. Văn phong giữ các thuật ngữ học thuật, câu nêu giả thiết, chỉ số và kết luận có điều kiện. Bản đầy đủ sau sửa nằm trong các tệp sản phẩm; bảng quyết định phía trên là báo cáo thay đổi.

| Nhóm trong eval.md | Kết quả tự đối chiếu |
|---|---|
| Editing principles 1–4 | Đạt: giữ ý nguồn, mọi bảng số và công thức hiện có; chỉ khôi phục giới hạn bảng tra của nguồn 7. Không cắt giả thiết hoặc phần chứng minh đúng để rút chữ. |
| Editing principles 5–8 | Đạt: điều kiện đặt lại và phạm vi kỳ vọng được nêu ngay tại thao tác/kết luận liên quan; từng câu bổ sung có đối tượng và chức năng học tập cụ thể. |
| Editing principles 9–11 | Đạt: động từ lưu, ghi, tăng, cập nhật và bắt đầu lại thể hiện đúng thứ tự. Không làm các đoạn thành một khuôn câu hoặc viết lại các câu vốn rõ. |
| Words to cut | Đạt: không thêm từ quảng bá, nhấn mạnh vô căn cứ hoặc lời dẫn rỗng. “Lấy mẫu quan trọng” giữ đúng thuật ngữ. |
| Patterns to cut 1–4 | Đạt: xóa diễn ngôn biên soạn khỏi desc; giải mơ hồ “dừng”; không thêm câu tu từ, chỉ dẫn giảng viên hoặc đổi thuật ngữ tùy tiện. |
| Patterns to cut 5–9 | Đạt: giữ tổng kết phục vụ năng lực lựa chọn; không có câu kết kịch tính, dấu hai chấm tạo kịch tính hoặc trang trí mới. “Câu hỏi:” và chú giải là nhãn có chức năng. |
| Final read 1–5 | Đạt trong phạm vi tự kiểm: trực tiếp đối chiếu eval, đọc lại bản sửa và diff; giữ giọng học thuật của học phần, ghi rõ thay đổi và giới hạn. |
| Final read 6 | Không áp dụng cho Edit; không chấm điểm AI hoặc suy đoán tác giả. |

### Quill và phạm vi yêu cầu tái kiểm

Quill được dùng để so dàn ý, thuật ngữ và phần kết nối trước/sau; không tạo `quill.json` hoặc tệp dự án sách. Luận điểm mở–kết và sáu ranh giới A→B→C→D→E→F→G giữ nguyên. Thay đổi thứ tự chỉ nằm trong notes B06: phép kiểm số → tách trọng số → Bellman → giới hạn, đúng storyboard đã chấp nhận. C05 tạo đúng chỉ số cho C06; D06/E05 giữ trạng thái để tiếp tục ở nhánh chưa kết thúc; giới hạn bảng tra ở B01 không phủ nhận sự truyền giá trị ở E06.

| Gói tái kiểm | Phần sửa cùng lân cận cần đọc | Đầu vào–đầu ra và tiêu chí |
|---|---|---|
| Bảng tra và nhãn mở phần | A03–A05, B01–B03; học liệu §§1.3/2.1–2.3 | A05 thiếu mẫu trái → B01 hai ô và giới hạn cập nhật trực tiếp → B02 đối tượng giá trị. Ranh giới A→B; không thay luận điểm mở đầu. SV-02 cần ảnh A05. |
| Cải thiện mềm và SVG MC | B04–B07, C01–C04; học liệu §§2.2–2.6/3.1–3.3 | B04/B05 chuẩn bị phân phối; B06 kiểm số trước lập luận đầy đủ; B07 phân biệt $q/Q$; C02 giữ vòng B–C. Ranh giới B→C. Rà toán đủ giả thiết, mẫu số và các đoạn chứng minh, không chỉ công thức cuối. |
| Lần ghé đầu | C03–C08 và D01–D02; học liệu §§3.2–3.6 | C05 ghi f trước tăng t; C06 dùng đúng $G_{f(s,a)}$; C07 áp dụng; C08 kiểm cặp lặp và nhãn. Có hai trang mỗi phía C05, thêm hai trang sau C08 tại ranh giới C→D. |
| Sarsa | D02–D08; học liệu §§4.1–4.6 | Giữ đủ bảng đầu, năm mẫu, hành động lấy trước, nhánh terminal và ngân sách. D→C còn ngân sách tiếp tục ở C; B→A còn ngân sách bắt đầu lượt mới; mẫu 5 hết ngân sách vẫn có mục tiêu −1.6. |
| Q-learning và chú giải hai vai | D07–D08, E01–E08, F01–F03; học liệu §§5.1–5.7 | Bao phủ hai trang mỗi phía E01/E05/E07; E05 chỉ reset sau terminal, E01/E07 dùng nét đứt cho cả hai thao tác. Ranh giới D→E và E→F; giữ hai bảng chạy riêng và cực đại từ bảng trước cập nhật. |
| Thuật ngữ giả thiết | E07–E08, F01–F05, G01–G04; học liệu §§6.1–6.5/7.1–7.2 | F01/F04/F05 và notes G03 chỉ làm rõ động lực không đổi; các giả thiết còn lại và kết luận không đổi. Bao phủ hai trang mỗi phía, các ranh giới E→F/F→G. G03 chỉ đổi thuật ngữ ở lời giải, không sửa đích kết luận. |
| Kỳ vọng TD(0) | Toàn học liệu §7.4, đoạn dẫn G04, mapping nguồn 19 và analysis DT1 | Giữ hỗ trợ hành động, điều kiện hóa trước $A_t$, bảng $V_t$ cố định, mẫu số $b$ và tỉ số nhân riêng mục tiêu. Kết luận chỉ thuộc gia số chưa nhân bước học. Không thêm giả thiết hoặc chứng minh hội tụ. |

Các mã HTML có nội dung hoặc cấu trúc thay đổi: A05, B01, B06, C05, C08, D06, E05, F01, F04, F05, G03. SVG làm thay đổi nội dung liên quan ở C02, E01, E07 dù các thẻ trang ấy không sửa. Học liệu sửa §§2.1, 2.5, 6.1, 6.5, 7.2, 7.4; không sửa dữ kiện/lời giải H03 hoặc DT2. Planning sửa các đặc tả thực liên quan và trạng thái; không thêm/bỏ/đổi thứ tự trang. Các yêu cầu tái kiểm trên chưa được coi là đã hoàn tất bởi lượt tự kiểm này.

### Kiểm kỹ thuật và số học của tác tử biên tập

- Trình phân tích HTML xác nhận 45 mã duy nhất, 45 notes, bảy section ngoài, mọi trang ở tầng hai; thứ tự khớp outline/storyboard. Thẻ đóng/mở cân bằng; bảy chủ đề học liệu đúng thứ tự; không còn công thức có dấu đô la lẻ, khối Markdown chưa đóng hoặc ký tự điều khiển bất thường.
- Các tài nguyên cục bộ được tham chiếu đều tồn tại; đủ bảy SVG có role và mô tả, không ảnh raster hoặc phụ thuộc mạng cốt lõi trong deck. Mọi bài và mẫu vẫn trỏ `lecture-slide.css`. Không sửa CSS, viewer, thư viện, index hoặc bài khác.
- KaTeX cục bộ chấp nhận 525 biểu thức HTML và 668 biểu thức học liệu, không lỗi cú pháp. HTML có sáu cảnh báo Unicode ở năm biểu thức tiếng Việt đã có nguyên trạng trong bản đầu vào 521 biểu thức; đã đối chiếu nội dung cảnh báo theo từng công thức, không có cảnh báo mới. Học liệu không có cảnh báo. Chưa dùng phép kiểm này để kết luận về bố cục.
- Đối chiếu XML xác nhận hai SVG chỉ đổi desc hoặc chữ chú giải; hình học và thuộc tính giữ nguyên. Mọi bảng dữ liệu trong HTML/học liệu và toàn bộ công thức khối học liệu khớp bản trước sửa.
- Tính Fraction xác nhận f của D–C–B–A bằng 0/1/2, không ghi hành động terminal; ở lượt cặp lặp, $f(D,0)=0$ được giữ khi gặp lại tại 2. Lợi tức vẫn là 998/999/1000 và 996/997/998/999/1000. Phép kiểm số B06 vẫn cho $1/5$ và $13/5$.
- Lần lại đủ năm mẫu cho hai thuật toán: hai bước đầu tiếp tục lượt, bước 3/4 reset sau A/E, bước 5 trả bảng. Giá trị cuối tại $(D,0)$ vẫn là $-32/25$ và $-16/25$; mục tiêu cuối là $-8/5$ và $-4/5$. Kiểm đại số DT1 trên dữ kiện nội bộ xác nhận hiệu hai gia số bằng $(\rho_t-1)V_t(s)$ và kỳ vọng có điều kiện bằng 0; không đưa dữ kiện kiểm mới vào bài giảng.
- Đối chiếu 21 SHA bảo vệ của Bài 05 và các tệp chung: khớp. Không tạo code/notebook sản phẩm, không commit/push. Các script kiểm nằm trong thư mục tạm.

Bằng chứng tự kiểm: `/tmp/rl06-rebuild/editor-static-report.json`, `editor-verification.json`, `editor-katex.json`, `editor-changes.diff` và manifest cuối của editor. Biên tập viên chưa chạy kiểm trình duyệt hoặc Codex Slides sau sửa; điều phối viên chịu kiểm ảnh rộng/hẹp, nhãn và khoảng trống, bàn phím, MathML ẩn đã nêu ở R04, rồi đồng bộ và xác minh đúng phiên bản. Các kiểm trước biên tập không được dùng thay kiểm cuối của bản này.

Dấu kiểm SHA-256 của năm báo cáo đã dùng cho lượt biên tập:

| Báo cáo | SHA-256 |
|---|---|
| `review-student.md` | `c494f3f28830dae13e3d0532ae1190c68a7910ab0434165e86c7d16d5c85b6f9` |
| `review-rl-expert.md` | `cdcf79755d0a619e892cc1bb948d0491f0ca96f47ab19cb1127c795098c1d119` |
| `review-math.md` | `e2ef835001500134e8cfd30c0567e5ec2aa334d43df2f3b14b409496f599cad5` |
| `review-academic.md` | `27f9da4f3bb613a71f417fc9f570e2a535e33ba8f4041a4bae28b1db1543144d` |
| `review-flow.md` | `f518dc1f5a4f358ffae291ac5951b72dadf13bb2e123aacb137dfb5cfe4e70a6` |
## 2026-09-29 — Nghiệm thu sau biên tập

### Chấp nhận hai lượt tái kiểm độc lập

Điều phối viên đã đọc hai báo cáo cuối và đối chiếu bản được rà với tệp hiện hành. Hai tác tử tiếp tục đúng vai chỉ đọc qua cơ chế collaboration gốc, cấu hình chỉ định GPT-6-Astra, xhigh; không tạo vai sửa mới. Cả hai tự xác nhận 15/15 SHA của snapshot sau biên tập. HTML được rà có SHA-256 1b69d384440b04294b80365e80c66b4d7d26337f037fed62f4606b71a279cf27; học liệu có SHA-256 8f3b7c821c1218aaaf1b99cdc0d2a3094d8c5315da45926fbbdf54939528c414. Hai tệp công khai và bảy SVG không đổi sau các lượt này.

| Vai | Phạm vi thực tế | Quyết định của điều phối viên |
|---|---|---|
| lec06_review_math | MC C03–C08; toàn quy trình và năm mẫu Sarsa/Q-learning; B01/B06; F/G; toàn DT1; đối chiếu hai SVG. Tự tính bằng phân số, kiểm ngân sách 3/4/5. H03/DT2 khớp byte với bản đã rà nên không tính lại. | Chấp nhận recheck-math.md. Đóng M01/RL-01, SV-01, M02; các sửa khác không tạo lỗi toán mới. Không còn lỗi ở cả bốn mức trong phạm vi tái kiểm. |
| lec06_review_flow | Đọc lại mặt trang và notes của 42 trang trong hợp các vùng sửa cùng hai trang mỗi phía; học liệu liên quan, hai SVG, bảy mạch và sáu ranh giới. A01/A02/D03 không đọc lại, đã xác nhận nguyên văn không đổi. Quill và no-ai-slop Detect. | Chấp nhận recheck-flow.md. Đóng FL-01; B06 có thứ tự ví dụ trước lập luận, các quy trình nối đúng, mở–kết giữ cùng bài toán. Không còn lỗi mạch viết trong phạm vi tái kiểm. |

Hai báo cáo nằm tại /tmp/rl06-rebuild/recheck-math.md và /tmp/rl06-rebuild/recheck-flow.md. Đây là tái kiểm có phạm vi, tiếp nối năm lượt rà đầy đủ đã ghi ở trên; không gọi thành hai lượt rà toàn bài mới. Các đề xuất tùy chọn O1/O2 đã có quyết định không áp dụng và không còn nghĩa vụ sửa. Điều phối viên chấp nhận cả phần xử lý văn phong AC-01/AC-02 vì bản sửa cùng ngữ cảnh đã được vai toán và vai mạch viết đọc lại.

### Kiểm kỹ thuật và trực quan trên sản phẩm cuối

- 45 trang có mã duy nhất, bảy section ngoài, 45 notes; thứ tự trùng outline/storyboard. Đủ bảy trang kiểm tra A05/B07/C08/D08/E08/F05/G03. Tổng thời lượng thiết kế 120 phút; 30 phút chữa bài riêng.
- 90 lượt kiểm trình duyệt trên HTML nêu SHA phía trên: toàn bộ 45 trang ở 1280 px và 390 px. Không sai trang đích, tràn khung, chạm chân trang, công thức lỗi, ký hiệu chưa dựng, tài nguyên hỏng, lỗi JavaScript/HTTP hoặc yêu cầu mạng ngoài. Cấu hình thực chạy đúng 1280×720, tiếng Việt, điều khiển ở cạnh, số trang và hash một gốc; ba plugin cục bộ hoạt động.
- Đã xem trực tiếp bản rộng của A05, B06, C05, C06, C08, D05, D06, E01, E04, E05, E07, F01, F04, F05; bản hẹp của A05, B06, C08, D06, E01, E05, E07, F01, F04, F05. Nhãn câu hỏi đứng trước danh sách, điều kiện terminal hiện đầy đủ, chú giải mới không bị cắt. C02 đã có kiểm riêng sau sửa khoảng cách; bản sau editor chỉ đổi mô tả thay thế của SVG.
- Sáu mục danh sách ở C05/C06/D05/E04/E05 có tỷ số chiều cao trên line-height xấp xỉ 2.21. Xem ảnh xác nhận mỗi mục vẫn chỉ hai dòng; khoảng đứng của KaTeX làm tăng chiều cao hộp. Không dùng chỉ số này để cắt giả thiết hoặc thu nhỏ chữ.
- Năm reviewer đã xem và đọc bản nháp theo phạm vi được ghi riêng: vai sinh viên xem đủ 90 ảnh slide và 52 ảnh học liệu. Các kiểm hiện hành cùng lượt xem vùng sửa bổ sung cho lần rà đó, không thay bằng tuyên bố điều phối viên đã xem lại toàn bộ ảnh lần thứ hai.
- Trình xem học liệu dựng đủ bảy chủ đề, bảy hình, 668 biểu thức và 16 khối gợi ý/lời giải. Kiểm hai khung, mở lời giải bằng bàn phím, chụp bảy chủ đề và 19 bảng ở mỗi khung. Không lỗi công thức, ký hiệu Markdown sót, liên kết nội bộ hỏng hoặc ảnh hỏng. Bàn phím và vùng cuộn bảng/hình đã được vai sinh viên thử trực tiếp.
- KaTeX phân tích 525 biểu thức HTML và 668 biểu thức học liệu không có lỗi. Sáu cảnh báo Unicode ở năm biểu thức HTML có nguyên trạng từ bản trước sửa; không phải lỗi hiển thị hoặc cảnh báo mới.
- Bảy SVG có mô tả, nhãn và quan hệ đúng; không dùng raster trong sản phẩm học thuật. Bốn SVG cũ không còn tham chiếu đã được loại. Không tải font, thư viện hoặc tài sản cốt lõi từ mạng.
- Tất cả 13 bài/mẫu dùng liên kết lecture-slide.css. CSS, viewer và thư viện không đổi. 21 SHA bảo vệ của Bài 05 và các tệp chung vẫn khớp. So với bản index đầu việc, chỉ mô tả Bài 06 đổi; thử liên kết mở đúng deck và học liệu, không có liên kết planning công khai.

Bằng chứng kỹ thuật: browser-report.json, note-browser-report.json, static-report.json, index06-browser-report.json, editor-katex.json và note-width-diagnosis.json tại /tmp/rl06-rebuild/. Các báo cáo chứa phiên bản nguồn và phạm vi, không chỉ một cờ đạt.

### Codex Slides và giới hạn kiểm định

Dự án hiện hành là 20260824175305-chuy-n-lecture-6-i-u-khi-n-phi-m-h-nh-mo-c905. Đã đồng bộ bản PNG hiện tại và ghi chú đã sửa. Đối chiếu đủ 45/45 hình bằng SHA, 45/45 tiêu đề và 45/45 ghi chú trích từ RevealJS; mọi trang có trạng thái rendered và workspace ở giai đoạn deck. Trạng thái dự án vẫn là draft theo ứng dụng; đây không phải lỗi của hình hoặc ghi chú.

Đã mở đúng liên kết Play trả về cho trang 26 và 35, xem trực tiếp bản hiển thị và tải lại; đúng trang, ảnh đã tải và không có lỗi JavaScript. Trang 26 hiện đủ điều kiện kết thúc lượt; trang 35 hiện chú giải hai thao tác của nét đứt. Bằng chứng: codex-final-metadata.json, codex-final-image-hashes.json, codex-final-slide26-report.json, codex-final-slide35-report.json và hai ảnh cùng tên tại thư mục tạm. Các Design Files chuẩn được thay bằng nội dung hiện hành và đọc lại để đối chiếu; học liệu được thêm mới. Nhật ký và các dòng trạng thái planning được đồng bộ lại sau mục nghiệm thu này.

Phiên không có Browser tích hợp của Codex. Kiểm giao diện Codex Slides được thực hiện bằng Chromium cục bộ, không nhận đã kiểm trong Browser tích hợp. Các bản tải lên lịch sử review-log-2.md và note-for-author.md trong dự án không được dùng làm đầu vào; bản chuẩn là các tệp không hậu tố vừa đồng bộ. Không gọi chức năng sinh nội dung hoặc ảnh qua mô hình của plugin.

Ở màn hình 390 px, RevealJS thu nhỏ khung trình chiếu nên chữ nhỏ; học liệu là bề mặt phù hợp hơn để đọc trên điện thoại. Khi mở toàn bộ lời giải, scrollWidth của học liệu là 399 px do MathML ẩn trong bảng. Chẩn đoán không thấy nội dung hiển thị bị mất ngoài vùng cuộn riêng; giữ MathML để bảo toàn khả năng tiếp cận. Không sửa CSS chung chỉ để xóa 9 px của phép đo. Chưa kiểm máy chiếu thực, trình đọc màn hình, mọi trình duyệt hoặc diễn tập 120 phút. Không có ngoại lệ raster.

### Đối chiếu yêu cầu hoàn thành

| Yêu cầu | Bằng chứng và kết quả |
|---|---|
| Làm lại dàn bài | Dàn cũ đã loại khỏi planning; analysis/outline/storyboard mới được viết từ đầu và kiểm định trước HTML. Bản lưu cũ không làm đầu vào. |
| Kiểm kê nguồn | Nguồn 30 trang và tài liệu resources đã có bảng kiểm kê; outline ánh xạ đủ 30/30 trang tới đích hoặc quyết định lược. |
| build-slide-deck-outline | Analysis bao phủ bài toán giảng dạy, nghiên cứu đối chiếu, phụ thuộc, mạch khái niệm, ví dụ/hình, hình thức hóa, bài tập/đọc thêm và quyết định tổng hợp; có hai bộ slide đại học được đọc trực tiếp cùng giới hạn nguồn bổ trợ. |
| Sườn và ký hiệu Sutton–Barto | Tuyến giá trị hành động → thăm dò → MC → Sarsa → Q-learning theo các mục sách đã ghi; bảng thuật ngữ/miền/chỉ số thống nhất và tương thích Bài 05. |
| Gate kế hoạch | Có planner riêng được chấp nhận trước phân tích; gate storyboard độc lập đủ 45 phiếu được chấp nhận trước dựng HTML. |
| Cấu trúc | Bảy mạch, mở–kết, 45 trang lồng đúng cấu trúc; mỗi mạch có kiểm tra riêng. |
| Thời lượng | Bảy phần cộng 120 phút, chữa bài 30 phút; nguồn không có demo tương ứng nên không tạo chương trình/notebook. |
| Chu trình học tập | Storyboard ghi nhu cầu, trực giác, ví dụ, hình thức, ứng dụng và kiểm tra; gate, vai học thuật và mạch viết đã đối chiếu với nội dung thực. |
| Toán và thuật toán | Kiểm độc lập số học, kỳ vọng, terminal, đồng hạng, bộ đếm và điều kiện hội tụ; editor sửa phát hiện; recheck-math đóng đúng phạm vi. |
| Văn phong | Edit và tự kiểm eval ở soạn/biên tập; Detect toàn văn bởi reviewer học thuật; câu sửa được đọc lại. Không còn phát hiện văn nói hoặc chỉ dẫn điều phối cần sửa. |
| Quill và mạch viết | Bảy phần có đầu vào/đầu ra; full review và tái kiểm 42 trang xác nhận các ranh giới cùng mở–kết; không có quill.json. |
| Tài sản | Bảy SVG mới/vẽ lại đúng đặc tả, có mô tả; không raster hoặc tài sản ngoài mạng. |
| Nền kỹ thuật | CSS chung, thư viện cục bộ, lang và cấu hình RevealJS đúng mẫu; không sửa hệ giao diện dùng chung. |
| Học liệu | Viết lại bảy chủ đề, cùng số liệu/ký hiệu; đủ giải thích, đáp án và hai phần đọc thêm; đã rà nội dung và thử viewer. |
| Index | Một mô tả Bài 06 được cập nhật; liên kết đúng; không công khai planning. |
| Các vai độc lập | Đủ năm báo cáo cùng snapshot; editor riêng sau chấp nhận; hai tái kiểm độc lập đã hoàn tất. Không còn phát hiện bắt buộc hoặc lỗi đang mở. |
| Hiển thị slide | 90 lượt kiểm đúng bản cuối, rà trực quan bản nháp và vùng sửa, bàn phím; không lỗi hiển thị nghiêm trọng. |
| Hiển thị học liệu | Hai khung, đủ công thức/ảnh/chủ đề/lời giải; giới hạn MathML ẩn và cuộn cục bộ được ghi đúng. |
| Codex Slides | 45 hình/tiêu đề/notes khớp, giao diện Play và reload đúng; Design Files đọc lại sau đồng bộ. Giới hạn Browser được công bố. |
| Mô hình | Các lời gọi collaboration đã chỉ định GPT-6-Astra, xhigh cho mọi vai; không sử dụng OpenRouter, API/CLI mô hình hoặc bí mật. Không suy diễn tuyến thực thi ngoài bằng chứng công cụ. |
| Phạm vi | Bài 05 và tệp chung giữ SHA đầu việc; không sửa Bài 04, không thêm slide chứng minh đã hủy; không commit/push trong lần dựng này. |
| Kiểm định cuối | Yêu cầu được đối chiếu với tệp, báo cáo, phép tính, ảnh và trạng thái dự án hiện hành. Không dùng mốc chấp nhận dàn bài hoặc tự kiểm của editor làm chứng nhận toàn bộ sản phẩm. |

Điều phối viên chỉ sửa trạng thái nghiệm thu trong planning sau các tái kiểm; không sửa nội dung học thuật, HTML, học liệu hoặc SVG đã được xác nhận. Các đoạn trạng thái mới được đọc lại theo no-ai-slop Edit: câu nêu rõ việc đã làm, phạm vi và giới hạn, không thêm lời ca tụng hoặc bảo đảm ngoài bằng chứng. Việc này không thay luận điểm, thứ tự, ký hiệu hoặc thời lượng đã qua Quill.

Kết quả: bộ sản phẩm Bài 06 đáp ứng phạm vi đã giao và đủ điều kiện bàn giao. Các giới hạn công cụ/thiết bị nêu trên không được trình bày thành kết quả đã kiểm. Nội dung sửa có chủ ý so với nguồn và quyết định không áp dụng đề xuất đều đã ghi trong dàn bài và nhật ký.


## Rà soát từng trang và biên tập lại — 01-10-2026

Yêu cầu của người dùng: duyệt lần lượt từng trang Bài 06, xác định trang muốn nói gì, đề xuất và sửa để tiêu đề ngắn gọn, học thuật; mạch lập luận chặt; khái niệm không xuất hiện đột ngột hay khiên cưỡng; xong mỗi trang thì sửa mục ghi chú bài giảng tương ứng; rồi commit và push. Bảng rà soát do điều phối (phiên chính, Claude Code, Opus 5.5) lập sau khi đọc deck, ghi chú và nguồn 30 trang. Biên tập: Agent fork, Opus 5.5 (kế thừa phiên); là tác tử duy nhất ghi tệp trong lượt này. Quy ước dùng chung với Bài 05: trang kiểm tra có tiêu đề "Kiểm tra …"; tiêu đề không viết tắt "MC"; thuật toán hai trang có tiêu đề "Thuật toán X: …".

Không đổi: 45 trang, bảy mạch, mọi `data-slide-id` và `data-note-topic-id`, phút mỗi trang (tổng 120), SVG, `lecture-slide.css`, `index.html`. CSS cục bộ thêm: bỏ `text-transform` cho KaTeX trong tiêu đề B06, B07, C04; giới hạn hình E07 ở 200px.

### Bảng từng trang (theo thứ tự trình chiếu mới)

| Mã trang | Trang muốn nói gì | Vấn đề | Đề xuất và thay đổi | Quyết định | Thay đổi ghi chú |
|---|---|---|---|---|---|
| L06-A01 | Tên bài và ba phương pháp | Không | Điều khiển phi mô hình (giữ). Không đổi. | giữ | Không |
| L06-A02 | Lộ trình bảy mạch và mục tiêu | Mục tiêu chung chung ("Kiểm tra điều kiện sử dụng và bảo đảm") | Nội dung và mục tiêu (giữ). Ba mục tiêu cụ thể: tính cập nhật MC/Sarsa/Q-learning trên bảng giá trị hành động; phân biệt chính sách sinh dữ liệu với chính sách được học; nêu điều kiện thăm dò và bước học để hội tụ tới giá trị tối ưu. Mục 6 đổi thành "Điều kiện hội tụ". | sửa | topic-01: danh sách năng lực thống nhất với ba mục tiêu |
| L06-A04 | Nhắc dự đoán, đặt bài toán điều khiển | Chưa nêu mục tiêu điều khiển; đứng sau ví dụ | Từ dự đoán đến điều khiển (giữ). Đặt trước A03 để bài toán điều khiển đứng trước ví dụ (nguồn tr. 6 trước tr. 15). Thêm hộp mục tiêu điều khiển theo nguồn tr. 6; gộp hai dòng tiên quyết thành một. | sửa, đổi chỗ | topic-01: mục 1.1 "Từ dự đoán đến điều khiển" lên đầu, thêm câu mục tiêu điều khiển |
| L06-A03 | Giới thiệu môi trường chuỗi năm trạng thái | Ví dụ đứng trước phát biểu bài toán | Quyết định từ kinh nghiệm lấy mẫu → Chuỗi năm trạng thái. Tiêu đề gọi tên ví dụ; trang đứng sau A04. | sửa, đổi chỗ | topic-01: mục 1.2 "Chuỗi năm trạng thái" |
| L06-A05 | Phân biệt thông tin trong một mẫu | Tiêu đề không theo quy ước kiểm tra | Thông tin có trong một mẫu → Kiểm tra thông tin trong một mẫu. Tiêu đề theo quy ước "Kiểm tra …". | sửa | topic-01: mục 1.3 đổi tiêu đề |
| L06-B01 | Bảng $Q$ cho từng cặp, chọn bằng cực đại | Thiếu lý do cần $Q$ thay vì $V$ | Giá trị của từng hành động → Giá trị hành động. Câu mở nêu lý do cần $Q$ thay vì $V$ khi thiếu mô hình (nguồn tr. 7); ghi chú nêu kỳ vọng một bước cần $p(s',r\mid s,a)$. | sửa | topic-02: mục 2.1 thêm lý do (kỳ vọng một bước cần mô hình) |
| L06-B02 | Định nghĩa $q_\pi$, ví dụ $\pi_L$ | $q_*$ chỉ nêu bằng tên | Giá trị đúng và bảng ước lượng → Giá trị hành động của một chính sách. Viết $q_*(s,a)=\max_\pi q_\pi(s,a)$ trên mặt trang; ghi chú nêu cực đại đạt được trong MDP hữu hạn có chiết khấu. | sửa | topic-02: mục 2.2 viết $q_*=\max_\pi q_\pi$ |
| L06-B03 | Vòng đánh giá–cải thiện; hành động chưa thử thiếu dữ liệu | Ý chính nêu trừu tượng | Đánh giá và cải thiện từ dữ liệu → Nhu cầu thăm dò. Hộp nêu ví dụ cụ thể: bảng I tham lam tại D luôn đi phải, $Q(D,0)$ không nhận mẫu dù lợi tức đi trái là 998. | sửa | topic-02: mục 2.3 "Nhu cầu thăm dò" với ví dụ bảng I |
| L06-B04 | Tính tay xác suất ε-tham lam tại D | Tiêu đề không gọi tên nội dung | Phân bổ xác suất thăm dò → Xác suất chọn hành động tại D. Tiêu đề. | sửa | topic-02: tách mục 2.4 "Xác suất chọn hành động tại D" |
| L06-B05 | Công thức ε-tham lam và lớp mềm | Không | Chính sách $\varepsilon$-tham lam (giữ). Không đổi. | giữ | Đánh số lại 2.5 |
| L06-B06 | ε-tham lam theo $q_\pi$ không làm giá trị giảm | Tiêu đề không gọi tên kết quả | Cải thiện với giá trị chính xác → Cải thiện chính sách $\varepsilon$-tham lam. Tiêu đề gọi tên kết quả; dòng cuối nêu ý nghĩa: với $q_\pi$ chính xác, vòng đánh giá–cải thiện giữ thăm dò mà không làm giảm giá trị. | sửa | topic-02: mục 2.6 đổi tiêu đề, thêm câu ý nghĩa |
| L06-B07 | Kiểm tra xác suất và đối tượng $q_\pi$ | Tiêu đề | Xác suất và đối tượng được ước lượng → Kiểm tra chính sách $\varepsilon$-tham lam. Tiêu đề. | sửa | topic-02: mục 2.7 đổi tiêu đề |
| L06-C01 | Vòng lượt → lợi tức → $Q$ → chính sách | Tiêu đề; hình trùng B03 | Giá trị hành động từ lượt hoàn chỉnh → Điều khiển Monte Carlo. Tiêu đề; hình vòng lặp giữ vì hộp trên trang cụ thể hóa vòng ở B03 bằng lợi tức của lượt. | sửa | topic-03: tách mục 3.1 "Điều khiển Monte Carlo" |
| L06-C02 | Một lượt tham lam D→E, $Q(D,1)=10$ | Tiêu đề | Một cập nhật Monte Carlo → Monte Carlo với chính sách tham lam. Tiêu đề. | sửa | topic-03: mục 3.2 riêng |
| L06-C03 | Quy tắc lần ghé đầu và trung bình mẫu | Tiêu đề | Trung bình mẫu theo lần ghé đầu → Cập nhật Monte Carlo theo lần ghé đầu. Tiêu đề. | sửa | topic-03: mục 3.3 đổi tiêu đề |
| L06-C04 | Lấy mẫu ε-tham lam bằng dãy số | Thiếu lý do dùng dãy số | Lấy mẫu một lượt từ dãy số đã cho → Lấy mẫu $\varepsilon$-tham lam bằng dãy số cho trước. Câu mở nêu lý do dùng dãy số: mọi người tái tạo cùng một lượt. | sửa | topic-03: mục 3.4 thêm câu lý do |
| L06-C07 | Cập nhật từ lượt D–C–B–A | Bị thuật toán C05–C06 chen giữa ví dụ | Cập nhật từ lượt D–C–B–A (giữ). Đặt ngay sau C04 để ví dụ lấy mẫu và cập nhật liền mạch trước thuật toán tổng quát. | giữ, đổi chỗ | topic-03: mục 3.5 đứng ngay sau 3.4 |
| L06-C05 | Thuật toán MC: sinh lượt và tính lợi tức | Tiêu đề viết tắt; lịch $\varepsilon_k$ chưa có ví dụ | MC: thu thập và tính lợi tức → Thuật toán điều khiển Monte Carlo: sinh lượt. Tiêu đề; đầu vào nêu ví dụ lịch $\varepsilon_k=1/k$ (nguồn tr. 11), ghi chú nối sang phần hội tụ. | sửa | topic-03: mục 3.6 "Thuật toán điều khiển Monte Carlo", thêm $\varepsilon_k=1/k$ và câu nối phần 6 |
| L06-C06 | Thuật toán MC: cập nhật và cải thiện | Tiêu đề viết tắt | MC: cập nhật và cải thiện chính sách → Thuật toán điều khiển Monte Carlo: cập nhật. Tiêu đề. | sửa | Gộp trong mục 3.6 |
| L06-C08 | Kiểm tra lần ghé đầu và mọi lần ghé | Tiêu đề | Lần ghé đầu của cặp → Kiểm tra lần ghé đầu của cặp. Tiêu đề. | sửa | topic-03: mục 3.7 đổi tiêu đề |
| L06-D01 | MC cần lượt hoàn chỉnh; cập nhật một bước | Tên Sarsa xuất hiện đột ngột | Cập nhật khi lượt chưa kết thúc → Từ Monte Carlo sang cập nhật một bước. Hộp nêu tên Sarsa lấy từ bộ năm $(S,A,R,S',A')$ (nguồn tr. 13); ghi chú nêu dạng cập nhật chung và câu hỏi chọn mục tiêu (nguồn tr. 12). | sửa | topic-04: mục 4.1 thêm dạng cập nhật chung và nguồn gốc tên |
| L06-D02 | Năm mẫu và bảng I dùng chung | Tiêu đề | Dữ liệu chung cho cập nhật một bước → Năm mẫu chuyển dùng chung. Tiêu đề. | sửa | topic-04: tách mục 4.2 |
| L06-D03 | Hai cập nhật Sarsa đầu | Underbrace KaTeX vượt khung | Hai bước tính Sarsa → Hai cập nhật Sarsa đầu tiên. Thay hai underbrace KaTeX (nét vượt khung) bằng một dòng văn bản có cùng số liệu. | sửa | topic-04: mục 4.3 đổi tiêu đề |
| L06-D04 | Công thức Sarsa | Chưa gọi tên học theo chính sách | Mục tiêu Sarsa → Quy tắc cập nhật Sarsa. Câu cuối gọi tên học theo chính sách (on-policy) theo nguồn tr. 13. | sửa | topic-04: mục 4.4 gọi tên on-policy |
| L06-D05 | Thuật toán Sarsa trong lượt | Tiêu đề | Sarsa: khởi tạo và bước không kết thúc → Thuật toán Sarsa: bước trong lượt. Tiêu đề. | sửa | topic-04: mục 4.5 "Thuật toán Sarsa" |
| L06-D06 | Thuật toán Sarsa khi kết thúc/hết ngân sách | Tiêu đề | Sarsa: kết thúc và ngân sách chạy → Thuật toán Sarsa: kết thúc và dừng. Tiêu đề. | sửa | Gộp trong mục 4.5 |
| L06-D07 | Mục tiêu khi vào trạng thái kết thúc | Tiêu đề | Cập nhật khi chuyển vào trạng thái kết thúc → Sarsa tại trạng thái kết thúc. Tiêu đề. | sửa | topic-04: mục 4.6 thêm câu về giá trị tiếp nối bằng 0 |
| L06-D08 | Kiểm tra Sarsa từ tiền tố | Tiêu đề | Cập nhật Sarsa từ tiền tố → Kiểm tra cập nhật Sarsa từ tiền tố. Tiêu đề. | sửa | topic-04: mục 4.7 đổi tiêu đề |
| L06-E01 | Tách hành vi và đích | Thiếu vấn đề dẫn vào; on/off-policy chưa định nghĩa | Chính sách hành vi và chính sách đích (giữ). Câu mở nêu vấn đề: mục tiêu Sarsa dùng hành động thăm dò; định nghĩa học theo chính sách ($b=\pi$) và khác chính sách ($b\ne\pi$) theo nguồn tr. 8; hình cỡ ngắn. | sửa | topic-05: mục 5.1 thêm câu vấn đề và định nghĩa |
| L06-E02 | Mẫu 2 với mục tiêu cực đại | Tiêu đề | Một mục tiêu cực đại → Một cập nhật Q-learning. Tiêu đề. | sửa | topic-05: mục 5.2 đổi tiêu đề |
| L06-E03 | Công thức Q-learning | Tiêu đề | Quy tắc Q-learning → Quy tắc cập nhật Q-learning. Tiêu đề. | sửa | topic-05: mục 5.3 đổi tiêu đề |
| L06-E04 | Thuật toán Q-learning: lấy mẫu | Tiêu đề | Q-learning: lấy mẫu và cập nhật → Thuật toán Q-learning: lấy mẫu và cập nhật. Tiêu đề. | sửa | topic-05: mục 5.4 "Thuật toán Q-learning" |
| L06-E05 | Thuật toán Q-learning: kết thúc, chi phí | Tiêu đề | Q-learning: kết thúc và chi phí → Thuật toán Q-learning: kết thúc và chi phí. Tiêu đề. | sửa | Gộp trong mục 5.4 |
| L06-E06 | Hai bảng trên cùng năm mẫu | Tiêu đề | Hai bảng từ cùng năm mẫu → Sarsa và Q-learning trên cùng năm mẫu. Tiêu đề. | sửa | topic-05: mục 5.5 đổi tiêu đề |
| L06-E07 | Điều kiện dùng dữ liệu hành vi | Thiếu lý do không cần hệ số lấy mẫu quan trọng | Điều kiện sử dụng dữ liệu hành vi → Dữ liệu hành vi trong Q-learning. Mặt trang nêu lý do Q-learning một bước không cần hệ số lấy mẫu quan trọng (nguồn tr. 19); $b$ chỉ quyết định cặp được cập nhật; điều kiện MDP và độ phủ trong hộp; câu về tập dữ liệu hữu hạn chuyển vào ghi chú; hình giới hạn 200px. | sửa | topic-05: mục 5.6 thêm đoạn mở |
| L06-E08 | Kiểm tra hai mục tiêu một bước | Tiêu đề | So sánh hai mục tiêu một bước → Kiểm tra mục tiêu Sarsa và Q-learning. Tiêu đề. | sửa | topic-05: mục 5.7 đổi tiêu đề |
| L06-F01 | Miền giả thiết của định lý | Tiêu đề | Phạm vi của bảo đảm hội tụ → Giả thiết chung của các định lý hội tụ. Tiêu đề. | sửa | topic-06: mục 6.1 đổi tiêu đề |
| L06-F02 | Định nghĩa GLIE | Tên mới, chưa nối lịch $\varepsilon_k$ | Hai yêu cầu của GLIE → Điều kiện GLIE. Nối lại lịch $\varepsilon_k$ của Monte Carlo; ví dụ $\varepsilon_k=1/k\to0$ (nguồn tr. 25). | sửa | topic-06: mục 6.2 nối lịch $\varepsilon_k$ |
| L06-F03 | Điều kiện bước học theo cặp | Tên Robbins–Monro chỉ xuất hiện ở F04 | Bước học theo từng cặp → Điều kiện Robbins–Monro. Gọi tên Robbins–Monro tại trang nêu điều kiện; công thức đặt trước hai ví dụ; ghi chú thêm diễn giải hai tổng (Sutton–Barto §2.5). | sửa | topic-06: mục 6.3 "Điều kiện Robbins–Monro" |
| L06-F04 | Hội tụ của Sarsa và Q-learning | Không | Hội tụ của Sarsa và Q-learning (giữ). Không đổi. | giữ | topic-06: mục 6.4 đổi tiêu đề cho khớp |
| L06-F05 | Kiểm tra giả thiết | Tiêu đề | Kiểm tra giả thiết bảo đảm → Kiểm tra giả thiết hội tụ. Tiêu đề. | sửa | topic-06: mục 6.5 đổi tiêu đề |
| L06-G01 | Bảng so sánh ba phương pháp | Thiếu câu nối Bài 07 | Dữ liệu và mục tiêu của ba phương pháp → Tổng kết ba phương pháp. Hộp nêu một ô cho mỗi cặp; chú thích nối Bài 07 (xấp xỉ hàm) theo nguồn tr. 7, 30. | sửa | topic-07: mục 7.1 "Tổng kết ba phương pháp", thêm giới hạn bảng và câu nối |
| L06-G02 | Trở lại quyết định tại D | Tiêu đề | Quyết định tại D sau các mẫu đã cho → Quyết định tại D sau các cập nhật. Tiêu đề. | sửa | topic-07: tách mục 7.2 |
| L06-G03 | Kiểm tra lựa chọn phương pháp | Tiêu đề | Lựa chọn phương pháp có điều kiện → Kiểm tra lựa chọn phương pháp. Tiêu đề. | sửa | topic-07: mục 7.3 đổi tiêu đề |
| L06-G04 | Bài tập và đọc thêm | Không | Bài tập và tài liệu đọc (giữ). Không đổi. | giữ | Đánh số lại 7.4–7.7 |

Không có đề xuất bị từ chối. Điều chỉnh khi làm: C01 giữ hình vòng điều khiển vì hộp trên trang đã nêu cụ thể vòng bằng lợi tức của lượt; E07 gộp hai câu về mục tiêu và hệ số lấy mẫu quan trọng thành một câu để trang vừa khung; A04 gộp hai dòng tiên quyết thành một vì hộp mục tiêu mới làm trang chạm đáy khung.

### Sai lệch so với storyboard cũ và nguồn

- Đổi thứ tự A04 trước A03: nguồn đặt bài toán điều khiển (tr. 6) trước ví dụ chuỗi năm trạng thái (tr. 15).
- Đổi thứ tự C07 ngay sau C04: ví dụ lấy mẫu (nguồn tr. 17) và cập nhật từ cùng lượt liền mạch trước thuật toán tổng quát; nguồn không có trang thuật toán MC tách riêng ở vị trí này.
- Bổ sung có nguồn: lý do dùng $Q$ (tr. 7); mục tiêu điều khiển (tr. 6); tên Sarsa và học theo chính sách (tr. 13); dạng cập nhật chung, câu hỏi chọn mục tiêu (tr. 12); học theo/khác chính sách (tr. 8); lịch $\varepsilon_k=1/k$ (tr. 11, 25); hệ số lấy mẫu quan trọng (tr. 19); giới hạn bảng $Q$ và câu nối Bài 07 (tr. 7, 30); diễn giải hai tổng Robbins–Monro (Sutton–Barto §2.5).

### Tự kiểm no-ai-slop Edit và liên tục

Phạm vi: mọi câu mới hoặc sửa trên mặt trang, ghi chú diễn giả liên quan và các đoạn mới của ghi chú bài giảng. Đối chiếu `eval.md`: không thêm khẳng định thiếu nguồn; không có tương phản nhị phân, câu đệm, siêu ngôn ngữ, dấu hai chấm kiểu tiết lộ hay chữ đậm trang trí; dấu hai chấm chỉ dùng cho nhãn ("Điều khiển:", "Điều kiện:", "Mẫu 2:") và khai báo. Đã sửa: "mọi người tái tạo" thành "người học tái tạo được" (văn nói); "sai phân thời gian TD(0)" thành "sai phân thời gian (TD)" theo quy tắc viết tắt. Liên tục theo danh sách Outline/Threads/Concept của quill: các khái niệm $q_*$, học theo/khác chính sách, GLIE, Robbins–Monro nay được gọi tên trước lần dùng đầu; thứ tự tiểu mục ghi chú khớp thứ tự trang mới; tham chiếu chéo trong ghi chú (mục 3.6 → phần 6, mục 5.6 → mục đọc thêm 7.5, mục 6.1/6.3) đã kiểm lại. Không tạo `quill.json`.

### Kiểm tra của biên tập

`git diff --check` đạt; 52 thẻ `<section>` mở và đóng; 45 `data-slide-id` duy nhất. Playwright (server cổng 8766, `wait_until="load"`, tắt hiệu ứng chuyển trang) cả 45 trang ở 1600×900 và 390×844: không lỗi console hoặc trang, không `.katex-error`, không tài nguyên hỏng, không cuộn ngang, chữ thân không dưới 0.75em; không trang nào đè chân trang (trước khi sửa, E07 đè 54px; đã sửa). Ảnh đã xem: A04, B03, C04, D03, E01, E07, F03. Trình xem ghi chú: không `.katex-error`, không yêu cầu mạng ngoài; lỗi CSP script nội dòng là lỗi có sẵn của trình xem. Chưa commit, chưa push.


### Rà soát độc lập và vòng sửa — 01-10-2026

Ba người rà soát độc lập, chỉ đọc, trên bản nháp sau lượt biên tập trên: toán học và RL; mạch lập luận và góc nhìn sinh viên; phê bình học thuật kèm no-ai-slop Detect. Theo thông báo của điều phối, cả ba là Agent fork, Opus 5.5; biên tập ghi theo thông báo, không tự kiểm được lệnh gọi. Không có phát hiện chặn bàn giao hoặc nghiêm trọng.

| Mức độ | Trang | Vấn đề | Người rà | Quyết định | Trạng thái |
|---|---|---|---|---|---|
| trung bình | L06-F02, ghi chú 6.2 | "Lịch $\varepsilon_k$ … là một ví dụ" chưa nói ví dụ của yêu cầu nào; dễ hiểu là đủ GLIE | toán, mạch, học thuật | Thay bằng: lịch $\varepsilon_k=1/k$ thỏa tham lam trong giới hạn; thăm vô hạn cần kiểm riêng. Bỏ dòng cuối trùng ý | đã sửa |
| trung bình | L06-E07, ghi chú 5.6 | Giới thiệu lấy mẫu quan trọng chỉ để nói không cần; ghi chú diễn giả có chuỗi rào đón | mạch, toán (nhẹ), học thuật | Mặt trang: mục tiêu cực đại không dùng hành động kế tiếp của $b$; $b$ quyết định cặp và tần suất cập nhật. Trường hợp cần hệ số (nguồn tr. 19) và lý do $A_t$ đã cho đưa vào ghi chú diễn giả và mục 5.6; giữ một câu điều kiện hội tụ | đã sửa |
| nhẹ | L06-B01, ghi chú 2.1 | Lý do cần $Q$ nêu chưa đủ (thiếu phần thưởng và xác suất) | toán | "…dẫn tới những $s'$ và phần thưởng nào, với xác suất bao nhiêu" | đã sửa |
| nhẹ | L06-F03 (ghi chú diễn giả) | Diễn giải tổng bình phương mơ hồ | toán | "giữ tổng phương sai của nhiễu tích lũy hữu hạn, nên ước lượng ổn định dần" | đã sửa |
| nhẹ | L06-D04, L06-E01, ghi chú 3.1, 4.4, 5.1; ghi chú diễn giả C01, D01, D04 | Thuật ngữ học theo chính sách dùng trước định nghĩa; tiếng Anh lặp | mạch, học thuật | D04 không kèm tiếng Anh; E01 giữ dạng đầy đủ và nhắc MC, Sarsa là học theo chính sách; 3.1 và ghi chú C01, D01 viết "dữ liệu sinh từ chính sách đang được cải thiện/đang học"; ghi chú D04 nêu hệ quả $A'$ phải được thực hiện đúng như đã lấy | đã sửa |
| nhẹ | L06-B03, L06-C01 | Vòng đánh giá–cải thiện chưa được định nghĩa trên trang; C01 chưa nói quan hệ với B03 | mạch | B03 thêm dòng định nghĩa vòng; hộp C01 nêu cụ thể hóa vòng bằng lợi tức của lượt | đã sửa |
| nhẹ | L06-D01 | Dạng cập nhật chung chỉ có trong ghi chú | mạch | Đưa công thức lên mặt trang (nguồn tr. 12) | đã sửa |
| nhẹ | L06-D02 | Chưa nói vì sao các hành động cho trước hợp lệ | mạch | Chú thích: mỗi hành động có xác suất dương dưới $\varepsilon$-tham lam, $\varepsilon=1/4$ (đúng vì mọi hành động nhận ít nhất $\varepsilon/2=1/8$; nguồn tr. 17–18) | đã sửa |
| nhẹ | L06-C08, ghi chú 3.7 | Mọi lần ghé chưa nối với Bài 05 | mạch | Thêm "(quy tắc của Bài 05)" | đã sửa |
| nhẹ | Ghi chú 3.1, 4.6 | Tiêu đề trùng tên phần; 4.6 không khớp D07 | mạch | "Vòng điều khiển Monte Carlo"; "Sarsa tại trạng thái kết thúc" | đã sửa |
| trung bình | Ghi chú diễn giả D01, F03, B03 | Câu rào đón lặp | học thuật | Bỏ ba câu; giới hạn nêu một lần ở trang có điều kiện tương ứng | đã sửa |
| nhẹ | Ghi chú diễn giả C05, A02, G01, B02; ghi chú 2.6 | Bình luận quy trình, lặp mặt trang | học thuật | C05 chỉ dẫn nguồn (câu "đặc tả bộ đếm, ngân sách và lần ghé đầu được bổ sung" ghi lại ở đây: bộ đếm, ngân sách, chỉ số ghé đầu là đặc tả bổ sung của bài, không có trong nguồn tr. 10–11); A02 gộp một câu; G01 bỏ đoạn lặp chú thích; B02 "Hai giá trị này là giá trị đúng của $\pi_L$, không phải số khởi tạo trong bảng I"; 2.6 bỏ câu lặp | đã sửa |
| — | L06-C07, L06-D02 (dẫn nguồn) | Cảnh báo dẫn "Bài 7, hw07-function-approximation.pdf" | (cảnh báo) | Từ chối: điều phối đã kiểm, hw07 Bài 7 chứa đúng chuỗi R(A)=1000 và các mẫu (D,0,−1,C), (C,0,−1,B), (B,0,+1000,A); dẫn nguồn đúng | từ chối |

Kiểm tra sau vòng sửa: `git diff --check` đạt; 52 thẻ `<section>` mở và đóng; 45 `data-slide-id` duy nhất. Playwright (cổng 8766, `wait_until="load"`, tắt hiệu ứng chuyển trang) cả 45 trang ở 1600×900 và 390×844: không lỗi console hoặc trang, không `.katex-error`, không tài nguyên hỏng, không cuộn ngang, không trang nào đè chân trang (B01, E07, F02 từng đè 3–38px trong lúc sửa; đã rút gọn chữ và gộp dòng, không giảm cỡ chữ). Ảnh đã xem: D01, E07. Tự kiểm no-ai-slop Edit trên các câu mới: không tương phản nhị phân, rào đón lặp hoặc dấu hai chấm tiết lộ. Chưa commit, chưa push.

### Rà lại sau vòng sửa — 01-10-2026

Người rà toán học và người rà mạch lập luận rà lại các trang đã đổi (theo thông báo của điều phối): kết quả **đạt**, kèm ba phát hiện nhẹ.

| Mức độ | Trang | Vấn đề | Người rà | Quyết định | Trạng thái |
|---|---|---|---|---|---|
| nhẹ | L06-E07 (ghi chú diễn giả) | "vì vậy được thay bằng yêu cầu độ phủ" gợi ý độ phủ là điều kiện tương đương với điều kiện hỗ trợ | toán | "trong Q-learning, vai trò tương ứng là yêu cầu độ phủ"; ghi chú 5.6 không có câu này | đã sửa |
| nhẹ | L06-E07 | Hai câu về vai trò của $b$ lặp ý | mạch | Gộp: "$b$ chỉ ảnh hưởng tới dữ liệu: cặp nào được cập nhật và với tần suất nào" | đã sửa |
| nhẹ | L06-F04, ghi chú 6.4 | Câu phủ định về Monte Carlo trên mặt trang | mạch | Phát biểu phạm vi: bài trình bày định lý cho Sarsa và Q-learning; kết quả GLIE cho điều khiển Monte Carlo (nguồn tr. 26) không được chứng minh trong bài; lý do (lợi tức dưới chính sách thay đổi) ở ghi chú diễn giả và mục 6.4 | đã sửa |

Kiểm tra sau ba sửa cuối: `git diff --check` đạt; Playwright 45 trang ở 1600×900 và 390×844 không lỗi, không `.katex-error`, không tràn; không trang nào đè chân trang. Chưa commit.

### Kiểm định cuối của điều phối — 01-10-2026

Bằng chứng vai trò theo lệnh gọi công cụ của phiên chính: một tác tử biên tập (Agent, `subagent_type: fork`, kế thừa Opus 5.5 của phiên; tiếp tục bằng SendMessage cho ba vòng sửa) và ba tác tử rà soát chỉ đọc chạy song song (Agent, `fork`): toán học và RL; mạch lập luận và góc nhìn sinh viên; phê bình học thuật kèm no-ai-slop Detect. Rà lại sau sửa dùng lại hai tác tử toán học và mạch lập luận qua SendMessage; cả hai kết luận đạt. Mức effort của phiên không xác nhận được từ trong phiên.

Kiểm trình duyệt do điều phối tự chạy (Playwright Chromium, `reloadserver` cổng 8766 vì cổng 8765 đang phục vụ dự án khác; tắt hiệu ứng chuyển trang): cả 45 trang theo thứ tự mới ở 1600×900 và 390×844 không có lỗi console hoặc trang, không `.katex-error`, không tài nguyên hỏng hay yêu cầu mạng ngoài, không cuộn ngang, không vượt khung 720, không đè chân trang, chữ thân ≥ 0.75em. Lỗi tràn nét underbrace ở L06-D03 trước khi sửa không còn. Ảnh đã xem: B03, D03, E07, F04. Trình xem ghi chú: không `.katex-error`, không yêu cầu mạng ngoài; lỗi CSP về script nội dòng có sẵn ở trình xem (tái hiện trên Bài 04). `git diff --check` đạt.

## Bài thực hành: điều khiển Sarsa và Q-learning trên LunarLander không gió (2026-10-03)

### Phạm vi và quyết định

- Yêu cầu của người dùng (mục tiêu phiên): "tiếp tục làm thực hành cho bài 6, điều khiển SARSA và Q-Learning, phi mô hình, dùng Lunar Lander (không có gió)", cùng các yêu cầu chung đã nêu cho thực hành Bài 04–05: notebook standalone tự cài gói, các bước chi tiết có tính sư phạm, đánh giá qua nhiều lượt, ô Markdown giải thích bằng công thức trong bài, chú thích code, trực quan hóa trực tiếp các chính sách sau khi đánh giá (kể cả baseline), gợi mở cuối bài, cột Thực hành trong `2627-1/index.html`. Đây là yêu cầu trực tiếp nên ngoại lệ "không tự tạo notebook" của AGENTS.md được áp dụng.
- Sản phẩm: `2627-1/materials/lec-06/thuc-hanh-lunarlander-dieu-khien-phi-mo-hinh.ipynb` (62 ô, 0,82 MB, lưu kèm output; ô code đầu `%pip install -q "gymnasium[box2d]>=1.0" numpy matplotlib`; chạy khoảng 3,5 phút trên CPU).
- Nguồn: bài giảng gốc `lecture-06-model-free-control.pdf` tr. 8, 11, 12–15, 20–21, 24, 25, 26–28 (đã đối chiếu bằng pdftotext); ký hiệu và quy trình theo `materials/lec-06/lecture-note.md` ($\pi_\varepsilon$ chia đều khi đồng hạng; Sarsa và Q-learning 5 bước; GLIE; Robbins–Monro theo cặp; định lý hội tụ); Singh và cộng sự (2000), Watkins–Dayan (1992) như ghi chú; Sutton–Barto ấn bản 2 §6.4–6.7 cho Expected Sarsa và Double Q-learning ở phần gợi mở (số trang §6.6–6.7, §9.5.4 chưa đối chiếu bản in). Bài giảng gốc không có ví dụ LunarLander.
- Thiết kế: `LunarLander-v3`, `enable_wind=False`; mốc ngẫu nhiên và hàm `heuristic`; lưới 2187 ô (8748 cặp), $Q_0=0$; $\varepsilon_k$ giảm tuyến tính từ 1 xuống 0,05 trong 1500 lượt; $\alpha_n=\max(0{,}05,n^{-0,6})$ theo cặp; $\gamma=0{,}99$; 3000 lượt mỗi thuật toán; đánh giá định kỳ trên `VALID_SEED`, đánh giá cuối trên `TEST_SEED` mới; lượt cắt ngắn bootstrap. Cấu hình chọn qua thử nghiệm sơ bộ đánh giá trên hạt giống riêng (900000, 700000); dữ liệu sơ bộ được nhúng trong notebook như bảng ghi nhận ngoài notebook, kèm nhận xét kết quả Sarsa của notebook (26,2) thấp hơn mọi lần thử cùng lịch. Notebook nêu cấu hình không thỏa GLIE và Robbins–Monro, ô gộp không Markov, nên không khẳng định hội tụ.
- Index: thẻ Bài 6 có link Colab và link tải `.ipynb` trong nhóm **Thực hành**.

### Tác tử

| Vai trò | Loại | Mô hình | Effort | Ghi file |
|---|---|---|---|---|
| Điều phối, kiểm tra cuối, index, nhật ký | phiên chính | claude-opus-5-5 | high | `index.html`, nhật ký này |
| Soạn thảo, sau đó biên tập hai lượt | fork (Agent tool) | claude-opus-5-5 (kế thừa) | high | notebook |
| Rà soát học tăng cường và toán/thuật toán | fork | claude-opus-5-5 | high | không |
| Rà soát góc nhìn sinh viên | fork | claude-opus-5-5 | high | không |
| Rà soát sư phạm, mạch, văn phong (no-ai-slop Detect) | fork | claude-opus-5-5 | high | không |
| Rà soát lại (gộp toán và mạch/văn phong) | fork | claude-opus-5-5 | high | không |

### Phát hiện và quyết định (vòng rà soát 1)

Không có phát hiện chặn bàn giao hay nghiêm trọng.

| mức độ | vị trí | vấn đề | quyết định | trạng thái |
|---|---|---|---|---|
| trung bình | 9.2, ô 29 | $\max_aQ$ được gọi là dự đoán lợi tức của chính sách tham lam; hai bảng có đích khác nhau | Sarsa hướng tới $q$ của chính sách hành vi, Q-learning hướng tới $q_*$ trên ô; in so sánh 100 lượt (Sarsa đánh giá thấp, Q-learning đánh giá cao), diễn giải có điều kiện, nêu thiên lệch chọn lượt minh họa | đã sửa |
| trung bình | 8.2 | Khẳng định dựa trên thử nghiệm ngoài notebook | Bảng dữ liệu sơ bộ ghi rõ nguồn và hạt giống; nêu kết quả notebook thấp hơn; sửa câu về hạt giống | đã sửa |
| trung bình | 4 | "Lưới 2187 ô tốt nhất" không đúng cho Q-learning | Viết theo đúng thử nghiệm | đã sửa |
| trung bình | ô 3, 38 | Tham chiếu "mục 8.3" không tồn tại | Sửa thành 8.2 | đã sửa |
| trung bình | 8.2 | Chưa giải thích khoảng cách tới heuristic; cơ chế cắt ngắn chưa đo | Bốn giả thuyết trỏ tới nhiệm vụ; in số đo lượt cắt ngắn (tàu chủ yếu lơ lửng) | đã sửa |
| trung bình | ô 0, 34 | Chưa báo trước thời gian chạy | Ghi thời gian notebook, mỗi thuật toán, `train_and_test`, nhiệm vụ 1 | đã sửa |
| trung bình | toàn bài | GLIE, MDP chưa viết đầy đủ | Viết đầy đủ lần đầu | đã sửa |
| trung bình (điều phối) | 8.1 | Đường đánh giá định kỳ dao động mạnh chưa giải thích | Ba nguồn dao động, nguyên tắc chọn điểm dừng theo `VALID_SEED`, nhiệm vụ 10 | đã sửa |
| nhẹ | nhiều ô | So sánh bội; đồng hạng; weasel "thước đo thường dùng"; câu về động cơ; metadiscourse ở 9.3; bước trực giác ε-tham lam; dẫn trang; cập nhật có bootstrap khác 0; Box2D trên Colab; Double Q-learning; "ô"/"ô mã"; hình quỹ đạo; thứ tự `terminated`/`truncated` | Sửa theo đề xuất | đã sửa |

### Rà soát lại

Không có phát hiện chặn, nghiêm trọng hay trung bình. Bảy mục nhẹ đã sửa: số cập nhật trace in từ output; "$\alpha_1R=R$" chỉ ở lần cập nhật đầu của mỗi cặp; SE dùng `np.sqrt(len(d))`; điểm cố định Q-learning trên ô gộp phụ thuộc phân phối ghé; bảng có thể tiếp tục dao động; câu về nhiên liệu và lực đẩy; dòng nguồn tr. 12–15.

### Kiểm tra

- `no-ai-slop`: tác tử soạn dùng Edit và tự kiểm `eval.md` sau mỗi lượt (đạt); hai vai rà soát dùng Detect trên toàn bộ ô Markdown, lời giải `<details>` và chú thích code; các mẫu còn lại đã sửa.
- Chạy: nbclient chạy hết 62 ô không lỗi, khoảng 210 giây; hai lần chạy trùng nhau (văn bản trừ số giây, HTML, PNG). Kiểm thử standalone trong venv mới chỉ có ipykernel/nbclient/nbformat ở bản nháp: ô `%pip` cài gymnasium 1.3.0 và Box2D, không cần khởi động lại kernel, 0 lỗi, 225 giây kể cả cài; ô cài gói không đổi sau đó. Chưa chạy trên Colab.
- Trình phát canvas (Playwright Chromium): không lỗi console, không gọi mạng, 50 bước/s.
- Kiểm của điều phối: `nbformat.validate` đạt; không ô lỗi, không ô chưa chạy, không stderr, không URL ngoài trong output, không dấu hỏi trong Markdown; công thức chỉ dùng `$...$`/`$$...$$`; đã xem đường học, trình phát bốn chính sách, bản đồ hành động, $\max_aQ$ so với $G_t$.
- Index: Playwright Chromium 1600×900 và 390×844 trên server cổng 8766 (gốc repo): không lỗi console, không tài nguyên hỏng, không cuộn ngang; `.ipynb` trả HTTP 200.
- Kết quả chính (100 lượt `TEST_SEED`, gymnasium 1.3.0): ngẫu nhiên −194,8; heuristic 236,9; Sarsa tham lam 26,2 ± 14,0 (38% nằm yên, 18% rơi, 44% cắt ngắn); Q-learning tham lam −6,6 ± 17,2 (37% nằm yên, 61% rơi, 2% cắt ngắn); Sarsa − Q-learning 32,8 ± 46,2, chưa xếp hạng được.

### Bổ sung phần 11: tinh chỉnh biểu diễn trạng thái và lịch học (2026-10-03)

- Yêu cầu của người dùng: "Tinh chỉnh để sarsa và q-learning tốt hơn, có thể thêm trạng thái", sau đó làm rõ "vẫn giữ các thiết lập trước đó, bổ sung phần tinh chỉnh phía dưới để so sánh". Các mục 0–10 và kết quả gốc giữ nguyên; output ô 0–56 trùng commit `8af9d8d` (trừ số giây), nguồn chỉ đổi tham chiếu chéo và thời gian chạy. Phần mới là mục 11; Tổng kết thành 12, Gợi mở thành 13.
- Nghiên cứu tinh chỉnh (ngoài notebook, cài đặt rút gọn tương đương `tune_lib.py`): 26 cấu hình × 4 hạt giống huấn luyện × 2 thuật toán, đánh giá chính sách tham lam trên 100 lượt hạt giống 800000+$i$ (tách khỏi `VALID_SEED`/`TEST_SEED`), tối đa 6 tiến trình song song. Toàn bộ kết quả nhúng trong notebook (bảng `TUNE`).
- Cấu hình chọn `todo3_e01`: hai đặc trưng $a_{\text{góc}}$, $a_{\text{cao}}$ lấy từ mã nguồn `heuristic` (hàm của quan sát hiện tại, nhánh chưa chạm đất), mỗi đặc trưng 5 khoảng; $y$ 5 khoảng; $v_y$ 4 khoảng; hai chân tách riêng; 2000 ô; $\varepsilon$ giảm từ 1 xuống 0,01 trong 2000 lượt; các tham số khác như thiết lập gốc. Lý do: trung bình cao nhất khi xét chung hai thuật toán với cùng biểu diễn và lịch. Công khai: biểu diễn mang kiến thức của người thiết kế heuristic; cấu hình là tốt nhất trong 26 trên tập tinh chỉnh nên điểm tinh chỉnh lạc quan.
- Kết quả trên `TEST_SEED` (100 lượt): Sarsa 26,2 → 202,8 ± 2,3 (hiệu ghép cặp +176,6 ± 25,7; 100% nằm yên); Q-learning −6,6 → 235,5 ± 4,3 (+242,1 ± 34,9; rơi 61% → 0%, cắt ngắn 2% → 13%); heuristic − Q-learning tinh chỉnh 1,4 ± 20,3 (khoảng chứa 0). Đánh giá định kỳ của Q-learning tinh chỉnh dao động mạnh (−10069 ở lượt 2250); notebook đo và giải thích cơ chế (khoảng $y\ge1{,}2$ gộp vùng xuất phát với độ cao phía trên, tàu bay lên mà vẫn ở cùng ô tới khi cắt ngắn) và nêu kết quả cuối phụ thuộc thời điểm dừng, đối chiếu với bảng `TUNE`.
- Tác tử: tác tử soạn/biên tập Bài 06 (fork, claude-opus-5-5, high) tiếp tục bằng SendMessage làm thử nghiệm và viết phần 11; một tác tử rà soát lại (fork, claude-opus-5-5, high, chỉ đọc, gộp toán và mạch/văn phong).

| mức độ | vị trí | vấn đề | quyết định | trạng thái |
|---|---|---|---|---|
| trung bình | 11.1, 11.2, 11.4 | Cơ chế điểm −10069 chưa nêu; mô tả khoảng $y\ge1{,}2$ sai; dòng `todo` "phần lớn" thay vì 100/100 | Giữ cấu hình (không chọn lại sau khi xem TEST); in số lượt cắt ngắn và $y$ cuối tại điểm thấp nhất; đoạn cơ chế; nhiệm vụ 16 thêm điểm cắt $y=1{,}5$ | đã sửa |
| trung bình | 11.4 | Mô tả bản đồ hành động sai ở cột phải của Q-learning | Mô tả riêng từng bảng theo số ô | đã sửa |
| trung bình (điều phối) | 11.4 | Kết quả TEST phụ thuộc thời điểm dừng | Đối chiếu bảng `TUNE` (227,5 ± 25,7), nối nguyên tắc chọn điểm dừng theo `VALID_SEED` | đã sửa |
| nhẹ | phần 11, ô 0 | Lời giải về độ phủ; câu về sd; cắt ngắn tăng ở Q-learning; nhánh chạm đất của heuristic; "cùng mã"; chú thích code và công thức trước 11.5; nhịp "Ô mã dưới"; thời gian chạy | Sửa theo đề xuất | đã sửa |

- Kiểm tra: nbclient chạy hết 82 ô không lỗi, khoảng 7,5–8 phút; hai lần chạy trùng nhau; `nbformat.validate` đạt; không ô lỗi, ô chưa chạy, stderr, URL ngoài, dấu hỏi trong Markdown; bốn trình phát không lỗi console, không gọi mạng (Playwright Chromium); điều phối đã xem đường đánh giá định kỳ trước/sau, trình phát bốn ô và bản đồ hành động so với heuristic. `no-ai-slop` Edit (tác tử soạn) và Detect (rà soát lại) trên phần 11. Notebook 1,29 MB. Chưa chạy trên Colab; thời gian trên Colab có thể vượt 9 phút.

## Đợt sửa 2026-10-12 — Giai đoạn I: ghi chú bài giảng

### Tác tử và phạm vi

- Vai: tác tử soạn ghi chú bài giảng Bài 06 (giai đoạn I), viết tệp. Loại `general-purpose`, mô hình Opus 5.5 (`claude-opus-5-5`), mức `high`, theo brief chung `brief_note_writer.md`; điều phối viên đối chiếu với lời gọi công cụ. Không commit, không push.
- Đầu vào đã đọc: `planning/quyet-dinh-chuan-2026-10-12.md` (mục 1–4, 6, 8), `planning/lec-06/revision-plan-2026-10-12.md` (A, B, C, D), `AGENTS.md` (các mục được giao), mẫu `materials/_templates/lecture-note.md`, sản phẩm mẫu `math-4-AI/2627-1/materials/lec-07/lecture-note.md` (chỉ cách trình bày), ghi chú cũ, mã chủ đề trên deck, ô Markdown và output của notebook `thuc-hanh-lunarlander-dieu-khien-phi-mo-hinh.ipynb`, bài giảng gốc `lecture-06-model-free-control.pdf` (30 trang), các tệp `RL-hk2-2025-2026/resources/` (không có tệp tuần 6; Bài 10 của `hw3.pdf` được ghi chú cũ dùng và theo kế hoạch C chuyển sang `exercises.md`).
- Tệp đã ghi: `2627-1/materials/lec-06/lecture-note.md` (viết lại toàn bộ); `2627-1/img/lec-06/chapter-structure.svg` (mới, hình cấu trúc chương, có `<title>`, `<desc>`, nhãn chữ, nét liền/nét đứt kèm chú thích chữ); mục này của `review-log.md`. Không sửa deck, `outline.md`, `storyboard.md`, `index.html`, CSS, viewer, notebook hay SVG cũ.

### Giáo trình và nguồn đã tham khảo theo mục

| Mục của ghi chú | Nguồn đối chiếu cách dẫn dắt và diễn giải |
|---|---|
| Mở chương, Mục 1.1 | Bài giảng gốc tr. 3–7, 15; Sutton và Barto (2018) §3.5–3.6 ($q_\pi$, $q_*$); giáo trình *Học máy thống kê*, mục học hàm Q (dẫn từ giới hạn của quy hoạch động sang học từ mẫu, thuật ngữ) |
| Mục 1.2 | Bài giảng gốc tr. 6–8, 11; Sutton và Barto §5.4 (tr. 100–101, chính sách $\varepsilon$-mềm, $\varepsilon$-tham lam) |
| Mục 1.3 | Bài giảng gốc tr. 24; Sutton và Barto §4.2 (tr. 78–80) và §5.4 (tr. 101–103, chứng minh cải thiện và lớp $\varepsilon$-mềm); tính co của $T^\pi$ theo ghi chú Bài 04 |
| Mục 2 | Bài giảng gốc tr. 9–11, 16–17; Sutton và Barto §5.1 (tr. 92–93, lần ghé đầu), §5.3–5.4 (tr. 97–103) |
| Mục 3 | Bài giảng gốc tr. 12–14, 18; Sutton và Barto §6.4 (tr. 129–130) |
| Mục 4 | Bài giảng gốc tr. 8, 19–21; Sutton và Barto §6.5 (tr. 131–132, Ví dụ 6.6) |
| Mục 5 | Bài giảng gốc tr. 11, 25–28; Sutton và Barto §2.5 (công thức (2.7), tr. 33), §5.3 (tr. 99, câu hỏi mở về hội tụ của Monte Carlo), §6.4–6.5; Watkins và Dayan (1992); Singh và cộng sự (2000, Định lý 1); Bertsekas và Tsitsiklis (1996) chỉ dẫn mục |
| Mục 6 (đọc thêm) | Bài giảng gốc tr. 19, 29; Sutton và Barto §7.3 (công thức (7.9)–(7.10), tr. 148); Hoeffding (1963, Định lý 2) |
| Tình huống, Ứng dụng | Notebook Bài 06 phần 2–13; bài giảng gốc tr. 15–16; Sutton và Barto §6.7 (tr. 134–136) |

Trang Sutton và Barto đã xác minh trên bản PDF (trang in = trang PDF − 22): tr. 33, 78–80, 92–93, 97–103, 129–132, 148. Trang Watkins–Dayan (tr. 282) và Singh và cộng sự (tr. 294–295) giữ theo ghi chú cũ, chưa xác minh lại trong đợt này vì không có bản PDF trong kho. Không dịch hay chép đoạn văn của giáo trình nào.

### Số hiệu cuối cùng

- Bộ đếm chung (27): Định nghĩa 06.1 (bảng $Q$, $q_*$); Nhận xét 06.2 (vòng B–C); Định nghĩa 06.3 ($\varepsilon$-tham lam), 06.4 ($\varepsilon$-mềm); Bổ đề 06.5 ($T^\pi$ đơn điệu, co); Mệnh đề 06.6 (cải thiện $\varepsilon$-tham lam); Nhận xét 06.7; Định nghĩa 06.8 (lần ghé đầu của cặp); Thuật toán 06.9 (Monte Carlo); Nhận xét 06.10; Định nghĩa 06.11 (mục tiêu Sarsa); Thuật toán 06.12 (Sarsa); Nhận xét 06.13 (kết thúc, cắt ngắn, ngân sách); Định nghĩa 06.14 (hành vi, đích); Định nghĩa 06.15 (mục tiêu Q-learning); Thuật toán 06.16 (Q-learning); Nhận xét 06.17; Nhận xét 06.18 (giả thiết nền); Định nghĩa 06.19 (GLIE), 06.20 (Robbins–Monro theo cặp); Định lý 06.21 (Q-learning), 06.22 (Sarsa với GLIE); Nhận xét 06.23 (Monte Carlo); Định nghĩa 06.24; Mệnh đề 06.25, 06.26; Nhận xét 06.27. Trùng bảng B2.
- Ví dụ (15): 06.1 dãy năm ô; 06.2 bảng nghiêng phải; 06.3 chính sách luôn đi trái; 06.4 xác suất tại D; 06.5 một trạng thái ba hành động (mới); 06.6 lượt tham lam D→E; 06.7 lượt thăm dò bằng dãy số; 06.8 cập nhật D–C–B–A; 06.9 năm mẫu, hai cập nhật Sarsa đầu; 06.10 Sarsa trên năm mẫu; 06.11 một cập nhật Q-learning; 06.12 Sarsa và Q-learning trên năm mẫu; 06.13 một chuyển của tàu đổ bộ; 06.14 khối xác suất tham lam và số lần thử khi $\varepsilon$ giảm; 06.15 ba lịch bước học.
- Bài tập (12): 06.1–06.6 trong các mục (trùng các bài tập trang chiếu của kế hoạch C), 06.7–06.12 thuộc "Bài tập củng cố". Tình huống 06.1, 06.2.
- `note-topic-id`: giữ `lec-06-topic-01` … `07`; thêm `lec-06-topic-08` (Mục 6, đọc thêm) và `lec-06-topic-09` (tình huống áp dụng, nhóm bổ sung). Vị trí: 01 trước `## 1.` (phần mở bài toán trung tâm), 02 trước `### 1.1`, 03–06 trước `## 2.`–`## 5.`, 08 trước `## 6.`, 09 trước tình huống, 07 trước "Tóm tắt chương".

### Sai khác so với kế hoạch B và lý do

| Mục | Sai khác | Lý do |
|---|---|---|
| Ví dụ | Thêm Ví dụ 06.5 trước Mệnh đề 06.6; các ví dụ 06.5–06.13 của B2 dịch thành 06.6–06.12 và 06.14–06.15; ví dụ tàu đổ bộ (B2 ghi 06.14 nếu dùng) thành 06.13, đặt sau Thuật toán 06.16 | Chuẩn "ví dụ tính tay trước phát biểu tổng quát" cho Mệnh đề 06.6; ví dụ một bước cho $q_\pi$ chính xác nên kiểm được cả kết luận về $v_{\pi'}$ và làm phản ví dụ cho hai giả thiết. Deck đồng bộ số hiệu ở giai đoạn II |
| Mục 1.3 | Danh sách "Bỏ giả thiết": $q_\pi$ chính xác và $\varepsilon$-mềm dùng môi trường của Ví dụ 06.5 thay cho bảng nghiêng phải | Phản ví dụ tính được chính xác; với dãy năm ô và $\gamma=1$ giá trị chính sách mềm có phân số lớn ($171\,337/200$) |
| Mục 5 | Thí nghiệm mở mục dùng dãy năm ô với $\gamma=0{,}9$ ($q_*(\mathrm D,0)=808{,}1$) làm phản ví dụ "bỏ độ phủ" trong miền định lý; phản ví dụ "bỏ GLIE" dẫn Ví dụ 6.6 của Sutton và Barto | Kế hoạch gợi ý "$Q(\mathrm D,0)$ không được cập nhật" nhưng dãy gốc dùng $\gamma=1$ nằm ngoài định lý |
| Ví dụ 06.14 | Thêm trường hợp $\varepsilon_k=1/k^2$ và bổ đề Borel–Cantelli (phát biểu tại chỗ) | Phản ví dụ cụ thể cho nhầm lẫn "$\varepsilon_k\to0$ là đủ cho GLIE" |
| Ví dụ 06.15(b) | Thêm mục tiêu $\pm1$ để tính phương sai dừng $2/3$ với bước hằng $0{,}8$ | Phản ví dụ định lượng cho "bỏ Robbins–Monro" |
| Tình huống 06.2 | Tính đủ năm cập nhật Sarsa trên vòng B–C với hành vi tham lam; dùng giới hạn ba bước của nguồn (tr. 15) để minh họa cắt ngắn | Kế hoạch chỉ nêu định tính; số liệu tự tính, ghi rõ không phải bảo đảm |
| Bài tập 06.10 | Hai lượt D–C–B–A cùng cập nhật đầu của lượt ba thay vì "một lượt" | Một lượt chưa cho thấy giá trị lan lùi chậm và $Q(\mathrm D,0)$ giảm ở lượt 2 |
| Bài tập 06.12 | Thêm câu (b) khối $0{,}9625$ và câu (c) giả thiết Markov | Phủ mục tiêu 5 bằng bài toán LunarLander; câu (a) ghi nguồn notebook phần 5 |
| Mục 2–4 | Không có tiểu mục "Kiểm tra lựa chọn phương pháp" và Bài 10 hw3 của ghi chú cũ | Kế hoạch B1: chuyển sang `exercises.md` (06.13, 06.17) |
| Q-learning | Giữ bảng nghiêng phải cho Q-learning (nguồn tr. 21 dùng bảng nghiêng trái), ghi lý do ngay trong ghi chú sau Ví dụ 06.12 | Giữ quyết định đã duyệt ở đợt 2026-09-29: mọi khác biệt giữa hai thuật toán đến từ mục tiêu |
| Độ dài | `wc` 27 333 (âm tiết, gồm công thức và bảng); khoảng 23 900 khi bỏ công thức, bảng và `alt`; vượt đích 16 000–19 000 của B4 | Thêm Bổ đề 06.5 có chứng minh, Ví dụ 06.5, hai tình huống có số liệu, sáu bài tập củng cố có lời giải; sản phẩm mẫu math-4-AI Bài 07 dài 34 853 theo cùng cách đếm. Đề nghị rà mạch viết xem có đoạn nào cần cắt |

### Số liệu đã tính lại (script phân số `verify06.py`, `chain06.py` trong scratchpad)

Năm mẫu Sarsa: $0;\,-3/5;\,800;\,41/5;\,-32/25$. Q-learning: $0;\,1/5;\,800;\,41/5;\,-16/25$. Bài tập 06.10: lượt 1 cho $(\mathrm D,0)=1/2$, $(\mathrm C,0)=1/2$, $(\mathrm B,0)=500$; lượt 2 cho $0$, $999/4$, $750$; lượt 3 cho $(\mathrm D,0)=995/8$. Vòng B–C (Tình huống 06.2): $0;\,1/5;\,-11/25;\,-19/25;\,800$. Lợi tức Bài tập 06.3: $996,997,998,999,1000$. Ví dụ 06.5 và Bài tập 06.11: $-0{,}2\to2{,}6$; $0{,}2\to2{,}6$; $w=(1/7,0,6/7)$. Tàu đổ bộ: $0{,}48\to2{,}748$; $3{,}45\to3{,}045$; $-100\to-7{,}3$ (khớp output notebook). $\gamma=0{,}9$: $q_*(\mathrm D,0)=808{,}1$, vòng B–C cho $q_{\pi_I}(\mathrm D,0)=-10$. Khối xác suất $0{,}9625$, $0{,}9925$. Hoeffding: $n\ge\lceil50\ln40\rceil=185$. Phương sai dừng $0{,}64/0{,}96=2/3$. Bài tập 06.9: $20^{5/3}\approx147{,}4$. Khoảng $32{,}8\pm46{,}2=[-13{,}4;\,79{,}0]$.

### Biên tập `no-ai-slop` (Edit) và tự đối chiếu `eval.md`

- Phạm vi: toàn bộ văn xuôi, tiêu đề, khối, lời giải và `alt` của ghi chú mới.
- Đã sửa trong lượt tự kiểm: ẩn dụ "hai bánh răng"; "hành vi không còn quan trọng"; ba câu "không phải… mà…" đổi thành câu khẳng định (còn lại là phân biệt toán học có chức năng, giữ theo `AGENTS.md`); câu hỏi treo cuối Mục 4 và câu dẫn có dấu hai chấm ở Mục 1.3; "Mục này…" ở Mục 6 (tài liệu làm chủ ngữ); hai đoạn kết mục đổi nhịp để tránh lặp khuôn "Như vậy, chúng ta đã…"; tham chiếu "ở trên" thay bằng số hiệu; ký hiệu $E$ (trùng ô E) đổi thành $\mathcal E_k$ và $\mathbf 1\{\cdot\}$.
- Kết quả đối chiếu `eval.md`: đạt các mục về lời dẫn rỗng, từ cấm, tương phản nhị phân không chức năng, kết thúc tóm tắt kịch tính, định dạng (không in đậm trang trí ngoài nhãn bước và nhãn giai đoạn theo chuẩn), gạch ngang dài (chỉ còn trong tiêu đề theo khuôn `# Bài 06 — …` và tên bài giảng gốc). Ghi nhận: các đoạn kết mục dùng cùng một khung ba ý theo yêu cầu của `AGENTS.md`, nên nhịp tương tự nhau là có chủ đích.
- `quill` (chỉ dùng bảng kiểm Outline, Threads, Concept, Revise; không tạo `quill.json`): mọi khái niệm được định nghĩa trước lần dùng (riêng Borel–Cantelli và GLIE được phát biểu tại chỗ); các "sợi" mở ở Mục 1 (vòng B–C, $q_\pi$ chính xác, độ phủ của $(\mathrm D,0)$) được đóng ở Tình huống 06.2, Nhận xét 06.7 và Mục 5; tham chiếu tiến chỉ có ở hình cấu trúc chương và Mục 2 ("Mục 4 định nghĩa thuật ngữ này").

### Kiểm tra đã chạy

- `note_check.py`: 27 khối bộ đếm chung, 15 ví dụ, 12 bài tập, không khoảng trống, không trùng, không khối lạ hay lồng, không khối chưa đánh số, không câu cấm, 0 dấu `\(`/`\[`.
- `check_note.py 06 lecture-06-dieu-khien-phi-mo-hinh.html` (server cổng 8766): 1600×900 và 390×844 đều 0 lỗi KaTeX, 0 lỗi console, 0 yêu cầu ngoài hay hỏng, 85 khối, 28 khối gập. Cờ `overflow` ở 390×844 là `true` (scrollWidth 476): trang không cuộn ngang được (`scrollTo` giữ `scrollX=0`); phần tràn là bảng (tự cuộn, `overflow-x:auto`) và công thức khối cuộn trong khối KaTeX; ghi chú Bài 05 và Bài 07 cho cùng cờ (510, 554). Ở 1600×900, công thức khối Hoeffding tràn 9 px đã được tách hai dòng; chuỗi căn cứ dài trong `aligned` đã đổi thành nhãn (1), (2)… kèm câu "Căn cứ của từng dòng" để không bị cắt. Đã xem ảnh chứng minh Mệnh đề 06.6 ở 1600×900.

### Giới hạn còn lại

- Kết quả của Bài 03–05 được dẫn theo mục ("ghi chú Bài 03, Mục 3–4", "Bài 04, Mục 1–4", "Bài 05, Mục 1–3") theo dàn mục trong kế hoạch sửa của các bài đó, vì bảy ghi chú được viết lại song song; đợt đồng bộ sau thay bằng số hiệu `0N.k` và kiểm lại số mục.
- Notebook Bài 06 còn dẫn số mục của ghi chú cũ (mục 2.1, 2.3, 2.5, 4.4–4.7, 5.1–5.7, 6.1–6.5); cần cập nhật ở giai đoạn III. Ánh xạ: 2.x cũ → Mục 1; 3.x → Mục 2; 4.x → Mục 3; 5.x → Mục 4; 6.x → Mục 5; 7.5–7.6 → Mục 6.
- Deck chưa đồng bộ: số hiệu ví dụ lệch kế hoạch A (xem bảng sai khác), mã chủ đề mới 08–09, tên mạch 4–5 đổi theo tiêu đề mục.
- Chỗ cần tác tử rà toán soi kỹ: chứng minh Bổ đề 06.5 và Mệnh đề 06.6 (Bước 4 dùng $T^{\pi'}v_\pi$); lập luận độc lập của các biến cố $\mathcal E_k$ trong Ví dụ 06.14; phát biểu giả thiết của Định lý 06.21–06.22 so với Watkins–Dayan và Singh và cộng sự (nhất là $\alpha\in(0,1]$ so với $[0,1)$, chặn phương sai phần thưởng); khẳng định "sau một thời điểm ngẫu nhiên, chính sách tham lam theo $Q_t$ là tối ưu"; Tình huống 06.2.

### Vòng sửa sau hai báo cáo rà soát (vai A toán, vai B mạch viết) — 2026-10-12

Tác tử soạn ghi chú Bài 06 tiếp tục (cùng vai, loại, mô hình Opus 5.5, mức `high`), sửa theo quyết định của điều phối viên; chỉ sửa `materials/lec-06/lecture-note.md` và tệp này; không commit. Thuật ngữ chốt cho học phần đã áp dụng: "hầu chắc chắn (almost surely)"; toán tử $T_\pi$, $T_{\pi'}$, $T_*$ viết chỉ số dưới; mức xác suất của Hoeffding là $\beta$.

**Số từ (`wc`).** Trước vòng sửa: 27 333. Sau vòng sửa: 24 966. Phần vượt 20 000 giữ lại vì chương có hai tình huống áp dụng có số liệu, bốn chứng minh hoặc ý tưởng chứng minh có căn cứ từng dòng, mười lăm ví dụ tính tay và mười hai bài tập có lời giải; các phần được giữ nguyên theo quyết định (Tình huống 06.2, Ví dụ 06.5, Ví dụ 06.14, danh sách "Bỏ giả thiết") chiếm khoảng 1 900 từ.

**Số hiệu thay đổi.**

- Bổ đề 06.5 thành Nhận xét 06.5 (Nhắc lại: toán tử Bellman của một chính sách), bỏ chứng minh; Bước 4–5 của chứng minh Mệnh đề 06.6 gộp thành một Bước 4 dùng `aligned`.
- Định nghĩa 06.1 chỉ còn "Bảng giá trị hành động"; $q_*$ chuyển thành câu nhắc lại Bài 04 (Mục 3–4) sau định nghĩa.
- Mục 5: GLIE thành Định nghĩa 06.18, Robbins–Monro theo cặp thành Định nghĩa 06.19, giả thiết nền thành Nhận xét 06.20 và được chuyển xuống ngay trước Định lý 06.21 (P-22). Định lý 06.21, 06.22, Nhận xét 06.23 và mọi số hiệu khác giữ nguyên. Danh sách theo mục trong "Tóm tắt chương" đã cập nhật.
- Ví dụ 06.14 đổi tiêu đề và dữ kiện (cặp $(\mathrm D,0)$ cố định); Ví dụ 06.15 đổi thành "Lịch bước học toàn cục và một cặp được cập nhật thưa" (chỉ còn trường hợp $t_n=2^n$).
- Bài tập 06.2, 06.4, 06.9, 06.12 đổi dữ kiện hoặc câu hỏi (P-18, P-07, P-19).

**Bảng ánh xạ dẫn chéo sang ghi chú Bài 03–05 hiện có trên đĩa (P-02).**

| Nội dung dẫn | Vị trí trên đĩa | Cách dẫn trong ghi chú 06 |
|---|---|---|
| MDP hữu hạn, lợi tức | Bài 03, Mục 1–2 (Định nghĩa 03.7, 03.9; Mệnh đề 03.11) | ghi chú Bài 03, Mục 1–2 |
| $v_\pi$, $q_\pi$ | Bài 03, Mục 3 (Định nghĩa 03.15, 03.16) | ghi chú Bài 03, Mục 3 |
| $v_\pi=\sum_a\pi q_\pi$, $q_\pi=r+\gamma\sum p\,v_\pi$, Bellman kỳ vọng | Bài 03, Mục 4 (Định lý 03.21, Mệnh đề 03.22–03.23) | ghi chú Bài 03, Mục 4 |
| $T_\pi$ đơn điệu, co, điểm bất động | Bài 04, Mục 1 (Bổ đề 04.2, Mệnh đề 04.4, Định lý 04.5, Hệ quả 04.6) | ghi chú Bài 04, Mục 1 |
| Định lý cải thiện chính sách | Bài 04, Mục 2 (Định lý 04.13) | ghi chú Bài 04, Mục 2 |
| $v_*$, $q_*$ | Bài 04, Mục 3 (Định nghĩa 04.19) | ghi chú Bài 04, Mục 3 |
| $T_*$ co, tồn tại chính sách tối ưu dừng | Bài 04, Mục 4 (Mệnh đề 04.24, Định lý 04.25) | ghi chú Bài 04, Mục 4 |
| Lần ghé, Monte Carlo dự đoán, trung bình gia tăng | Bài 05, Mục 2 (Định nghĩa 05.6, 05.8; Mệnh đề 05.9) | ghi chú Bài 05, Mục 2 |
| Khung cập nhật chung | Bài 05, Mục 1 (Định nghĩa 05.10 ở Mục 2) | ghi chú Bài 05, Mục 1 và 3 |
| TD(0) | Bài 05, Mục 3 (Định nghĩa 05.19) | ghi chú Bài 05, Mục 3 |
| Hội tụ TD(0), Robbins–Monro theo trạng thái, $n^{-p}$ | Bài 05, Mục 4 (Định lý 05.30, mục 4.4; ý $n^{-p}$ nằm ở một bài tập củng cố của Bài 05) | ghi chú Bài 05, Mục 4 |

Đợt đồng bộ sau có thể thay "ghi chú Bài 0N, Mục k" bằng các số hiệu trong cột giữa.

**Phát hiện và xử lý.**

| Mã | Mức | Trạng thái | Xử lý |
|---|---|---|---|
| A1 | nghiêm trọng | đã sửa | Ví dụ 06.14: dữ kiện "ở mọi lượt, hàng D có cùng cực đại duy nhất là hành động 1"; $\mathcal E_k$ = chọn hành động 0 tại D ở đầu lượt $k$; xác suất có điều kiện hằng $\varepsilon_k/2$ ⇒ độc lập; hai chiều Borel–Cantelli cho kết luận về cặp $(\mathrm D,0)$; với $1/k^2$ thêm lý do hành động 1 kết thúc lượt nên $(\mathrm D,0)$ chỉ xuất hiện trong lượt có $\mathcal E_k$. Đoạn sau ví dụ nêu dạng có điều kiện của Borel–Cantelli khi cực đại đổi chỗ |
| A2 | trung bình | đã sửa | Phạm vi Định lý 06.21: câu về $0\le\alpha_n<1$ của Watkins–Dayan và hữu hạn lần $\alpha_n=1$ |
| A3 | nhẹ | đã sửa | Trang GLIE tr. 291–292, Định lý 1 tr. 294–295; câu "Định nghĩa 06.18 mạnh hơn, thay giả thiết liên thông" trong Định lý 06.22 |
| A4 | nhẹ | đã sửa | Tình huống 06.2: câu dẫn bảng theo bước 2 của Thuật toán 06.12; câu Q-learning nêu $S'\ne S$ và dẫn đoạn sau Thuật toán 06.16 |
| A5 | nhẹ | đã sửa | "hàng B đổi cực đại sau cập nhật thứ ba và lượt kết thúc ở chuyển thứ năm" |
| A6 | nhẹ | đã sửa | Câu "283 cập nhật" bỏ khỏi "Trong thực hành" Mục 3 (cùng phương án rút gọn của vai B) |
| A7 | nhẹ | đã sửa | Câu: ví dụ vách đá không chiết khấu nên không cô lập GLIE |
| A8 | nhẹ | đã sửa | Bài tập 06.8 câu 4 thêm điều kiện; lời giải dẫn Bài 04 và nêu $q_*$ chưa định nghĩa khi $\gamma=1$ |
| P-01 | trung bình | đã sửa | Bổ đề 06.5 → Nhận xét 06.5 nhắc lại, bỏ chứng minh; sửa câu "có thêm tính đơn điệu"; Bước 4 Mệnh đề 06.6 dẫn lập luận Bài 04 |
| P-02 | trung bình | đã sửa | Số mục theo bảng ánh xạ trên |
| P-03 | trung bình | đã sửa | Định nghĩa 06.1 chỉ còn bảng; $q_*$ nhắc lại dạng Bài 04, dạng $\max_\pi q_\pi$ suy từ định lý tồn tại |
| P-04 | trung bình | đã sửa | $T_\pi$, $T_{\pi'}$, $T_*$ toàn tệp; bảng ký hiệu |
| P-05 | trung bình | đã sửa | "hầu chắc chắn (almost surely)" ở lần đầu, 16 chỗ |
| P-06 | trung bình | đã sửa | Khối `derivation` thay bằng hai câu nhắc lại (Bài 05, Mục 2) |
| P-07 | nhẹ | đã sửa | Ví dụ 06.15 giữ (c), (a)(b) thành câu nhắc lại; phương sai $2/3$ chuyển vào gạch "Bỏ Robbins–Monro"; Bài tập 06.9 bỏ câu chứng minh $n^{-p}$, giữ và mở rộng phần lịch có sàn |
| P-08 | trung bình | đã sửa | Ví dụ 06.10 có bảng ba mẫu còn lại trong "Dữ kiện"; Ví dụ 06.12 nêu bảng và dẫn số hiệu nguồn |
| P-09 | trung bình | đã sửa | Mọi câu "Mục N làm…", "Chương dùng…", "Chương gọi…" viết lại với "chúng ta" hoặc đối tượng làm chủ ngữ |
| P-10 | trung bình | đã sửa | Bỏ câu "Không có mạch nào…" |
| P-11 | trung bình | đã sửa | Mục 6 mở bằng bài toán $b=(1/8,7/8)$, $\pi_L$; kết mục nêu giới hạn hai kết quả và nối Tình huống 06.1 |
| P-12 | trung bình | đã sửa | Câu nối chỉ còn ở một phía tại các ranh giới Mục 1/2, 2/3, 3/4, 4/5 |
| P-13 | trung bình | đã sửa | Tách các đoạn nhiều ý; ba hệ quả Sarsa/Q-learning thành danh sách |
| P-14 | trung bình | đã sửa | Chuỗi quan hệ trong Bước 4 đặt trong `aligned` |
| P-15 | trung bình | đã sửa | Hai công thức cập nhật của Mục 6.1 thành hai dòng hiển thị, mỗi dòng có câu dẫn; không còn ngoặc lồng |
| P-16 | trung bình | đã sửa | "điều kiện của ô $Q(S_t,A_t)$ được cập nhật, tức của $q_*(S_t,A_t)$" |
| P-17 | nhẹ | đã sửa | Mức xác suất $\beta$; tổng $\sum1/k^2\approx1{,}645$ thay cho biểu thức chứa $\pi$; $T$ theo P-04 |
| P-18 | trung bình | đã sửa | Bài tập 06.2 dùng $\varepsilon=0{,}2$ và một trạng thái ba hành động; Bài tập 06.4 dùng $\alpha=0{,}5$ và thêm câu trạng thái kết thúc; bản trùng trang chiếu để cho `exercises.md` |
| P-19 | nhẹ | đã sửa | Bài tập 06.12 câu 2 dùng $\varepsilon_{\min}=0{,}01$ của thiết lập tinh chỉnh |
| P-20 | nhẹ | đã sửa | "Trong thực hành" Mục 5 rút còn hai câu dẫn Tình huống 06.1 |
| P-21 | nhẹ | đã sửa | $f(s,a)$ vào bảng ký hiệu; công thức cần nhớ viết $Y=G_{f(s,a)}$, $\alpha=1/N(s,a)$ sau khi tăng $N$ |
| P-22 | nhẹ | đã sửa | Giả thiết nền thành Nhận xét 06.20 đặt ngay trước Định lý 06.21 |
| P-23 | nhẹ | đã sửa | Tiên quyết phát biểu lại đúng giả thiết Định lý 05.29 ($\gamma=1$ với lượt kết thúc xác suất 1; $\alpha_n\in[0,1]$) |
| P-24 | nhẹ | đã sửa | Trực giác $q_\pi$ mở bằng "Nhắc lại từ Bài 03" |
| P-25 | nhẹ | đã sửa | Câu kết "Trong thực hành" Mục 4 nêu việc đánh giá chạy chính sách đích tham lam |
| P-26 | nhẹ | đã sửa | Bỏ câu bình về kiểu nét của hình |
| P-27 | nhẹ | đã sửa | Ý "Monte Carlo không cập nhật được từ tiền tố" giữ ở Nhận xét 06.10 và đoạn mở Mục 3; các chỗ khác dẫn Nhận xét 06.10 hoặc bỏ; Nhận xét 06.13 mở bằng câu dẫn Nhận xét 06.10 |
| Phép thử đọc 190 | trung bình | đã sửa | Câu "lượt minh họa tối đa ba bước" chuyển vào Tình huống 06.2 |
| Phép thử đọc 715 | trung bình | đã sửa | "Các hành động $A$ và $A'$ trong bảng là dữ kiện cho trước…" |
| Phép thử đọc 1043 | trung bình | đã sửa | Bỏ so sánh đích/hành vi và "bảy phép so sánh" |
| Phép thử đọc 1331 | trung bình | đã sửa | Bỏ "nghiên cứu tinh chỉnh" và $-19\,484{,}6$; nêu lý do chặn Hoeffding không có $B$ |
| Phép thử đọc 1366 | trung bình | đã sửa | Đoạn đánh giá cao viết lại: nói rõ hai đại lượng được so và kết luận |
| Phép thử đọc 1368 | trung bình | đã sửa | Thiết lập tinh chỉnh còn một câu: "cách chia ô dựng từ các đại lượng mà bộ điều khiển heuristic tính từ quan sát" |
| Phép thử đọc 417 | trung bình | đã sửa | "Chứng minh Mệnh đề 06.6 dưới đây dùng…" |

Không bác bỏ phát hiện nào. Rút gọn thêm theo phương án vừa phải của vai B: Mục 6 (giữ một dạng gia số trong Mệnh đề 06.25, bỏ Bước 3 "hai dạng"; Mệnh đề 06.26 thay chứng minh ba bước bằng dẫn Hoeffding kèm một đoạn ý tưởng), Tình huống 06.1 (gộp "Thay đổi biểu diễn" và "Giới hạn"), bản đồ chủ đề, các đoạn "Trong thực hành", tóm tắt chương và nhiều đoạn văn dài.

**Kiểm tra sau vòng sửa.** `note_check.py`: 27 khối bộ đếm chung (06.1–06.27, không khoảng trống, không trùng), 15 ví dụ, 12 bài tập, không khối lạ hay lồng, không khối chưa đánh số, không câu cấm. `check_note.py 06 lecture-06-dieu-khien-phi-mo-hinh.html`: 1600×900 và 390×844 đều 0 lỗi KaTeX, 0 lỗi console, 0 yêu cầu ngoài hay hỏng, `overflow` false ở cả hai kích thước; ở 1600×900 không còn công thức khối nào tràn. Đã xem ảnh chứng minh Mệnh đề 06.6 và Ví dụ 06.14. `no-ai-slop` Edit trên toàn bộ đoạn được sửa, tự đối chiếu `eval.md`: đạt (đã sửa thêm các câu tài liệu làm chủ ngữ phát sinh khi rút gọn).

### Rà lại vòng 2 và sửa — 2026-10-12

Hai tác tử rà lại chỉ đọc (vai A toán và vai B mạch viết, Opus 5.5, mức `high`, `no-ai-slop` Detect cho vai B) báo 0 chặn bàn giao, 0 nghiêm trọng; vai A 6 nhẹ, vai B 2 trung bình và 11 nhẹ. Tác tử soạn (cùng vai, Opus 5.5, `high`) sửa toàn bộ theo quyết định của điều phối viên; không commit. Thuật ngữ chốt mới: "lần ghé đầu tiên (first-visit)", "mọi lần ghé (every-visit)" theo Định nghĩa 05.6. Bảng ánh xạ ở vòng trước đã sửa dòng hội tụ TD(0) thành Định lý 05.30, mục 4.4 (A-5).

| Mã | Mức | Trạng thái | Xử lý |
|---|---|---|---|
| A-1 | nhẹ | đã sửa | Gạch "Trường hợp trùng nhau": với hành vi tham lam, $A'\in\mathcal G_{Q_t}(S')$ nên hai mục tiêu bằng nhau trên cùng dữ liệu; điều kiện $S'\ne S$ và cùng quy tắc phá hòa chỉ cần để hai thuật toán chọn cùng hành động tiếp theo |
| A-2 | nhẹ | đã sửa | Ví dụ 06.14: bỏ "như trong thí nghiệm ở đầu mục"; thêm câu giả định tách riêng vai trò của lịch $\varepsilon_k$, trường hợp cực đại đổi chỗ xét sau ví dụ |
| A-3 | nhẹ | đã sửa | Đoạn sau Thuật toán 06.9: "bước cải thiện $\varepsilon$-tham lam có dạng của Mệnh đề 06.6, áp dụng cho bảng ước lượng (Nhận xét 06.7)" |
| A-4 | nhẹ | đã sửa | Bài tập 06.2: câu dẫn nói rõ câu 1, 3, 4 thuộc dãy năm ô, câu 2 xét một trạng thái ngoài dãy (cùng R-13) |
| A-5 | nhẹ | đã sửa | Tiên quyết hội tụ TD(0) thêm "dữ liệu sinh theo $\pi$"; ý $n^{-p}$ ghi là từ một bài tập củng cố của ghi chú Bài 05; bảng ánh xạ sửa thành Định lý 05.30, mục 4.4 |
| A-6 | nhẹ | đã sửa | Phạm vi Định lý 06.21: "với lịch tất định theo số lần cập nhật" |
| R-01 | trung bình | đã sửa | Ví dụ 06.12: bảng năm mẫu $(S,A,R,S')$ trong "Dữ kiện" |
| R-02 | trung bình | đã sửa | 22 chỗ "lần ghé đầu" đổi thành "lần ghé đầu tiên" (gồm tiên quyết, bảng ký hiệu, Định nghĩa 06.8, Thuật toán 06.9, Bài tập 06.3, tóm tắt, tài liệu tham khảo) |
| R-03 | nhẹ | đã sửa | "trong Mục 4, chúng ta xét điều khiển khác chính sách; trong Mục 6, chúng ta xét dự đoán khác chính sách" |
| R-04 | nhẹ | đã sửa | Đoạn sau Ví dụ 06.14: trường hợp cực đại đổi chỗ "cần một lập luận riêng … nằm ngoài phạm vi chương" |
| R-05 | nhẹ | đã sửa | Nhận xét 06.20: "Việc dãy có hai trạng thái kết thúc A và E không bảo đảm…" |
| R-06 | nhẹ | đã sửa | Tình huống 06.1: "Khoảng $\pm1{,}96$ sai số chuẩn của cả hai hiệu đều không chứa $0$" |
| R-07 | nhẹ | đã sửa | Mở Mục 5 bằng "Xét dãy năm ô với $\gamma=0{,}9$"; kết Mục 6: "Hai kết quả có phạm vi hẹp. Mệnh đề thứ nhất…" |
| R-08 | nhẹ | đã sửa | Bài tập 06.2 câu 2: hàng $(4;1;1)$, $\varepsilon=0{,}6$, lời giải $(0{,}6;\,0{,}2;\,0{,}2)$ |
| R-09 | nhẹ | đã sửa | Ranh giới 3/4: bỏ câu nhiệm vụ ở cuối Mục 3; ranh giới 4/5: bỏ câu nhiệm vụ ở cuối Mục 4, đoạn mở Mục 5 viết lại thành câu nêu loại giả thiết |
| R-10 | nhẹ | đã sửa | Ngoặc lồng: "công thức 2.7", "công thức 7.9–7.10" ở thân bài và tài liệu tham khảo |
| R-11 | nhẹ | đã sửa | Bước 4 Mệnh đề 06.6: bốn dòng `aligned`, mỗi dòng một quan hệ, nhãn (1)–(4) kèm căn cứ |
| R-12 | nhẹ | đã sửa | Đoạn mở Mục 6 tách hai đoạn; bỏ câu nhắc $n^{-p}$ ở Mục 5.3; "(Mục 5.4)" thành "(danh sách \"Bỏ giả thiết\" sau Định lý 06.22)" |
| R-13 | nhẹ | đã sửa | Tiên quyết định lý cải thiện thêm "MDP hữu hạn, phần thưởng bị chặn, $0\le\gamma<1$, $\pi$ dừng"; đề Bài tập 06.2 câu 4 chép bảng nghiêng phải |

Không bác bỏ phát hiện nào. Số từ (`wc`): 24 966 trước vòng 2, 24 997 sau vòng 2. Để giữ dưới 25 000, rút gọn thêm: diễn giải Ví dụ 06.12, Nhận xét 06.23, đoạn sau Ví dụ 06.12, danh sách "Ứng dụng", vài câu của Tình huống 06.1, mục Sutton và Barto trong tài liệu tham khảo; bỏ dòng "Đọc tiếp".

Kiểm tra: `note_check.py` 27/15/12 khối liên tục, không khối lạ, lồng, chưa đánh số hay câu cấm; `check_note.py 06 lecture-06-dieu-khien-phi-mo-hinh.html` 0 lỗi KaTeX, 0 lỗi console, 0 yêu cầu ngoài, `overflow` false ở 1600×900 và 390×844. `no-ai-slop` Edit trên mọi câu sửa, tự đối chiếu `eval.md`: đạt (đã loại câu mở kịch tính, dấu hai chấm hé lộ, câu tài liệu làm chủ ngữ).

## Đợt sửa 2026-10-12 — Giai đoạn II: bộ trang chiếu

### Tác tử và phạm vi

- Vai: tác tử soạn bộ trang chiếu Bài 06 (giai đoạn II), viết tệp. Loại `general-purpose`, mô hình Opus 5.5 (`claude-opus-5-5`), mức `high`, theo brief chung `brief_deck_writer.md`; điều phối viên đối chiếu với lời gọi công cụ. Không commit, không push.
- Đầu vào đã đọc: `planning/quyet-dinh-chuan-2026-10-12.md`; `planning/lec-06/revision-plan-2026-10-12.md` mục A, C, D; `AGENTS.md` (Ngôn ngữ và biên tập, Mẫu RevealJS bắt buộc, Trang tiêu đề mạch, Chuyển và vẽ lại hình, Cấu trúc học tập, Tiêu chuẩn nội dung, Văn phong và mật độ, Tiêu chuẩn trang chiếu và ghi chú, Ghi nhận trong storyboard); `CLAUDE.md` mục Deck structure and content; ghi chú bài giảng đã commit `19323ad`; mục giai đoạn I của nhật ký này; deck, `outline.md`, `storyboard.md` cũ; `lecture-slide.css`; deck mẫu `math-4-AI/2627-1/lecture-07-quy-hoach-tuyen-tinh-va-dong.html`; kỹ năng `no-ai-slop` (`SKILL.md`, `eval.md`) và các phần Outline, Threads, Concept, Revise của `quill/references/workflows.md` (không tạo `quill.json`).
- Tệp đã ghi: `2627-1/lecture-06-dieu-khien-phi-mo-hinh.html` (viết lại theo từng mạch, mỗi lần ghi dưới 150 dòng); `2627-1/img/lec-06/chain-five-states.svg` (dời nhãn "bắt đầu"); `planning/lec-06/outline.md`, `planning/lec-06/storyboard.md` (viết lại); mục này của `review-log.md`. Không sửa ghi chú bài giảng, `lecture-slide.css`, `index.html`, viewer, notebook, mẫu, tệp của bài khác.

### Kết quả

- 7 mạch, 75 trang (deck cũ 45 trang). Sáu trang tiêu đề mạch B00–G00 (`id="mach-2"` … `mach-7`), số trong `span.strand-number` khớp trang "Nội dung" và `#/N` (kiểm bằng Playwright). Mạch mở đầu theo thứ tự bìa → Tiên quyết và quy ước → Mục tiêu → Nội dung → Vấn đề trung tâm → Khung chung. Mạch kết luận có hai trang "Tổng kết", bảng khung chung, bảng hội tụ, bài tập tổng hợp tàu đổ bộ có lời giải, trang trả lời vấn đề trung tâm có "Nguồn:", "Câu hỏi tự kiểm tra", "Bài tập về nhà và tài liệu đọc".
- Thuật ngữ và ký hiệu theo quyết định chung: "lần ghé đầu tiên (first-visit)", "hầu chắc chắn (almost surely)", $T_\pi$, $T_{\pi'}$ chỉ số dưới, $p$, $r$ chữ thường, tên ô chữ đứng $\mathrm A,\dots,\mathrm E$, dấu thập phân phẩy (`0{,}8`). Số hiệu kết quả theo ghi chú: 06.1, 06.3, 06.6, 06.8, 06.9, 06.11, 06.12, 06.14, 06.15, 06.16, 06.18, 06.19, 06.21, 06.22, mỗi trang tối đa một lần, sau phát biểu bằng lời.
- Sáu trang bài tập có lời giải trên mặt trang trùng Bài tập 06.1–06.6 của ghi chú (06.1 bằng fragment, 06.2–06.6 ở trang kế); bài tập tổng hợp G03/G07 là bài 06.17 dự kiến của `exercises.md`.
- Bỏ hai liên kết tới `../RL-hk2-2025-2026/*.pdf`; nguồn ghi bằng "Bài giảng gốc (2025–2026), trang N" trong ghi chú diễn giả.
- Khối `<style>` cục bộ cũ (19 quy tắc theo mã trang, gồm thu khoảng đệm bảng và chiều cao hình) đã bỏ; chỉ còn một quy tắc `text-transform: none` cho KaTeX trong `h2`, `h3`, không đổi cỡ chữ.

### Bảng mã trang cũ → mới

| Loại | Mã |
|---|---|
| giữ mã (sửa nội dung) | A01, A02, A03, A05, B01, B02, B03, B04, B05, B06, B07, C01, C02, C03, C04, C05, C06, C07, C08, D01, D02, D03, D04, D05, D06, D07, D08, E01, E02, E03, E04, E06, E07, E08, F02, F03, F04, F05, G01, G02, G03, G04 |
| bỏ (gộp) | A04 → A07 và ghi chú diễn giả B00; E05 → E10 và ghi chú diễn giả E04; F01 → F04, F08, G06, F12 và ghi chú diễn giả |
| thêm | A07, A08, A09, B00, B08, B09, B10, B11, C00, C09, C10, D00, D10, D11, E00, E09, E10, E11, E12, F00, F06, F07, F08, F09, F10, F12, F13, G00, G05, G06, G07, G08, G09 |

Không có liên kết nào từ ghi chú, notebook hay `index.html` tới mã trang hoặc chỉ số `#/N/k` của deck này (đã tìm bằng `grep`).

### Sai lệch so với kế hoạch A và lý do

| Chỗ | Kế hoạch A | Deck | Lý do |
|---|---|---|---|
| B07/B10, D08/D11 | Bài tập lặp số liệu ví dụ ($\varepsilon=\tfrac14$; mẫu 5 với $\alpha=0{,}8$) | Dùng đúng Bài tập 06.2 ($\varepsilon=0{,}2$, hàng $(4;1;1)$) và 06.4 ($\alpha=0{,}5$) của ghi chú; mẫu 5 ($-1{,}28$) chuyển vào ví dụ D07 | Ghi chú đã commit đổi số liệu (P-18) để bài tập không trùng ví dụ; deck là bản tóm tắt của ghi chú; D11 nêu đối chiếu $\alpha=0{,}8$ cho $-1{,}28$ |
| B11 | Phép kiểm $q=(3,3,-1)$ để trong ghi chú diễn giả | Trang "Cải thiện chính sách khi giữ thăm dò" (nhu cầu, Ví dụ 06.5, trực quan) | Kế hoạch A4 ghi cụm cải thiện thiếu trực giác và ví dụ trên mặt trang; ghi chú có Ví dụ 06.5 trước Mệnh đề 06.6 |
| C10 | Không có | Trang ứng dụng: lượt bị cắt của tàu đổ bộ, Nhận xét 06.10 | A4 ghi bước ứng dụng của Monte Carlo còn yếu; số liệu lấy từ "Trong thực hành" của ghi chú (một lần chạy đã nhúng) |
| D05/D10/D06, E04/E10, E05 | D05 tách thành D05 + D10, D06 giữ bước 4–6; E04 tách, E05 giữ | D10 chứa đủ năm bước (≤ 8 dòng); D06 thành bảng ba sự kiện (Nhận xét 06.13); E10 chứa đủ bốn bước; E05 bỏ | Giả mã vừa một trang; Nhận xét 06.13 là bước ứng dụng có tàu đổ bộ (cầu nối 3 của A5); giữ số trang 75 |
| F12, F10, F13; F01 | F01 giữ làm trang giả thiết chung | F12 (nhu cầu, dãy năm ô $\gamma=0{,}9$), F10 (trực quan), F13 (vai trò từng giả thiết); F01 bỏ | Theo đoạn mở Mục 5, Mục 5.1 và danh sách "Bỏ giả thiết" của ghi chú; giả thiết nền đặt trên mặt F04, F08, G06 vì định lý hội tụ phải nêu giả thiết quyết định trên mặt trang |
| Số hiệu | Mệnh đề 06.8, Định lý 06.24/06.25, Định nghĩa 06.19/06.20 | Mệnh đề 06.6, Định lý 06.21/06.22, Định nghĩa 06.18/06.19 | Số hiệu cuối của ghi chú đã commit |
| G05 | Một trang (tách nếu vượt 80) | G05 + G09 | Bảng sáu hàng tràn khung 16:9 |
| B12, B13 (cân nhắc) | Không có trong kế hoạch | Không thêm; vòng B–C ở ghi chú diễn giả B02, F13, G05; hàng bốn hành động của tàu đổ bộ ở ghi chú diễn giả B05 | Giữ số trang |
| A01 | Đơn vị cần hỏi; câu luận đề dài | "Trường Đại học Công nghệ, Đại học Quốc gia Hà Nội" (quyết định chung §5); luận đề ngắn hơn, 19 âm tiết | Trần 20 âm tiết mỗi dòng |
| A08 | Có dòng đọc trước | Dòng đọc trước chuyển vào ghi chú diễn giả | Trang đã có 7 dòng |
| E00 | Dòng dẫn "… phải tách chính sách hành vi khỏi chính sách đích" | "… phải dùng cực đại của hàng kế tiếp" | Tránh dùng thuật ngữ trước trang định nghĩa có tên tiếng Anh |
| F00 | Từ khóa "GLIE", "Hội tụ gần chắc chắn" | "Tham lam trong giới hạn", "Hội tụ hầu chắc chắn" | Viết tắt chưa giải thích; thuật ngữ đã chốt |
| G08 câu 1 | Sarsa với $\varepsilon=0{,}25$ cố định | Bảng ước lượng từ mẫu có đủ cho Mệnh đề 06.6 không | Câu cũ trùng F05 câu b |
| G03 | "hai giả thiết bị vi phạm" | "các giả thiết bị vi phạm" (Markov, Robbins–Monro, thêm GLIE với Sarsa) | Theo Tình huống 06.1 của ghi chú |
| `data-note-topic-id` | 01–07 | G03, G07 dùng `lec-06-topic-09` | Ghi chú gắn tình huống LunarLander với chủ đề 09 |

### Mật độ trước và sau

| | Trước | Sau |
|---|---:|---:|
| Số trang | 45 | 75 |
| Trang trên 40 âm tiết | 30 | 62 |
| Trang trên 60 âm tiết | 21 | 4 (A02, F13, G06, G04, đều thuộc nhóm trần 80) |
| Trang trên 1,5 lần trần | 3 (D02, D05, F04) | 0 |
| Trung vị âm tiết | 55 | 50 |
| Trang `density.py` gắn cờ | 30 | 16 (6 trang tiêu đề mạch do dòng dẫn 20–23 âm tiết; A08 7 dòng theo quyết định chung; 5 trang có bảng dữ kiện; A02, F13, G06, G04 nhóm trần 80) |

Bảng chi tiết trước/sau cho 30 trang cũ và lý do của 16 cờ còn lại ở `storyboard.md` mục "Mật độ". Đích 40 âm tiết chưa đạt ở đa số trang; không trang nội dung nào vượt trần 60.

### SVG

- Sửa `img/lec-06/chain-five-states.svg`: nhãn "bắt đầu" dời từ $(790,91)$, nơi chồng lên cung D→C, lên $(826,86)$ phía trên bên phải ô D. Không đổi nội dung, hình vẫn dùng trong ghi chú.
- Không tạo SVG mới. `greedy-chain.svg` và `chapter-structure.svg` không còn trên deck nhưng ghi chú dùng, nên giữ. Không có ảnh raster.

### Đề nghị sửa ghi chú

Không có đề nghị bắt buộc. Mọi số liệu trên deck khớp ghi chú (tính lại bằng `deck06_verify.py` trong scratchpad: năm mẫu Sarsa $0;-0{,}6;800;8{,}2;-1{,}28$, Q-learning $0;0{,}2;800;8{,}2;-0{,}64$; lượt có cặp lặp $996,997$; $-0{,}2\to2{,}6$; $q_*(\mathrm D,0)=808{,}1$; tàu đổ bộ $0{,}48\to2{,}748$, $3{,}45\to3{,}045$, $-7{,}3$; khối $0{,}95$, $0{,}9625$; $\sum_k1/(2k^2)\approx0{,}822$; $20^{5/3}\approx147{,}4$; phương sai dừng $2/3$).

### Đề nghị cho `lecture-slide.css` và cấu hình

- Chuyển quy tắc `.reveal.lecture-deck h2 .katex, .reveal.lecture-deck h3 .katex { text-transform: none; }` vào `lecture-slide.css`: chủ đề `white` viết hoa tiêu đề, làm $\varepsilon$ trong tiêu đề thành chữ hoa; quy tắc này cần cho mọi deck có công thức trong tiêu đề. Sau đó bỏ khối `<style>` của deck.
- Deck 01 và 02 đặt `scrollActivationWidth:null`, deck 06 (như mẫu `lecture-template.html`) không đặt, nên ở 390×844 deck 06 chạy chế độ cuộn của Reveal 5. Đề nghị điều phối viên thống nhất cấu hình cho cả học phần; deck này giữ cấu hình hiện có theo brief.
- Ngoài phạm vi tệp của tác tử: `planning/lec-06/analysis.md` chưa có dòng đầu "Hồ sơ lịch sử trước đợt sửa 2026-10-12; không còn phản ánh deck hiện tại." theo quyết định chung §5.

### Tự kiểm `no-ai-slop` (Edit) và `quill`

- Phạm vi: toàn bộ tiêu đề, mặt trang, `alt`, ghi chú diễn giả của 75 trang; `outline.md`, `storyboard.md`, mục này.
- Đã sửa trong lượt tự kiểm: câu luận đề dài và có ba cụm tiếng Anh; câu "Muốn … trong mục tiêu" quá 25 âm tiết ở E00; dòng kết ở B10, F09 viết thành kết luận có điều kiện; không còn "ta thấy", "chúng ta", "rõ ràng", "Trang này", "hãy", mã trang hay mã bài khác trong ghi chú diễn giả (kiểm bằng `grep`).
- Đối chiếu `eval.md`: đạt các mục về lời dẫn rỗng, từ cấm, tương phản nhị phân không chức năng (các câu "không phải … " còn lại là phân biệt toán học: $\delta_t$ không phải sai số so với $q_\pi$, ngân sách không phải tiêu chuẩn hội tụ), kết luận kịch tính, định dạng (in đậm chỉ ở nhãn), gạch ngang dài (không dùng). Câu cuối mỗi trang là kết luận có điều kiện hoặc con số.
- `quill` (bảng kiểm Outline, Threads, Concept, Revise): mọi khái niệm được định nghĩa hoặc nhắc lại trước lần dùng trên mặt trang; thuật ngữ tiếng Anh ở lần đầu (kiểm bằng script, xem bảng Việt–Anh trong `outline.md`); các "sợi" mở ở mạch mở đầu (ô $(\mathrm D,0)$ không được thử, $\gamma=1$ ngoài miền định lý, $q_\pi$ chính xác) đóng ở F12, F13, B10; câu trả lời có điều kiện ở A03 khớp G02.

### Kiểm trình duyệt và kỹ thuật

- Script Playwright Chromium `check_deck06.py` (scratchpad), server reloadserver cổng 8766: duyệt đủ 75 trang bằng `Reveal.slide(h,v,99)` ở 1600×900 và 390×844. Kết quả cuối: 0 lỗi console hoặc trang, 0 `.katex-error`, 0 yêu cầu ra ngoài `localhost:8766`, 0 phản hồi lỗi, không cuộn ngang; ở 16:9 không phần tử nào vượt khung 1280×720 của trang (đo theo hộp bao quanh so với hộp của `section`); số trong `span.strand-number` khớp `#/N/1` cho sáu trang tiêu đề mạch; phím mũi tên chuyển trang. Các trang đã tràn ở lượt kiểm đầu (A03, B09, C07, D03, E02, E03, E06, G05) đã sửa bố cục và kiểm lại.
- Ảnh đã xem: các trang tiêu đề mạch, G05, G09, G01, G06, G04, E04, D06, F05, B09, A03 ở 1600×900; E00, G05 ở 390×844 (`scratchpad/shots06/`). Ở 390×844, Reveal 5 chạy chế độ cuộn và thu nhỏ trang; chữ nhỏ nhưng không tràn, như các deck khác không đặt `scrollActivationWidth`.
- `git diff --check` trên deck, `planning/lec-06/`, `img/lec-06/`: sạch.

### Chỗ cần rà soát kỹ

- Mật độ: trung vị 50 âm tiết, cao hơn đích 40; các trang định lý và thuật toán (C05, D05, E04, F04, F08) giữ đủ giả thiết trên mặt trang.
- F02 nêu tên tiếng Anh của GLIE chỉ trong ghi chú diễn giả.
- E01 và E09 dùng "hành vi" trước định nghĩa chính thức ở E09 (từ thường, chưa phải thuật ngữ).
- Ghi chú diễn giả B09 giải thích chứng minh; cần rà toán đối chiếu với chứng minh Mệnh đề 06.6 trong ghi chú.

## Rà soát năm vai và biên tập (giai đoạn II)

### Tác tử

- Rà soát: năm tác tử chỉ đọc (SV: góc nhìn sinh viên và mật độ; RL: chuyên gia Học tăng cường; TOAN: toán và thuật toán; PB: phản biện sư phạm và `no-ai-slop` Detect; MACH: kết nối và mạch), Opus 5.5 (`claude-opus-5-5`) mức `high`, theo `brief_deck_reviewers.md`; báo cáo `scratchpad/deckrev-06-{SV,RL,TOAN,PB,MACH}.md`. Kết quả: 0 chặn bàn giao, 0 nghiêm trọng; các phát hiện trung bình trùng nhau giữa các vai.
- Biên tập: tác tử biên tập viết tệp, Opus 5.5 (`claude-opus-5-5`), mức `high`, theo `brief_deck_writer.md` và `brief_deck_editor.md`, tiếp quản từ tác tử soạn trước (đã dừng); điều phối viên đối chiếu loại và mô hình với lời gọi công cụ. `no-ai-slop` chế độ Edit. Không commit, không push.
- Quyết định của điều phối viên được áp dụng nguyên văn ở A03, E00, E01, A07, A05/A09, F13, G06, F08, E07, E03/G01, G04, C10, D06, B01, G02, G07, C05/D05, C02→C04, B09, D03/E02, A03/C07 (nhãn SVG), G05/C04/F06 và toàn bộ danh sách mục nhẹ. Trước khi sửa, điều phối viên đã bỏ khối `<style>` cục bộ của deck (quy tắc KaTeX trong tiêu đề nay ở `lecture-slide.css`).
- Tệp đã ghi: deck; `img/lec-06/chain-five-states.svg` và `img/lec-06/episode-return.svg` (nhãn phóng 1,3 lần, xem dưới); `outline.md`, `storyboard.md`, mục này. Ghi chú bài giảng, `lecture-slide.css`, `index.html`, viewer, notebook không đổi. Ngoài phạm vi deck: sửa mẫu tuyến `**/api-reloadserver/**` trong `scratchpad/deck_check.py` (mẫu cũ `**/reloadserver*` không chặn được lệnh nạp lại của reloadserver).

### Bảng phát hiện và xử lý

Mã theo vai: SV, RL, TOAN, PB, MACH (MACH dùng T1–T7 cho mức trung bình, N cho mức nhẹ).

| Mã | Trang | Mức | Phát hiện | Trạng thái |
|---|---|---|---|---|
| RL-1, MACH-N (A03), PB (chấp nhận), SV (A03) | A03, E00, E01 | trung bình | "hành vi", "đích" dùng như thuật ngữ trước Định nghĩa 06.14 | đã sửa: A03 dòng 5 "Dữ liệu từ chính sách còn thăm dò, mục tiêu theo chính sách tham lam"; E00 dòng dẫn mới; E01 "chính sách sinh dữ liệu chọn $A'=0$"; ghi chú A03 nói ký hiệu được định nghĩa ở phần cùng số |
| RL-2 | F13, ghi chú B02 | trung bình | hàng $\gamma<1$ không là phản ví dụ cho $Q_t\to q_*$ | đã sửa: cột thành "Hệ quả", ô "$\gamma=1$: toán tử Bellman tối ưu không còn co theo chuẩn cực đại; định lý không áp dụng, cần giả thiết thay thế"; ghi chú F13 nêu vòng B–C chỉ minh họa giá trị không hữu hạn của một chính sách, dẫn Bertsekas và Tsitsiklis (1996) §2.2; ghi chú B02 "nằm ngoài giả thiết $\gamma<1$ của bài" |
| RL-3, PB-2, MACH-N (E07) | E07 | trung bình | tỉ số lấy mẫu quan trọng chỉ xuất hiện để bị phủ định | đã sửa: hai dòng nhu cầu ($\rho=\pi(A\mid S)/b(A\mid S)$ của dự đoán TD(0) khác chính sách) trước nhận xét; gộp hai dòng giả thiết |
| RL-4 | ghi chú E03, G01; outline | trung bình | thiếu nhận định ước lượng cao do cực đại (nguồn tr. 28) | đã sửa: ghi chú E03 (Sutton và Barto §6.7, Bài 09), ghi chú G01; bảng ánh xạ trang 28 trong `outline.md` |
| RL-5, MACH-T4 | G06, F08 | trung bình | "chưa có định lý tới $q_*$" nói quá; trích §5.3 sai đối tượng; mạch 6 không đóng sợi Monte Carlo | đã sửa: G06 "bài không nêu định lý tới $q_*$"; F08 thêm dòng "Điều khiển Monte Carlo trộn lợi tức nhiều $\pi_k$; bài không nêu định lý tương ứng"; ghi chú F08 nêu §5.3 nói về biến thể điểm bắt đầu thăm dò, Tsitsiklis (2002) |
| RL-6, TOAN-2 | ghi chú F02 | nhẹ | $\varepsilon=1/t$ toàn cục mâu thuẫn bài học F07 | đã sửa: nêu cả $\varepsilon_t(s)=c/n_t(s)$ của Singh và cộng sự (2000) |
| RL-7, PB-11 | D05 | nhẹ | đầu vào chỉ có $\varepsilon$ hằng | đã sửa: "$\varepsilon$ hoặc lịch $\varepsilon_t$"; ghi chú nói điều kiện hội tụ đòi lịch giảm |
| RL-8, RL-9 | F02 | nhẹ | tên tiếng Anh GLIE chỉ trong ghi chú; "độ phủ" chưa gọi tên | đã sửa: tên đầy đủ trên mặt trang (dòng riêng), "thăm dò vô hạn (độ phủ)"; dòng ví dụ lịch chuyển vào ghi chú để giữ ≤ 60 âm tiết |
| RL-10, PB-10, MACH-N (D04) | D04 | nhẹ | "sai lệch" khác "sai số TD" của Bài 05; "học theo chính sách" trước E09 | đã sửa: "Sai số TD (TD error, Bài 05)"; bỏ vế "Sarsa học theo chính sách" khỏi mặt trang, ghi chú báo trước định nghĩa |
| RL-11, MACH-T1 | A07, A09 | trung bình (MACH) / nhẹ (RL) | thiếu nhắc lại Bài 04–05; chưa nêu lý do chuyển $V$→$Q$ | đã sửa: A07 ba dòng "Nhắc lại:" (Bài 03, 04 với $q_*=T_*q_*$ và $T_*$ co, 05 với Monte Carlo, TD(0), Robbins–Monro theo trạng thái); A09 dòng nhắc lại Bài 05 với $\pi$ cố định và dòng "Chọn hành động theo $V$ cần $p$ và $r$; theo bảng $Q$ chỉ cần so một hàng"; ghi chú A09 nêu công thức một bước nhìn trước |
| RL-12, PB-7 | C05, D05, E04 | trung bình (PB) | $d_0$, $n$, $h$ chưa định nghĩa trên mặt trang | đã sửa: A07 "$S_0\sim d_0$ (phân phối đầu)"; D05 dòng "$n(s,a), h$: số cập nhật của cặp và tổng" |
| RL-13 | B06 | nhẹ | MDP thiếu tên tiếng Anh | đã sửa |
| RL-14, PB-21 | E09, ghi chú F08, G06; F06, F09, G07 | nhẹ | "Monte Carlo điều khiển" lẫn "điều khiển Monte Carlo"; ba cách gọi khối cực đại | đã sửa: chốt "điều khiển Monte Carlo" và "khối cực đại (xác suất trên tập cực đại)", ghi vào bảng thuật ngữ `outline.md` |
| RL-15, TOAN-3, PB-6, SV (G07), MACH (ngoài vai) | G07 | trung bình (PB) | ± không nói nghĩa; câu kết đọc thành xếp hạng | đã sửa: "100 lượt kiểm tra (trung bình ± sai số chuẩn)"; câu kết "Hiệu ghép cặp $32{,}8\pm46{,}2$ (nửa khoảng tin cậy 95 %) chứa 0: chưa xếp hạng được"; ghi chú: tổng phần thưởng không chiết khấu, $46{,}2=1{,}96$ lần sai số chuẩn |
| RL-16, MACH-T5 | G01, ghi chú G04, A09 | trung bình (MACH) | bảng tổng kết không thu hồi theo/khác chính sách; nối DQN, bán gradient | đã sửa: cột "Dữ liệu dùng" ghi theo/khác chính sách; ghi chú G04 nối DQN (Bài 08–09); ghi chú A09 nối bán gradient (Bài 07) |
| RL-17 | ghi chú A03 | nhẹ | nguồn ghi lượt minh họa tối đa ba bước | đã sửa |
| RL-18, TOAN-1, PB-25, MACH-T7, SV (G04) | G04 | trung bình | bảng trỏ tới 06.13–06.17 của tệp chưa có; thiếu 06.14 | đã sửa theo brief mục 4: bảng chỉ ghi 06.1–06.12 theo mạch; dòng "Tệp bài tập: chưa có"; ghi chú không mô tả tệp chưa có; số dự kiến (gồm 06.14) ghi dưới đây |
| TOAN-4 | D07, E06 | nhẹ | cập nhật mẫu 5 thiếu giá trị cũ | đã sửa: "$0+0{,}8\cdot(\dots)$" |
| TOAN-5, SV (B09) | B09 | trung bình (SV) | ký hiệu $w_a$ khác $w(a\mid s)$; bước $q_\pi=r+\gamma\sum p\,v_\pi$ chỉ trong ghi chú | đã sửa: "$w_a=w(a\mid s)$"; dòng "Vì $q_\pi(s,a)=r(s,a)+\gamma\sum_{s'}p(s'\mid s,a)v_\pi(s')$, vế trái là $(T_{\pi'}v_\pi)(s)$"; storyboard thêm 1 phút cho B09 |
| TOAN-6 | F13 | nhẹ | thiếu "độc lập" cho mục tiêu ±1 | đã sửa |
| TOAN-7 | E02 | nhẹ | thiếu $\gamma=1$ | đã sửa |
| PB-1, MACH-T3, SV (C10) | C10 | trung bình | nhắc "bảng Sarsa" trước mạch 4 | đã sửa: "chính sách tham lam học được trong bài thực hành"; tên Sarsa trong ghi chú |
| PB-3, SV (D06) | D06 | trung bình | nhận xét "ba mục tiêu khác nhau" sai so với bảng; ô "giữ nguyên" mơ hồ | đã sửa: "Chỉ kết thúc lượt bỏ số hạng $\gamma Q_t(S_{t+1},A_{t+1})$"; ô hết ngân sách ghi đủ mục tiêu bootstrap. Không dùng chữ "bootstrap" trên mặt trang vì thuật ngữ chỉ có trong ghi chú diễn giả A09 |
| PB-4 | B01 | trung bình | so sánh 998 với 10 thiếu chính sách tiếp nối | đã sửa: "ngược với lợi tức khi đi trái liên tục $(998>10)$"; ý "số khởi tạo chưa là quan sát" chuyển vào ghi chú (C02 giữ ý này trên mặt trang) |
| PB-5, MACH-T6, SV (G02) | G02, ghi chú G07 | trung bình | ba hàng D khác khởi tạo; chuyển đột ngột G07→G02 | đã sửa: dòng "Bài toán:", cột "Khởi tạo"; câu nối cuối ghi chú G07 và đầu ghi chú G02 |
| PB-8, MACH (ngoài vai) | E01 | trung bình | Nhu cầu mô tả sai đối tượng | đã sửa: "giá trị của $(\mathrm C,0)$ khi từ B trở đi luôn chọn hành động tốt nhất" |
| PB-9 | C03, C04, C07 | nhẹ | bước ví dụ của "lần ghé đầu tiên theo cặp" vắng trên mặt trang | đã xử lý theo cách thứ hai của PB: storyboard ghi bước ví dụ gộp vào bài tập C08/C09 (C03 đã 6 dòng) |
| PB-12 | B06 | nhẹ | "Ý nghĩa:" không đọc kết quả | đã sửa: "trong lớp $\varepsilon$-mềm, bước $\varepsilon$-tham lam không giảm giá trị (Mệnh đề 06.6)" và dòng "$\varepsilon=0$ cho định lý cải thiện của Bài 04"; "với mọi $s$" chuyển vào công thức để giữ ≤ 60 âm tiết |
| PB-13 | B05 | nhẹ | hai định nghĩa trên một trang; chuyển $\varepsilon$-mềm sang B11 | từ chối: định nghĩa $\varepsilon$-mềm đặt cạnh $\varepsilon$-tham lam để nêu ngay quan hệ "mọi $\varepsilon$-tham lam đều $\varepsilon$-mềm, chiều ngược sai" (ghi chú có cùng thứ tự Định nghĩa 06.3, 06.4); chuyển sang B11 đẩy B11 tới 60 âm tiết. PB ghi đề xuất là tùy chọn. Câu nối B05→B11 thêm vào ghi chú B05 (MACH) |
| PB-14 | B07, G03 | nhẹ | số hiệu đứng thay phát biểu | đã sửa: "mệnh đề cải thiện (Mệnh đề 06.6)", "giả thiết hội tụ bị vi phạm (Định lý 06.21–06.22)" |
| PB-15 | B10 | nhẹ | câu kết lặp câu 4 | đã sửa: bỏ câu kết. Không dùng câu thay thế PB gợi ý ("thay $Q_0$ bằng $q_\pi$ ước lượng") vì mệnh đề cần $q_\pi$ chính xác |
| PB-16 | E12 | nhẹ | câu kết kiểu khẩu hiệu | đã sửa: "Với $A'=1\notin\mathcal G_Q(\mathrm B)$, hai mục tiêu lệch nhau 799" |
| PB-17 | E02, D03, D07 | nhẹ | tiêu đề E02 không song song D03 | đã sửa: ba tiêu đề theo một khuôn "Ví dụ: năm mẫu chuyển, Sarsa ở mẫu 1–2", "… Q-learning ở mẫu 1–2", "… Sarsa ở mẫu 3–5" để tiêu đề E02 vừa một dòng (E02 tràn khung khi tiêu đề hai dòng) |
| PB-18, PB-19, PB-20 | ghi chú B00, C00, D00, E00, F00, G00, A09, D01, E06, F08 | nhẹ | tài liệu làm chủ ngữ; lời kể quy trình | đã sửa: mở bằng đối tượng hoặc kết quả kế thừa, cấu trúc câu khác nhau giữa các mạch; bỏ câu quy trình ở A09, D01, E06 (lý do nguồn ở storyboard) |
| PB-22 | D07, E06, E11, F06, F07 | nhẹ | trang ví dụ thiếu "Tính …"/"Xác định …" | đã sửa |
| PB-23 | F05, D08 | nhẹ | đề dạng câu hỏi | đã sửa: động từ học tập |
| PB-24, MACH-N (G00) | G00 | nhẹ | từ khóa là tên trang; dòng dẫn đổi đích | đã sửa: "Bài toán tàu đổ bộ"; dòng dẫn "Muốn trả lời bài toán tại D, …" (21 âm tiết) |
| MACH-T2 | ghi chú C02, C03, C04 | trung bình | sợi ô $(\mathrm D,0)$ đứt ở C02→C04 | đã sửa: ghi chú C02 trỏ sang C03 (cặp lặp, bộ đếm), ghi chú C03 nối sang C04, ghi chú C04 nêu bảng nghiêng trái lấy từ bài giảng gốc trang 17, thăm dò xảy ra ở B, và xác suất thử $(\mathrm D,0)$ dưới bảng nghiêng phải là $\varepsilon/2$ |
| MACH-N | E03, E11, E12 | nhẹ | ba trang cùng nêu điều kiện trùng mục tiêu | đã sửa: dòng điều kiện của E03 chuyển vào ghi chú; câu 2 của E08 còn là bước suy luận |
| MACH-N | E06→E11→E07 | nhẹ | thứ tự khác ghi chú | đã sửa: E07 dời lên trước E11; E11 đứng sát bài tập E08 |
| MACH-N | F12 | nhẹ | dùng lại luận điểm B03 mà không đánh dấu; không nêu lý do đổi $\gamma$ | đã sửa: nhãn "Nhắc lại:"; ghi chú "Ví dụ chuyển sang $\gamma=0{,}9$ vì các định lý của phần này giả thiết $\gamma<1$". Không dùng câu MACH gợi ý "$q_*$ chỉ xác định khi $\gamma<1$" vì RL-2 chỉ ra $q_*$ của dãy năm ô vẫn hữu hạn khi $\gamma=1$ |
| MACH-N | G09, G01, G06 | nhẹ | thứ tự hàng ngược; công thức lặp | đã sửa thứ tự hàng (Monte Carlo, Sarsa, Q-learning ở cả ba bảng). Từ chối bỏ cột công thức của G09: bảng `Kết quả | Giả thiết không được bỏ | Công thức hoặc thuật toán` là khuôn bắt buộc |
| MACH-N, PB | G05, G09 | nhẹ | hai trang cùng tiêu đề "Tổng kết" | đã sửa: "Kết quả về giá trị hành động và thăm dò", "Kết quả về ba thuật toán" |
| MACH-N | G08 | nhẹ | câu 3 trùng G07 | đã sửa: "Lịch $\alpha_t=1/t$ theo thời gian toàn cục có đủ Robbins–Monro theo cặp?"; lời giải trong ghi chú dựa vào ví dụ F07 |
| MACH-N, SV | D00, E00, B00, F00 | nhẹ | KaTeX trong từ khóa và dòng dẫn trang tiêu đề mạch | đã sửa: "Bộ năm của mẫu chuyển", "Bộ bốn của mẫu chuyển", "ε" chữ thường ở B00, dòng dẫn F00 không KaTeX |
| MACH-N | B05→B11 | nhẹ | thiếu câu nối | đã sửa (ghi chú B05) |
| MACH-N | A08 | nhẹ | 7 dòng | chấp nhận theo quyết định chung §5 |
| SV | D03, E02 | trung bình | hình trong `grid2` quá nhỏ | đã sửa: hình ra hàng riêng (`figure short`), phép tính thành bảng `Mẫu | Ô | Y | δ | Giá trị mới` (cùng khuôn bảng của E11) |
| SV | toàn deck | trung bình | nhịp 120 phút chặt | đã sửa: storyboard ghi năm cặp bài tập có phần tự làm thuộc khối 30 phút, trang lướt C10, E11, F13, thêm 1 phút cho B09 (lấy từ E11, F13) |
| SV | cấu hình | trung bình | thiếu `scrollActivationWidth:null` | đã sửa |
| SV | G05, C04, F06 | nhẹ | công thức trong ô bảng quá nhỏ | đã sửa: công thức một dòng ở G05, số thập phân ở C04, F06 |
| SV | A03, C07 | nhẹ | nhãn SVG nhỏ | đã sửa: phóng nhãn 1,3 lần trong `chain-five-states.svg` (28→36, 25→32; dời nhãn "bắt đầu") và `episode-return.svg` (28→36, 27→34, 25→32; nới khoảng cách ba vạch lợi tức, chiều cao 265→285). Nội dung, chiều mũi tên, tỉ lệ giữ nguyên |
| SV | D03 so với A03 | nhẹ | hai ký pháp nhãn cạnh "0; thưởng −1" và "0 · −1" | từ chối trong đợt này: ghi chú bài giảng đã commit trích nguyên văn nhãn trong alt (dòng 593, 711, 906); đổi SVG làm alt của ghi chú sai. Ghi vào đề nghị sửa ghi chú |
| SV | B11, B07, C06, D06 | nhẹ | "một trạng thái"; trạng thái ngoài dãy năm ô; ký pháp $f$; ô "giữ nguyên" | đã sửa |
| SV | B01, D05, B06, E06, E12, G09 (thêm A03, B11, D04, D07, G05, G07, F06) | nhẹ | ngắt dòng xấu | đã sửa bằng nhóm `{…}` trong KaTeX hoặc khoảng trắng không ngắt; kiểm bằng ảnh |
| SV | B07, C08, D08, E08, G03, G08 | nhẹ | khung "Câu hỏi:" chỉ chứa nhãn | đã sửa: `div.check` bao cả nhãn và danh sách |
| SV | A09, D04, ghi chú A07 (và B02, D05, E03, E04, B06, D03, E02, F07) | nhẹ | chữ Việt có dấu trong `\text{}` | đã sửa: không còn `\text{` nào trong deck; trạng thái kết thúc viết $S_{t+1}\in\mathcal S^+\setminus\mathcal S$ hoặc "$Q(s,\cdot)=0$ khi $s\notin\mathcal S$" (ký hiệu đã có ở A07) |
| SV | ghi chú B02, F08, F13 | nhẹ | ghi chú dài | đã sửa: mọi ghi chú 40–150 từ (không tính dòng nguồn, mỗi công thức tính một) |
| SV | `p.strand-keys` 0,72em | nhẹ | dưới 0,75em | ngoài phạm vi (CSS dùng chung); đề nghị cho điều phối viên |
| SV | A01–A09 | nhẹ | không thấy chân trang ở mạch mở đầu | ngoài phạm vi (CSS dùng chung); đề nghị điều phối viên kiểm |

### Đề nghị sửa ghi chú (sau giai đoạn II)

| Vị trí trong ghi chú | Nội dung sửa | Nguồn |
|---|---|---|
| Dòng 852 (mở Mục 4) | "giá trị của việc hành động tốt nhất từ C trở đi" → "giá trị của $(\mathrm C,0)$ khi từ B trở đi luôn chọn hành động tốt nhất" | PB 8, MACH |
| Mục 5.4, dòng 1172 ("mỗi giả thiết bị bỏ đều có phản ví dụ"), gạch "Bỏ $\gamma<1$"; Nhận xét 06.20 và 06.2 | Bỏ $\gamma<1$ thì định lý không còn áp dụng, cần giả thiết thay thế; vòng B–C chỉ minh họa một chính sách có giá trị không hữu hạn; với $\gamma=1$, $q_*$ của dãy năm ô vẫn hữu hạn ($q_*(\mathrm D,0)=998$; bài toán đường đi ngắn nhất ngẫu nhiên, Bertsekas và Tsitsiklis 1996, §2.2, §5.6). Deck đã sửa F13 theo hướng này (lệch tạm thời với ghi chú) | RL 2 |
| Mục 5.2, dòng 1100 (câu dẫn Sutton và Barto §6.4 về $\varepsilon=1/t$) | Thêm lịch theo trạng thái $\varepsilon_t(s)=c/n_t(s)$ của Singh và cộng sự (2000), hoặc nói rõ $t$ toàn cục vẫn cần kiểm thăm dò vô hạn theo từng cặp (cùng lý do Ví dụ 06.15) | RL, TOAN |
| Nhận xét 06.17, dòng 993 | "hệ số lấy mẫu quan trọng" → "tỉ số lấy mẫu quan trọng" (khớp Định nghĩa 06.24, Bài tập 06.7, deck) | TOAN, PB 3 |
| Đoạn "Trong thực hành" sau Nhận xét 06.10, dòng 633 | "các lượt của chính sách Sarsa tham lam" đứng trước Mục 3: viết "chính sách tham lam học được trong bài thực hành" hoặc thêm "(Thuật toán 06.12, Mục 3)" | PB 2 |
| Tóm tắt chương, dòng 1401 | Câu so Monte Carlo "xếp trái" với Sarsa, Q-learning "xếp phải" nêu rõ hai khởi tạo khác nhau (nghiêng trái, nghiêng phải) | MACH 2 |
| Mục 2.2, dòng 543 | Câu "Để ô $(\mathrm D,0)$ nhận dữ liệu, lượt phải được sinh bởi chính sách $\varepsilon$-tham lam" đứng trước ví dụ dùng bảng nghiêng trái, nơi $(\mathrm D,0)$ đã là hành động tham lam: viết lại thành ví dụ minh họa thăm dò tại B theo bảng của bài giảng gốc (trang 17); khả năng thử $(\mathrm D,0)$ dưới bảng nghiêng phải ở Ví dụ 06.4 và 06.14 | MACH 1 |
| Ví dụ 06.11 (tiêu đề "Một cập nhật Q-learning") | Tùy chọn: đổi thành "Q-learning ở mẫu 1–2" để khớp tiêu đề E02 | PB 4 |
| Alt hình dòng 593, 711, 906 | Tùy chọn: nếu thống nhất ký pháp nhãn cạnh của `sarsa-target.svg`, `q-learning-target.svg` với "0 · −1" của `chain-five-states.svg`, `episode-return.svg`, sửa alt tương ứng cùng lúc | SV |

### Số dự kiến của `exercises.md` (cho giai đoạn III; không ghi trên deck)

Theo `revision-plan-2026-10-12.md` mục D: 06.13 (mạch 3, 5: dãy sáu ô, Monte Carlo lần ghé đầu tiên và Q-learning), 06.14 (mạch 2: chứng minh $\pi_\varepsilon$ là $\varepsilon$-mềm, phản ví dụ chiều ngược), 06.15 (mạch 4: notebook, $Y=R$ khi cắt ngắn so với bootstrap), 06.16 (mạch 6: notebook, lịch thỏa GLIE và Robbins–Monro), 06.17 (mạch 7: chọn phương pháp cho tàu đổ bộ, trùng G03/G07). Khi tệp có, bảng `Mạch | Bài tập` của G04 thêm các số này và đổi dòng "Tệp bài tập: chưa có" thành liên kết viewer.

### Mật độ trước và sau vòng biên tập

| | Trước | Sau |
|---|---:|---:|
| Số trang | 75 | 75 |
| Trang trên 40 âm tiết | 62 | 64 |
| Trang trên 60 âm tiết | 4 (A02, F13, G06, G04; nhóm trần 80) | 6 (A02 73, F13 79, G01 67, G06 73, G02 77, G04 61; nhóm trần 80, G02 có ngoại lệ ghi trong storyboard) |
| Trang nội dung trên 60 | 0 | 0 |
| Trung vị | 50 | 52 |
| Dòng `density.py` gắn cờ | 16 | 18 (thêm E11: bảng đếm từng hàng; G01: bảng so sánh, nhóm trần 80) |

Các trang tăng mật độ do quyết định của điều phối viên (A07, A09, E07, F02, F08, F13, G02, G07) đã được cắt chữ ở chỗ khác để không trang nội dung nào vượt 60; `density.py` đếm cả dấu câu đứng riêng sau khi bỏ KaTeX nên số âm tiết thật thấp hơn vài đơn vị.

### Tự kiểm `no-ai-slop` (Edit) và `eval.md`

- Phạm vi: mọi câu mới hoặc viết lại trên mặt trang, `alt`, ghi chú diễn giả của các trang trong bảng trên; `outline.md`, `storyboard.md`, mục này.
- Đã sửa trong lượt tự kiểm: mẫu "dramatic fragmentation" ở D06, "summary-recap" ở B10, "kicker" ở E12, "synonym cycling" (điều khiển Monte Carlo, khối cực đại), tài liệu làm chủ ngữ và lời kể quy trình trong ghi chú B00…G00, A09, D01, E06, F08.
- Đối chiếu `eval.md`: không từ cấm, không lời dẫn rỗng, không tương phản nhị phân trang trí (các câu "không phải …" còn lại là phân biệt toán học: sai số TD so với sai số tới $q_\pi$; ngân sách so với tiêu chuẩn hội tụ; hàng $\gamma<1$ "không là phản ví dụ" trong ghi chú F13), không câu kết khẩu hiệu, không gạch ngang dài, in đậm chỉ ở nhãn. Câu cuối mỗi trang đổi là kết luận có điều kiện hoặc con số. `grep` không thấy "ta thấy", "chúng ta", "rõ ràng", "hãy", "Trang này", "Phần này", "đáp án", "tổng thưởng", `\text{` trong deck.

### Kiểm trình duyệt và kỹ thuật

- Playwright Chromium, server reloadserver cổng 8766, chặn lệnh nạp lại `**/api-reloadserver/**`. `scratchpad/deck_check.py` (75 trang, cả hai cỡ 1600×900 và 390×844): 0 lỗi hoặc cảnh báo console (kể cả cảnh báo KaTeX về chữ Việt), 0 `.katex-error`, 0 yêu cầu ra ngoài localhost, 0 tài nguyên lỗi, không cuộn ngang. Danh sách "overflow" và "small_font" của script là cờ giả đã biết (đo cả nút `.katex-mathml` ẩn; chia cỡ chữ cho hệ số co).
- Đo tràn khung bằng script riêng `scratchpad/ed06/ovf2.py` (bỏ `.katex-mathml` và ghi chú, đo theo đơn vị trang 1280×720): 0 trang tràn dọc hay ngang. Lượt đo đầu sau sửa phát hiện E02 tràn dọc (816 px, tiêu đề hai dòng) và B09 tràn ngang (1343 px, công thức $w(a\mid s)$); đã sửa (tiêu đề một dòng, bảng; $w_a$) và đo lại. Ba trang cao nhất: B09 699, D03 690, E02 684 px.
- Số trong `span.strand-number` của B00…G00 bằng $h+1$ của `Reveal.getIndices` (2…7), `#/7/1` mở G00; phím mũi tên phải và xuống chuyển trang. Ở 390×844 với `scrollActivationWidth:null`, Reveal không vào chế độ cuộn, trang thu nhỏ trọn khung, không cuộn ngang.
- Ảnh đã xem (1600×900): A07, A03, A09, B00, B01, B02, B06, B09, B07, B10, B11, C04, C07, C06, C10, C08, D00, D03, D04, D05, D06, D07, D08, E00, E01, E02, E03, E04, E06, E07, E11, E12, F00, F02, F06, F07, F08, F12, F13, F05, G00, G05, G09, G01, G06, G03, G07, G02, G08, G04; ở 390×844: D03, E00, G02. Hai SVG sửa được xem riêng. Ảnh ở `scratchpad/ed06/shots/`.
- `git diff --check` trên deck, `img/lec-06/`, `planning/lec-06/`: sạch.

### Đề nghị cho `lecture-slide.css`

- `p.strand-keys` 0,72em, dưới ngưỡng 0,75em cho chữ thân bài (SV): cân nhắc nâng lên 0,75em cho mọi deck, hoặc ghi nhận là chú thích ngắn đã được vai sinh viên xác nhận đọc được.
- Chân trang không hiện ở mạch mở đầu (SV): kiểm quy tắc ẩn chân trang của CSS chung có chủ ý không.

## Rà lại vòng 2 và sửa (giai đoạn II)

### Tác tử

- Rà lại: hai tác tử chỉ đọc, Opus 5.5 (`claude-opus-5-5`) mức `high`. TOAN rà lại toán và thuật toán trên cả 75 trang. MACH rà lại mạch và kết nối các trang đã đổi. Báo cáo ở `scratchpad/deckrecheck-06-TOAN.md` và `scratchpad/deckrecheck-06-MACH.md`. Kết quả: 0 chặn, 0 nghiêm trọng; 1 trung bình (TOAN, A07); 5 nhẹ của TOAN và 9 nhẹ của MACH (N1–N9). Các phát hiện của vòng trước đều được xác nhận đạt, hoặc bị từ chối với lý do hợp lý.
- Sửa: tác tử biên tập của vòng trước (Opus 5.5, `high`), chế độ `no-ai-slop` Edit, theo quyết định của điều phối viên. Không commit.

### Bảng phát hiện và xử lý

| Mã | Trang | Mức | Phát hiện | Trạng thái |
|---|---|---|---|---|
| TOAN-R1 | A07 | trung bình | Viết "$q_*=T_*q_*$" không khớp Bài 04, vì $T_*$ ở Bài 04 tác động trên bảng $V$ | Đã sửa: dòng "$v_*=T_*v_*$ với $T_*$ co khi $\gamma<1$; $q_*(s,a)=r(s,a)+\gamma\sum_{s'}p(s'\mid s,a)v_*(s')$" nối với dòng nhắc lại Bài 04. Quy ước $\mathbb E_\pi$ chuyển vào ghi chú diễn giả để trang giữ ≤ 60 âm tiết. Ghi chú: $T_*$ tác động trên bảng $V$ |
| TOAN-R2 | F10 | nhẹ | Tính co của dạng $Q$ của toán tử được gán cho Bài 04 | Đã sửa: "co khi $\gamma<1$, cùng lập luận như $T_*$ ở Bài 04" |
| TOAN-R3 | F07 | nhẹ | Chữ "cần" đọc thành điều kiện cần | Đã sửa: "định lý hội tụ TD(0) giả thiết … theo từng trạng thái (Bài 05)" |
| TOAN-R4 | B06 | nhẹ | "$\varepsilon=0$ cho định lý cải thiện Bài 04" nói quá | Đã sửa: "$\varepsilon=0$ là trường hợp tham lam của định lý cải thiện Bài 04". Dòng "Ý nghĩa:" bỏ chữ "bước" để giữ ≤ 60 âm tiết |
| TOAN-R5 | G07 | nhẹ | Viết "nửa khoảng tin cậy" | Đã sửa: "nửa độ rộng khoảng tin cậy 95 %". Bỏ chữ "kiểm tra" ở dòng trên để giữ 60 âm tiết |
| TOAN-R6 | D05 | nhẹ | Đầu ra không nói giá trị $\varepsilon$ nào | Từ chối: giữ đúng cách viết đầu ra của Thuật toán 06.12 trong ghi chú đã commit. Dòng đầu vào đã cho phép "$\varepsilon$ hoặc lịch $\varepsilon_t$", và chính sách đầu ra tham lam theo $\varepsilon$ hiện hành |
| MACH-N1 | E00 | nhẹ | Từ khóa "Dữ liệu hành vi" đứng trước Định nghĩa 06.14 | Đã sửa: đổi thành "Chính sách sinh dữ liệu" |
| MACH-N2 | A03, ghi chú A03 | nhẹ | Dùng "thăm dò tắt dần", cụm chưa được định nghĩa; ghi chú chỉ sai chỗ định nghĩa | Đã sửa: dòng 6 thành "Sarsa thêm tham lam trong giới hạn". Ghi chú: $Q(S',A')$ định nghĩa ở phần 4, độ phủ và tham lam trong giới hạn ở phần 6, $q_*$ nhắc lại từ Bài 04 |
| MACH-N3 | E11 | nhẹ | Dòng "Diễn giải:" trả lời trước câu 2 của E08 | Đã sửa: vế "trùng khi $A_{t+1}\in\{1,2\}$" chuyển vào ghi chú E11 |
| MACH-N4 | E07 → E11 | nhẹ | Chưa có câu nối giữa hai trang | Đã sửa: câu mở ghi chú E11 kiểm giả thiết độ phủ trên tàu đổ bộ. Hành vi $\varepsilon$-tham lam có $\varepsilon\ge\varepsilon_{\min}=0{,}05$ và bốn hành động, nên ở mỗi lần ghé ô, mỗi hành động có xác suất ít nhất $0{,}05/4=0{,}0125$ (khớp ghi chú B05 và notebook) |
| MACH-N5 | F08, G06 | nhẹ | Lấy "bài" làm chủ ngữ trên mặt trang | Đã sửa: F08 "Điều khiển Monte Carlo trộn lợi tức nhiều $\pi_k$; chưa có định lý hội tụ tổng quát". G06 "chưa có định lý tổng quát tới $q_*$". Nguồn (Sutton và Barto §5.3, biến thể điểm bắt đầu thăm dò là vấn đề mở; Tsitsiklis 2002 cho lời giải từng phần) giữ trong ghi chú F08 để trang không vượt 60 âm tiết |
| MACH-N6 | D03 | nhẹ | Dùng $\delta$ trước khi nhắc lại | Đã sửa: dòng dữ kiện thêm "$\delta=Y-Q(S,A)$" và rút gọn thành "Tính mẫu 1, 2", để dòng vừa một hàng và trang không tràn khung |
| MACH-N7 | A07 | nhẹ | "TD(0)" xuất hiện lần đầu mà chưa có tên Việt | Đã sửa: "sai phân thời gian TD(0)". Tên tiếng Anh nằm trong ghi chú A07 |
| MACH-N8 | ghi chú C00, D00, E00 | nhẹ | Ba câu cuối cùng một khuôn "để lại một giới hạn: …" | Đã sửa: ba câu viết thành câu thường, mỗi câu một cấu trúc khác |
| MACH-N9 | `storyboard.md` | nhẹ | Hàng E03 và F08 chưa khớp deck | Đã sửa |

### Đề nghị sửa ghi chú (bổ sung)

| Vị trí trong ghi chú | Nội dung sửa | Nguồn |
|---|---|---|
| Mục 5.1 ("Toán tử ấy là ánh xạ co khi $\gamma<1$", dẫn ghi chú Bài 04, Mục 4) | Nói rõ đây là dạng $Q$ của toán tử Bellman tối ưu, co theo cùng lập luận của Mệnh đề 04.24. Bảng ký hiệu (dòng 58) chỉ định nghĩa $T_*$ trên bảng $\mathcal S\to\mathbb R$ | TOAN vòng 2 |

### Mật độ và kiểm tra

- Âm tiết các trang đổi, trước → sau vòng 2:
  - A07 59→60; A03 60→59; B06 58→60; D03 33→28
  - E00 42→43; E11 48→42
  - F10 52→56; F07 56→58; F08 59→60
  - G06 73→74 (nhóm trần 80); G07 60→60
- Toàn deck: 64/75 trang trên 40 âm tiết; 6 trang trên 60, tất cả thuộc nhóm trần 80 (A02, F13, G01, G06, G02, G04); trung vị 52. `density.py` gắn cờ 18 dòng, cùng tập trang với vòng trước. Bảng cờ trong `storyboard.md` đã cập nhật (E00, E11, G06).
- Ghi chú diễn giả: mọi trang dài 40–150 từ.
- `deck_check.py` chạy trên server cổng 8799 (`http.server`, thư mục gốc là kho), 75 trang, ở hai cỡ 1600×900 và 390×844. Kết quả: 0 lỗi hoặc cảnh báo console, 0 `.katex-error`, 0 yêu cầu ra ngoài, không cuộn ngang. Sáu trang tiêu đề mạch đủ.
- `ovf2.py` (cổng 8799) đo tràn khung:
  - Lượt đầu phát hiện D03 tràn dọc 34 px, do dòng dữ kiện xuống hai hàng. Đã rút gọn dòng này.
  - Lượt đo lại: 0 trang tràn; trang cao nhất là B09 với 699 px.
- Đã xem ảnh 1600×900 của A07, A03, B06, D03, E00, E11, F07, F08, F10, G06, G07, G02 (`scratchpad/ed06/shots/m-r3-*.png`).
- `git diff --check` sạch.

### Quyết định của điều phối viên (2026-10-12, giai đoạn II, deck)

- Tác tử: biên tập viên (general-purpose, claude-opus-5-5, high) hai vòng; rà lại toán và rà lại mạch (general-purpose, claude-opus-5-5, high, chỉ đọc); điều phối viên Claude Fable 5.1 (medium).
- Kiểm độc lập của điều phối viên sau vòng 2: `density.py` 18 cờ, tất cả có lý do trong bảng cờ của `storyboard.md`, không trang nội dung vượt 60; Playwright 1600×900 và 390×844: 75 trang, 0 lỗi console, 0 `.katex-error`, 0 yêu cầu ngoài, không cuộn ngang, 6 trang tiêu đề mạch; ảnh A07, D03, E02, F13, G02 xem trực tiếp; tính lại bảng Q-learning E02; đối chiếu Định nghĩa 04.22 cho phát hiện A07; `git diff --check` sạch.
- Quyết định: **chấp nhận** bản deck sau vòng 2; từ chối TOAN D05 được chấp thuận. Hai điểm thuộc CSS chung (cỡ `p.strand-keys` 0,72em; chân trang ẩn ở mạch mở đầu) chuyển sang đợt đồng bộ chéo. Commit `fix(lecture-06)` kèm `lecture-slide.css` (ba quy tắc dùng chung: bảng 0,94em, KaTeX trong tiêu đề không viết hoa, `ol[type="a"]`).
