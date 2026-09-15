# Rà từng slide Bài 02: tiên quyết và mạch khái niệm

- Ngày rà: 2026-09-16.
- Bản được rà: [Giao diện tác tử–môi trường](../../lecture-02-giao-dien-tac-tu-moi-truong.html), tại commit `202d9f7`.
- SHA-256 HTML: `3598b918e6ea362cd60e978015bc6623a6e4a7f8e6d498591f1429370840b1cc`.
- Phạm vi: **47/47 slide, 7 section chính**, gồm trang mở phần và 5 trang bài tập; đọc mặt slide, ghi chú diễn giả và 11 SVG được tham chiếu. Đã duyệt bản RevealJS trong Chromium ở 1280 × 720 và xem ảnh của từng trang.
- Đây là báo cáo đề xuất; chưa sửa HTML, SVG hoặc thứ tự bài giảng.

## 1. Kết luận

Bảy mạch lớn có thứ tự hợp lý: định hướng → giao diện tương tác → tín hiệu học → thông tin và tính Markov → chính sách, giá trị, mô hình → mê cung → tổng kết. **Không cần đảo toàn bộ bài.** Các chỗ cần sửa nằm chủ yếu trong từng cụm: ký hiệu đến trước lời giải thích, ví dụ đứng sau công thức, và phần tổng hợp chưa sử dụng đủ các khái niệm vừa dạy.

Ưu tiên đầu tiên là **D04**: người học được yêu cầu tính với $\gamma$ trước khi biết ý nghĩa của hệ số này. Tiếp theo là **C06**, **D05–D06**, **D07–D10** và **E05**. Trang mở phần mới giúp định vị chủ đề, nhưng chưa giải quyết các cầu nối còn thiếu bên trong phần.

Báo cáo có **13 nhóm phát hiện**, không đồng nghĩa 13 lỗi toán học. Mức “nghiêm trọng” dùng cho bước học quan trọng bị thiếu; “trung bình” cho cầu nối, ví dụ hoặc quy ước chưa rõ. Các điểm nhẹ và những nhận xét không được chứng cứ xác nhận được ghi riêng.

Không coi tên khái niệm trong mục tiêu, bản đồ hoặc giới thiệu bài sau là lỗi “đột ngột”. Không dùng số thứ tự ID để suy ra thứ tự dạy. Bảng thuật ngữ trong outline không thay cho lời giới thiệu trên slide; ghi chú có giải thích được ghi nhận, nhưng người tự học từ mặt slide chưa chắc nhìn thấy.

## 2. Nhật ký duyệt đủ 47 slide

Cột “Vị trí” là số ngang.dọc của RevealJS, tính từ 1. Liên kết mở đúng trang trong HTML. “Giữ” nghĩa là không thấy lỗi mạch cần sửa tại trang đó, không phải chứng nhận mọi khía cạnh của bài.

| STT | Vị trí | ID và tiêu đề | Khái niệm / vai trò được kiểm tra | Kết luận và hướng xử lý |
|---:|---|---|---|---|
| 1 | 1.1 | [P00 — Giao diện tác tử–môi trường](../../lecture-02-giao-dien-tac-tu-moi-truong.html#/1/1) | Phạm vi bài: giao diện trước mô hình quyết định đầy đủ. | Giữ. Trang bìa định hướng phạm vi, không đòi hỏi biết MDP. |
| 2 | 1.2 | [P01 — Mục tiêu học tập](../../lecture-02-giao-dien-tac-tu-moi-truong.html#/1/2) | Chuỗi mục tiêu quan sát–trạng thái–Markov–vai trò–mê cung. | Giữ. Nêu tên điều sẽ học là hợp lý. |
| 3 | 1.3 | [P02 — Bản đồ nội dung](../../lecture-02-giao-dien-tac-tu-moi-truong.html#/1/3) | Bản đồ 7 mạch; ghi chú mô tả quan hệ giữa các vai trò. | Giữ bản đồ; chỉnh câu notes gộp chính sách, giá trị và mô hình cùng “quyết định cách chọn hành động”, xem mục 4. |
| 4 | 2.1 | [A-TITLE — Giao diện tương tác](../../lecture-02-giao-dien-tac-tu-moi-truong.html#/2/1) | Mở vòng quan sát–hành động–phản hồi. | Giữ; câu dẫn phù hợp A00–A04. |
| 5 | 2.2 | [A00 — Ranh giới tác tử–môi trường](../../lecture-02-giao-dien-tac-tu-moi-truong.html#/2/2) | Ranh giới hai phía; SVG bắt đầu dùng ký hiệu. | F01: giải nghĩa $O_t,R_{t+1}$ cùng ký hiệu hành động ngay tại lần đầu. |
| 6 | 2.3 | [A02 — Giao diện tại bước $t$](../../lecture-02-giao-dien-tac-tu-moi-truong.html#/2/3) | Chỉ số $t$ và $t+1$. | F01: đặt chú giải trước công thức; làm rõ phản hồi gồm thưởng và quan sát. |
| 7 | 2.4 | [A03 — Lịch sử tương tác có thứ tự](../../lecture-02-giao-dien-tac-tu-moi-truong.html#/2/4) | Lịch sử $H_t$ và dữ liệu kế tiếp. | Mặt slide nối tốt với A02; ghi chú đi trước sang lịch sử trạng thái/Markov, xem F03 và mục 4. |
| 8 | 2.5 | [A04 — Kiểm tra chỉ số](../../lecture-02-giao-dien-tac-tu-moi-truong.html#/2/5) | Vận dụng quy ước chỉ số. | Giữ câu hỏi; fragment thực sự ẩn đáp án. Có thể nói rõ phép nối lịch sử, mục 4. |
| 9 | 3.1 | [B-TITLE — Tín hiệu học và phần thưởng](../../lecture-02-giao-dien-tac-tu-moi-truong.html#/3/1) | Nguồn tín hiệu và thưởng trễ. | Giữ; không thêm định nghĩa hình thức ở trang mở. |
| 10 | 3.2 | [B00 — Ba nguồn tín hiệu học](../../lecture-02-giao-dien-tac-tu-moi-truong.html#/3/2) | Ba nguồn tín hiệu trong SVG. | Đủ ba dạng học. Chỉnh nhãn “tương tác + thưởng trễ” để tránh hiểu trễ là điều kiện bắt buộc, mục 4. |
| 11 | 3.3 | [B02 — Dữ liệu phụ thuộc hành động](../../lecture-02-giao-dien-tac-tu-moi-truong.html#/3/3) | Chính sách, quỹ đạo, dữ liệu phụ thuộc hành động. | F02: thuật ngữ chính sách/quỹ đạo cần một lời giải nghĩa ngắn tại đây. |
| 12 | 3.4 | [B03 — Phản hồi trễ](../../lecture-02-giao-dien-tac-tu-moi-truong.html#/3/4) | Chuỗi trạng thái và quy công trạng theo thời gian. | F02: SVG dùng $S_0,\ldots,S_3$ trước C00; ghi đây là trạng thái môi trường. |
| 13 | 3.5 | [B04 — Giả thuyết phần thưởng](../../lecture-02-giao-dien-tac-tu-moi-truong.html#/3/5) | Giả thuyết phần thưởng, tổng tương lai. | Giữ vị trí. Đã hẹn hình thức hóa sau; không cần đưa công thức $G_t$ lên sớm. |
| 14 | 3.6 | [B05 — Nhận dạng bài toán](../../lecture-02-giao-dien-tac-tu-moi-truong.html#/3/6) | Phân biệt nhãn trực tiếp với tương tác có thưởng. | Giữ. Kết nối B00–B02 và mở nhu cầu mô tả thông tin. |
| 15 | 4.1 | [C-TITLE — Trạng thái, quan sát và tính Markov](../../lecture-02-giao-dien-tac-tu-moi-truong.html#/4/1) | Mở ba tầng thông tin và tính Markov. | Giữ; tiêu đề bao phủ nội dung. |
| 16 | 4.2 | [C00 — Ba tầng thông tin](../../lecture-02-giao-dien-tac-tu-moi-truong.html#/4/2) | Miền $\mathcal S,\mathcal O,\mathcal X$ và vai trò $S,O,X$. | Giữ. Ví dụ xe trong notes hữu ích; không cần định nghĩa Markov trước ví dụ C02. |
| 17 | 4.3 | [C02 — Ví dụ: vị trí chưa đủ](../../lecture-02-giao-dien-tac-tu-moi-truong.html#/4/3) | Vị trí chưa đủ khi vận tốc ảnh hưởng bước kế. | Giữ trước C03. F03: dùng ví dụ này để phát biểu tiêu chuẩn bằng lời trước xác suất. |
| 18 | 4.4 | [C03 — Tính Markov theo trạng thái và hành động](../../lecture-02-giao-dien-tac-tu-moi-truong.html#/4/4) | Lịch sử trạng thái, điều kiện hóa, tính Markov. | F03: thêm câu trực giác và phân biệt hai lịch sử trước công thức. |
| 19 | 4.5 | [C04 — Quan sát đầy đủ](../../lecture-02-giao-dien-tac-tu-moi-truong.html#/4/5) | Quan sát xác định trạng thái Markov; nhắc MDP. | F04: bỏ so sánh dựa vào thuật ngữ MDP chưa được giới thiệu; chỉ hẹn mô hình đầy đủ. |
| 20 | 4.6 | [C05 — Quan sát một phần](../../lecture-02-giao-dien-tac-tu-moi-truong.html#/4/6) | Quan sát một phần và tên POMDP. | F04: đi từ hai trạng thái cho cùng ảnh tới tên gọi; nối rõ với hình C04. |
| 21 | 4.7 | [C06 — Khôi phục thông tin cho quyết định](../../lecture-02-giao-dien-tac-tu-moi-truong.html#/4/7) | Lịch sử → biểu diễn → chính sách; niềm tin. | F05: $\pi(a\mid X_t)$ dùng trước D02; giải thích hoặc chuyển phần niềm tin vào notes. |
| 22 | 4.8 | [C07 — Kiểm tra khả năng quan sát](../../lecture-02-giao-dien-tac-tu-moi-truong.html#/4/8) | Phân loại theo thông tin tác tử nhận. | F13: tách cảm biến/quan sát khỏi biết mô hình và có bộ nhớ. |
| 23 | 5.1 | [D-TITLE — Chính sách, hàm giá trị và mô hình](../../lecture-02-giao-dien-tac-tu-moi-truong.html#/5/1) | Ba vai trò và hai bài toán dự đoán/điều khiển. | Giữ. Mở phần không cần dạy ngay cả năm tên. |
| 24 | 5.2 | [D00 — Ba vai trò của tác tử](../../lecture-02-giao-dien-tac-tu-moi-truong.html#/5/2) | Chính sách, giá trị, mô hình trong SVG. | F06: bỏ mũi tên khiến ba vai trò bị đọc thành chuỗi xử lý; lược ký hiệu giá trị chưa dạy. |
| 25 | 5.3 | [D02 — Chính sách chọn hành động](../../lecture-02-giao-dien-tac-tu-moi-truong.html#/5/3) | Chính sách tất định/ngẫu nhiên, tập hành động hợp lệ. | F07: đưa ví dụ hợp lệ trước hai công thức. |
| 26 | 5.4 | [D03 — Chính sách là một phân phối hợp lệ](../../lecture-02-giao-dien-tac-tu-moi-truong.html#/5/4) | Chuẩn hóa xác suất; phát hiện tổng 1,2. | F07: giữ bài kiểm tra sau ví dụ hợp lệ; nói rõ đang xét chính sách ngẫu nhiên. |
| 27 | 5.5 | [D04 — Phần thưởng tích lũy](../../lecture-02-giao-dien-tac-tu-moi-truong.html#/5/5) | Chính sách Markov, $\gamma$, $T$, $G_t$. | F08, ưu tiên cao nhất: giải nghĩa trọng số và tách đổi giả thiết khỏi định nghĩa tổng thưởng. |
| 28 | 5.6 | [D05 — Hàm giá trị trạng thái](../../lecture-02-giao-dien-tac-tu-moi-truong.html#/5/6) | Kỳ vọng có điều kiện và hàm giá trị. | F09: cho người học tính ví dụ D06 trước rồi đặt tên $v_\pi(s)$. |
| 29 | 5.7 | [D06 — Kỳ vọng gộp nhiều quỹ đạo](../../lecture-02-giao-dien-tac-tu-moi-truong.html#/5/7) | Hai kết quả với xác suất 0,7 và 0,3. | F09: phép tính đúng; chuyển phần dữ kiện lên trước định nghĩa giá trị, không cần thay số. |
| 30 | 5.8 | [D07 — Mô hình dự báo một bước](../../lecture-02-giao-dien-tac-tu-moi-truong.html#/5/8) | Ví dụ mô hình một bước trong mê cung. | F10: thêm quy ước tối thiểu ngay tại ví dụ, giải nghĩa $p$ trước số 1. |
| 31 | 5.9 | [D07B — Mô hình là phân phối có điều kiện](../../lecture-02-giao-dien-tac-tu-moi-truong.html#/5/9) | Phân phối chung và mô hình ước lượng $\hat p$. | Giữ sau D07. Đã có miền rời rạc, chuẩn hóa và phân biệt động lực thật/ước lượng. |
| 32 | 5.10 | [D10 — Mô hình dự báo cục bộ có điều kiện](../../lecture-02-giao-dien-tac-tu-moi-truong.html#/5/10) | Phạm vi mô hình, sai số, lập kế hoạch. | F11: bỏ đối tượng tranh luận “mô hình hoàn thiện về thế giới” chưa được đặt ra. |
| 33 | 5.11 | [D08 — Dự đoán và điều khiển](../../lecture-02-giao-dien-tac-tu-moi-truong.html#/5/11) | Dự đoán giữ chính sách; điều khiển cải thiện chính sách. | Giữ. F11 cần câu nối từ giới hạn mô hình trở lại hai nhiệm vụ này. |
| 34 | 5.12 | [D09 — Ghép đúng vai trò](../../lecture-02-giao-dien-tac-tu-moi-truong.html#/5/12) | Ghép phát biểu với chính sách/giá trị/mô hình. | Giữ câu hỏi. F10: ghi rõ tình huống chuyển tiếp ngẫu nhiên khác mê cung tất định. |
| 35 | 6.1 | [E-TITLE — Mô hình hóa bài toán mê cung](../../lecture-02-giao-dien-tac-tu-moi-truong.html#/6/1) | Mở ví dụ tổng hợp. | Giữ; lời hứa áp dụng cần được thực hiện đủ ở E05, xem F12. |
| 36 | 6.2 | [E00 — Mô hình hóa mê cung cố định](../../lecture-02-giao-dien-tac-tu-moi-truong.html#/6/2) | Tọa độ, hành động, thưởng, va tường, kết thúc. | Đã có quy ước trên mặt slide. F12: nối thưởng −1 với mục tiêu ít bước. |
| 37 | 6.3 | [E02 — Mỗi bước nối đúng chỉ số](../../lecture-02-giao-dien-tac-tu-moi-truong.html#/6/3) | Vận dụng chuyển tiếp và trường hợp va tường. | Giữ. Cùng chỉ số A02, quy ước E00; không có khái niệm mới đột ngột. |
| 38 | 6.4 | [E03 — Giao diện quan sát đổi kết luận](../../lecture-02-giao-dien-tac-tu-moi-truong.html#/6/4) | So sánh tọa độ với ảnh cục bộ. | Giữ; F13 cần nêu rõ biết trạng thái khác biết bản đồ/chuyển tiếp. |
| 39 | 6.5 | [E04 — Phân loại có điều kiện](../../lecture-02-giao-dien-tac-tu-moi-truong.html#/6/5) | Lập luận về nhập nhằng quan sát. | F13: kết luận dựa vào cặp trạng thái cùng ảnh; không suy ra chỉ từ thiếu bản đồ/bộ nhớ. |
| 40 | 6.6 | [E05 — Từ giao diện đến quyết định](../../lecture-02-giao-dien-tac-tu-moi-truong.html#/6/6) | Khép vòng lịch sử–biểu diễn–hành động–phản hồi. | F12: bổ sung một quyết định cụ thể, giá trị và dự báo trong mê cung; sửa “bốn trục”, mục 4. |
| 41 | 7.1 | [Z-TITLE — Tổng kết và bài tập](../../lecture-02-giao-dien-tac-tu-moi-truong.html#/7/1) | Mở tổng kết và bài tập. | Giữ; nối đúng từ ví dụ sang tự kiểm tra. |
| 42 | 7.2 | [Z00 — Tự kiểm tra và đọc tiếp](../../lecture-02-giao-dien-tac-tu-moi-truong.html#/7/2) | Thu hồi mục tiêu và giới thiệu Bài 03. | Giữ. Chuỗi Markov/MRP/Bellman là hẹn học sau, không yêu cầu vận dụng ở đây; xử lý viết tắt theo F04. |
| 43 | 7.3 | [X01 — Bài tập 1](../../lecture-02-giao-dien-tac-tu-moi-truong.html#/7/3) | So sánh ba dạng học và phản hồi trễ. | Đủ tiên quyết từ B. Giải thích trễ có thể xảy ra, không phải mọi thưởng đều trễ, mục 4. |
| 44 | 7.4 | [X02 — Bài tập 2](../../lecture-02-giao-dien-tac-tu-moi-truong.html#/7/4) | Tự đặc tả mê cung với hai giao diện quan sát. | Giữ; dựa trực tiếp E00–E04. F13 giúp tránh trộn trạng thái với quan sát. |
| 45 | 7.5 | [X05 — Bài tập 5](../../lecture-02-giao-dien-tac-tu-moi-truong.html#/7/5) | Tính hai tổng chiết khấu. | Giữ sau khi sửa F08. Đáp án $G_0=3,G_1=4$ đúng. |
| 46 | 7.6 | [X06 — Bài tập 6](../../lecture-02-giao-dien-tac-tu-moi-truong.html#/7/6) | Chuẩn hóa chính sách trên ba hành động. | Giữ sau D02–D03. Xác suất còn lại bằng 0,3; không xuất hiện thuật toán mới. |
| 47 | 7.7 | [X10 — Bài tập mở rộng 10](../../lecture-02-giao-dien-tac-tu-moi-truong.html#/7/7) | Mô hình hóa một bài toán tự chọn. | Giữ. Từ “tiếp diễn” cần lời giải thích ngắn trên mặt bài hoặc khi giao bài, mục 4. |

## 3. Phát hiện và hướng dẫn sửa

### F01 — Giải nghĩa quan sát và phần thưởng sau khi đã dùng ký hiệu

**Mức độ: trung bình. Vị trí: A00 → A02 → A03; phần giải nghĩa rõ của $O_t$ tới C00 mới xuất hiện.**

- **Bằng chứng:** `agent-environment-loop.svg` ghi “Hành động $A_t$” ở mũi tên đi và chỉ ghi “$R_{t+1},O_{t+1}$” ở mũi tên về. A02 tiếp tục bằng $A_t\longrightarrow(R_{t+1},O_{t+1})$. A03 đã yêu cầu đọc một dãy lịch sử. Ghi chú có gọi tên thưởng và quan sát, nhưng mặt slide chưa có chú giải tương ứng cho hai ký hiệu.
- **Khoảng trống:** người học phải tự đoán chữ nào là dữ liệu cảm biến, chữ nào là tín hiệu đánh giá. Điều này xảy ra trước cả câu hỏi kiểm tra chỉ số.
- **Sửa:** ngay A00 hoặc đầu A02, thêm ba nhãn: “$O_t$: quan sát nhận ở bước $t$”; “$A_t$: hành động chọn ở bước $t$”; “$R_{t+1}$: phần thưởng dạng số nhận sau hành động”. Trong SVG, đổi nhãn về thành “Phần thưởng $R_{t+1}$; quan sát $O_{t+1}$”. Không cần đưa phân biệt trạng thái–quan sát của C00 lên toàn bộ.
- **Kết nối sau sửa:** A00 xác định hai phía → A02 gọi tên dữ liệu và chỉ số → A03 ghép thành lịch sử → A04 kiểm tra đúng kỹ năng vừa học.

### F02 — “Chính sách”, “quỹ đạo” và trạng thái chen vào phần tín hiệu

**Mức độ: trung bình. Vị trí: B02–B03; đối chiếu D02 và C00.**

- **Bằng chứng:** B02 viết “phân phối dữ liệu có thể đổi khi chính sách đổi” và “thứ tự một quỹ đạo”. B03 dùng các nút $S_0,S_1,S_2,S_3$ trong `delayed-feedback.svg`, trong khi A03 vừa dùng $O_t$; C00 mới phân biệt $S_t$ với $O_t$.
- **Khoảng trống:** ba thuật ngữ đều hợp chủ đề, nhưng cần một câu giải nghĩa khi dùng để lập luận. Đây khác với việc chỉ liệt kê tên “chính sách” trong P01.
- **Sửa:** tại B02 viết “cách chọn hành động, gọi là chính sách” và “một chuỗi tương tác, gọi là quỹ đạo”. Tại B03 chú thích “Các nút là trạng thái môi trường $S_t$; tác tử nhận quan sát $O_t$ về trạng thái đó”. Không đổi tùy tiện $S$ thành $O$ vì hình đang mô tả diễn biến môi trường.
- **Câu nối:** “Các hành động tạo một chuỗi trạng thái; phần thưởng có thể chỉ đánh giá kết quả ở cuối chuỗi.” C00 sau đó mở rộng chính sự phân biệt vừa báo trước.

### F03 — Từ hai xe đến công thức Markov còn thiếu bước phát biểu bằng lời

**Mức độ: trung bình. Vị trí: C02 → C03; liên quan notes A03.**

- **Bằng chứng:** C02 đưa hai xe cùng vị trí nhưng khác vận tốc. C03 mở bằng “Đặt $\mathcal H_t^S=\ldots$”, điều kiện xác suất dương và đẳng thức xác suất chung của $S_{t+1},R_{t+1}$. Sự khác nhau giữa $H_t$ và $\mathcal H_t^S$ mới được giải thích trong notes C03.
- **Khoảng trống:** ví dụ đúng chỗ, nhưng câu “trạng thái là bản tóm tắt đủ của lịch sử” chưa được đặt lên mặt slide trước bộ ký hiệu mới. Người học phải đồng thời hiểu tiêu chuẩn Markov, đổi loại lịch sử và đọc điều kiện hóa.
- **Sửa theo thứ tự:**
  1. Giữ C02 trước C03. Chốt: “Khi đã biết trạng thái và hành động hiện tại, quá khứ không bổ sung thông tin để dự báo bước tiếp theo.”
  2. Nêu “$H_t$ chứa quan sát; $\mathcal H_t^S$ chứa trạng thái môi trường”. Dời đoạn so sánh dài trong notes A03 về đây.
  3. Đọc vế trái là dự báo khi biết cả lịch sử, vế phải là dự báo khi chỉ biết hiện tại; rồi mới hiển thị công thức đầy đủ.
- **Giả thiết cần làm rõ:** công thức theo xác suất tại từng giá trị phù hợp cách trình bày rời rạc. Ví dụ vị trí–vận tốc gợi biến liên tục; nói rõ đang dùng mô hình rời rạc hóa minh họa, hoặc để cách viết tổng quát cho phần nâng cao. Không khẳng định chỉ thêm vận tốc là đủ trong mọi mô hình xe; vẫn giữ giả thiết động lực trong notes C02.
- **Không nên sửa:** chuyển C02 xuống sau mô hình $p$ ở phần D. C02 đang cung cấp trực giác cần cho C03; chuyển xuống sẽ làm mất tiên quyết.

### F04 — Dùng MDP để sửa một hiểu nhầm trước khi người học biết MDP

**Mức độ: trung bình. Vị trí: C04–C05; liên quan Z00.**

- **Bằng chứng:** C04 viết “Quan sát đầy đủ chưa đủ để định nghĩa một MDP”. C05 bắt đầu bằng “Trong quá trình quyết định Markov quan sát một phần (POMDP)…”. P00/P01 và Z00 lại xác định định nghĩa đầy đủ mô hình quyết định thuộc Bài 03. MDP chưa được viết tên đầy đủ kèm viết tắt trên mặt slide trước khi dùng.
- **Điểm đứt:** C04 phản bác cách hiểu trong bản nguồn, nhưng sinh viên của bản hiện tại chưa được giới thiệu mệnh đề cần phản bác. C05 có mở rộng tên POMDP, nên không phải viết tắt hoàn toàn không giải thích; vấn đề là tên mô hình đứng trước trực giác quan sát ẩn.
- **Sửa:** C04 giữ định nghĩa quan sát đầy đủ; thay hộp dưới bằng “Bài 03 sẽ bổ sung tập hành động, động lực và phần thưởng để mô tả đầy đủ bài toán quyết định”. C05 mở bằng tình huống hai vị trí cho cùng ảnh cục bộ, nối với hình C04; sau khi nêu hệ quả mới giới thiệu POMDP như tên sẽ hình thức hóa sau. Khi giữ MDP trên slide, viết lần đầu “quá trình quyết định Markov (MDP)”.
- **Không cần thêm:** cả bộ định nghĩa MDP/POMDP hoặc phương trình Bellman vào phần C. Mục tiêu hiện tại là hiểu trạng thái, quan sát và biểu diễn.

### F05 — Công thức chính sách và trạng thái niềm tin xuất hiện trong bước khôi phục thông tin

**Mức độ: trung bình. Vị trí: C06, trước D02.**

- **Bằng chứng:** sơ đồ C06 kết thúc bằng “Chính sách $\pi(a\mid X_t)$”; danh sách nêu “cửa sổ quan sát, bộ nhớ hoặc trạng thái niềm tin”. Định nghĩa chính sách ngẫu nhiên tới D02 mới có. “Trạng thái niềm tin là phân phối…” chỉ nằm trong notes.
- **Khoảng trống:** luận điểm của C06 là giữ thông tin từ lịch sử, nhưng phải đọc ngay một phân phối chọn hành động và một loại biểu diễn xác suất chưa được chuẩn bị.
- **Sửa tối thiểu:** thay ô cuối bằng “Chọn hành động từ $X_t$”. Đưa ký hiệu $\pi(a\mid x)$ vào D02 như hiện tại. Với niềm tin, chọn một trong hai cách: chuyển tên này xuống notes vì chưa dùng tiếp; hoặc chú thích “phân phối xác suất trên các trạng thái có thể xảy ra” và minh họa hai vị trí cùng quan sát. Không thêm thuật toán cập nhật niềm tin trong bài này.
- **Kết nối:** C05 nêu nhập nhằng → C06 giải thích dùng lịch sử tạo biểu diễn → C07 kiểm tra thông tin → D02 định nghĩa cách chọn hành động từ biểu diễn đó.

### F06 — Hình ba vai trò có mũi tên dễ bị đọc thành một quy trình bắt buộc

**Mức độ: trung bình. Vị trí: D00, `rl-components.svg`.**

- **Bằng chứng thị giác:** hình đặt ba ô Chính sách → Hàm giá trị → Mô hình với mũi tên nối từ trái sang phải. Ô mô hình nét đứt và câu dưới nói mô hình là tùy chọn; ô giá trị đã có $v_\pi(s)$.
- **Điểm không nhất quán:** nội dung muốn phân biệt ba vai trò, còn mũi tên có thể gợi thứ tự xử lý “chọn hành động rồi đánh giá rồi mới dự báo môi trường”. Đây là nguy cơ từ cách biểu diễn, không phải khẳng định văn bản đang tuyên bố thuật toán sai.
- **Sửa:** dùng ba ô song song, bỏ mũi tên nối tuần tự; ghi mỗi ô một chức năng: chọn hành động / đánh giá kết quả tương lai / dự báo bước kế. Giữ nét đứt cho mô hình tùy chọn. Có thể bỏ $v_\pi(s)$ khỏi hình mở phần và đưa lại khi tới D05.
- **Lý do giữ D00:** một bản đồ vai trò trước định nghĩa là hữu ích. Không cần chuyển cả trang xuống sau mê cung; chỉ tránh để sơ đồ mở phần được hiểu là cơ chế vận hành đã học.

### F07 — Chính sách được hình thức hóa trước khi có một ví dụ hợp lệ

**Mức độ: trung bình. Vị trí: D02 → D03.**

- **Bằng chứng:** D02 mở bằng $\mathcal A(x)$ rồi đặt cạnh nhau $A_t=\pi(X_t)$ và $\pi(a\mid x)=\Pr(A_t=a\mid X_t=x)$. D03 lập tức kiểm tra phân phối có các xác suất $0{,}5;0{,}5;0{,}2$.
- **Khoảng trống:** trực giác “cách chọn hành động” đã có ở D00, nhưng ví dụ định lượng đầu tiên lại là một ví dụ sai. Chưa có bước nối một lựa chọn cụ thể với hai cách biểu diễn tất định/ngẫu nhiên.
- **Sửa:** đầu D02 dùng chính các hành động của D03, nêu tập hợp lệ rõ ràng và ví dụ hai hành động có xác suất $0{,}5;0{,}5$. Nói một lựa chọn cố định là trường hợp luôn chọn cùng hành động; sau đó mới viết hai công thức. Giữ tổng $1{,}2$ ở D03 để kiểm tra.
- **Chỉnh nhan đề D03:** “Chính sách ngẫu nhiên là phân phối hợp lệ”. Nếu muốn nói chính sách tất định cũng là phân phối suy biến, cần chỉ rõ xác suất 1 cho hành động được chọn.
- **Giới hạn kết luận:** từ câu hỏi D03 hiện tại chỉ chắc chắn tổng xác suất sai. Không kết luận hành động “nghĩ” không hợp lệ khi tập $\mathcal A(x)$ của tình huống chưa được cho.

### F08 — Chiết khấu, thời điểm kết thúc và đổi lớp chính sách dồn vào một trang

**Mức độ: nghiêm trọng về trình tự học. Vị trí: D04; ảnh hưởng D05–D09 và X05.**

- **Bằng chứng:** D04 bắt đầu bằng “chính sách Markov có dạng $\pi(a\mid s)$”, sau đó nói “tổng chiết khấu $-1-\gamma$” và yêu cầu tính với ba giá trị $\gamma$. Miền $\gamma\in[0,1]$ chỉ xuất hiện cùng công thức tổng cuối trang. Không có câu trên mặt slide giải thích trọng số của phần thưởng tương lai. $T$ cũng xuất hiện tại đây.
- **Khoảng trống:** câu hỏi số học được đặt trước ý nghĩa đại lượng. Người học có thể thế số đúng mà không hiểu chiết khấu. Giả thiết quan sát đầy đủ/chính sách Markov lại dễ bị hiểu là điều kiện cần để định nghĩa phần thưởng tích lũy trên một quỹ đạo.
- **Sửa theo thứ tự:**
  1. “$\gamma$ là trọng số tương đối của phần thưởng cách thêm một bước; $\gamma=1$ không giảm trọng số, $\gamma=0$ chỉ giữ phần thưởng kế tiếp.”
  2. Dùng hai thưởng $-1,-1$ đã có: $G_t=R_{t+1}+\gamma R_{t+2}=-1-\gamma$.
  3. Hỏi ba giá trị như hiện tại; giải thích kết quả $-1,-1{,}5,-2$ bằng trọng số, không chỉ phép thế.
  4. Nêu $T$ là thời điểm kết thúc quỹ đạo; viết tổng hữu hạn. Chuyển giả thiết $X_t=S_t$ và lớp chính sách sang đầu phần giá trị, nơi chúng thực sự dùng để viết $v_\pi(s)$.
- **Giải nghĩa “chính sách Markov”:** trong phạm vi đang dùng, chọn hành động từ trạng thái hiện tại thay vì toàn bộ lịch sử. Cách viết $\pi(a\mid s)$ không có chỉ số thời gian còn chọn trường hợp chính sách không đổi theo thời gian; không đồng nhất hai ý mà không nói rõ.
- **Điểm cần chốt trước khi sửa D05:** nếu $T$ là hạn cố định chung cho nhiệm vụ, giá trị nói chung còn phụ thuộc thời gian còn lại; dùng $v_{\pi,t}(s)$ hoặc đưa thời gian vào trạng thái. Nếu $T$ là thời điểm chạm trạng thái kết thúc trong mô hình dừng phù hợp, nói rõ cách hiểu đó. Báo cáo không khẳng định công thức hiện tại sai trong mọi cách hiểu; khoảng trống là thiếu quy ước nối giữa hai trang.
- **Bố cục:** ảnh duyệt D04 cho thấy công thức cuối sát mép dưới. Có thể tách trực giác/kiểm tra và công thức tổng thành hai trang; lấy thời gian trong cụm hiện có, không thu nhỏ chữ.

### F09 — Ví dụ làm rõ hàm giá trị nằm sau định nghĩa

**Mức độ: trung bình. Vị trí: D04 → D05 → D06.**

- **Bằng chứng:** D05 mở bằng $v_\pi(s)=\mathbb E_\pi[G_t\mid S_t=s]$. D06 mới cho hai kết quả $4,-1$ với xác suất $0{,}7,0{,}3$ và tính $2{,}5$.
- **Khoảng trống:** định nghĩa không sai vì dùng kỳ vọng; sinh viên đã có nền xác suất. Tuy nhiên ví dụ cụ thể giải thích nhu cầu “gộp nhiều quỹ đạo từ cùng một trạng thái” đến sau ký hiệu mà nó cần chuẩn bị.
- **Sửa:** sau $G_t$, đưa bảng dữ kiện D06 lên trước; yêu cầu tính trung bình có trọng số $0{,}7\cdot4+0{,}3\cdot(-1)=2{,}5$. Sau đó đặt tên kết quả là hàm giá trị và viết công thức D05. Nếu đổi thứ tự cả hai trang, sửa D06 để chưa dùng $v_\pi(s)$ trước lúc đặt tên.
- **Câu nối:** “Một quỹ đạo cho một tổng thưởng; cùng trạng thái và chính sách có thể sinh nhiều quỹ đạo. Ta cần một giá trị đánh giá trung bình.”
- **Không báo thành lỗi:** D05 đã giải thích kỳ vọng theo cả hành động của chính sách và chuyển tiếp của môi trường. Không cần thêm lại cùng một câu chỉ vì ký hiệu $\mathbb E_\pi$ có chỉ số $\pi$.

### F10 — Ví dụ mô hình dựa một phần vào mê cung sắp được dạy

**Mức độ: trung bình. Vị trí: D07 → D07B; D09 → E00.**

- **Bằng chứng:** D07 có dòng “mê cung lưới ở cuối bài, chuyển tất định, mỗi chuyển tiếp nhận $-1$” và chuyển $(2,1)$ sang $(3,1)$ bằng hành động Đông; E00 mới có trục tọa độ và bản đồ. D07 viết $p(\ldots)=1$ trước định nghĩa tổng quát D07B. D09 lại dùng “xác suất $0{,}1$ va tường”; chỉ notes nói đó là tình huống ngẫu nhiên khác.
- **Đánh giá:** D07 đã cho một phần quy ước, nên không thể kết luận “hoàn toàn không có bối cảnh” hoặc bắt buộc chuyển cả section E lên trước. Dùng ví dụ trước định nghĩa là đúng hướng; thiếu là chú giải cục bộ và tín hiệu đổi tình huống.
- **Sửa D07:** thêm hình hai ô hoặc một dòng: “$x$ tăng về Đông; ô $(3,1)$ trống. Chọn Đông từ $(2,1)$ luôn sang $(3,1)$ và nhận $-1$”. Trước ký hiệu $p$, đọc bằng lời “xác suất của kết quả này bằng 1”. D07B sau đó khái quát đúng cùng ví dụ.
- **Sửa D09:** ghi “Ba phát biểu minh họa độc lập; phát biểu thứ ba xét môi trường chuyển tiếp ngẫu nhiên”. Không thêm “theo đúng mê cung tất định trên”, vì sẽ tạo mâu thuẫn mới.
- **Câu nối sang E00:** “Ta đã dùng một chuyển tiếp cục bộ. Bây giờ đặc tả toàn bộ mê cung và quan sát của tác tử.”

### F11 — Trang giới hạn mô hình trả lời một tranh luận chưa được đặt ra

**Mức độ: trung bình. Vị trí: D07B → D10 → D08.**

- **Bằng chứng:** D10 đối chiếu mô hình một bước với “mô hình hoàn thiện về thế giới”. Notes giải thích đây là câu trả lời cho câu hỏi ở trang 13 của nguồn. Bản deck hiện tại chưa nêu câu hỏi đó. Trang còn dùng “lập kế hoạch kém nếu mô hình sai” mà chưa giải thích lập kế hoạch là thao tác gì.
- **Vai trò trong mạch:** đánh giá phạm vi và sai số của mô hình. **Kết nối vào:** D07B phân biệt $p$ và $\hat p$. **Kết nối ra cần có:** trở lại hai nhiệm vụ đánh giá/cải thiện chính sách ở D08.
- **Sửa:** đổi tiêu đề thành “Phạm vi và sai số của mô hình”. Bắt đầu: “$\hat p$ dự báo một bước trong bài toán đã đặc tả; dự báo có thể sai.” Giữ hai ý phạm vi và sai số; chuyển phần tranh luận “mô hình hoàn thiện về thế giới” xuống ghi chú hoặc bỏ vì không phục vụ mục tiêu hiện tại.
- **Nếu giữ lập kế hoạch:** giải nghĩa ngắn “dùng mô hình để dự báo kết quả của các hành động trước khi chọn”. Kết bằng câu: “Có hoặc không có mô hình, ta vẫn phân biệt đánh giá một chính sách với cải thiện chính sách.”
- **Không nên sửa bằng cách:** thêm một câu hỏi tu từ mới chỉ để hợp thức hóa đoạn tranh luận cũ, hoặc chuyển D10 xuống sau mê cung nhưng giữ nguyên vấn đề chưa có điểm xuất phát.

### F12 — Phần mê cung chưa hoàn tất lời hứa tích hợp ba vai trò

**Mức độ: trung bình. Vị trí: E00–E05; đối chiếu mục tiêu P01, D00 và D09.**

- **Bằng chứng:** E00 đặc tả trạng thái/hành động/thưởng; E02 thực hiện chuyển tiếp; E03–E04 phân loại quan sát. E05 trở về sơ đồ $H_t\to X_t\to A_t\to(R_{t+1},O_{t+1})$ và hai câu mô tả giá trị, mô hình. Chưa có một chính sách cụ thể và giá trị của chính sách đó được tính trong chính mê cung này.
- **Khoảng trống:** đây không phải khái niệm mới đột ngột mà là điểm kết chưa dùng hết kết quả vừa xây dựng. Học viên phải tự nối phần chính sách/giá trị/mô hình với ví dụ tổng hợp.
- **Sửa tối thiểu ở E05 hoặc một trang ngay trước E05:** dùng điểm $(2,1)$ của E02, giữ quan sát đầy đủ và mê cung cố định. Chọn chính sách “đi Đông đến cột 6, rồi đi Bắc đến đích”, và $\gamma=1$. Quỹ đạo đi qua:

  $$(2,1)\to(3,1)\to(4,1)\to(5,1)\to(6,1)\to(6,2)\to(6,3)\to(6,4).$$

  - Chính sách chọn Đông tại $(2,1)$: $\pi(\mathsf E\mid(2,1))=1$.
  - Mô hình dự báo chuyển tiếp đã có ở D07: $p((3,1),-1\mid(2,1),\mathsf E)=1$.
  - Có đúng 7 chuyển tiếp, mỗi lần thưởng $-1$, nên trong trường hợp tất định này $G_t=v_\pi((2,1))=-7$.

  Đây là **ví dụ sửa đề xuất**, suy ra từ lưới và quy ước có sẵn; chưa có trong slide. Đã kiểm tra đường đi tránh hai ô tường $(3,3)$, $(5,2)$ và kết thúc tại $(6,4)$. Chính sách được nêu đủ trên đường đi đang xét; không cần xây bảng chính sách cho mọi ô nếu chỉ tính giá trị từ điểm này.
- **Kết nối mở–kết:** E00 giải thích thưởng âm mỗi bước khuyến khích đến đích sau ít chuyển tiếp; ví dụ trên dùng lại cả D09 và B04. E05 sau đó mới tổng kết vòng tương tác.

### F13 — Tiêu chí quan sát có nguy cơ bị trộn với biết mô hình và có bộ nhớ

**Mức độ: trung bình. Vị trí: C07, E03–E04.**

- **Bằng chứng:** C07 hỏi robot có “cảm biến, bản đồ và bộ nhớ nào”. E04 nêu “ảnh phía trước nhưng không có bản đồ hay bộ nhớ” trước khi yêu cầu phân loại. E03 mới giải thích trong notes rằng tọa độ vẫn có thể là trạng thái Markov khi tác tử chưa biết mô hình.
- **Nguy cơ lập luận:** người học có thể dùng quy tắc “không có bản đồ/bộ nhớ thì quan sát một phần” thay cho tiêu chí nhiều trạng thái cho cùng quan sát. Các câu hỏi gợi mở của E04 đúng hướng, nên không kết luận trang đang định nghĩa sai một cách tường minh.
- **Sửa:** C07 hoặc E03 nêu rõ ba câu riêng: tác tử nhận dữ liệu gì; dữ liệu đó có phân biệt trạng thái không; tác tử có biết quy luật chuyển tiếp không. Bộ nhớ giúp xây biểu diễn từ lịch sử, không tự thay đổi dữ liệu cảm biến hiện tại.
- **Ở E04:** cho hoặc yêu cầu tìm một cặp vị trí khác nhau có cùng ảnh cục bộ; chỉ kết luận sau khi nêu bằng chứng nhập nhằng. Nhắc “không có bản đồ” không phải bằng chứng duy nhất. Điều này nối lại đúng $S_t,O_t,X_t$ ở C00 và $X_t=f(H_t)$ ở C06.

## 4. Các chỉnh nhẹ và nhận xét không nên nâng thành lỗi lớn

- **P02, ghi chú:** thay câu gộp ba vai trò cùng “quyết định cách chọn hành động” bằng “chính sách chọn hành động; hàm giá trị đánh giá tương lai; mô hình dự báo phản hồi”. Đây là chỉnh độ chính xác của lời nối, không đổi bản đồ 7 phần.
- **A03–A04:** có thể nói “dấu ngoặc là cách viết gọn phép nối thêm một chuyển tiếp vào lịch sử”. Không cần mở riêng một trang về cấu trúc dữ liệu. Đoạn notes A03 so sánh cách ghi của “notes” và “deck” là thông tin biên tập; nên thay bằng lời giảng ngắn, chuyển phần ký hiệu trạng thái tới C03.
- **B00/B03/X01:** SVG B00 ghi “tương tác + thưởng trễ”, trong khi B02 đã nói phản hồi **có thể** trễ. Đổi nhãn B00 thành “tương tác + phần thưởng”; giải thích ở B03 rằng thưởng $0$ vẫn là phần thưởng, kết quả hữu ích có thể chỉ xuất hiện muộn. Mô tả thay thế của `delayed-feedback.svg` nên đổi “chưa có phần thưởng” thành “nhận phần thưởng bằng 0”. Khi chữa X01, phân biệt tín hiệu ở từng bước với hậu quả dài hạn, không dạy trễ là điều kiện bắt buộc của mọi bài toán.
- **E05:** “Ví dụ mê cung đã nối bốn trục” không còn khớp bản đồ P02 hiện chỉ liệt kê bảy mạch. Đổi thành “Ví dụ mê cung nối giao diện, thông tin và quyết định”, hoặc bỏ câu vì sơ đồ đã làm nhiệm vụ tổng kết.
- **Z00:** chuỗi Markov, quá trình phần thưởng Markov và Bellman là nội dung được hẹn cho Bài 03. Không cần dạy trước để trang này hợp logic; chỉ làm rõ tên viết tắt MDP theo F04.
- **X10:** giải thích “tiếp diễn: nhiệm vụ không có một thời điểm kết thúc tự nhiên” khi giao bài. Notes D04 có tổng vô hạn nhưng mặt slide chỉ phát triển trường hợp kết thúc; đây là mở rộng nhẹ ở bài tập, không cần thêm cả lý thuyết nhiệm vụ tiếp diễn.

### Những nhận xét đã loại sau đối chiếu

| Nhận xét từ lượt rà độc lập | Kết quả đối chiếu của điều phối viên |
|---|---|
| A04 lộ đáp án ngay, trái notes | **Loại.** HTML có `.grid2.fragment`; bản duyệt ban đầu chỉ hiện câu hỏi, hai ô đáp án ẩn. |
| B00 không cung cấp đủ ba dạng học | **Loại.** Cả ba dạng hiện rõ trong `learning-signals.svg`; không yêu cầu lặp lại toàn bộ chữ của hình trong thân slide. |
| D05 không nói kỳ vọng gồm ngẫu nhiên môi trường | **Loại.** Gạch đầu dòng thứ hai đã nói rõ cả chính sách và chuyển tiếp môi trường. Giữ F09 về thứ tự ví dụ, không biến nó thành lỗi định nghĩa. |
| E00 chưa có quy ước tọa độ trên mặt slide | **Loại.** Gạch đầu dòng đầu tiên và lưới SVG đã ghi quy ước, trục và tọa độ. |
| D07 hoàn toàn chưa có bối cảnh mê cung | **Hạ mức.** D07 đã nêu chuyển tất định và thưởng $-1$; F10 chỉ yêu cầu bổ sung bối cảnh cục bộ còn thiếu. |
| D07B dùng $p$ và $\Pr$ nên ký hiệu mâu thuẫn | **Loại.** Trang định nghĩa $p$ bằng xác suất có điều kiện và nói rõ miền rời rạc. |
| Kỳ vọng ở B04 là tiên quyết hoàn toàn chưa có | **Không coi là lỗi nặng.** Đối tượng đã học học máy/xác suất; B04 còn hẹn hình thức hóa. Có thể thêm trực giác bằng lời nếu lớp cần. |
| Ví dụ xe phải chuyển sau mô hình ở phần D | **Loại.** Ví dụ đang chuẩn bị trực giác cho Markov; chuyển xuống làm đảo tiên quyết. |
| D10/D08 hoặc ID thiếu số làm mạch sai | **Loại.** Thứ tự HTML mới quyết định thứ tự giảng; ID không hiển thị. |

Một số reviewer gán nhầm trích dẫn A03 thành A02, C02 thành C00, D07 thành D02 và E02/E03 thành E00. Báo cáo này dùng vị trí đã kiểm tra trong HTML, không giữ các nhãn gán sai đó.

## 5. Trình tự sửa đề xuất

1. **Sửa tại chỗ phần A–B:** thêm chú giải ký hiệu, hai định nghĩa ngắn “chính sách/quỹ đạo”, phân biệt thưởng 0 với phản hồi trễ. Không đổi thứ tự A trước B.
2. **Giữ C00 → C02 → C03:** chèn lời phát biểu Markov trước công thức; phân biệt lịch sử quan sát/lịch sử trạng thái. Cho ví dụ nhập nhằng trước tên POMDP; bỏ công thức chính sách khỏi C06.
3. **Giữ D00 làm bản đồ vai trò:** bỏ mũi tên tuần tự. D02 thêm ví dụ hợp lệ trước công thức; D03 tiếp tục kiểm tra chuẩn hóa.
4. **Tổ chức lại D04–D06:** ý nghĩa $\gamma$ → quỹ đạo hai thưởng → tính thử → tổng $G_t$ → hai quỹ đạo với trung bình 2,5 → tên và định nghĩa $v_\pi$. Chốt giả thiết thời gian/trạng thái trước khi dùng giá trị.
5. **Giữ D07 → D07B → D10 → D08:** làm ví dụ một bước tự đủ dữ kiện; D10 chỉ nói phạm vi/sai số và nối trở lại dự đoán–điều khiển. D09 nêu rõ các tình huống minh họa độc lập.
6. **Giữ phần mê cung và kết luận:** thêm một lần dùng chung chính sách, mô hình, giá trị từ $(2,1)$; sau đó mới tổng kết E05 và tự kiểm tra Z00. Làm rõ tiêu chí quan sát ở E03–E04.

Sau sửa vẫn giữ **7 section ngoài**. Chỉ tách trang nếu cần làm rõ D04 hoặc ví dụ tích hợp; dành thời gian từ diễn giải cũ trong cùng cụm, không tự tăng tổng 120 phút. Nếu đổi thứ tự D05/D06, rà lại D03–D07B và các ghi chú tham chiếu “trang trước/trang sau”; nếu thêm trang tích hợp ở E, rà D09 và toàn ranh giới E–Z.

## 6. Tiêu chí kiểm tra sau khi sửa

- Người học gọi tên được $O_t,A_t,R_{t+1}$ trước A04, và phân biệt $S_t$ với $O_t$ khi B03 chuyển sang sơ đồ trạng thái.
- C03 có một câu phát biểu Markov bằng lời và lời giải thích hai loại lịch sử trước đẳng thức.
- C06 không yêu cầu đọc công thức chính sách trước D02; niềm tin được giải nghĩa hoặc đưa khỏi tuyến chính.
- Mỗi công thức chính sách/giá trị đều có ví dụ cụ thể chuẩn bị; người học biết ý nghĩa $\gamma$ trước khi thế số.
- D04–D05 thống nhất cách hiểu $T$, thông tin trong trạng thái và lớp chính sách đang xét.
- D07 tự đủ quy ước; D10 có điểm xuất phát từ $p,\hat p$, không trả lời một tranh luận chưa có trong bài.
- Phần E có một hành động do chính sách chọn, một chuyển tiếp mô hình dự báo và một giá trị tích lũy trong cùng ví dụ.
- Các kết luận quan sát dựa vào dữ liệu nhận được và sự nhập nhằng trạng thái, không chỉ dựa vào việc tác tử biết bản đồ.
- Kiểm tra lại fragment A04, SVG, công thức ở mép dưới và tất cả liên kết sau khi tách/đổi thứ tự trang. Duyệt trình chiếu thực tế; không chỉ dựa vào kiểm tra DOM.

## 7. Phương pháp, phạm vi chứng cứ và giới hạn

- Điều phối viên đọc bản hiện tại, tách đủ 47 ID theo thứ tự section, đọc notes và chữ trong 11 SVG, duyệt 47 trang bằng Chromium tại cổng 8766 và xem ảnh của tất cả trang. Không có lỗi JavaScript hoặc HTTP trong lượt duyệt; điều đó không thay cho đánh giá sư phạm ở trên.
- Reader lập kế hoạch riêng đề xuất kiểm tra ký hiệu, tiên quyết, SVG/notes và chia gói. Điều phối viên chỉ chấp nhận phương pháp; sửa số lượng reader nêu nhầm 41 thành 47 và không dùng bảng thuật ngữ nội bộ làm bằng chứng sinh viên đã được học.
- Năm reviewer độc lập nhận bằng chứng trích sẵn, dùng `--no-tools`, không tự mở rộng đọc repo. Vai sinh viên, chuyên gia Học tăng cường, phản biện giảng dạy và mạch viết nhận toàn bộ chuỗi cùng nội dung/notes/SVG đã trích; vai toán nhận gói C–D và ranh giới E kèm tóm tắt tiên quyết. Điều phối viên kiểm chứng mọi phát hiện và loại nhận xét không khớp HTML hoặc hình.
- Báo cáo phân biệt nội dung có trên mặt slide với giải thích chỉ có trong ghi chú. Các đề xuất là đánh giá sư phạm dựa trên thứ tự quan sát được, không phải kết quả thử nghiệm trên sinh viên.
- Lượt này không chuyển lại PPTX hoặc thẩm định toàn bộ tài liệu gốc. Mục tiêu là mạch của bản RevealJS hiện tại. Ví dụ sửa đường đi trong F12 được suy ra và tính lại từ SVG, không coi là dữ liệu thực nghiệm hoặc trích nguyên văn nguồn.
- Codex Slides không có Browser nhúng để xác nhận trực quan trong phiên này; không tuyên bố đã rà bản canvas Codex Slides. Bản được đánh giá trực quan là RevealJS cục bộ.

### Bằng chứng chạy worker

Các tên dưới đây lấy từ trường JSON do cầu nối trả, không lấy từ lời tự khai của reviewer. `provider` trong cầu nối là tên dịch vụ OpenRouter, không xác định nhà cung cấp suy luận phía sau.

| Vai | requested_model | observed_model | provider | Kết quả sử dụng |
|---|---|---|---|---|
| Reader lập kế hoạch | `deepseek/deepseek-v4-flash-0731` | `deepseek/deepseek-v4-flash-0731` | `OpenRouter` | Chấp nhận phương pháp; sửa lỗi đếm trang. |
| Sinh viên | `z-ai/glm-5.3-flash` | `z-ai/glm-5.3-flash` | `OpenRouter` | Đã đối chiếu và hợp nhất. |
| Chuyên gia Học tăng cường | `deepseek/deepseek-v4-flash-0731` | `deepseek/deepseek-v4-flash-0731` | `OpenRouter` | Đã đối chiếu và loại nhận xét trùng/sai chứng cứ. |
| Toán học | `deepseek/deepseek-v4-flash-0731` | `deepseek/deepseek-v4-flash-0731` | `OpenRouter` | Lượt đầu bị cắt đầu ra; lượt thu hẹp hoàn tất. |
| Phản biện giảng dạy | `deepseek/deepseek-v4-flash-0731` | `deepseek/deepseek-v4-flash-0731` | `OpenRouter` | Đã sửa ID gán sai khi hợp nhất. |
| Mạch viết | `z-ai/glm-5.3-flash` | `z-ai/glm-5.3-flash` | `OpenRouter` | Đã đối chiếu SVG và fragment trước khi chấp nhận. |

Lượt toán đầu nhận câu trả lời bị cắt và không hoàn tất sau lượt phục hồi. Điều phối viên thử lại một lần bằng cùng mô hình, chỉ giữ C02–C03, D02, D04–D07B. Lượt sau hoàn tất; phạm vi hẹp này không được coi là rà toán toàn bài.

Nhận xét toán “công thức tổng tự giả định $T$ cố định” không được chấp nhận nguyên văn: tổng theo thời điểm kết thúc vẫn có thể dùng trên từng quỹ đạo khi thời điểm ấy khác nhau. F08 chỉ yêu cầu chốt cách hiểu $T$ và cách viết giá trị tương ứng. Không lấy đề xuất “chỉ xác định khi $t<T$” làm kết luận loại trừ giá trị ở trạng thái kết thúc; cần nêu quy ước tổng rỗng $G_T=0$.

### Tự kiểm bản báo cáo

- Đủ 47 hàng theo đúng thứ tự HTML, mỗi hàng có vị trí ngang/dọc và đường dẫn mở trang.
- Đã phân biệt bằng chứng trực tiếp, nguy cơ hiểu nhầm và ví dụ sửa đề xuất; không coi toàn bộ 13 nhóm là lỗi toán học.
- Đã kiểm tra nội dung theo no-ai-slop: loại lời dẫn rỗng, giữ thuật ngữ nhất quán, dùng câu sửa cụ thể, không thêm nguồn hoặc kết quả thực nghiệm. Công thức Markdown chỉ dùng ký hiệu đô la.
- Chỉ tạo tệp báo cáo này; HTML và toàn bộ SVG của bài không thay đổi.
