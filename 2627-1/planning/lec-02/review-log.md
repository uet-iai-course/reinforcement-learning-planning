# Nhật ký rà soát — Bài 02

## Trạng thái sau chỉnh sửa

- Nguồn đã kiểm kê: 58 trang; Bài 02 dùng trang 1–27.
- Tuyến chính: 34 trang, 120 phút; X01–X02 là nhánh dọc cho phần chữa bài.
- Tài sản: 11 SVG cục bộ; không dùng raster; không có tài nguyên mạng cốt lõi.
- Đã đối chiếu `2627-1/lecture-template.html`; tệp tồn tại và Bài 02 giữ đúng cấu hình RevealJS bắt buộc.

## Báo cáo kiểm định storyboard

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa | trạng thái xử lý |
|---|---|---|---|---|---|
| chặn bàn giao | X01–X02 | Nhiệm vụ không phải Bài 1–2 của `hw02.pdf`. | Bản nháp thay bằng hai bài tự soạn. | Khôi phục nguyên văn nhiệm vụ cốt lõi và nguồn. | Đã sửa nguyên văn, ghi trang nguồn. |
| chặn bàn giao | B04 | Dùng $\pi,G_t$ trước định nghĩa. | Hai ký hiệu chỉ được định nghĩa ở D02, D04. | Viết giả thuyết bằng lời. | Đã sửa; công thức xuất hiện sau tiên quyết. |
| nghiêm trọng | D00–D09 | Gộp bốn khái niệm vào một chu trình. | Chính sách, giá trị, mô hình và hai bài toán có sản phẩm khác nhau. | Tách thành các vi chu trình. | Đã tách trong storyboard với 8, 14, 6 và 8 phút. |
| nghiêm trọng | C02–C03 | Công thức Markov xuất hiện trước ví dụ. | C02 cũ chỉ lặp phát biểu trừu tượng. | Đưa ví dụ cụ thể trước công thức. | Đã thêm ví dụ vị trí–vận tốc và vẽ lại SVG. |
| trung bình | B00–B01, D00–D01 | Trang mở phần lặp nội dung. | Cùng SVG và cùng luận điểm. | Gộp. | Đã gộp; đồng thời gộp A, C, E để còn 34 trang. |
| trung bình | E00–E05 | 12 phút quá ngắn. | Cụm có đặc tả, chuyển tiếp và quan sát. | Dành 18–20 phút. | Đã dành 20 phút. |
| trung bình | planning | Ghi sai rằng template không tồn tại; thuật ngữ Anh không cần thiết. | Tệp template có trong kho; có các từ `policy`, `return`, `caveat`. | Đối chiếu thật và Việt hóa. | Đã sửa. |

## Báo cáo góc nhìn sinh viên

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa | trạng thái xử lý |
|---|---|---|---|---|---|
| nghiêm trọng | B04 | Tiên quyết ký hiệu bị đảo. | $\pi,G_t$ chưa xuất hiện. | Bỏ công thức. | Đã sửa. |
| nghiêm trọng | toàn bài | 39 trang và 8 tương tác cần khoảng 125–140 phút. | Vượt 120 phút. | Gộp trang lặp hoặc dùng nhánh dọc. | Đã giảm còn 34 trang; bài tập ở nhánh dọc. |
| nghiêm trọng | SVG | Chữ 18–19 px khi render khó đọc. | Nhiều nhãn nguồn chỉ 23–27 px. | Tăng cỡ chữ tương đương ít nhất `0.65em`. | Đã tăng các nhãn nội dung nhỏ; mê cung dùng 40–42 px. |
| trung bình | A04 | Đáp án lộ ngay. | Hai ô đáp án có sẵn. | Dùng fragment hoặc ghi chú. | Đã dùng fragment và notes. |
| trung bình | D08, SVG | $q_\pi$ chưa định nghĩa. | Chỉ xuất hiện ở phân biệt dự đoán. | Bỏ hoặc định nghĩa. | Đã bỏ khỏi HTML và SVG. |
| trung bình | D04 | $\gamma$ thiếu nghĩa. | Chỉ có miền $[0,1]$. | Nêu vai trò chiết khấu. | Đã nêu trên slide và notes. |
| trung bình | B02 | “Không i.i.d.” mơ hồ. | Trộn phụ thuộc và đổi phân phối. | Tách hai mệnh đề. | Đã sửa. |
| nhẹ | toàn bài | Câu hỏi và mạch A/C/E tốt; khả năng tiếp cận tốt. | Có alt, notes và câu hỏi kiểm tra. | Giữ. | Đã giữ. |

## Báo cáo chuyên gia Học tăng cường

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa | trạng thái xử lý |
|---|---|---|---|---|---|
| nghiêm trọng | C03 | Trộn trạng thái với lịch sử quan sát $H_t$. | A03 định nghĩa $H_t$ bằng $O_t$. | Dùng lịch sử trạng thái riêng. | Đã định nghĩa $\mathcal H_t^S$. |
| nghiêm trọng | E00–E03 | Đồng nhất Markov với tác tử biết bản đồ. | Kiến thức mô hình không quyết định tính Markov. | Cố định/biến thiên bản đồ và tách hai khái niệm. | Đã sửa E00, E03 và SVG quan sát. |
| nghiêm trọng | D02 | Chính sách chỉ viết theo $S_t$ sau POMDP. | Tác tử có thể chỉ dùng $X_t$. | Viết theo $X_t$, nêu $X_t=S_t$ là trường hợp riêng. | Đã sửa D02–D03. |
| nghiêm trọng | B04 | Tiên quyết bị đảo. | Như báo cáo storyboard. | Bỏ ký hiệu. | Đã sửa. |
| trung bình | C05 | Thiếu tên đầy đủ POMDP. | Chỉ dùng từ viết tắt trong notes. | Giới thiệu đầy đủ lần đầu. | Đã sửa trên slide. |
| trung bình | D08 | $q_\pi$ chưa định nghĩa. | Không dùng ở nơi khác. | Bỏ. | Đã bỏ. |
| trung bình | B02 | Phát biểu i.i.d. quá mạnh. | Không đúng cho mọi cách lấy mẫu. | Dùng mệnh đề có điều kiện. | Đã sửa. |
| trung bình | D00–D09 | Tải khái niệm cao. | Bốn đối tượng trong một cụm. | Tách vi chu trình và thời lượng. | Đã sửa storyboard. |

## Báo cáo độ chính xác toán học và thuật toán

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa | trạng thái xử lý |
|---|---|---|---|---|---|
| chặn bàn giao | A03, C03, SVG Markov | Hai loại lịch sử dùng cùng ký hiệu; điều kiện hóa không nhất quán. | $H_t$ chứa $O_t$ nhưng vế Markov cần lịch sử trạng thái. | Tách ký hiệu và đồng bộ hình. | Đã sửa C03; SVG nay là ví dụ không dùng lịch sử. |
| nghiêm trọng | B04 | Dùng đối tượng chưa định nghĩa. | $\pi,G_t$ xuất hiện sớm. | Viết bằng lời. | Đã sửa. |
| nghiêm trọng | D08, SVG vai trò | $q_\pi$ chưa định nghĩa. | Không có miền hoặc kỳ vọng. | Bỏ. | Đã bỏ. |
| nghiêm trọng | D02–D03 | Thiếu miền chính sách và $\mathcal A(x)$. | Chuẩn hóa cũ theo $\mathcal A(s)$ nhưng chính sách tổng quát theo $X$. | Định nghĩa $\mathcal X,\mathcal A(x)$. | Đã sửa. |
| nghiêm trọng | SVG quan sát | Nói $O_t$ là tập con của $S_t$. | Quan sát và trạng thái có thể thuộc hai miền khác nhau. | Diễn đạt bằng quan hệ xác định/nhập nhằng. | Đã sửa. |
| nghiêm trọng | D07 | Thiếu giả thiết rời rạc và chuẩn hóa. | Chỉ nêu hàm khối xác suất. | Nêu miền, không âm và tổng bằng 1. | Đã sửa; trường hợp liên tục ở notes. |
| trung bình | E00–E03 | Tọa độ, thưởng đích và ký hiệu hành động chưa rõ. | $E$ vừa là chữ vừa là hành động; thưởng “trước kết thúc” mơ hồ. | Nêu gốc tọa độ, $\mathsf E$, thưởng khi vào đích. | Đã sửa. |
| trung bình | D09 | “Kỳ vọng mất 7 bước” chưa đủ để là giá trị. | Thiếu chính sách và quy ước thưởng. | Nêu $v_\pi(s)=-7$ dưới $\pi$ và thưởng $-1$. | Đã sửa. |
| nhẹ | A04, D03, D04, D06, E02 | Các phép kiểm số học đúng. | Chỉ số A04; tổng $1{,}2$; chỉ số hữu hạn; $2{,}5$; va tường. | Giữ. | Đã giữ. |

## Sai khác có chủ ý so với nguồn

- Bỏ trang 5, 6 và 11 vì không có mệnh đề dạy học có thể truy nguyên hoặc có tuyên bố AGI thiếu căn cứ.
- Sửa chỉ số ở trang nguồn 15 thành $A_t\to(R_{t+1},O_{t+1})$.
- Bổ sung lịch sử trạng thái, định nghĩa $G_t$, $\gamma$, chuẩn hóa chính sách và mô hình vì thiếu chúng sẽ gây hiểu sai.
- Cố định bản đồ mê cung, quy ước tọa độ, va tường, thưởng chuyển tiếp vào đích và điều kiện dừng.
- Gộp năm cặp trang để phù hợp 120 phút; đã rà hai trang lân cận mỗi phía như ghi trong storyboard.

## Báo cáo phản biện học thuật thứ tư

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa | trạng thái xử lý |
|---|---|---|---|---|---|
| nghiêm trọng | C03 | Đẳng thức Markov chưa gắn giá trị lịch sử với trạng thái cuối. | Vế trái điều kiện trên biến ngẫu nhiên $\mathcal H_t^S$, vế phải dùng $S_t$ mà không ghi $S_t=s$. | Viết $\mathcal H_t^S=h_t^S$, yêu cầu $h_t^S$ kết thúc ở $s$ và biến cố điều kiện có xác suất dương. | Đã sửa công thức và notes. |
| nghiêm trọng | D04–D09 | Chính sách theo $X_t$ ở D02 nhưng $v_\pi(s)$ theo trạng thái ở D05. | Chưa chốt trường hợp quan sát đầy đủ. | Nêu rõ $X_t=S_t$ và chính sách Markov $\pi(a\mid s)$ trước cụm giá trị. | Đã thêm trên mặt D04, notes, outline và storyboard. |
| nghiêm trọng | D04 | Công thức tổng đứng trước ví dụ. | Chu trình yêu cầu ví dụ trước hình thức. | Đặt quỹ đạo thưởng cụ thể và tự tính trước tổng. | Đã thêm $(-1,-1)\mapsto-1-\gamma$ trước công thức. |
| nghiêm trọng | D07 | Mô hình chung đứng trước trường hợp kiểm tra được. | Người học chưa thấy xác suất khối trong một chuyển tiếp. | Dùng chuyển tiếp mê cung tất định với xác suất $1/0$ trước công thức. | Đã sửa theo quy ước nguồn, không thêm số liệu ngoài nguồn. |
| trung bình | E05–Z00 | Câu nối Bài 03 quá chung. | Chưa phân biệt chuỗi Markov, quá trình phần thưởng Markov và MDP. | Nêu tuyến mô hình rồi Bellman, không mở thêm suy diễn. | Đã sửa cô đọng trên hai trang. |
| trung bình | `maze-mdp.svg` | Nhãn thưởng thiếu chỉ số thời gian. | HTML dùng $R_{t+1}$ nhưng hình dùng $R$. | Đồng bộ $R_{t+1}=-1$. | Đã sửa SVG. |
| trung bình | storyboard | Cụm định hướng đảo bước vấn đề/trực giác/hình thức. | P01 và P02 bị ép vào chu trình không phù hợp. | Ghi các bước không áp dụng và lý do. | Đã sửa. |
| chặn bàn giao | D04, storyboard D07 | Mã trang xuất hiện trên mặt trang/notes và D07 có phụ thuộc ngược tới ví dụ nằm sau. | D04 ghi phạm vi bằng mã nội bộ; đầu vào D07 liệt kê E00. | Viết phạm vi bằng tên khái niệm; để ví dụ D07 tự đủ. | Đã bỏ mã nội bộ khỏi mặt/notes và bỏ phụ thuộc ngược. |

## Tái rà độ chính xác toán học

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa | trạng thái xử lý |
|---|---|---|---|---|---|
| nghiêm trọng | C03 | Điều kiện xác suất có thể không xác định trên lịch sử xác suất bằng không. | Công thức cũ lượng hóa mọi lịch sử “phù hợp” nhưng không nêu điều kiện dương. | Chỉ lượng hóa $h_t^S,a$ có xác suất điều kiện dương. | Đã sửa. |
| nghiêm trọng | D04–D06 | Miền của chính sách và biến điều kiện hàm giá trị chưa thống nhất. | D02 dùng $X_t$, D05 dùng $S_t$. | Giới hạn cục bộ $X_t=S_t$, $\pi(a\mid s)$. | Đã sửa và truyền giả thiết qua notes/storyboard. |
| trung bình | D04 | Cần kiểm tra ví dụ tổng chiết khấu. | Hai thưởng đều $-1$. | Tính $R_{t+1}+\gamma R_{t+2}=-1-\gamma$. | Đã tính lại; đúng với $T=t+2$. |
| trung bình | D07 | Ví dụ tất định phải thỏa chuẩn hóa. | Một kết quả có xác suất $1$, mọi kết quả khác $0$. | Giữ tổng xác suất bằng $1$ rồi mới tổng quát hóa. | Đã sửa; công thức chuẩn hóa vẫn có mặt. |
| nhẹ | E05–Z00 | Không đưa Bellman vào trước tiên quyết. | Bài 02 chưa định nghĩa đầy đủ MDP. | Chỉ nêu tuyến của Bài 03. | Đã giữ ở mức câu nối. |
| nhẹ | D04, D07 | Tái rà cuối về phạm vi và thứ tự tiên quyết. | Giả thiết quan sát đầy đủ cần áp theo khái niệm; ví dụ mô hình phải tự đủ. | Dùng tên phần thay mã trang và bỏ đầu vào tương lai. | Đã xử lý; không đổi công thức hoặc số trang. |

## Ngoại lệ và giới hạn

- Không có ngoại lệ raster.
- Codex Slides đã lưu bền vững PPTX nguồn, HTML, outline, storyboard và review-log trong dự án `20260824132931-chuy-n-lecture-2-markov-decision-process-jnbq`; nội dung Design File khớp bản trong kho. Môi trường không cung cấp trình duyệt Codex nhúng nên chưa thể xác nhận trực quan từng trang trong Codex Slides.
- Ví dụ số D06 và ví dụ xe C02 là ví dụ giảng dạy, không phải số liệu thực nghiệm.

## Kiểm định cuối

- Chạy `python3 -m reloadserver 8765` với mô-đun cài tạm ngoài kho: máy chủ khởi động tại cổng 8765.
- HTTP 200: chỉ mục, HTML Bài 02, bốn tệp planning và 11 SVG.
- Cấu trúc đạt: 36 `data-slide-id` duy nhất, 34 trang tuyến chính, 2 trang nhánh dọc, 36/36 ghi chú diễn giả và đủ 36 mục storyboard.
- KaTeX đạt: 12 công thức khối và 108 công thức nội dòng biên dịch không lỗi.
- Tài sản đạt: 11 SVG hợp lệ XML, có `role="img"`, `title`, `desc`; không có ảnh raster hoặc tài nguyên mạng cốt lõi.
- Cỡ chữ nhỏ nhất trong SVG là 30 đơn vị thiết kế; không có nhãn dưới ngưỡng đã sửa theo báo cáo góc nhìn sinh viên.
- Codex Slides chạy bằng Node.js 20 sau khi runtime Node.js 18 gây lỗi `File is not defined`; Design Files đã được đọc lại và đối chiếu byte với tệp trong kho.
- Giới hạn: không có Chromium, Firefox, Playwright hoặc trình duyệt Codex nhúng trong phiên này. Chưa duyệt trực quan 1280×720 và màn hình hẹp; không tuyên bố đã kiểm tra tràn, chồng lấn hoặc bàn phím bằng trình duyệt.

## Tự kiểm `no-ai-slop/eval.md`

- Đạt: giữ ý nguồn; không thêm thành tựu, số liệu hoặc nhận định quảng bá.
- Đạt: câu trực tiếp, không hỏi tu từ, không dùng câu mở rỗng hoặc kết luận lặp.
- Đạt: dùng nhất quán các thuật ngữ trạng thái, quan sát, biểu diễn, chính sách, giá trị và mô hình.
- Đạt: đã thay `policy`, `return`, `control`, `caveat` trong nội dung quy trình bằng thuật ngữ Việt phù hợp.
- Đạt: không có khẩu hiệu, câu cảm thán hoặc nhịp câu kịch tính trong nội dung hiển thị và ghi chú diễn giả.

## Rà mạch theo Quill

- Đạt: ví dụ C02 đứng trước công thức C03; dữ kiện vị trí–vận tốc được truyền trực tiếp.
- Đạt: $X_t$ đi từ phần C sang miền chính sách ở D02–D03.
- Đạt: $G_t$ và $\gamma$ xuất hiện trước $v_\pi$; dự đoán và điều khiển xuất hiện sau chính sách và giá trị.
- Đạt: mê cung giữ một đặc tả môi trường khi thay giao diện quan sát.
- Không tạo `quill.json`; đây không phải dự án sách.

## Thay đổi cần tái rà toán

- C03: thay công thức Markov bằng lịch sử trạng thái $\mathcal H_t^S$.
- D02–D03: đổi miền chính sách từ trạng thái sang biểu diễn $X_t$ và $\mathcal A(x)$.
- D07: thêm giả thiết rời rạc và điều kiện chuẩn hóa.
- E00–E03: làm rõ trạng thái Markov, tọa độ, thưởng chuyển tiếp đích và giao diện quan sát.
- Vòng tái rà cuối: C03 đã thêm điều kiện $\mathcal H_t^S=h_t^S$, $S_t=s$ và xác suất dương; D04–D09 đã thống nhất $X_t=S_t$, $\pi(a\mid s)$; ví dụ D04 và D07 đã được tính lại.

## Vòng rà lại ngày 2026-08-30

### Bằng chứng runtime

| vai trò | requested_model | observed_model | provider |
|---|---|---|---|
| planner | z-ai/glm-5.3-flash | z-ai/glm-5.3-flash | OpenRouter |
| source reader | z-ai/glm-5.3-flash | z-ai/glm-5.3-flash | OpenRouter |
| storyboard reviewer | z-ai/glm-5.3-flash | z-ai/glm-5.3-flash | OpenRouter |
| reviewer 1 (sinh viên) | z-ai/glm-5.3-flash | z-ai/glm-5.3-flash | OpenRouter |
| reviewer 2 (chuyên gia RL) | z-ai/glm-5.3-flash | z-ai/glm-5.3-flash | OpenRouter |
| reviewer 3 (toán và thuật toán) | z-ai/glm-5.3-flash | z-ai/glm-5.3-flash | OpenRouter |
| reviewer 4 (phản biện học thuật) | z-ai/glm-5.3-flash | z-ai/glm-5.3-flash | OpenRouter |
| reviewer 5 (mạch viết) | z-ai/glm-5.3-flash | z-ai/glm-5.3-flash | OpenRouter |

### Tóm tắt kiểm định storyboard mới

Storyboard giữ 34 trang tuyến chính cộng X01–X02, tổng 120 phút. P02 nêu đủ bốn trục; B04 có cầu nối tới hình thức hóa tổng phần thưởng ở phần giá trị; D07 tự nêu quy ước tối thiểu và tách $p$ với $\hat p$; D00 được ghi rõ là trang mở phần dùng chung; E05 chỉ thu hồi vòng giao diện, Z00 là nơi duy nhất nêu tuyến Bài 03 và phân tuyến bài tập.

### Góc nhìn sinh viên

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa | trạng thái xử lý |
|---|---|---|---|---|---|
| trung bình | D04 | $\gamma$ xuất hiện mà thiếu trực giác số. | Quỹ đạo $(-1,-1)$ đã có nhưng chưa so sánh các giá trị $\gamma$. | Tính với $\gamma=0,0{,}5,1$. | Đã thêm câu hỏi và đáp án trong notes. |
| trung bình | C03 | Trang có nhiều ký hiệu mới. | Lịch sử trạng thái, điều kiện xác suất dương và đẳng thức cùng xuất hiện. | Tách trang hoặc giảm tải. | Không tách; C02 đã đặt ví dụ trước, C03 giữ một luận điểm hình thức. Sẽ kiểm tra tràn trực quan. |
| trung bình | D07 | Ví dụ mê cung dùng trước đặc tả E00. | Tọa độ và thưởng xuất hiện trước phần mê cung. | Tự nêu quy ước tối thiểu. | Đã sửa. |
| trung bình | E00, E02 | Hình mê cung thiếu tọa độ. | Không đối chiếu được $(2,1)\to(3,1)$. | Thêm nhãn hàng, cột và đích. | Đã sửa SVG. |
| nhẹ | D09 | Giá trị $-7$ thiếu $\gamma$ và số bước. | Con số không kiểm tra được với giả thiết cũ. | Nêu $\gamma=1$ và đúng 7 bước. | Đã sửa trên mặt trang. |
| nhẹ | P00 | Notes ghi sai nguồn ghép Bài 2–3. | Tệp là Lecture 2; phạm vi dùng trang 1–27. | Sửa mô tả nguồn. | Đã sửa. |
| nhẹ | toàn bài | Reviewer đếm nhầm 36 trang chính. | 36 mã gồm 34 trang chính và X01–X02. | Đối chiếu lại cấu trúc. | Bác bỏ; số trang planning đúng. |

### Chuyên gia Học tăng cường

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa | trạng thái xử lý |
|---|---|---|---|---|---|
| trung bình | D07 | Định nghĩa $p$ làm mờ ranh giới với Bài 03. | Bài 02 dừng trước MDP đầy đủ. | Chuyển $p$ sang Bài 03 hoặc ghi rõ vai trò tiên quyết. | Giữ $p$ để định nghĩa mô hình; không giới thiệu bộ MDP hay Bellman. |
| trung bình | D00, D08 | SVG dùng ký hiệu giá trị không khớp HTML. | Hình dùng `vᵖⁱ`, HTML dùng $v_\pi$. | Đồng bộ ký hiệu. | Đã sửa hai SVG. |
| trung bình | D04 | Thiếu trực giác về hệ số chiết khấu. | Mặt trang cũ chỉ nêu miền $[0,1]$. | Thêm so sánh số. | Đã sửa cục bộ. |
| trung bình | E00, E02 | Hình mê cung thiếu hệ tọa độ. | Ví dụ dùng tọa độ cụ thể. | Thêm nhãn hàng và cột. | Đã sửa. |
| nhẹ | C02 | SVG khẳng định vị trí kế tiếp chắc chắn khác. | HTML chỉ kết luận “có thể khác”. | Giảm mức khẳng định, thêm đơn vị. | Đã sửa SVG. |
| nhẹ | B04 | Phạm vi giả thuyết phần thưởng chưa đủ rõ. | Nguồn phát biểu quá mạnh. | Nêu điều kiện tín hiệu thưởng nhất quán với hành vi mong muốn. | Đã sửa notes. |

### Độ chính xác toán học và thuật toán

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa | trạng thái xử lý |
|---|---|---|---|---|---|
| trung bình | D07 | Ví dụ dùng quy ước mê cung trước khi thiết lập. | Thưởng $-1$ và chuyển tất định chỉ có ở E00. | Tự nêu quy ước. | Đã sửa. |
| trung bình | D04–D05 | Định nghĩa chỉ khép cho nhiệm vụ hữu hạn. | $G_t$ dùng thời điểm kết thúc $T$, còn $v_\pi$ được phát biểu chung. | Nêu trường hợp tiếp diễn và điều kiện hội tụ. | Đã thêm vào notes với $\gamma<1$ và phần thưởng bị chặn. |
| nhẹ | D09 | $v_\pi(s)=-7$ thiếu giả thiết. | Với $\gamma<1$ hoặc số bước khác, kết quả đổi. | Nêu $\gamma=1$, đúng 7 bước. | Đã sửa. |
| nhẹ | D00, D08 | Ký hiệu $v_\pi$ trong SVG sai dạng. | Hình dùng ký tự chỉ số trên ghép. | Dùng `tspan` cho chỉ số dưới $\pi$. | Đã sửa. |
| nhẹ | B03 | Mô tả thay thế nói ba hành động đầu chưa có thưởng. | Hình chỉ có hai hành động đầu thưởng 0. | Sửa thành hai hành động đầu. | Đã sửa. |
| nhẹ | B02 | Câu “người giám sát chỉ sẵn” thiếu từ. | Câu không trọn nghĩa. | Viết “cung cấp sẵn”. | Đã sửa. |

### Phản biện học thuật và giảng dạy

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa | trạng thái xử lý |
|---|---|---|---|---|---|
| trung bình | D04 | Công thức hữu hạn thiếu cầu nối tới nhiệm vụ tiếp diễn. | $T$ hữu hạn được dùng nhưng chưa nói $T=\infty$. | Bổ sung trường hợp tiếp diễn trong notes. | Đã sửa. |
| trung bình | D04 | $\gamma$ thiếu ví dụ trực giác. | Bài tập nguồn có yêu cầu so sánh, nhưng nằm ngoài phạm vi Bài 1–2. | Dùng quỹ đạo sẵn có để minh họa ngắn. | Đã sửa mà không mở thêm bài tập. |
| trung bình | D07 | $\mathcal R$ chưa định nghĩa; $p$ dễ bị hiểu là mô hình tác tử. | Outline chỉ có $R_{t+1}\in\mathbb R$. | Định nghĩa $\mathcal R$ và tách $p$ với $\hat p$. | Đã sửa. |
| trung bình | Z00 | Nhánh bài tập không nói rõ phần bị hoãn. | Nguồn có 10 bài, nhánh chỉ dùng Bài 1–2. | Nêu Bài 3–10 xử lý sau Bài 03. | Đã sửa. |
| nhẹ | A03, C03 | Hai lịch sử dễ nhầm. | $H_t$ chứa quan sát; $\mathcal H_t^S$ chứa trạng thái. | Nêu khác biệt trong notes. | Đã sửa. |
| nhẹ | C02 | Ví dụ xe thiếu đơn vị. | Hình ghi 10, 1, 5 không có đơn vị. | Thêm m và m/s. | Đã sửa SVG. |

### Kết nối và mạch viết

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa | trạng thái xử lý |
|---|---|---|---|---|---|
| trung bình | P02 | Bản đồ bỏ sót mạch tín hiệu học. | Cụm B dài 16 phút nhưng không có trên P02. | Thêm trục Tín hiệu học. | Đã sửa; P02 có bốn trục nội dung. |
| trung bình | D07 | Ví dụ mượn quy ước từ phần sau. | Kết nối vào thiếu tiên quyết. | Tự nêu quy ước tối thiểu. | Đã sửa. |
| trung bình | B04 | Sản phẩm không được thu hồi trước D04. | Cầu nối B04→D04 bị treo qua một mạch. | Thêm mốc hồi đầu và ghi trong storyboard. | Đã sửa. |
| nhẹ | E05, Z00 | Hai trang lặp chức năng mở Bài 03. | Cả hai cùng nêu tuyến chi tiết. | E05 thu hồi bài; Z00 mở bài kế tiếp. | Đã sửa. |
| nhẹ | B05, C00 | Câu nối liên mạch chỉ có trong storyboard. | Notes B05 chưa báo chuyển sang tầng thông tin. | Thêm câu nối trong notes. | Đã sửa. |

### Quyết định bác bỏ

- Bác bỏ nhận xét “36 trang chính”: sai đếm; 36 gồm 34 trang chính cộng X01–X02 nhánh dọc.
- Bác bỏ đề xuất đưa hw02 Bài 3–10 vào Bài 02: chỉ ghi sẽ xử lý sau Bài 03.
- Bác bỏ đề xuất tách C03: ví dụ C02 đã đứng trước và công thức cần liền mạch.
- Bác bỏ đề xuất loại $p$ khỏi D07: $p$ là tiên quyết để định nghĩa vai trò mô hình; chỉ phân biệt động lực $p$ với mô hình ước lượng $\hat p$.

### Ghi nhận tiến trình và giới hạn

- Writer lượt đầu chạm giới hạn tool-call sau khi sửa HTML, SVG và outline; lượt này hoàn tất planning. Đây không phải lỗi nội dung.
- Kiểm định trực quan của vòng hiện tại CHƯA chạy; không tuyên bố đã đạt.
- Đã tự rà no-ai-slop và mạch Quill: đạt; không tạo quill.json.

### Tái rà sau chỉnh sửa

- Độ chính xác toán học và thuật toán: `requested_model=z-ai/glm-5.3-flash`, `observed_model=z-ai/glm-5.3-flash`, `provider=OpenRouter`. Không còn lỗi chặn bàn giao hoặc nghiêm trọng. Các phép tính ở D04, D06, D09; giả thiết hữu hạn/tiếp diễn; chuẩn hóa; $p$/$\hat p$ và tọa độ SVG đều đúng. Đã bổ sung trong notes D09 rằng phát biểu chuyển tiếp xác suất $0{,}1$ minh họa môi trường ngẫu nhiên.
- Kết nối và mạch viết: `requested_model=z-ai/glm-5.3-flash`, `observed_model=z-ai/glm-5.3-flash`, `provider=OpenRouter`. Đủ bảy mạch ngoài; P02 giữ đúng bốn trục nội dung; B04 nối tới D04; D07 tự đủ; E05 và Z00 không lặp chức năng. Hai góp ý nhẹ ở E05 được xử lý bằng một câu thu hồi ví dụ mê cung và dẫn sang tự kiểm tra.
- Rà lân cận E03–X02 phát hiện chuyển ý E04→E05 còn mờ ở mức trung bình. Đã thêm một dòng trên E04 để báo trước trang tổng hợp; không đổi luận điểm, số trang hoặc thứ tự.
- Tái rà tiếp phát hiện E05 dùng $O_t\to X_t$ như trường hợp tổng quát, không khớp $X_t=f(H_t)$ ở C06. Đã đổi ô đầu thành lịch sử $H_t$, thêm giải thích trong notes và ghi E04 áp dụng lại bảng kiểm quan sát.

### Kiểm định cuối của vòng rà ngày 2026-08-30

- Lệnh bắt buộc `python3 -m reloadserver 8765` không chạy vì môi trường không có mô-đun `reloadserver`. Để không phục vụ tệp `.env`, đã tạo một gói kiểm thử cô lập chỉ gồm Bài 02 và tài sản cục bộ, rồi phục vụ bằng `python3 -m http.server 8765` tại `http://127.0.0.1:8765/2627-1/lecture-02-giao-dien-tac-tu-moi-truong.html`.
- Kiểm tra tĩnh đạt: 7 `<section>` ngoài; 36 trang với 36 `data-slide-id` duy nhất; 36 ghi chú diễn giả; 11 SVG; không có ảnh raster, tham chiếu mạng cốt lõi, tài nguyên thiếu hoặc liên kết planning trên chỉ mục.
- Chromium ở khung 1280 × 720: duyệt đủ 36 trang; không có lỗi JavaScript, lỗi tài nguyên, tràn chữ hoặc chồng lấn. Đã xem lại riêng D04, D07, E00, E04, E05 và Z00.
- Chromium ở khung 800 × 600: duyệt đủ 36 trang; không có lỗi JavaScript, lỗi tài nguyên, tràn chữ hoặc chồng lấn.
- Điều hướng bàn phím đạt: `P00` → `P01` bằng phím xuống, trở lại `P00` bằng phím lên và sang `A00` bằng phím phải.
- Rà cuối theo `no-ai-slop/eval.md` và Quill đạt; không tạo `quill.json`.
- Codex Slides trong trình duyệt nhúng không khả dụng ở vòng hiện tại. Vì vậy, vòng này chỉ xác minh bằng RevealJS cục bộ và không tuyên bố đã rà trực quan bằng Codex Slides. Bằng chứng dự án Codex Slides lịch sử ở trên được giữ để truy nguyên, không thay cho phép kiểm tra trình duyệt hiện tại.
- Sau các lượt tái rà toán học, mạch viết và vùng lân cận, không còn lỗi `chặn bàn giao`, `nghiêm trọng` hoặc `trung bình` chưa xử lý.

## Giai đoạn I — Lecture note (2026-09-03)

## Trạng thái

- Giai đoạn: I (soạn và sửa theo phạm vi duyệt).
- Chưa commit; chưa tuyên bố kiểm định viewer/deck.

## Kiểm kê plan/source/merge

- Plan: `.worker/lec02-approved-scope.md` — đặc tả 12 topic, thứ tự học, yêu cầu hình thức.
- Source: `RL-hk2-2025-2026/lecture2-3-MDPswithKeyConcepts.pptx` trang 1–27 (bằng chứng kiểm kê trực tiếp do điều phối viên cung cấp trong plan, gồm trang 15, 17, 22, 23, 25–26); `RL-hk2-2025-2026/resources/hw02.pdf` (Bài 1, 2, 5, 6 chính; Bài 10 mở rộng; Bài 3, 4, 7, 8, 9 để dành).
- Merge: `materials/lec-02/lecture-note.md` — áp dụng 20 mục sửa từ `.worker/lec02-note-review-queue.md`.

## Năm báo cáo hợp lệ (metadata)

| Vai | requested_model | observed_model | provider | Kết quả |
|---|---|---|---|---|
| Góc nhìn sinh viên (chạy lại) | z-ai/glm-5.3-flash | z-ai/glm-5.3-flash | OpenRouter | hoàn tất vòng 2, review, timeout 300 giây |
| Chuyên gia Học tăng cường (chạy lại) | deepseek/deepseek-v3.2 | deepseek/deepseek-v3.2 | OpenRouter | hoàn tất vòng 3, review, timeout 300 giây |
| Độ chính xác toán học–thuật toán | deepseek/deepseek-v3.2 | deepseek/deepseek-v3.2 | OpenRouter | hoàn tất vòng 3, review |
| Phản biện học thuật–giảng dạy | deepseek/deepseek-v3.2 | deepseek/deepseek-v3.2 | OpenRouter | hoàn tất vòng 3, review |
| Kết nối và mạch viết | z-ai/glm-5.3-flash | z-ai/glm-5.3-flash | OpenRouter | hoàn tất vòng 2, review |

## Lượt bị loại/lỗi (không tính vào năm báo cáo)

| Lượt | Vấn đề |
|---|---|
| Reviewer sinh viên (lượt 1) | Lỗi `OpenRouter request exceeded 240s wall timeout`. |
| Reviewer chuyên gia RL (lượt 1) | Gọi `search_text` trái phạm vi nên bị loại dù có kết quả. |

## Bảng phát hiện và quyết định

| # | Mức độ | Vị trí | Vấn đề | Bằng chứng | Đề xuất sửa | Quyết định |
|---|---|---|---|---|---|---|
| 1 | Bắt buộc | Tiên quyết | "Hai kiến thức này" sai số nhiều; thiếu dẫn giải trước lần dùng đầu | Queue mục 1 | Đổi thành "Các kiến thức này", thêm dẫn giải | Áp dụng |
| 2 | Bắt buộc | Topic 10, 11 | Heading `###` thấp hơn các topic khác | Queue mục 2 | Nâng lên `##` | Áp dụng |
| 3 | Bắt buộc | Topic 04 Vấn đề | Câu hỏi tu từ trong mục Vấn đề | Queue mục 3 | Viết phát biểu trực tiếp | Áp dụng |
| 4 | Bắt buộc | Topic 01 ví dụ | Quy ước thưởng không nhất quán (0 ở đích) | Queue mục 4 | $-1$ mỗi bước kể cả bước đích | Áp dụng |
| 5 | Bắt buộc | Topic 01 hình thức | Mục tiêu mơ hồ $\sum_t R_{t+1}$ | Queue mục 5 | Đổi thành $\max_\pi\mathbb E_\pi[G_t]$, báo $G_t$ ở topic 07 | Áp dụng |
| 6 | Bắt buộc | Topic 03 | Tính Markov thiếu biến cố đầy đủ, lịch sử chưa bắt đầu ở $S_0$ | Queue mục 6 | Viết $\Pr(S_{t+1}\mid S_t)=\Pr(S_{t+1}\mid S_0,\ldots,S_t)$, nêu dạng viết tắt sau | Áp dụng |
| 7 | Bắt buộc | Topic 04 hình thức + đáp án | Định nghĩa một phần chỉ bằng $O_t\ne S_t$ | Queue mục 7 | Định nghĩa qua đủ thông tin dự báo/khôi phục trạng thái | Áp dụng |
| 8 | Bắt buộc | Mục Ký hiệu | Danh sách thay vì bảng | Queue mục 8 | Chuyển thành bảng Markdown, tách đoạn quy ước chu kỳ | Áp dụng |
| 9 | Bắt buộc | Topic 05 | "10 bước thưởng" mơ hồ | Queue mục 9 | Diễn đạt thưởng $-1$ mỗi bước; dẫn $P^a_{ss'},R^a_s$ tới topic 07 | Áp dụng |
| 10 | Bắt buộc | Topic 06 ví dụ | Ví dụ chưa tính thực sự | Queue mục 10 | Thưởng Bắc $=2$, Đông $=-1$, kỳ vọng $0{,}5$; ghi rõ dữ kiện tự đặt | Áp dụng |
| 11 | Bắt buộc | Topic 07 | Thiếu tách tiếp diễn/hữu hạn và công thức tổng hình học | Queue mục 11 | Tách hai công thức $G_t$, nhắc $\gamma=1$ phân kỳ, giải thích $1/(1-\gamma)$ | Áp dụng |
| 12 | Bắt buộc | Topic 09 ví dụ | Trộn hai chính sách trong cùng phân tích | Queue mục 12 | Nêu rõ chính sách (a) xác định và (b) chọn đều từ đầu | Áp dụng |
| 13 | Bắt buộc | Tự kiểm 4, 8 | Câu 4 thiếu giả sử; câu 8 đếm sai | Queue mục 13 | Thêm giả sử $|R_{t+1}|\le10$ mọi bước; đổi "bốn" thành "năm" | Áp dụng |
| 14 | Bắt buộc | Trước tự kiểm | Thiếu mục tổng kết thu hồi mục tiêu | Queue mục 14 | Thêm `## Tổng kết bài`, 5 câu | Áp dụng |
| 15 | Bắt buộc | Topic 11 đáp án | "Trả lời (gợi ý)" không trực tiếp | Queue mục 15 | Đổi thành đáp án trực tiếp, giữ hai tiêu chí | Áp dụng |
| 16 | Bắt buộc | Topic 02 ứng dụng | Tuyên bố quá rộng "mọi bài toán đều đặc tả được" | Queue mục 16 | Thêm quan sát, điều kiện kết thúc, $\gamma$; nói đây là khung đặc tả | Áp dụng |
| 17 | Bắt buộc | Topic 06 hình thức | Nguy cơ hiểu $\pi(s)$ và $\pi(a\mid s)$ mâu thuẫn | Queue mục 17 | Nêu rõ hai ký hiệu cho hai loại chính sách | Áp dụng |
| 18 | Bắt buộc | Topic 04 ví dụ | Tham chiếu mê cung trước khi đặc tả | Queue mục 18 | Thêm "sẽ đặc tả ở topic 09" | Áp dụng |
| 19 | Điều phối viên | Tự kiểm 9, đáp án, Đọc thêm | Phân loại sai hw02 Bài 10 (gán $q_\pi$/Bellman) | Queue mục 19 | Bài 10 chỉ cần S, A, chuyển tiếp, thưởng, kết thúc/tiếp diễn; xếp mở rộng sau topic 09; không đưa lời giải | Áp dụng |
| 20 | Điều phối viên | Đọc thêm | Chưa ghi lý do Bài 5, 6 thuộc bài này | Queue mục 20 | Ghi rằng $\gamma$ và chính sách ngẫu nhiên có ở trang 21–22 cùng hw02 | Áp dụng |

### Phát hiện bị bác

| Phát hiện | Quyết định | Lý do |
|---|---|---|
| Topic 11 thiếu `::: solution` | Bác | Checkpoint đã có câu kiểm tra và khối lời giải. |
| Dùng "kiểm soát" thay "điều khiển" | Bác | Checkpoint dùng "điều khiển" nhất quán ở tiêu đề, định nghĩa, đáp án. |
| Topic 10 không có comment ID | Bác | Có `<!-- note-topic-id: lec-02-topic-10 -->`; chỉ cấp heading sai (đã sửa). |
| Bảng nguồn topic 10–12 để trống | Bác | Bảng đã ghi nguồn; giữ định dạng rõ. |
| Thêm ví dụ mới cho kỳ vọng theo chính sách | Không bắt buộc | Sau sửa mục 10, topic 06 đã đủ cầu nối. |

## Sai khác có chủ ý so với nguồn

1. Sửa chu kỳ trang 15 theo quy ước chuẩn ($S_t, R_t$ nhận trước; $A_t$ chọn; $S_{t+1}, R_{t+1}$ phát).
2. Bổ sung điều kiện hội tụ: tiếp diễn cần $0\le\gamma<1$ và phần thưởng bị chặn; hữu hạn cho phép $0\le\gamma\le1$.
3. Sửa phát biểu MDP trang 18: quan sát đầy đủ không tự nó là định nghĩa MDP; đặc tả hình thức ở bài sau.
4. Chuyển câu hỏi mô hình thế giới (trang 13) tới topic 11, sau định nghĩa mô hình ở topic 07.
5. Không dùng ảnh trang 5–7, 9, 12, 19, 21, 27 (kể cả đồ thị chuyển và bảng đánh số trạng thái mê cung); ví dụ mê cung ba ô là dữ kiện tự đặt.

## Tuân thủ

- No-ai-slop: không câu hỏi tu từ trong lời dẫn, không quảng bá, không câu tổng kết lặp, không lộ chỉ dẫn người viết.
- Mạch viết rà theo Quill; không tạo `quill.json`.
- 12 `note-topic-id` duy nhất giữ nguyên; công thức chỉ dùng `$...$` và `$$...$$`.
- Không thêm Bellman, MRP hoặc $q_\pi$ vào nội dung cốt lõi.

### Recheck lecture note sau sửa

- Toán: requested/observed `deepseek/deepseek-v3.2`, provider OpenRouter, recheck hoàn tất vòng 3; không lỗi chặn bàn giao/nghiêm trọng, bốn điểm nhẹ ở trên.
- Mạch viết: requested/observed `z-ai/glm-5.3-flash`, provider OpenRouter, recheck hoàn tất vòng 3 sau một lượt phục hồi `finish_reason=length`; không lỗi chặn bàn giao/nghiêm trọng, một điểm nhẹ về ánh xạ lặp hw02 Bài 2.
- Ghi quyết định áp dụng năm sửa nhẹ; giữ chu trình rút gọn topic 10/11 vì đây không phải khái niệm cốt lõi độc lập.

### Recheck cuối sau năm sửa nhẹ

- Toán học–thuật toán: `requested_model=observed_model=deepseek/deepseek-v3.2`, provider OpenRouter, profile `recheck`, hoàn tất vòng 2 với `--max-rounds 3 --timeout 300 --max-tokens 3000`. Xác nhận định nghĩa $R_{\max}$, hai miền $\gamma$, trường hợp $\gamma=1$ hữu hạn, cận trên $100$ và điều kiện hội tụ đều đúng; không có lỗi chặn bàn giao hoặc nghiêm trọng.
- Mạch viết: `requested_model=observed_model=z-ai/glm-5.3-flash`, provider OpenRouter, cùng cấu hình, hoàn tất vòng 2. Xác nhận ánh xạ kép hw02 Bài 2 có hai vai trò riêng (phân biệt quan sát ở topic 04; áp dụng tổng hợp ở topic 09), câu nối hai chiều rõ và không trùng chức năng; không có lỗi chặn bàn giao hoặc nghiêm trọng.
- Giữ hai điểm nhẹ không bắt buộc: topic 04 giới thiệu ví dụ mê cung trước topic 09 rồi topic 09 tái dùng ở vai trò tổng hợp; dạng $S_1,\ldots,S_t$ được giữ khi trích đúng công thức trang 17, còn dạng chuẩn của note bắt đầu ở $S_0$ và đã ghi rõ khác biệt.

### Công bố lecture note

- Cổng nội dung Giai đoạn I đạt: đủ 12 `note-topic-id` duy nhất, bản đồ bốn nhóm, công thức đúng cú pháp Markdown, không còn lỗi chặn bàn giao hoặc nghiêm trọng trong năm báo cáo và hai recheck cuối.
- `index.html` đổi trạng thái Ghi chú bài giảng của Bài 02 thành liên kết tĩnh `material-viewer.html?doc=materials/lec-02/lecture-note.md&deck=lecture-02-giao-dien-tac-tu-moi-truong.html`.
- Nhóm hai tài nguyên “Bài giảng / Ghi chú bài giảng” thay thế quy tắc một liên kết duy nhất trong `AGENTS.md` theo yêu cầu cụ thể của `prompt_lecture_note_deck.md`.
- Lệnh bắt buộc `python3 -m reloadserver 8765` chưa chạy được vì môi trường không có mô-đun `reloadserver`; kiểm định trình duyệt cổng 8765 cho note được thực hiện ở bước kế tiếp bằng máy chủ dự phòng cô lập, không chứa `.env`.

### Kiểm định viewer Giai đoạn I

- Lệnh bắt buộc `python3 -m reloadserver 8765` trả `/usr/bin/python3: No module named reloadserver`. Dùng `python3 -m http.server 8765 --bind 127.0.0.1` trên webroot tạm chỉ chứa tài sản công khai; không sao chép `.env`.
- Chromium qua Playwright 1.55.0 mở đúng URL viewer của Bài 02: HTTP 200, tiêu đề đúng, 23 mục lục/tiêu đề, 12 khối lời giải, 305 biểu thức KaTeX, 0 `.katex-error`; không lỗi console, lỗi trang hoặc yêu cầu thất bại.
- Comment `note-topic-id` được loại khỏi DOM hiển thị; liên kết nguồn Markdown và deck đúng; phím Tab đầu tiên tới liên kết bỏ qua nội dung `#material-content`.
- Kiểm tra đường dẫn lệch số bài đạt: ghép note Bài 02 với deck Bài 01 bị từ chối, ẩn bố cục và báo “Số bài của tài liệu không khớp với bộ trang chiếu.” Lỗi console ở ca âm là thông báo có chủ ý từ hàm `fail`, không phải lỗi tải.
- `index.html` trả HTTP 200, có đúng một liên kết deck Bài 02 và một liên kết lecture note Bài 02, không có liên kết tới planning/outline/storyboard/review-log.
- Đã xem ảnh chụp toàn trang viewer ở 1280 × 720; nội dung, bảng, công thức, mục lục và khối lời giải hiển thị đầy đủ, không thấy chồng lấn hoặc phần tử hỏng.

## Pha II — Áp dụng đặc tả đã duyệt (2026-09-03)

### Bằng chứng runtime

| vai trò | requested_model | observed_model | provider |
|---|---|---|---|
| reader lập kế hoạch Pha II | deepseek/deepseek-v3.2 | deepseek/deepseek-v3.2 | OpenRouter |
| writer tuần tự Pha II | z-ai/glm-5.3-flash | z-ai/glm-5.3-flash | OpenRouter |

### Phạm vi và kết quả duyệt

- Chỉ đọc và sửa bốn tệp: `lecture-02-giao-dien-tac-tu-moi-truong.html`, `planning/lec-02/outline.md`, `planning/lec-02/storyboard.md`, `planning/lec-02/review-log.md`; đọc `materials/lec-02/lecture-note.md` làm chuẩn, không sửa. Worker không đọc `.env` và không thêm SVG mới. Worker đã gọi `search_text` khi tự kiểm dù prompt cấm tìm kiếm; truy vấn bị giới hạn ở tệp deck và không chạm nội dung bí mật.
- Kết quả duyệt: hoàn tất toàn bộ sáu hạng mục đặc tả; không còn mục chặn bàn giao hoặc nghiêm trọng. Sai khác có chủ ý được liệt kê riêng bên dưới.

### Hạng mục đã thực hiện

1. Ánh xạ hai chiều 12 note-topic-id → data-slide-id: thêm bảng đầy đủ vào `outline.md` và bảng trang tương ứng trong `storyboard.md`. topic-10 ánh xạ A03, C02, C03 và không tạo C10; topic-11 ánh xạ đúng một trang mới D10, đặt sau D07 trước D08; topic-12 ánh xạ Z00 và ghi chú, không tạo trang riêng. Các mã P00–P02 ghi rõ là trang mở bài không gắn topic. ID trong deck: 40 `data-slide-id` duy nhất (35 tuyến chính + 5 nhánh dọc), đã tự kiểm tra không trùng.
2. D10 mới: mô hình dự báo cục bộ có điều kiện, hai tiêu chí phân biệt với "mô hình hoàn thiện về thế giới" (phạm vi, độ tin cậy), sai số của $\hat p$ khi học từ dữ liệu, vai trò tùy chọn của mô hình và không suy diễn AGI. Dùng HTML/KaTeX, không SVG. Không đặt mã topic vào mặt slide.
3. Z00 và notes cập nhật: đọc thêm Sutton & Barto Chương 3 và David Silver Lecture 2 (ghi rõ phần Bellman thuộc Bài 03); phân tuyến bài tập — Bài 1, 2, 5, 6 chính; Bài 10 mở rộng; Bài 3, 4, 7, 8, 9 để sau Bài 03.
4. Nhánh dọc: thêm X05, X06, X10 sau X02, dùng đúng câu hỏi của hw02; notes có đáp án ngắn (X05: $G_0=3$, $G_1=4$; X06: $0{,}3$, ngẫu nhiên; X10: hướng dẫn năm thành phần) và nguồn `hw02.pdf`. Các trang bài tập ghi rõ nằm ngoài 120 phút.
5. Thời lượng: tuyến chính 35 trang vẫn đúng 120 phút bằng cách giảm cụm dự đoán và điều khiển từ 8 xuống 6 phút, cấp 2 phút cho D10; không đổi 7 mạch ngoài. Tổng kiểm tra lại: $6+14+16+12+12+8+14+6+2+6+20+4=120$.
6. Outline cập nhật ánh xạ nguồn (hw02 Bài 5, 6, 10 và trang 13 → D10), thuật ngữ (mô hình dự báo cục bộ có điều kiện), tài liệu kiểm tra (thêm Silver Lecture 2) và điểm nối Bài 03 (MRP, $q_\pi$, Bellman; phần Bellman của Silver Lecture 2).

### Sai khác có chủ ý trong lượt này

- Phân tuyến hw02 ghi trên Z00 là "Bài 1, 2, 5, 6 chính; Bài 10 mở rộng; Bài 3, 4, 7, 8, 9 sau Bài 03" thay cho ghi trước đây "chỉ Bài 1–2": theo đặc tả Pha II đã duyệt, Bài 5, 6 thuộc Bài 02 vì $\gamma$ và chính sách ngẫu nhiên có trong nội dung bài.
- Cụm dự đoán và điều khiển giảm 2 phút trong storyboard để giữ đúng 120 phút sau khi thêm D10; không đổi luận điểm của cụm.
- X05, X06 dùng câu hỏi của hw02 với đáp án ngắn trong notes, không giữ nguyên văn toàn bộ đề bài dài; ý nhiệm vụ cốt lõi không đổi.

### Giới hạn

- Chưa chạy kiểm định trình duyệt sau sửa; cấu trúc đã tự kiểm tra tĩnh: đủ 7 `<section>` ngoài, 40 `data-slide-id` duy nhất, D10 duy nhất một lần, không có C10, không có `note-topic-id` trên mặt slide hoặc notes, không thêm SVG hay tài nguyên mạng mới.

## Editor tuần tự sau năm review Pha II (2026-09-03)

### Bằng chứng runtime

Lượt đầu của cả năm reviewer Pha II bị loại với lỗi nguyên văn: `model exceeded the tool-call limit (4)`; không tính vào năm báo cáo hợp lệ. Lượt chạy lại của năm reviewer:

| vai trò | requested_model | observed_model | provider |
|---|---|---|---|
| góc nhìn sinh viên | z-ai/glm-5.3-flash | z-ai/glm-5.3-flash | OpenRouter |
| kết nối–mạch viết | z-ai/glm-5.3-flash | z-ai/glm-5.3-flash | OpenRouter |
| chuyên gia Học tăng cường | deepseek/deepseek-v3.2 | deepseek/deepseek-v3.2 | OpenRouter |
| toán học–thuật toán | deepseek/deepseek-v3.2 | deepseek/deepseek-v3.2 | OpenRouter |
| phản biện học thuật–giảng dạy | deepseek/deepseek-v3.2 | deepseek/deepseek-v3.2 | OpenRouter |

requested=observed cho cả hai vai trò; không đổi provider.

### Phát hiện và quyết định

| # | Mức độ | Trang/vị trí | Vấn đề | Bằng chứng | Đề xuất | Quyết định |
|---|---|---|---|---|---|---|
| 1 | nghiêm trọng | D10 | Câu mở chưa là cầu nối vấn đề rõ giữa mô hình một bước (D07) và mô hình hoàn thiện | HTML D10: câu mở chỉ lặp định nghĩa | Viết lại câu mở: mô hình một bước hữu ích nhưng có phạm vi và sai số, nên cần phân biệt với mô hình hoàn thiện; giữ một luận điểm, không quá tải | Áp dụng |
| 2 | trung bình | notes A03 | Hai cách ghi lịch sử dễ nhầm | notes A03 ghi "thay $O$ bằng $S$" chung chung | Làm rõ: notes dùng $H_t$ với $S_t$ ở quan sát đầy đủ; deck dùng $H_t$ với $O_t$ và lịch sử trạng thái ký hiệu $\mathcal H_t^S$; khi $O_t=S_t$ hai cách trùng nhau | Áp dụng |
| 3 | trung bình | C02 | Thiếu cầu nối ngắn sang tiêu chuẩn Markov | Notes C02 dừng ở giải thích ví dụ | Thêm: trạng thái chỉ thay lịch sử khi là bản tóm tắt đủ, dẫn thẳng C03 | Áp dụng |
| 4 | trung bình | outline bảng ánh xạ | topic-03, topic-04 thiếu trang | Bảng ghi topic-03 chỉ C02, C03; topic-04 chỉ C04, C05 | Sửa: topic-03 gồm C00, C02, C03; topic-04 gồm C04, C05, C06, C07 | Áp dụng |
| 5 | nhẹ | outline, storyboard | Chưa ghi lý do giữ thứ tự deck topic-02 trước topic-01 | Note theo thứ tự tín hiệu trước giao diện | Ghi lý do: dựng ranh giới và chỉ số trước khi so sánh tín hiệu; khác thứ tự note nhưng không đổi logic | Áp dụng |
| 6 | trung bình | storyboard D07–D10–D08 | Vai trò/kết nối vào–ra quanh D10 chưa nêu thành dòng | Bảng trang chưa ghi câu nối vào ra hai phía | Cập nhật vai trò và kết nối vào–ra của D10 và hai trang lân cận; giữ 35 trang chính, 7 mạch, 120 phút | Áp dụng |

### Quyết định ghi rõ không áp dụng / giữ nguyên

- Không tạo C10: cầu nối lịch sử → trạng thái được củng cố cục bộ tại A03 và C02–C03; ánh xạ topic-10 giữ nguyên.
- Không thêm hyperlink ngoài: tài nguyên cốt lõi offline và tên nguồn đã có trong notes (Sutton & Barto, Silver Lecture 2).
- Không thêm timeline: thứ tự trang và thời lượng giữ nguyên.
- Giữ công thức $G_t$ hữu hạn trên mặt D04: notes đã nêu tổng vô hạn, $\gamma<1$ và phần thưởng bị chặn; thêm nữa sẽ quá tải mặt slide.
- Bellman ở Bài 03 không mâu thuẫn tiên quyết: Bài 02 chỉ nêu tuyến ở E05/Z00.
- Giữ câu nối X02→X05: cột câu nối mô tả đầu ra sang trang kế, không phải chuỗi phụ thuộc.
- Không sửa `materials/lec-02/lecture-note.md` trong Pha II; note chỉ được dùng làm chuẩn đối chiếu.
- Biên tập thuần Việt theo no-ai-slop; không thêm SVG hay mạng. Tự kiểm sau sửa: cấu trúc HTML không thay đổi (số `<section>`, thứ tự `data-slide-id` giữ nguyên), chỉ chỉnh văn bản trong câu mở D10, notes A03, notes C02.

### Recheck sau sửa Pha II

- Phản biện học thuật–giảng dạy: `requested_model=observed_model=deepseek/deepseek-v3.2`, provider OpenRouter, profile `recheck`, hoàn tất vòng 4. Rà D05–D09 và D10; xác nhận cầu nối D07 → D10 → D08 đã xử lý lỗi nghiêm trọng, D10 đúng vị trí sư phạm, có một luận điểm trung tâm và không quá tải. Không còn lỗi chặn bàn giao hoặc nghiêm trọng.
- Kết nối–mạch viết: `requested_model=observed_model=z-ai/glm-5.3-flash`, provider OpenRouter, profile `recheck`, hoàn tất vòng 2. Rà A03, C00–C07, D05–D10, ranh giới phần và ánh xạ topic 03, 04, 10, 11; xác nhận 7 mạch, 35 trang chính và 120 phút. Không còn lỗi chặn bàn giao hoặc nghiêm trọng.
- Áp dụng hai điểm nhẹ cơ học từ recheck: thống nhất cách gọi “7 mạch, gồm mở bài và kết luận”; đặt D08 là trang nêu vấn đề của vi chu trình dự đoán–điều khiển. Không thêm câu nối lên mặt D07 vì D07 đã dày; câu mở D10 đảm nhiệm rõ kết nối vào. Không thay đổi cấu trúc hoặc nội dung toán học, nên không cần mở thêm lượt recheck.

### Sửa lỗi hiển thị phát hiện bằng Chromium

- Chromium ở khung 1280 × 720 phát hiện công thức C03 và D07 bị cắt ngang. Đây là lỗi chặn bàn giao về khả năng đọc, dù các lượt rà nội dung trước không phát hiện.
- C03 giữ nguyên công thức Markov nhưng xuống thành hai dòng bằng `aligned`.
- D07 được tách thành D07 (quy ước và ví dụ tất định $1/0$) và D07B (định nghĩa phân phối có điều kiện, chuẩn hóa, phân biệt $p$ với $\hat p$). Không thu nhỏ chữ và không thêm SVG.
- Tuyến chính tăng từ 35 lên 36 trang; thời lượng cụm mô hình vẫn 6 phút và tổng vẫn 120 phút. Cấu trúc ngoài vẫn 7 mạch; nhánh bài tập vẫn 5 trang ngoài 120 phút.
- Vì thay đổi công thức và cấu trúc, mở lại recheck toán học–thuật toán, phản biện học thuật–giảng dạy và kết nối–mạch viết cho C02–C05 và D05–D09 trước khi kiểm định trình duyệt lại.

### Recheck sau sửa lỗi hiển thị

- Toán học–thuật toán: `requested_model=observed_model=deepseek/deepseek-v3.2`, provider OpenRouter, profile `recheck`, hoàn tất vòng 4. Xác nhận công thức C03 đúng, D07/D07B giữ đúng miền, chuẩn hóa, ví dụ $1/0$, phân biệt $p$ với $\hat p$ và giả thiết. Không có lỗi chặn bàn giao hoặc nghiêm trọng.
- Phản biện học thuật–giảng dạy: `requested_model=observed_model=deepseek/deepseek-v3.2`, provider OpenRouter, profile `recheck`, hoàn tất vòng 4. Xác nhận trình tự ví dụ → định nghĩa → giới hạn, một luận điểm trung tâm và tải nhận thức phù hợp. Không có lỗi chặn bàn giao hoặc nghiêm trọng. Áp dụng hai đề xuất trung bình: nhắc lại ý nghĩa $G_t$ trên D05 và tách câu mở D10 thành ba câu ngắn.
- Kết nối–mạch viết: `requested_model=observed_model=z-ai/glm-5.3-flash`, provider OpenRouter, profile `recheck`, hoàn tất vòng 3. Xác nhận 7 mạch, 36 trang chính, 5 trang nhánh, 120 phút, ánh xạ topic 07 và tuyến D07 → D07B → D10 → D08. Không có lỗi chặn bàn giao hoặc nghiêm trọng.
- Không áp dụng cảnh báo cú pháp C03 từ báo cáo sư phạm vì kiểm tra nguồn xác nhận đủ `\begin{aligned}`/`\end{aligned}` và Chromium dựng KaTeX không lỗi. Giữ ký hiệu `...` trong lịch sử vì đã có giải thích ở ghi chú. Giữ tổng vô hạn của $G_t$ trong notes D04 để tránh làm trang quá tải.

### Kiểm định cuối Pha II

- Lệnh bắt buộc `python3 -m reloadserver 8765` trả `/usr/bin/python3: No module named reloadserver`. Lần mở `http.server` trong sandbox trả `PermissionError: [Errno 1] Operation not permitted`; sau đó dùng quyền nâng cao để chạy `python3 -m http.server 8765 --bind 127.0.0.1` trên webroot tạm cô lập, không chứa `.env`.
- Chromium qua Playwright kiểm tra toàn bộ 41 trang ở 1280 × 720 và 800 × 600: 36 trang tuyến chính, 5 trang nhánh, 41 `data-slide-id` duy nhất, 41 khối notes, 7 section ngoài. Không còn tràn ngang hoặc dọc sau khi xuống dòng C03 và tách D07/D07B.
- KaTeX dựng 171 biểu thức, không có `.katex-error`. Cả 12 thẻ ảnh có văn bản thay thế; 11 SVG chính đều có `role="img"`; không có ảnh raster hoặc tài nguyên cốt lõi từ mạng. Không có ảnh hỏng, lỗi console, lỗi trang, request thất bại hoặc phản hồi HTTP 4xx/5xx.
- Kiểm tra bàn phím đạt: từ Z00, phím mũi tên xuống mở X01. `index.html` có đúng một liên kết deck Bài 02 và một liên kết lecture note, không có liên kết tới planning. Material-viewer trả HTTP 200, có 23 tiêu đề/mục lục, 12 khối lời giải, không lỗi KaTeX và không lộ comment `note-topic-id`.
- Đã xem trực quan C03, D07, D10 ở 1280 × 720 và Z00 ở 800 × 600; công thức, tiêu đề, thẻ nội dung, chân trang và điều khiển đều nằm trong khung, không chồng lấn.
- Kiểm tra tĩnh cuối: 12 `note-topic-id` đều có ánh xạ trong outline; 7 mạch gồm mở bài và kết luận; tổng thời lượng vẫn 120 phút; 11 SVG được giữ nguyên, không tạo tài sản mới.

### Giới hạn Codex Slides

- Codex Slides không khả dụng trong môi trường hiện tại. Gói `codex-slides-web@0.2.1` yêu cầu Node `>=20`, trong khi runtime là Node `v18.19.1`.
- Lệnh kiểm tra `npm run dev:status` dừng với `Error [ERR_REQUIRE_ESM]` khi Electron gọi `@electron/get`, sau đó báo `Electron failed to install correctly`. Vì vậy không tuyên bố đã rà bằng Codex Slides; kiểm định trực quan cuối dùng RevealJS cục bộ và Chromium headless như ghi trên.
