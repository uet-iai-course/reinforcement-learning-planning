# Nhật ký rà soát Bài 04

## Triển khai lại theo dàn bài — 24-09-2026

**Trạng thái:** đang thực hiện bảy phần theo dàn bài 45 slide/120 phút. Mỗi phần được kiểm tra rồi commit và push theo ủy quyền của người dùng. Chưa coi toàn bài là hoàn tất trước khi đủ năm báo cáo độc lập và kiểm định toàn bộ bản cuối. Các mục lịch sử phía dưới thuộc những phiên bản trước.

**Yêu cầu mới về số liệu:** người dùng yêu cầu số trong ví dụ dễ phân biệt. Mô hình hai trạng thái giữ cấu trúc nguồn, đổi phần thưởng thành 2/−1/5/10 và hệ số chiết khấu 0,5. Các cặp giá trị chính sách là (4,7), (4,20), (9,20); lưới dùng thưởng −1/24, cùng hệ số. Ví dụ hội tụ dùng chặn đầu 64; các câu hỏi sai số dùng phần dư 0,15 hoặc 0,1 và ngưỡng sai số 0,2. Số được gắn với vai trò đại lượng; các bằng nhau có lý do toán học vẫn giữ nguyên. Tham số gốc PDF chỉ dùng để truy nguyên nguồn.

**Giao diện:** yêu cầu gọi tên lecture-style.css được đối chiếu với kho và AGENTS.md; tệp chung thực tế là lecture-slide.css. Dùng lớp reveal lecture-deck, không tạo bản sao CSS hay hệ giao diện mới. Các kiểu cục bộ của bài cũ được loại bỏ khi lắp bản mới.

**Điều phối:** tác tử lập kế hoạch và tác tử phân tích nguồn chạy qua OpenRouter; writer chỉ được ghi một sản phẩm trong thư mục tạm của từng phần. GPT-6-astra, reasoning ultra, được giao điều phối kiểm định kỹ thuật và trình duyệt. Điều phối viên chính đối chiếu dữ kiện, xét từng góp ý và kiểm tra bản ghép. Các reviewer nội dung vẫn dùng cầu nối OpenRouter theo AGENTS.md.

**Kế hoạch được chấp nhận có điều chỉnh:** viết và kiểm từng phần theo thứ tự1–7; rà các phần đã thay bằng các vai phù hợp, kiểm hình và toán trước mỗi commit. Khi đủ bản nháp45 slide, chạy kiểm định storyboard và đủ năm vai độc lập trên phạm vi toàn bài; giao writer chỉnh sửa riêng rồi rà lại phần bị ảnh hưởng. Bản trung gian giữ nội dung các phần chưa viết lại, không dùng trang giữ chỗ. Những bản trung gian chưa phải sản phẩm cuối đã qua toàn bộ kiểm định.

**Kiểm soát chất lượng tác tử:** planner diễn đạt nhầm “lỗi slide10,11”; thực tế lỗi cũ là gọi cặp giá trị(10,11) tối ưu. Hai lượt reader về bố cục lẫn nhiều ngôn ngữ, không được chép vào sản phẩm. Điều phối viên biên tập lại đủ45 quyết định bố cục bằng tiếng Việt trong storyboard. Bản writer mở đầu đầu tiên có chữ SVG quá nhỏ, công thức bên trong SVG và nội dung lặp; đã yêu cầu soạn lại, đồng thời áp dụng bộ số mới.

**Kiểm số độc lập:** đã tính bằng phân số chính xác cả bốn chính sách của MDP hai trạng thái, chuỗi cải thiện, bảng q tối ưu, ba lượt đánh giá, năm lượt lưới, ví dụ co và ngưỡng sai số. Reviewer DeepSeek đề nghị sai rằng q tối ưu(s0,a)=4; bác bỏ vì phải dùng phần tiếp diễn tối ưu9, nên 2+0,5×9=6,5. Giá trị4 thuộc chính sách luôn a. Góp ý này cho thấy cần gắn nhãn phần tiếp diễn trên mặt slide, không sửa số đúng theo kết luận sai của tác tử.

**Công cụ:** Codex Slides khả dụng tại http://127.0.0.1:4311/project/20260824154346-chuy-n-lecture-4-gi-i-mdp-b-ng-quy-ho-ch-z4es. Trạng thái hiện tại mới là hồ sơ tiếp nhận, chưa là bản deck đồng bộ. Phiên không có công cụ Browser trong trình biên tập; Playwright dùng để kiểm giao diện cục bộ, không tuyên bố đã mở trong Browser của Codex. Máy chủ RevealJS chạy bằng python3 -m reloadserver 8765. Hướng dẫn bố cục tham khảo từ [SLIDE_STYLE_GUIDE.md](https://github.com/uet-iai-course/machine-learning/blob/main/SLIDE_STYLE_GUIDE.md), chỉ lấy nguyên tắc trình bày; không sao chép CSS hoặc tài sản.

### Tiến độ từng phần

| Phần | Slide | Trạng thái | Commit |
|---|---|---|---|
| 1 | 01–05 | Đã kiểm nội dung, số học và hai khung hiển thị | `ae1cc0a` |
| 2 | 06–12 | Đã kiểm nội dung và hai khung hiển thị | `dfb5d73` |
| 3 | 13–18 | Đã kiểm nội dung và hai khung hiển thị | `8d0dd23` |
| 4 | 19–26 | Đã kiểm nội dung và hai khung hiển thị | `1dcb88d` |
| 5 | 27–34 | Đã kiểm nội dung và hai khung hiển thị | Commit lặp giá trị trong lịch sử Git |
| 6 | 35–41 | Chưa triển khai | — |
| 7 | 42–45 | Chưa triển khai | — |

### Bằng chứng runtime của lượt triển khai

| Tác vụ | requested_model | observed_model | provider | Quyết định |
|---|---|---|---|---|
| Planner | `deepseek/deepseek-v4-flash-0731` | `deepseek/deepseek-v4-flash-0731` | OpenRouter | Chấp nhận kế hoạch sau sửa phạm vi và cách hiểu số |
| Reader bố cục lần1 | `deepseek/deepseek-v4-flash-0731` | `deepseek/deepseek-v4-flash-0731` | OpenRouter | Không dùng nguyên văn do lẫn ngôn ngữ |
| Reader bố cục lần2 | `deepseek/deepseek-v4-flash-0731` | `deepseek/deepseek-v4-flash-0731` | OpenRouter | Vẫn không đạt ngôn ngữ; điều phối viên biên tập lại |
| Writer mở đầu lần1 | `z-ai/glm-5.3-flash` | `z-ai/glm-5.3-flash` | OpenRouter | Yêu cầu viết lại bố cục và đổi tham số |
| Rà storyboard | `z-ai/glm-5.3-flash` | `z-ai/glm-5.3-flash` | OpenRouter | Báo cáo chỉ còn phần tiếp sau giới hạn token; chưa tính là hoàn tất |
| Rà bộ số mới | `deepseek/deepseek-v4-flash-0731` | `deepseek/deepseek-v4-flash-0731` | OpenRouter | Giữ các tính đúng, bác bỏ nhầm chính sách tiếp diễn |


### Rà phần mở đầu và storyboard triển khai

- Writer lần hai và patch: requested/observed `z-ai/glm-5.3-flash`, provider OpenRouter. Bộ số mới được áp dụng; bỏ hình lặp ở trang đầu, đưa câu hỏi trước các fragment đáp án, sửa nhãn giá trị tiếp diễn.
- Rà sinh viên: requested/observed `z-ai/glm-5.3-flash`; rà toán: requested/observed `deepseek/deepseek-v4-flash-0731`; provider OpenRouter. Hai báo cáo xác nhận phép tính 4, 9 và 2,5. Chấp nhận đề nghị gắn giá trị (4,7) với chính sách luôn chọn a. Bác bỏ đề nghị tách đáp án thành slide riêng: đáp án đã là fragment, kiểm trình duyệt xác nhận câu hỏi hiện trước. Sáu mục nội dung sau phần mở đầu tạo đúng bảy phần, không thiếu mục. Thưởng và chuyển trạng thái là hai dữ kiện mô hình; bảng v là đầu vào riêng, cách hỏi không sai. Biên tập câu phân vai bốn số thành lời giảng trực tiếp.
- Reviewer storyboard lần thu gọn: requested/observed `z-ai/glm-5.3-flash`, provider OpenRouter. Chấp nhận sửa số27 tồn dư tại ghi chú bố cục S21 thành giá trị20. Bác bỏ nhầm “thưởng24” thành “24 ô”: lưới vẫn năm ô. Chặn đầu64 là giả định minh họa đã ghi rõ, không phải chặn tự nhiên của MDP; giữ ví dụ để tính được mốc7 lượt.
- Kiểm kỹ thuật và quan sát đủ năm trang: không tràn, chồng lấn, hỏng tài nguyên, lỗi KaTeX hoặc yêu cầu mạng ngoài ở1280×720 và960×540. Bàn phím và cửa sổ ghi chú hoạt động. Sửa ngắt dòng tách số7 khỏi nhãn. SVG hai trạng thái có mô tả, nhãn và chiều mũi tên đúng. Bảng S04 cỡ30,24px và dòng học phần27,55px đọc được trong ảnh đã xem; không dùng chữ nhỏ hơn0,65em.
- Phần còn lại trong commit này giữ bản trung gian; các số cũ ở phần chưa triển khai chưa được coi là bản cuối đồng bộ.

### Rà phần Bellman tối ưu

- Writer đã được gọi lại để sửa sơ đồ: cả hai hành động phải dùng cùng quy ước phần tiếp diễn. Bỏ văn bản quy trình soạn thảo, rút chữ trên mặt, đặt công thức dài toàn chiều ngang. Bổ sung điều kiện số trạng thái/hành động hữu hạn, thưởng bị chặn và hệ số chiết khấu trong [0,1).
- Writer và reviewer sinh viên: requested/observed `z-ai/glm-5.3-flash`; reviewer toán: requested/observed `deepseek/deepseek-v4-flash-0731`; provider OpenRouter. Hai vai xác nhận bảng Q, phép cực đại, định nghĩa và điểm bất động đúng. Reviewer toán tự gắn nhãn lỗi rồi xác nhận phép tính đúng; đề nghị “sửa” từ thành chính từ ấy không có hiệu lực. Giữ phép tính đã kiểm độc lập.
- Gợi ý nhắc lại gamma và nghiệm tối ưu ở định nghĩa được cân nhắc: gamma đã xuất hiện ở mô hình và phép tính, nghiệm được xây dựng ở phần lặp chính sách; không thêm kết quả sớm làm mất nhu cầu tính. Câu kiểm tra ngay sau hai toán tử phân biệt một lần cập nhật với điểm bất động.
- Đã xem đủ bảy trang mới và biên phần mở đầu; hai viewport không tràn, chồng lấn, lỗi công thức hoặc tài nguyên. S11 hai công thức vừa hai thẻ; bảng chữ30,24px đọc được. S05 rút nhãn để hết dấu hai chấm lẻ. Chưa thay CSS chung.

### Rà phần đánh giá chính sách

- Writer và reviewer sinh viên: requested/observed `z-ai/glm-5.3-flash`; reviewer toán: requested/observed `deepseek/deepseek-v4-flash-0731`; provider OpenRouter. Xác nhận hệ cho (4,7), các lượt (2,5) rồi (3,6), cập nhật tại chỗ (2,6), câu hỏi (3,5;6,5). Các tiêu đề “lỗi” trong báo cáo toán đều tự xác nhận công thức đúng, không có sửa toán bắt buộc.
- Chấp nhận làm rõ trạng thái kết thúc giữ giá trị0 và định nghĩa n,m trong chi phí. Thay bố cục ba cột thuật toán bằng bốn bước toàn chiều ngang; tách từng phương trình đáp án để không ngắt sau dấu nhân. Hình chỉ giữ hai cạnh a để tập trung vào chính sách cố định.
- Kiểm sáu trang mới cùng biên hai trang trước ở1280×720 và960×540: không lỗi kỹ thuật. Sau chỉnh ngắt dòng, kiểm lại14–18; không tràn/chồng/KaTeX/tài nguyên; đã xem lại16–18. Phép tính tại chỗ dùng chữ thân bài; chú thích điều kiện hội tụ vẫn đọc được.

### Rà phần lặp chính sách

- Writer lần đầu bị lặp công cụ, đã gọi lại với thư mục mới và nhiệm vụ ghi trực tiếp; không đổi mô hình. Bản nội dung đầu có lỗi trong notes: dùng nhầm trạng thái tiếp diễn tại s0, mô tả sai chính sách mới chỉ đổi hành động một lần, sai quan hệ argmax. Điều phối viên không đưa bản đó vào HTML và yêu cầu writer viết lại với phép tính cụ thể. Các lỗi đã được sửa, cả mặt và lời giảng dùng cùng mô hình.
- Writer và reviewer sinh viên: requested/observed `z-ai/glm-5.3-flash`; reviewer toán: requested/observed `deepseek/deepseek-v4-flash-0731`; provider OpenRouter. Rà bản sửa xác nhận chuỗi (4,7)→(4,20)→(9,20), quy tắc giữ hòa, đơn điệu, chặn đuôi và cặp chính sách–giá trị trả về đúng.
- Chấp nhận góp ý ghi20 là giá trị tại s1, thêm hệ của pi2 vào notes, và kiểm hành động a tại pi2 cho6,5/9,5 thấp hơn b cho9/20. Không nhồi các lời cảnh báo lặp vào mặt thuật toán; bước trả đã gắn đúng pi và v của nó, notes giải thích rõ.
- Đã xem tám trang, kiểm hai viewport; công thức, bảng, quy trình bốn bước không tràn/chồng hay ngắt bất thường, không lỗi tài nguyên/KaTeX/bàn phím. Bổ sung sau rà chỉ nằm trong lời giảng, không đổi bố cục hay thứ tự.

### Rà phần lặp giá trị

- Writer và reviewer sinh viên: requested/observed `z-ai/glm-5.3-flash`; reviewer toán: requested/observed `deepseek/deepseek-v4-flash-0731`; provider OpenRouter. Bảng lưới qua bốn cập nhật và lượt kiểm thứ5 đã tính bằng phân số; khớp các báo cáo rà.
- Điều phối viên thay đường dẫn lưu đồ không tồn tại do writer tự thêm bằng bốn bước HTML đầy đủ. Sửa caption mô tả mũi tên/viền không có, sửa số thập phân chưa đặt trong công thức và nhắc câu hỏi trước đáp án.
- Chấp nhận giải thích bước c1 nhận ảnh hưởng đích: −1+0,5×4,5=1,25; ghi rõ v5=v4. Bác bỏ phép tính minh họa sai của reviewer rằng đi trái tại c1 đọc4,5: đi trái tự khép đọc1,25, cho−0,375; đi phải cho1,25. Bổ sung phần dư của v3 bằng3 và làm rõ giá trị0 ở lượt đầu thuộc bảng v0.
- Đã xem tám trang và SVG lưới mới; hai viewport không có lỗi kỹ thuật. Rút cụm lặp ở S32 để nhãn v1 không xuống dòng riêng; giữ font và CSS chung. Mỗi phần thưởng, trạng thái và lượt được gắn nhãn nhất quán.

## Lập dàn bài theo skill — 23-09-2026

**Trạng thái hiện tại:** đã hoàn tất kế hoạch 45 slide, 120 phút, bảy phần và bảy slide kiểm tra. Đây là kết quả lập dàn bài theo yêu cầu mới, chưa triển khai các mã L04-S01–L04-S45 vào HTML. Các nhận định về 42 trang, SVG và kiểm định trình duyệt ở phần lịch sử bên dưới thuộc những lần triển khai trước, không phải bằng chứng cho dàn bài mới.

Đầu ra lần này: [analysis.md](analysis.md), [outline.md](outline.md), [storyboard.md](storyboard.md) và nhật ký này. HTML, SVG, CSS, chỉ mục, lecture note và note-for-author giữ trạng thái cũ; chưa đồng bộ và chưa kiểm định hiển thị theo dàn bài mới.

### Kế hoạch và phân công được chấp nhận

1. Điều phối viên xác định đúng nguồn lecture04-solving-MDP.pdf, đọc 38 trang và học liệu liên quan, kiểm các tài sản và mẫu có sẵn.
2. Reader lập kế hoạch riêng; điều phối viên chốt phạm vi năm 3, 45 slide/120 phút, bảy phần, câu kiểm tra từng phần và không triển khai HTML.
3. Reader thứ hai phân tích nguồn/ánh xạ; điều phối viên đối chiếu PDF, sửa các suy diễn sai trước khi dùng. Phân tích thô có đoạn không thuần Việt, đề nghị 140 phút và nhận xét chặn sai số chưa đúng; những điểm này không được tiếp nhận. Quy mô cuối theo yêu cầu 120 phút.
4. Writer nhận phần giới hạn slide 13–26 trong thư mục tạm riêng. Điều phối viên ghép với các phần còn lại, sửa mã giữ chỗ, công thức lỗi, ký hiệu, mô tả lượt quét và chặn đuôi chứng minh. Worker không sửa HTML hoặc tệp chung.
5. Năm reviewer chạy trong các tiến trình độc lập; điều phối viên hợp nhất, tự tính lại và quyết định từng góp ý. Rà lại hai cụm thuật toán và chứng minh sau sửa; điều phối viên kiểm các biên và các thay đổi câu chữ cuối.

Dùng build-slide-deck-outline cho cấu trúc phân tích/dàn bài, quill cho quan hệ khái niệm và no-ai-slop cho biên tập. Không tạo quill.json. Đối chiếu hai nguồn đại học chính thức và phạm vi đã đọc được ghi trong analysis; không dùng danh tiếng trường thay cho kiểm chứng toán học.

### Bằng chứng runtime

Các trường sau được lấy từ JSON của cầu nối; không dùng lời tự khai của worker. Chỉ có OpenRouter là nhà cung cấp trong các lượt thành công.

| Vai/lượt | requested_model | observed_model | provider |
|---|---|---|---|
| Lập kế hoạch | `deepseek/deepseek-v4-flash-0731` | `deepseek/deepseek-v4-flash-0731` | OpenRouter |
| Phân tích nguồn | `deepseek/deepseek-v4-flash-0731` | `deepseek/deepseek-v4-flash-0731` | OpenRouter |
| Soạn slide 13–26 | `z-ai/glm-5.3-flash` | `z-ai/glm-5.3-flash` | OpenRouter |
| Góc nhìn sinh viên | `z-ai/glm-5.3-flash` | `z-ai/glm-5.3-flash` | OpenRouter |
| Chuyên gia Học tăng cường | `deepseek/deepseek-v4-flash-0731` | `deepseek/deepseek-v4-flash-0731` | OpenRouter |
| Toán học và thuật toán | `deepseek/deepseek-v4-flash-0731` | `deepseek/deepseek-v4-flash-0731` | OpenRouter |
| Phản biện giảng dạy | `deepseek/deepseek-v4-flash-0731` | `deepseek/deepseek-v4-flash-0731` | OpenRouter |
| Kết nối và mạch viết | `z-ai/glm-5.3-flash` | `z-ai/glm-5.3-flash` | OpenRouter |
| Rà lại thuật toán 14–26 | `deepseek/deepseek-v4-flash-0731` | `deepseek/deepseek-v4-flash-0731` | OpenRouter |
| Rà lại chứng minh 33–45 | `deepseek/deepseek-v4-flash-0731` | `deepseek/deepseek-v4-flash-0731` | OpenRouter |

Reader có lượt đầu chạm giới hạn công cụ; đã thu hẹp gói và dùng cùng mô hình. Hai vai sinh viên/mạch viết ban đầu hết ngân sách sinh 2.500 token mà chưa có báo cáo; gói sau rút bớt trường không liên quan, vẫn bao phủ 45 slide cùng bản đồ bảy phần, dùng hồ sơ review-full và ngân sách 5.000 token. Endpoint GLM từ chối tham số reasoning=none; đã dùng low, không đổi mô hình. Không tính lượt lỗi tham số hay gói thiếu nội dung là một báo cáo hợp lệ.

Gói rà chứng minh ban đầu vượt 16.000 ký tự khi tính cả chỉ dẫn cầu nối, chưa gửi API; rút gọn một lần, cùng mô hình, thành công với 15.878 ký tự toàn ngữ cảnh. Không tăng timeout hoặc chuyển nhà cung cấp. Các lời gọi mạng dựa trên ủy quyền sẵn tại AGENTS.md; lần kiểm duyệt đầu được giải quyết bằng cách cung cấp đúng điều khoản ủy quyền. Không có phần nào còn chờ quyền.

### Quyết định sau năm báo cáo độc lập

| Vai | Mức reviewer nêu | Slide | Bằng chứng/vấn đề | Quyết định cuối |
|---|---|---|---|---|
| Sinh viên, RL | Trung bình | 16,24,31 | Hai quy trình trả bảng khác nhau, PI chưa rõ khi hết ngân sách | Giữ hai quy ước hợp lệ với chặn đúng bảng; giải thích lý do ở 16/39. Slide 24 trả chính sách vừa đánh giá cùng giá trị của nó; 31 ghi cả hai nhánh trả trong nội dung. Không ép hai thuật toán giống nhau. |
| Sinh viên | Nhẹ | 19 | “Theo chính sách cũ” dễ lẫn với cách chạy chính sách mới | Làm rõ đó là giả định trong phép tính giá trị hành động một bước; chính sách mới được đánh giá riêng. |
| Sinh viên, mạch viết | Nhẹ | 13–18 | Viết hoa đầu câu không nhất quán | Biên tập các trường nội dung; giữ cấu trúc dàn bài. |
| Sinh viên | Nhẹ | 44 | Reviewer không có toàn văn bài tập để kiểm tham chiếu | Điều phối viên đối chiếu hw3.pdf: B3 tồn tại, B6 hệ Bellman, B7 đơn điệu, B9 MDP ba trạng thái ở tr.1–2. |
| RL, giảng dạy | Trung bình | 16 | Chặn sai số xuất hiện sớm, thuật toán nhiều ý | Chuyển công thức chặn sang ghi chú/slide 39; định nghĩa thay đổi lớn nhất bằng lời; không lặp lại giải hệ trên mặt slide. |
| RL | Nhẹ | 17 | Điều kiện cập nhật công bằng chưa đủ đặc tả | Bổ sung mỗi cập nhật dùng đúng công thức Bellman theo bảng hiện có, dưới giả thiết chiết khấu. |
| RL, giảng dạy | Nhẹ/nghiêm trọng | 22–23 | Tính đơn điệu và lý do giá trị bị chặn chưa được chuẩn bị | Slide 22 mở bước trọng số không âm; 23 dùng chặn Rmax/(1−gamma) cho đuôi. |
| RL, giảng dạy | Nhẹ/nghiêm trọng | 37 | Chứng minh mọi chính sách trong 4 phút quá dày; cần điều kiện hóa đúng lịch sử | Giữ phát biểu tối ưu đầy đủ, chỉ giảng sơ đồ hai nhánh. Chứng minh theo lịch sử nằm trong ghi chú đọc thêm, điều kiện hóa theo H_t. Không thu hẹp định lý một cách ngầm định. |
| Toán | Nghiêm trọng | 35,38,43 | Reviewer tính lại các số đều đúng nhưng muốn có phép tính mẫu | Xếp lại thành yêu cầu giải thích, không là lỗi số học. Thêm phép tính mẫu và bước logarit trong ghi chú; giữ số đúng. |
| Toán | Trung bình | 39 | Thiếu bước tam giác trong suy diễn | Bổ sung đầy đủ tam giác → co → chặn. |
| Toán | Nhẹ | 31 | Thứ tự Q, max/argmax, phần dư chưa rõ | Viết rõ trình tự, cùng bảng v cho toàn bộ phép tính. |
| Toán, RL, giảng dạy | Nhẹ/trung bình | 40 | Chưa chỉ rõ biến nào 3 khoảng, biến nào 6 | Đối chiếu trực tiếp NG1 tr.36; ghi x và vận tốc mỗi biến 3, góc và vận tốc góc mỗi biến 6. Giữ cảnh báo gộp trạng thái chưa bảo đảm Markov, thêm đặc tả hình gộp hai điểm. |
| Giảng dạy | Trung bình | 38 | Chặn 100 có thể bị nhầm là dữ kiện của lưới | Ghi ngay trong nội dung đây là giả định minh họa số học; 44 là số lượt đủ theo chặn. |
| Giảng dạy | Nhẹ | 44 | Sản phẩm chứng minh chưa rõ | Yêu cầu viết bằng lời của mình, nêu giả thiết và bước dùng từng giả thiết. |
| Mạch viết | Trung bình | 06–12 | Báo cáo cộng sai thành 15 phút và toàn bài 117 | Bác bỏ: 2+3+3+3+2+2+3=18; kiểm bằng mã cho toàn bài 120. Không tăng thời gian để sửa một phát hiện sai. |
| Mạch viết | Nhẹ | 23 | Cách viết chỉ số chính sách cải thiện | Chuẩn hóa ký hiệu prime trong nguồn Markdown; không đổi ý nghĩa. |

### Kết quả rà lại và kiểm định cuối của điều phối viên

- Rà lại 14–26 xác nhận đơn điệu, chặn đuôi và cặp trả của PI; tuy nhiên báo cáo nhầm cạnh s1,a quay về s1. Đề nghị đổi v2(s1) từ 2,9 thành 3,8 là sai. Nguồn tr.17 ghi s1,a → thưởng 2, trạng thái s0; vì vậy v2(s1)=2+0,9×1=2,9 và v3(s1)=2+0,9×1,9=3,71. Bác bỏ sửa số; đã tính độc lập bằng phân số chính xác. Thứ tự cập nhật tại chỗ s0 rồi s1 đã được ghi rõ, không phải thiếu.
- Rà lại 33–45 xác nhận phép tính co, số 44, chặn phần dư, 324 ô, bảng Q tối ưu và chứng minh theo lịch sử; không còn đề nghị sửa có căn cứ. Một số hàng báo cáo gắn nhãn “trung bình” rồi tự xác nhận “đúng”; không coi đó là lỗi còn mở.
- Kiểm 45 mã duy nhất và liên tục; tổng 120 phút; phân bổ 10/18/17/23/23/20/9; đủ bảy slide kiểm tra có đáp án và tiêu chí; hỏi–chữa đã nằm trong thời lượng.
- Ánh xạ đủ trang nguồn 1–38. Liên kết cục bộ trong ba tệp kế hoạch đều tồn tại. Không có ký tự điều khiển hoặc dấu công thức Markdown sai quy ước.
- Tính lại bằng phân số: ba chính sách, bảng giá trị hành động, ba lượt đánh giá, năm bảng lưới gồm lượt kiểm điểm bất động, ví dụ co, hai ngưỡng sai số. Kết quả khớp dàn bài.
- 567 biểu thức trong analysis/outline/storyboard được bộ phân tích KaTeX cục bộ chấp nhận, không lỗi. Đây là kiểm cú pháp, không thay cho kiểm toán học hoặc kiểm hiển thị.
- Rà chu trình và ranh giới theo quill: tiên quyết xuất hiện trước thuật toán; ví dụ truyền cùng dữ kiện sang công thức; kết luận giải đúng vấn đề mở đầu. Không có trang chỉ để trang trí. Không đổi số lượng/thứ tự sau năm báo cáo; các bổ sung cuối chỉ làm rõ nội dung và ghi chú.
- Tự kiểm no-ai-slop/eval.md: giữ ý và dữ kiện nguồn, bỏ lời dẫn rỗng, dùng động từ cụ thể, phân biệt nhận định với chứng cứ; các trường lặp theo mẫu có chức năng tra cứu. Không tuyên bố kiểm định giọng nói từ bản thu âm hoặc khả năng đọc của slide chưa dựng.

**Kết luận của điều phối viên:** kế hoạch đủ điều kiện bàn giao. Không còn lỗi nội dung chặn bàn giao có căn cứ sau phân xử. Thời lượng vẫn là dự toán; cần chạy thử khi triển khai slide. HTML/note hiện có còn theo bản cũ và không được coi là đã cập nhật hoặc đã qua kiểm định cho cấu trúc này.

### Báo cáo độc lập được lưu để truy nguyên

Các báo cáo sau là đầu ra worker trước phân xử. Quyết định có hiệu lực nằm trong các bảng trên; không áp dụng máy móc những đề xuất đã bị bác bỏ.

#### Góc nhìn sinh viên

##### Báo cáo rà outline.md (L04, 45 slide / 120 phút)

Đã kiểm toàn bộ 45 slide: tổng thời lượng đúng 120 phút, khớp bản đồ phần (10+18+17+23+23+20+9=120); đủ mã L04-S01–S45. Các phép tính chính đều kiểm lại đúng: bảng $Q_v$ (S07), $T_*v=(10,12{,}9)$ (S12), nghiệm $(10,11)$ (S14), dãy quét (S15, S18), chuỗi PI $(10,11)\to(10,30)\to(27,30)$ (S21, S26), lưới 5 ô $v_1$–$v_4$ và điểm bất động (S28–S29, S34), ví dụ co $1{,}8=0{,}9\cdot2$ (S35), $100\cdot0{,}9^{44}\approx0{,}97$ và $k>43{,}71$ (S38), chặn $0{,}02/0{,}1=0{,}2$ (S41), $Q_{v_*}=(25{,}3,27;26{,}3,30)$ (S43), đáp án S45 $\le0{,}1$. Chặn $\gamma\delta/(1-\gamma)$ ở S16 và suy diễn $\rho/(1-\gamma)$ ở S39 đều đúng. Không thấy lỗi chặn bàn giao.

**Các vấn đề tìm thấy:**

1. **Trung bình | L04-S16 vs L04-S31 | Không nhất quán về bảng trả khi hết ngân sách** | Bằng chứng: S16 ghi "sau lượt thứ $K$... trả bảng $w$ cuối cùng kèm nhãn hết ngân sách"; S31 ghi "ở lượt thứ $K$, nếu chưa đạt thì trả chính bảng $v$ đã kiểm cùng $\pi_v,\rho(v)$... không âm thầm trả $w$ chưa kiểm" | Hai quy trình trả hai bảng khác nhau ($w=Tv$ vs $v$) trong cùng tình huống, dễ gây nhầm khi sinh viên đối chiếu PI/VI | Đề xuất: thống nhất một quy ước (khuyến nghị theo S31: trả bảng đã kiểm kèm phần dư đo được) và sửa ghi chú S16 cho khớp, nêu rõ lý do khác nhau nếu cố tình giữ.

2. **Nhẹ | L04-S19 | Câu "phần tiếp diễn vẫn theo $\pi_0$" dễ hiểu sai** | Bằng chứng: S19 nêu đổi hành động tại $s_1$ nhưng "phần tiếp diễn vẫn theo $\pi_0$", trong khi S20 cho ra $\pi_1=(a,b)$ là chính sách mới hoàn chỉnh | Sin viên năm 3 có thể tưởng $\pi_1$ chỉ khác $\pi_0$ tại một bước rồi quay lại $\pi_0$ | Đề xuất: sửa thành "hành động tại $s_1$ đổi sang $b$; tại $s_0$ giữ $a$, tạo chính sách mới $\pi_1=(a,b)$".

3. **Nhẹ | L04-S13–S18 | Lỗi văn phong: nhiều slide bắt đầu bằng chữ thường** | Bằng chứng: S13 "với $\pi_0=(a,a)$...", S14 "với $\pi_0$ và $\gamma=0.9$...", S15 "khởi $v_0$...", S17 "đồng bộ:...", S18 "đề:..." | Không nhất quán với S01–S12 viết hoa đầu câu; ảnh hưởng bản HTML sau này | Đề xuất: viết hoa đầu câu khi đồng bộ sang HTML.

4. **Nhẹ | L04-S44 | Tham chiếu đọc thêm chưa kiểm được** | Bằng chứng: "NG1 tr.20–24,31–34", "NG2 Bài 9/6/3/7, B10" — outline không kèm trích dẫn nội dung các nguồn | Không xác nhận được trang/bài tập khớp tài liệu thật từ excerpt được cấp | Đề xuất: đối chiếu số trang với NG1/NG2 trước khi phát tài liệu; không phải lỗi nội dung mặt slide.

**Kết luận:** Không có lỗi nghiêm trọng hay chặn bàn giao; số học, định lý và nhịp 120 phút đều nhất quán. Chỉ cần xử lý mục 1 trước khi dựng HTML.

#### Chuyên gia Học tăng cường

#### Báo cáo rà soát dàn bài Bài 04 — Giải MDP bằng quy hoạch động

##### Tổng quan

Dàn bài 45 slide/120 phút bám sát nguồn NG1 (38 trang), đúng cấu trúc Bellman → đánh giá → PI → VI → hội tụ → tổng hợp, có 7 slide kiểm tra đúng theo yêu cầu. Các giá trị số trong ví dụ hai trạng thái và lưới năm ô đều khớp với dữ kiện đã xác minh. Không phát hiện lỗi mức **chặn bàn giao** hay **nghiêm trọng**.

---

##### Vấn đề 1 — Mức độ: trung bình

**Trang chiếu:** L04-S16, L04-S24, L04-S31

**Vấn đề:** Mâu thuẫn giữa ba quy trình về cách xử lý khi hết ngân sách $K$: slide 16 trả bảng $w$ cuối cùng, slide 31 trả bảng $v$ đã kiểm, slide 24 không nói rõ trả bảng nào khi hết ngân sách.

**Bằng chứng:** S16: "sau lượt thứ K, nếu chưa đạt ngưỡng thì trả bảng w cuối cùng"; S31: "trả chính bảng v đã kiểm cùng π_v, ρ(v)"; S24: "Nếu dừng do ngân sách K, phải gắn nhãn 'chưa chứng nhận tối ưu'" — không chỉ rõ bảng trả.

**Đề xuất sửa:** Thống nhất quy ước: mọi quy trình trả bảng đã kiểm $v$ kèm phần dư $\rho(v)$ và nhãn hết ngân sách; sửa slide 16 cho đồng nhất với slide 31.

---

##### Vấn đề 2 — Mức độ: trung bình

**Trang chiếu:** L04-S16

**Vấn đề:** Chặn sai số cho bảng trả $w$ được ghi là $\gamma\delta/(1-\gamma)$ nhưng chưa giải thích vì sao hệ số có $\gamma$ ở tử số, trong khi slide 39 mới giải thích đầy đủ. Người học có thể nhầm với chặn $\rho(v)/(1-\gamma)$ của slide 39.

**Bằng chứng:** S16: "chặn sai số cho bảng trả w là γδ/(1−γ), dẫn chiếu Phần 6, không chứng minh ở đây"; S39: "Nếu dùng bản trả w=Tv như đánh giá chính sách ở slide 16, chặn của w là γ‖Tv−v‖∞/(1−γ)".

**Đề xuất sửa:** Giữ nguyên vì slide 39 đã làm rõ, nhưng nên thêm một câu ở slide 16: "hệ số γ xuất hiện vì w=T^π v đã tiến một bước gần điểm bất động hơn v" để tránh hiểu nhầm ngay từ đầu.

---

##### Vấn đề 3 — Mức độ: nhẹ

**Trang chiếu:** L04-S17

**Vấn đề:** Câu "lập luận hội tụ chỉ cần mỗi trạng thái được cập nhật vô hạn lần" chưa chính xác hoàn toàn — cần thêm điều kiện bước cập nhật phải theo toán tử $T^\pi$ đúng và thứ tự cập nhật không làm sai lệch phép tính.

**Bằng chứng:** S17: "lập luận hội tụ chỉ cần mỗi trạng thái được cập nhật vô hạn lần; điều đó không cho phép kết luận tại chỗ nhanh hơn với mọi MDP."

**Đề xuất sửa:** Bổ sung: "với điều kiện mỗi lần cập nhật dùng đúng công thức $T^\pi$ theo bảng hiện tại" để tránh hiểu lầm rằng chỉ cần cập nhật nhiều lần là đủ.

---

##### Vấn đề 4 — Mức độ: nhẹ

**Trang chiếu:** L04-S23

**Vấn đề:** Phác thảo chứng minh dùng "hạng đuôi $\gamma^n\mathbb{E}_{\pi'}[v^\pi(S_n)]$ tiến về 0" nhưng chưa nói rõ vì sao $v^\pi$ bị chặn — cần nhắc lại giả thiết $|R_t|\le R_{\max}$ từ quy ước soạn.

**Bằng chứng:** S23: "hạng đuôi γ^n E_{π'}[v^π(S_n)] tiến về 0 vì v^π bị chặn và 0≤γ<1"; quy ước soạn có "$|R_t|\le R_{\max}<\infty$".

**Đề xuất sửa:** Thêm một cụm: "v^π bị chặn bởi R_max/(1−γ) theo giả thiết phần thưởng bị chặn" để sinh viên thấy rõ nguồn của tính bị chặn.

---

##### Vấn đề 5 — Mức độ: nhẹ

**Trang chiếu:** L04-S37

**Vấn đề:** Ghi chú triển khai nói "chặn trên cho mọi chính sách, kể cả phụ thuộc lịch sử" nhưng phép lặp bất đẳng thức $\bar v(s)\ge\mathbb{E}[R_1+\gamma\bar v(S_1)]$ cần làm rõ kỳ vọng được lấy theo chính sách phụ thuộc lịch sử như thế nào — có thể gây nhầm vì $T^\pi$ chỉ định nghĩa cho chính sách Markov dừng.

**Bằng chứng:** S37: "chặn trên cho mọi chính sách, kể cả phụ thuộc lịch sử, bằng lặp bất đẳng thức... Không dùng T^π cho chính sách phụ thuộc lịch sử."

**Đề xuất sửa:** Thêm câu: "kỳ vọng ở mỗi bước được lấy theo phân phối hành động của chính sách đó tại trạng thái hiện tại, không cần dùng toán tử T^π" để phân biệt rõ hai cách dùng.

---

##### Vấn đề 6 — Mức độ: nhẹ

**Trang chiếu:** L04-S40

**Vấn đề:** Ví dụ CartPole chia $3\times3\times6\times6=324$ ô nhưng chưa nói rõ đây là số ô của biến nào (x, ẋ, θ, θ̇) — người học có thể không hiểu cách phân bổ.

**Bằng chứng:** S40: "Chia thành 3×3×6×6=324 ô tạo biểu diễn hữu hạn" — không ghi rõ biến nào 3, biến nào 6.

**Đề xuất sửa:** Ghi rõ: "ví dụ: x và ẋ mỗi biến 3 khoảng, θ và θ̇ mỗi biến 6 khoảng" hoặc bỏ con số cụ thể nếu không cần thiết cho mục tiêu MT6.

---

##### Kết luận

Không có lỗi mức chặn bàn giao hoặc nghiêm trọng. Các vấn đề chủ yếu là mâu thuẫn nhỏ giữa các slide về quy ước trả bảng khi hết ngân sách (cần thống nhất) và một số chỗ cần bổ sung giải thích ngắn để tránh hiểu nhầm. Dàn bài đạt yêu cầu về độ bao phủ nội dung, phù hợp 120 phút, giữ đúng nguồn NG1 38 trang, không yêu cầu thêm chương trình hay chủ đề mới.

#### Toán học và thuật toán

#### Báo cáo rà soát độc lập — Dàn bài Bài 04

##### Vấn đề 1
- **Mức độ:** Nghiêm trọng
- **Slide:** L04-S35
- **Vấn đề:** Ví dụ số chưa được kiểm chứng độc lập: $T_*v=(11{,}7,14{,}7)$ cần tính lại từ mô hình hai trạng thái. Với $v=(11,13)$, $T_*v(s_0)=\max\{1+0{,}9\cdot11,\ 0+0{,}9\cdot13\}=\max\{10{,}9,\ 11{,}7\}=11{,}7$ (đúng); $T_*v(s_1)=\max\{2+0{,}9\cdot11,\ 3+0{,}9\cdot13\}=\max\{11{,}9,\ 14{,}7\}=14{,}7$ (đúng). Tuy nhiên slide chưa trình bày phép tính này, khiến người học không thể tự kiểm chứng.
- **Bằng chứng:** Slide chỉ ghi kết quả "$T_*u=(10,12{,}9)$, $T_*v=(11{,}7,14{,}7)$" mà không nêu công thức tính từng ô.
- **Đề xuất sửa:** Thêm dòng tính mẫu: "$T_*v(s_0)=\max\{1+0{,}9\cdot11,\ 0+0{,}9\cdot13\}=11{,}7$; $T_*v(s_1)=\max\{2+0{,}9\cdot11,\ 3+0{,}9\cdot13\}=14{,}7$" để người học theo dõi được.

##### Vấn đề 2
- **Mức độ:** Nghiêm trọng
- **Slide:** L04-S38
- **Vấn đề:** Số lượt 44 cần kiểm chứng: $100\cdot0{,}9^{44}\approx0{,}970<1$ là đúng, nhưng slide chưa giải thích cách chọn 44 từ bất đẳng thức $\gamma^k\|v_0-v_*\|_\infty<1$. Cần nêu rõ đây là chặn đủ (sufficient bound), không phải số lượt tối thiểu thực tế.
- **Bằng chứng:** Slide ghi "cần 44 lượt để chặn nhỏ hơn 1: $100\cdot0{,}9^{44}\approx0{,}970$" nhưng không chỉ dẫn cách suy ra 44 từ logarit.
- **Đề xuất sửa:** Thêm: "Giải $100\cdot0{,}9^k<1$ cho $k>\ln(0{,}01)/\ln(0{,}9)\approx43{,}7$, nên $k=44$ là đủ. Đây là chặn lý thuyết, không phải số lượt tối thiểu thật của mọi MDP."

##### Vấn đề 3
- **Mức độ:** Nghiêm trọng
- **Slide:** L04-S43
- **Vấn đề:** Bảng $Q_{v_*}=(25{,}3,27;26{,}3,30)$ chưa được kiểm chứng đầy đủ. Tính lại: $Q_{v_*}(s_0,a)=1+0{,}9\cdot27=25{,}3$; $Q_{v_*}(s_0,b)=0+0{,}9\cdot30=27$; $Q_{v_*}(s_1,a)=2+0{,}9\cdot27=26{,}3$; $Q_{v_*}(s_1,b)=3+0{,}9\cdot30=30$. Các số đúng, nhưng slide chưa trình bày phép tính để người học tự kiểm.
- **Bằng chứng:** Slide ghi "Kiểm $Q_{v_*}=(25{,}3,27;26{,}3,30)$" mà không nêu công thức.
- **Đề xuất sửa:** Thêm dòng tính mẫu: "$Q_{v_*}(s_0,b)=0+0{,}9\cdot30=27$; $Q_{v_*}(s_1,b)=3+0{,}9\cdot30=30$" và chỉ rõ $\max$ tại mỗi trạng thái khớp với $v_*$.

##### Vấn đề 4
- **Mức độ:** Trung bình
- **Slide:** L04-S39
- **Vấn đề:** Suy diễn $e\le\rho(v)+\gamma e$ thiếu bước trung gian: cần dùng bất đẳng thức tam giác $v-v_*=(v-T_*v)+(T_*v-v_*)$ rồi áp dụng tính co cho $T_*v$ và $v_*$. Slide hiện chỉ nêu kết quả.
- **Bằng chứng:** Slide ghi "Đặt $e=\|v-v_*\|_\infty$: $e\le\rho(v)+\gamma e$, nên $e\le\rho(v)/(1-\gamma)$" — thiếu giải thích nguồn gốc.
- **Đề xuất sửa:** Thêm: "Dùng bất đẳng thức tam giác và tính co: $\|v-v_*\|\le\|v-T_*v\|+\|T_*v-v_*\|\le\rho(v)+\gamma\|v-v_*\|$."

##### Vấn đề 5
- **Mức độ:** Trung bình
- **Slide:** L04-S40
- **Vấn đề:** Chỉ số phân chia CartPole chưa rõ ràng: $3\times3\times6\times6=324$ cần ghi rõ biến nào nhận 3, biến nào nhận 6. Nếu theo thứ tự $(x,\dot x,\theta,\dot\theta)$ thì $x$:3, $\dot x$:3, $\theta$:6, $\dot\theta$:6 — cần xác nhận với nguồn NG1 tr.35–37.
- **Bằng chứng:** Slide ghi "Chia thành $3\times3\times6\times6=324$ ô" không chỉ rõ ánh xạ biến.
- **Đề xuất sửa:** Ghi cụ thể: "$x$: 3 khoảng, $\dot x$: 3, $\theta$: 6, $\dot\theta$: 6" hoặc theo đúng nguồn đã xác minh.

##### Vấn đề 6
- **Mức độ:** Nhẹ
- **Slide:** L04-S31
- **Vấn đề:** Mô tả "một lượt tính $Q_v$ phục vụ cả $w$, chính sách và phần dư" là đúng, nhưng cần làm rõ thứ tự: phải tính $Q_v$ trước, rồi mới lấy $\max$ cho $w$, $\arg\max$ cho $\pi_v$, và $\max_s|w(s)-v(s)|$ cho $\rho(v)$. Hiện tại slide liệt kê song song có thể gây hiểu nhầm là ba phép tính độc lập.
- **Bằng chứng:** Slide ghi "tính từng $Q_v$, $w=T_*v$, chính sách $\pi_v$ tham lam theo cùng $v$ và $\rho(v)$" — thứ tự chưa rõ.
- **Đề xuất sửa:** Viết lại: "Trước tiên tính $Q_v(s,a)$ cho mọi $(s,a)$; từ đó lấy $w(s)=\max_a Q_v(s,a)$, $\pi_v(s)\in\arg\max_a Q_v(s,a)$, và $\rho(v)=\max_s|w(s)-v(s)|$."

---

**Tổng kết:** Không phát hiện lỗi sai số học trong các ví dụ trọng yếu (các giá trị $(10,11),(10,30),(27,30)$, $Q_{v_*}$, $T_*v$ đều tính lại đúng). Các vấn đề chủ yếu là thiếu trình bày phép tính kiểm chứng và thiếu bước trung gian trong suy diễn, ảnh hưởng đến khả năng tự học của sinh viên hơn là sai nội dung.

#### Phản biện giảng dạy

#### Báo cáo phản biện dàn bài Bài 04 (45 slide/120 phút)

##### Tổng quan
Dàn bài có cấu trúc chặt chẽ, mạch ví dụ–hình thức–thuật toán hợp lý, bám sát nguồn NG1 38 trang. Các công thức kiểm tra đều đúng. Tuy nhiên có một số vấn đề về thứ tự trình bày, tính khả thi chứng minh trên lớp và nhất quán dữ kiện.

---

##### Vấn đề 1 — Nghiêm trọng
**Trang chiếu:** L04-S23 (Định lý cải thiện chính sách)

**Vấn đề:** Chứng minh phác thảo dùng chuỗi bất đẳng thức `v^π ≤ T^π' v^π ≤ (T^π')²v^π ≤ ...` nhưng không giải thích vì sao `T^π'` đơn điệu — đây là bước cần chứng minh phụ, chưa được chuẩn bị ở slide nào trước đó.

**Bằng chứng:** "dùng đơn điệu (trọng số không âm) lặp khai triển" — không có slide nào giới thiệu tính đơn điệu của toán tử Bellman trước slide 23.

**Đề xuất sửa:** Thêm 1–2 câu ở slide 22 hoặc đầu slide 23 chứng minh nhanh: nếu `u ≤ v` theo từng tọa độ thì `T^π'u ≤ T^π'v` vì trọng số xác suất không âm; hoặc chuyển bước này thành câu hỏi kiểm tra nhanh.

---

##### Vấn đề 2 — Nghiêm trọng
**Trang chiếu:** L04-S37 (Điểm bất động và chính sách tối ưu)

**Vấn đề:** Phác thảo chứng minh "chặn trên cho mọi chính sách, kể cả phụ thuộc lịch sử" bằng lặp bất đẳng thức `v̄(s) ≥ E[R₁ + γv̄(S₁)]` là không tầm thường: cần lập luận quy nạp qua các bước thời gian và xử lý chính sách phụ thuộc lịch sử — khối lượng này quá lớn cho 4 phút trên lớp, đặc biệt khi sinh viên chưa quen kỹ thuật này.

**Bằng chứng:** "chặn trên cho mọi chính sách, kể cả phụ thuộc lịch sử, bằng lặp bất đẳng thức... sau n bước, hạng đuôi bị chặn bởi γⁿ‖v̄‖∞→0" — toàn bộ nằm trong ghi chú triển khai, không có slide minh họa.

**Đề xuất sửa:** Giới hạn phát biểu ở lớp chính sách Markov dừng (đã dùng trong `T^π`), nêu rõ trường hợp phụ thuộc lịch sử là mở rộng đọc thêm; hoặc tăng thời lượng slide này lên 5–6 phút và thêm một slide phụ minh họa bước quy nạp.

---

##### Vấn đề 3 — Trung bình
**Trang chiếu:** L04-S16 (Quy trình đánh giá chính sách)

**Vấn đề:** Slide đưa cùng lúc quá nhiều khái niệm mới: ngưỡng θ, chuẩn vô cùng, chặn sai số `γδ/(1-γ)` (dẫn chiếu Phần 6), ngân sách K, nhãn "hết ngân sách" — trong 4 phút. Sinh viên chưa học chuẩn vô cùng (chỉ mới thấy ở slide 35) và chưa hiểu vì sao chặn sai số lại có dạng đó.

**Bằng chứng:** "Ngưỡng chỉ trả ước lượng; chặn sai số cho bảng trả w là γδ/(1-γ), dẫn chiếu Phần 6, không chứng minh ở đây" — nêu nhưng không giải thích trực giác.

**Đề xuất sửa:** Tách thành hai slide: (a) quy trình lặp với ngưỡng θ và chuẩn vô cùng (định nghĩa nhanh); (b) ngân sách K và ý nghĩa "chưa chứng nhận". Chuyển chặn sai số thành ghi chú "sẽ giải thích ở Phần 6", không nêu công thức.

---

##### Vấn đề 4 — Trung bình
**Trang chiếu:** L04-S38 (Hội tụ hình học)

**Vấn đề:** Ví dụ "chặn sai số đầu bằng 100, γ=0.9, cần 44 lượt" là con số giả định không gắn với bất kỳ ví dụ nào trong bài — sinh viên khó hình dung vì sao chọn 100, và con số 44 có thể bị hiểu nhầm là số lượt thực tế cần cho ví dụ lưới ở Phần 5.

**Bằng chứng:** "Với chặn sai số đầu bằng 100 và γ=0.9, cần 44 lượt để chặn nhỏ hơn 1: 100·0.9⁴⁴≈0.970" — không có nguồn gốc từ ví dụ cụ thể nào.

**Đề xuất sửa:** Dùng chặn sai số đầu từ ví dụ lưới (‖v₀-v_*‖∞ ≤ 10 chẳng hạn) hoặc nêu rõ "đây là minh họa số học cho công thức, không phải dự đoán số lượt thực tế" ngay trên slide, không chỉ trong ghi chú.

---

##### Vấn đề 5 — Trung bình
**Trang chiếu:** L04-S40 (Giới hạn mô hình dạng bảng)

**Vấn đề:** Slide nói "chia thành 3×3×6×6=324 ô" nhưng không giải thích vì sao chọn số ô này, và quan trọng hơn — không nêu rõ rằng việc rời rạc hóa có thể phá vỡ tính Markov (trạng thái gộp không còn đủ thông tin). Ghi chú có nhắc nhưng mặt slide chỉ có sơ đồ.

**Bằng chứng:** "chưa cung cấp hạt nhân chuyển/phần thưởng hay bảo đảm tính Markov của trạng thái gộp" — nằm trong luận điểm nhưng không có hình minh họa cụ thể về việc mất tính Markov.

**Đề xuất sửa:** Thêm một ví dụ nhỏ: hai trạng thái liên tục khác nhau (vận tốc khác nhau) rơi vào cùng một ô nhưng hành vi tương lai khác nhau — minh họa trực quan việc mất tính Markov.

---

##### Vấn đề 6 — Nhẹ
**Trang chiếu:** L04-S44 (Bài tập và tài liệu đọc)

**Vấn đề:** Giao "Bài 3/7: hoàn thiện chứng minh tồn tại/đơn điệu" từ NG2 nhưng không nêu rõ sản phẩm cần nộp là gì (điền vào chỗ trống? viết lại chứng minh?); trong khi hai bài kia (B9, B6) có sản phẩm rõ ràng. Sinh viên có thể không biết mức độ hoàn thiện được kỳ vọng.

**Bằng chứng:** "Bài 3/7: hoàn thiện chứng minh tồn tại/đơn điệu" — không có mô tả sản phẩm cụ thể như hai bài còn lại.

**Đề xuất sửa:** Ghi rõ sản phẩm: "viết lại chứng minh bằng ngôn ngữ của mình, chỉ rõ chỗ dùng giả thiết γ<1" hoặc chuyển thành bài tự đọc không chấm điểm.

---

##### Kết luận
Không có lỗi sai công thức hay dữ kiện. Các vấn đề chính thuộc về thứ tự trình bày (đơn điệu chưa được chuẩn bị trước slide 23), tải nhận thức quá lớn ở một số slide (16, 37), và thiếu trực giác cho các con số minh họa (38, 40). Cấu trúc 7 phần, 7 slide kiểm tra, mạch ví dụ–hình thức–thuật toán là hợp lý và khả thi nếu điều chỉnh các điểm trên.

#### Kết nối và mạch viết

##### Báo cáo rà dàn bài L04 (outline.md)

Đã đối chiếu toàn bộ 45 slide, bản đồ 7 phần, các con số tính tay (S04, S07, S12, S14–S18, S21, S26, S28–S29, S34–S35, S38, S41, S43, S45) — tất cả đúng. Không thấy lỗi chặn bàn giao. Các vấn đề thực sự tìm được:

**1. trung bình | Bản đồ phần 2 | Tổng thời lượng phần 2 không khớp |** Bảng bản đồ ghi Phần 2 = 18 phút, nhưng các slide S06–S12 cộng lại: 2+3+3+2+2+2+3 = 15 phút (S06:2, S07:3, S08:3, S09:3, S10:2, S11:2, S12:3). Tổng toàn bài cũng chỉ đạt 117 phút, không phải 120 như tiêu đề. | **Đề xuất:** tăng thời lượng một slide ở phần 2 (ví dụ S08 hoặc S12 lên 5 phút) hoặc sửa bản đồ thành 15 phút và tổng thành 117, nêu rõ phần dư 3 phút dùng cho buffer.

**2. trung bình | L04-S31 | Thiếu đặc tả nhánh trả khi hết ngân sách |** Mục "Hình/ví dụ" nêu "lưu đồ có hai nhánh trả: đạt ngưỡng; hết ngân sách", nhưng phần "Luận điểm và nội dung" chỉ mô tả nhánh đạt ngưỡng ("Nếu ρ(v)≤θ, trả v,π_v,ρ(v)") và nhánh "đặt v←w"; không nói trả gì, kèm nhãn gì khi hết K lượt. Trong khi S16 đã đặc tả rõ nhánh tương tự ("trả bảng w cuối cùng kèm nhãn hết ngân sách… không phải chứng nhận"). | **Đề xuất:** bổ sung vào nội dung S31 một câu đặc tả nhánh hết ngân sách (trả v, π_v, ρ(v) kèm nhãn chưa chứng nhận, đồng bộ với S16 và S45).

**3. nhẹ | L04-S13–S18 | Lỗi kiểu chữ nhất quán |** S13 ("với π₀=(a,a)…"), S14, S15, S16, S17, S18 bắt đầu câu bằng chữ thường, trong khi mọi slide khác (S01–S12, S19 trở đi) viết hoa đầu mục. | **Đề xuất:** viết hoa ký tự đầu phần "Luận điểm và nội dung" tại 6 slide này.

**4. nhẹ | L04-S23 | Lỗi ký hiệu trong chứng minh |** Cụm "hạng đuôi γⁿ𝔼_{π\prime}[v^π(S_n)]" dùng "\prime" thay chỉ số đúng; nên là 𝔼_{π′} (chính sách cải thiện π′, vì khai triển theo T^{π′}). | **Đề xuất:** sửa chỉ số kỳ vọng thành π′.

Không có vấn đề về chu trình vấn đề–trực giác–ví dụ–hình thức–ứng dụng–kiểm tra: cả 7 phần đều có slide kiểm tra (S05/S12/S18/S26/S34/S41/S45), phần 7 thu hồi đúng bài toán mở đầu (S43 đối chiếu S03–S04, kết luận (b,b), (27,30) khớp S04). Ranh giới khái niệm–thuật toán và phân biệt mặt slide/ghi chú được giữ nhất quán.

#### Rà lại thuật toán 14–26

##### Báo cáo rà soát lỗi còn lại — L04-S14 đến S26

| Mức độ | Slide | Vấn đề | Bằng chứng | Sửa |
|---|---|---|---|---|
| **Trung bình** | S15 | Giá trị `v2` tính sai theo cập nhật đồng bộ từ `v1=(1,2)`. | `v2(s0)=1+0.9*1=1.9`; `v2(s1)=2+0.9*2=3.8`, không phải `2.9`. | Sửa thành `v2=(1.9,3.8)`. |
| **Trung bình** | S17 | Bảng tại chỗ `(1,2.9)` sai: sau khi cập nhật `s0=1`, cập nhật `s1` dùng bảng mới: `2+0.9*1=2.9` — đúng, nhưng nếu cập nhật `s1` trước rồi `s0` thì khác. Cần nêu rõ thứ tự cập nhật. | Ghi chú nói "cập nhật s0 rồi s1" nhưng không nêu rõ thứ tự ảnh hưởng kết quả. | Ghi rõ thứ tự cập nhật `s0` trước, `s1` sau; kết quả `(1,2.9)` đúng với thứ tự đó. |
| **Thấp** | S18 | Đáp án `v3=(2.71,3.71)` đúng, nhưng lời giải thích "s1: 2+0.9×1.9=3.71" — đúng vì `v2(s0)=1.9` (sau khi sửa S15). | Nếu giữ `v2=(1.9,2.9)` cũ thì `v3(s1)=2+0.9*2.9=4.61`, sai. | Sau khi sửa S15, đáp án S18 tự khớp. |
| **Thấp** | S21 | `v^{π1}=(10,30)` — kiểm tra: `s0: a→(1,s0)` nên `x=1+0.9x → x=10`; `s1: b→(3,s1)` nên `y=3+0.9y → y=30`. Đúng. | Không có lỗi. | — |
| **Thấp** | S21 | `q^{π1}(s0,b)=27` — kiểm tra: `b→(0,s1)` nên `0+0.9*30=27`. Đúng. | Không có lỗi. | — |
| **Thấp** | S22 | Ghi chú chuẩn bị chứng minh: "nếu u≤v thì Q_u(s,a)≤Q_v(s,a)" — đúng vì γ≥0. | Không có lỗi. | — |
| **Thấp** | S23 | Chứng minh dùng `‖v^π‖∞ ≤ Rmax/(1−γ)` — cần Rmax hữu hạn (giả thiết thưởng bị chặn). Đúng. | Không có lỗi. | — |
| **Thấp** | S24 | "Sau lượt đánh giá thứ K, nếu bước cải thiện còn đổi hành động, trả π vừa đánh giá cùng v^π" — đúng, không ghép chính sách mới với bảng cũ. | Không có lỗi. | — |
| **Thấp** | S25 | `∏_s|A(s)|=2×2=4` — đúng với 2 trạng thái, mỗi trạng thái 2 hành động. | Không có lỗi. | — |
| **Thấp** | S26 | `q^{π1}(s0,a)=10` — kiểm tra: `a→(1,s0)` nên `1+0.9*10=10`. Đúng. | Không có lỗi. | — |

**Lỗi chính còn lại:** S15 tính `v2(s1)` sai (2.9 thay vì 3.8). Lỗi này lan sang S17 (bảng tại chỗ dùng `v2` sai làm chuẩn so sánh) và S18 (đáp án `v3` chỉ đúng nếu `v2=(1.9,3.8)`). Các phép tính khác trong chuỗi S19–S26 đều khớp với mô hình đã cho.

#### Rà lại chứng minh 33–45

##### Báo cáo rà soát lỗi còn lại — L04-S33 đến L04-S45

| Mức độ | Slide | Vấn đề | Bằng chứng | Sửa |
|--------|-------|--------|------------|-----|
| Trung bình | S35 | Sai phép tính mẫu `T_*u` | Ghi `T_*u=(10,12,9)` nhưng tính lại với mô hình hai trạng thái: `T_*u(s0)=max{1+0,9·10, 0+0,9·11}=10`, `T_*u(s1)=max{2+0,9·10, 3+0,9·11}=12,9`. Giá trị 10 tại s0 đúng, 12,9 tại s1 đúng → kết quả ghi đúng. **Tuy nhiên** hiệu tuyệt đối giữa `T_*u` và `T_*v`: `(10,12,9)` và `(11,7,14,7)` → chênh lệch lớn nhất là `|14,7−12,9|=1,8` — đúng với chặn `0,9·2=1,8`. **Không còn lỗi.** |
| Thấp | S38 | Kiểm tra số 44 lượt | `100·0,9^44 ≈ 0,970`, giải bất phương trình `k > ln(0,01)/ln(0,9) ≈ 43,71` → 44 là số nguyên nhỏ nhất thỏa. **Đúng.** |
| Trung bình | S39 | Tam giác bất đẳng thức và hệ số | Ghi chú "Nếu dùng bản trả `w=Tv` như đánh giá chính sách ở slide 16, chặn của `w` là `γ‖Tv−v‖∞/(1−γ)`". Cần kiểm: `‖w−v_*‖ ≤ ‖Tv−v_*‖ = ‖Tv−Tv_*‖ ≤ γ‖v−v_*‖`, và `‖v−v_*‖ ≤ ρ(v)/(1−γ)` → `‖w−v_*‖ ≤ γρ(v)/(1−γ)`. **Công thức đúng.** |
| Thấp | S40 | Đếm số ô 324 | `3×3×6×6 = 324`. **Đúng.** |
| Thấp | S43 | Phép kiểm Q | `Q(s0,b)=0+0,9·30=27`; `Q(s1,b)=3+0,9·30=30`; hai hành động còn lại: `Q(s0,a)=1+0,9·27=25,3`; `Q(s1,a)=2+0,9·27=26,3`. **Đúng.** |
| Thấp | S41 | Chặn sai số | `0,02/(1−0,9) = 0,2`; so với `0,1` → chưa bảo đảm. **Đúng.** |
| Thấp | S45 | Câu hỏi tổng hợp | `ρ=0,01` → `e ≤ 0,01/(0,1) = 0,1` — đúng. Câu trả lời chính xác về mặt khái niệm. |

---

**Kết luận:** Không phát hiện lỗi nghiêm trọng còn lại. Các phép tính số (S35, S38, S40, S43), bất đẳng thức (S39), ngưỡng dừng (S41) và phân biệt khái niệm (S37, S45) đều chính xác. Phép tính 44 lượt đúng. Phần đọc thêm ở S37 nhất quán với giả thiết MDP hữu hạn, γ<1 và Π gồm chính sách phụ thuộc lịch sử. Phép kiểm S43 khớp với v*=(27,30). Tải học phù hợp với thời lượng khai báo. **Không còn lỗi cần sửa.**

## Lịch sử triển khai trước yêu cầu lập dàn bài này

Giữ nguyên nội dung dưới đây để truy nguyên; các mã và trạng thái thuộc bản HTML cũ.


## Trạng thái sau chỉnh sửa

- 38 trang tuyến chính, 4 trang bài tập dọc; 5 SVG cục bộ; không dùng raster hoặc tài nguyên mạng cốt lõi.
- Bản trước đã hợp nhất bốn báo cáo độc lập; lượt bổ sung dưới đây có kiểm định storyboard và đủ năm báo cáo độc lập. Mọi mục `chặn bàn giao` và `nghiêm trọng` đều có quyết định xử lý.
- Không sửa `index.html`, CSS dùng chung, không commit hoặc push.

## Bốn báo cáo độc lập — đầu vào chỉnh sửa

### Góc nhìn sinh viên

| Mức độ | Trang chiếu | Vấn đề | Bằng chứng | Đề xuất sửa | Xử lý |
|---|---|---|---|---|---|
| nghiêm trọng | A00–A03 cũ | Hình thức hóa $v_*,T^\pi,T_*$ đến trước khi người học thấy một quyết định cụ thể. | A02 nằm sau hai trang định nghĩa/tính chất. | Chuyển micro-example lên trước mọi hình thức tối ưu. | A02 đứng trước A08,A00,A01,A03. |
| nghiêm trọng | B06,C04,D03 cũ | Giả mã và chứng minh quá dày cho màn chiếu. | Codebox dưới 0,75 em; nhiều kết luận trên một trang. | Tăng chữ, tách thuật toán và chứng minh. | Codebox và bảng 0,92 em theo cỡ chữ trang; tách C04/C09, D03/D06, D04/D07. |
| trung bình | A07,D05 cũ | Hai kiểm tra thiếu mô hình cách nhau xa và lặp vai trò. | Cùng hỏi trạng thái hữu hạn/hạt nhân. | Gộp kiểm tra vào CartPole gần cuối bài. | Bỏ A07; D05 có câu hỏi và đáp án fragment. |
| trung bình | các câu hỏi chính | Thiếu kết luận thấy được sau tương tác. | Đáp án chỉ có trong notes. | Thêm fragment ngắn khi thực tế. | P02, B06, C05, D05 có đáp án fragment. |

### Chuyên gia Học tăng cường

| Mức độ | Trang chiếu | Vấn đề | Bằng chứng | Đề xuất sửa | Xử lý |
|---|---|---|---|---|---|
| chặn bàn giao | phần Bellman tối ưu | Thiếu $q_*$, Bellman $q_*$ và cách trích chính sách. | Bài đi thẳng từ $v_*$ sang $T_*$, không nối giá trị hành động. | Thêm định nghĩa, phương trình và greedy extraction từ A02. | Thêm A08,A09; A00 nối $v_*=\max_aq_*$. |
| nghiêm trọng | B02–B03 | Bước đổi hành động ở $s_0$ thiếu giá trị hành động giải thích. | Chỉ ghi $\pi_2=(b,b)$. | Tính $q_{\pi_1}(s_0,b)$. | B03 hiển thị $27$. |
| nghiêm trọng | X09 | Bài tập không tự chứa MDP. | Notes trỏ người học sang PDF. | Chép dữ kiện gọn và lời giải truy nguyên. | X09 có đủ sáu cặp trạng thái–hành động; notes cho $V_1$ và greedy. |
| trung bình | D08 mới | Thiếu cầu nối tới điều khiển phi mô hình. | CartPole kết bài nhưng không nêu vai trò $q_*$. | Thêm trang quyết định cuối. | D08 nối $q_*$ với các bài điều khiển sau. |

### Độ chính xác toán học và thuật toán

| Mức độ | Trang chiếu | Vấn đề | Bằng chứng | Đề xuất sửa | Xử lý |
|---|---|---|---|---|---|
| chặn bàn giao | A01,A03,D01–D02 cũ | Miền toán tử và chuẩn xuất hiện ngầm. | Dùng “co” trước khi định nghĩa không gian và chuẩn. | Định nghĩa $\mathcal V$, chuẩn vô cùng, kiểu $T^\pi,T_*$. | P02, A01, A03 đã sửa. |
| nghiêm trọng | A01 cũ | Miền chính sách của $T^\pi$ không rõ. | Có thể bị hiểu áp dụng trực tiếp cho chính sách phụ thuộc lịch sử. | Ghi chính sách Markov dừng. | A01 và D03/D06 phân biệt hai miền. |
| nghiêm trọng | B04 cũ | Ngưỡng dừng chưa cho biết sai số của giá trị nào. | Dừng theo chênh lệch nhưng không gắn với bảng trả về. | Dùng $\varepsilon_{\mathrm{step}}$ và chặn contraction đúng. | B04 trả $v_{j+1}$, chặn $\gamma\varepsilon_{\mathrm{step}}/(1-\gamma)$. |
| nghiêm trọng | C04 cũ | Phần dư tại bảng mới cần thêm một lượt $T_*$. | Giả mã vừa cập nhật vừa dùng residual không tách chi phí. | Tách lượt cập nhật và lượt residual. | C04/C09; C06 tính lượt kiểm đầu và nêu cách tái sử dụng $w=T_*v$ ở các vòng sau. |
| chặn bàn giao | D04 cũ | Hai chặn được nêu mà không suy diễn. | Không có bước $\rho+\gamma e$ hay greedy identity. | Tách residual→value và value→policy. | D04, D07 mở đầy đủ bước chính. |
| chặn bàn giao | D03 cũ | Chứng minh tối ưu toàn cục quá dày và dễ dùng sai $T^\pi$. | Cận trên và đạt cận nằm chung một trang. | Tách upper bound và greedy attainment. | D03 và D06. |
| trung bình | C06 cũ | Nhãn chi phí “thường cao/thấp” không kiểm chứng được. | Không ghi phép tính chính. | Ghi chi phí theo $|\mathcal S|$ và lượt mô hình. | C06 dùng ba hàng định lượng. |

### Phản biện học thuật và giảng dạy Học tăng cường–lập kế hoạch

| Mức độ | Trang chiếu | Vấn đề | Bằng chứng | Đề xuất sửa | Xử lý |
|---|---|---|---|---|---|
| chặn bàn giao | A00–A04 cũ | Công thức đúng riêng lẻ nhưng trình tự chưa hỗ trợ suy luận $q_*\to v_*\to T_*$. | Micro-example đến muộn; thiếu cầu nối giá trị hành động. | Dùng A02 trước, truyền cùng số qua các hình thức. | A02→A08→A00→A01→A03→A09. |
| nghiêm trọng | B07 cũ | Lặp chính sách sửa đổi không đủ dữ kiện để tái lập hoặc gắn bảo đảm. | Không rõ mang $v_0$, dừng ngoài, phá hòa, chi phí. | Hoàn thiện hoặc bỏ khỏi tuyến chính. | Bỏ B07; log sai khác; giữ PI chính xác B06–B08. |
| nghiêm trọng | C04–C08 cũ | Tiêu chuẩn dừng xuất hiện trước cơ chế tính residual và chứng minh. | Chưa thấy lượt $T_*$ bổ sung. | Tách cơ chế, xem trước, rồi chứng minh cuối bài. | C04,C09,C08→D04,D07. |
| trung bình | D05 cũ | CartPole trong nửa lưới khó đọc. | Hình chỉ có max-width, không có width cục bộ. | Đặt width rõ và giữ max-height. | CSS `.figure` và `.grid2 .figure` đã sửa. |
| trung bình | kết bài cũ | Không có trang tổng hợp quyết định trước bài tập. | D05 chuyển thẳng sang nhánh dọc. | Thêm trang quyết định. | D08 được thêm trước X09. |

## Sai khác có chủ ý so với nguồn

- Gộp các trang mục lục/tính chất lặp; bỏ trang định lý xem trước để dành không gian cho $q_*$ và các bước chứng minh.
- Bổ sung A08/A09 về $q_*$, Bellman $q_*$ và greedy extraction. Đây là sai khác nội dung lớn nhất nhưng dùng trực tiếp micro-example A02 và ký hiệu chuẩn của chính bài.
- Bỏ lặp chính sách sửa đổi khỏi tuyến chính vì nguồn không đủ đặc tả tái lập. Không bỏ PI chính xác hoặc bảo đảm tối ưu hữu hạn.
- Tách C04/C09 để tính residual bằng một lượt $T_*$ thêm; bổ sung chi phí lượt này.
- Tách D03/D06 và D04/D07 để mỗi trang chỉ giữ một bước chứng minh.
- Gộp kiểm tra mô hình đầu bài vào CartPole; thêm D08 làm trang quyết định cuối.
- Không thêm code demo hoặc thuật toán phi mô hình.

## Quyết định không áp dụng

- Không hoàn thiện lặp chính sách sửa đổi bằng các giả thiết hoặc định lý ngoài nguồn. Việc này sẽ mở rộng phạm vi và cần một phân tích hội tụ riêng.
- Không đưa Q-learning vào A09/D08. Chỉ nêu $q_*$ là cầu nối; thuật toán học từ trải nghiệm thuộc bài sau.
- Không chuyển X09 thành ví dụ chính vì 120 phút đã phân bổ đủ; dữ kiện đầy đủ được giữ ở nhánh dọc.

## Sửa cục bộ sau tái rà

| Mức độ | Trang chiếu | Vấn đề | Bằng chứng | Đề xuất sửa | Xử lý |
|---|---|---|---|---|---|
| nghiêm trọng | A08 | Định nghĩa $q_*$ bằng điều kiện $A_0=a$ có thể không xác định khi biến cố này có xác suất bằng không dưới chính sách. | Chính sách tiếp tục và hành động đầu chưa được tách. | Dùng can thiệp ép hành động đầu, rồi tối ưu chính sách từ $t=1$. | Định nghĩa $a\triangleright\pi$ và giải thích rõ trong notes. |
| nghiêm trọng | A09,D06 | Trích tham lam được gọi là chính sách tối ưu trước khi chứng minh đạt cận. | Kết luận xuất hiện trước bước $T^{\pi_v}v_*=v_*$. | Chỉ gọi là ứng viên tại A09. | Dùng $\bar\pi$ tại A09; chỉ kết luận tối ưu ở D06. |
| nghiêm trọng | X09 | Lời giải tham lam chưa cho các giá trị hành động tạo từ $V_1$. | Kết quả $(b,a,a)$ thiếu phép tính trung gian. | Ghi đủ hai giá trị tại mỗi trạng thái. | Notes có $Q_{V_1}(s_0)=(1{,}35;2{,}8)$, $Q_{V_1}(s_1)=(2{,}9;0{,}8)$ và $Q_{V_1}(s_2)=(3{,}8;0{,}9)$. |
| nghiêm trọng | C09 | Lượt kiểm phần dư có thể bị tính lại khi VI chưa dừng. | $w=T_*v$ đã là bảng lặp kế tiếp. | Gán $v\leftarrow w$ và lặp. | Giả mã và notes nêu rõ tái sử dụng; ngưỡng được giới hạn cho $\gamma>0$. |
| trung bình | A02 | Hai nhánh số chưa nói rõ là kết quả tất định và giá trị tiếp tục tối ưu. | Người học có thể hiểu $v_*(s')$ là giá trị tức thời. | Nêu trạng thái kế chắc chắn và chính sách tiếp tục. | Hai nhánh ghi rõ kết quả tất định; notes nêu tiếp tục tối ưu từ $t=1$. |
| trung bình | A09 | Cầu nối từ Bellman $q_*$ tới phép cực đại chưa có tương tác thực. | Chỉ có công thức và kết luận. | Hỏi vị trí của phép cực đại và cho đáp án ngắn. | Thêm “Câu hỏi:” và fragment giải thích cực đại tại trạng thái kế. |
| trung bình | B08 | Notes còn câu biên tập về phân tuyến nội dung. | Câu này không thuộc mạch nói. | Chuyển quyết định biên tập sang planning. | Notes chỉ giữ bảo đảm và giả thiết phá hòa. |
| trung bình | CSS,D08 | Bảng/codebox nhỏ và bảng kết bài dài. | Cỡ cục bộ dưới ngưỡng; câu trong ô dài. | Tăng cỡ chữ, rút gọn hàng. | Bảng và codebox 0,92 em; D08 dùng bốn lựa chọn ngắn. |

Rà lân cận sau sửa: A02–A09–A00–A01 giữ mạch ví dụ → định nghĩa → hình thức; B06–B08 giữ bảo đảm PI; C04–C09–C05–C06 nối cập nhật → kiểm phần dư → chi phí; D06–D08–X09 nối chứng minh → quyết định → bài tập. Số trang và tổng thời lượng không đổi.

## Tự kiểm toán học của tác tử chỉnh sửa

- A02: $2+0{,}9\cdot5=6{,}5$; $0+0{,}9\cdot8=7{,}2$.
- B03: $q_{\pi_1}(s_0,b)=0+0{,}9\cdot30=27$.
- B04: nếu $\Delta_j\le\varepsilon_{\mathrm{step}}$, sai số của $v_{j+1}$ không quá $\gamma\varepsilon_{\mathrm{step}}/(1-\gamma)$.
- C02 dùng đúng $\gamma=0{,}9$ và cập nhật đồng bộ.
- D04: $e\le\rho+\gamma e$ cho $e\le\rho/(1-\gamma)$.
- D07: từ $T^{\pi_v}v=T_*v$, $L\le\gamma e+\gamma(e+L)$, nên $L\le2\gamma e/(1-\gamma)$.
- X09: $V_1=(1,2,2)$; chính sách tham lam $(b,a,a)$.

## Tự kiểm biên tập và mạch

- `no-ai-slop`: câu trực tiếp, không khẩu hiệu, không nhận định quảng bá, không lặp kết luận; thuật ngữ và ký hiệu nhất quán.
- Quill: ví dụ → định nghĩa → toán tử → thuật toán → bảo đảm → giới hạn; không có công thức trọng tâm trước tiên quyết.
- Không tạo `quill.json`; đây không phải dự án sách.

## Giới hạn

- Cần tác tử độc lập tái rà phần $q_*$, B04, C09 và D03–D07 vì đây là các thay đổi toán học đáng kể.
- Cần điều phối viên rà trực quan toàn bộ trang bằng RevealJS/Codex Slides ở khung 16:9 và màn hình hẹp.

## Kiểm tĩnh của tác tử chỉnh sửa

- HTML có 42 `data-slide-id` duy nhất: 38 trang chính và 4 trang dọc; cả 42 trang có notes và nằm ở độ sâu section đúng mẫu.
- Mọi ID có mục tương ứng trong storyboard; không có ID, phân bổ hoặc chỉ dẫn phân tuyến xuất hiện trên mặt trang hay trong notes.
- 15 đường dẫn CSS, script và hình đều là tài sản cục bộ tồn tại; không có raster hoặc URL cốt lõi bên ngoài.
- Năm SVG phân tích XML được, có `role="img"`, `title`, `desc`; cỡ chữ nhỏ nhất là 30 px.
- KaTeX nghiêm ngặt phân tích 232 công thức không có lỗi; `git diff --check` sạch.

## Tái rà cuối

- Tác tử toán học–thuật toán xác nhận định nghĩa $q_*$ bằng hành động đầu bị ép, ứng viên tham lam, chứng minh tối ưu, phép tính X09 và luồng lặp giá trị đều đúng. Không còn lỗi `chặn bàn giao` hoặc `nghiêm trọng`.
- Tác tử học thuật–giảng dạy xác nhận cỡ chữ hiệu dụng của bảng/giả mã là $0{,}7544\,\mathrm{em}$, câu hỏi A09 và storyboard khớp, ghi chú diễn giả sạch chỉ dẫn nội bộ, 38 trang chính đủ 120 phút và ranh giới Bài 03/Bài 05 được giữ. Không còn lỗi `chặn bàn giao` hoặc `nghiêm trọng`.

## Kiểm định cuối của điều phối viên

- `python3 -m reloadserver 8765` không chạy vì môi trường thiếu mô-đun `reloadserver`. Điều phối viên dùng cây web tạm không có `.env` và `python3 -m http.server 8765 --bind 127.0.0.1` để kiểm thử tại đúng cổng 8765.
- HTML có 42 mã trang duy nhất, 42 ghi chú diễn giả và đúng cấu trúc section lồng; mọi mã đều có mục trong storyboard.
- Chromium headless dựng đủ 42 trang ở 1280 × 720 và 800 × 600, không có lỗi console hoặc request. Điều hướng `↓`, `↑`, `→` cho kết quả P01, P00, A02. Điều phối viên duyệt ảnh mọi trang và mở riêng các trang công thức bị bộ dò hình học gắn dương tính giả do cấu trúc nội bộ KaTeX; không thấy cắt, chồng hoặc tràn.

## Pha II — đồng bộ với lecture note và rà lại độc lập

### Runtime OpenRouter

- Tác tử lập kế hoạch: `requested_model=deepseek/deepseek-v3.2`, `observed_model=deepseek/deepseek-v3.2`, `provider=OpenRouter`; hồ sơ `plan`, 10 lượt. Lần đầu dừng với `model exceeded the tool-call limit (8)`; lần chạy lại thành công.
- Hai lượt writer đầu dùng `requested_model=z-ai/glm-5.3-flash` lần lượt dừng với `model exceeded the tool-call limit (10)` và `model exceeded the tool-call limit (8)`. Lượt sửa tiếp theo bị mất JSON ở lớp điều phối nên không dùng lời tự khai của worker làm bằng chứng runtime; điều phối viên kiểm tra diff và hoàn tất các sửa còn thiếu.
- Năm báo cáo độc lập ban đầu dùng đúng mô hình quy định. Bốn lượt thành công ngay; vai phản biện học thuật–giảng dạy lần đầu dừng với `model exceeded the tool-call limit (8)` rồi chạy lại thành công. Các JSON thành công đều ghi `provider=OpenRouter` và `requested_model=observed_model`.
- Tái rà toán–thuật toán: lần đầu dừng với `model exceeded the tool-call limit (6)`; lần chạy lại thành công với hồ sơ `recheck`, 8 lượt, `requested_model=observed_model=deepseek/deepseek-v3.2`, `provider=OpenRouter`.
- Tái rà phản biện học thuật–giảng dạy: hồ sơ `recheck`, 6 lượt, `requested_model=observed_model=deepseek/deepseek-v3.2`, `provider=OpenRouter`.
- Tái rà kết nối và mạch viết: hồ sơ `recheck`, 5 lượt, `requested_model=observed_model=z-ai/glm-5.3-flash`, `provider=OpenRouter`.
- Mọi liên kết `.env` tạm trong gói worker đã được gỡ sau khi các tiến trình kết thúc. Không đưa `.env` vào gói nội dung, prompt hoặc nhật ký.

### Năm báo cáo độc lập và quyết định

| Vai | Mức cao nhất | Vấn đề chính | Quyết định |
|---|---|---|---|
| Góc nhìn sinh viên | trung bình | A02 thiếu nguồn của giá trị tiếp tục 10/11; A08 cần giải thích can thiệp trên mặt trang; cầu nối miền chính sách ở A01 còn mờ. | Nêu 10/11 ở A02; định nghĩa rõ can thiệp ở A08; A01 hẹn chặn chân trời ở phần bảo đảm. Sửa câu phân bổ Bài 9 thành 12 phút. |
| Chuyên gia Học tăng cường | trung bình | A08 cần tách can thiệp khỏi điều kiện hóa; D01 cần nêu cơ sở đơn điệu. | Sửa A08; tách hai cơ sở đơn điệu thành hai gạch đầu dòng ở D01. Không đổi thứ tự A02→A08→A00 vì đây là mạch ví dụ→định nghĩa→giá trị. |
| Toán học và thuật toán | trung bình | C09 cần ký hiệu phép nhân rõ; lecture note cần chặn dừng B04 và ngưỡng mất mát chính sách. | Dùng `\cdot` ở C09; bổ sung hai chặn vào topic 06 và 13; tự tính lại micro-example và $k=44$. |
| Phản biện học thuật–giảng dạy | nghiêm trọng | A08 chưa nói rõ $a\triangleright\pi$ buộc $A_0=a$, không phải điều kiện hóa theo hành động do $\pi$ sinh. | Đã sửa trực tiếp trên mặt trang và trong ghi chú; tái rà xác nhận lỗi nghiêm trọng được xử lý triệt để. |
| Kết nối và mạch viết | trung bình | C08 cần báo rõ ba bước sẽ được xử lý theo thứ tự; topic 06 trong note cần neo B04. | Thêm câu chuyển ở C08 và chặn đánh giá vào topic 06. Báo cáo ban đầu đếm nhầm nhánh dọc thành section ngoài; kiểm tĩnh xác nhận đúng 5 section ngoài. |

Các đề xuất không áp dụng:

- Giữ dấu phẩy thập phân theo quy ước tiếng Việt; không đổi sang dấu chấm.
- Giữ định nghĩa ngắn của $\Pi$ ở A00 dù đã có ở P02 để trang định nghĩa $v_*$ tự chứa.
- Giữ công thức đếm chính sách ở B08 vì sửa trực tiếp lỗi của nguồn trang 33.
- Không đổi thứ tự cụm tối ưu và không chuyển Bài 9 vào tuyến chính; hai thay đổi này không cần thiết để sửa lỗi cục bộ.

### Tái rà sau chỉnh sửa

- Toán–thuật toán xác nhận các số $10$, $11$, $9{,}9$, nghiệm biến thể $20$, định nghĩa $a\triangleright\pi$, chặn đánh giá, ngưỡng phần dư, số chính sách, tính đơn điệu và $k=44$ đều đúng; không còn lỗi chặn hoặc nghiêm trọng.
- Phản biện học thuật–giảng dạy xác nhận A08 đã phân biệt can thiệp với điều kiện hóa; các cầu nối từ ví dụ tới hình thức và từ tiêu chuẩn dừng tới chứng minh nhất quán; không còn lỗi chặn hoặc nghiêm trọng.
- Kết nối và mạch viết rà A02±2, A08–A03, B06–C00 và C08–D03; xác nhận 5 section ngoài, 42 mã trang và bốn bài tập dọc nằm trong section kết luận; không còn lỗi chặn hoặc nghiêm trọng.
- `no-ai-slop`: loại từ tiếng Anh không cần thiết trong topic 06, cắt diễn giải trùng và giữ câu trực tiếp. Quill: dàn ý vẫn theo ví dụ→định nghĩa→toán tử→thuật toán→bảo đảm→giới hạn; không tạo `quill.json`.

### Kiểm định cuối sau Pha II

- Kiểm tĩnh: 42 `data-slide-id` duy nhất, 42 ghi chú, 5 section ngoài; mọi tài nguyên tương đối tồn tại; `git diff --check` sạch.
- `python3 -m reloadserver 8765` không chạy vì thiếu mô-đun `reloadserver`. Dùng cây web cô lập trong `/tmp`, không chứa `.env`, và `python3 -m http.server 8765 --bind 127.0.0.1 --directory <cây-tạm>`.
- Chromium headless kiểm đủ 42 trang ở 1280×720 và 800×600. Lần đầu phát hiện A01 bị cắt công thức ở mép phải; đã tách kiểu toán tử và định nghĩa thành hai dòng rồi chạy lại toàn bộ. Kết quả cuối: không tràn, không lỗi KaTeX, console, request hoặc tài nguyên; không có request ngoài máy chủ cục bộ. Phím `↓`, `↑`, `→` lần lượt tới P01, P00, A02.
- Trình đọc lecture note ở 390×844 trả HTTP 200, dựng 589 công thức KaTeX, 30 khối `details`, 15 lời giải; không tràn ngang, không lộ `note-topic-id`, phím Enter mở được khối đầu tiên.
- Codex Slides không khả dụng trong môi trường này do runtime Node.js 18 thấp hơn yêu cầu Node.js 20 của gói. Vì vậy chỉ xác nhận kiểm định RevealJS cục bộ, không tuyên bố đã rà bằng Codex Slides.
- Năm SVG tải được trong Chromium; mỗi tệp có `role="img"`, `title`, `desc`. Không có ảnh raster hoặc tài nguyên cốt lõi qua mạng. Môi trường thiếu `xmllint`, nên tính hợp lệ được xác nhận qua tải ảnh thực tế và không có request lỗi.
- Bốn tệp văn bản HTML/outline/storyboard/review-log đã được ghi vào Design Files của dự án Codex Slides `20260824154346-chuy-n-lecture-4-gi-i-mdp-b-ng-quy-ho-ch-z4es` và đọc lại trùng chính xác nội dung trong kho. Tải riêng `gridworld.svg` lên Design Files trả HTTP 500; SVG vẫn được kiểm trực tiếp trong RevealJS.
- Dự án Codex Slides vẫn ở trạng thái `draft`, bước `clarify`, 0 trang; Codex Browser không khả dụng trong phiên này. Vì vậy không tuyên bố đã rà trực quan bằng Codex Slides; kiểm tra trực quan được thực hiện trên RevealJS cục bộ.

## Lượt rà storyboard và năm báo cáo độc lập — lượt bổ sung B04

Runtime: các lượt thành công dùng `requested_model=z-ai/glm-5.3-flash`, `observed_model=z-ai/glm-5.3-flash`, `provider=OpenRouter` (storyboard, sinh viên, chuyên gia Học tăng cường, toán lượt hẹp, học thuật–giảng dạy và mạch viết). Lượt toán đầu vượt giới hạn tool-call nên không được tính; lượt toán hẹp sau đó thành công.

### Rà storyboard

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa | quyết định |
|---|---|---|---|---|---|
| nhẹ | A02,A09 | Cột Kiểm tra ghi cả A02. | A02 là ví dụ; chỉ A09 đặt câu hỏi kiểm tra Bellman tối ưu. | Chỉ ghi A09 ở cột Kiểm tra. | Chấp nhận. |
| nhẹ | C09 | Dùng $\varepsilon_{\mathrm{pol}}$ trước khi định nghĩa trên mặt trang. | Ký hiệu chỉ được giải thích trong mạch chứng minh sau đó. | Nêu đây là mức mất mát chính sách cho phép. | Chấp nhận. |

### Góc nhìn sinh viên

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa | quyết định |
|---|---|---|---|---|---|
| nhẹ | A02,A09 | Storyboard gán sai vai trò kiểm tra cho A02. | A02 không có nhãn “Câu hỏi:”. | Chỉ giữ A09 ở bước kiểm tra. | Chấp nhận. |
| nhẹ | B06 | Cụm “giá trị có thể không tăng nghiêm” chưa nói rõ hệ quả. | Người học chưa thấy vì sao phá hòa tùy ý nguy hiểm. | Nêu khả năng tạo chu trình chính sách. | Chấp nhận. |
| nhẹ | X07 | Có thể thêm nhãn tự luyện trên mặt trang. | Nhãn giúp phân tuyến bài tập. | Thêm nhãn. | Không áp dụng: quy ước cấm hiển thị nhãn phân tuyến nội bộ. |
| chặn bàn giao | toàn bài | Báo thiếu thư viện RevealJS trong cây worker. | Cây tạm chỉ chứa tệp được phép gửi, không phải kho đầy đủ. | Bổ sung thư viện. | Bác bỏ là dương tính giả; kho thật có đủ tài sản cục bộ và sẽ được kiểm khi render. |

### Chuyên gia Học tăng cường

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa | quyết định |
|---|---|---|---|---|---|
| trung bình | X09 | Chỉ bao phủ phần 1 của Bài 9. | Phần 2 không xuất hiện trong nhánh bài tập. | Thêm phần 2. | Không thêm trang: nội dung trùng chu trình B01–B03 và vượt 12 phút; ghi rõ sai khác trong outline, notes và nhật ký. |
| nhẹ | A08–A00 | Có thể nhắc lại quan hệ $q_\pi$–$v_\pi$. | Bài đi thẳng vào $q_*$ và $v_*$. | Thêm trang/công thức nhắc lại. | Không áp dụng: đây là tiên quyết đã hoàn thành ở Bài 03. |
| nhẹ | C06 | Ánh xạ trang nguồn 29 chưa rõ. | Nguồn dùng so sánh định tính, đích dùng chi phí định lượng. | Ghi sai khác. | Chấp nhận trong outline và nhật ký. |
| nhẹ | P01 | Từ “hạt nhân” có thể mơ hồ. | Notes chưa ghi ký hiệu cụ thể. | Gọi rõ mô hình chuyển–thưởng $p(s',r\mid s,a)$. | Chấp nhận. |
| nhẹ | D08 | Cầu nối sang Bài 05 chưa thu hồi phân ranh mô hình. | Kết bài chỉ nhắc $q_*$. | Nêu rõ biết mô hình và không biết mô hình. | Chấp nhận. |

### Độ chính xác toán học và thuật toán

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa | quyết định |
|---|---|---|---|---|---|
| nhẹ | B06 | Giải thích phá hòa chưa nêu điều kiện gây chu trình. | Đổi tùy ý giữa các hành động đồng hạng có thể làm chính sách đổi qua lại dù giá trị không đổi. | Nêu phá hòa tùy ý có thể tạo chu trình; dùng quy tắc cố định. | Chấp nhận. |
| nhẹ | A02,B04,C09,D04,D07,X09 | Không phát hiện lỗi số hay công thức. | Tính lại cho kết quả lần lượt $6{,}5$, $7{,}2$, các chặn phần dư và chính sách $(b,a,a)$. | Giữ các phép tính. | Chấp nhận; X09 được rà lại sau khi tách bốn hàng chuyển. |

### Phản biện học thuật và giảng dạy

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa | quyết định |
|---|---|---|---|---|---|
| nghiêm trọng | X09 | Hai hàng gộp làm mỗi hành động có hai kết quả xác suất 1. | Mỗi hàng `(s_1,a),(s_1,b)` và `(s_2,a),(s_2,b)` chứa hai chuyển tất định. | Tách thành bốn hàng, mỗi cặp $(s,a)$ có đúng một kết quả. | Chấp nhận. |
| trung bình | B05 | Điều kiện công bằng được viết như mô tả, chưa phải giả thiết chủ động. | Câu cũ không chỉ rõ lịch cập nhật phải thỏa điều kiện. | Viết “lịch cập nhật phải…”. | Chấp nhận. |
| trung bình | C03 | “Bảng đã kiểm tra” không chỉ ra quan hệ với phần dư. | Chặn ở C09 yêu cầu cùng một $v$. | Nói chính bảng $v$ dùng để kiểm phần dư. | Chấp nhận. |
| nhẹ | B06 | Tổng chuyển bị viết tắt. | Thiếu chỉ số $s',r$ và đối số của $p$. | Viết đầy đủ phép tổng Bellman. | Chấp nhận. |

### Kết nối và mạch viết

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa | quyết định |
|---|---|---|---|---|---|
| trung bình | A02→A00 | $v_*$ xuất hiện trước trang định nghĩa. | A02 ghi trực tiếp $v_*(s_1),v_*(s_2)$. | Dùng cụm “giá trị tiếp tục tối ưu”, đặt ký hiệu ở A00. | Chấp nhận. |
| nhẹ | B08→C00 | Chuyển từ PI sang VI chưa hiện trên mặt trang. | Vai trò trong mạch: kết PI; kết nối ra Gridworld còn nằm ở suy luận của người học. | Thêm câu báo bỏ bước giải hệ và chuyển sang VI. | Chấp nhận. |
| nhẹ | D08 | Kết bài chưa thu hồi rõ P01 và nối Bài 05. | Vai trò trong mạch: chọn công cụ; kết nối vào từ bảo đảm, kết nối ra bài tập/Bài 05 còn mờ. | Thu hồi đầu vào–đầu ra và phân ranh mô hình. | Chấp nhận. |
| trung bình | số section | Báo cáo đếm sáu section ngoài. | Bộ phân tích HTML và storyboard đều cho năm section ngoài; nhánh X nằm dọc trong section D. | Giảm số section. | Bác bỏ là lỗi đếm; giữ năm mạch hợp lệ. |

## Sửa sau các báo cáo

- HTML: sửa P01, A02, B05, B06, B08, C00, C03, C09, D08 và X09; bỏ `RevealMarkdown` không dùng khỏi riêng tệp B04.
- SVG: `gridworld.svg` bỏ vòng tự lặp “0” ở trạng thái kết thúc và ghi rõ không sao lưu.
- X09 có bốn hàng chuyển tất định riêng; $V_1=(1,2,2)$ và chính sách tham lam $(b,a,a)$ vẫn đúng.
- Outline ghi sai khác trang nguồn 29, lỗi gõ trang 33 và việc lược Bài 9 phần 2.
- Worker từng sửa nhầm bản sao `lecture-template.html`; điều phối viên loại thay đổi này, không đưa vào kho.
- Chưa tính lượt này là đã render hoặc kiểm định cuối; các bước đó do điều phối viên thực hiện sau tái rà.

## Tái rà sau chỉnh sửa

- Runtime của hai lượt thành công: `requested_model=z-ai/glm-5.3-flash`, `observed_model=z-ai/glm-5.3-flash`, `provider=OpenRouter`.
- Rà toán học–thuật toán: tính lại độc lập X09 cho $V_1=(1,2,2)$, sáu giá trị hành động $(1{,}35;2{,}8)$, $(2{,}9;0{,}8)$, $(3{,}8;0{,}9)$ và chính sách $(b,a,a)$; tổng xác suất của mỗi cặp $(s,a)$ bằng 1. B05, B06, C03, C09 và `gridworld.svg` nhất quán; không còn lỗi chặn bàn giao hoặc nghiêm trọng.
- Rà mạch viết: xác nhận đúng 5 section ngoài và các ranh giới A02±2, B05–C00, C03–C09, D05–X09. Không còn lỗi chặn bàn giao hoặc nghiêm trọng. Đề xuất nhẹ ở A02 được áp dụng bằng cách hiển thị trực tiếp hai phép tính thay cho ký hiệu suy ra; thứ tự ID C09 trước C05 là chủ ý và không đổi thứ tự trình bày.

## Giai đoạn I — ghi chú bài giảng

### Đầu ra và runtime

- Tạo `materials/lec-04/lecture-note.md` gồm 15 chủ đề duy nhất, đủ bốn nhóm cốt lõi, cầu nối, bổ sung và đọc thêm; mỗi chủ đề có câu hỏi, gợi ý và lời giải.
- Ba reader lập kế hoạch, phân tích nguồn và hợp nhất đều trả
  `requested_model=observed_model=deepseek/deepseek-v3.2`, `provider=OpenRouter`.
- Writer bản đầu và các lượt sửa thành công đều trả
  `requested_model=observed_model=z-ai/glm-5.3-flash`, `provider=OpenRouter`.
- Năm vai rà độc lập dùng đúng model được phân công: sinh viên và mạch viết dùng
  `z-ai/glm-5.3-flash`; chuyên gia Học tăng cường, toán–thuật toán và phản biện
  giảng dạy dùng `deepseek/deepseek-v3.2`; mọi kết quả hợp lệ có provider
  `OpenRouter`.

### Vấn đề bắt buộc và quyết định

| mức độ | chủ đề | vấn đề | bằng chứng | quyết định |
|---|---|---|---|---|
| nghiêm trọng | `lec-04-topic-11` | Bài tập yêu cầu sai số nhỏ hơn 1 nhưng lời giải dùng ngưỡng 0,1. | Bất đẳng thức đúng là $0{,}9^k100<1$. | Sửa thành $k>43{,}7$, cần 44 lượt. |
| nghiêm trọng | `lec-04-topic-06` | Tuyên bố đánh giá dừng sớm vẫn bảo đảm PI dừng hữu hạn thiếu giả thiết và ngoài phạm vi nguồn. | Bảo đảm trong bài dùng đánh giá chính xác. | Ghi rõ đánh giá dừng sớm là biến thể chưa phân tích. |
| nghiêm trọng | `lec-04-topic-12` | Chứng minh dùng tính đơn điệu trước khi phát biểu. | $T^\pi$ và $T_*$ phải bảo toàn thứ tự. | Thêm bổ đề đơn điệu ở topic 04, truy nguyên hw3 Bài 7. |
| nghiêm trọng | `lec-04-topic-02` | Lời giải ban đầu giữ $v_*(s_1)=11$ sau khi đổi phần thưởng của nhánh $b$, nên không tự nhất quán. | Hệ mới cho $v_*(s_0)=v_*(s_1)=20$. | Viết lại hệ, phép thế và kiểm tra nhánh $a$. |
| nghiêm trọng | `lec-04-topic-13` | Chặn mất mát chính sách được nêu nhưng suy diễn quá tắt. | Cần đưa $L$ sang hai vế trong $L\le\gamma e+\gamma(e+L)$. | Mở đầy đủ chuỗi bất đẳng thức và chặn theo phần dư. |

### Các sửa và sai khác có chủ ý

- Sửa lỗi gõ nguồn trang 33: số chính sách xác định tổng quát là
  $\prod_s|\mathcal A(s)|$; khi mọi trạng thái có cùng tập hành động thì bằng
  $|\mathcal A|^{|\mathcal S|}$.
- Dùng $C_{\text{model}}=O(\sum_s\sum_a|\operatorname{supp}p_{s,a}|)$ thay cho
  nhãn định tính “đắt/rẻ”; không tuyên bố PI hoặc VI nhanh hơn tuyệt đối.
- Giữ phần 1 Bài 9 trong khối 30 phút; phần 2 là tự học bằng PI ở topic 05–07.
  Không thêm Monte Carlo, Q-learning hoặc code demo.
- Giữ cả bản đồ bốn nhóm và danh sách 15 chủ đề: bản đồ phục vụ phân loại theo
  yêu cầu, danh sách cố định thứ tự ánh xạ. Đề xuất bỏ một khối được bác vì làm
  mất một trong hai chức năng này.
- Báo động `(27,30)` phải thành `(29,30)` được bác sau khi đối chiếu: MDP
  topic 05 dùng $s_0\xrightarrow{b}(0,s_1)$, còn biến thể topic 02–03 mới dùng
  phần thưởng 2. Hai reviewer tái rà đã xác nhận các nghiệm 10/11, 20/20 và
  27/30 đúng trong từng MDP.

### Lỗi worker và phục hồi

- Một lượt reviewer toán trên gói lớn dừng đúng lỗi
  `model exceeded the tool-call limit (4)`; chạy lại cùng DeepSeek trên một tệp
  cô lập và hoàn tất.
- Các writer vá rộng lần lượt dừng `model exceeded the tool-call limit (8)`,
  `model exceeded the tool-call limit (12)`, và
  `model returned an empty or incomplete answer after all retries`. Lượt vá ba
  điểm tiếp theo dừng `model exceeded the tool-call limit (4)` sau khi ghi một
  phần. Không đổi model; điều phối viên kiểm diff, khôi phục đoạn bị thay nhầm,
  áp dụng các vá cơ học còn lại và yêu cầu tái rà độc lập.
- Một recheck DeepSeek phạm vi hẹp dừng `model exceeded the tool-call limit (3)`;
  chạy lại cùng model với phạm vi dòng rõ hơn và hoàn tất.
- Liên kết `.env` chỉ tồn tại tạm để cầu nối nạp khóa, bị MCP chặn đọc và được
  gỡ ngay sau mỗi nhóm tiến trình. Không nội dung `.env` nào được đưa vào prompt,
  log hoặc sản phẩm.

### Tái rà sau sửa

- DeepSeek xác nhận Bellman, tính đơn điệu, tính co, số chính sách, điều kiện PI,
  phép tính 44 lượt, chi phí, chặn mất mát và Bài 9 đều đúng; không còn lỗi
  `chặn bàn giao` hoặc `nghiêm trọng`.
- GLM xác nhận đủ 15 marker, các kết nối vào–ra, thuật ngữ và văn phong; không
  còn lỗi `chặn bàn giao` hoặc `nghiêm trọng`.
- Hai lượt cuối cùng đọc riêng topic 02 xác nhận ví dụ gốc thêm $b$ với phần
  thưởng 0 cho 10/11, còn bài kiểm tra đổi phần thưởng thành 2 cho 20/20; không
  còn bước nhảy logic. Phép thế được viết thêm một bước theo đề xuất mức trung bình.
- Tự kiểm `no-ai-slop`: không có khẩu hiệu, câu hỏi tu từ, kết luận lặp hoặc lời
  dẫn rỗng. Tự kiểm Quill: tuyến Bellman kỳ vọng → tối ưu → toán tử → PI/VI →
  hội tụ → phần dư → giới hạn liên tục giữ thứ tự tiên quyết. Không tạo
  `quill.json`.

### Kiểm định cuối ghi chú

- `python3 -m reloadserver 8765` thất bại vì môi trường thiếu mô-đun
  `reloadserver`. Điều phối viên dùng cây web tạm không chứa `.env` và
  `python3 -m http.server 8765 --bind 127.0.0.1` tại đúng cổng 8765.
- Chromium headless tải `material-viewer.html` ở 1440 × 900 và 390 × 844:
  HTTP 200, không lỗi console, page hoặc request; không tràn ngang toàn trang.
- Trình xem dựng 584 biểu thức KaTeX, không có `.katex-error`; nhận đủ 30 khối
  thu gọn gồm 15 lời giải; không hiển thị `note-topic-id`.
- Liên kết “Mở ghi chú” trên thẻ Bài 04 trỏ đúng tài liệu và deck. Dùng bàn
  phím đặt tiêu điểm vào `summary` rồi nhấn Enter mở được khối “Gợi ý”. Một
  bảng rộng dùng cuộn ngang cục bộ trong khung, không làm tràn trang.
- Kiểm tĩnh xác nhận 15 marker duy nhất, đủ 15 bộ exercise/hint/solution, chỉ
  dùng cú pháp `$...$` và `$$...$$` cho toán Markdown, không có `quill.json`
  hoặc liên kết `.env` ngoài tệp bí mật gốc đã được git bỏ qua.
- Codex Slides không khả dụng trong phiên này do runtime Node.js 18 thấp hơn
  yêu cầu của gói (Node.js 20 trở lên). Vì vậy không tuyên bố đã rà bằng Codex
  Slides; toàn bộ kiểm tra hiển thị giai đoạn này được thực hiện bằng trình xem
  tài liệu cục bộ và Chromium.

## Giai đoạn II — đồng bộ deck với lecture note

### Kế hoạch và bản nháp

- Reader lập kế hoạch thành công với
  `requested_model=observed_model=deepseek/deepseek-v3.2`,
  `provider=OpenRouter`. Lượt trước đó đọc gói bảy tệp rồi dừng đúng lỗi
  `model exceeded the tool-call limit (8)`; lượt thành công dùng gói bốn tệp
  đã đóng băng và không đổi model.
- Writer dùng `requested_model=observed_model=z-ai/glm-5.3-flash`,
  `provider=OpenRouter`. Lượt đầu dừng `model exceeded the tool-call limit (10)`
  sau khi sửa HTML và một phần outline. Lượt phục hồi cùng model dừng
  `model exceeded the tool-call limit (8)` sau khi hoàn thiện D01 và bảng ánh
  xạ outline. Điều phối viên kiểm diff và hoàn tất phần metadata planning còn
  lại trước khi mở đợt review.
- A02, A08, A00 và ghi chú A03 dùng lại micro-example của note: hành động $a$
  cho giá trị 10, hành động $b$ với phần thưởng 0 cho $9{,}9$; câu hỏi đổi phần
  thưởng $b$ thành 2 cho nghiệm tự nhất quán 20/20.
- B08 thêm số chính sách xác định $\prod_s|\mathcal A(s)|$ và trường hợp chung
  $|\mathcal A|^{|\mathcal S|}$; vẫn giả sử đánh giá chính xác và phá hòa cố định.
- D01 phát biểu tính đơn điệu của $T^\pi,T_*$ với đúng lý do; D02 thêm phép tính
  $0{,}9^k100<1$, cho số lượt tối thiểu 44.
- Giữ nguyên 42 trang, 5 mạch, 120 phút và năm SVG. `bellman-choice.svg` chỉ mô
  tả quan hệ tổng quát, không chứa phần thưởng hoặc giá trị số nên không cần sửa.
- Outline và storyboard ánh xạ đủ 15 `note-topic-id` tới mọi `data-slide-id`.
  Các mã chỉ nằm trong HTML và planning, không hiển thị trên mặt trang hoặc
  trong ghi chú diễn giả.

Checkpoint này chưa được tính là đã qua năm báo cáo độc lập hoặc kiểm định
RevealJS. Các bước đó được thực hiện sau khi đóng băng bản nháp.
