# Storyboard Bài 04

Đã triển khai 45 slide theo kế hoạch 120 phút ngày 24-09-2026. Mã L04-S01–L04-S45 khớp HTML; kiểm định và lịch sử từng phần nằm trong review-log. Nội dung chi tiết, dữ kiện, nguồn, ghi chú và đáp án ở [outline.md](outline.md); phân tích nguồn ở [analysis.md](analysis.md).

## Bản đồ các phần và chức năng

| Phần | Loại | Đầu vào | Chức năng riêng | Đầu ra cho phần sau | Phút |
|---|---|---|---|---|---:|
| 1 | Mở đầu | Bài 03, tổng chiết khấu | Thiết lập bài toán và khoảng cách thưởng trước mắt–dài hạn | Nhu cầu tối ưu phần tiếp diễn | 10 |
| 2 | Khái niệm | Mô hình hai trạng thái, kỳ vọng | Phân biệt bảng ước lượng và giá trị tối ưu, tạo hai toán tử | $Q_v,T^\pi,T_*$ | 18 |
| 3 | Thuật toán dự đoán | $T^\pi$, chính sách cố định | Tính giá trị chính sách và đối chiếu hai lịch | Bảng $v^\pi$ dùng cải thiện | 17 |
| 4 | Khái niệm và thuật toán điều khiển | Giá trị chính sách | Tham lam, đánh giá lại và dừng ổn định | PI chính xác; giới hạn chi phí đánh giá đầy đủ | 23 |
| 5 | Thuật toán điều khiển | $T_*$, nhu cầu giảm chi phí | Cập nhật bảng trực tiếp, trích chính sách nhất quán | Dãy bảng và phần dư cần chứng nhận | 23 |
| 6 | Khái niệm và định lý | Các thuật toán đã thao tác được | Chứng nhận điểm đến, sai số và miền áp dụng | Ngưỡng dừng và điều kiện bảo đảm | 20 |
| 7 | Tổng hợp, kết luận | Các kết quả trước | Giải bài toán mở đầu và đánh giá một đầu ra | Năng lực chọn, tính và kiểm chứng; nhu cầu phi mô hình ở Bài 05 | 9 |

Không tách phần thực hành thứ tám: ứng dụng ở mỗi cụm giúp kiểm tra ngay cơ chế vừa học. 30 phút chữa bài theo quy ước học phần nằm ngoài 120 phút này; không dựng code demo.

## Chu trình từng cụm

| Cụm | Vấn đề | Trực giác | Ví dụ | Hình thức/quy trình | Ứng dụng | Kiểm tra | Dữ kiện truyền qua |
|---|---|---|---|---|---|---|---|
| Động lực (rút gọn) | 03 | 04 | 03–04 | Ôn công thức chiết khấu ở 04; không có khái niệm mới | 04–05 | 05 | Bốn cạnh mô hình, $\gamma=0{,}5$; ví dụ dẫn nhập làm rõ giới hạn thưởng tức thời |
| Bellman tối ưu | 06 | 06 | 07 | 08–11 | 10 và tính toán 12 | 12 | $Q_v$ từ bốn cạnh → phân biệt $q^\pi,q_*$ → kỳ vọng/max → toán tử |
| Đánh giá | 13 | 13 | 14–15 | 16 | 17 và 18 | 18 | $\pi_0=(a,a)$; nghiệm $(4,7)$; cùng khởi tạo 0 cho các lượt |
| Cải thiện/PI | 19 | 19–20 | 20–21 | 22–25 | Dùng quy trình 24 lần lại chuỗi ở 25; bước kế tiếp 26 | 26 | $q^{\pi_0}$ → $\pi_1$ → $v^{\pi_1}$ → $\pi_2$; không dùng bảng cũ làm giá trị mới |
| VI | 27 | 27–28 | 28–29 | 30–31 | 32–33 | 34 | Lưới tất định, bảng $v_k$, $w=T_*v$ và $\pi_v$ cùng bảng $v$ |
| Co/hội tụ/sai số | 35 | 35 | 35 | 36–37; chặn 38–39 | 38–40 | 41 | Khoảng cách 4 → 2; chuẩn vô cùng; phần dư và sai số của đúng bảng |
| Giới hạn (phụ) | 40 | 40 | CartPole ở 40 | Dùng lại giả thiết, không thêm thuật toán | 40,42 | 41 xét giả thiết; 45 xét chứng nhận | 324 ô chưa đồng nghĩa biết mô hình hoặc bảo đảm Markov |
| Kết luận (rút gọn) | Thu hồi 03–04 ở 43 | Bảng quyết định 42 | Dùng lại mô hình 43 | Không thêm hình thức mới | 43–44 | 45 | Chính sách $(b,b)$, giá trị $(9,20)$, phần dư và tiêu chuẩn ổn định |

Các bước được gộp có cùng nhiệm vụ tính hoặc giải thích; không tạo trang chỉ để gắn nhãn bước. Phần 1 và 7 không cần chu trình định nghĩa mới. Cụm giới hạn là ứng dụng của giả thiết đã học, không mở tuyến về lý thuyết rời rạc hóa.

**Ranh giới khái niệm–thuật toán:** Bellman tối ưu nhận diện đích; đánh giá là bài toán dự đoán; PI/VI là điều khiển có mô hình. Không gán các phương pháp này nhãn theo/khác chính sách của dữ liệu lấy mẫu vì nguồn dữ liệu ở đây là mô hình đầy đủ. Trạng thái kết thúc và ngân sách thuật toán là hai kiểu dừng khác nhau.

**Mức chứng minh:** 23 phác thảo cải thiện; 36 chứng minh bước co; 37 phát biểu Banach và phác thảo chặn trên/đạt cận, để quy nạp theo lịch sử ở ghi chú đọc thêm; 38–39 suy diễn chặn sai số. Thuật toán đầy đủ ở 16,24,31; các ví dụ tính tay đi trước. Chặn mất mát chính sách chuyển sang đọc thêm có ghi trong analysis.

## Lý do tồn tại và quyết định từng slide

Mỗi hàng chỉ bổ sung lý do và tác động biên tập; không thay đặc tả hình/công thức/câu hỏi trong outline. Cột vào–ra xác định slide liền trước/sau; nội dung cầu nối cụ thể ở từng mục outline.

| Mã | Tiêu đề | Lý do tồn tại / sản phẩm | Quyết định | Vào → ra | Phút |
|---|---|---|---|---|---:|
| L04-S01 | Giải MDP bằng quy hoạch động | Xác lập sản phẩm chính sách có căn cứ từ mô hình. | giữ/gộp: bảo toàn ý và bỏ lặp | Bài 03 → L04-S02 | 1 |
| L04-S02 | Nội dung bài giảng | Cho người học biết chuỗi năng lực phải đạt trước khi vào động lực. | giữ/gộp: bảo toàn ý và bỏ lặp | L04-S01 → L04-S03 | 2 |
| L04-S03 | Lập kế hoạch từ mô hình đã biết | Cung cấp một mô hình nhỏ dùng xuyên suốt, không bắt đầu bằng ký hiệu trừu tượng. | giữ/gộp: bảo toàn ý và bỏ lặp | L04-S02 → L04-S04 | 2 |
| L04-S04 | Phần thưởng trước mắt và dài hạn | Bộc lộ hạn chế của quyết định chỉ theo thưởng trước mắt. | thêm: làm rõ nhu cầu hoặc dữ kiện trước ký hiệu | L04-S03 → L04-S05 | 3 |
| L04-S05 | Câu hỏi: giá trị của một bước nhìn trước | Kiểm tra phép chiết khấu và dùng trạng thái kế tiếp đã học ở Bài 03. | thêm: kiểm tra ngay phần vừa học | L04-S04 → L04-S06 | 2 |
| L04-S06 | Hành động đầu và phần tiếp diễn | Tách hành động đầu khỏi chính sách tiếp diễn để chuẩn bị tối ưu. | thêm: làm rõ nhu cầu hoặc dữ kiện trước ký hiệu | L04-S05 → L04-S07 | 2 |
| L04-S07 | Điểm của hành động từ bảng giá trị | Biến bốn cạnh của ví dụ thành bảng điểm kiểm tra được. | thêm: làm rõ nhu cầu hoặc dữ kiện trước ký hiệu | L04-S06 → L04-S08 | 3 |
| L04-S08 | Giá trị tối ưu | Đặt tên đại lượng tối ưu và phân biệt với bảng hiện có. | giữ/gộp: bảo toàn ý và bỏ lặp | L04-S07 → L04-S09 | 3 |
| L04-S09 | Bellman tối ưu cho giá trị trạng thái | Chốt đúng thứ tự kỳ vọng môi trường rồi chọn hành động. | tách/sửa: giảm bước nhảy hoặc làm rõ giả thiết | L04-S08 → L04-S10 | 3 |
| L04-S10 | Giá trị hành động và chính sách tham lam | Nối giá trị hành động với hành động của chính sách cần tìm. | tách/sửa: giảm bước nhảy hoặc làm rõ giả thiết | L04-S09 → L04-S11 | 2 |
| L04-S11 | Hai toán tử Bellman | Tạo hai phép biến đổi bảng làm đầu vào cho thuật toán. | giữ/gộp: bảo toàn ý và bỏ lặp | L04-S10 → L04-S12 | 2 |
| L04-S12 | Câu hỏi: một cập nhật có phải nghiệm tối ưu | Phát hiện nhầm một cập nhật với điểm bất động tối ưu. | thêm: kiểm tra ngay phần vừa học | L04-S11 → L04-S13 | 3 |
| L04-S13 | Giá trị của chính sách cố định | Đặt bài toán dự đoán khi chính sách cố định. | giữ/gộp: bảo toàn ý và bỏ lặp | L04-S12 → L04-S14 | 2 |
| L04-S14 | Hai phương trình Bellman | Cho nghiệm chính xác làm chuẩn đối chiếu phương pháp lặp. | tách/sửa: giảm bước nhảy hoặc làm rõ giả thiết | L04-S13 → L04-S15 | 3 |
| L04-S15 | Đánh giá bằng các lượt quét | Thực hiện các lượt hữu hạn trước quy trình tổng quát. | tách/sửa: giảm bước nhảy hoặc làm rõ giả thiết | L04-S14 → L04-S16 | 3 |
| L04-S16 | Quy trình đánh giá chính sách | Đặc tả đánh giá, bảng trả, ngân sách và ý nghĩa ngưỡng. | tách/sửa: giảm bước nhảy hoặc làm rõ giả thiết | L04-S15 → L04-S17 | 4 |
| L04-S17 | Hai lịch cập nhật | Phân biệt một lượt đồng bộ với một lượt tại chỗ. | giữ/gộp: bảo toàn ý và bỏ lặp | L04-S16 → L04-S18 | 2 |
| L04-S18 | Câu hỏi: đánh giá chính sách | Kiểm tra sinh viên giữ đúng chính sách và đúng bảng cũ. | thêm: kiểm tra ngay phần vừa học | L04-S17 → L04-S19 | 3 |
| L04-S19 | Nhu cầu cải thiện chính sách | Bộc lộ một hành động có thể cải thiện quyết định đang dùng. | tách/sửa: giảm bước nhảy hoặc làm rõ giả thiết | L04-S18 → L04-S20 | 2 |
| L04-S20 | Cải thiện bằng một bước nhìn trước | Thực hiện tham lam ở cả hai trạng thái trên cùng bảng. | tách/sửa: giảm bước nhảy hoặc làm rõ giả thiết | L04-S19 → L04-S21 | 3 |
| L04-S21 | Đánh giá lại sau cải thiện | Khôi phục bước đánh giá lại bị lược giữa hai lần cải thiện. | tách/sửa: giảm bước nhảy hoặc làm rõ giả thiết | L04-S20 → L04-S22 | 3 |
| L04-S22 | Quy tắc cải thiện chính sách | Phát biểu quy tắc có xử lý hòa và cùng bảng tiếp diễn. | tách/sửa: giảm bước nhảy hoặc làm rõ giả thiết | L04-S21 → L04-S23 | 3 |
| L04-S23 | Định lý cải thiện chính sách | Giải thích vì sao cải thiện một bước dẫn tới cải thiện dài hạn. | tách/sửa: giảm bước nhảy hoặc làm rõ giả thiết | L04-S22 → L04-S24 | 3 |
| L04-S24 | Quy trình lặp chính sách | Ghép hai khâu thành thuật toán chính xác có thể lần theo. | tách/sửa: giảm bước nhảy hoặc làm rõ giả thiết | L04-S23 → L04-S25 | 4 |
| L04-S25 | Chính sách ổn định và dừng hữu hạn | Nối ổn định chính sách với hữu hạn và tối ưu. | giữ/gộp: bảo toàn ý và bỏ lặp | L04-S24 → L04-S26 | 2 |
| L04-S26 | Câu hỏi: kiểm tra bước cải thiện | Kiểm tra một lần đổi hành động và vai trò của quy tắc giữ hòa. | thêm: kiểm tra ngay phần vừa học | L04-S25 → L04-S27 | 3 |
| L04-S27 | Cập nhật từ bảng giá trị hiện có | Nêu nhu cầu giảm chi phí đánh giá rồi chuẩn bị lưới minh họa. | giữ/gộp: bảo toàn ý và bỏ lặp | L04-S26 → L04-S28 | 2 |
| L04-S28 | Một lượt quét trên lưới | Cho một lượt quét tự tính được trước ký hiệu lặp giá trị. | tách/sửa: giảm bước nhảy hoặc làm rõ giả thiết | L04-S27 → L04-S29 | 3 |
| L04-S29 | Giá trị lan dần từ đích | Thể hiện thông tin từ đích lan tới trạng thái xa. | tách/sửa: giảm bước nhảy hoặc làm rõ giả thiết | L04-S28 → L04-S30 | 3 |
| L04-S30 | Quy tắc lặp giá trị | Khái quát các lượt lưới thành phép lặp trên mô hình bất kỳ. | tách/sửa: giảm bước nhảy hoặc làm rõ giả thiết | L04-S29 → L04-S31 | 3 |
| L04-S31 | Quy trình lặp giá trị có kiểm tra dừng | Buộc ngưỡng, bảng trả và chính sách cùng có căn cứ đo được. | tách/sửa: giảm bước nhảy hoặc làm rõ giả thiết | L04-S30 → L04-S32 | 4 |
| L04-S32 | Trích chính sách từ cùng bảng giá trị | Thực hiện trích chính sách và tránh trộn hai bảng ở hai nhánh. | tách/sửa: giảm bước nhảy hoặc làm rõ giả thiết | L04-S31 → L04-S33 | 3 |
| L04-S33 | Chi phí của một lượt tính | So sánh đơn vị công việc, bộ nhớ và giới hạn mô hình. | giữ/gộp: bảo toàn ý và bỏ lặp | L04-S32 → L04-S34 | 2 |
| L04-S34 | Câu hỏi: tính lượt tiếp theo | Kiểm tra lan truyền, đồng bộ và việc xét toàn bảng. | thêm: kiểm tra ngay phần vừa học | L04-S33 → L04-S35 | 3 |
| L04-S35 | Khoảng cách giữa hai bảng giá trị | Tạo nhu cầu về chuẩn và tính co bằng hai bảng cụ thể. | thêm: làm rõ nhu cầu hoặc dữ kiện trước ký hiệu | L04-S34 → L04-S36 | 2 |
| L04-S36 | Tính co của toán tử Bellman | Chứng minh tính co với giả thiết đủ, không dựa vào ví dụ. | tách/sửa: giảm bước nhảy hoặc làm rõ giả thiết | L04-S35 → L04-S37 | 3 |
| L04-S37 | Điểm bất động và chính sách tối ưu | Nhận diện điểm bất động là giá trị tối ưu và dựng chính sách đạt nó. | tách/sửa: giảm bước nhảy hoặc làm rõ giả thiết | L04-S36 → L04-S38 | 4 |
| L04-S38 | Hội tụ hình học của lặp giá trị | Định lượng hội tụ và bộc lộ việc chưa biết sai số thật. | tách/sửa: giảm bước nhảy hoặc làm rõ giả thiết | L04-S37 → L04-S39 | 3 |
| L04-S39 | Phần dư Bellman và ngưỡng dừng | Biến phần dư tính được thành một ngưỡng có ý nghĩa. | tách/sửa: giảm bước nhảy hoặc làm rõ giả thiết | L04-S38 → L04-S40 | 3 |
| L04-S40 | Giới hạn của mô hình dạng bảng | Áp dụng lại giả thiết vào trường hợp rời rạc hóa CartPole. | giữ/gộp: bảo toàn ý và bỏ lặp | L04-S39 → L04-S41 | 2 |
| L04-S41 | Câu hỏi: kiểm tra sai số và giả thiết | Kiểm tra chặn sai số và giới hạn của chứng minh khi đổi giả thiết. | thêm: kiểm tra ngay phần vừa học | L04-S40 → L04-S42 | 3 |
| L04-S42 | Chọn quy trình theo đầu ra cần tính | Tổng hợp chọn quy trình theo đầu vào, đầu ra và chi phí. | giữ/gộp: bảo toàn ý và bỏ lặp | L04-S41 → L04-S43 | 2 |
| L04-S43 | Lời giải cho bài toán mở đầu | Khép vấn đề mở đầu bằng chính sách và chứng nhận Bellman. | tách/sửa: giảm bước nhảy hoặc làm rõ giả thiết | L04-S42 → L04-S44 | 2 |
| L04-S44 | Bài tập và tài liệu đọc | Giao sản phẩm tự học có nguồn và đúng kiến thức đã chuẩn bị. | giữ/gộp: bảo toàn ý và bỏ lặp | L04-S43 → L04-S45 | 2 |
| L04-S45 | Câu hỏi: đánh giá một kết quả lập kế hoạch | Đánh giá khả năng nối thuật toán, sai số và chứng nhận chính sách. | thêm: kiểm tra ngay phần vừa học | L04-S44 → Tự học / Bài 05 | 3 |

## Rà lại ranh giới sau đổi cấu trúc

- Mở đầu 01–07: giữ đúng giới thiệu → nội dung → động lực; 05 kiểm tiên quyết, không hỏi công thức tối ưu chưa dạy.
- 10–15: hoàn tất hai toán tử rồi chuyển sang giữ chính sách cố định; ví dụ đánh giá không bị gọi tối ưu.
- 16–21: ngưỡng đánh giá và cập nhật tại chỗ được phân biệt trước khi đổi chính sách; 19–21 làm rõ phần tiếp diễn cũ và đánh giá lại.
- 24–29: PI chính xác kết thúc bằng kiểm tra, rồi lưới giải quyết nhu cầu giảm chi phí; không đổi ngầm sang đánh giá PI bị cắt.
- 32–37: trích chính sách, chi phí và kiểm tra đi trước chuẩn/co; ví dụ khoảng cách đứng trước định lý.
- 38–43: phần dư áp dụng cho đúng bảng, CartPole kiểm giả thiết; kết luận dùng kết quả cũ, không đưa thuật toán mới.
- 43–45: lời giải trở lại vấn đề mở đầu; bài tập chỉ dẫn sản phẩm; câu cuối phân biệt gần đúng giá trị với tối ưu chính sách.

Số slide 45; tổng thời gian 120 phút; các slide kiểm tra 05,12,18,26,34,41,45. Mọi thay đổi so với 38 trang NG1 có ánh xạ trong analysis. Các kiểm tra ở đây là kiểm định kế hoạch, không phải kiểm định hiển thị HTML.

Rà sau góp ý độc lập: slide 16 dùng chênh lệch lớn nhất trước khi gọi tên chuẩn; 22 chuẩn bị tính đơn điệu cho 23; 24 trả đúng cặp chính sách–giá trị khi hết ngân sách; 31 ghi rõ cả hai nhánh trả; 37 dành chứng minh theo lịch sử cho đọc thêm; 38 ghi rõ dữ kiện minh họa. Các thay đổi này không đổi thứ tự hay thời lượng.

## Phân tích cách thể hiện khi triển khai — 24-09-2026

Phân tích dưới đây cụ thể hóa dàn bài cho khung 1280 × 720. Hai báo cáo reader có quyết định hình thức hữu ích nhưng lẫn ngôn ngữ; điều phối viên không dùng nguyên văn và biên tập lại toàn bộ bảng. Công thức và bảng số được dựng bằng KaTeX/HTML, sơ đồ bằng SVG. Các chỉ dẫn trong bảng chỉ dành cho công việc soạn; nội dung trình chiếu và ghi chú diễn giả dùng lời giảng trực tiếp.

| Mã | Cách thể hiện | Lý do sư phạm và phân chia nội dung |
|---|---|---|
| L04-S01 | Tên bài lớn, học phần và học kỳ; một dòng mô hình → giá trị → chính sách. | Xác định đầu vào và sản phẩm trước thuật toán; diễn giải quan hệ với Bài 03 trong ghi chú. |
| L04-S02 | Sáu mục ngắn chia hai cột, kèm ba năng lực: tính, cải thiện, kiểm chứng. | Mục lục cho biết các thao tác sẽ học, chưa đưa ký hiệu mới. |
| L04-S03 | SVG hai nút, bốn cạnh có hướng và nhãn hành động/thưởng; hệ số chiết khấu ở ngoài hình. | Một mô hình nhỏ dùng xuyên suốt giúp giảm số dữ kiện phải nhớ; cách đọc cạnh nằm trong lời giảng. |
| L04-S04 | Hai hàng chuỗi thưởng cùng mốc thời gian; hai tổng chiết khấu bằng KaTeX. | So trực tiếp thưởng trước mắt với tổng dài hạn; nguồn gốc số 4 và 9 được giải thích trong ghi chú. |
| L04-S05 | Một cạnh chuyển và bảng tiếp diễn đã cho; câu hỏi riêng, đáp án hiện sau. | Kiểm tra chọn đúng trạng thái kế tiếp và đặt hệ số chiết khấu. |
| L04-S06 | Cây một bước tách hành động đầu khỏi phần tiếp diễn. | Sinh viên nhận ra hai quyết định cần tối ưu trước khi đọc định nghĩa; lời giảng phân biệt lựa chọn và ngẫu nhiên. |
| L04-S07 | Bảng hai trạng thái × hai hành động, cạnh đó một phép tính mẫu. | Từ bốn cạnh mô hình tạo bảng điểm; công thức tổng quát được nối với từng thành phần của phép tính. |
| L04-S08 | Hai định nghĩa ngắn cho giá trị trạng thái và hành động, rồi quan hệ cực đại. | Phân biệt đối tượng tối ưu và hành động đầu cố định; giải thích supremum bằng lời, chưa chứng minh tồn tại. |
| L04-S09 | Công thức Bellman lớn; sơ đồ nhỏ kỳ vọng theo chuyển → cực đại theo hành động. | Thứ tự hai phép toán là trọng tâm; phép suy diễn dài ở ghi chú. |
| L04-S10 | Công thức cho giá trị hành động và dòng chọn chính sách bên dưới. | Tách giá trị cực đại với hành động đạt cực đại; điều kiện hữu hạn và chính sách tối ưu có trong lời giảng. |
| L04-S11 | Hai cột nhận cùng bảng giá trị: trung bình theo chính sách và cực đại theo hành động. | Hai toán tử là hai phép biến đổi bảng; quan hệ điểm bất động được diễn giải sau ví dụ. |
| L04-S12 | Bảng điểm có đủ dữ kiện, hai ô đầu ra để tính và một câu về điểm bất động. | Kiểm tra một lượt tối ưu chưa có nghĩa bảng đầu vào đã tối ưu. |
| L04-S13 | Mô hình hai trạng thái với hai cạnh của chính sách cố định được đánh dấu. | Xác định đường đi trước khi lập hệ; các cạnh còn lại chỉ là lựa chọn chưa dùng. |
| L04-S14 | Hai phương trình song song với hai trạng thái; nghiệm hiện ở cuối. | Sinh viên lần từ cạnh đến phương trình, rồi tự kiểm số 7; phép biến đổi chi tiết nằm trong ghi chú. |
| L04-S15 | Bảng các lượt từ 0, cạnh nghiệm chính xác để đối chiếu. | Thấy xấp xỉ tiến dần trước giả mã; một ô mẫu làm rõ mọi cập nhật dùng bảng cũ. |
| L04-S16 | Danh sách bước có thứ tự và nhánh trả, công thức thay đổi lớn nhất ở một khối riêng. | Giữ thuật toán đủ để thực hiện; chặn sai số hoãn đến phần 6, không dồn vào mặt slide. |
| L04-S17 | Hai bảng cùng khởi tạo, mũi tên cho thấy dữ liệu cũ hoặc giá trị vừa cập nhật. | Tác động của thứ tự được kiểm bằng cùng hai trạng thái; điều kiện hội tụ giải thích trong ghi chú. |
| L04-S18 | Bảng lượt trước và câu hỏi tính lượt tiếp; đáp án ẩn. | Đo khả năng giữ chính sách và dữ liệu đầu vào, đồng thời giải thích việc không lấy cực đại. |
| L04-S19 | Một ô giá trị hành động đặt cạnh giá trị chính sách tại cùng trạng thái. | Bất đẳng thức 13,5 > 7 tạo nhu cầu thay hành động; lời giảng phân biệt chấm điểm với đánh giá chính sách mới. |
| L04-S20 | Bảng hai hàng đánh dấu hành động được chọn, bên dưới là chính sách mới. | Cải thiện được thực hiện ở mọi trạng thái từ cùng bảng cũ. |
| L04-S21 | Bảng ba chính sách và ba cặp giá trị, nối từng lần đánh giá–cải thiện. | Hiện rõ bước đánh giá lại đã bị lược trong nguồn; tính mẫu giá trị 20 của $v^{\pi_1}(s_1)$ trong ghi chú. |
| L04-S22 | Quy tắc tham lam cùng hai trường hợp giữ hoặc đổi hành động khi hòa. | Cách xử lý hòa có vai trò thuật toán; tính đơn điệu được chuẩn bị bằng một lập luận ngắn trong lời giảng. |
| L04-S23 | Phát biểu định lý, chuỗi bất đẳng thức ngắn và điều kiện đuôi chiết khấu mất đi. | Thấy bước từ cải thiện một hành động đến giá trị dài hạn; khai triển đầy đủ ở ghi chú. |
| L04-S24 | Các bước đánh giá chính xác → cải thiện → kiểm ổn định, kèm hai nhánh trả. | Có thể lần theo ví dụ mà không trộn chính sách mới với giá trị cũ; chi tiết ngân sách được giải thích bằng lời. |
| L04-S25 | Chuỗi chính sách không lặp và công thức số chính sách hữu hạn. | Nối hai căn cứ: cải thiện nghiêm ngặt và tập hữu hạn; việc giữ hòa gắn trực tiếp với dừng. |
| L04-S26 | Bảng hai hành động cần điền và câu hỏi về hòa. | Dùng lại mô hình để kiểm cơ chế thay hành động, không tạo một bài toán mới. |
| L04-S27 | SVG lưới năm ô, đích và thưởng ghi trên đúng cạnh. | Mô hình cho phép thấy tác động của khoảng cách tới đích; quy ước biên và kết thúc nói rõ. |
| L04-S28 | Hai hàng bảng giá trị trước/sau một lượt, một phép tính tại ô sát đích. | Giải thích tính đồng bộ bằng thông tin truyền từ hàng cũ sang hàng mới. |
| L04-S29 | Bảng năm cột qua bốn lượt, viền đánh dấu ô vừa nhận ảnh hưởng của thưởng đích. | Nhìn thấy thông tin lan từng bước; lời giảng phân biệt điểm bất động của ví dụ với hội tụ chung. |
| L04-S30 | Phép tính ở ô cụ thể cạnh công thức tổng quát. | Ánh xạ dữ kiện quen thuộc sang ký hiệu; chỉ số lượt tính được phân biệt với thời gian tương tác. |
| L04-S31 | Các bước tính bảng điểm, lấy cực đại, trích chính sách, đo phần dư và trả kết quả. | Giữ cùng bảng đầu vào cho mọi nhánh; hai điều kiện dừng thể hiện tường minh, không giấu trong mã dài. |
| L04-S32 | Hai điểm hành động tại một ô và hành động được chọn từ cùng bảng giá trị. | Phân biệt phép nhìn trước từ bảng với giá trị thật của chính sách vừa trích. |
| L04-S33 | Bảng so sánh thao tác và chi phí của hai thuật toán. | So cùng đơn vị công việc thay vì nhận xét nhanh/chậm; bộ nhớ và mô hình thưa ở ghi chú. |
| L04-S34 | Hàng giá trị đã cho, hai ô cần điền và câu về tiêu chí toàn bảng. | Kiểm cả thao tác đồng bộ lẫn sai lầm kết luận từ một ô không đổi. |
| L04-S35 | Hai cặp bảng trước/sau và hàng chênh lệch lớn nhất. | Chuẩn vô cùng xuất hiện như cách đo tự nhiên; ví dụ co đi trước phát biểu định lý. |
| L04-S36 | Ba dòng suy diễn hiện lần lượt: chênh cực đại, kỳ vọng, hệ số chiết khấu. | Bước dùng xác suất và hệ số nhỏ hơn 1 có thể theo được trên lớp; khai triển từng tổng ở ghi chú. |
| L04-S37 | Phát biểu điểm bất động và hai khối: chặn mọi chính sách, chính sách tham lam đạt cận. | Tách tồn tại nghiệm với việc nghiệm ấy tối ưu; quy nạp theo lịch sử nằm trong ghi chú đọc thêm. |
| L04-S38 | Đồ thị SVG chặn lý thuyết với trục ghi rõ, mốc 7 và ngưỡng 1. | Đường cong diễn giải tốc độ hình học; chặn ban đầu 64 được ghi là giả định minh họa. |
| L04-S39 | Phần dư đo được, một bước tam giác–co và chặn sai số; ví dụ ngưỡng ở cuối. | Nối bảo đảm với quyết định dừng thực tế; chặn cho bảng mới của đánh giá chính sách nằm trong ghi chú. |
| L04-S40 | SVG trạng thái liên tục → ô gộp → mô hình chuyển/thưởng, cạnh bảng số khoảng. | Phân biệt có biểu diễn hữu hạn với có mô hình Markov; hai điểm trong một ô minh họa thông tin bị gộp. |
| L04-S41 | Hai thẻ dữ kiện cho hệ số 0,5 và 1; câu tính chặn và kiểm giả thiết. | Đo khả năng áp dụng công thức trong đúng miền, không chỉ thay số máy móc. |
| L04-S42 | Bảng ba hàng: đánh giá, lặp chính sách, lặp giá trị; đầu vào và tiêu chí dừng. | Dùng yêu cầu bài toán để chọn phương pháp; nối nhu cầu học từ trải nghiệm trong ghi chú. |
| L04-S43 | Mô hình mở đầu cạnh bảng giá trị hành động tối ưu và phép kiểm Bellman. | Thu hồi quyết định ban đầu bằng cả chính sách đạt được lẫn chứng nhận toán học. |
| L04-S44 | Ba dòng bài tập gắn với sản phẩm cụ thể và tài liệu đọc. | Sinh viên biết phải tự tính hoặc chứng minh điều gì; không đưa lời giải dài hoặc kiến thức chưa dạy. |
| L04-S45 | Phiếu kết quả có phần dư và chính sách, kèm ba câu đánh giá kết luận. | Kiểm việc phân biệt sai số giá trị, tối ưu chính sách và chứng nhận ổn định của lặp chính sách. |

Bộ số mới ngày 24-09-2026 theo yêu cầu người dùng: hai trạng thái dùng thưởng 2/−1/5/10 và hệ số0,5; lưới dùng thưởng −1/24 và cùng hệ số. Mọi thay tham số được ghi ở analysis mục6 và outline; không đổi mạch, số slide hoặc thời lượng.

## Quyết định bố cục sau triển khai

Các quyết định dưới đây cụ thể hóa hoặc thay phương án hình ban đầu sau khi kiểm khung 1280×720 và 960×540; không đổi thứ tự 45 trang, nội dung toán học hay thời lượng.

| Slide | Cách thể hiện cuối | Lý do và ảnh hưởng |
|---|---|---|
| 01 | Tiêu đề, đầu vào và đầu ra; bỏ sơ đồ lặp | Dành diện tích cho tên bài và nhiệm vụ |
| 06 | Cây SVG một bước, toàn chiều ngang | Hai nhánh dùng cùng quy ước phần tiếp diễn; nhãn đủ lớn |
| 08–11 | Định nghĩa, công thức KaTeX và các thẻ ngắn | Bỏ sơ đồ lặp lại cùng công thức; giữ một luận điểm/trang |
| 13 | SVG chỉ giữ hai cạnh của chính sách luôn a | Phân biệt mô hình đầy đủ với mô hình theo chính sách |
| 16,24,31 | Quy trình bốn bước HTML, đủ các nhánh trả | Công thức đọc được; tránh đặt ký hiệu vào SVG hoặc ba cột chật |
| 19–21 | Thẻ so sánh và bảng chính sách–giá trị | Nhãn phân biệt giá trị 7, điểm nhìn trước 13,5 và giá trị mới 20 |
| 28–29,34 | Bảng HTML có trạng thái và chỉ số lượt | Không dùng màu làm tín hiệu duy nhất; đọc số từ đúng bảng cũ |
| 36–37 | Công thức lớn, hai nhánh lập luận; chứng minh chi tiết trong notes | Tách trực giác, định lý và suy diễn; giữ mức năm 3 |
| 38 | Đồ thị SVG từ Matplotlib, trục tung logarit cơ số 2, nhãn 24 đơn vị | Cả mốc 1 và 0,5 đọc rõ; 64 là giả định minh họa độc lập |
| 40 | Hai thẻ dữ kiện và SVG gộp trạng thái; bỏ caption lặp | Công thức 324 ở KaTeX, không chồng chân trang |
| 42–45 | Bảng tổng hợp rộng, lời giải có nhãn đại lượng, bài tập và câu hỏi cuối | Thu hồi bài toán mở đầu; giữ công thức cùng giá trị khi xuống dòng |

Ghi chú 29/34 bổ sung tên ô nguồn của từng bảng sau khi reviewer nhầm lượt; số đúng không đổi. Các nguồn có tham số điều chỉnh được ghi rõ trong notes. Bảy slide kiểm tra vẫn là 05/12/18/26/34/41/45; đáp án hiện sau câu hỏi hoặc nằm trong notes. Không thêm code demo, notebook, khái niệm trọng tâm mới hoặc phần thứ tám.
