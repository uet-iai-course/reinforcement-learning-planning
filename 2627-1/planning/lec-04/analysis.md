# Phân tích học thuật và thiết kế Bài 04

Bài 04 — Giải MDP bằng quy hoạch động. Học phần Học tăng cường, học kỳ 1 năm học 2026–2027. Người học: sinh viên đại học đã học học máy, học sâu và thuật toán; tiên quyết dùng trực tiếp là MDP, xác suất có điều kiện, tổng chiết khấu, vector, chuẩn vô cùng được định nghĩa lại và hệ tuyến tính.

Vấn đề trung tâm: từ mô hình chuyển–thưởng đã biết, tính giá trị của một chính sách, cải thiện lựa chọn và tìm chính sách tối ưu có điều kiện kiểm chứng. Phần trình chiếu gồm **45 trang, 7 mạch, 120 phút**; thời gian đã gồm các câu kiểm tra riêng và chữa ngắn. **30 phút còn lại của buổi 150 phút dành cho chữa bài tập** theo nguồn; không tự tạo code demo vì PDF và tài liệu tuần 4 không có chương trình.

Đây là bản dàn bài mới, không dùng dàn bài cũ làm khung. Chỉ dẫn cụ thể của người dùng cho phép thay thứ tự nguồn để theo Sutton–Barto chương 4: đánh giá → cải thiện → lặp chính sách → lặp giá trị → bất đồng bộ/GPI/hiệu quả. Chủ đề và dữ kiện của PDF nguồn được bảo toàn qua ánh xạ đủ 38 trang. Kế hoạch đã được chấp nhận và triển khai ngày 2026-09-28. Năm vai đã rà độc lập cùng bản cố định; các sửa cục bộ sau rà được cập nhật trong hồ sơ này. Bằng chứng kiểm định và trạng thái rà lại nằm trong review-log.md.

## Mục tiêu học tập

| Mã | Năng lực quan sát được | Kiểm tra chính |
|---|---|---|
| MT1 | Xác định mô hình, chính sách, phần thưởng và tổng chiết khấu trong bài toán lập kế hoạch. | Kiểm tra mở đầu |
| MT2 | Tính một lượt đánh giá đồng bộ, phân biệt $V_k$ với $v_\pi$, dùng phần dư đánh giá. | Kiểm tra đánh giá chính sách |
| MT3 | Tính $q_\pi$, chọn hành động cải thiện và giải thích vì sao giá trị không giảm dưới giả thiết. | Kiểm tra cải thiện |
| MT4 | Thực hiện một lần lặp chính sách và phân biệt bảo đảm đánh giá chính xác với dừng gần đúng. | Kiểm tra lặp chính sách |
| MT5 | Thực hiện lặp giá trị, trích chính sách và kiểm tra phần dư trên đúng bảng trả về. | Kiểm tra lặp giá trị; kiểm tra tổng hợp |
| MT6 | So sánh đồng bộ, tại chỗ, bất đồng bộ; nêu điều kiện lịch, chi phí và giới hạn mô hình. | Kiểm tra thực hành; kiểm tra tổng hợp |

## Học liệu và mức truy cập

| Mã | Tài liệu, tác giả/đơn vị, năm | Đường dẫn hoặc URL | Vị trí đã đọc và vai trò |
|---|---|---|---|
| NG1 | Tạ Việt Cường, “Giải bài toán MDPs với Quy Hoạch động”, 19-03-2026; PDF Beamer | `RL-hk2-2025-2026/lecture04-solving-MDP.pdf` | Đủ 38 trang; số in trùng số PDF. Nguồn chủ đề, ví dụ, bảng, hình và bài toán CartPole. |
| NG2 | Richard S. Sutton, Andrew G. Barto, *Reinforcement Learning: An Introduction*, ấn bản 2, bản quyền 2018/2020 | [PDF của tác giả](http://incompleteideas.net/book/RLbook2020.pdf) | Ch. 4, tr. in 73–89/PDF 95–111; Ch. 3, §3.1 tr. 47–49, §3.3–3.5 tr. 54–59, §3.6 tr. 62–65. Sườn mới theo yêu cầu người dùng, hệ ký hiệu và kiểm chứng. |
| NG3 | Tạ Việt Cường, “Bài tập tuần 4 – Đánh giá chính sách”, 26-03-2026 | `RL-hk2-2025-2026/resources/hw04.pdf` | Toàn bộ 1 trang: hai trạng thái, lưới nhiễu; câu Monte Carlo/sai phân thời gian ngoài phạm vi. |
| NG4 | Phiếu bài tập `hw3.pdf`; không suy đoán thêm tác giả/năm từ tên tệp | `RL-hk2-2025-2026/resources/hw3.pdf` | Đủ 4 trang được tác tử nguồn kiểm kê; các bài 1–9 ở tr. 1–2 hỗ trợ tiên quyết và chữa bài; phần sau vượt phạm vi. |
| NG5 | Stanford CS234, Emma Brunskill, Winter 2026, Lecture 2, *Making Sequences of Good Decisions Given a Model of the World*; bộ 58 trang | [PDF bài giảng](https://web.stanford.edu/class/cs234/slides/lecture2pre.pdf), [trang môn](https://web.stanford.edu/class/cs234/) | Tr. 1–42, 49–51; xem hình tr. 13. Đối chiếu bố cục học thuật, ví dụ tính và câu kiểm tra; không thay nguồn toán chính. |
| NG6 | UCL, David Silver, Advanced Topics 2015, Lecture 3, *Planning by Dynamic Programming*; bộ 42 trang | [PDF bài giảng](https://davidstarsilver.wordpress.com/wp-content/uploads/2025/04/lecture-3-planning-by-dynamic-programming-.pdf), [trang giảng dạy](https://davidstarsilver.wordpress.com/teaching/) | Tr. 1–31, 35–42; xem hình tr. 10. Đối chiếu trực giác, cập nhật và phụ lục hội tụ. Năm đường dẫn 2025 không phải niên khóa. |
| NG7 | Bài 03 và cấu trúc kỹ thuật hiện có trong kho | `2627-1/lecture-template.html`, `2627-1/lecture-slide.css`, `2627-1/index.html`; bài giảng và ghi chú Bài 03 | Mẫu/CSS/index đã đọc để giữ cấu trúc, không lấy nội dung bài mẫu. Tác tử nguồn kiểm tra ký hiệu Bài 03 và đầu ra: so sánh $q_\pi$ chưa tự chứng minh tối ưu. |

NG2 được tải đủ 548 trang, 73.129.769 byte; SHA-256 `2dd0d71d9ee883fbeb99f9b888c65ac3255fae2512203d11b18e838befffe9a6`. Bản HTTPS gặp lỗi chứng chỉ/502; bản HTTP hoàn chỉnh được đọc bằng công cụ PDF. Văn bản trích mất một số dấu âm và ký tự $\gamma$, nên các công thức được đối chiếu nội dung gốc và báo cáo số. Công cụ chụp PDF Stanford gặp lỗi bộ nhớ đệm; tác tử nghiên cứu đã tải PDF và xem ảnh cục bộ. Không dùng tài liệu chưa đọc làm bằng chứng.

Các báo cáo nguồn độc lập được điều phối viên chấp nhận: `/tmp/rl04-rebuild/source-report.md`, `research.md`, `numeric-report.md`. Tác tử soạn trực tiếp đọc bản trích đủ 38 trang và §4.1–4.8 của sách; chi tiết kiểm kê hw3, Bài 03 và hai bộ đại học dựa trên báo cáo đọc độc lập nêu rõ ở trên.

## Đối chiếu hai bộ trang chiếu đại học

| Nguồn | Quan sát trực tiếp theo trang | Nhận định và quyết định cho bài mới |
|---|---|---|
| Stanford/NG5 | Tr. 5–13 nối mô hình với đánh giá; tr. 13 có tính một bước; tr. 18–31 xây dựng cải thiện/lặp chính sách; tr. 32–42 có lặp giá trị và hội tụ. | Giữ nhịp cơ chế–bài tính–kiểm tra, nhưng đặt bước tính tay trước công thức tổng quát theo quy ước địa phương. Không sao chép lỗi tr. 38 thiếu hệ số co nhỏ hơn 1 và tr. 34 khởi chỉ số không nhất quán của bản pre. |
| UCL/Silver/NG6 | Tr. 5 phân biệt dự đoán/điều khiển; tr. 7–11 theo dõi lưới; tr. 16–18 nối cải thiện, đánh giá cắt ngắn và lặp giá trị; tr. 27–29 tách bất đồng bộ/tại chỗ; tr. 37–42 bổ sung chứng minh. | Giữ một ví dụ qua nhiều cơ chế và sơ đồ các nhánh cập nhật. Dùng hai trạng thái từ nguồn địa phương thay lưới của Silver. Giữ phác thảo co đủ dùng, không biến phụ lục chứng minh thành trục chính. |

Quan sát nguồn và lựa chọn sư phạm được tách riêng. Hai bộ từ hai trường đã đủ căn cứ đối chiếu; không bổ sung bộ thứ ba chỉ để tăng số lượng. Không chép tài sản hay CSS. Bố cục theo mẫu/CSS cục bộ: một luận điểm mỗi trang, hình hoặc công thức lớn, ví dụ số dùng lại và kiểm tra sau cụm.

## Khái niệm và quan hệ phụ thuộc

| Mã | Vai trò | Tiên quyết | Năng lực và phân biệt cần kiểm | Đầu ra dùng tiếp |
|---|---|---|---|---|
| KN0: mô hình, tổng thưởng, chính sách | Nhắc lại | Xác suất, quỹ đạo Markov | MT1: trạng thái/quan sát; mô hình/chính sách; thưởng/tổng thưởng | Đánh giá chính sách |
| KN1: đánh giá chính sách | Trọng tâm, thuật toán và khái niệm | KN0; bảng ước lượng, kỳ vọng | MT2: tính lượt; phân biệt $V_k,v_\pi$; bảng cũ/mới | Căn cứ chọn hành động |
| KN2: cải thiện chính sách | Trọng tâm, khái niệm và quy tắc | KN1; giá trị tiếp nối | MT3: tính $q_\pi$ và hành động mới; một thay đổi đầu tiên/đổi chính sách vĩnh viễn | Chu trình điều khiển |
| KN3: lặp chính sách | Trọng tâm, thuật toán | KN1–KN2; đánh giá chính xác | MT4: lần theo chu trình; giữ hòa; ổn định gần đúng/điểm tối ưu | Giới hạn chi phí đánh giá đầy đủ |
| KN4: lặp giá trị | Trọng tâm, thuật toán | KN2–KN3; cực đại và giá trị tiếp nối | MT5: tính cập nhật tối ưu, chính sách trích, phần dư đúng bảng | Tổ chức lịch tính toán |
| KN5: bất đồng bộ | Trọng tâm ở mức một trạng thái, thuật toán | KN1/KN4; bảng hiện có | MT6: tại chỗ/bất đồng bộ; điều kiện mọi trạng thái được cập nhật | Phân bổ chi phí và giới hạn |
| KN6: GPI | Hỗ trợ tổng hợp | KN1–KN5 | MT6: nhận diện hai quá trình; không coi mọi xen kẽ đều có bảo đảm | So sánh phương pháp |
| KN7: rời rạc hóa CartPole | Ứng dụng giới hạn | Mô hình Markov, chi phí bảng | MT6: 324 ô biểu diễn không tự cung cấp mô hình | Kiểm tra điều kiện sử dụng |
| KN8: lưới ngẫu nhiên | Luyện tập tổng hợp | KN4; kỳ vọng và terminal | MT2/MT5: trọng số xác suất và thưởng của chuyển thực tế | Bài tập có lời giải kiểm chứng |

Đồ thị phụ thuộc là KN0 → KN1 → KN2 → KN3 → KN4 → KN5; KN6 tổng hợp KN1–KN5, KN7 kiểm giới hạn mô hình, KN8 dùng lại KN4. Tính co theo chính sách được đặt trong đánh giá để hỗ trợ chứng minh cải thiện; tính co tối ưu xuất hiện sau ví dụ lặp giá trị. Bellman tối ưu không mở đầu bài vì khi đó chưa có nhu cầu chọn hành động từ một bảng giá trị. Định lý tối ưu ở lặp chính sách được phát biểu với giả thiết, sau đó tính duy nhất được chứng minh trong lặp giá trị; không lấy suy luận vòng làm chứng minh.

## Phiếu lựa chọn cho từng khái niệm trọng tâm

### KN1 — Đánh giá chính sách

Vấn đề là tổng thưởng vô hạn của chính sách $(a,a)$ chưa được tính. Trực giác dùng thưởng một bước cộng giá trị tiếp nối. Ví dụ tính hai lượt $(0,0)\to(1,2)\to(1.9,2.9)$ trước định nghĩa $v_\pi$, $T_\pi$ và quy trình. Ứng dụng giải hệ được $(10,11)$; kiểm tra lượt tiếp theo và phần dư. Sơ đồ có một trạng thái gốc, nhánh theo chính sách và mô hình; bảng cũ/mới tách rõ. Phương án mở bằng hệ ma trận bị loại vì che cơ chế cập nhật; hệ tuyến tính được giữ như đối chiếu. Lưới $4\times4$ của sách chuyển đọc thêm vì $\gamma=1$ cần giả thiết riêng. Hình thức hóa HT1–HT5. Kết quả giá trị chính xác trở thành dữ kiện của nhìn trước một bước.

### KN2 — Cải thiện chính sách

Vấn đề là chọn hành động tốt hơn khi đã có $v_{\pi_0}=(10,11)$. So sánh tại $s_1$ cho 11 và 12.9 trước định nghĩa $q_\pi$. Quy tắc tham lam và định lý được phác thảo bằng đơn điệu và hội tụ $T_{\pi'}$. Ứng dụng tạo $(a,b)$ rồi đánh giá được $(10,30)$; kiểm tra tại $s_0$ cho 10 và 27. Hình hai nhánh đều ghi tiếp tục theo chính sách cũ. Không dùng riêng thưởng tức thời để giải thích tham lam; không gọi 12.9 là giá trị 30 của chính sách mới. Hình thức hóa HT6–HT7. Bước đánh giá còn thiếu của nguồn được khôi phục để tạo nhu cầu lặp.

### KN3 — Lặp chính sách

Vấn đề là một lần cải thiện chưa tối ưu. Trực giác xen kẽ hai đối tượng cố định; ví dụ đủ chuỗi $(a,a)\to(a,b)\to(b,b)$ trước giả mã. Quy trình dùng đánh giá chính xác, giữ hành động cũ khi hòa và trả cặp chính sách–giá trị tương ứng. Ứng dụng kiểm nghiệm $(27,30)$ thỏa lựa chọn tham lam; kiểm tra phản ví dụ bảng $V=0$ làm $(a,b)$ ổn định nhưng chưa tối ưu. Sơ đồ có nhãn hai đầu ra, không chỉ vòng lặp trang trí. Phương án dùng đánh giá theo ngưỡng nhưng tuyên bố dừng tối ưu chính xác bị loại; xấp xỉ được nêu như giới hạn riêng. Hình thức hóa HT8–HT10. Chi phí đánh giá đầy đủ dẫn tới lặp giá trị.

### KN4 — Lặp giá trị

Vấn đề là giảm mức hoàn tất đánh giá trước khi cải thiện. Trực giác chọn nhánh lớn nhất, ví dụ $V_1=(1,3)$ và $V_2=(2.7,5.7)$ trước $Q_V,T_*$. Quy trình đồng bộ trả bảng đã kiểm phần dư; chứng minh co dùng bất đẳng thức cực đại và tổng xác suất. Ứng dụng lưới năm ô giữ bảng nguồn, bổ sung biên trái và kiểm $V_5=V_4$; kiểm tra hai ô của lượt kế. Lưới bổ sung biểu diễn đường lan truyền, còn hai trạng thái giữ liên tục khi so sánh thuật toán. Hình thức hóa HT11–HT14. Không lấy chính sách sớm ổn định làm chứng minh giá trị đã hội tụ. Đầu ra cần được tính hiệu quả khi mô hình lớn.

### KN5 — Quy hoạch động bất đồng bộ

Vấn đề là quét toàn bảng có thể tốn nhiều tính toán. Ví dụ tại chỗ cho $(1,2.9)$ thay $(1,2)$, rồi lưới quét ngược cho phép thấy giá trị mới lan truyền. Quy trình chọn từng trạng thái dùng bảng mới nhất, kèm giả thiết mọi trạng thái được cập nhật vô hạn lần trong xét hội tụ. Ứng dụng trên lưới kiểm phần dư toàn cục bằng 0 sau quét ngược; kiểm tra lịch bỏ $s_1$ và điều kiện mô hình. Không đồng nhất với xử lý song song, không bàn trường hợp giá trị truyền trễ. Hình thức hóa HT15–HT16. GPI ở HT17 dùng chu trình rút gọn vì tổng hợp hai thao tác đã học, không phải thuật toán trọng tâm mới.

## Danh mục hình thức hóa và mức chứng minh

Miền chung cho các bảo đảm: $\mathcal S,\mathcal A(s)$ hữu hạn, phần thưởng bị chặn, mô hình đã biết, $0\le\gamma<1$, bảng khởi tạo hữu hạn. Trạng thái kết thúc nếu có luôn có giá trị 0. “Chính xác” là giá trị toán học, khác với kết quả số theo ngưỡng.

| Mã và loại | Nội dung chính xác, ý nghĩa | Mức trình bày và căn cứ | Nơi dùng |
|---|---|---|---|
| HT1, định nghĩa/phương trình | $v_\pi(s)=\mathbb E_\pi[G_t\mid S_t=s]$ và Bellman kỳ vọng | Phát biểu, giải thích từng trọng số; NG2 (4.3)–(4.4), tr. 74/PDF 96 | Đánh giá và hệ ví dụ |
| HT2, định nghĩa toán tử | $T_\pi$ là tổng theo $\pi,p$ của $r+\gamma V(s')$ | Ánh xạ trực tiếp từ hai lượt tính; NG1 tr. 10,14; NG2 (4.5), tr. 74 | Quy tắc đồng bộ và chứng minh |
| HT3, thuật toán/định nghĩa | Đồng bộ hai bảng, phần dư $b_\pi(V)=\|T_\pi V-V\|_\infty$ | Quy trình đầy đủ trong outline; phần dư trả đúng bảng là bổ sung suy luận | Kiểm tra độ chính xác đánh giá |
| HT4, định lý/hệ quả | $\|T_\pi U-T_\pi V\|_\infty\le\gamma\|U-V\|_\infty$; sai số không quá $b_\pi(V)/(1-\gamma)$ | Phác thảo trọng số không âm và tam giác; phát triển từ NG1 tr. 31–32, NG2 tr. 74–75 cho hội tụ | Cải thiện chính sách, tiêu chuẩn dừng |
| HT5, biểu diễn tuyến tính | $(I-\gamma P_\pi)v_\pi=r_\pi$, kích thước $n\times n$ và $n$ | Đối chiếu, không chứng minh nghịch đảo trong tuyến chính; NG1 tr. 6; NG2 tr. 74 | Nghiệm $(10,11)$ và đánh giá chính xác |
| HT6, định nghĩa | $q_\pi(s,a)=\sum_{s',r}p(s',r\mid s,a)[r+\gamma v_\pi(s')]$; $v_\pi=\sum_a\pi q_\pi$ | Định nghĩa + áp dụng; NG2 (4.6), tr. 78/PDF 100 | Chọn hành động |
| HT7, định lý | Nếu $q_\pi(s,\pi'(s))\ge v_\pi(s)$ mọi $s$, thì $v_{\pi'}\ge v_\pi$ | Phác thảo lặp toán tử đơn điệu; NG1 tr. 21, NG2 (4.7)–(4.9), tr. 78–79 | Cải thiện và dừng PI |
| HT8, thuật toán | Đánh giá chính xác → tham lam giữ hòa → kiểm ổn định | Đầu vào/ra, ngân sách, terminal, giá trị cố định trong outline; NG1 tr. 20; NG2 tr. 80,82 | Điều khiển trên ví dụ hai trạng thái |
| HT9, định nghĩa/định lý | $v_*=\max_\pi v_\pi$, $q_*=\max_\pi q_\pi$; chính sách tham lam theo giá trị của nó thỏa Bellman tối ưu | Phát biểu tồn tại và lập luận điểm bất động; NG1 tr. 7–9; NG2 §3.6, tr. 62–65; tr. 79–80 | Chứng nhận chính sách ổn định |
| HT10, định lý | PI chính xác với giữ hòa dừng hữu hạn; số chính sách $\prod_s\lvert\mathcal A(s)\rvert$ | Phác thảo cải thiện nghiêm ở ít nhất một trạng thái + hữu hạn; NG1 tr. 33, NG2 tr. 80, Ex. 4.4 tr. 82 | Giới hạn đánh giá gần đúng |
| HT11, định nghĩa | $Q_V=\sum p[r+\gamma V]$, $(T_*V)(s)=\max_aQ_V(s,a)$ | Giải thích max sau kỳ vọng; NG1 tr. 8,10,23; NG2 (4.10), tr. 83 | Lặp giá trị và trích chính sách |
| HT12, thuật toán | Đồng bộ $V\leftarrow T_*V$, trích $\pi_V$ theo đúng bảng trả và đo $b_*(V)$ | Quy trình đầy đủ trong outline; điều chỉnh ngưỡng có căn cứ; NG1 tr. 24,34; NG2 tr. 83 | Nghiệm gần đúng có phần dư |
| HT13, định lý | $T_*$ co hệ số $\gamma$, $\|V_k-v_*\|_\infty\le\gamma^k\|V_0-v_*\|_\infty$ | Phác thảo bất đẳng thức max và chuẩn; NG1 tr. 31–32 | Hội tụ và tính duy nhất |
| HT14, hệ quả tự suy | $\|V-v_*\|_\infty\le b_*(V)/(1-\gamma)$ | Ba dòng tam giác + co; không gán nguyên công thức cho sách Ch. 4 | Ngưỡng sai số $0.1\Rightarrow b\le0.01$ khi $\gamma=0.9$ |
| HT15, đếm chi phí | Một lượt tối ưu $O(n^2m)$ đặc, $O(nmd)$ thưa; mô hình đặc $O(n^2m)$, bảng $O(n)$ | Đếm số nhánh khi thưởng đã gộp; NG2 §4.7 cho bối cảnh, không gán số phép toán tự đếm cho sách | Lịch cập nhật và CartPole |
| HT16, thuật toán/định lý | Một trạng thái dùng bảng hiện có; mọi trạng thái cập nhật vô hạn lần thì hội tụ dưới giả thiết chung | Phát biểu và áp dụng, không chứng minh bất đồng bộ đầy đủ; NG2 §4.5 tr. 85–86 | Kiểm tra lịch |
| HT17, khái niệm/hệ quả | GPI phối hợp đánh giá và cải thiện; điểm chung chính xác $V=v_\pi$, $\pi$ tham lam theo $V$ là tối ưu | Tổng hợp từ cơ chế đã học; NG2 §4.6 tr. 86–87 | So sánh thuật toán; không bảo đảm mọi xấp xỉ |

## Quyết định về ví dụ và hình

Ví dụ hai trạng thái giữ nguyên thưởng $(1,0,2,3)$ và $\gamma=0.9$ của NG1 tr. 17–19. Nó cho đủ hai lần cải thiện và đối chiếu cùng mô hình giữa đánh giá, PI, VI. Lưới năm ô bổ sung trực giác lan truyền và trạng thái kết thúc; không thay ví dụ trung tâm. Lưới ngẫu nhiên lấy dữ kiện NG3 và bổ sung công khai biên/thưởng/yêu cầu. Lưới $4\times4$ không chiết khấu của sách, bài thuê xe và con bạc không vào tuyến chính vì thêm dữ kiện, giả thiết hoặc yêu cầu mã vượt thời lượng và nguồn được chọn.

Tất cả hình dự kiến là SVG có mô tả thay thế; bảng dùng HTML, công thức dùng KaTeX, giả mã dùng văn bản HTML. Không có hình thực nghiệm, ảnh chụp hoặc logo cần ngoại lệ raster. Tên mới dùng tiền tố `dp04-` để không ghi đè năm SVG đang phục vụ ghi chú chuyên sâu với bộ số khác. Đặc tả từng hình nằm trong outline và storyboard.

## Phạm vi, sai khác và giới hạn bàn giao kế hoạch

Thứ tự mới được người dùng yêu cầu; không chỉ sắp xếp cục bộ nguồn. Bốn mục lục lặp bỏ trang riêng; các công thức tối ưu và hội tụ chuyển về nơi có nhu cầu. Ma trận và Bellman $q$ giữ trong ghi chú; các điều kiện bị thiếu được bổ sung có nguồn. Bảng ánh xạ từng trang nằm trong outline; lý do từng trang và chu trình học tập nằm trong storyboard.

Không có phần thực hành mã riêng. 30 phút chữa bài dự kiến: 15 phút lưới ngẫu nhiên tuần 4, 10 phút lần theo PI và lỗi dừng gần đúng, 5 phút đối chiếu điều kiện mô hình. Bài 9 của hw3 là bài thêm nếu người học cần luyện ở nhà, không cộng vào 150 phút. Câu Monte Carlo/sai phân thời gian và các bài Q-learning/xấp xỉ hàm không đưa vào tuyến chính.

Các số được kiểm chứng độc lập bằng phân số hữu tỉ: đánh giá $(10,11)$; chuỗi PI $(a,a)\to(a,b)\to(b,b)$ và giá trị $(10,11)\to(10,30)\to(27,30)$; VI $(1,3),(2.7,5.7),(5.13,8.13),(7.317,10.317)$; lưới xác định $(4.58,6.2,8,10,0)$; lưới nhiễu $V_1=(-1,-1,-1,7.8,0)$, $V_2(c_3)=4.436$. Chi tiết phép tính và các giả thiết bổ sung đã được chấp nhận ở báo cáo số. Các phép kiểm số trên thuộc giai đoạn lập kế hoạch. Bản HTML sau triển khai đã được năm vai rà trên cùng bản cố định; mọi kiểm định sau sửa được ghi riêng trong review-log.md.


## Quyết định sau rà độc lập — 2026-09-28

Năm vai chấp nhận tuyến bảy mạch; sửa cục bộ miền trạng thái, ví dụ chính sách ngẫu nhiên, phần dư trước định nghĩa, tín hiệu đổi mô hình và toán tử, câu nối tới CartPole và thuật ngữ. Hai quy trình chính trong ghi chú được thống nhất với deck về số lần nhận bảng mới và bảng đã kiểm; bộ số riêng được giữ. Quyết định theo trang ở storyboard.md và hồ sơ từng phát hiện ở review-log.md. Không thay thứ tự, số trang hoặc thời lượng.
