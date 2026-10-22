# Storyboard Bài 08

## Đợt sửa 2026-10-22: bản đồ bảy mạch

Căn cứ: kế hoạch sửa đã duyệt ngày 2026-10-22 và ba báo cáo rà soát (cấu trúc–mạch, sinh viên–mật độ, RL–toán), xem `review-log.md`, mục "Đợt sửa 2026-10-22". Bản đồ này thay bản đồ cũ ở cuối tệp.

**Vấn đề trung tâm.** Học $q_*$ với tập hành động hữu hạn khi quan sát là ảnh và không có mô hình môi trường. Ba thách thức của nguồn (tr. 12): tối ưu không lồi trên tham số mạng, đích bootstrap phụ thuộc chính tham số đang học, phân phối dữ liệu dịch chuyển theo chính sách hành vi.

| mạch | loại | chức năng | đầu vào | đầu ra | đóng góp cho vấn đề trung tâm | trang tiêu đề mạch | thời lượng |
|---|---|---|---|---|---|---|---:|
| 1. Mở đầu | mở bài | Nhắc lại Q-learning bảng và Q-learning bán gradient tuyến tính, nêu ký hiệu, mục tiêu, nội dung và vấn đề trung tâm | Bài 06: Q-learning bảng, hành vi–đích, điều kiện hội tụ; Bài 07: $\hat q(s,a,w)=x(s,a)^\top w$, bán gradient, bộ ba bất ổn | Nhu cầu một hàm giá trị hành động học từ quan sát thô; ba thách thức làm khung cho mạch 2–6 | Phát biểu bài toán và câu trả lời có điều kiện của từng mạch | không có (bìa là trang tiêu đề của mạch mở đầu) | 10 |
| 2. Mạng giá trị hành động và đích hồi quy | khái niệm | Định nghĩa giao diện $\mathbf q_\theta(o)$, chỉ ra đích di động khi một tham số vừa dự đoán vừa tạo đích, đưa mạng mục tiêu và đích có mặt nạ | Nhu cầu từ mạch 1; mục tiêu Q-learning (Nhắc lại) | Đích $y$ có mặt nạ $(1-Z)$ tính từ $Q_{\theta^-}$; bộ sáu thành phần $(O_t,A_t,R_{t+1},O_{t+1},Z_{t+1},U_{t+1})$ | Với $\theta^-$ cố định giữa hai lần đồng bộ, mỗi mẫu chuyển có một nhãn hồi quy cố định | `L08-M2T`, `id="mach-2"` | 25 |
| 3. Bộ nhớ phát lại | khái niệm | Nêu tương quan của mẫu liền nhau (vấn đề), cơ chế lưu và lấy mẫu đều, dữ liệu khác chính sách, giới hạn | Bộ sáu thành phần của mạch 2 | Mini-batch $\{(O_i,A_i,R_i,O'_i,Z_i,U_i)\}_{i=1}^b$ lấy đều từ $\mathcal D$ | Lấy đều từ bộ nhớ làm giảm tương quan ngắn hạn; dữ liệu vẫn không i.i.d. theo một phân phối cố định | `L08-M3T`, `id="mach-3"` | 15 |
| 4. Hàm mất mát và thuật toán DQN | thuật toán | Viết hàm mất mát với dừng gradient, tính tay một mini-batch, ghép thu thập, tối ưu và đồng bộ thành thuật toán với hai bộ đếm, kiểm kích thước tensor và lỗi cài đặt | $y_i$ (mạch 2), mini-batch (mạch 3) | Gradient $\nabla_\theta L_B$ cho bộ tối ưu; thuật toán DQN đầy đủ | Gradient chỉ đi qua $Q_\theta(O_i,A_i)$; $\theta^-\leftarrow\theta$ sau mỗi $C$ bước tối ưu | `L08-M4T`, `id="mach-4"` | 30 |
| 5. Bộ tối ưu theo gradient | thuật toán (phụ trợ) | Viết SGD, RMSprop, Adam theo tọa độ và so sánh trạng thái phụ, siêu tham số | $g_j=\nabla_\theta L_{B_j}$ từ mạch 4 | Quy tắc cập nhật $\theta$ cùng giới hạn: bộ tối ưu không sửa đích, dữ liệu hay xấp xỉ hàm | Bộ tối ưu đổi gradient thành bước tham số, không gỡ bất ổn của đích hay dữ liệu | `L08-M5T`, `id="mach-5"` | 10 |
| 6. Bất ổn và phạm vi bảo đảm của DQN | kết quả, giới hạn | Đặt hai cơ chế cạnh hai nguồn bất ổn, lượng hóa độ nhảy của đích tại mốc đồng bộ, áp bộ ba bất ổn vào DQN, thiết kế thí nghiệm loại bỏ | Thuật toán (mạch 4), giới hạn bộ tối ưu (mạch 5), bộ ba bất ổn (Nhắc lại Bài 07) | Kết luận có điều kiện: hai cơ chế giảm hai nguồn bất ổn, không tạo bảo đảm hội tụ | Khi đủ xấp xỉ hàm, bootstrap và dữ liệu khác chính sách, không có bảo đảm hội tụ tổng quát | `L08-M6T`, `id="mach-6"` | 15 |
| 7. Tổng kết và chuyển tiếp | kết bài | Bảng kết quả–giả thiết, bảng so sánh phương pháp, bài tổng hợp, trả lời vấn đề trung tâm, câu hỏi tự kiểm tra, bài tập về nhà và tài liệu đọc | Kết quả của mạch 2–6 | Câu trả lời có điều kiện cho vấn đề trung tâm; nối Bài 09 | Tổng hợp; không thêm khái niệm mới | `L08-M7T`, `id="mach-7"` | 15 |

Tổng: $10+25+15+30+10+15+15=120$ phút trên lớp; 30 phút chữa bài ngoài 120 phút. Mã trang tiêu đề mạch dùng dạng `L08-MNT` vì mã trang của bài không có tiền tố mạch bằng chữ cái; quy ước `<tiền tố>T` của `AGENTS.md` áp dụng cho trường hợp này.

### Danh sách trang theo mạch (đích của đợt sửa)

Ký hiệu cột "C0": vị trí sau bước C0 (chỉ di chuyển trang, bỏ CSS cục bộ, chưa thêm hay bỏ trang). "chưa có" là trang sẽ thêm ở bước sau.

| mạch | mã | tiêu đề dự kiến | quyết định | lý do | C0 |
|---|---|---|---|---|---|
| 1 | `L08-01` | Deep Q-Learning (bìa) | sửa | Bỏ phụ đề "Từ…đến…"; thêm câu luận đề, đơn vị, năm học | 1.1 |
| 1 | `L08-01b`, `L08-01b2` | Tiên quyết và quy ước (hai trang cùng tiêu đề) | thêm (gộp `L08-04`, `L08-05`) | Dòng "Nhắc lại:" cho Q-learning bảng và giả thiết hội tụ (MDP hữu hạn, phần thưởng bị chặn, $\gamma<1$, mọi cặp cập nhật vô hạn lần, Robbins–Monro theo cặp), Q-learning bán gradient tuyến tính có đủ bộ ba bất ổn, mạng nhiều tầng và mạng tích chập học $\theta$ bằng lan truyền ngược | 1.2–1.3 (S2) |
| 1 | `L08-04` | (gộp vào `L08-01b`) | gộp, bỏ trang riêng | Bài 06 đã dạy; $Z$ xuất hiện trước định nghĩa | đã bỏ ở S2 |
| 1 | `L08-05` | (gộp vào `L08-01b`; ý khác chính sách sang `L08-05r`) | gộp, bỏ trang riêng | "replay" dùng trước khi giới thiệu; 82 âm tiết; lý do không cần tỉ số lấy mẫu quan trọng phải sửa | đã bỏ ở S2; ý dữ liệu khác chính sách trong bộ nhớ viết lại ở `L08-05r` |
| 1 | `L08-01c` | Tiên quyết và quy ước (cùng tiêu đề) | thêm | Dòng "Ký hiệu:" và bảng: $O_t$, $S_t$, $\mathcal A$ hữu hạn, $R_{t+1}$, $\gamma$, $\theta$, $t$, $k_{\mathrm{opt}}$, $i$, $\epsilon_{\mathrm{exp}}$ ($\varepsilon$ của Bài 06), $\epsilon_{\mathrm{opt}}$; $q_i$ khai báo ở `L08-17` | 1.4 (S3) |
| 1 | `L08-02` | Mục tiêu học tập | sửa | Sáu mục tiêu ứng mạch 2–7 (`outline.md`) | 1.5 (S4) |
| 1 | `L08-02b` | Nội dung | thêm | Bảy mục khớp trang tiêu đề mạch và `#/N`; dòng đọc trước: Sutton và Barto (2018), §11.3, §16.5; Mnih và cộng sự (2015) | 1.6 (S5) |
| 1 | `L08-02c` | Vấn đề trung tâm | thêm (gộp ý quy mô của `L08-06`) | Một dòng bài toán, một dòng trả lời có điều kiện cho mỗi mạch 2–6 | 1.7 (S6) |
| 1 | `L08-06` | (gộp vào `L08-02c` và `L08-03`) | gộp, bỏ trang riêng | Cảnh báo phủ định cận mẫu chưa từng nêu trên mặt trang | đã bỏ ở S6; ý "số ô tăng theo $\lvert\mathcal S\rvert\lvert\mathcal A\rvert$" sang bước `L08-03`, ý "xấp xỉ hàm cần giả thiết cấu trúc mới có bảo đảm" sang bước `L08-30` |
| 2 | `L08-M2T` | 2. Mạng giá trị hành động và đích hồi quy | thêm | Trang tiêu đề mạch, điểm vào mạch 2 | 2.0 (S7) |
| 2 | `L08-03` | Giới hạn của bảng giá trị hành động | sửa | Nhu cầu; Lunar Lander rời rạc hóa $9\,216$ ô, $1\,896$ ô có mẫu sau $2\,000$ lượt (Bài 07, Ví dụ 07.1); sửa nhãn SVG | 2.2 (S8) |
| 2 | `L08-31` | Ví dụ: đầu vào bốn khung Atari | sửa, chuyển lên | Ví dụ cho giao diện; bốn khung phải có trước $[b,4,h,w]$ ở `L08-20` | 2.2 |
| 2 | `L08-07` | Mạng giá trị hành động | tách | Chỉ giữ giao diện; phản ví dụ sang `L08-07b`, mạng mục tiêu sang `L08-07c` | 2.3 |
| 2 | `L08-32` | Bốn khung và tính Markov | sửa, chuyển lên | Câu hỏi và Lời giải; rút còn ≤ 60 âm tiết | 2.4 |
| 2 | `L08-07b` | Ví dụ: một tham số tạo cả dự đoán lẫn đích | thêm | $Q_\theta=\theta$, $R=1$, $\gamma=0{,}9$, $\theta_0=0$, $\alpha=0{,}5$: $y=1$, $\theta_1=0{,}5$, đích mới $1{,}45$ | chưa có |
| 2 | `L08-07c` | Mạng mục tiêu | thêm (nhận hình của `L08-16`) | Khởi tạo $\theta^-\leftarrow\theta$, giữ $C$ bước tối ưu rồi sao chép; định nghĩa đồng bộ trước `L08-08` | chưa có |
| 2 | `L08-08` | Đích hồi quy | sửa | Định nghĩa $Z$ trước khi dùng | 2.5 |
| 2 | `L08-09` | Ví dụ: đích tại mẫu chuyển kết thúc | sửa | Mẫu 2 của ví dụ xuyên suốt "mini-batch hai mẫu chuyển" | 2.6 |
| 2 | `L08-12` | Kết thúc và cắt ngắn | sửa | $U=1,Z=0$ vẫn bootstrap; đặt lại khi $Z\lor U$; mặt nạ chỉ $1-Z$; hình dòng thời gian | 2.7 |
| 3 | `L08-M3T` | 3. Bộ nhớ phát lại | thêm | Trang tiêu đề mạch, điểm vào mạch 3 | chưa có |
| 3 | `L08-28` | Tương quan giữa các mẫu chuyển liên tiếp | sửa, chuyển lên | Vấn đề đứng trước cơ chế; hình dải quỹ đạo | 3.1 |
| 3 | `L08-13` | Bộ nhớ phát lại | sửa | Nhu cầu:, định nghĩa $\mathcal D$, ví dụ $N=6$; quan sát cuối khi tự đặt lại, không nêu tên trường API | 3.2 |
| 3 | `L08-05r` | Dữ liệu khác chính sách trong bộ nhớ | thêm (từ `L08-05`) | Hai nguồn khác chính sách; lý do không cần tỉ số lấy mẫu quan trọng đã sửa (Sutton và Barto 2018, §6.6, §7.3) | chưa có |
| 3 | `L08-14` | Giới hạn của bộ nhớ phát lại | sửa | Thêm Câu hỏi $N=6$, $b=2$ không hoàn lại: $1/\binom62=1/15$ | 3.3 |
| 4 | `L08-M4T` | 4. Hàm mất mát và thuật toán DQN | thêm | Trang tiêu đề mạch, điểm vào mạch 4 | chưa có |
| 4 | `L08-17` | Hàm mất mát trên mini-batch | sửa, chuyển lên đầu mạch | $q_i$, $y_i$, $L_B$ định nghĩa trước đồ thị tính | 4.1 |
| 4 | `L08-10` | Dừng gradient ở đích | sửa (gộp `L08-15`) | Định nghĩa $\operatorname{sg}$; nối bán gradient Bài 07; sửa tràn khung (chặn bàn giao); vẽ lại `dqn-computation-graph.svg` | 4.2 |
| 4 | `L08-15` | (gộp vào `L08-10`) | gộp, bỏ trang riêng | Trùng hình và công thức của `L08-10` | 4.3 (tạm) |
| 4 | `X01` | Bài tập: một mini-batch | sửa | Bảng dữ liệu cùng khuôn ví dụ xuyên suốt; Gợi ý trong ghi chú | 4.4 |
| 4 | `L08-21` | Bài tập: một mini-batch (lời giải) | sửa | Lời giải từng bước; giả thiết bỏ qua giao thoa qua $\theta$ dùng chung cho câu hỏi dấu cập nhật | 4.5 |
| 4 | `L08-11` | Vòng huấn luyện DQN | sửa | Nhu cầu:; sửa SVG ($O'$, $\epsilon_{\mathrm{exp}}$-tham lam, nhãn cạnh) | 4.6 |
| 4 | `L08-18a` | Thuật toán DQN: đầu vào và khởi tạo | thêm (tách từ `L08-18`) | Mỗi siêu tham số một dòng nghĩa; ngân sách dừng | chưa có |
| 4 | `L08-18` | Thuật toán DQN: tương tác và lưu | sửa | Bước 1–4; 87 âm tiết trước sửa | 4.7 |
| 4 | `L08-19` | Thuật toán DQN: tối ưu và đồng bộ | sửa | Vòng lặp ngoài; thứ tự cập nhật → tăng $k_{\mathrm{opt}}$ → kiểm $C$ | 4.8 |
| 4 | `L08-16` | (bỏ; hình sang `L08-07c`, thứ tự sang ghi chú `L08-19`) | bỏ | Trùng bước 9 của giả mã | 4.9 (tạm) |
| 4 | `L08-20` | Kích thước tensor của mini-batch Atari | sửa | Nhắc lại bốn khung; định nghĩa $h,w$ | 4.10 |
| 4 | `X02` | Bài tập: lỗi cài đặt đích DQN | sửa (có thể tách `X02b`) | Mã lỗi nhất quán theo batch; lỗi `.max()` không chiều; không gắn tên trường API cố định | 4.11 |
| 5 | `L08-M5T` | 5. Bộ tối ưu theo gradient | thêm | Trang tiêu đề mạch, điểm vào mạch 5 | chưa có |
| 5 | `L08-22` | Vai trò của bộ tối ưu | sửa | Hình chuỗi $B_j\to L_{B_j}\to g_j\to\theta_j$, $j=k_{\mathrm{opt}}$; bỏ dẫn chiếu "bước 8 giả mã" | 5.1 |
| 5 | `L08-23` | Hạ gradient ngẫu nhiên (SGD) | sửa | Viết đầy đủ tên | 5.2 |
| 5 | `L08-24` | RMSprop | sửa | Ký hiệu $\odot,\oslash$; Ý nghĩa: | 5.3 |
| 5 | `L08-25` | Adam | sửa | Ý nghĩa: hiệu chỉnh lệch | 5.4 |
| 5 | `L08-26` | So sánh ba bộ tối ưu | sửa, gộp mạch | Mạch 5 cũ chỉ có trang này; thêm Ký hiệu $m_j,v_j$ và câu giới hạn | 5.5 |
| 6 | `L08-M6T` | 6. Bất ổn và phạm vi bảo đảm của DQN | thêm | Trang tiêu đề mạch, điểm vào mạch 6 | chưa có |
| 6 | `L08-27` | Hai nguồn bất ổn và hai cơ chế giảm | sửa | Bảng `Nguồn bất ổn \| Cơ chế giảm \| Điều còn lại`; tương quan không thuộc bộ ba bất ổn | 6.1 |
| 6 | `L08-29` | Ví dụ: đích của một mẫu chuyển qua mốc đồng bộ | sửa | Mẫu 1: $4{,}6\to5{,}5$, $\Delta y=0{,}9$; hình bậc thang | 6.2 |
| 6 | `L08-30` | Bộ ba bất ổn trong DQN | sửa | Nhắc lại định nghĩa Bài 07; ánh xạ ba yếu tố; đổi tên SVG | 6.3 |
| 6 | `L08-30b` | Ví dụ: hai trạng thái dùng chung tham số với mạng mục tiêu | thêm | Ví dụ Bài 07 ($x(s_1)=1$, $x(s_2)=2$, $\gamma=0{,}9$, $\alpha=0{,}1$): $w_{n+1}=1{,}08\,w_n$; với $w^-$ giữ $C$ bước, $w_C=(1{,}8-0{,}8\cdot0{,}9^C)\,w^-$; $C=10$: $1{,}521$ so với $1{,}08^{10}\approx2{,}159$ | chưa có |
| 6 | `X03` | Bài tập: thí nghiệm loại bỏ | sửa, chuyển từ mạch 7 cũ | ≤ 60 âm tiết; 91 âm tiết trước sửa | 6.4 |
| 6 | `X03b` | Bài tập: thí nghiệm loại bỏ (lời giải) | thêm (tách từ `X03`) | Lời giải từng dòng | chưa có |
| 7 | `L08-M7T` | 7. Tổng kết và chuyển tiếp | thêm | Trang tiêu đề mạch, điểm vào mạch 7 | chưa có |
| 7 | `L08-34` | Kết quả và giả thiết của bài | sửa | Bảng `Kết quả \| Giả thiết không được bỏ \| Công thức hoặc thuật toán`; tách hai trang cùng tiêu đề nếu > 80 âm tiết | 7.1 |
| 7 | `L08-K1` | So sánh Q-learning bảng, tuyến tính và DQN | thêm | Bảng `Phương pháp \| Quy tắc cập nhật \| Dữ liệu dùng \| Điều kiện dừng` và `Phương pháp \| Giả thiết không được bỏ \| Kết luận` | chưa có |
| 7 | `L08-K2` | Bài tập: một bước DQN trên CartPole | thêm | Bài tổng hợp; CartPole-v1: $+1$ mỗi bước, cắt ngắn ở $500$ bước | chưa có |
| 7 | `L08-K3` | Bài tập: một bước DQN trên CartPole (lời giải) | thêm | $y=(10,1)$, $L=1$, $\partial L/\partial q=(-1,1)$; mặt nạ $Z\lor U$ cho $\delta_1=-8$; $k_{\mathrm{opt}}=1000$ thì đồng bộ | chưa có |
| 7 | `L08-K4` | Trả lời vấn đề trung tâm | thêm | Kết luận có điều kiện, dòng "Nguồn:" | chưa có |
| 7 | `L08-33` | Câu hỏi tự kiểm tra | sửa | Mở bằng "Câu hỏi: trả lời và nêu kết quả đã dùng."; bỏ hộp chỉ đường | 7.2 |
| 7 | `L08-K5` | Bài tập về nhà và tài liệu đọc | thêm | Bảng `Mạch \| Bài tập` trỏ Bài tập 08.x của ghi chú; "Tài liệu đọc:"; liên kết ghi chú; dòng nối Bài 09 | chưa có |

Số trang sau đợt sửa dự kiến: 37 trang hiện có − 5 trang bỏ (`L08-04`, `L08-05`, `L08-06`, `L08-15`, `L08-16`) + 22 trang thêm (kể cả `L08-01b2`) = 54 trang, chưa tính `X02b` và các trang cùng tiêu đề được tách khi vượt trần mật độ.

### Lệch khỏi trật tự nguồn (đợt sửa 2026-10-22)

1. Tr. 3–7 (tổng quan Q-learning) gộp vào "Tiên quyết và quy ước": Bài 06 đã dạy đầy đủ. Các ý chính giữ dưới dạng dòng "Nhắc lại:" (giá trị, phi mô hình, khác chính sách, cập nhật, $\epsilon_{\mathrm{exp}}$-tham lam, điều kiện hội tụ).
2. Tr. 8–13 (độ phức tạp mẫu, khó mở rộng): bỏ hai cận theo `note-for-author.md`. Ý quy mô vào "Vấn đề trung tâm" và `L08-03`. Ba thách thức tr. 12 làm khung "Vấn đề trung tâm". Kết luận tr. 13 về khoảng cách lý thuyết–thực hành vào `L08-30`.
3. Tr. 35 (Atari) chuyển lên mạch 2 làm ví dụ cho giao diện: giao diện thiếu ví dụ cụ thể, và `L08-20` dùng $[b,4,h,w]$ trước khi bốn khung được giới thiệu. Tr. 17 của nguồn đã nêu CNN cho đầu vào ảnh.
4. Tr. 30 (tương quan có hại) chuyển lên đầu mạch 3: hành trình khái niệm đặt vấn đề trước cơ chế. Tr. 19 của nguồn cũng mở bộ nhớ phát lại bằng "To remove correlations".
5. Tr. 31 và 33 (đích di động, mạng mục tiêu) đặt ở mạch 2 như bản trước; mạch 6 chỉ lượng hóa và đánh giá.
6. Tr. 36 (thảo luận) vào ghi chú diễn giả của "Câu hỏi tự kiểm tra", như bản trước.

### Ngoại lệ mật độ

`L08-02b` (Nội dung): 8 dòng > 6 vì phải liệt kê đủ bảy mạch và dòng đọc trước; 54 âm tiết (xem mục của trang). `L08-02c` (Vấn đề trung tâm): 70 âm tiết > 60, một dòng bài toán và năm dòng trả lời có điều kiện (xem mục của trang). Số âm tiết trước sửa của các trang vượt trần (đo ngày 2026-10-22): `L08-05` 82, `L08-18` 87, `L08-27` 70, `L08-28` 64, `L08-32` 68, `X03` 91; `L08-33` 73 (trần 80 của trang tự kiểm tra). Số sau sửa ghi vào mục của từng trang khi sửa.

### Mục từng trang (đợt sửa 2026-10-22)

#### `L08-01` Bìa: Deep Q-Learning (bước S1)

- **Trang muốn nói gì:** tên bài và câu luận đề: mạng nơ-ron thay bảng và hàm tuyến tính để biểu diễn giá trị hành động; mạng mục tiêu và bộ nhớ phát lại giảm bất ổn, không bảo đảm hội tụ.
- **Phục vụ mạch nào và thế nào:** trang tiêu đề của mạch 1 (Mở đầu). Câu luận đề nêu trước kết luận của mạch 6 và câu trả lời ở `L08-K4`, để mọi mạch sau được đọc như một phần của kết luận có điều kiện này.
- **Vấn đề còn lại trước sửa:** phụ đề "Từ bảng giá trị hành động đến mạng nơ-ron sâu" dùng mẫu "Từ … đến …" bị cấm; không có câu luận đề, đơn vị, năm học (`review-structure.md` §2 và §3 `L08-01`; `review-student.md` bảng 2 và phát hiện "trung bình | L08-01"); ghi chú diễn giả 37 âm tiết, dưới 40, và có "Bài này" làm chủ ngữ.
- **Quyết định:** sửa. Khuôn bìa theo deck 06: `h1` tên bài, `h3` "Bài 08 · Học tăng cường", câu luận đề trong `.box`, đơn vị, năm học. Câu luận đề là một câu (36 âm tiết, hiển thị trên ba dòng trong `.box`, mỗi dòng dưới 20 âm tiết ở 1280×720) như bìa deck 06; tên tiếng Anh của mạng mục tiêu và bộ nhớ phát lại đặt ở lần dùng đầu là trang này.
- **Lý do tồn tại, nhu cầu, liên kết:** điểm vào bài và mạch 1; trang sau là "Tiên quyết và quy ước" (hiện tạm là `L08-04`). Ghi chú diễn giả nêu kết quả nhận từ Bài 07 (hàm tuyến tính, Q-learning bán gradient có đủ bộ ba bất ổn), các thành phần của DQN và phạm vi kết luận. Mục tiêu hỗ trợ: định hướng cho cả sáu mục tiêu.
- **Mật độ:** trước sửa 19 âm tiết mặt trang, 2 dòng, ghi chú 37 âm tiết; sau sửa 58 âm tiết (không tính `h1`), 4 dòng nội dung, dòng hiển thị dài nhất dưới 20 âm tiết, 0 công thức hiển thị, 1 hộp chữ 1 câu, ghi chú 141 âm tiết.
- **Ghi chú bài giảng:** đoạn mở đầu thay dòng giảng viên–học kỳ–thời lượng và đoạn mô tả tài liệu nguồn bằng một đoạn giới thiệu khớp câu luận đề.

#### `L08-01b`, `L08-01b2` Tiên quyết và quy ước, phần Nhắc lại (bước S2)

- **Trang muốn nói gì:** các kết quả của Bài 06–07 mà Bài 08 dùng: quy tắc Q-learning dạng bảng; học khác chính sách và lý do không cần tỉ số lấy mẫu quan trọng; giả thiết hội tụ tới $q_*$; Q-learning bán gradient tuyến tính có bộ ba bất ổn; mạng nhiều tầng và mạng tích chập học $\theta$ bằng lan truyền ngược.
- **Phục vụ mạch nào và thế nào:** mạch 1. Cho mạch 2 mục tiêu Q-learning để biến thành đích hồi quy; cho mạch 3 khái niệm học khác chính sách; cho mạch 6 định nghĩa bộ ba bất ổn và giả thiết hội tụ dạng bảng để so sánh.
- **Vấn đề còn lại trước sửa:** `L08-04` và `L08-05` dạy lại Bài 06 như nội dung mới, không có "Nhắc lại:" (`review-structure.md` §3, bảng phát hiện nghiêm trọng); $Z$ xuất hiện trước định nghĩa (`review-math.md`, `review-student.md`); lý do không cần tỉ số lấy mẫu quan trọng sai (`review-math.md`, nghiêm trọng 1); giả thiết hội tụ thiếu MDP hữu hạn, phần thưởng bị chặn, $\gamma<1$ (`review-math.md`, nghiêm trọng 4); `L08-05` dùng "replay" trước khi giới thiệu, 82 âm tiết; thiếu nhắc lại mạng nơ-ron (`review-student.md`, nghiêm trọng).
- **Quyết định:** thêm hai trang cùng tiêu đề, gộp và bỏ `L08-04`, `L08-05`. Một trang không đủ chỗ (khoảng 95 âm tiết), nên trang đầu giữ quy tắc cập nhật và học khác chính sách (Bài 06), trang sau giữ hội tụ dạng bảng, Q-learning bán gradient và mạng nơ-ron (đi từ bảo đảm của bảng tới chỗ bảo đảm mất). Không dùng $Z$; quy ước $Q(s,\cdot)=0$ tại trạng thái kết thúc như Bài 06. Lý do không cần tỉ số lấy mẫu quan trọng rút còn một dòng trên mặt trang, lập luận đầy đủ trong ghi chú diễn giả. "Hầu chắc chắn" và vai trò của từng giả thiết nằm trong ghi chú diễn giả. Ý "bộ nhớ phát lại giữ mẫu của các chính sách cũ" của `L08-05` chuyển sang `L08-05r` ở mạch 3.
- **Liên kết:** trước là bìa `L08-01`; sau là trang "Ký hiệu" `L08-01c` (chưa có; hiện là `L08-02`). Mục tiêu hỗ trợ: mục tiêu 2 (học khác chính sách), mục tiêu 5 (giả thiết hội tụ còn thiếu).
- **Mật độ:** trước sửa `L08-04` 2 âm tiết + 2 công thức hiển thị; `L08-05` 82 âm tiết (vượt trần). Sau sửa `L08-01b` 55 âm tiết, 4 dòng (dài nhất 18 âm tiết), 1 công thức hiển thị (cỡ chữ thân, không `.math-large`, để vừa khung), 0 hộp chữ, ghi chú 121 âm tiết; `L08-01b2` 59 âm tiết, 5 dòng (dài nhất 20 âm tiết), 0 công thức hiển thị, 0 hộp chữ, ghi chú 148 âm tiết.
- **Ghi chú bài giảng:** "Phần 1 — Cầu nối từ Q-learning dạng bảng" thành mục "Kiến thức tiên quyết" (sáu nhóm in đậm có số hiệu và phát biểu lại); lý do không cần tỉ số lấy mẫu quan trọng và giả thiết hội tụ sửa theo Bài 06 (Nhận xét 06.17, Định lý 06.21); đoạn "Về độ phức tạp mẫu" chuyển tạm xuống cuối mục "Vì sao cần Deep Q-learning", sẽ viết lại ở bước `L08-02c`; câu lý do sai trong mục bộ nhớ phát lại cũng sửa ở bước này.

#### `L08-01c` Tiên quyết và quy ước, phần Ký hiệu (bước S3)

- **Trang muốn nói gì:** ký hiệu dùng ở nhiều mạch: $\gamma\in[0,1)$, $\theta\in\mathbb R^d$, $O_t\in\mathcal O$, $A_t\in\mathcal A$ hữu hạn, $R_{t+1}$ nhận sau $A_t$, $S_t$ chỉ khi $O_t$ đủ Markov, hai bộ đếm $t$ và $k_{\mathrm{opt}}$, chỉ số mẫu $i=1,\dots,b$, hai chữ epsilon.
- **Phục vụ mạch nào và thế nào:** mạch 1; cố định cách đọc chỉ số cho mạch 2 (quan sát, $R_{t+1}$), mạch 3–4 (chỉ số $i$, hai bộ đếm), mạch 5 ($\epsilon_{\mathrm{opt}}$).
- **Vấn đề còn lại trước sửa:** chưa có trang Ký hiệu (`review-structure.md` §2 `L08-01c`); $o$, $\mathcal O$ chưa định nghĩa trên mặt trang và giả thiết Markov chỉ ở ghi chú `L08-07` (`review-student.md`, `review-math.md`); $\epsilon_{\mathrm{exp}}$ chưa nối với $\varepsilon$ của Bài 06 (`review-math.md`, thuật ngữ); chỉ số thời gian và chỉ số mini-batch dễ trộn.
- **Quyết định:** thêm. Dòng "Ký hiệu:" cho $\gamma$, $\theta$; bảng hai cột `Ký hiệu | Nghĩa` bốn hàng. Không đưa $Z$, $U$, $\mathcal D$, $N$, $C$, $F$, $N_{\mathrm{start}}$ (riêng một mạch, giới thiệu tại chỗ). Không đưa $Q_\theta$, $q_i$: $Q_\theta$ là khái niệm trung tâm của mạch 2, không mở bằng ký hiệu; $q_i$ khai báo bằng dòng "Ký hiệu:" ở `L08-17` (khác $q_*$). Kỳ vọng không xuất hiện trên trang chiếu nên quy ước kỳ vọng chỉ ghi trong ghi chú bài giảng.
- **Liên kết:** trước là `L08-01b2` (Nhắc lại); sau là `L08-02` Mục tiêu học tập. Mục tiêu hỗ trợ: mục tiêu 1 và 3 (đọc đúng chỉ số trong đích và mất mát).
- **Mật độ:** trang mới. 58 âm tiết (dòng Ký hiệu 10, tiêu đề cột 3, bốn hàng 13, 7, 10, 15), 5 dòng nội dung, 0 công thức hiển thị, 0 hộp chữ, ghi chú diễn giả 123 âm tiết. Cỡ chữ bảng 0,752 em theo `lecture-slide.css`.
- **Ghi chú bài giảng:** thêm mục "Bảng ký hiệu" (22 hàng, ba cột), đoạn "Quy ước đọc", đoạn về các chữ trùng với bài trước ($\epsilon_{\mathrm{exp}}$, $q_i$, $m_j$, $v_j$, $\rho$, $m$) và tương ứng với giáo trình *Học máy thống kê*. `outline.md` thêm $\mathcal O$, $\lvert\mathcal A\rvert$, $q_*$, $\theta$, $Q_\theta$, $\mathbf q_\theta$, $\delta$, $L_B$, $g_j$; $\gamma$ đổi thành $[0,1)$.

#### `L08-02` Mục tiêu học tập (bước S4)

- **Trang muốn nói gì:** sáu việc người học làm được sau bài, mỗi việc ứng một mạch từ 2 đến 7 và có một sản phẩm kiểm được.
- **Phục vụ mạch nào và thế nào:** mạch 1; báo trước sản phẩm của từng mạch sau, để trang "Nội dung" và trang tiêu đề mỗi mạch đối chiếu được. Mục 6 là bài tổng hợp của mạch 7.
- **Vấn đề còn lại trước sửa:** tiêu đề "Kết quả học tập" lệch deck 06–07; bốn thẻ lệch sáu mục tiêu của `outline.md` (thiếu bộ tối ưu, bộ nhớ phát lại); thẻ "Mục tiêu" dễ hiểu nhầm; "mạng online", "đường dừng gradient" chưa giải nghĩa; ghi chú diễn giả có siêu dữ liệu biên soạn (`review-structure.md` §3 `L08-02`; `review-student.md`; `review-math.md` mục C).
- **Quyết định:** sửa. Danh sách đánh số sáu mục, mỗi mục một dòng ≤ 15 âm tiết, mở bằng động từ học tập (Đọc, Tính, Nêu, Viết, Giải); diễn đạt bằng ý, không dùng ký hiệu chưa giới thiệu ($\mathbf q_\theta$, $Z$, $U$, $\theta^-$). Mặt trang rút gọn sáu mục tiêu của `outline.md`; ghi chú bài giảng giữ bản đầy đủ có sản phẩm. Thêm "(optimizer)" vào lần dùng đầu "bộ tối ưu" ở `L08-01c`.
- **Liên kết:** trước là `L08-01c` (Ký hiệu); sau là trang "Nội dung" `L08-02b` (chưa có; hiện là `L08-06`).
- **Mật độ:** trước sửa 64 âm tiết, 8 dòng (bốn tiêu đề thẻ, bốn câu), ghi chú 59 âm tiết. Sau sửa 79 âm tiết (trần 80 của trang mục tiêu), 6 dòng (14, 10, 12, 14, 15, 14), 0 công thức, 0 hộp chữ, ghi chú 150 âm tiết. `L08-01c` sau khi thêm "(optimizer)": 59 âm tiết.
- **Ghi chú bài giảng:** đoạn "Sau bài này…" thành mục `## Mục tiêu học tập`, sáu mục cùng thứ tự với trang, mỗi mục nêu sản phẩm.

#### `L08-02b` Nội dung (bước S5)

- **Trang muốn nói gì:** bảy phần của bài theo đúng thứ tự, mỗi tên trùng tên trang tiêu đề mạch và trỏ tới `#/N`; tài liệu đọc trước.
- **Phục vụ mạch nào và thế nào:** mạch 1; cho người học bản đồ bài và số mạch để đối chiếu với `#/N` khi điều hướng.
- **Vấn đề còn lại trước sửa:** không có trang Nội dung (`review-structure.md` §2 `L08-02b`, bảng phát hiện nghiêm trọng "mở bài"; `review-student.md`: "sinh viên không có bản đồ bài").
- **Quyết định:** thêm. Danh sách đánh số 1–7; mỗi mục là liên kết nội bộ `#/N` (đã thử: bấm mục $N$ mở trang đầu của section ngoài thứ $N$); dòng "Đọc trước:" không in đậm như deck 07, chỉ ghi các mục kế hoạch đã xác minh (Sutton và Barto, 2018, §11.3, §16.5; Mnih và cộng sự, 2015). Ghi chú diễn giả: một câu về sản phẩm của mỗi phần 2–7, không thời lượng.
- **Liên kết:** trước là `L08-02` (Mục tiêu học tập); sau là trang "Vấn đề trung tâm" `L08-02c` (chưa có; hiện là `L08-06`).
- **Mật độ và ngoại lệ:** 54 âm tiết (trần 80 của trang nội dung), 8 dòng (bảy mục và dòng đọc trước; mục dài nhất 9 âm tiết, dòng đọc trước 13), 0 công thức, 0 hộp chữ, ghi chú 137 âm tiết. Ngoại lệ số dòng (8 > 6): trang Nội dung phải liệt kê đủ bảy mạch (`AGENTS.md`, mạch mở đầu), như deck 06–07.
- **Ghi chú bài giảng:** mục "Bảy mạch và thời lượng (120 phút)" thành "Bảy phần của chương" theo cấu trúc mới, mỗi phần kèm `note-topic-id`; bỏ thời lượng (mẫu `materials/_templates/lecture-note.md` không có mục thời lượng); thêm dòng "Đọc trước:".

#### `L08-02c` Vấn đề trung tâm (bước S6)

- **Trang muốn nói gì:** bài toán của bài (học $q_*$ khi quan sát là ảnh, hành động hữu hạn, không có mô hình) và câu trả lời có điều kiện của mỗi phần 2–6.
- **Phục vụ mạch nào và thế nào:** mạch 1; nêu trước kết luận của từng mạch, để trang tiêu đề mạch và trang trả lời vấn đề trung tâm `L08-K4` đối chiếu được.
- **Vấn đề còn lại trước sửa:** không có trang Vấn đề trung tâm (`review-structure.md` §2 `L08-02c`); `L08-06` có tiêu đề mơ hồ, dòng cảnh báo phủ định một cận mẫu chưa từng nêu, ghi chú chứa lý do biên soạn và lời chuyển "Trang kế…" (`review-structure.md` §3 `L08-06`; `review-student.md`).
- **Quyết định:** thêm `L08-02c`, xóa `L08-06`. Khuôn deck 07: hộp chứa dòng bài toán, danh sách đánh số từ 2 tới 6. Không dùng ký hiệu chưa giới thiệu: "bản sao mạng cố định" thay $\theta^-$, "dừng gradient" thay $\operatorname{sg}$. Ghi chú diễn giả: bốn khó khăn của nguồn tr. 12 (không lồi, bootstrap, dịch chuyển phân phối, bộ ba bất ổn) ứng với phần nào; lý do không trình bày hai cận độ phức tạp mẫu tr. 9, 11 (thiếu mô hình lấy mẫu, chuẩn sai số, xác suất thành công, điều kiện bao phủ). Ý "số ô tăng theo $\lvert\mathcal S\rvert\lvert\mathcal A\rvert$" của `L08-06` chuyển cho bước `L08-03`; ý "xấp xỉ hàm cần giả thiết cấu trúc mới có bảo đảm" chuyển cho bước `L08-30`.
- **Liên kết:** trước là `L08-02b` (Nội dung); sau là `L08-03`, hiện là trang đầu mạch 2 (sẽ là `L08-M2T`).
- **Mật độ và ngoại lệ:** `L08-06` trước sửa 58 âm tiết. `L08-02c` 70 âm tiết (hộp 13; dòng 14, 13, 9, 9, 12), 6 dòng, 0 công thức, 1 hộp chữ 1 câu, ghi chú 148 âm tiết. Ngoại lệ 70 > 60 (1,17 lần): trang Vấn đề trung tâm phải có dòng bài toán và một dòng trả lời cho mỗi phần 2–6 (`CLAUDE.md`, mạch mở đầu); rút thêm sẽ bỏ điều kiện của câu trả lời.
- **Ghi chú bài giảng:** thêm mục "Bài toán trung tâm của chương" ở đầu Phần 2 (bài toán, bốn khó khăn của nguồn, năm câu trả lời có điều kiện khớp trang); đoạn "Về độ phức tạp mẫu" viết lại với chúng ta làm chủ ngữ, ghi hai cận của nguồn bằng $\varepsilon_{\mathrm{acc}}$ (theo `note-for-author.md`) và lý do không dùng, chuyển vào mục này.

#### `L08-M2T` Trang tiêu đề mạch 2 (bước S7), điểm vào mạch 2

- **Trang muốn nói gì:** mạch 2 "Mạng giá trị hành động và đích hồi quy" có nhiệm vụ biến mục tiêu bootstrap của Q-learning thành nhãn hồi quy giữ cố định khi cập nhật một mạng.
- **Phục vụ mạch nào và thế nào:** điểm vào mạch 2; số "2." khớp mục 2 của `L08-02b` và `#/2` (đã thử: `#/2` và liên kết mục 2 cùng mở `L08-M2T`). Dòng dẫn nêu đúng nhu cầu chung của mạch, không trùng nhu cầu riêng của `L08-03`, nên trang ghi "ngoài hành trình khái niệm".
- **Vấn đề còn lại trước sửa:** không mạch nào có trang tiêu đề (`review-structure.md` bảng phát hiện nghiêm trọng; `review-student.md`).
- **Quyết định:** thêm. Tên mạch, dòng dẫn và từ khóa theo `review-structure.md` §1 mạch 2. Tên khác tiêu đề trang nội dung đầu tiên (`L08-03`, sẽ là "Giới hạn của bảng giá trị hành động"). Năm từ khóa đều là khái niệm của mạch: vector giá trị hành động (`L08-07`), mạng trực tuyến và mạng mục tiêu (`L08-07c`), đích hồi quy (`L08-08`), mặt nạ kết thúc (`L08-09`, `L08-12`). Không định nghĩa, công thức, hình hay "Đầu vào/Đầu ra" trên mặt trang. `data-note-topic-id` là `lec-08-topic-01`, chủ đề của trang nội dung đầu mạch.
- **Liên kết:** kế thừa: Q-learning bán gradient tuyến tính của Bài 07 (`L08-01b2`) và bài toán trung tâm (`L08-02c`, dòng 2). Giao cho mạch 3: đích hồi quy có mặt nạ kết thúc và bộ sáu thành phần của mẫu chuyển.
- **Mật độ:** dòng dẫn 17 âm tiết (trần 25), dòng từ khóa 18 âm tiết, 5 cụm; ghi chú diễn giả 88 âm tiết (khoảng 40–100).
- **Ghi chú bài giảng:** "Phần 2 — …" tách thành `## 1. Mở đầu` (chỉ gồm "Bài toán trung tâm của chương") và `## 2. Mạng giá trị hành động và đích hồi quy`; số mục bằng số mạch. Các mục con của mục 2 xếp theo thứ tự trang: "Vì sao cần Deep Q-learning" (`L08-03`), "Ví dụ: đầu vào bốn khung Atari" (`L08-31`, tách từ mục Atari của topic-15 thành chủ đề mới `lec-08-topic-16`, vì trình xem ghi chú yêu cầu mỗi `note-topic-id` xuất hiện một lần; `L08-31`, `L08-32` đổi `data-note-topic-id` sang `lec-08-topic-16`; `outline.md` cập nhật bảng ánh xạ), "Giao diện DQN và hai mạng" (`L08-07`; phần mạng mục tiêu sẽ tách cho `L08-07c`), "Bốn khung và tính Markov" (`L08-32`), topic-03 (`L08-08`), topic-04 (`L08-09`), topic-05 (`L08-12`). Nội dung từng mục chưa sửa. Các mục còn lại tạm nằm dưới tiêu đề không đánh số "Bộ nhớ phát lại, hàm mất mát, vòng huấn luyện và bất ổn" và "Kiểm tra tổng hợp và đọc thêm" cho tới bước trang tiêu đề mạch 3, 4, 6, 7. Lý do đặt "Bài toán trung tâm" ở mục 1: trang `L08-02c` thuộc mạch 1, và giữ số mục ghi chú bằng số mạch; phần mở đầu chung (mục tiêu, tiên quyết, ký hiệu, bản đồ chủ đề) giữ không đánh số theo mẫu ghi chú.

#### `L08-03` Giới hạn của bảng giá trị hành động (bước S8)

- **Trang muốn nói gì:** bảng giá trị hành động không dùng được khi quan sát là ảnh: số ô bằng $\lvert\mathcal S\rvert\lvert\mathcal A\rvert$ và phần lớn ô không có mẫu; hàm có tham số dùng chung cho giá trị ở ô chưa thăm.
- **Phục vụ mạch nào và thế nào:** mạch 2, bước vấn đề, ví dụ dẫn nhập và trực giác của khái niệm "mạng giá trị hành động" (`L08-07` là bước hình thức). Ví dụ dẫn nhập làm cụ thể vấn đề "bảng thiếu dữ liệu và phình theo $\lvert\mathcal S\rvert\lvert\mathcal A\rvert$".
- **Vấn đề còn lại trước sửa:** không có "Nhu cầu:/Muốn …" và ví dụ có số; SVG ghi "o hoặc s", $Q(s,a)$, $q_{11}$ không giải thích, nhãn chạm viền; ghi chú mở bằng "Sau khi nhắc lại…, trang này chốt…" (`review-structure.md` §3 `L08-03`; `review-student.md`; `review-math.md` nhẹ). Ý "số ô tăng theo $\lvert\mathcal S\rvert\lvert\mathcal A\rvert$" nhận từ `L08-06` (đã bỏ ở S6).
- **Quyết định:** sửa. Dòng "Muốn …"; "Ví dụ." Lunar Lander với số đặt ngay trên trang ($9\,216$ ô trạng thái, $2\,000$ lượt, $1\,896$ ô có mẫu); dòng $\lvert\mathcal S\rvert\lvert\mathcal A\rvert=9\,216\cdot4=36\,864$ (bốn hành động, Bài 06); hình vẽ lại; "Trực giác." một dòng. $9\,216$ là lưới trạng thái của bài dự đoán ở Bài 05/07, không phải số ô của bảng $Q$; trang ghi rõ "ô trạng thái" và tính riêng số ô của bảng $Q$. Nguồn số và tỉ lệ $20{,}6\%$ ở ghi chú diễn giả, không viết "như Bài 07".
- **Hình:** `img/lec-08/table-vs-dqn.svg` vẽ lại: bên trái lưới minh họa 4×5 với 4 ô có chấm (tỉ lệ một phần năm, gần $20{,}6\%$), chú giải bằng ký hiệu chấm và ô trống (không chỉ màu); bên phải $o\to$ mạng $Q_\theta$ trả về $Q_\theta(o,a_1),\dots,Q_\theta(o,a_4)$, nhãn "tham số $\theta$ dùng chung". Phông sans-serif, nhãn 32–34 đơn vị trên khung 1000×310; hiển thị bằng `figure short` (cao 260 px) nên nhãn khoảng 27 px, trên mức 0,75 em (25,2 px). Không nhãn chạm viền, mũi tên không đè chữ.
- **Liên kết:** trước là `L08-M2T`; sau là `L08-31` (ví dụ đầu vào Atari, quan sát là ảnh).
- **Mật độ:** trước sửa 23 âm tiết, 1 dòng 23 âm tiết, 1 hộp chữ, ghi chú 46 âm tiết. Sau sửa 51 âm tiết, 4 dòng (11, 13, 8, 19), 0 công thức hiển thị, 0 hộp chữ, 1 hình, ghi chú 124 âm tiết.
- **Ghi chú bài giảng:** mục "Vì sao cần Deep Q-learning" thành "Giới hạn của bảng giá trị hành động": vấn đề, Ví dụ 08.1 (khối `example`, đánh số đầu tiên của chương), đoạn về quan sát là ảnh, trực giác nối với mức lan của Bài 07, hình và đoạn đọc hình, lợi ích của dạng có tham số theo nguồn tr. 14–15, giới hạn, kiểm tra nhanh; "mạng neural" thành "mạng nơ-ron" (hai chỗ); hàng topic-01 của bản đồ chủ đề đổi tên.

### Bản trước đợt sửa 2026-10-22

Các mục dưới đây mô tả bản trước đợt sửa. Bản đồ bảy mạch cũ đã được thay ở bước C0; các bảng hành trình khái niệm, thời lượng và mục từng trang được thay khi sửa trang tương ứng.

#### Bản đồ bảy mạch ngoài (đã thay ở C0)

| mạch | range | chức năng | kết nối vào | đầu ra |
|---|---|---|---|---|
| M1 | `L08-01`, `L08-02`, `L08-04`, `L08-05`, `L08-03`, `L08-06` | Cầu nối từ bảng Q sang DQN; mốc 7+13 phút giữa `L08-03`/`L08-04` | Từ Bài 07; `L08-06` có câu nối sang giao diện mạng | Nhận ra cần tham số dùng chung và giới hạn của bảng |
| M2 | `L08-07`–`L08-09`, `L08-12`–`L08-14` | Giao diện mạng, đích bootstrap, hai cờ và replay | Vào từ `L08-06`; đích có mặt nạ dẫn sang schema chuyển tiếp và nguồn batch | Hai mạng, bộ sáu thành phần và giới hạn của replay |
| M3 | `L08-10`, `L08-15`, `L08-17`, `X01`, `L08-21`, `L08-11`, `L08-18`–`L08-20`, `L08-16`, `X02` | Đồ thị tính, loss, kiểm tra, vòng DQN, giả mã, tensor, đồng bộ và bài tập | Vào từ replay ở `L08-14`; hai đường tính đứng trước loss và hai trang kiểm tra đứng trước vòng hoàn chỉnh | Thuật toán hoàn chỉnh, gradient chỉ qua mạng online và kiểm cài đặt |
| M4 | `L08-22`–`L08-25` | Gradient và ba bộ tối ưu (nhánh dọc linh hoạt) | Vào ngang từ `L08-22` sau M3 | Quy tắc cập nhật SGD/RMSprop/Adam theo tọa độ |
| M5 | `L08-26` | Bảng so sánh và phạm vi chọn optimizer | Vào ngang từ `L08-22`; câu nối quay lại bất ổn cấu trúc | Chọn optimizer bằng thí nghiệm có kiểm soát |
| M6 | `L08-28`, `L08-27`, `L08-29`, `L08-30` | Tương quan, replay, mạng mục tiêu và bộ ba nguy hiểm | Vào từ `L08-26`; tương quan dữ liệu đứng trước trang tổng hợp hai biểu hiện | Quan hệ nhân quả đúng: hai cơ chế giảm bất ổn, không bảo đảm hội tụ |
| M7 | `L08-31`–`L08-34` + `X03` | Pipeline Atari, kiểm tra tổng hợp, ablation, hợp đồng DQN | Vào từ `L08-30`; `X03` là bài ablation dùng lại hai cơ chế; `L08-34` thu hồi bốn kết quả `L08-02` | Danh sách kiểm hợp đồng DQN |

Ranh giới hai phía đã rà: M1↔M2 (`L08-06`→`L08-07`), M2↔M3 (`L08-14`→`L08-10`), M3↔M4 (`X02`→`L08-22`), M4↔M5 (`L08-25`→`L08-26`), M5↔M6 (`L08-26`→`L08-28`), M6↔M7 (`L08-30`→`L08-31`).

#### Trang dùng chung giữa các mạch

`L08-11` và `L08-20` được dùng chung trong bảng chu trình sáu bước dưới đây (xuất hiện ở nhiều cụm khái niệm) nhưng mỗi trang chỉ chiếm một vị trí vật lý và thời lượng của nó chỉ được tính một lần trong mạch M3; không tính hai lần.

#### X03 gộp ứng dụng + kiểm tra

`X03` gộp hai vai trò: ứng dụng (thiết kế ablation loại bỏ đúng một trong hai cơ chế replay/mạng mục tiêu) và kiểm tra (phân biệt dự đoán cơ chế với kết luận thực nghiệm qua các lần chạy độc lập). Gộp để không thêm trang mới và giữ 30 phút chữa bài đúng chuẩn.

#### Hành trình khái niệm và thời lượng

| cụm | chu trình | trang | đầu vào → sản phẩm | tuyến chính | linh hoạt |
|---|---|---|---|---:|---:|
| Mở bài | vấn đề → trực giác | `L08-01`–`L08-03` | Bảng Q → nhu cầu tham số dùng chung | 7 phút | 0 |
| Q-learning làm cầu nối | hình thức → giới hạn | `L08-04`–`L08-06` | Cập nhật bảng → hành vi/đích và phạm vi kết luận | 13 phút | 0 |
| Giao diện, đích và dữ liệu | vấn đề → trực giác → ví dụ → hình thức → ứng dụng → kiểm tra | `L08-07`–`L08-09`, `L08-12`–`L08-14` | Hai mạng đã khởi tạo → đích có mặt nạ, bộ sáu thành phần và replay | 25 phút | 0 |
| Phép tính và vòng DQN | vấn đề → trực giác → ví dụ → hình thức → ứng dụng → kiểm tra | `L08-10`, `L08-15`, `L08-17`, `X01`, `L08-21`, `L08-11`, `L08-18`–`L08-20`, `L08-16`, `X02` | Batch từ replay → hai đường tính, loss, kiểm tra số, giả mã, tensor, đồng bộ và kiểm cài đặt | 35 phút | 0 |
| Bộ tối ưu phụ trợ | chu trình rút gọn | `L08-22`–`L08-26` | Gradient loss → quy tắc cập nhật có phạm vi | 7 phút | 10 phút |
| Bất ổn | vấn đề → trực giác → ví dụ → hình thức → ứng dụng → kiểm tra | `L08-28`, `L08-27`, `L08-29`, `L08-30`, `X03` | Tương quan và bootstrap đang học → mục tiêu di động, replay và bộ ba nguy hiểm | 13 phút | 0 |
| Atari và tổng hợp | ứng dụng → kiểm tra | `L08-31`–`L08-34` | Lịch sử bốn khung → kiểm hợp đồng DQN | 10 phút | 0 |

Tuyến chính có 110 phút, cộng 10 phút linh hoạt = 120 phút chính. Ba bài tập dọc có 30 phút chữa bài ngoài 120 phút chính: `X01`, `X02`, `X03`, mỗi bài 10 phút; đây không phải vượt giờ. Từ `L08-22`, đi ngang sang `L08-26` để giữ tuyến cốt lõi; đi xuống `L08-23`–`L08-25` cho 10 phút linh hoạt về SGD, RMSprop và Adam. Optimizer là công cụ phụ nên không chiếm một chu trình trọng tâm riêng.

#### Chu trình sáu bước cho các khái niệm trọng tâm

##### 1. Từ bảng Q sang biểu diễn DQN

| bước | mã trang | kiến thức hoặc dữ kiện đầu vào | sản phẩm học tập | gộp / không áp dụng |
|---|---|---|---|---|
| Vấn đề | `L08-03` | Bảng có một ô cho mỗi $(s,a)$ | Nêu được giới hạn không chia sẻ thông tin | Gộp với trực giác vì cùng một hình so sánh. |
| Trực giác | `L08-03` | Tham số dùng chung | Giải thích được khái quát và giao thoa | Gộp với vấn đề; hai hệ quả đi cùng một phép thay thế. |
| Ví dụ | `L08-06` | $|\mathcal S||\mathcal A|$ và không gian liên tục | So sánh được chi phí bảng với xấp xỉ hàm | Ví dụ định tính; không dùng cận mẫu thiếu giả thiết. |
| Hình thức / thuật toán | `L08-07` | $o\in\mathcal O$, $a\in\mathcal A$ | Đọc được giao diện vector Q và lý do tách hai mạng | Cùng trang đặt phản ví dụ một mạng trước $\theta^-\leftarrow\theta$. |
| Ứng dụng | `L08-20`, `L08-31` | Giao diện vector Q | Truy được đầu vào ảnh $[b,4,h,w]$ đến đầu ra $[b,|\mathcal A|]$ | Hai trang: hợp đồng tensor trước, pipeline Atari sau. |
| Kiểm tra | `L08-32` | Lịch sử bốn khung | Phân biệt biểu diễn giàu thông tin với bảo đảm Markov | Không gộp. |

Dữ kiện truyền xuyên cụm: $o$, $\mathcal A$ và $\mathbf q_\theta(o)$ từ `L08-07` được giữ nguyên ở `L08-20`, `L08-31` và `L08-32`.

##### 2. Đích bootstrap và loss DQN

| bước | mã trang | kiến thức hoặc dữ kiện đầu vào | sản phẩm học tập | gộp / không áp dụng |
|---|---|---|---|---|
| Vấn đề | `L08-04`, `L08-07` | Phép sao lưu tối ưu Bellman và tham số dùng chung | Nhận ra một mạng đang học có thể làm đổi cả dự đoán lẫn đích | `L08-04` khôi phục đích bảng; `L08-07` đặt phản ví dụ trước giải pháp hai mạng. |
| Trực giác | `L08-08` | $Q_\theta$, $Q_{\theta^-}$ đã khởi tạo | Xem bootstrap như nhãn hồi quy tạm thời | Không gộp. |
| Ví dụ | `L08-09` | $R=-2$, $\gamma=0{,}9$, giá trị bootstrap 100 | Tính được hai đích khi $Z=0$ và $Z=1$ | Không gộp. |
| Hình thức / thuật toán | `L08-10`, `L08-15`–`L08-17` | Batch $\{(O_i,A_i,R_i,O'_i,Z_i,U_i)\}_{i=1}^b$ | Viết đúng $y_i$, MSE, gather, $\operatorname{sg}$ và thứ tự đồng bộ | `L08-15` nối hai đường tính; `L08-16` đồng bộ sau cập nhật. |
| Ứng dụng | `L08-20` | $b$, bốn khung Atari, $|\mathcal A|$ | Truy đủ $O,O'$, online/target, gather/max, $R,Z,U$ và loss | Không gộp với kiểm tra để người học thấy hợp đồng tensor trước khi tính. |
| Kiểm tra | `X01`, `L08-21` | Batch hai mẫu, $y=(4{,}6,-2)$ | Tính loss và kiểm đúng dấu gradient | Bài dọc tính đủ; trang chính kiểm dấu cập nhật. |

Dữ kiện truyền xuyên cụm: quy ước batch $(O_i,A_i,R_i,O'_i,Z_i,U_i)$, $i=1,\ldots,b$, bắt đầu ở `L08-10`, được dùng lại nguyên dạng ở `L08-17`, `L08-19`, `L08-20` và `L08-29`.

##### 3. Bộ nhớ phát lại

| bước | mã trang | kiến thức hoặc dữ kiện đầu vào | sản phẩm học tập | gộp / không áp dụng |
|---|---|---|---|---|
| Vấn đề | `L08-11` | Chuyển tiếp liên tiếp từ một quỹ đạo | Nhận ra thu thập và tối ưu dùng hai nhịp khác nhau | Gộp với trực giác qua sơ đồ vòng huấn luyện. |
| Trực giác | `L08-11` | Hai luồng tương tác và tối ưu | Giải thích vì sao cần nơi lưu rồi lấy lại dữ liệu | Gộp với vấn đề. |
| Ví dụ | `L08-13` | Dòng thời gian các chuyển tiếp | Chỉ được các vị trí rải ra trong một mini-batch | Hình replay đồng thời minh họa cơ chế. |
| Hình thức / thuật toán | `L08-12`–`L08-14` | Schema thời gian và final observation | Mô tả hai cờ, autoreset, bộ đệm vòng và giới hạn không i.i.d. | `L08-12` là tiên quyết schema; `L08-13` gộp ví dụ với hình thức. |
| Ứng dụng | `L08-18`–`L08-19` | $\mathcal D$, $N$, $N_{\mathrm{start}}$, $b$, $F$ | Truy dấu lưu, làm nóng và lấy batch theo tần suất | Không gộp. |
| Kiểm tra | `X02`, `L08-33` | Hai cờ, final observation và batch lấy lại | Sửa bốn lỗi: quan sát, mask, dừng gradient, gather | `X02` kiểm cài đặt; `L08-33` kiểm giải thích. |

Dữ kiện truyền xuyên cụm: chuyển tiếp theo thời gian ở `L08-12` được lưu tại `L08-13`, rồi sau khi lấy batch đổi tên chỉ số sang $(O_i,A_i,R_i,O'_i,Z_i,U_i)$ ở `L08-19`.

##### 4. Vòng DQN hoàn chỉnh

| bước | mã trang | kiến thức hoặc dữ kiện đầu vào | sản phẩm học tập | gộp / không áp dụng |
|---|---|---|---|---|
| Vấn đề | `L08-11` | Mạng cần vừa tương tác vừa học từ dữ liệu cũ | Xác định hai luồng phải ghép trong một vòng | Gộp với trực giác. |
| Trực giác | `L08-11` | Vòng môi trường–replay–hai mạng | Kể được hướng đi của dữ liệu và gradient | Gộp với vấn đề bằng sơ đồ. |
| Ví dụ | `L08-12` | Một chuyển tiếp có $Z$, $U$ và API tự reset | Phân biệt final observation, reset và mask bootstrap | Dùng một schema kiểm được thay cho ví dụ số mới. |
| Hình thức / thuật toán | `L08-17`–`L08-19` | Loss batch, $N_{\mathrm{start}}$, $F$, $C$, $t$, $k_{\mathrm{opt}}$ | Truy dấu chọn, lưu, warmup, update, sync sau update và dừng | Giả mã tách hai trang để giữ cỡ chữ ít nhất 0,77 em. |
| Ứng dụng | `L08-20`, `L08-31` | Batch và giao diện mạng | Áp dụng vòng vào ảnh Atari và hành động rời rạc | `L08-20` đặt trước kiểm tra số theo yêu cầu sư phạm. |
| Kiểm tra | `L08-21`, `X02`, `L08-34` | Dấu gradient, mask, detach và sáu điều kiện | Phát hiện được cài đặt sai nghĩa DQN | Ba mức: số, code, danh sách kiểm. |

Dữ kiện truyền xuyên cụm: $Z$ che bootstrap theo MDP đang mô hình hóa; $U$ điều khiển reset; $O_{t+1}$ là final observation nếu autoreset; $t$ đếm bước môi trường; $k_{\mathrm{opt}}$ tăng sau update rồi mới kiểm tra chu kỳ $C$.

##### 5. Bất ổn, mạng mục tiêu và bộ ba nguy hiểm

| bước | mã trang | kiến thức hoặc dữ kiện đầu vào | sản phẩm học tập | gộp / không áp dụng |
|---|---|---|---|---|
| Vấn đề | `L08-07`, `L08-27` | Một mạng vừa đổi dự đoán vừa đổi đích; dữ liệu phụ thuộc hành vi | Thấy phản ví dụ trước mạng mục tiêu và nối hai biểu hiện với deadly triad | `L08-07` đặt nguyên nhân sớm; `L08-27` quay lại ánh xạ cấu trúc. |
| Trực giác | `L08-28` | Các quan sát gần nhau và chính sách thay đổi | Giải thích cỡ mẫu hiệu dụng và giới hạn replay | Không gộp. |
| Ví dụ | `L08-29` | Một chuyển tiếp cố định qua mốc đồng bộ | Chỉ ra đích có thể đổi dù dữ liệu không đổi | Gộp với hình thức bằng hiệu $y_i^{\mathrm{new}}-y_i^{\mathrm{old}}$. |
| Hình thức / thuật toán | `L08-29`–`L08-30` | $\theta^-\leftarrow\theta$, xấp xỉ hàm, bootstrap, khác chính sách | Nêu đúng quan hệ nhân quả và phạm vi deadly triad | `L08-29` gộp ví dụ–hình thức; `L08-30` tổng quát hóa. |
| Ứng dụng | `X03` | Hai cơ chế replay và mạng mục tiêu | Thiết kế phép loại bỏ đúng một thành phần | Gộp với kiểm tra vì sản phẩm là một thiết kế thí nghiệm. |
| Kiểm tra | `X03`, `L08-33` | Thước đo và nhiều lần chạy độc lập | Phân biệt dự đoán cơ chế với kết luận thực nghiệm | Không yêu cầu một số seed cố định; phải nêu cách tổng hợp độ phân tán. |

Dữ kiện truyền xuyên cụm: cùng chuyển tiếp batch ở `L08-29` giữ nguyên $(O_i,A_i,R_i,O'_i,Z_i,U_i)$; chỉ tham số tạo phần bootstrap đổi tại mốc đồng bộ.

##### Chu trình rút gọn: bộ tối ưu

Optimizer không phải khái niệm trọng tâm của DQN trong bài này. `L08-22` nêu vai trò, miền siêu tham số và giới hạn; tuyến ngang đi sang `L08-26`. `L08-23`–`L08-25` là nhánh dọc 10 phút cho ba quy tắc. Bước “ví dụ tính số” và “kiểm tra riêng” ghi `không áp dụng`: nguồn không có ví dụ optimizer, còn việc thêm một bài tính mới sẽ lấy thời gian khỏi replay, mạng mục tiêu và loss.

#### Bản đồ truyền dữ kiện

- Chuyển tiếp $(O_t,A_t,R_{t+1},O_{t+1},Z_{t+1},U_{t+1})$ được định nghĩa ở `L08-12`; $O_{t+1}$ lấy từ final observation trước autoreset. Khi lấy batch, đổi tên thành $(O_i,A_i,R_i,O'_i,Z_i,U_i)$, $i=1,\ldots,b$, ở `L08-10`, `L08-17`, `L08-19`, `L08-20` và `L08-29`.
- $b,N_{\mathrm{start}},N,F,C,t,k_{\mathrm{opt}}$ đi từ miền khai báo ở `L08-13`, `L08-16`, `L08-18` vào điều kiện tối ưu và đồng bộ ở `L08-19`.
- Giao diện $\mathbf q_\theta(O)\in\mathbb R^{|\mathcal A|}$ ở `L08-07` đi vào `gather` ở `L08-19`–`L08-20` và pipeline Atari ở `L08-31`.
- Ví dụ hai mẫu ở `X01` được tóm lại ở `L08-21`; cùng dấu sai số được dùng để kiểm hướng gradient.
- Replay và mạng mục tiêu được tách ở `L08-13`–`L08-16`, hợp nhất trong công thức `L08-17`, rồi quay lại như hai cơ chế ở `L08-27`–`L08-30`.

#### Ánh xạ lecture note → deck

Mỗi trang có đúng một `data-note-topic-id`; một chủ đề có thể trải trên nhiều trang.

| `note-topic-id` | `data-slide-id` |
|---|---|
| `lec-08-topic-01` | `L08-01`, `L08-02`, `L08-03`, `L08-06` |
| `lec-08-topic-02` | `L08-07` |
| `lec-08-topic-03` | `L08-08` |
| `lec-08-topic-04` | `L08-09` |
| `lec-08-topic-05` | `L08-12`, `X02` |
| `lec-08-topic-06` | `L08-13` |
| `lec-08-topic-07` | `L08-14`, `L08-28` |
| `lec-08-topic-08` | `L08-10`, `L08-15` |
| `lec-08-topic-09` | `X01`, `L08-17`, `L08-21` |
| `lec-08-topic-10` | `L08-11`, `L08-18`, `L08-19` |
| `lec-08-topic-11` | `L08-20` |
| `lec-08-topic-12` | `L08-16`, `L08-27`, `L08-29`, `L08-30` |
| `lec-08-topic-13` | `L08-04`, `L08-05` |
| `lec-08-topic-14` | `L08-22`–`L08-26` |
| `lec-08-topic-15` | `L08-31`–`L08-34`, `X03` |

#### Từng trang chiếu

| mã | luận điểm trung tâm | bước học tập | câu nối / lý do |
|---|---|---|---|
| `L08-01` | DQN thay bảng Q bằng mạng sâu. | mở vấn đề | Nối từ Bài 07. |
| `L08-02` | Bốn sản phẩm học tập kiểm chứng được. | định hướng | Chuyển sang giới hạn của bảng. |
| `L08-03` | Tham số chung tạo khái quát và giao thoa. | vấn đề, trực giác | Chuẩn bị cập nhật Q. |
| `L08-04` | Q-learning dạng bảng khai báo mặt nạ, $\alpha_t>0$ và điều kiện biên của $\gamma$. | hình thức | Xác định đích và miền trước chính sách. |
| `L08-05` | Hành vi khám phá khác phép tối ưu Bellman; phép cực đại không cần importance sampling. | hình thức, giới hạn | Nêu nguồn lệch hành vi thứ nhất. |
| `L08-06` | Cận mẫu cần thiết lập, không chỉ chiều biểu diễn. | giới hạn | Dẫn sang giao diện mạng thay vì định lý thiếu giả thiết. |
| `L08-07` | Phản ví dụ một mạng đặt mục tiêu di động trước giải pháp hai mạng. | vấn đề, hình thức | Khởi tạo $\theta^-\leftarrow\theta$ sau khi nguyên nhân đã rõ. |
| `L08-08` | Bootstrap tạo nhãn hồi quy tạm thời từ mạng mục tiêu cố định theo đoạn. | trực giác | Dẫn tới ca kết thúc. |
| `L08-09` | Kết thúc thật loại nhánh bootstrap. | ví dụ | Chuẩn bị mặt nạ trong loss. |
| `L08-10` | Gather chọn hành động lưu; MSE chỉ truyền gradient qua mạng online. | hình thức | Dẫn tới bài tính. |
| `X01` | Tính target, TD error, MSE và gradient. | kiểm tra | Hoàn tất cụm đích DQN. |
| `L08-11` | Huấn luyện xen kẽ tương tác và tối ưu. | trực giác | Mở cụm thuật toán. |
| `L08-12` | Kết thúc, cắt ngắn và autoreset có nghĩa khác nhau. | hình thức | Chốt schema và final observation trước khi lưu. |
| `L08-13` | Replay có dung lượng, batch và hai nguồn lệch hành vi. | cơ chế | Dẫn tới giới hạn. |
| `L08-14` | Replay không tạo mẫu i.i.d. | giới hạn | Chuyển sang mạng mục tiêu. |
| `L08-15` | Đường dự đoán và đường tạo đích không nhận cùng gradient. | cơ chế | Nối hai mạng đã giới thiệu với lịch đồng bộ. |
| `L08-16` | Đồng bộ dùng $k_{\mathrm{opt}}$ sau bước cập nhật. | hình thức | Hợp nhất thành loss. |
| `L08-17` | Công thức đầy đủ dùng $(O_i,A_i,R_i,O'_i,Z_i,U_i)$, $i=1,\ldots,b$. | hình thức | Chuẩn bị giả mã. |
| `L08-18` | Thu thập lưu final observation; khai báo warmup và tần suất. | thuật toán | Chuyển sang tối ưu. |
| `L08-19` | Tối ưu sau warmup theo $F$; đồng bộ sau update theo $C$. | thuật toán | Chuyển sang tensor. |
| `L08-20` | Batch Atari truy đủ hai mạng, gather, max, cờ, dtype và thiết bị. | ứng dụng | Đặt hợp đồng tensor trước kiểm tra số. |
| `L08-21` | Dấu gradient khớp sai số của hai mẫu. | kiểm tra | Dẫn tới sửa giả mã. |
| `X02` | Sửa final observation, mask MDP, dừng gradient và gather. | kiểm tra | Hoàn tất cụm thuật toán. |
| `L08-22` | Optimizer chỉ biến gradient thành bước tham số; miền siêu tham số được khai báo. | vấn đề phụ | Trang ngang cốt lõi; đi xuống để xem chi tiết. |
| `L08-23` | SGD dùng gradient hiện tại. | hình thức phụ | Nhánh dọc linh hoạt. |
| `L08-24` | RMSprop chuẩn hóa theo moment bậc hai. | hình thức phụ | Phần linh hoạt. |
| `L08-25` | Adam kết hợp moment bậc nhất và bậc hai. | hình thức phụ | Phần linh hoạt; đã sửa dấu `\quad`. |
| `L08-26` | Chọn optimizer bằng thí nghiệm có kiểm soát. | ứng dụng, giới hạn | Trang ngang tiếp theo; quay lại bất ổn cấu trúc. |
| `L08-27` | Hai biểu hiện bất ổn được ánh xạ vào deadly triad. | vấn đề | Tách nguyên nhân khỏi biện pháp giảm nhẹ. |
| `L08-28` | Tương quan làm giảm thông tin mới trong batch. | trực giác | Nối lại replay. |
| `L08-29` | Mạng mục tiêu làm chậm, không tạo ra, mục tiêu di động. | ví dụ, hình thức | Nối đúng quan hệ nhân quả với đồng bộ. |
| `L08-30` | DQN vẫn chứa deadly triad. | giới hạn | Chuyển sang ứng dụng Atari. |
| `L08-31` | Atari có giao diện quan sát–hành động–phần thưởng tối thiểu, không phải đặc tả tái lập. | ứng dụng | Kiểm tra giả thiết Markov. |
| `L08-32` | Bốn khung không bảo đảm Markov. | kiểm tra | Chuẩn bị tổng hợp. |
| `L08-33` | Bốn câu phân biệt cơ chế và phạm vi. | kiểm tra | Dẫn tới bài phân tích loại bỏ. |
| `X03` | Thí nghiệm loại bỏ đổi đúng một thành phần và dùng cùng kế hoạch chạy cho mọi nhánh. | ứng dụng, kiểm tra | Không áp đặt một số seed cụ thể khi chưa có ngân sách. |
| `L08-34` | Sáu điều kiện tạo hợp đồng DQN đúng nghĩa. | tổng hợp | Kết thúc bằng danh sách kiểm. |
