# Năm vai rà deck 10 (bản đóng băng `bf5e2ecc`, 2026-11-21): phát hiện và quyết định của điều phối viên

Năm vai `general-purpose`, `opus`, `high`, chạy song song, chỉ đọc: sinh viên (chỉ ảnh), toán, văn học thuật–sư phạm (`no-ai-slop` Detect), mạch truyện, chuyên gia học tăng cường. Không vai nào thấy số sai giá trị. Phần A là bản tóm tắt phát hiện theo vai (báo cáo đầy đủ trả về trong phiên); phần B là quyết định giao biên tập viên; phần C là đề xuất chờ tác giả.

## A. Phát hiện theo vai (tóm tắt)
## Sinh viên (xong)
NT: 2-09 số "bài toán một bước của ghi chú… 0,5" ngoài deck; 3-04 critic w_A,w_B trước thuật toán 3-10; narrow 390 chữ 7–8px (giới hạn học phần?).
TB: 2-04 H_t chưa định nghĩa (có ở 2-10), thiếu bước Σπ∇logπ=∇Σπ; 3-02 số trước định nghĩa, G^1 vs λ∈[0,1), chú thích hình nhỏ; 4-24 ν^π tổng 0,145 gọi "phân bố"; 4-15 π'=(0,6;0,8) gán lại không kết luận; 4-17 dòng cuối "giá trị không khớp" mơ hồ; 4-25 tìm kiếm lùi trước thuật toán 4-09; 4-09 g mất γ^t; 5-05/5-12 "vòng trong" chưa định nghĩa; 5-03 vs 5-05 mâu thuẫn tham số tách, "quán tính bộ tối ưu" 5-06; 6-15 câu 4 lượt bị cắt ngắn chưa dựng.
Nhẹ: 3-11 bước 3 λ=1 kết quả; t trùng chỉ số thời gian (4-04,4-10,4-07); Δ ba nghĩa (4-19 vô hướng); ψ_A tọa độ; "mạch" nội bộ & "(chưa có)" trên sơ đồ; CPI, "Fisher–vector"; "trang trước" chỉ đường (4-05/4-23/4-04/4-24/4-07); 4-21 14,7 vs 0,054→14,8 (ghi 0,0536); 1-04 chú thích "cạnh chấm", cột p_A → "p_A sau bước"; 3-06/3-05 p_B có điều kiện A_0=1; 3-09 độ chệch +1 không có phép tính; 4-18 bổ đề dịch chuyển, 6-13 "điều kiện hỗ trợ"; câu khó 2-06,1-09,4-01,2-09; chữ hình 13–15px (2-02? 2-06,4-01,5-05); ngắt dòng 4-20, 5-12, 5-13; 1-06/6-11 câu hỏi không thành danh sách; 2-11 cột "Hệ số" G_0 nhưng số là G_0ψ_A.
## Mạch truyện (xong)
NT: câu hỏi 2 (1-05/1-06/6-11) không nối "dùng lại lượt cũ" — đưa câu "REINFORCE dùng mỗi lượt cho đúng một bước…" lên 1-05, câu 2 thành "dùng lượt của chính sách cũ cho bước cập nhật dài…"; mạch 5 mục đích: 5-01 L^CPI tuyến tính theo ρ nên tới biên, lợi thế sai dấu quyết định hướng, "giảm 0,4 như mạch 1"; 5-05 hộp "phép cắt không sửa lợi thế sai; giới hạn |ρ−1|≤ε" + dòng các bước gradient p_A 0,5→0,4; 5-02 câu nối ρ gần 1 → D_TV nhỏ; thời lượng 135–145 phút.
TB: 4-01 nguồn π̃ (ghi chú diễn giả sai so mạch 1; "đủ xa… hiện rõ" metadiscourse) ; thứ tự mạch 4 đề xuất 4-02→4-14→4-15→4-03→4-11→4-16→4-05; 4-24 câu dẫn cần độ đo; 4-12 lý do KL đưa lên đầu; 4-22 vì sao xấp xỉ, 4-08 g=∇L; 3-01 mở bằng định nghĩa + actor sớm; 3-05 đặt sau 3-02; 5-03/5-06 giả định trái ví dụ; 5-02 hình trước định nghĩa với mẫu bộ đệm; 4-15 π'=(0,6;0,8) không nguồn (đề xuất dùng π̃: 1,5−1,4=0,1 vs −0,5 — cần kiểm); 1-08 NT11 (ol có liên kết); mạch 1 không câu hỏi nhanh; bìa vs 6-11 (đề xuất tác giả).
Nhẹ: 4-09 câu mở; 5-00 "chặn"→"cắt"; vòng trong; CPI; −0,18 bốn lần; 2-08/2-11, 5-08/6-14 lặp; 3-04 critic; 2-00 dòng dẫn; 6-11 nhãn Câu hỏi, "Critic học được"→"Critic sai", câu tự nói; ghi chú diễn giả 6-12/6-15 còn số; 2-07 tiêu đề điện tín; storyboard §9 74 vs 79.
## Chuyên gia RL (xong) — 0 chặn/0 NT; mọi số đúng
TB: bìa khẳng định quá (cùng mạch truyện; đề xuất tác giả); 4-06/6-13 điều kiện hỗ trợ không cần cho dạng tổng (ghi chú tự mâu thuẫn: Định lý 10.26 vs đoạn sau, bảng dòng 2205 → đề xuất ghi chú; deck: chuyển điều kiện sang 4-11); 4-09/5-07 trung bình đều ước lượng g^γ không phải ∇J (Nhận xét 10.17(1), Nota&Thomas 2020) → "Lưu ý:" + tài liệu; Engstrom 2020 dẫn sai ở ghi chú diễn giả 5-06 (theo Nhận xét 10.42(2), 10.50) + dòng dưới 5-08/ghi chú 6-14; thiếu MM Hệ quả 10.29 (J(π_{k+1})≥M_k(π_{k+1})≥M_k(π_k)=J(π_k)) ở 4-21/4-07 + lý do chuyển ràng buộc, D^max vs trung bình; bảng đối chiếu ký hiệu với bài báo (η(π), ρ_π, δ, r_t) — ghi chú dòng 90 → ghi chú diễn giả 6-17 hoặc 1-02.
Nhẹ: "không chặn KL" sắc thái (5-06, 6-15); 6-11 mục 4 "cả hai giới hạn bước" vs PPO không chặn KL; PPO-Penalty một dòng (ghi chú diễn giả 5-07); "(epoch)" 5-07, L^{CLIP+VF+S} ghi chú diễn giả; 4-09 ghi chú diễn giả TRPO gốc Monte Carlo, bước 2,5 từ GAE 2016; 6-17 nơi công bố, phụ đề Engstrom, Kakade 2001 NPG, Cover&Thomas, Nota&Thomas, S&B §13.3; ν^π khối ≤1 trên mặt trang 4-24; 5-02 "mọi ρ_t gần 1" quá mạnh; 6-15 câu 4 trộn hai loại cắt ngắn; thuật ngữ (hiệu hiệu năng, chặn→cận, tỉ số chính sách→tỉ số xác suất theo TB26, clipped surrogate objective, hàm mục tiêu thay thế) → tác giả; ghi chú diễn giả 4-16 "kết quả chính của nửa đầu mạch" metadiscourse.
## Toán (xong) — không số sai giá trị
NT: 2-09 phản ví dụ một bước sai mục đích (A_đều=r−1,5 → gradient vẫn đúng); thay bằng chuỗi: chính sách đều v(s_B)=1,5, q(s_A,1)=1,35, v(s_A)=1,175, A_đều(s_A,·)=(0,175;−0,175), tọa độ θ_A = 0,0875 ≠ 0,2 (điều phối viên kiểm: đúng). Đề xuất ghi chú: phản ví dụ một bước chỉ áp cho (a).
TB: 4-15 π' hai nghĩa → dùng π̃: 1,5−1,4=0,1 vs A_π(s_B,π̃)=−0,5 (v_π̃(s_B)=0,5·3=1,5 ✓); 5-05 s_A là đỉnh gấp tại 0,4 (không đoạn phẳng) → sửa câu + ghi chú diễn giả; 5-03 giả định không xảy ra (ghi rõ giả định/tham số dùng chung).
Nhẹ: 4-25 làm tròn (Δp=(0,0860;0,2137), p=(0,5860;0,8804)); 4-21 0,0536; 4-25 ví dụ dùng g,F chính xác; 1-05 công thức p lên mặt trang, số chưa có trong ghi chú; 4-07 công thức D̄_KL(t) + số chưa có trong ghi chú; 4-12 "p̃_A→1"→"p'_A→1", 2,76 ghi chú diễn giả, E_ν ký hiệu; 4-22 lý do F_B<F_A (ν nhỏ hơn); 4-17 vs 4-06 "chính xác" giả thiết hay điều kiện áp dụng → "Điều kiện áp dụng" như ghi chú; 2-04 H_t; 3-04 critic bảng + α_w trong đề; 3-06/3-05 xác suất khi A_0=1; 5-12/5-13 π' ghi rõ; 4-02 Ý nghĩa thêm số, 5-11 thêm hàng Â=0 + dòng số; ghi chú diễn giả 2-08 "ba cột cuối", 2-04 "bài toán một bước"; 4-09/5-07 câu mở giới hạn phương pháp trước.
## Văn học thuật–sư phạm (xong) — 0 chặn, 6 nghiêm trọng
NT: 2-08/2-11 gọi tích $G_0\psi_A$ là "hệ số" (hệ số đã định nghĩa ở 1-02 là số nhân với $\psi_t$) → "ước lượng"; 3-06 mất điều kiện "từ một lượt bắt đầu bằng hành động 1 ở $s_A$" và câu Đ4 về độ chệch; 2-02 mất câu giải thích ô $-0{,}7$ (góp ý #10); "nơi chính sách tới" ở 4-01, 4-16, 5-13, nhãn hình `chuoi-ti-le-toi-sB*` (TB26) → xác suất thăm, $\eta$, $A_\pi(s,\pi')$; 3-02 "trộn" (#17) và $-0{,}95$ không có phép tính; 5-06/5-03 văn nói và giả định trái ví dụ (#26).
TB: bìa; 1-08 NT11 (ý kiến: `<ol>` có liên kết, bỏ cột danh sách khỏi SVG); 2-00 dòng dẫn; 4-01 câu mở và câu ý đồ; 4-02 "số lần thăm" → số lần thăm có chiết khấu; 4-03 Ý nghĩa cần $\pi'(a\mid s)$; 4-11 câu mở; 4-17 câu mơ hồ; 4-22 câu mở, $F_s$; 2-09; 3-07/3-11 bổ đề lợi thế $n$ bước không phát biểu (TB28); 3-02/3-05 $0{,}4$ trùng hợp; "vòng trong", "đoạn phẳng" chưa định nghĩa (5-02, 5-05, 5-12); 4-25 tìm kiếm lùi; 3-04 critic; 1-04/2-02 tên cột $p_A$; 1-05 $p$ của $\alpha=2$; 6-11 nhãn "Câu hỏi:" và "critic học được"; 5-02 câu mở và hai tên; 4-12/4-24 "kỳ vọng theo $\nu^\pi$" khi khối $0{,}145$. Lớp `dense` (KaTeX 1,1em) là thu nhỏ để vừa khung (NT17) → tác giả duyệt hoặc trả về mặc định; `table.calc .katex 1em` chấp nhận được nếu tác giả duyệt.
Nhẹ: 1-02 nhãn, $\gamma^t$; 1-09 "được đọc qua"; 1-07 mục tiêu 2, 4; 2-01, 5-09 câu hỏi khẩu ngữ, CPI; 2-07 tiêu đề, tên đầy đủ TD; "làm chệch gradient" (3-09, 6-12); 3-06 câu kết; "=" thay "là", câu điều hướng (4-04, 4-10, 4-19, 4-23); "thật" (4-19, 4-25); dấu hai chấm lật bài (5-08, 6-14, 5-10); 4-08, 5-11 thiếu Giả thiết/Kết luận, định nghĩa gradient tự nhiên; 4-15 ba ý; tên tiếng Anh thiếu (bộ đệm, tính chất tháp, lợi tức $n$ bước, số lần thăm có chiết khấu, bán kính cắt, PPO ở 5-00); "tỉ số xác suất" ở ghi chú diễn giả 4-11, "chặn" ở 5-00; câu quy trình trong ghi chú diễn giả (1-07, 1-09, 2-01, 2-11, 3-10, 4-04, 4-16, 4-25, 5-08, 6-10); 6-10 tiêu đề "năm mạch"; 4-09 câu mở.

## B. Quyết định của điều phối viên (giao biên tập viên)

Mỗi mục: `chấp nhận` (sửa), `chấp nhận một phần`, `bác bỏ` (lý do). Mã trang theo deck.

**B1. Câu hỏi 2 và việc dùng lại lượt cũ** (mạch truyện NT) — chấp nhận.
- `1-05`: đưa lên mặt trang câu "REINFORCE dùng mỗi lượt cho đúng một bước, vì sau bước đó lượt đã thuộc chính sách cũ." Dòng gradient đúng chuyển xuống ghi chú diễn giả. Nếu giữ dòng này, ghi đủ $p$ của $\alpha=2$, tức $(0{,}599;0{,}785)$ (vai văn, vai toán).
- `1-06`: câu 2 đổi thành "Làm thế nào để dùng lượt của chính sách cũ cho bước cập nhật dài mà hàm mục tiêu không giảm?". Hai câu tách thành danh sách.
- `6-11`: chép đúng hai câu hỏi của `1-06` dưới nhãn "Câu hỏi:".

**B2. Mạch 5 nêu mục đích trên mặt trang** (mạch truyện NT; vai toán, vai văn, chuyên gia) — chấp nhận.
- `5-01`: nêu hai nguyên nhân trên mặt trang: $\mathcal L^{\mathrm{CPI}}$ tuyến tính theo $\rho$ nên cực đại nằm ở biên, và lợi thế sai dấu quyết định hướng. Thêm "cùng mức giảm $0{,}4$ của bước dài theo một lượt ở mạch 1".
- `5-02`:
  - câu nối: $\rho_t$ gần 1 trên phân bố trạng thái của $\pi_{\mathrm{old}}$ thì $D_{\mathrm{TV}}$ nhỏ, nên sai số của hàm thay thế nhỏ (không viết "mọi $\rho_t$");
  - định nghĩa *đoạn phẳng*;
  - một tên duy nhất "mục tiêu cắt (clipped surrogate objective)";
  - nếu bố cục cho phép, đặt hình trước định nghĩa.
- `5-05`:
  - dòng mở định nghĩa *vòng trong* (bước 3 của thuật toán, $K$ lần qua bộ đệm);
  - sửa câu kết theo vai toán: "vòng trong dừng tại cực đại của phần $s_A$ ($p_A=0{,}4$) và ở đầu đoạn phẳng của phần $s_B$ ($p_B=\tfrac{11}{15}$)". Sửa cả ghi chú diễn giả;
  - đưa lại lý do dừng ở $0{,}4$: dưới $0{,}4$, mẫu $(s_A,2)$ có $\rho>1{,}2$, không bị cắt;
  - hộp: "Phép cắt không sửa lợi thế ước lượng sai; nó giới hạn mỗi vòng ở $\lvert\rho_t-1\rvert\le\epsilon$."
- `5-03`: "Giả sử $p_B\approx0{,}57$ …". Ghi rõ đây là giá trị giả định, không xảy ra trên bộ đệm này vì tham số tách theo trạng thái; với tham số dùng chung, bước trên mẫu khác có thể làm $p_B$ giảm. Bỏ câu "được chọn ở phía bất lợi".
- `5-06`, viết lại theo vai văn và chuyên gia:
  - Nhận xét: trên đoạn phẳng, gradient của mục tiêu cắt theo $\theta_B$ bằng $0$.
  - (1) Không có cận KL: nếu $p_B$ vượt $\tfrac{11}{15}$, mục tiêu không đổi trong khi $D_{\mathrm{KL}}(s_B)$ tăng; phép cắt chỉ bỏ động lực đẩy tỉ số ra ngoài khoảng.
  - (2) Gradient bằng $0$ cả khi tăng $p_B$ làm $J$ tăng: $\partial J/\partial p_B=2{,}7p_A=1{,}08>0$.
  - Bỏ "quán tính của bộ tối ưu".
  - Ghi chú diễn giả về Engstrom 2020 theo Nhận xét 10.42(2) và 10.50 của ghi chú.
- `5-00`: dòng dẫn dùng "cắt", không dùng "chặn".
- `5-07`: thêm "(epoch)". Ghi chú diễn giả thêm hai ý: PPO-Penalty (một câu theo §6.2 ghi chú) và hàm mất mát gộp (9) của PPO 2017.
- `5-11`: thêm hàng $\widehat A_t=0$, thêm dòng "**Giả thiết:**/**Kết luận:**", và một dòng số (mẫu $(s_B,2)$: $-\max(1{,}3;0{,}8)=-1{,}3$).
- `5-12`: chép câu định nghĩa vòng trong của Bài tập 10.23. Ghi "$\pi'$ là chính sách nơi vòng trong dừng".
- `5-13`, ý (d): viết theo $\eta$ và $A_\pi(s_B,\pi')$.
- `5-08`, `6-14`: "không bảo đảm $J$ tăng" (bỏ dấu hai chấm lật bài). Giữ cả hai trang; bác bỏ đề xuất gộp, vì so sánh hai thuật toán ở cuối mạch 5 khác bảng tổng kết bốn phương pháp.

**B3. `2-09` phản ví dụ** (vai toán NT) — chấp nhận.
- Thay câu "bài toán một bước của ghi chú" bằng phản ví dụ trên chuỗi, có đường tính:
  - chính sách đều có $v(s_B)=0{,}5\cdot3=1{,}5$;
  - $q(s_A,1)=0{,}9\cdot1{,}5=1{,}35$;
  - $v(s_A)=\tfrac12(1{,}35+1)=1{,}175$;
  - $A_{\text{đều}}(s_A,\cdot)=(0{,}175;-0{,}175)$;
  - tọa độ $\theta_A$ là $\tfrac12\cdot0{,}175\cdot0{,}5+\tfrac12(-0{,}175)(-0{,}5)=0{,}0875\ne0{,}2$.
- Nếu trang quá dày, chỉ giữ dòng kết quả, phép tính đặt ở ghi chú diễn giả. Điều phối viên đã kiểm các số này.
- Ghi chú diễn giả `2-04`: nói rõ phản ví dụ thuộc bài toán một bước.

**B4. Thuật ngữ và câu tác giả đã chê** (vai văn NT) — chấp nhận.
- `2-08`, `2-11`: tích $G_0\psi_A$ là *ước lượng*, không phải *hệ số*. Tên cột "Ước lượng (tọa độ $\theta_A$)". Hộp: "Ba ước lượng có cùng kỳ vọng $\partial J/\partial\theta_A=0{,}2$. Hai ước lượng sau cần $v_\pi$, mà $v_\pi$ chưa biết khi chỉ có dữ liệu." Tiêu đề 2-08: "Ba ước lượng gradient trên chuỗi hai trạng thái". Sửa câu ghi chú diễn giả "ba cột cuối".
- `3-06`:
  - dòng mở có điều kiện "từ một lượt bắt đầu bằng hành động 1 ở $s_A$; khi đó lượt chỉ còn hai loại, xác suất $p_B$ và $1-p_B$";
  - hàng "độ chệch $=$ kỳ vọng $-\,0{,}4$";
  - "**Lưu ý:** độ chệch là kỳ vọng của ước lượng trừ $A_\pi(s_A,1)$, không phải sai số của một lượt";
  - câu kết thay "cách nhau $2{,}7$" bằng phát biểu về phương sai.
- `3-05`: cột xác suất ghi "khi $A_0=1$".
- `2-02`: đưa lại câu giải thích ô $-0{,}7$ (lượt $s_A\xrightarrow1s_B\xrightarrow2$ nhận hệ số âm vì phần thưởng $0$ ở $s_B$).
- "nơi chính sách tới":
  - `4-01`: xác suất thăm $s_B$: $0{,}5$ dưới $\pi$, $0{,}9$ dưới $\tilde\pi$;
  - `4-16`: theo $\eta_{\tilde\pi}(s_B)=0{,}81>\eta_\pi(s_B)=0{,}45$ và $A_\pi(s_B,\tilde\pi)=-0{,}5<0$;
  - `5-13`(d);
  - nhãn hình `chuoi-ti-le-toi-sB*.svg` "xác suất tới" → "xác suất thăm". Biên tập viên được sửa đúng chuỗi chữ này trong hai SVG.
- `3-02`: bỏ "trộn"; viết hai phép tính $\tfrac12(-0{,}5)+\tfrac12\cdot1{,}3=0{,}4$ và $\tfrac12(-0{,}5)+\tfrac12(-1{,}4)=-0{,}95$, đặt sau định nghĩa. Quy ước $\lambda=1$ viết thành câu riêng.
- `3-05`, hộp: $\lambda$ tăng thì độ chệch giảm, phương sai tăng. Với $\lambda=0{,}5$, kỳ vọng là $-0{,}05$; giá trị $0{,}4$ của lượt (i) chỉ đúng trên lượt đó.
- `1-04`, `2-02`: cột "$p_A$" → "chiều đổi của $p_A$". `1-04`: chú thích "cạnh chấm" rõ nghĩa.
- `4-02`, Ý nghĩa: "số lần thăm có chiết khấu $\eta_{\pi'}(s)$".
- `4-03`, Ý nghĩa: $A_\pi(s,\pi')$ cần thêm $\pi'(a\mid s)$; do đó $\mathcal L$ tính được từ lượt của $\pi$ mà không cần chạy $\pi'$.
- `4-11`: câu mở nói vì sao cần tỉ số. Chuyển điều kiện hỗ trợ $\pi'>0\Rightarrow\pi>0$ về trang này (chuyên gia).
- `4-17`: dòng cuối thành "**Lưu ý:** với lợi thế ước lượng, $\mathcal L_\pi(\pi)=J(\pi)$ có thể sai: …". Xếp "$\eta_\pi$, $A_\pi$ chính xác" thống nhất với ghi chú (điều kiện áp dụng) ở 4-17 và ghi chú diễn giả 4-06.
- `4-22`: câu mở theo vai toán ($s_B$ có trọng số $\nu^\pi(s_B)=0{,}045<\nu^\pi(s_A)=0{,}1$) và thêm câu "bài toán miền tin cậy không giải đúng được; gần $\theta$ thay $\mathcal L$ bằng bậc một, $\bar D_{\mathrm{KL}}$ bằng bậc hai". Định nghĩa phần tử của $F$. `4-08`: "**Giả thiết:**/**Kết luận:**", "$g=\nabla\mathcal L$", định nghĩa gradient tự nhiên.
- `6-11`: mục 2 "Khi critic khác $v_\pi$, sai số TD là ước lượng chệch của lợi thế". Bỏ câu tự nói về văn bản, thay bằng "Ví dụ chung: chuỗi hai trạng thái."; mục 4 tách TRPO và PPO theo chuyên gia.
- Nhẹ (chấp nhận):
  - 1-02: nhãn "Giả thiết", thêm $\gamma^t$, "Lưu ý:" → "Nhắc lại:" nếu hợp;
  - 1-09 "được đọc qua"; 1-07 mục tiêu 2, 4; câu hỏi 2-01, 5-09;
  - CPI có tên đầy đủ ở lần đầu (5-09); 2-07 tiêu đề và tên đầy đủ TD;
  - "làm chệch gradient" → "làm chệch ước lượng gradient";
  - "=" → "là" và câu "trang trước" (nhắc lại công thức tại chỗ);
  - "thật" → "tính trực tiếp" hoặc "tính chính xác"; dấu hai chấm lật bài;
  - tên tiếng Anh thiếu; "tỉ số chính sách" ở ghi chú diễn giả 4-11;
  - câu quy trình trong ghi chú diễn giả; 6-10 tiêu đề bỏ "năm mạch";
  - ghi chú diễn giả 6-12, 6-15 bỏ số (TB32);
  - 4-21 và 4-12 ghi $0{,}0536$; 4-25 làm tròn: $\Delta p=(0{,}0860;0{,}2137)$, $p=(0{,}5860;0{,}8804)$;
  - 4-12 "$p'_A\to1$";
  - 4-24 "Ký hiệu:" thêm $\sum_s\nu^\pi(s)\le1$, $\mathbb E_{\nu^\pi}[f]=\sum_s\nu^\pi(s)f(s)$; 4-12 "tổng có trọng số $\nu^\pi$";
  - 3-09 phép tính độ chệch $+1$; 3-11 Bước 3 viết kết quả $\lambda=1$;
  - ngắt dòng 4-20, 5-12, 5-13; 4-07 công thức $\bar D_{\mathrm{KL}}(t)$;
  - 2-04 định nghĩa $H_t$ và bước $\sum_a\pi\nabla\log\pi=\nabla\sum_a\pi=0$;
  - 4-18 và 6-13 phát biểu một dòng bổ đề dịch chuyển, bỏ "điều kiện hỗ trợ" khỏi cột "không được bỏ" ở 6-13 và khỏi giả thiết 4-06 (đã chuyển sang 4-11).

**B5. Thứ tự và câu dẫn** — chấp nhận một phần.
- Mạch 4 (mạch truyện): chấp nhận thứ tự 4-02 → 4-14 → 4-15 → 4-03 → 4-11 → 4-16 → 4-05.
- `4-15`: phản ví dụ $\mu_0$ dùng $\tilde\pi$: vế trái $v_{\tilde\pi}(s_B)-v_\pi(s_A)=1{,}5-1{,}4=0{,}1$, vế phải $A_\pi(s_B,\tilde\pi)=-0{,}5$; thêm câu kết luận. Bỏ $\pi'=(0{,}6;0{,}8)$.
- `4-01`: câu mở theo vai văn; "Giả sử một bước dài cho chính sách ứng viên $\tilde\theta=(\log9;0)$", bỏ "đủ xa … hiện rõ"; sửa ghi chú diễn giả (không so với bước ở mạch 1).
- `4-24`: câu đầu "Để chặn sai số cho mọi MDP, cần đo khoảng cách giữa $\pi'$ và $\pi$ tại mỗi trạng thái."
- `4-12`: đưa lý do chọn KL lên đầu (KL trơn theo $\theta$; $D_{\mathrm{TV}}$ có $\lvert\cdot\rvert$, không khả vi tại $\pi'=\pi$); 4-07 chỉ giữ câu nối.
- `4-21` hoặc `4-07`: thêm "**Hệ quả.**" theo Hệ quả 10.29 của ghi chú: $J(\pi_{k+1})\ge\mathcal M_k(\pi_{k+1})\ge\mathcal M_k(\pi_k)=J(\pi_k)$, kèm điều kiện đại lượng chính xác. Ghi chú diễn giả 4-07: vì sao chuyển phạt thành ràng buộc ($C$ lớn), $D^{\max}$ của TRPO 2015 và kỳ vọng của Achiam 2017.
- `4-25`: bỏ tên "tìm kiếm lùi, $j=0$", viết "bước $\Delta_0$ thỏa ràng buộc KL và làm hàm thay thế tăng nên được nhận". Thêm một dòng: ví dụ dùng $g$ và $F$ chính xác thay cho trung bình trên bộ đệm.
- `4-09`:
  - câu mở nêu giới hạn của actor–critic;
  - "**Lưu ý:** trung bình đều trên bộ đệm (không có $\gamma^t$) ước lượng $g^\gamma$, khác $\nabla J$" theo Nhận xét 10.17(1);
  - ghi chú diễn giả: TRPO 2015 gốc ước lượng $Q$ bằng Monte Carlo; bước 2 và bước 5 theo GAE 2016.
- `5-07`: câu mở nêu giới hạn của TRPO.
- `3-01`: mở bằng bài toán ($v_\pi$ chưa biết) và sự kiện critic sai trước định nghĩa. Giữ định nghĩa actor ở đây vì 3-04 dùng.
- `3-04`: đề nêu critic dạng bảng $\hat v(s,w)=w_s$, quy tắc $w_s\leftarrow w_s+\alpha_w(\widehat A_t+\hat v(S_t)-w_s)$, $\alpha_w=0{,}5$, và hỏi cả critic mới.
- `3-07`: thêm "**Bổ đề.**" lợi thế $n$ bước $=\sum_{k<n}\gamma^k\delta_{t+k}$ với một dòng "Chứng minh." (TB28).
- `2-00`: dòng dẫn "So lợi tức với giá trị của trạng thái giữ nguyên kỳ vọng của ước lượng gradient và giảm phương sai."
- Mạch 1 thêm một câu hỏi nhanh (TB22) ở `1-05`, lời giải ở fragment: "Lượt $s_A\xrightarrow1s_B\xrightarrow1$ cho $\widehat g=(1{,}35;0{,}9)$; với $\alpha=1$, $J$ bằng bao nhiêu?" Lời giải: $p=(\sigma(1{,}35);\sigma(\log2+0{,}9))=(0{,}794;0{,}831)$, $J=1{,}988$, tức bước dài theo lượt tốt làm $J$ tăng. Điều phối viên đã kiểm. Nếu `1-05` tràn thì đặt ở `1-04`.
- **Bác bỏ:**
  - chuyển `3-05` lên ngay sau `3-02`, vì bảng dùng dạng tổng của mệnh đề ở 3-08;
  - đổi tham số đoạn thẳng $t$ thành $u$, vì nhãn trục trong hình dùng $t$. Thay vào đó ghi rõ "$t\in[0,1]$ là tham số của đoạn thẳng".
- Đổi $\Delta$ vô hướng ở 4-19 thành $d$ (chấp nhận).

**B6. `1-08`** (NT11; vai văn, mạch truyện) — chấp nhận. Bỏ cột danh sách khỏi `so-do-neo-m1.svg`; biên tập viên được sửa riêng tệp này. Đặt `<ol>` sáu mục có `<a href="#/k">`, tên trùng tiêu đề trang mạch. `alt` thêm tên mạch.

**B7. Cỡ chữ** — giữ, chờ tác giả.
- Giữ lớp `dense` (KaTeX 1,1em, tức .88em, vẫn lớn hơn chữ thân bài .8em) và `table.calc` (.752em ≥ .75em). Ghi ngoại lệ ở storyboard §7 với lý do.
- Không tách thêm trang, vì thời lượng đã vượt.
- Tác giả quyết ở bước duyệt.

**B8. Thời lượng** — chấp nhận. Biên tập viên tính lại storyboard §5 sau khi sửa. Bài tập 10.23 (`5-12`/`5-13`) tính vào 30 phút bài tập trên lớp. Ghi con số thật vào §5 và §9 (thống nhất 79 trang đếm hoặc số mới).

**B9. Bác bỏ hoặc ngoài phạm vi.**
- Màn 390 px thu nhỏ cả trang: đây là cách hiển thị chung của mọi deck rl-plan; mỗi trang đều được kiểm tràn ở 390 px.
- Đổi thuật ngữ ("hiệu hiệu năng", "chặn"→"cận", "tỉ số chính sách"→"tỉ số xác suất", "hàm mục tiêu thay thế"): chuyển sang đề xuất cho tác giả (C).
- Gộp `5-08` vào `6-14`: bác bỏ (xem B2).
- Chuyển `4-23` xuống ghi chú diễn giả: bác bỏ, vì góp ý #22 của tác giả cần bước khai triển trên trang.

## C. Đề xuất chờ tác giả
1. Luận điểm bìa (ba vai): bìa hứa "hàm mục tiêu không giảm", trong khi `6-11` kết luận cả TRPO và PPO không bảo đảm điều đó. Hai bản đề xuất:
   - "Giữ chính sách mới gần chính sách cũ để dùng lại lượt đã thu." (17 âm tiết)
   - "Dùng lại lượt đã thu mà vẫn giữ chính sách mới gần chính sách cũ." (16 âm tiết)
2. Ngoại lệ: 79 trang đếm (P6 là 60); thời lượng sau sửa; lớp `dense` (KaTeX 1,1em) và chữ bảng .752em.
3. Ghi chú bài giảng:
   - (a) Định lý 10.26 ghi "điều kiện hỗ trợ" là giả thiết, đoạn sau nói bỏ được, bảng tổng kết (dòng ~2205) lại ghi là giả thiết. Đề xuất chuyển điều kiện này sang dạng tỉ số.
   - (b) Thêm phản ví dụ chính sách đều trên chuỗi ($0{,}0875\ne0{,}2$) sau Mệnh đề 10.5.
   - (c) Thêm các số mặt trang dùng mà ghi chú chưa có: $p=(0{,}550;0{,}730)$, $J=1{,}53$, $1{,}67$ (bước theo gradient đúng); $(0{,}706;0{,}581)$, $0{,}0155$ ($t=0{,}515$); $J=1{,}988$ (câu hỏi nhanh mạch 1).
4. Thuật ngữ:
   - "bổ đề hiệu hiệu năng" → "bổ đề chênh lệch hiệu năng"?
   - "chặn cải thiện" → "cận cải thiện"?
   - "tỉ số chính sách" (ghi chú) hay "tỉ số xác suất" (TB26)?
   - "hàm thay thế" → "hàm mục tiêu thay thế"?
5. Đối chiếu ký hiệu với các bài báo ($\eta(\pi)$, $\rho_\pi$, $\delta$, $r_t$) đưa vào ghi chú diễn giả `6-17`; tài liệu tham khảo bổ sung nơi công bố và các nguồn deck dùng (Kakade 2001, Cover & Thomas 2006, Nota & Thomas 2020). Biên tập viên làm ngay vì đã có trong ghi chú.

## D. Kiểm lại sau lượt sửa (bản `90ee7201`)

**Mạch truyện (xong):** 0 chặn, 2 nghiêm trọng.
- `1-12` cắt mạch tới "Vấn đề trung tâm" (TB20). Câu kết "J tăng" làm yếu vấn đề. Câu hỏi đòi tính σ (TB22). Đề xuất: chuyển lên giữa `1-04` và `1-05`, hỏi dự đoán dấu; đưa câu "cùng độ dài bước, $J$ tăng hay giảm tùy lượt" lên mặt trang.
- Hộp `5-05` "giới hạn mỗi vòng ở $\lvert\rho_t-1\rvert\le\epsilon$" nói quá, mâu thuẫn `5-06`. Lỗi do câu nguyên văn của điều phối viên ở B2; sửa thành "chỉ bỏ phần tăng của mục tiêu khi $\rho_t$ ra ngoài khoảng theo hướng có lợi".
- Trung bình:
  - `6-11`: câu trả lời chưa khớp câu hỏi 2 (từ lượt cũ; PPO dùng lại bộ đệm $K$ lần; "không bảo đảm $J$ không giảm"; "lượt đầy đủ").
  - `5-11`: dòng số dùng $\rho=1{,}3$ trước `5-03` → dùng $(s_A,1)$, $\rho=1$: $-1{,}4$.
  - `5-05`: "bước 3 của thuật toán, $K$" trước thuật toán → định nghĩa tại chỗ.
  - `1-05`: hộp hai câu nối với giới hạn $0{,}4$.
  - Thời lượng ước khoảng 145–155 phút, không phải 118,5; bài tập 10.23 khoảng 10–12 phút.
- Nhẹ:
  - ghi chú diễn giả `1-06` "hai trang vừa xem", `4-05` "ở trang sau";
  - `4-16` thêm dòng điều còn thiếu;
  - `4-12` câu bài toán (khả vi để tối ưu theo $\theta$), bỏ lặp;
  - `4-24` một dòng Trực quan;
  - `4-13` giới thiệu $\pi'$;
  - `4-25` "được nhận" và vị trí dòng $g$, $F$ chính xác;
  - `5-01` tiêu đề;
  - `6-11` danh sách, dòng ví dụ chung ra ngoài hộp;
  - `1-08` `#/1` dẫn tới bìa (chấp nhận, ghi §7);
  - ghi chú diễn giả `2-08` "chưa phải critic", `5-06` "quán tính của Adam", `6-15` "lực kéo về";
  - storyboard §1, §3, §5 đồng bộ.

**Toán (xong):** 0 chặn, 1 nghiêm trọng (hộp `5-05`, trùng mạch truyện).
- Trung bình:
  - ghi chú diễn giả `4-19` "$d p_A=0$" → "$\Delta p_A=0$";
  - `4-25`: $\sigma(0{,}35)=0{,}5866\ne0{,}5860$. Ghi $\Delta_0=0{,}04344\cdot(8;30)=(0{,}3475;\,1{,}3031)$, rồi $p=(0{,}5860;\,0{,}8804)$; điều phối viên đã kiểm.
- Nhẹ:
  - `4-12`, `4-20`: ghi $D_{\mathrm{KL}}(s_B)\approx0{,}0566$;
  - `4-09`: "tỉ lệ với $g^\gamma$". `4-25`: ghi rõ trung bình trên bộ đệm ước lượng $g^\gamma=(0{,}2;\,0{,}333)$ trên chuỗi;
  - `4-21`: một dòng "Chứng minh.";
  - `4-15`: "$J(\tilde\pi)-J(\pi)$" thay $\Delta J$ trước định nghĩa;
  - `3-07`: điều kiện $\delta_k=0$ khi $k\ge T$ và hai hệ số trong dòng chứng minh;
  - `4-22`: "không có nghiệm dạng đóng", "chủ yếu vì $\nu^\pi$";
  - `4-14`: $r(s,a)=\mathbb E[R_{t+1}\mid s,a]$;
  - ghi chú diễn giả: `4-20` $p'_A$, `2-02` tên cột, `6-17` $h$;
  - `4-02` Ý nghĩa thêm số (chưa sửa từ lượt trước).

**Văn học thuật (xong):** 0 chặn, 3 nghiêm trọng, 19 trung bình, khoảng 25 nhẹ. Sáu mục nghiêm trọng của lượt trước: 4 đã sửa xong, 2 sửa một phần (2-02, 5-06/5-03).
- Nghiêm trọng:
  - `1-02` "hệ số" có $\gamma^t$, trái các trang sau và ghi chú;
  - hộp `5-05`;
  - `6-11` chưa thành danh sách, các kết luận chưa gắn với từng câu hỏi.

## E. Quyết định lượt sửa thứ hai (giao biên tập viên)

Các câu đề xuất dưới đây là ý; biên tập viên viết lại bằng `no-ai-slop` Edit, giữ đúng số.

**E1. Nghiêm trọng**
- `5-05`, hộp: thay câu của B2 bằng: "Phép cắt không sửa lợi thế ước lượng sai. Trên bộ đệm này, vòng trong dừng khi $\lvert\rho_t-1\rvert=\epsilon$ ở cả ba mẫu, $\rho=(0{,}8;\,1{,}2;\,0{,}8)$." Không viết rằng phép cắt giữ tỉ số trong khoảng.
- `1-12`:
  - chuyển lên giữa `1-04` và `1-05`;
  - câu hỏi đổi thành dự đoán dấu: "$J$ tăng hay giảm?", để số $\sigma$ trong lời giải;
  - tiêu đề gọi tên lượt ($s_A\xrightarrow1s_B\xrightarrow1$), không dùng "lượt tốt";
  - tách dấu ";" của dòng Nhắc lại thành hai câu.
- `1-05`, hộp:
  - nối với `1-12`: cùng $\alpha$, chiều đổi của $J$ phụ thuộc lượt đã thu; ở giới hạn $J$ giảm $0{,}4$;
  - câu về REINFORCE viết theo vai văn: $\widehat g$ không chệch chỉ khi lượt sinh bởi chính sách đang cập nhật, nên REINFORCE dùng mỗi lượt cho đúng một bước;
  - sửa câu ghi chú diễn giả `1-06` "hai trang vừa xem" cho khớp.
- `1-02`: "Số nhân với $\gamma^t\psi_t$ là *hệ số* của bước $t$; ở REINFORCE hệ số là $G_t$". Bỏ hai dấu hai chấm liền nhau ở dòng Giả thiết. Kiểm mọi chỗ dùng "hệ số" trong deck khớp nghĩa này; `3-10` dùng "lợi thế GAE $\widehat A_t$".
- `6-11`:
  - khung "Câu hỏi:" là `<ol>` hai câu như `1-06`;
  - dưới khung, "Trả lời câu 1:" gồm mục 1, 2, và "Trả lời câu 2:" gồm mục 3, 4;
  - mục 2 thêm "trên lượt đầy đủ" và viết "$\hat v=v_\pi$";
  - mục 3 thêm "tính được từ lượt của chính sách cũ"; "tiếp xúc $J$" thay "khớp đến bậc một";
  - mục 4 thêm "PPO dùng lại bộ đệm $K$ lần" và viết "không bảo đảm $J$ không giảm";
  - "Ví dụ chung: chuỗi hai trạng thái." là dòng riêng, đặt ngoài khung.

**E2. Toán**
- Ghi chú diễn giả `4-19`: "$\Delta p_A=0$".
- `4-25`: ghi $\Delta_0=0{,}04344\cdot(8;30)=(0{,}3475;\,1{,}3031)$, rồi $p=(\sigma(0{,}3475);\,\sigma(\log2+1{,}3031))=(0{,}5860;\,0{,}8804)$ (điều phối viên đã kiểm). Giữ các số KL $0{,}0085$, $\Delta\mathcal L=0{,}357$, $J=1{,}807$. Dòng "ví dụ dùng $g=\nabla\mathcal L$ và $F$ theo $\nu^\pi$; trung bình trên bộ đệm ước lượng $g^\gamma$, trên chuỗi là $(0{,}2;\,0{,}333)$" đặt ở đầu trang. Viết "thỏa ràng buộc KL và làm hàm thay thế tăng", không viết "được nhận".
- `4-12`, `4-20`: $D_{\mathrm{KL}}(s_B)\approx0{,}0566$. Bỏ câu lặp "không phải trung bình trên các mẫu của một bộ đệm" ở `4-12`. Mở `4-12` bằng câu bài toán: để tối ưu hàm thay thế theo $\theta$ với ràng buộc khoảng cách, khoảng cách cần khả vi theo $\theta$.
- `4-09`, Lưu ý: "tỉ lệ với $g^\gamma$".
- `4-21`: thêm dòng "Chứng minh." (bất đẳng thức đầu theo định lý chặn cải thiện; bất đẳng thức thứ hai vì $\pi_{k+1}$ cực đại $\mathcal M_k$; đẳng thức cuối vì $\mathcal L_{\pi_k}(\pi_k)=J(\pi_k)$ và $D_{\mathrm{TV}}=0$). Viết "như định lý chặn cải thiện".
- `4-15`: hàng tổng ghi "$J(\tilde\pi)-J(\pi)$".
- `3-07`: thêm điều kiện $\delta_k=0$ khi $k\ge T$; sửa hai hệ số trong dòng chứng minh: "$-\gamma^{k+1}\hat v(S_{t+k+1})$ của $\gamma^k\delta_{t+k}$".
- `4-22`: "không có nghiệm dạng đóng"; "chủ yếu vì $\nu^\pi(s_B)=0{,}045<0{,}1$".
- `4-14`: thêm $r(s,a)=\mathbb E[R_{t+1}\mid s,a]$.
- Ghi chú diễn giả: `4-20` viết $p'_A\to1$; `2-02` dùng tên cột mới; `6-17` ghi rõ $h$ là ký hiệu của ghi chú.

**E3. Mạch truyện và văn (trung bình)**
- `5-01`, tiêu đề: "Hàm thay thế mẫu tuyến tính theo tỉ số nên cực đại nằm ở biên", hoặc câu tương đương ≤ một dòng.
- `5-05`: dòng mở định nghĩa *vòng trong* tại chỗ (nhiều bước gradient tăng $\mathcal L^{\mathrm{CLIP}}$ trên cùng bộ đệm, lợi thế giữ cố định), không dẫn tới bước 3 hay $K$. `5-07` gọi lại tên này.
- `5-11`: dòng số dùng mẫu $(s_A,1)$ với $\rho=1$: $-1{,}4\max(1;\,0{,}8)=-1{,}4$.
- `5-03`: "Trên bộ đệm này $p_B$ không giảm: mỗi trạng thái có tham số riêng, và mẫu duy nhất tại $s_B$ có $\widehat A<0$ nên chỉ đẩy $p_B$ tăng."
- `5-06`: "Trên bộ đệm hai lượt, với $p_A=0{,}4$:". Mục 1: phép cắt chỉ đặt gradient của số hạng bằng $0$ khi tỉ số ra ngoài khoảng theo hướng làm số hạng tăng; bỏ "động lực đẩy". Ghi chú diễn giả: "động lượng (momentum) của Adam" thay "quán tính", bỏ "lực kéo về".
- `5-02`: định nghĩa một lần "hướng có lợi: hướng làm $\rho_t\widehat A_t$ tăng".
- `2-09`: định nghĩa chính sách đều $\bar\pi=(\tfrac12;\tfrac12)$ và $\bar A$ trên mặt trang.
- `2-02`: câu về ô $-0{,}7$: $G_0=0<v_\pi(s_A)=1{,}4$ do phần thưởng $0$ ở $s_B$, nên ước lượng giảm $p_A$ dù $q_\pi(s_A,1)=1{,}8>1{,}4$. Gọi tên "mệnh đề đường cơ sở"; bỏ dấu hai chấm lật bài.
- `4-02`, Ý nghĩa: "$J(\pi')-J(\pi)$ là tổng của lợi thế $A_\pi(s,\pi')$ theo trọng số $\eta_{\pi'}(s)$". Ký hiệu: "*số lần thăm có chiết khấu*", kèm tên tiếng Anh như ghi chú. Nếu còn chỗ, thêm một dòng số từ `4-15`.
- `4-16`:
  - tiêu đề không dùng "thực tế", ví dụ "Hàm thay thế dự báo $J$ tăng $0{,}095$ khi $J$ giảm $0{,}085$";
  - dòng cuối nêu điều còn thiếu: sai số $\Delta J-\Delta\mathcal L$ phụ thuộc thế nào vào khoảng cách giữa $\pi'$ và $\pi$;
  - bỏ dấu hai chấm lật bài.
- `4-17`, Lưu ý: gọi tên $-0{,}45$ là ước lượng của $A_\pi(s_A,\pi)$, khác giá trị đúng $0$. "Ý nghĩa:" đặt ở đầu dòng riêng.
- `4-13`: Nhắc lại "$\pi'$ là chính sách mới bất kỳ; $\tilde\pi$ là một trường hợp".
- `4-24`: một dòng "Trực quan:" (TV đo lượng xác suất phải dời) trước định nghĩa.
- `4-19`, `4-07`: bỏ dấu hai chấm lật bài, "lỏng" → "không chặt", bỏ chữ "nó".
- `6-15`, câu 4: "Một môi trường dừng mỗi lượt sau $H$ bước, nên nhiều lượt kết thúc trước trạng thái kết thúc. Với critic sai, …". Câu 2: dùng "số lần thăm có chiết khấu $\eta_{\pi'}$ khác $\eta_\pi$".
- Hình, chỉ sửa chữ, giữ bố cục; kiểm XML và độ rộng chữ:
  - "giá trị thật" → "$\Delta J$ tính trực tiếp" (hoặc "tính trực tiếp") trong `ham-thay-the-tiep-xuc*.svg` và `ham-thay-the-mien-tin-cay*.svg`, kèm `alt`;
  - nhãn nhỏ ở `1-06` "bước dài làm J giảm" → "bước dài theo một lượt làm J giảm";
  - chú thích "cạnh chấm" ở `reinforce-truc-so*.svg` cho rõ nghĩa (số cạnh chấm là xác suất của lượt).
- `1-08`: `alt` ghi tên các mạch. PPO ở lần đầu (mục 5 của `<ol>` và `5-00`) kèm "Proximal Policy Optimization".
- Thời lượng: ghi cả hai ước lượng vào §5 (biên tập viên 118,5; vai mạch truyện 145–155, mạch 4 khoảng 50). Bài tập 10.23 khoảng 10–12 phút. Ghi là ngoại lệ chờ tác giả. Đồng bộ §1, §3, §5 với deck.

**E4. Nhẹ** (làm nếu không làm trang tràn)
- 1-07 "mức độ";
- 2-07 tên tiếng Anh TD;
- 3-01 "Giả sử";
- 3-02 câu GAE;
- 3-05, 4-19 tách dấu chấm phẩy;
- 3-06 cột "Xác suất khi $A_0=1$", "có kỳ vọng sai dấu";
- 3-10 "Ước lượng REINFORCE có phương sai lớn";
- ghi chú diễn giả 4-01 "nó";
- 4-04 tách câu mở;
- tên tiếng Anh của "điều kiện hỗ trợ" và "bổ đề dịch chuyển" (4-11, 4-18), nếu không có trong ghi chú thì bỏ qua;
- 5-07 tách mục 3 thành hai dòng con;
- 5-09 thứ tự tên CPI theo VP3, "tích $Fv$ của ma trận Fisher với một vectơ";
- 5-12 "tại đó", và câu "Bộ đệm chứa các cặp $(s,a)$ với tần suất hành động bằng $\pi(a\mid s)$";
- "thật" trong ghi chú diễn giả 4-06, 4-08, 4-09, 4-25, 5-13;
- câu quy trình trong ghi chú diễn giả ("Câu hỏi kiểm…" ở 1-12, 2-03, 3-04, 4-10, 5-03; 4-23 "Đây là phép kiểm…"; 2-08 "chưa phải critic"; 4-05 "ở trang sau");
- storyboard §1 dòng dẫn.

**Bác bỏ:**
- Chuyển `4-21` về sau `4-19`, vì không còn chỗ và đã ghi là ngoại lệ.
- Đổi "tỉ số chính sách", vì việc này chờ tác giả (C4).

## F. Kiểm lại lượt hai (bản `114690b1`)

**Toán (xong):** 0 chặn, 0 nghiêm trọng, không có số sai giá trị.
- Trung bình, cả hai ở `4-25`:
  - Câu "trung bình trên bộ đệm ước lượng $g^\gamma$, trên chuỗi là $(0{,}2;0{,}333)$" thiếu thừa số $1/\mathbb E[T]$, mà $\mathbb E[T]=1{,}5$. Câu này lấy từ đề xuất của điều phối viên ở E2. Viết lại thành "tỉ lệ với $g^\gamma$" và chuyển sang Lưu ý của `4-09`.
  - "tìm kiếm lùi", $j$ và $g^\gamma$ dùng trước `4-09`. Sửa thành "…nên được giữ nguyên"; dòng đầu chỉ ghi "Ví dụ dùng $g=\nabla\mathcal L$ và $F$ theo $\nu^\pi$, tính chính xác."
- Nhẹ:
  - ghi chú diễn giả `1-12`: "cùng bước học $\alpha=1$";
  - `3-07`/`3-08`: "$\delta_j=0$ khi $j\ge T$, $\hat v(S_T)=0$";
  - `6-18`: thừa số $2\gamma\chi_{\pi'}/(1-\gamma)^2$;
  - ghi chú diễn giả `4-21`: $2\cdot0{,}5\cdot90=90$;
  - `4-02`: $\eta_{\tilde\pi}(s_B)=\gamma\tilde p_A=0{,}81$;
  - `6-15` câu 4: lượt bị cắt ngắn, không phải kết thúc của MDP, và GAE bootstrap từ $\hat v$;
  - `<title>` của `gae-tinh-lui*.svg`: "lợi thế GAE".

**Mạch truyện và văn (xong):** 0 chặn, 2 nghiêm trọng.
- Tiêu đề `1-05`, nhãn hình nhỏ và `alt` ở `1-06` khái quát quá, trái với `1-12`.
- `4-25` dùng "tìm kiếm lùi", $j$, $g^\gamma$ trước `4-09` (trùng phát hiện của vai toán).
- Trung bình:
  - `1-12`: lời giải nêu lý do của dấu; câu hỏi có đường tính $\widehat g=(2{,}7\cdot0{,}5;\,0{,}9\cdot3\cdot\tfrac13)$;
  - hộp `1-05` nối tới "lượt của chính sách cũ";
  - `6-11`/`6-18`: số câu trả lời trùng số câu hỏi (dùng `<ul>`); mục 1 thiếu phương sai; mục 3 thiếu điều kiện;
  - `6-15`: bỏ "trả lời và nêu kết quả đã dùng". Câu này thuộc NT-RL-9 cũ, đã bị thay ở §6 của `NGUYEN-TAC-HOC-PHAN.md`;
  - `5-03`: thứ tự lập luận;
  - `4-02`: số $0{,}81$ chưa có đường tính;
  - `4-12`: câu "phạt nặng" không có số chứng minh.
- Nhẹ: 5-05 (câu dừng, hộp), 5-06 mục 1, 5-01, 5-02, 6-18 (phủ định kép, dòng cuối), 4-24, 4-13, 4-12, 4-16, 4-17, 4-04, 2-02, 2-09, nhãn "số cạnh chấm", các câu điều hướng trong ghi chú diễn giả, ghi chú diễn giả 1-06/6-11/3-10, 5-00/5-07 (tên PPO), đồng bộ storyboard §3, §5, §7.

## G. Quyết định lượt sửa thứ ba (giao biên tập viên)

Chấp nhận mọi phát hiện của mục F, cả toán lẫn mạch truyện và văn. Biên tập viên dùng các câu thay thế đề xuất trong báo cáo, đã chép lại dưới đây. Điều phối viên đã kiểm các số:
- `1-12`: $2{,}7\cdot0{,}5=1{,}35$; $0{,}9\cdot3\cdot\tfrac13=0{,}9$; $\partial J/\partial p_A=2{,}7p_B-1>0$ khi $p_B\ge\tfrac23$.
- `2-09`: $\bar v=(1{,}175;\,1{,}5)$.
- `4-02`: $\eta_{\tilde\pi}=(1;\,\gamma\tilde p_A)=(1;\,0{,}81)$.

**G1. Nghiêm trọng**
- `1-05`:
  - Tiêu đề: "Bước dài theo lượt $s_A\xrightarrow2$ làm $J$ giảm".
  - Nhãn hình nhỏ ở `1-06` và `alt` theo cùng ý: "bước dài theo lượt s_A → 2 làm J giảm".
  - Hộp: cùng $\alpha$, chiều đổi của $J$ phụ thuộc lượt đã thu. Với lượt $s_A\xrightarrow2$, $J$ giảm $0{,}4$ khi $\alpha\to\infty$. Sau một bước, lượt đã thu là lượt của chính sách cũ và $\widehat g$ tính từ nó không còn không chệch, nên REINFORCE dùng mỗi lượt cho đúng một bước.
- `4-25`:
  - Dòng 1: "Ví dụ dùng $g=\nabla\mathcal L$ và $F$ tính chính xác theo $\nu^\pi$."
  - Câu cuối: "Bước $\Delta_0$ thỏa ràng buộc KL và làm hàm thay thế tăng, nên giữ nguyên." Không nhắc tìm kiếm lùi, $j$ hay $g^\gamma$.
  - Chuyển ý $g^\gamma$ thành câu thứ hai của "Lưu ý:" ở `4-09`: "trung bình trên bộ đệm tỉ lệ với $g^\gamma$; trên chuỗi $g^\gamma=(0{,}2;\,0{,}333)$, khác $\nabla J=(0{,}2;\,0{,}3)$." Không viết rằng trung bình bằng $g^\gamma$.

**G2. Trung bình**
- `1-12`:
  - Câu hỏi có đường tính $\widehat g=(G_0\psi_A;\,\gamma G_1\psi_B)=(2{,}7\cdot0{,}5;\,0{,}9\cdot3\cdot\tfrac13)=(1{,}35;\,0{,}9)$.
  - Lời giải nêu lý do: cả hai tọa độ dương nên $p_A$, $p_B$ cùng tăng; $J$ tăng theo $p_B$, và tăng theo $p_A$ khi $2{,}7p_B>1$. Sau đó kiểm bằng số.
  - Ghi chú diễn giả: "cùng $\alpha=1$" thay "cùng độ dài bước".
- `6-11`/`6-18`:
  - Câu trả lời dùng `<ul>`.
  - Mục 1 thêm "trên ví dụ chung phương sai giảm".
  - Mục 3 viết theo đề xuất: khi lợi thế và số lần thăm tính chính xác, $J$ không giảm nếu mức tăng của hàm thay thế vượt phạt tỉ lệ với kỳ vọng khoảng cách TV, hoặc với căn của KL trung bình.
  - Thừa số $2\gamma\chi_{\pi'}/(1-\gamma)^2$ nếu còn ghi.
  - Mục 4: "Với lợi thế ước lượng, cả hai đều có thể làm $J$ giảm."
  - Dòng cuối: "Ví dụ chung của bài là chuỗi hai trạng thái."
- `6-15`: khung chỉ ghi "Câu hỏi:". Câu 4: lượt bị cắt ngắn vì giới hạn thời gian, không phải kết thúc của MDP; GAE bootstrap từ $\hat v$ ở bước cắt.
- `5-03`: đổi thứ tự lập luận theo đề xuất: mẫu → $p_B$ không giảm trên bộ đệm này → trường hợp tham số dùng chung → giả sử $\rho=1{,}3$.
- `4-02`: dòng số thêm $\eta_{\tilde\pi}=(1;\,\gamma\tilde p_A)=(1;\,0{,}81)$ và "$=J(\tilde\pi)-J(\pi)$".
- `4-12`: "KL tăng không giới hạn khi chính sách mới gần bỏ một hành động, còn $D_{\mathrm{TV}}\le1$." Câu tỉ số $0{,}2$ và số của $p'_A=0{,}99$ để ở ghi chú diễn giả. Đoạn mở viết đủ tên phân kỳ Kullback–Leibler trước chữ "KL". Công thức kết thúc bằng dấu chấm.

**G3. Nhẹ** (theo bảng của hai vai)
- 5-05:
  - câu dừng "Tại điểm dừng, cả ba tỉ số nằm ở biên khoảng cắt với $\epsilon=0{,}2$, $\rho=(0{,}8;1{,}2;0{,}8)$";
  - hộp "…, nên $J$ vẫn giảm".
- 5-06 mục 1: có chủ ngữ, dùng "hướng có lợi".
- 5-01 câu cực đại và "theo lượt $s_A\xrightarrow2$". 5-02 "phần tăng của $\rho_t\widehat A_t$".
- 4-24 bỏ "TV" trước định nghĩa. 4-13 dòng "Ký hiệu:" riêng.
- 4-16 tiêu đề "…, còn $J$ giảm $0{,}085$". 4-17 điều kiện chính xác chuyển vào Giả thiết. 4-04 tách dấu chấm phẩy.
- 2-02 "Với đường cơ sở khác $v_\pi$…" và ghi chú "hành động 2". 2-09 thêm đường tính $\bar v$.
- 3-07/3-08 "$\delta_j=0$ khi $j\ge T$, $\hat v(S_T)=0$".
- Ghi chú diễn giả `4-21`: $2\cdot0{,}5\cdot90$.
- Nhãn `1-04` "số ghi cạnh mỗi chấm là xác suất của lượt", sửa trong SVG `reinforce-truc-so*` (chỉ sửa chữ). `<title>` của `gae-tinh-lui*.svg`: "lợi thế GAE".
- Ghi chú diễn giả: bỏ câu điều hướng ở 1-10, 2-01, 3-07, 3-08, 4-06, 1-12; `1-06` "Câu trả lời theo mạch:"; `6-11` có điều kiện; `3-10` câu stop-gradient.
- 5-00 và 5-07: không lặp tên tiếng Anh của PPO, viết theo VP3.
- Storyboard: §3 câu 2 của `1-06` theo deck; §5 đánh dấu đoạn cũ là lịch sử; §7 thêm hàng `1-08` `#/1` dẫn tới bìa (chấp nhận).
