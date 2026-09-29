# Phân tích xây dựng lại Bài 06: Điều khiển phi mô hình

Ngày lập: 29-09-2026. Đây là bản phân tích mới từ PDF nguồn và các báo cáo nghiên cứu đã được điều phối viên chấp nhận. Không kế thừa dàn bài, HTML hay học liệu Bài 06 cũ. Trạng thái ngày 29-09-2026: đã triển khai HTML, bảy SVG và học liệu; năm báo cáo độc lập trên bản cố định đã được điều phối viên chấp nhận. Bản sau biên tập đã hoàn tất tái kiểm toán học và mạch viết, kiểm hiển thị rộng/hẹp và đối chiếu Codex Slides. Bằng chứng, phạm vi và giới hạn được ghi trong review-log.

## 1. Bài toán giảng dạy

Bài học thuộc học phần **Học tăng cường**, học kỳ 1 năm học 2026–2027. Người học là sinh viên đại học đã học học máy, học sâu và thuật toán; cần dùng kiến thức về quá trình quyết định Markov (MDP), kỳ vọng có điều kiện, giá trị trạng thái, đánh giá và cải thiện chính sách, Monte Carlo (MC), sai phân thời gian (TD). Các tiên quyết này được nhắc ở phần mở đầu và ngay trước chỗ dùng; không giả định đã học lý thuyết xấp xỉ ngẫu nhiên.

**Vấn đề trung tâm:** khi chỉ có các lượt hoặc các chuyển tiếp lấy mẫu, xây dựng bảng giá trị hành động để chọn hành động tại D của chuỗi A–E; xác định dữ liệu, mục tiêu cập nhật và điều kiện cần để kết quả học có bảo đảm.

Môi trường được công bố đầy đủ cho phép kiểm tra phép tính. Thuật toán chỉ nhận mẫu và tập hành động hợp lệ, không truy cập bảng chuyển hay bảng thưởng để tính kỳ vọng. Vì vậy việc người đọc biết mô hình minh họa không biến quy trình học thành quy hoạch động.

| Mã mục tiêu | Sản phẩm có thể đánh giá | Trang kiểm tra |
|---|---|---|
| MT1 | Phân biệt dự đoán và điều khiển; diễn giải giá trị đúng $q_\pi$ khác bảng $Q$, xác định phần thông tin thiếu trong một mẫu | A05, B07 |
| MT2 | Tính phân phối $\varepsilon$-tham lam, kể cả đồng hạng; phân biệt chính sách hành vi và chính sách đích | B07, E08 |
| MT3 | Tính lợi tức, chọn lần ghé đầu của cặp, cập nhật MC với bộ đếm riêng và xác định thời điểm cải thiện chính sách | C08 |
| MT4 | Thực hiện Sarsa theo đúng thứ tự chọn hành động tiếp theo, cập nhật và xử lý kết thúc | D08 |
| MT5 | Thực hiện Q-learning từ cùng dữ liệu, giải thích khác biệt mục tiêu và điều kiện hai mục tiêu trùng nhau | E08 |
| MT6 | Kiểm tra giả thiết bao phủ, lịch bước học, giới hạn tham lam và miền chiết khấu; phân biệt dừng thực hành với hội tụ | F05, G03 |
| MT7 | Chọn phương pháp theo loại dữ liệu và mục tiêu học, giải thích kết quả hữu hạn mẫu đối với quyết định tại D | G03 |

Phần trình chiếu gồm **45 trang, 7 mạch, 120 phút**, đã tính thời gian trả lời và chữa bảy trang kiểm tra. Phần chữa bài riêng kéo dài **30 phút**, dùng lại bài nguồn và phần bảng tra của H03; không có code demo mới vì nguồn không cung cấp code. Ngoài tuyến chính: xấp xỉ hàm, thuật toán sâu, nhiều bước, vết đủ điều kiện, chứng minh xấp xỉ ngẫu nhiên, công thức hiệu chỉnh khác chính sách và chặn đánh giá hữu hạn mẫu. Hai nội dung cuối đã được triển khai tại §§7.4–7.5 của [học liệu](../../materials/lec-06/lecture-note.md), theo đặc tả đọc thêm ở mục 7 của bản phân tích này.

## 2. Học liệu và mức truy cập

Số trang L06 là trang PDF đếm từ 1, đồng thời trùng số trang in. Số trang SB là trang in; trang PDF bằng trang in cộng 22. Mã nguồn được dùng thống nhất trong outline và storyboard. Phạm vi đọc dưới đây tổng hợp việc đọc của tác tử phân tích, nghiên cứu, kiểm toán và điều phối viên đã được chấp nhận; không khẳng định tác tử soạn tự xem mọi ảnh.

| Mã | Tài liệu, loại, tác giả/đơn vị, năm | Đường dẫn hoặc URL | Vị trí đã đọc; trạng thái và vai trò |
|---|---|---|---|
| L06 | *Lecture 06: Điều khiển phi mô hình*, PDF 30 trang, Tạ Việt Cường | [Nguồn trong kho](../../../RL-hk2-2025-2026/lecture-06-model-free-control.pdf) | Đọc và kiểm kê 30/30 trang; tác tử phân tích xem đủ 30 trang, root xem riêng 15, 19, 24, 25, 29. Nguồn bắt buộc. Không xác minh được tên đơn vị từ PDF; ngày tạo tệp không được dùng làm niên khóa. |
| SB | Sutton và Barto, *Reinforcement Learning: An Introduction*, ấn bản 2, bản quyền 2018, 2020; giáo trình | [Trang sách của tác giả](https://incompleteideas.net/book/the-book-2nd.html) | Đọc bản PDF được cung cấp: §4.2 tr. 76–79, §4.6 tr. 86–87; §§5.1–5.7 tr. 91–105, 109–111; §6.2 tr. 124, §§6.4–6.5 tr. 129–132; §§7.3–7.4 tr. 148–150. Sườn khái niệm, thuật toán và kiểm chứng. Tệp nằm trong bộ tài liệu làm việc; chưa xác minh lại bản tải trên trang sách. |
| H02 | Bài tập, Tạ Việt Cường, 12-03-2026, 2 trang | [hw02.pdf](../../../RL-hk2-2025-2026/resources/hw02.pdf) | Đọc toàn bộ; bài 4, 6, 7, 9 hỗ trợ tiên quyết chính sách, quá trình phần thưởng Markov, $v_\pi$–$q_\pi$. |
| H03 | Bài tập, Tạ Việt Cường, 08-05-2026, 4 trang | [hw3.pdf](../../../RL-hk2-2025-2026/resources/hw3.pdf) | Đọc toàn bộ; Bài 10 tr. 2–3 dùng cho chữa MC lần ghé đầu/Q-learning. Môi trường sáu trạng thái, tách khỏi A–E. Lược phần xấp xỉ hàm. |
| H04 | Bài tập, Tạ Việt Cường, 26-03-2026, 1 trang | [hw04.pdf](../../../RL-hk2-2025-2026/resources/hw04.pdf) | Đọc toàn bộ; không bổ sung dữ kiện điều khiển trực tiếp. Không kế thừa số bài tập bị lặp. |
| H05 | Bài tập dự đoán phi mô hình, 2 trang | [hw05-model-free-prediction.pdf](../../../RL-hk2-2025-2026/resources/hw05-model-free-prediction.pdf) | Đọc toàn bộ; câu 1, 3, 5 phục vụ ôn MC/TD/bước học. Không dùng so sánh tốc độ chung ở câu 4 làm bảo đảm. |
| H07 | Bài tập xấp xỉ hàm, Tạ Việt Cường, 08-04-2026, 3 trang | [hw07-function-approximation.pdf](../../../RL-hk2-2025-2026/resources/hw07-function-approximation.pdf) | Đọc toàn bộ; Bài 7 tr. 2 cho lượt D–C–B–A. Bài 8 có hành động kế tiếp không nối khớp; không dùng nguyên dữ liệu đó cho Sarsa. |
| UCL | David Silver, UCL, *Lecture 5: Model-Free Control*, COMPM050/COMPGI13, niên khóa 2015; slide 43 trang | [Trang giảng viên](https://davidstarsilver.wordpress.com/teaching/), [PDF](https://davidstarsilver.wordpress.com/wp-content/uploads/2025/04/lecture-5-model-free-control-.pdf) | Đọc tr. 1–25, 31–43; xem trực tiếp 8, 9, 12, 16, 20, 22, 23, 37, 40. PDF tải được. Ngày 2025 trong URL là ngày tải lên, không thay niên khóa. |
| ST26 | Emma Brunskill, Stanford CS234, *Lecture 4: Model Free Control and Function Approximation*, Winter 2026; bản slide trước buổi học | [Danh mục](https://web.stanford.edu/class/cs234/modules.html), [PDF](https://web.stanford.edu/class/cs234/slides/lecture4pre.pdf) | Đọc tr. 1, 3–5, 17–38, 78–89; xem 17, 21, 25, 26, 35–37, 85, 87–89. Tải được 89 trang; chân trang cuối ghi 89/88. Dùng số PDF. |
| ST23 | Emma Brunskill, Stanford CS234, cùng tên bài, Winter 2023; slide | [PDF trên miền Stanford](https://web.stanford.edu/class/cs234/CS234Spr2024/CS234Win2023/slides/lecture4.pdf) | Đọc tr. 1–43 qua bản lưu của công cụ web; không xem bố cục. Tải trực tiếp trả HTTP 404. Chỉ bổ trợ thứ tự nội dung, không dùng làm chứng cứ trực quan. |
| SI00 | Singh, Jaakkola, Littman và Szepesvári, *Convergence Results for Single-Step On-Policy Reinforcement-Learning Algorithms*, 2000; bài báo | [PDF](https://ics.uci.edu/~dechter/courses/ics-295/winter-2018/papers/2000-singh-littmansingh98convergence.pdf) | Đọc tr. 290–295, 302–304, nhất là Định lý 1 và Phụ lục B; kiểm GLIE, Sarsa và đếm theo trạng thái/cặp. |
| WD92 | Watkins và Dayan, *Technical Note: Q-Learning*, 1992; bài báo | [PDF](https://www.ece.uvic.ca/~bctill/papers/learning/Watkins_Dayan_1992.pdf) | Đọc định lý tr. 282, mở rộng tr. 285–286; kiểm Q-learning có chiết khấu và giới hạn khi $\gamma=1$. |
| TS02 | Tsitsiklis, *On the Convergence of Optimistic Policy Iteration*, 2002; bài báo | [PDF tại JMLR](https://www.jmlr.org/papers/volume3/tsitsiklis02a/tsitsiklis02a.pdf) | Đọc tr. 60, 66–67, 72; chỉ xác minh các biến thể MC có giả thiết riêng, không dùng thay chứng minh cho L06 tr. 26. |
| HF63 | Hoeffding, *Probability Inequalities for Sums of Bounded Random Variables*, 1963; bài báo | [PDF](https://www.cs.rpi.edu/academics/courses/spring06/random/hoefding.pdf) | Đọc Định lý 2 tr. 16; căn cứ chặn hai phía cho một giá trị chính sách cố định trong đọc thêm. |
| STYLE | UET IAI, hướng dẫn bố cục slide; tài liệu thiết kế | [SLIDE_STYLE_GUIDE.md](https://github.com/uet-iai-course/machine-learning/blob/main/SLIDE_STYLE_GUIDE.md) | Root đọc trực tiếp bản raw ngày 29-09-2026. Chỉ dùng một luận điểm/trang, hình hoặc công thức trung tâm, chú thích có kết luận, không giảm chữ để nhét. |

Kiểm kê resources đã bỏ `.DS_Store`, tiền tố `._`, `~$`; chỉ có năm PDF H02–H07 nêu trên, không có hw06. L06 không có ghi chú diễn giả riêng, trang tài liệu tham khảo, code, notebook, ảnh chụp, logo hoặc dữ liệu đường học. Các hộp thuật toán là giả mã. Không có ảnh nhúng theo kiểm kê PDF; mọi hình mới là sơ đồ suy từ dữ kiện hoặc cơ chế đã xác minh, không phải ảnh gốc được trích.

Giới hạn truy cập: địa chỉ UCL cũ trên `www0.cs.ucl.ac.uk` trả lỗi 502; dùng trang hiện hành của giảng viên được môn CS234 dẫn. Liên kết PDF sách 2018 từ Stanford cũng trả 502; nội dung sách được đọc từ bản cung cấp, không giả rằng bản web đã tải thành công. ST23 không thay hai nguồn đối chiếu chính UCL và ST26.

### So sánh các bộ slide và quyết định

| Nội dung | Quan sát UCL | Quan sát Stanford | Quyết định sư phạm cho Bài 06 |
|---|---|---|---|
| Dẫn nhập và tiên quyết | Tr. 3–9: dự đoán/điều khiển, hai vai chính sách, nhu cầu $Q$, vòng đánh giá–cải thiện | ST23 tr. 2–3 kiểm thiếu dữ liệu hành động; ST26 tr. 17–18 bắt đầu bằng thăm dò | Đặt quyết định tại D trước định nghĩa $q_\pi$; A05 đo phần thông tin còn thiếu. |
| Thăm dò | Tr. 10–12: hai cửa, $\varepsilon$-tham lam, bất đẳng thức cải thiện | ST26 tr. 18–21: thăm dò trước MC; tr. 21 để chỗ tiếp tục chứng minh | Tái dùng bảng A–E, tính 7/8 và 1/8 trước công thức. Đặt cải thiện chính xác cạnh cơ chế; đủ lời giải trong notes, không để chứng minh trống. |
| MC | Tr. 13–18: từ đánh giá đầy đủ tới một lượt, rồi Blackjack | ST26 tr. 24–31: giả mã, Mars Rover tùy chọn; ST23 tr. 17–24 có kiểm tra | Dùng một lượt số trước cập nhật tổng quát; tách thu thập, chọn lần ghé đầu, cập nhật và cải thiện. Không thêm luật Blackjack hoặc Mars Rover. |
| Sarsa | Tr. 19–23: sơ đồ mẫu, công thức, giả mã; hình tr. 20 dành diện tích lớn cho một chuỗi sao lưu | ST26 tr. 38 chỉ nhắc Sarsa, ví dụ ở 83–85; ST23 tr. 26–33 giữ tuyến đầy đủ | Giữ mạch Sarsa riêng vì MT4 đòi hỏi thực hiện thuật toán; đưa ví dụ tính tay trước quy tắc. |
| Q-learning | Tr. 31–38 đi qua lấy mẫu quan trọng; tr. 37 chỉ rõ cực đại tại trạng thái tiếp | ST26 tr. 85/87 dùng cùng khởi tạo để đối chiếu hai cập nhật; tr. 88 hỏi điều kiện trùng nhau | Cùng bảng đầu và cùng năm mẫu cho hai bản chạy riêng; bỏ công thức hiệu chỉnh khỏi cầu nối bắt buộc. E08 đo cơ chế mục tiêu. |
| Bảo đảm | UCL tr. 15–16, 23, 37 phát biểu ngắn, không chứng minh | ST23 tr. 22–24, 32–33, 43; ST26 tr. 29–31, 37–38 rút gọn điều kiện | Bổ sung giả thiết từ SB/SI00/WD92; không suy GLIE từ riêng $\varepsilon_k\to0$. MC cần khớp đúng biến thể với định lý. |
| Bố cục và đánh giá | UCL tr. 12 dồn chuỗi bất đẳng thức; tr. 40 ghép Cliff Walking với đường thực nghiệm | ST26 tr. 25–26 ghép giả mã hoặc dữ kiện, quỹ đạo, bảng và nhiều lựa chọn | Tách giả mã qua hai trang liên tiếp; bảng HTML, công thức KaTeX, SVG lớn. Bảy kiểm tra có đáp án riêng, tính trong 120 phút. Không dựng lại đường thực nghiệm không có dữ liệu. |

Nhận định ở cột cuối là lựa chọn cho đối tượng và thời lượng của bài này. Không suy một bố cục luôn tốt hơn từ tên trường.

## 3. Khái niệm và quan hệ phụ thuộc

| Mã | Vai trò và khái niệm | Tiên quyết | Năng lực cần đạt; dễ nhầm | Đầu ra dùng tiếp |
|---|---|---|---|---|
| KN0 | Nhắc lại: MDP, lợi tức, MC/TD dự đoán | Xác suất, chính sách Markov, Bài 05 | Đọc mẫu, phân biệt thưởng với lợi tức; trạng thái kết thúc với cắt dữ liệu | KN1, KN3, KN4 |
| KN1 | Trọng tâm: giá trị hành động và điều khiển từ bảng | KN0, cải thiện chính sách | Diễn giải hành động đầu cố định và chính sách tiếp nối; $q_\pi$ khác $Q$ | KN2–KN5 |
| KN2 | Trọng tâm: thăm dò và $\varepsilon$-tham lam | KN1, phân phối rời rạc | Tính xác suất, xử lý đồng hạng; thăm hành động tại s khác đạt tới s | KN3–KN6 |
| KN3 | Trọng tâm thuật toán: MC theo chính sách lần ghé đầu | KN0–KN2 | Chọn một lợi tức cho mỗi cặp/lượt, đếm mẫu, giữ chính sách trong lượt | KN4 và giới hạn KN6 |
| KN4 | Trọng tâm thuật toán: Sarsa | KN1–KN3, TD(0) | Tính mục tiêu từ hành động đã chọn, giữ thứ tự, xử lý trạng thái kết thúc | KN5 |
| KN5 | Trọng tâm kết hợp: hành vi/đích và Q-learning | KN4, phép cực đại trên bảng | Tách mẫu chuyển khỏi hành động đích; cùng dữ liệu nhưng hai bảng cập nhật riêng | KN6, kết luận |
| KN6 | Trọng tâm khái niệm: điều kiện bảo đảm | KN2–KN5, chuỗi số; không đòi xấp xỉ ngẫu nhiên | Kiểm GLIE, bước học theo cặp và miền định lý; khác dừng theo ngân sách | Chọn phương pháp có điều kiện |
| KN7 | Hỗ trợ: cải thiện trong lớp $\varepsilon$-mềm | KN1–KN2, cải thiện chính sách | Phân biệt $q_\pi$ chính xác và bảng nhiễu; tối ưu trong lớp mềm khác toàn bộ chính sách | Cơ chế MC, giới hạn KN6 |
| KN8 | Mở rộng đọc thêm: lấy mẫu quan trọng, chặn Hoeffding | Hai chính sách, kỳ vọng; độc lập và biến bị chặn | Đọc đúng đại lượng và phạm vi kết luận | Không làm tiên quyết của tuyến chính |

Quan hệ phụ thuộc: dữ liệu dự đoán → giá trị của từng hành động → chọn và thăm dò hành động → lợi tức hoàn chỉnh cho MC → mục tiêu một bước Sarsa → tách hành vi/đích của Q-learning → điều kiện để phát biểu hội tụ. Cải thiện $\varepsilon$-mềm đặt sau phân phối chọn hành động và trước MC; phần bảo đảm dùng lại kết quả ấy nhưng không đưa nó thành bảo đảm từng cập nhật mẫu. Đây là cách dùng sườn Sutton–Barto: §5.2 chuẩn bị đối tượng, §5.3 chuẩn bị vòng đánh giá–cải thiện, §5.4 xác định thăm dò và đúng biến thể MC, §§6.4–6.5 nối hai loại mục tiêu một bước. Thứ tự không chỉ là danh sách trích dẫn.

## 4. Mạch từng khái niệm trọng tâm

| Cụm | Vấn đề → trực giác → ví dụ → hình thức → ứng dụng → kiểm tra | Dữ kiện truyền sang hình thức; lựa chọn thay thế |
|---|---|---|
| KN1 | A03–A05 thiếu giá trị của hành động chưa thử → B01 so sánh hai ô tại cùng trạng thái → bảng I ở B01 → định nghĩa B02 → vòng dữ liệu–Q–chính sách B03 → B07 | Cặp $(D,0)$ chỉ cố định hành động đầu, các hành động sau phụ thuộc $\pi$. Bổ sung chính sách tiếp nối $\pi_L$ luôn đi trái để có một ví dụ $q_\pi$ xác định; chỉ dưới chính sách ấy mới dùng 998 và 10 như hai giá trị của cùng chính sách. Bảng I giữ nguyên. Định nghĩa trước động lực bị loại vì chưa rõ nhu cầu tách hành động. |
| KN2 | B03 đặt chính sách từ Q → B04 nguy cơ bỏ hành động trái, phân bổ một phần chọn ngẫu nhiên → B04 tính 7/8, 1/8 → B05 công thức tổng quát và lớp mềm → B06 cải thiện với giá trị chính xác → B07 tính và giải thích | Hai hành động, $\varepsilon=1/4$, cực đại duy nhất rồi đồng hạng. Có thể dùng ví dụ hai cửa UCL nhưng tăng quy ước môi trường; A–E đã có đủ cơ chế. |
| KN3 | C01 cần học hai ô từ lượt → C01 trung bình lợi tức gắn với cặp → C02 lượt D→E và mẫu đầu thay 1 bằng 10 → C03 công thức, C05–C06 quy trình → C04/C07 lấy lượt nguồn 17 và cập nhật → C08 cặp lặp | Bước số C02 có $N_0=0$ trước công thức. C04 là dữ kiện cho ứng dụng đầy đủ, không thay trực giác C01. Phương án mọi lần ghé không được chọn làm bản chính vì mục tiêu cần xác định thống nhất với SB tr. 101/H03. |
| KN4 | D01 lượt chưa xong nên thiếu $G_t$ → D01 ước lượng phần tiếp bằng giá trị hành động đã chọn → D02–D03 hai chuyển có số → D04 quy tắc, D05–D06 quy trình → D07 hai bước trạng thái kết thúc → D08 bước 5 | Bảng I, $\alpha=4/5$, $\gamma=1$, năm mẫu đã chốt. Không lấy ví dụ Sarsa khác môi trường vì cần nối trực tiếp với Q-learning. |
| KN5 | E01 mục tiêu theo hành vi còn thăm dò → E01 cực đại làm đích trong khi hành vi sinh mẫu → E02 tính lại mẫu 2 → E03 quy tắc, E04–E05 quy trình → E06 năm mẫu, E07 điều kiện dùng dữ liệu → E08 so sánh mục tiêu | Q-learning đặt lại bảng I, không tiếp tục bảng Sarsa. Công thức lấy mẫu quan trọng không là bước trước bắt buộc; nó làm tăng tiên quyết mà không cần để tính cực đại. |
| KN6 | F01 năm mẫu không suy ra hội tụ → F01 sai lệch mẫu cần độ phủ và bước học → F02 lịch $\varepsilon$ cố định/giảm và F03 dãy bước học → F02–F04 định nghĩa/định lý → F04 đối chiếu thuật toán → F05 nhận diện giả thiết → G03 chọn phương pháp | Phép cộng chuỗi $\alpha_n=1/n$, bước học hằng và đếm riêng từng cặp kiểm được bằng tiên quyết. Không chứng minh xấp xỉ ngẫu nhiên vì vượt nền và 120 phút. |

Bản đồ chi tiết mã trang, bước gộp và thời lượng nằm trong storyboard. KN7 là kết quả hỗ trợ: ví dụ số một trạng thái cho bất đẳng thức chỉ là kiểm phép tính, không là chứng minh hội tụ. KN8 không chiếm trang tuyến chính; nội dung được đặc tả để không mất các trang nguồn 19/29.

## 5. Ví dụ và đặc tả hình

### 5.1. Dữ kiện xuyên bài đã chốt

$\mathcal S=\{B,C,D\}$; $\mathcal S^+=\{A,B,C,D,E\}$; A/E kết thúc; bắt đầu D; hành động 0 trái, 1 phải sang trạng thái kề, chuyển tất định. Thưởng trên chuyển vào A là 1000, vào E là 10, vào B/C/D là −1; $\gamma=1$. Trạng thái kết thúc có giá trị tiếp nối 0, không có hành động ra. Câu “tối đa ba bước” nguồn 15 được sửa thành mô tả độ dài lượt minh họa; không tạo trạng thái kết thúc giả tại trạng thái giữa chuỗi. Nếu giữ thời hạn thật, phải thêm thời gian vào trạng thái và đổi bảng; phương án ấy vượt mục tiêu so sánh cập nhật.

| Trạng thái | Bảng I: trái | Bảng I: phải | Bảng II: trái | Bảng II: phải |
|---|---:|---:|---:|---:|
| B | 0 | 1 | 0 | 1 |
| C | 1 | 0 | 1 | 0 |
| D | 0 | 1 | 1 | 0 |

- MC tham lam dùng bảng I: chính sách cho B→C, C→B, D→E. Lượt từ D có lợi tức 10; $N_0=0$ cho $Q(D,1)=10$. Vòng B↔C cho thấy không được gán giá trị hữu hạn cho mọi cặp dưới chính sách này với $\gamma=1$.
- MC thăm dò dùng bảng II và số thao tác $x_j=(2x_{j-1}+1)\bmod5$, $x_0=1$, $u_j=(x_j+1)/5$. Đọc $u$ để kiểm thăm dò khi $u\le1/4$; chỉ nhánh đó mới đọc số phụ, chọn trái nếu số phụ $\le1/2$. Bốn số đầu $4/5,3/5,1/5,2/5$ tạo D→C→B→A, lợi tức $998,999,1000$. Đây là dãy tất định để tái hiện thao tác, không phải mẫu đều độc lập. Khi giải thích phân phối lý thuyết, phép chọn đều sử dụng nguồn ngẫu nhiên thích hợp và độc lập; không đồng nhất hai cơ chế.
- Sarsa và Q-learning dùng **hai bản sao riêng của bảng I**, $\alpha=4/5$, $\gamma=1$, cùng dữ liệu năm chuyển sau. Hành động được công bố; không suy từ riêng $\varepsilon=1/4$ ra quỹ đạo duy nhất.

| Mẫu | $(S,A,R,S')$ | $A'$ cho Sarsa | Q mới Sarsa | Q mới Q-learning |
|---:|---|---|---:|---:|
| 1 | $(D,0,-1,C)$ | 0 | 0 | 0 |
| 2 | $(C,0,-1,B)$ | 0 | $-3/5$ | $1/5$ |
| 3 | $(B,0,1000,A)$ | Không có | 800 | 800 |
| 4 | $(D,1,10,E)$, khởi động lại D | Không có | $41/5$ | $41/5$ |
| 5 | $(D,0,-1,C)$, khởi động lại D | 0, lấy trước cập nhật | $-32/25$ | $-16/25$ |

Các giá trị ở cột cuối là ô $(S,A)$ của hàng tương ứng, dùng bảng đã cập nhật ở những hàng trước. Mẫu 5 dừng ngân sách ở C; C vẫn không kết thúc. Bảng cuối Sarsa: B=(800,1), C=(−0.6,0), D=(−1.28,8.2). Bảng cuối Q-learning: B=(800,1), C=(0.2,0), D=(−0.64,8.2). Các hành động đã cho có xác suất dương với hành vi mềm của từng bản; điều kiện hóa trên cùng dữ liệu không có nghĩa hai quá trình học có cùng phân phối quỹ đạo.

Ví dụ kiểm tra bổ sung, suy từ đúng môi trường nguồn: C08 dùng D→C→D→C→B→A, các hành động 0,1,0,0,0, các thưởng −1,−1,−1,−1,1000. Lợi tức theo thời gian là 996,997,998,999,1000; cặp $(D,0)$ ghé ở 0 và 2. Lần ghé đầu với $N_0=0$ cho 996, mọi lần ghé cho trung bình 997. Đây là bài kiểm tra tự xây dựng đã tính lại bằng số hữu tỉ, không gán cho L06. Nó phân biệt hai biến thể mà lượt ba bước của nguồn không phân biệt được.

### 5.2. Bảy tài sản SVG đã triển khai

| Tệp trong `img/lec-06/` | Đối tượng, nhãn, quan hệ và kết luận phải thấy | Trang dùng; nguồn |
|---|---|---|
| `chain-five-states.svg` | A–B–C–D–E thẳng hàng; D có nhãn bắt đầu; A/E viền kép, nhãn kết thúc; cạnh 0 trái, 1 phải; nhãn thưởng đúng từng chiều; không có cạnh ra từ A/E | A03 và học liệu §1.1; L06 tr. 15. Alt nêu ba trạng thái không kết thúc, hai trạng thái kết thúc, thưởng trên cạnh. |
| `greedy-chain.svg` | B→C và C→B đều −1; D→E nhận 10; giữ nguyên vòng B↔C, không biến thành đường tới A | C02 và học liệu §2.2; suy từ bảng I nguồn 16. Chú thích: chỉ D→E là lượt đang xét. |
| `control-loop.svg` | Bốn khối dữ liệu → cập nhật Q → chính sách → tương tác → dữ liệu; nhãn MC theo lượt/TD theo chuyển chỉ khi dùng | B03/C01; L06 tr. 6/10–11, SB §4.6/§5.3. Không vẽ đường hội tụ thực nghiệm hoặc điểm đích tất yếu. |
| `episode-return.svg` | D→C→B→A; thời điểm 0–3, hành động 0, thưởng −1,−1,1000; ba đoạn lợi tức ghi 998,999,1000 | C07; L06 tr. 15/17, H07 Bài 7, quy ước số được bổ sung. |
| `sarsa-target.svg` | Từ cặp $(C,0)$ nhận −1 tới B; nhánh hành động 0 tại B được lấy mẫu, giá trị 0; nhánh 1 giá trị 1 không tham gia mục tiêu; nhãn mục tiêu −1 | D03; cùng dữ liệu dùng lại tại E02. Bảng số đặt HTML nếu nhãn hình chật. |
| `q-learning-target.svg` | Hình học và tỷ lệ giống hình Sarsa; tại B chọn cực đại 1 làm giá trị tiếp nối, dù mẫu $A'=0$; mục tiêu 0 | E02; L06 tr. 20, SB tr. 131. Phân biệt bằng nét và chữ, không chỉ màu. |
| `behavior-target.svg` | b→hành động→môi trường→mẫu chuyển→mục tiêu→Q; từ Q tách nhánh tính cực đại làm mục tiêu; hành động kế tiếp thực hiện vẫn do b. Nét đứt biểu diễn cả tạo mục tiêu và cập nhật bảng | E01/E07; L06 tr. 8/19/20, SB tr. 103/131. Không vẽ tỉ số IS hay mô hình chuyển trong đường cập nhật. |

Mỗi SVG dùng `role="img"`, title/desc riêng, `viewBox` phù hợp và nhãn đủ lớn. Không có trục tọa độ giả vì đây là sơ đồ quan hệ; nếu thêm đồ thị phải có dữ liệu và nguồn mới được duyệt. Bảng Q, dữ liệu năm chuyển, xác suất, giả mã và công thức dựng bằng HTML/KaTeX, không ảnh hóa. Không có ngoại lệ raster cần xin.

## 6. Danh mục hình thức hóa và mức chứng minh

### HT1. Giá trị hành động, định nghĩa

$$
G_t=\sum_{j=t}^{T-1}\gamma^{j-t}R_{j+1},\qquad
q_\pi(s,a)=\mathbb E_\pi[G_t\mid S_t=s,A_t=a].
$$

$s\in\mathcal S$, $a\in\mathcal A(s)$; $q_\pi$ cố định hành động đầu, sau đó theo $\pi$, lấy kỳ vọng cả chuyển và thưởng. $Q$ là bảng ước lượng, $q_*$ là giá trị hành động tối ưu. Trong biểu diễn bảng, cập nhật một cặp không trực tiếp thay đổi ước lượng của các cặp khác, dù các trạng thái có đặc điểm tương tự; ý này khôi phục giới hạn tổng quát hóa ở L06 tr. 7 tại ghi chú B01 và học liệu §2.1. Với $\gamma=1$ phải có lợi tức khả tích; không sử dụng $q_\pi$ hữu hạn cho chính sách vòng B↔C. Trong miền hữu hạn, thưởng bị chặn và $\gamma<1$, giá trị hữu hạn. Ví dụ chính sách tiếp nối riêng $\pi_L$ luôn chọn trái tại B,C,D cho $q_{\pi_L}(D,0)=998$ và $q_{\pi_L}(D,1)=10$. Hai giá trị dùng cùng một chính sách có lợi tức hữu hạn; không thay bảng I hoặc chính sách tham lam của bảng ấy. Vị trí B02; SB §5.2 tr. 96–97, tiên quyết Ch.3. Không chứng minh định nghĩa; kiểm bằng cách diễn giải cặp $(D,0)$.

### HT2. Phân phối $\varepsilon$-tham lam, định nghĩa

Đặt $m(s)=|\mathcal A(s)|$ và $\mathcal G_Q(s)=\arg\max_aQ(s,a)$. Quy ước chia đều phần khai thác giữa các cực đại:

$$
\pi_\varepsilon(a\mid s)=\frac{\varepsilon}{m(s)}+(1-\varepsilon)\frac{\mathbf1\{a\in\mathcal G_Q(s)\}}{|\mathcal G_Q(s)|},\qquad 0\le\varepsilon\le1.
$$

Chính sách $\varepsilon$-mềm có $\pi(a\mid s)\ge\varepsilon/m(s)$ với mọi hành động. Phân phối trên là một cách chọn trong lớp ấy; không phải mọi chính sách mềm đều tham lam dạng này. Hai hành động và $\varepsilon=1/4$ cho $(1/8,7/8)$ khi hành động 1 cực đại; đồng hạng cho $(1/2,1/2)$. Vị trí B04–B05; SB tr. 100–101. Quy ước chia đều là mở rộng khai báo rõ của phá hòa tùy ý trong sách. Chỉ kiểm tổng xác suất, không cần chứng minh riêng.

### HT3. Cải thiện trong lớp $\varepsilon$-mềm, mệnh đề

Giả thiết: MDP hữu hạn, có động lực không đổi theo thời gian, thưởng bị chặn, $0\le\gamma<1$; cùng $\varepsilon\in[0,1)$; $\pi$ là $\varepsilon$-mềm; biết **chính xác** $q_\pi$. Nếu $\pi'$ là $\varepsilon$-tham lam theo $q_\pi$ thì $v_{\pi'}\ge v_\pi$ ở mọi trạng thái. $\varepsilon=1$ cho chính sách đều và đẳng thức. Giữ $\varepsilon>0$ là xét lớp mềm tương ứng; không kết luận tối ưu toàn bộ chính sách.

B06 chỉ giữ giả thiết, kết luận và một dòng $\sum_a\pi'(a\mid s)q_\pi(s,a)\ge v_\pi(s)$. Ghi chú chứa chứng minh: $w_a=(\pi(a\mid s)-\varepsilon/m(s))/(1-\varepsilon)$ không âm, tổng bằng 1; cực đại chặn trung bình theo $w$; cộng thành phần đều suy bất đẳng thức; lặp toán tử Bellman bảo toàn thứ tự và co với $\gamma<1$ suy kết luận. Ví dụ số tự xây dựng để kiểm một bước, không gán cho môi trường A–E: $q=(3,3,-1)$, $\varepsilon=0.3$, $\pi=(0.2,0.1,0.7)$ cho kỳ vọng 0.2; $\pi'=(0.45,0.45,0.1)$ cho 2.6. Phép tính đặt trong notes, không thêm môi trường chính. Nguồn L06 tr. 24, SB tr. 101–103, UCL tr. 12. Mức phác thảo đủ dùng với tiên quyết cải thiện chính sách; không đồng nhất với cải thiện sau mỗi mẫu MC.

### HT4. MC lần ghé đầu, quy tắc và thuật toán

Dùng $N(s,a)=0$ và k=1 ban đầu; K là số nguyên dương chỉ số lượt hoàn chỉnh cần thu. Mỗi đầu lượt đặt lại quỹ đạo và bảng chỉ số ghé đầu f, nhưng giữ Q và N tích lũy. Mỗi lượt hoàn chỉnh được sinh theo chính sách giữ cố định trong lượt. Sau mỗi chuyển, ghi $f(S_t,A_t)=t$ nếu cặp chưa có trong $f$, rồi mới tăng $t$; không ghi hành động tại trạng thái kết thúc. Chỉ lấy $G_t$ của lần xuất hiện đầu của **cặp** $(s,a)$ theo chiều thời gian, tăng N rồi cập nhật:

$$
N(s,a)\leftarrow N(s,a)+1,\qquad
Q(s,a)\leftarrow Q(s,a)+\frac{G_t-Q(s,a)}{N(s,a)}.
$$

C03 hình thức sau mẫu số C02; C05–C06 ghi quy trình đầy đủ, đầu vào, đầu ra và dừng. Bộ đếm N là số lợi tức được sử dụng, không phải số lượt toàn cục. Đầu ra là Q và chính sách mềm từ Q; không gắn nhãn đã tối ưu. Bộ nhớ $O(M+T)$ với $M=\sum_s|\mathcal A(s)|$; lưu chỉ số ghé đầu giúp phần xử lý lượt $O(T)$, cộng chi phí tìm cực đại khi chọn/cải thiện chính sách. MC cần kết thúc thật và lợi tức tồn tại. Trung bình MC dưới chính sách cố định khác điều khiển đổi chính sách. SB tr. 93, 99–103; L06 tr. 10–11. Không giữ định lý tổng quát thiếu giả thiết của L06 tr. 26.

### HT5. Sarsa một bước, quy tắc và thuật toán

$Q_t$ là bảng trước cập nhật. Nếu $S_{t+1}$ chưa kết thúc, lấy $A_{t+1}$ theo chính sách từ $Q_t$, đặt $Y_t=R_{t+1}+\gamma Q_t(S_{t+1},A_{t+1})$. Nếu kết thúc, $Y_t=R_{t+1}$ và không chọn $A_{t+1}$. Cập nhật

$$
Q_{t+1}(S_t,A_t)=Q_t(S_t,A_t)+\alpha_t\big[Y_t-Q_t(S_t,A_t)\big].
$$

Các ô còn lại giữ nguyên. Sau cập nhật thực hiện chính hành động $A_{t+1}$ đã lấy, không lấy lại theo bảng mới. D03 có bước số trước D04; D05–D06 quy trình. Lưu $O(M)$, mục tiêu dùng một tra cứu khi đã có hành động; chọn $\varepsilon$-tham lam có thể cần duyệt $m(s)$ ô. Chỉ bắt đầu lượt mới khi trạng thái kế tiếp kết thúc và còn ngân sách; nhánh chưa kết thúc tiếp tục từ cặp đã lưu. Dừng toàn bộ khi hết ngân sách sau cập nhật; nếu mẫu cuối chưa kết thúc, vẫn giữ giá trị tiếp nối. Nguồn L06 tr. 12–14/18, SB tr. 129–130. Không chứng minh hội tụ tại trang thuật toán.

### HT6. Q-learning một bước, quy tắc và thuật toán

Nếu $S_{t+1}$ chưa kết thúc, $Y_t=R_{t+1}+\gamma\max_{a\in\mathcal A(S_{t+1})}Q_t(S_{t+1},a)$; nếu kết thúc, $Y_t=R_{t+1}$. Dùng cùng dạng cập nhật HT5, các ô khác giữ nguyên. Hành động thực hiện do b chọn; chính sách đích tham lam rút ra từ Q. E02 bước số trước E03; E04–E05 quy trình bổ sung từ SB tr. 131, nguồn L06 tr. 20 chỉ có công thức. Lưu $O(M)$; tìm cực đại trực tiếp tốn $O(m(S_{t+1}))$, chọn hành vi cũng có chi phí. Không cần $A_{t+1}$ lấy mẫu để tính mục tiêu; không cần biết p hoặc tỉ số IS. Chỉ bắt đầu lượt mới khi trạng thái kế tiếp kết thúc và còn ngân sách; dừng vì hết ngân sách áp dụng cho cả hai nhánh, không xóa cực đại ở mục tiêu cuối chưa kết thúc.

### HT7. GLIE, định nghĩa có hai yêu cầu

Cách gọi đầu tiên: **tham lam trong giới hạn với thăm dò vô hạn (GLIE)**. Dùng t là chỉ số tương tác toàn bộ quá trình, $Q_t$ là bảng trước cập nhật ở bước t, $\pi_t$ là quy tắc chọn hành động theo bảng ấy. $C_t(s,a)$ đếm số lần đã thăm cặp đến bước t; phân biệt với N đếm lợi tức được chọn trong MC. Đặt $\mathcal G_t(s)=\arg\max_a Q_t(s,a)$. Trong phạm vi các cặp cần học, yêu cầu gần chắc chắn:

$$
C_t(s,a)\to\infty,\qquad
\sum_{a\in\mathcal G_t(s)}\pi_t(a\mid s)\to1.
$$

Với MC, k vẫn là chỉ số lượt; $Q^{[k]}$ là bảng trước lượt k và $\pi_k$ giữ cố định suốt lượt. Phiên bản GLIE theo lượt dùng $C^{[k]}$, $Q^{[k]}$, tập cực đại và chính sách cùng thời điểm ấy; không đổi ngầm nghĩa $Q_t$ thành bảng cuối lượt. Định nghĩa không đòi các phân phối phải hội tụ điểm một khi đồng hạng. $\varepsilon_k\to0$ bảo đảm vế tham lam của quy tắc HT2 theo lượt; độ phủ còn phụ thuộc đạt tới và phân phối đầu. F02 dùng lịch cố định/giảm để giải thích trước hai công thức. Không gọi riêng $1/k$ là GLIE. L06 tr. 25 được sửa theo SI00 tr. 290–292, 302–304. Phản ví dụ hai bước của kiểm toán chỉ dành đọc thêm, không tạo trang chính.

### HT8. Bước học và hội tụ bảng tra, điều kiện và định lý

Đánh số n theo lần cập nhật riêng của cặp. Yêu cầu với mọi cặp cần học:

$$
0<\alpha_n(s,a)\le1,\qquad \sum_{n=1}^\infty\alpha_n(s,a)=\infty,\qquad
\sum_{n=1}^\infty\alpha_n(s,a)^2<\infty.
$$

Ví dụ $1/n$ thỏa; hằng $0.8$ không thỏa tổng bình phương. Dùng $1/t$ toàn cục có thể thất bại: một cặp cập nhật tại $t_n=2^n$ chỉ nhận tổng $\sum_n2^{-n}<\infty$. F03 trình bày ví dụ trước công thức.

Miền định lý F01/F04: MDP hữu hạn, có động lực không đổi theo thời gian; thưởng bị chặn; $0\le\gamma<1$; $Q_0$ hữu hạn; mẫu tuân động lực có điều kiện theo cặp; mỗi cặp cập nhật vô hạn gần chắc chắn; bước học thỏa HT8 và dựa trên thông tin có trước mẫu. Q-learning có $Q_t\to q_*$ gần chắc chắn. Sarsa có cùng kết luận khi thêm chính sách trở nên tham lam theo bảng hiện hành. Hành vi Q-learning không cần tham lam trong giới hạn. Chỉ phát biểu và áp dụng, không chứng minh bằng xấp xỉ ngẫu nhiên. Nguồn SB tr. 129–131, SI00 Định lý 1 tr. 294–295, WD92 tr. 282. Ví dụ $\gamma=1,\alpha=0.8$ không thuộc bảo đảm này. Mở rộng không chiết khấu đòi kiểm giả thiết hấp thụ riêng; xem WD92 tr. 285–286.

## 7. Nội dung đọc thêm và chữa bài đã triển khai

### Đọc thêm DT1: sửa đối tượng của nguồn 19

Tên đúng là **Dự đoán TD(0) khác chính sách**. Chính sách đích $\pi$ cố định, hành vi b có $\pi(a\mid s)>0\Rightarrow b(a\mid s)>0$. Giữ đúng ngoặc của công thức nguồn:

$$
\rho_t=\frac{\pi(A_t\mid S_t)}{b(A_t\mid S_t)},\qquad
V_{t+1}(S_t)=V_t(S_t)+\alpha_t\{\rho_t[R_{t+1}+\gamma V_t(S_{t+1})]-V_t(S_t)\}.
$$

Với bảng $V_t$ cố định theo lịch sử trước lấy hành động, kỳ vọng gia số chưa nhân bước học bằng $(T^\pi V_t)(s)-V_t(s)$. Hệ số nhân **mục tiêu**, khác từng mẫu với dạng $\rho_t(Y_t-V_t(s))$ của SB (7.9)–(7.10), tr. 148. Hai gia số chưa nhân bước học có cùng kỳ vọng có điều kiện vì kỳ vọng có điều kiện của $\rho_t$ bằng 1. Không gọi đây là mẫu không chệch trực tiếp của $v_\pi$; không khẳng định thứ tự phương sai chung.

Đặc tả bổ sung nếu đối chiếu Sarsa khác chính sách: dùng Q và $\rho_{t+1}$ của hành động kế tiếp, nhân toàn sai lệch như SB (7.11), tr. 149. Trạng thái kết thúc có hệ số rỗng bằng 1, giá trị tiếp nối 0. Không đưa công thức này vào tuyến chính hoặc coi nó là tiên quyết của Q-learning.

### Đọc thêm DT2: phạm vi chặn nguồn 29

Cố định $\pi,d_0,n,\delta$ với $n\ge1$, $0<\delta<1$. Sinh n lượt độc lập từ cùng phân phối đầu $d_0$ và cùng chính sách. Trong mục đọc thêm này, n là số lượt độc lập, khác vai trò số cập nhật riêng của cặp ở phần chính; i đánh số lượt. Gọi $G^{(i)}$ là lợi tức ngẫu nhiên hoàn chỉnh của lượt i, $J_{d_0}(\pi)=\mathbb E_{S_0\sim d_0,\pi}[G_0]$, $\widehat J_n=n^{-1}\sum_i G^{(i)}$. Nếu $L\le G^{(i)}\le U$ gần chắc chắn, $B=U-L$, thì

$$
\Pr\{|\widehat J_n-J_{d_0}(\pi)|>\eta\}\le2\exp(-2n\eta^2/B^2).
$$

Với xác suất ít nhất $1-\delta$, sai số không quá $B\sqrt{\log(2/\delta)/(2n)}$. Muốn bán kính không quá $\eta$, cần $n\ge B^2\log(2/\delta)/(2\eta^2)$. Nếu $0\le R\le R_{\max}$ và $\gamma<1$, có thể lấy $B=R_{\max}/(1-\gamma)$; nếu chỉ $|R|\le R_{\max}$, độ rộng gấp đôi. Không áp hệ số ấy cho chuỗi $\gamma=1$; kết thúc gần chắc chắn không bảo đảm lợi tức bị chặn bởi một B cố định. Đây là đánh giá một chính sách tại n cố định, không phải số mẫu tìm chính sách tối ưu, không dùng mẫu đang đổi chính sách hoặc coi mọi lần ghé cùng lượt là độc lập. Nguồn HF63 Định lý 2 tr. 16; suy hai phía bằng cộng hai đuôi. G04 chỉ dẫn đọc, không thêm trang chứng minh.

### Chữa bài riêng 30 phút

| Bài | Thời gian | Dữ kiện và sản phẩm |
|---|---:|---|
| L06 tr. 16–17, với quy ước đã sửa | 10 phút | Vẽ chính sách tham lam giữ vòng B↔C; tính lượt D→E; tái hiện bốn số thao tác và ba cập nhật MC từ bảng II. |
| L06 tr. 18/21, dữ liệu chung trong bài mới | 10 phút | Viết đủ hai bảng sau từng mẫu; giải thích khác biệt bắt đầu mẫu 2 và truyền về D ở mẫu 5. |
| H03 Bài 10 tr. 2–3, chỉ phần bảng tra | 10 phút | Môi trường A–B–C–D–E–F, A/F kết thúc, bắt đầu D, $\gamma=1/2$; vào A thưởng 10, F thưởng−2, còn lại−1; B đi trái tới A xác suất 0.9, đứng B xác suất 0.1. Bảng đầu B=(−1,1), C=(0,2), D=(1,0), E=(1,5). Hai lượt cho sẵn: D–C–B–B–A (đều trái), D–E–F (đều phải). Tính MC lần ghé đầu và Q-learning $\alpha=1$ trên hai bản sao riêng. |

Đáp án H03 đã kiểm: lợi tức lượt 1 $(-0.5,1,4,10)$, lượt 2 $(-2,-2)$. MC với $N_0=0$: B=(4,1), C=(1,2), D=(−0.5,−2), E=(1,−2); mọi lần ghé cho riêng ô (B,trái) bằng 7. Q-learning đặt lại bảng đầu: B=(10,1), C=(−0.5,2), D=(0,1.5), E=(1,−2). Hai lượt đều kết thúc thật trước giới hạn năm bước của bài gốc. Không nhập phần xấp xỉ hàm hoặc tạo chương trình.

## 8. Quyết định tổng hợp và trạng thái kiểm định

Bảy mạch giữ ngân sách 5/7/8/8/8/5/4 trang và 10/18/22/22/22/16/10 phút. Không có phần thực hành tách riêng trong 120 phút: các bài tính và kiểm tra dùng ngay kết quả của mạch tương ứng. Phần chữa 30 phút được tách bằng mục tiêu tái thực hiện và đối chiếu; không cộng vào 120 phút.

Các thay đổi chính so với L06: đưa chuỗi nguồn 15 lên động lực; đưa cải thiện nguồn 24 tới cạnh thăm dò; xác định lần ghé đầu và N0; hoàn thiện RNG; sửa giới hạn ba bước; bổ sung năm mẫu; đổi khởi tạo Q-learning sang bảng I; sửa trạng thái kết thúc và tiêu chuẩn dừng; đủ giả mã Q-learning; chuẩn hóa ký hiệu; sửa điều kiện hội tụ; đặt nguồn 19/29 vào đọc thêm; lược ma trận thuật toán sâu nguồn 23. Bảng ánh xạ đủ 30 trang và các đích cụ thể nằm trong outline. Không thêm dữ liệu thực nghiệm hoặc kết quả tối ưu không có căn cứ.

Đã đọc mẫu, CSS chung và index cho nền kỹ thuật. HTML đã triển khai dùng `.reveal.lecture-deck`, `href="lecture-slide.css"`, khung 1280×720, bảy section ngoài, trang con có mã duy nhất, thư viện cục bộ RevealJS/KaTeX/Notes/Highlight và cấu hình hash/controls theo mẫu. Không sao chép metadata hoặc nội dung Cơ sở toán học cho AI của mẫu. Chỉ dùng thẻ/lưới và cỡ chữ chung; phép chứng minh, đáp án dài và giới hạn chi tiết vào ghi chú/học liệu. Footer là Học tăng cường · Học kỳ 1, 2026–2027 · Bài 06. Mã, thời lượng và nhãn quy trình chỉ ở planning.

Bản nháp đã qua năm lượt rà độc lập và kiểm kỹ thuật rộng/hẹp của điều phối viên; phạm vi và giới hạn được ghi trong review-log. Sau biên tập, điều phối viên đã kiểm 90 lượt hiển thị cho 45 trang ở hai khung rộng/hẹp và xem trực tiếp các trang sửa, gồm nhãn câu hỏi A05/C08, điều kiện tái khởi đầu D06/E05 và giả thiết ở B06/F01/F04/F05. Không thu nhỏ chữ để khắc phục bố cục. Đã đối chiếu đủ 45 hình, tiêu đề và ghi chú trong Codex Slides.

Bản phân tích đã được biên tập theo no-ai-slop chế độ Edit và tự kiểm eval; Quill được dùng để rà vai trò khái niệm, đầu vào–đầu ra, tính liên tục và thuật ngữ. Không tạo `quill.json`. Dàn bài đã được kiểm định độc lập và chấp nhận trước triển khai. Biên tập giữ 45 trang và bảy mạch; hai lượt tái kiểm độc lập xác nhận các sửa toán/thuật toán và mạch viết, tách khỏi tự kiểm của tác tử biên tập.
