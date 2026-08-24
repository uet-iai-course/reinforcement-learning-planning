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
- Đạt: không có dấu gạch ngang dài, khẩu hiệu, câu cảm thán hoặc nhịp câu kịch tính.

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
