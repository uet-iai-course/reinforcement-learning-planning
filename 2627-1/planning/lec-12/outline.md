# Dàn ý Bài 12: Nhập môn Học tăng cường đa tác tử

## Phạm vi

Nguồn chính: `RL-hk2-2025-2026/Lecture12-MARL.pptx`, 54 trang chiếu, 76 mục media, không có trang ẩn, không có ghi chú nội dung và không có code demo. Bài giữ toàn bộ mạch kiến thức có liên quan tới Học tăng cường đa tác tử (MARL), sửa các công thức sai và thay mọi ảnh kỹ thuật bằng HTML, KaTeX hoặc SVG. Không giữ tài sản raster.

Mục tiêu đầu ra:

1. viết đúng hợp đồng trò chơi Markov dưới quan sát cục bộ, joint action, reward regime và cân bằng Nash;
2. giải thích huấn luyện tập trung, thực thi phân tán (CTDE) và phân biệt CTDE với giao tiếp khi chạy;
3. tính baseline COMA, viết một bước TD của QMIX, target MADDPG và objective MAPPO/HAPPO;
4. chọn benchmark theo action, observation, reward và số tác tử;
5. kiểm tra giới hạn bằng chứng, phiên bản framework và hợp đồng giao tiếp.

## Thời lượng

| cụm | trang | cốt lõi | linh hoạt |
|---|---|---:|---:|
| Định hướng | `L12-01`–`L12-03` | 6 phút | 0 |
| Hợp đồng MARL và CTDE | `L12-04`–`L12-12`, gồm `L12-07B` | 25 phút | 0 |
| COMA | `L12-13`–`L12-17` | 15 phút | 0 |
| VDN và QMIX | `L12-18`–`L12-22B` | 15 phút | 0 |
| MADDPG, MAPPO, HAPPO/HATRPO | `L12-23`–`L12-28` | 18 phút | 0 |
| Benchmark | `L12-29`–`L12-34` | 19 phút | 0 |
| Framework | `L12-35`–`L12-37` | 0 | 6 phút |
| Giao tiếp: kênh, topology, policy và nội dung | `L12-38`–`L12-42` | 10 phút | 0 |
| Giao tiếp: tích hợp và mô hình đe dọa | `L12-43`–`L12-44` | 0 | 4 phút |
| Kết | `L12-45` | 2 phút | 0 |
| Tổng | 42 trang cốt lõi + 5 trang linh hoạt | 110 phút | 10 phút |

Tuyến trình chiếu cốt lõi 110 phút dùng phím Phải tại `L12-34` (`#/5/6`) để sang `L12-38` (`#/6/1`), và tại `L12-42` (`#/6/5`) để sang `L12-45` (`#/7/1`). Tuyến trình chiếu đủ 120 phút dùng thêm `L12-35`–`L12-37` (`#/5/7`–`#/5/9`) và `L12-43`–`L12-44` (`#/6/6`–`#/6/7`).

Ba bài tập `X01`–`X03` nằm ngoài 120 phút trình chiếu và dùng 30 phút còn lại, lần lượt 8, 12 và 10 phút. Sau kết luận, dùng phím Xuống để mở các trang tại `#/7/2`–`#/7/4`. Bảy mạch ngoài lần lượt là mở bài; hợp đồng MARL; COMA–VDN/QMIX; actor–critic; benchmark–framework; giao tiếp; kết luận–bài tập. Không có code demo vì nguồn không có nội dung tương ứng.

## Ánh xạ 54/54 trang nguồn

| nguồn | quyết định | trang đích | lý do |
|---:|---|---|---|
| 1 | sửa | `L12-01` | Sửa “Muti”, metadata và bỏ logo. |
| 2 | giữ, sửa | `L12-02` | Vẽ lại tuyến phương pháp và dùng làm cầu nối. |
| 3 | bỏ, thay | `L12-03` | Overview sót nội dung bài trước; thay bằng kết quả học tập. |
| 4 | gộp, sửa | `L12-04`–`L12-05` | Tách động lực nền khỏi góc nhìn siêu tác tử. |
| 5 | gộp, sửa | `L12-04`–`L12-05` | Nêu MDP cảm sinh thay đổi khi $\pi_{-i}$ đổi. |
| 6 | tách, sửa, thêm cầu nối | `L12-06`–`L12-07B` | Bổ sung miền/kiểu, định nghĩa $\tau_i$, kernel chuẩn hóa và công thức MDP cảm sinh trong trường hợp đủ giả thiết. |
| 7 | sửa | `L12-08`–`L12-09` | Sửa Nash, objective và reward regimes; giới hạn quan hệ tối ưu chung → Nash cho common payoff. |
| 8 | tách, sửa | `L12-10`–`L12-11` | CTDE là hợp đồng thông tin, không chỉ actor–critic. |
| 9 | sửa | `L12-09` | Sửa zero-sum và general-sum reward vector. |
| 10 | gộp, sửa | `L12-12` | Gom bốn trục khó; nối parameter sharing với agent ID, vai trò và tác tử dị thể. |
| 11 | gộp | `L12-03` | Danh sách thuật toán trở thành bản đồ mục tiêu. |
| 12 | tách, sửa | `L12-13`–`L12-17`, `X02` | COMA đi từ gán công đến ví dụ nhất quán $Q=6$, công thức, giới hạn và kiểm tra tại chỗ. |
| 13 | sửa | `L12-23`, `X02` | Thay stochastic score gradient sai bằng deterministic chain rule và target đủ. |
| 14 | tách, sửa, thêm thuật toán | `L12-18`–`L12-22B`, `X02` | Tách VDN khỏi QMIX, sửa argmax theo quan hệ tập hợp, thêm replay/online-target/terminal mask/TD loss và kiểm tra tại chỗ. |
| 15 | tách, sửa | `L12-24`, `L12-26` | Tách miền thông tin IPPO/MAPPO; bỏ thứ hạng phổ quát. |
| 16 | sửa | `L12-25` | Tỷ số và tham số theo từng tác tử; batch, old log-probability và advantage cố định. |
| 17 | sửa, sắp lại | `L12-27`–`L12-28`, `X02` | Đặt vấn đề/ví dụ trước objective clipped đầy đủ và recurrence $M_{m+1}=r_m^{\mathrm{new}}M_m$. |
| 18 | sửa | `L12-27`–`L12-28` | Giữ contour như động cơ định tính, bỏ claim quá mạnh. |
| 19 | gộp | `L12-29` | Mở phần benchmark bằng các trục kiểm soát. |
| 20 | gộp, sửa | `L12-30` | MPE có cooperative, competitive và mixed tasks. |
| 21 | bỏ ảnh, giữ giới hạn | `L12-34` | Không dựng lại đường cong thiếu dữ liệu gốc. |
| 22 | gộp, sửa | `L12-30` | LBF phụ thuộc reward mode và observability. |
| 23 | gộp, sửa | `L12-31` | RWARE có reward shared hoặc individual. |
| 24 | gộp | `L12-31` | Minigrid/MARLGrid dùng làm grid benchmark. |
| 25 | gộp, sửa | `L12-32` | MAMuJoCo chia khớp cho tác tử, bỏ caption lặp. |
| 26 | gộp, sửa | `L12-32`, `L12-34` | Giữ partition, bỏ đường cong thiếu dữ liệu. |
| 27 | gộp | `L12-32` | Giữ SMAC, observation và action type. |
| 28 | gộp, sửa | `L12-32`, `L12-34` | Giữ scenario, bỏ xếp hạng từ biểu đồ. |
| 29 | gộp | `L12-33` | Unity football là một ca mixed-team. |
| 30 | gộp | `L12-33` | GRF có state/image observation và self-play. |
| 31 | sửa | `L12-33`–`L12-34` | Bỏ claim SOTA và bar chart thiếu protocol. |
| 32 | gộp, sửa | `L12-33` | Số 22–1000 là cấu hình nguồn, không phải giới hạn platform. |
| 33 | gộp | `L12-33` | Pogema minh họa partial observation và sparse reward. |
| 34 | bỏ hiển thị | ghi chú `L12-33` | AutoGen là hệ agent LLM, không mặc nhiên là MARL. |
| 35 | sửa, gộp | `L12-33` | Neural MMO 2023 được ghi như sự kiện đã kết thúc. |
| 36 | sửa, gộp | `L12-33` | OpenAI Five dùng action phân rã/rời rạc hóa. |
| 37 | bỏ | `L12-33` | UI/gameplay không thêm nội dung khái niệm. |
| 38 | sửa, gộp | ghi chú `L12-33`, `L12-34` | Tỷ lệ Arena có mẫu và mốc lịch sử; bảng training không dùng để suy rộng. |
| 39 | gộp | `L12-35` | Mở phần framework bằng ma trận chức năng. |
| 40 | gộp | `L12-35` | PyMARL được mô tả theo vai trò lịch sử. |
| 41 | gộp, sửa | `L12-35` | Dùng tên EPyMARL và phạm vi nguồn. |
| 42 | bỏ ảnh | `L12-34` | Không dựng lại đường cong LBF thiếu protocol. |
| 43 | gộp, sửa | `L12-35` | MARLlib được mô tả theo paper, không nói hiện trạng. |
| 44 | sửa, vẽ lại | `L12-36` | Khái quát kiến trúc thành các lớp chức năng. |
| 45 | gộp, sửa | `L12-35` | HARL gắn với tác tử dị thể; support cần pin phiên bản. |
| 46 | bỏ ảnh | `L12-34`, `L12-37` | Đường cong chuyển thành yêu cầu tái lập và câu kiểm tra framework tại chỗ. |
| 47 | gộp, thêm ví dụ | `L12-38` | Mở phần giao tiếp bằng ca robot kho có quan sát cục bộ. |
| 48 | sửa | `L12-38` | Tách CTDE khỏi message passing khi thực thi bằng miền input actor. |
| 49 | giữ, sửa | `L12-39` | Chuẩn hóa năm trục và tách topology khỏi quyết định gửi. |
| 50 | giữ, sửa | `L12-40` | Who-to-whom chỉ xác định các cạnh hợp lệ. |
| 51 | giữ, sửa | `L12-41` | Policy quyết định có gửi/khi nào trên topology đã có; $T$ chỉ là tần suất. |
| 52 | giữ, sửa | `L12-42` | Chuẩn hóa experience, hidden state và intention. |
| 53 | giữ, sửa | `L12-43` | Hiện đường phụ thuộc actor/critic và execution availability. |
| 54 | giữ, sửa | `L12-44` | Sửa chiều privacy và yêu cầu threat model. |

## Ánh xạ chủ đề bài đọc sang trang chiếu

| note-topic-id | vai trò | data-slide-id |
|---|---|---|
| topic-01 | mở nền tảng | `L12-01`–`L12-06` |
| topic-02 | hợp đồng trò chơi Markov | `L12-07`, `L12-07B`, `L12-08`, `L12-09`, `X01` |
| topic-03 | CTDE | `L12-10`–`L12-12` |
| topic-11 | cầu nối policy gradient/actor–critic | `L12-13` |
| topic-04 | COMA | `L12-14`–`L12-17` |
| topic-05 | VDN/QMIX | `L12-18`–`L12-22B`, `X02` |
| topic-06 | MADDPG | `L12-23` |
| topic-12 | cầu nối PPO | `L12-24` |
| topic-07 | IPPO/MAPPO | `L12-25`–`L12-26` |
| topic-08 | HAPPO/HATRPO | `L12-27`–`L12-28` |
| topic-09 | benchmark | `L12-29`–`L12-32`, `L12-34`, `X03` |
| topic-13 | framework | `L12-35`–`L12-37` |
| topic-10 | giao tiếp | `L12-38`–`L12-44` |
| topic-14 | đọc thêm benchmark | `L12-33` |
| topic-15 | tài liệu/kết luận | `L12-45` |

Mỗi trong 50 trang có đúng một topic chính; topic-14 và topic-15 được gấp vào trang có nội dung tương ứng để không thêm trang riêng. `X02` lấy topic-05 làm chủ đề chính nhưng đồng thời kiểm tra COMA, MADDPG và HAPPO thuộc topic-04, topic-06 và topic-08.

## Kiểm kê và ánh xạ 76/76 media

| media | nguồn | xử lý |
|---|---|---|
| `image1.png` | 1, 4–10, 12–18, 20–38, 40–46, 48–54 | Logo chữ HMI; bỏ. |
| `image2.png` | cùng nhóm trên | Biểu tượng HMI; bỏ. |
| `image3.png` | 1 | Logo FIT/VNU; bỏ. |
| `image4.png` | 2 | Vẽ lại `path-to-marl.svg`. |
| `image5.png` | 3 | Overview sai bài; bỏ. |
| `image6.png` | 4 | Vẽ lại trong `two-views.svg`. |
| `image7.png` | 5 | Gộp vào `two-views.svg`. |
| `image8.png` | 5 | Gộp vào `two-views.svg`. |
| `image9.png` | 6 | Vẽ lại `markov-game-loop.svg`. |
| `image10.png` | 7 | Dựng objective bằng KaTeX. |
| `image11.png` | 7 | Dựng lại Nash bằng KaTeX và sửa ký hiệu. |
| `image12.png` | 8, 50 | Vẽ lại CTDE trong `ctde-flow.svg`; topology trong `comm-topologies.svg`. |
| `image13.png` | 12 | Dựng COMA advantage bằng KaTeX. |
| `image14.png` | 12 | Dựng policy gradient bằng KaTeX. |
| `image15.png` | 12 | Dựng baseline bằng KaTeX và thêm trọng số policy. |
| `image16.png` | 12 | Dựng COMA gradient bằng KaTeX. |
| `image17.png` | 13 | Dựng critic loss/target bằng KaTeX. |
| `image18.png` | 13 | Thay bằng deterministic gradient KaTeX. |
| `image19.png` | 14 | Dựng đạo hàm đơn điệu bằng KaTeX. |
| `image20.png` | 14 | Dựng IGM argmax bằng KaTeX. |
| `image21.png` | 14 | Dựng phép cộng và gắn đúng nhãn VDN. |
| `image22.png` | 16 | Dựng PPO objective bằng KaTeX. |
| `image23.png` | 16 | Dựng ratio MAPPO theo tác tử bằng KaTeX. |
| `image24.png` | 18 | Không chép contour; giữ kết luận định tính có giới hạn. |
| `image25.png` | 20 | Thay bằng taxonomy và `benchmark-map.svg`. |
| `image26.png` | 21 | Đường cong thiếu dữ liệu; bỏ. |
| `image27.png` | 22 | Thay bằng mô tả LBF và sơ đồ benchmark. |
| `image28.png` | 23 | Thay bằng mô tả RWARE và sơ đồ benchmark. |
| `image29.png` | 24 | Screenshot Minigrid; bỏ. |
| `image30.png` | 24 | Thay bằng sơ đồ benchmark. |
| `image31.png` | 25 | Vẽ khái quát trong `benchmark-map.svg`. |
| `image32.png` | 25–26 | Screenshot lặp; bỏ. |
| `image33.png` | 26 | Gộp partition vào `benchmark-map.svg`. |
| `image34.png` | 26 | Gộp partition vào `benchmark-map.svg`. |
| `image35.png` | 26 | Đường cong thiếu dữ liệu; bỏ. |
| `image36.png` | 26 | Gộp partition vào `benchmark-map.svg`. |
| `image37.png` | 27 | Logo SMAC; bỏ. |
| `image38.png` | 28 | Vẽ scenario khái quát trong `benchmark-map.svg`. |
| `image39.png` | 28 | Đường cong thiếu dữ liệu; bỏ. |
| `image40.png` | 29 | Screenshot Unity; thay bằng taxonomy. |
| `image41.png` | 30 | Screenshot GRF 3v1; thay bằng taxonomy. |
| `image42.png` | 30 | Screenshot GRF 11v11; thay bằng taxonomy. |
| `image43.png` | 31 | Bar chart thiếu protocol; bỏ. |
| `image44.png` | 32 | Vẽ many-agent khái quát trong `benchmark-map.svg`. |
| `image45.png` | 32 | Gộp vào `benchmark-map.svg`. |
| `image46.png` | 33 | Vẽ local-view khái quát trong `benchmark-map.svg`. |
| `image47.png` | 34 | AutoGen không thuộc benchmark MARL; bỏ. |
| `image48.png` | 35 | Neural MMO map; thay bằng taxonomy. |
| `image49.png` | 35 | Gameplay; bỏ. |
| `image50.png` | 35 | Inventory UI; bỏ. |
| `image51.png` | 36 | Dota poster; bỏ. |
| `image52.png` | 37 | Dota UI; bỏ. |
| `image53.png` | 37 | Dota gameplay; bỏ. |
| `image54.png` | 37 | Dota gameplay; bỏ. |
| `image55.png` | 38 | Bảng training; chỉ giữ mốc cần thiết trong ghi chú. |
| `image56.png` | 40 | PyMARL plots; bỏ. |
| `image57.png` | 41 | Dựng EPyMARL bằng bảng HTML. |
| `image58.png` | 42 | Đường cong LBF; bỏ. |
| `image59.png` | 43 | MARLlib mosaic; bỏ. |
| `image60.png` | 44 | Vẽ lại `framework-layers.svg`. |
| `image61.png` | 45 | Dựng HARL bằng bảng HTML. |
| `image62.png` | 46 | Đường cong HARL; bỏ. |
| `image63.emf` | 48 | Dựng nhận biết/CTDE bằng HTML. |
| `image64.png` | 50 | Vẽ lại trong `comm-topologies.svg`. |
| `image65.png` | 50 | Vẽ lại trong `comm-topologies.svg`. |
| `image66.png` | 51 | Vẽ lại `comm-gate.svg`. |
| `image67.png` | 52 | Dựng nội dung message bằng HTML. |
| `image68.png` | 53 | Vẽ lại `message-integration.svg`. |
| `image70.png` | 13 | Prose MADDPG raster; thay HTML/KaTeX. |
| `image73.png` | 14 | Prose QMIX raster; thay HTML/KaTeX. |
| `image77.png` | 15 | Prose MAPPO raster; thay HTML, bỏ SOTA. |
| `image80.png` | 17 | Thủ tục HAPPO raster; thay danh sách HTML. |
| `image520.png` | 6 | Formal block; thay HTML/KaTeX. |
| `image540.png` | 7 | Objective/NE/type block; thay HTML/KaTeX. |
| `image560.png` | 52 | Future-intent block; thay HTML. |
| `image750.png` | 16 | PPO/MAPPO prose; thay HTML/KaTeX. |

## Ký hiệu

| ký hiệu | nghĩa và miền |
|---|---|
| $\mathcal N=\{1,\ldots,N\}$ | tập tác tử |
| $\Delta(\mathcal X)$ | tập các phân phối xác suất trên $\mathcal X$ |
| $S_t\in\mathcal S$ | trạng thái môi trường |
| $O_{t,i}\in\mathcal O_i$, $\tau_{t,i}\in\mathcal T_i$ | quan sát và chuỗi $(o_{0,i},a_{0,i},\ldots,o_{t,i})$ của tác tử $i$ |
| $A_{t,i}\in\mathcal A_i$, $\mathbf A_t\in\prod_i\mathcal A_i$ | hành động cục bộ và hành động chung |
| $P:\mathcal S\times\mathcal A\to\Delta(\mathcal S)$ | kernel chuyển tiếp nền |
| $\Omega:\mathcal S\to\Delta(\mathcal O)$ | kernel quan sát chung, $\mathcal O=\prod_i\mathcal O_i$ |
| $r_i:\mathcal S\times\mathcal A\to\mathbb R$ | phần thưởng của tác tử $i$ |
| $\pi_i:\mathcal T_i\to\Delta(\mathcal A_i)$ | policy phân tán ngẫu nhiên |
| $P_i^{\pi_{-i}}$, $r_i^{\pi_{-i}}$ | chuyển tiếp và reward cảm sinh khi cố định policy của các tác tử khác; tích policy giả định hành động độc lập có điều kiện theo state, còn công thức tổng chỉ áp cho trường hợp rời rạc đầy đủ giả thiết |
| $\mu_i(o_i)$ | actor tất định của MADDPG |
| $Q(s,\mathbf a)$ | centralized critic chung trong COMA |
| $Q_i(x,\mathbf a)$, $x$ | centralized critic riêng của tác tử $i$ và input chung, chẳng hạn joint observation hoặc state |
| $Q_i(\tau_i,a_i)$, $Q_{\mathrm{tot}}$ | utility cục bộ và joint action-value trong VDN/QMIX |
| $\theta$, $\bar\theta$ | tham số online và target của QMIX; dấu gạch cũng ký hiệu mạng đích trong MADDPG |
| $m=1-d$ | mặt nạ terminal thật: $0$ ở terminal, $1$ nếu tiếp tục; cutoff chưa terminal vẫn bootstrap |
| $r_{t,i}(\theta_i)$ | tỷ số policy mới/cũ của tác tử $i$ trong MAPPO |
| $M_m$, $M_{m+1}=r_m^{\mathrm{new}}M_m$ | multiplier HAPPO trước và sau khi cập nhật tác tử hiện tại |

## Tài sản SVG đích

`path-to-marl.svg`, `two-views.svg`, `markov-game-loop.svg`, `ctde-flow.svg`, `coma-counterfactual.svg`, `qmix-mixer.svg`, `benchmark-map.svg`, `framework-layers.svg`, `comm-topologies.svg`, `comm-gate.svg`, `message-integration.svg`.

Mọi SVG có `role="img"`, `title`, `desc`, nhãn chữ và đường viền; không dùng màu làm tín hiệu duy nhất. Toàn bộ chữ có nghĩa dùng cỡ nguồn từ `30px` trở lên; `benchmark-map.svg` dùng `34px`, và các hình cao được nới cục bộ để cỡ chiếu đạt ít nhất khoảng `0.75em`.

## Danh mục mã trang đích

Thứ tự nội dung: `L12-01`–`L12-07`, `L12-07B`, `L12-08`–`L12-22`, `L12-22B`, `L12-23`–`L12-45`. Cụm bài tập nằm sau kết luận trong cùng mạch cuối: `X01`, `X02`, `X03`. Tổng cộng 47 trang chính và 3 trang bài tập.

Danh mục 50 mã trang: `L12-01`, `L12-02`, `L12-03`, `L12-04`, `L12-05`, `L12-06`, `L12-07`, `L12-07B`, `L12-08`, `L12-09`, `L12-10`, `L12-11`, `L12-12`, `L12-13`, `L12-14`, `L12-15`, `L12-16`, `L12-17`, `L12-18`, `L12-19`, `L12-20`, `L12-21`, `L12-22`, `L12-22B`, `L12-23`, `L12-24`, `L12-25`, `L12-26`, `L12-27`, `L12-28`, `L12-29`, `L12-30`, `L12-31`, `L12-32`, `L12-33`, `L12-34`, `L12-35`, `L12-36`, `L12-37`, `L12-38`, `L12-39`, `L12-40`, `L12-41`, `L12-42`, `L12-43`, `L12-44`, `L12-45`, `X01`, `X02`, `X03`.

Bản trích văn bản nguồn dùng để kiểm kê có 585 dòng theo `wc -l`; con số 639 do cầu nối chuẩn hóa không được dùng làm số dòng nguồn.
