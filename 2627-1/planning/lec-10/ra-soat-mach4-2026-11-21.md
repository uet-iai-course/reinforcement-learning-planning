# Năm vai rà mạch 4 sau đề xuất TRPO (bản `6f238a48`, 2026-11-21): phát hiện và quyết định

## A. Phát hiện theo vai (tóm tắt)
## Sinh viên (xong)
NT: 4-17 Lưu ý −0,45: tổng Σ η Â = −0,45 + 0,45·1 = 0 trên chuỗi → ví dụ không chứng tỏ L≠J; thay bằng gradient: ∇L̂ = (−0,025; 0,3) ≠ ∇J = (0,2; 0,3) (điều phối viên đã kiểm). 4-07: ν^π tổng 0,145 gọi "phân bố", "kỳ vọng"; KL trung bình 0,0536 < cả hai thành phần → ghi rõ tổng có trọng số.
TB: 4-07 t=0,515/κ không đường tính (thêm "giải D̄(t)=0,01", hai KL 0,0930, 0,0155); 4-21 hệ quả trước định lý, sơ đồ gọi tên kết quả chưa phát biểu, D̄_KL(π‖π'); lý do KL thay TV (TV có |·| không khả vi, KL có Hessian F, Pinsker giữ cận) ở 4-12 hoặc 4-22; 4-30/4-08 lý do bằng lời: ν(s_B)=0,045 nhỏ → đổi θ_B tốn ít KL, nối 4-25 KL s_B 0,156 vs s_A 0,015; 4-17 chứng minh thiếu ψ(s,2)=−p_s e_s, đường tính ∇J; 4-29 χ̄ thay χ lý do (|A(s,π')|≤max_a|A|), kiểm "mọi bước làm M_k giảm" (d: 1,35d vs 16,2d; e: 0,8e vs 36e); 4-25 Δ0/giữ nguyên dựa vào tìm kiếm lùi, "0,8Δp_A" chưa viết ra (0,8=A(s_A,1)−A(s_A,2)); 4-26 g^γ tên ngược nghĩa, mục đích, ví dụ lý tưởng; 390px (giới hạn học phần – bác).
Nhẹ: 4-01 nguồn θ̃, nhãn t của chấm; 4-27/4-13 "phần thưởng 1", (hành động 1; hành động 2); 4-04 đường tính 0,0125 (0,095²/0,72); 4-10 cột "|ΔJ−ΔL|=0,18t²"; 4-12 "từ t=0,25 tới π̃"; 4-14 đường tính 0,1/−0,5; "giả thiết chung" nhắc một lần ở 4-02; 4-16 "nơi … tới"; 4-31 chấm xanh nhãn "bước nhận".
GHI CHÚ dòng 1163 (sau Mệnh đề 10.22) cùng lỗi: "−0,45≠0 và L(θold)≠J(θold)" sai kết luận (tổng có trọng số = 0). Sửa: tổng theo η bằng 0 nên giá trị vẫn khớp trên chuỗi, nhưng gradient lệch: ∇L̂ = (1·¼·(−0,5+0,4); 0,45·(2/9)·3) = (−0,025; 0,3) ≠ ∇J = (0,2; 0,3). Giao người viết ghi chú (giữ trần số từ).
## Mạch truyện (xong) — 0 chặn
NT: thời lượng ~50 phút (46–56), deck 132–140; rút ở cụm lý thuyết trước (§5 #1 4-29, #2 4-19 gộp 4-06, #3 4-14) — chờ tác giả.
TB: 4-01 dòng Nhắc lại 1-05 vẫn gợi lý do sai → thay bằng câu nối 3-10 ("Mạch 2–3 cho hướng ít phương sai, nhưng mỗi lượt chỉ cho một bước. Dùng lại lượt đã thu cho bước dài hơn thì phải biết đi bao xa."); 4-01 nguồn π̃ ("không theo hướng gradient, p_B giảm") + lý do đánh giá trước khi chạy (J cần mô hình); 4-27 đưa câu "dữ liệu cũ đánh giá thấp vai trò s_B" lên hộp; 4-13 câu dẫn tách theo trạng thái; 4-16 thêm điều còn thiếu / 4-04 tiêu đề khẳng định "Sai số của hàm thay thế tăng theo bình phương độ dài bước" (bỏ "từ…tới"); 4-12 câu nghĩa "KL trơn theo θ và nhạy với thay đổi lớn, nên TRPO ràng buộc KL"; có thể chuyển Ký hiệu ν^π, D̄ về 4-12; 4-21 hệ quả trước định lý (nhãn/chú dẫn) + nửa dương (phạt ∝ √D̄ → 0 khi κ→0); vào cụm lý thuyết: chuyển 4-14 xuống trước 4-06 hoặc Nhắc lại bổ đề; H10 thu nhỏ tô mắt xích ở 4-20/4-24/4-06 (tùy); 4-22 mở bằng Nhắc lại bài toán + ∇L=∇J; 4-31 tiêu đề "Hàm thay thế, miền tin cậy và gradient tự nhiên", câu thông điệp lên mặt trang.
Nhẹ: H14 miền tin cậy vẽ tròn (nên elip); 4-16 đẳng thức sai số hiện sau lời giải; ghi chú diễn giả 4-16 metadiscourse, 4-31 "không chỉ là"; storyboard ghi lệch Taylor→hình học.
## Chuyên gia (xong) — 0 chặn, mọi số đúng
NT: so sánh ngầm g vs gradient tự nhiên không trung thực: bước theo g cùng bán kính bậc hai → (0,649;0,973), KL thật 0,0093, ΔL thật 0,361 (NG 0,357), J 1,835 (NG 1,807) [điều phối viên kiểm: 1,8347]; NG chỉ thắng trên mô hình tuyến tính g^TΔ 0,460 vs 0,422. Sửa: Lưu ý ở 4-25 (mặt trang): bước theo g cho J≈1,835; NG tối ưu bài toán xấp xỉ, không tối ưu J; ghi chú 4-08 sửa; câu hỏi 4-30 trả lời bằng lý do thật (κ đo trên hành vi, bất biến với cách tham số hóa); 4-31 "hướng tốt nhất của bài toán xấp xỉ bậc một–bậc hai".
TB: 4-08 cách đọc 21/79: (F^{-1}g)_s = (A(s,1)−A(s,2))/(1−γ) = 0,8/0,1=8 và 3/0,1=30; tần suất thăm và độ dốc sigmoid triệt tiêu; lý do "s_B ít được thăm" sai → "gradient thường bị thu nhỏ tại s_B vì ν nhỏ; NG bỏ thừa số đó, để lại chênh lệch lợi thế 0,8 và 3" (Kakade 2001 Đl 1). GHI CHÚ dòng 1716 cùng lỗi. 4-21/4-29: nguồn cận kỳ vọng (Achiam 2017 Hệ quả 1, 3); TRPO 2015 dùng D^max, hằng 4γχ̄/(1−γ)², KL trung bình là kinh nghiệm (ghi chú diễn giả + mặt 4-29). 4-07: khối 0,145, κ=0,01 ≈ 0,07 thang chuẩn hóa (ghi chú diễn giả); trang tham khảo "κ là δ (bài báo dùng trung bình mẫu)".
Nhẹ: 4-29 MM phạt tuyến tính TV đứng yên, phạt bình phương KL bước nhỏ ≠0; "(minorize–maximize, MM)"; 4-31/4-00 "dự báo còn đáng tin" → "sai số của dự báo bị chặn theo KL"; 4-12 chiều KL "(chiều cũ‖mới, như TRPO)"; 4-20 ghi chú phản ví dụ TV nhỏ KL ∞: π=(1−ε;ε), π'=(1;0); 4-09 ghi chú nguồn bước 5 "cài đặt thông dụng"; 4-09 Â_T → cuối bộ đệm; 4-04 ghi chú CPI hỗn hợp, phạt 90t² vs 0,18t²; tên tiếng Anh: số lần thăm có chiết khấu (discounted visitation frequency), bổ đề dịch chuyển; ghi chú diễn giả 4-16, 4-31 slop; 5-09 sơ đồ thiếu nhánh "không j nào: giữ θ_old" (tùy).
## Văn học thuật (xong)
NT: 4-16 "nơi π̃ tới thường hơn và kém π" (TB26) → dùng η và A; ghi chú diễn giả theo. 4-21 hình chuoi-bon-mat-xich khối 2 "TV nhỏ tại mỗi trạng thái" SAI toán: KL trung bình ≤κ chỉ cho TV kỳ vọng E_ν[D_TV] ≤ √(κ/2) (Pinsker + Jensen) → nhãn khối 2 "TV kỳ vọng nhỏ", mũi tên "Pinsker và Jensen", alt theo; kiểm ghi chú §4.5 đoạn ba mắt xích cùng lỗi? 4-01 hai thông điệp (tiêu đề đánh giá, hộp độ dài bước), nguồn θ̃, câu Nhắc lại → kết hợp đề xuất mạch truyện.
TB: 4-01 câu hỏi khẩu ngữ "chạy"; cụm lý thuyết không có dấu hiệu → tiền tố tiêu đề "Cơ sở lý thuyết: …" (VP7) hoặc H10 thu nhỏ; 4-14 dòng Nhắc lại phát biểu bổ đề, δ_t công thức, dòng cuối "Lưu ý: bổ đề cần cùng μ0…"; 4-21 dòng mở câu hỏi, nhãn hệ quả nêu gốc, "số hạng phạt"; 4-06 Nhắc lại hệ quả ở dòng chứng minh; 4-03 dòng mở, Ý nghĩa dùng η ("mức thay đổi" chứ không "mức tăng"); 4-02 hình ba-thanh-phan nhãn "tần suất gặp" → "số lần thăm có chiết khấu", "chưa có lượt của π'"; ghi chú diễn giả phủ nhận thuật ngữ; thêm Ý nghĩa; 4-16/4-10 "thực tế/tần suất" → ΔJ tính trực tiếp/η (hình dong-gop nhãn); 4-27 dòng mở, tỉ lệ 0,5→0,9, câu học có giám sát; 4-24 trực quan khẩu ngữ, "tại mọi trạng thái" sai với kỳ vọng; vế trái viết (1−γ)|η−η|; 4-12 "từ t=0,25 tới π̃", Nhận xét KL +∞, không đối xứng; 4-07 dòng mở, κ trên trang, D_KL(s_B) đường tính, t=0,515 "nghiệm của D̄(π_t)=0,01"; 4-28 dòng mở, tiêu đề "…mức thay đổi phân phối hành động"; 4-08 "Ký hiệu:" gradient tự nhiên trước mệnh đề, hộp O(d²)/O(d³) (cần nguồn ghi chú? chỉ nếu ghi chú có); 4-22 dòng mở tách câu; 5-09 "Ứng viên" đổi, L^CPI = L̂ của TRPO; 4-04 tiêu đề khẳng định, "khoảng cách 0,18t²".
Nhẹ: 4-10 cột |ΔJ−ΔL|, lời giải; 4-20 "Ý tưởng chứng minh." thay "Chứng minh." nếu là phác thảo, dòng mở; 4-24 "tích lũy"; 4-06 chứng minh tách dòng có nhãn; 4-29 "đứng yên", χ̄ nguồn, dòng mở; 4-25 θ_old, KL từng trạng thái; 4-09 "cực đại hóa", bước 1 có động từ, "(buffer)" lần đầu; 4-26 Lưu ý sau bước 5 (mâu thuẫn quyết định trước: Lưu ý ngay sau bước 3 — giữ sau bước 3? TB31 liệt kê không đứt → chuyển sau bước 5 nhưng ghi "g ở bước 3"); 4-31 tiêu đề; 4-19 tiêu đề "…đúng nhưng lỏng"; 4-11 câu nối 0,32/−0,5, ghi chú "tỉ số chính sách"; tên tiếng Anh (action distribution, state distribution, discounted visitation frequency); ghi chú diễn giả "Câu hỏi gợi cho lớp" → "Câu hỏi: … Lời giải: …"; metadiscourse 4-16, 4-10, 4-03, 4-12; khẩu ngữ ghi chú 4-00, 4-01, 4-27, 4-13, 4-28.
## Toán (xong) — 1 nghiêm trọng (trùng sinh viên)
NT: `4-17` Lưu ý $-0{,}45$ và ghi chú dòng 1163: tổng $\sum_s\eta_\pi\,\widehat A(s,\pi)=0$ trên chuỗi; gradient lệch $(-0{,}025;0{,}3)$.
TB: hình chuỗi bốn mắt xích khối 2 (trùng văn); `4-25` $\Delta p_A$, $0{,}8\Delta p_A$, $3\Delta p_B$ chưa dựng trên mặt trang (đưa lên `4-04`); `4-19` $d$ trùng số chiều → $\Delta p_B$; `4-29` $\pi$ làm biến chính sách mới → $\pi'$, thêm $\chi_{\pi'}\le\bar\chi_k$; `4-26` "xấp xỉ tỉ lệ", $g^\gamma$ vào NT3; §10 NT3 thiếu số của `4-04`, `4-07`, `4-17`, `4-21`.
Nhẹ: `4-07` "khoảng 41", $\kappa$ ghi trong chữ mảnh 2, đường tính $0{,}0566$; `4-25` hệ số $0{,}043437$; `4-28` $\lVert\Delta\theta\rVert_2$; `4-09` cuối bộ đệm, $k_{\max}$; `4-30` $\Delta\theta_B/\Delta\theta_A$; ghi chú diễn giả `4-07` dạng (14) "với bán kính quy đổi"; `4-14` quy ước $v_\pi(S_T)=0$; `4-21` nhãn hệ quả nêu gốc.

## B. Quyết định của điều phối viên

**B1. Ghi chú bài giảng** (người viết ghi chú, chạy trước biên tập viên deck; giữ văn xuôi ≤ 32 500 từ):
1. Dòng ~1163 (sau Mệnh đề 10.22): với critic $(1{,}4;1)$, $\lambda=0$, tổng $\sum_s\eta_\pi(s)\sum_a\pi\widehat A=1\cdot(-0{,}45)+0{,}45\cdot1=0$ nên giá trị vẫn khớp trên chuỗi; gradient lệch: $\nabla\widehat{\mathcal L}=(1\cdot\tfrac14(-0{,}5+0{,}4);\,0{,}45\cdot\tfrac29\cdot3)=(-0{,}025;\,0{,}3)\ne\nabla J=(0{,}2;0{,}3)$ (số $-0{,}025$ đã có ở §3).
2. Dòng ~1716 (5.1): lý do dồn bước về $\theta_B$ là $(F^{-1}g)_s=\bigl(A_\pi(s,1)-A_\pi(s,2)\bigr)/(1-\gamma)$, tức $8$ và $30$; gradient thường bị thu nhỏ tại $s_B$ vì $\nu^\pi(s_B)$ nhỏ, gradient tự nhiên bỏ thừa số này (Kakade 2001). Bỏ câu "chủ yếu vì $s_B$ ít được thăm".
3. 5.1, một câu trung thực: bước theo $g$ co về cùng bán kính bậc hai cho $J\approx1{,}835$, KL thật $0{,}0093$; gradient tự nhiên tối ưu bài toán xấp xỉ, không tối ưu $J$; ưu điểm của nó là độ dài bước đo trên phân phối hành động, không phụ thuộc cách tham số hóa.
4. §4.5 mắt xích 2: "TV kỳ vọng theo $\nu^\pi$ nhỏ" (Pinsker theo trạng thái cộng Jensen).
5. Dòng ~1277 (dạng (14)): thêm "với bán kính quy đổi theo khối $\nu^\pi(\mathcal S)$".

**B2. Deck** (biên tập viên, sau B1):
- Nghiêm trọng:
  - `4-17` Lưu ý theo B1.1 (gradient lệch);
  - `4-25` thêm "Lưu ý:" về bước theo $g$ ($J\approx1{,}835$) và B1.3; `4-08` lý do theo B1.2, câu trả lời "vì sao TRPO ưu tiên $\theta_B$" bằng chênh lệch lợi thế; `4-30` câu hỏi trả lời bằng tính bất biến; `4-31` "hướng tốt nhất của bài toán xấp xỉ bậc một–bậc hai";
  - hình `chuoi-bon-mat-xich*` khối 2 "TV kỳ vọng theo $\nu^\pi$ nhỏ", mũi tên "Pinsker và Jensen", `alt` và `<desc>` theo (chỉ sửa chữ SVG);
  - `4-16` câu sai số viết theo $\eta$ và $A_\pi$, bỏ "nơi … tới"; ghi chú diễn giả theo; nhãn hình `dong-gop-tung-trang-thai*` "$\Delta\mathcal L$: số lần thăm $\eta_\pi$", "$\Delta J$: số lần thăm $\eta_{\tilde\pi}$" (chỉ sửa chữ);
  - `4-01`: một thông điệp. Tiêu đề nêu ý chính (gợi ý "Hướng làm $J$ tăng chưa cho biết độ dài bước"); dòng mở nối `3-10` (mỗi lượt chỉ cho một bước; dùng lại lượt cho bước dài cần biết đi bao xa), bỏ dòng "Nhắc lại" về `1-05`; nguồn $\tilde\pi$: "một ứng viên không theo hướng gradient ($p_B$ giảm)"; câu hỏi: "tính $J(\pi_t)-J(\pi)$ thế nào chỉ từ lượt của $\pi$, khi chưa có lượt nào của $\pi_t$?", kèm lý do (công thức $J$ cần mô hình).
- Trung bình:
  - **Cụm lý thuyết:** tiền tố tiêu đề "Cơ sở lý thuyết: …" cho `4-14`, `4-20`, `4-24`, `4-06`, `4-19`, `4-29`; `4-14` thêm dòng "Nhắc lại:" phát biểu bổ đề, $\delta_t$ có công thức, dòng cuối "Lưu ý: bổ đề cần cùng $\mu_0$ …" có đường tính; `4-22` mở bằng "Nhắc lại:" bài toán miền tin cậy và $\nabla\mathcal L=\nabla J$.
  - **`4-21`:** dòng mở câu hỏi; nhãn "Hệ quả (của định lý chặn cải thiện và bất đẳng thức Pinsker; …)"; câu nửa dương (phạt tỉ lệ $\sqrt{\bar D_{\mathrm{KL}}}$, về $0$ khi $\kappa\to0$); "số hạng phạt"; ghi chú diễn giả nguồn Achiam (2017, Hệ quả 1, 3).
  - **`4-29`:** $\pi'$ thay $\pi$; $\chi_{\pi'}\le\bar\chi_k$; $\bar\chi=\lvert A_\pi(s_B,2)\rvert=2$; một dòng: TRPO 2015 chứng minh với $D^{\max}$, KL trung bình là xấp xỉ kinh nghiệm; "(minorize–maximize, MM)"; bỏ "đứng yên".
  - **`4-12`:** câu nghĩa "KL trơn theo $\theta$ (TV chứa $\lvert\cdot\rvert$, không khả vi tại $\pi'=\pi$), nên TRPO ràng buộc KL; Pinsker giữ cận"; "từ $t=0{,}25$ tới $\tilde\pi$"; chiều KL "(chiều cũ‖mới, như TRPO)".
  - **`4-07`:**
    - dòng mở nêu bài toán;
    - $\kappa=0{,}01$ trong chữ;
    - đường tính $D_{\mathrm{KL}}(s_B)=0{,}0566$;
    - $t=0{,}515$ là nghiệm của $\bar D_{\mathrm{KL}}(\pi_t)=0{,}01$;
    - ghi rõ $\sum_s\nu^\pi=0{,}145\le1$ nên $\bar D_{\mathrm{KL}}$ là tổng có trọng số (nhỏ hơn từng thành phần);
    - "khoảng 41";
    - ghi chú diễn giả: thang $\kappa$ so với trung bình chuẩn hóa.
  - **`4-27`:** dòng mở; câu "dữ liệu của $\pi$ đánh giá thấp vai trò của $s_B$" lên hộp; tỉ lệ $0{,}5\to0{,}9$.
  - **`4-13`:** câu dẫn tách theo trạng thái.
  - **`4-02`:** nhãn hình `ba-thanh-phan*` "số lần thăm có chiết khấu", "chưa có lượt của $\pi'$"; thêm "Ý nghĩa:".
  - **`4-03`:** dòng mở và Ý nghĩa theo $\eta$ ("mức thay đổi").
  - **`4-04`:** tiêu đề khẳng định về sai số $-0{,}18t^2$; dựng $\Delta p_s$, $A_\pi(s_A,\pi')=0{,}8\Delta p_A$, $A_\pi(s_B,\pi')=3\Delta p_B$ trên mặt trang; đường tính $0{,}0125$.
  - **`4-16`:** thêm câu điều còn thiếu; đẳng thức sai số hiện cùng hoặc sau lời giải.
  - **`4-10`:** cột $\lvert\Delta J-\Delta\mathcal L\rvert$; câu hỏi dùng $\Delta\mathcal L$, $\Delta J$.
  - **`4-24`:** trực quan theo kỳ vọng; vế trái $(1-\gamma)\lvert\eta_{\tilde\pi}(s_B)-\eta_\pi(s_B)\rvert$.
  - **`4-19`:** $\Delta p_B$ thay $d$; tiêu đề "…đúng nhưng lỏng".
  - **`4-25`:** $\theta_{\mathrm{old}}$; KL từng trạng thái; hệ số $0{,}043437$.
  - **`4-26`:** "xấp xỉ tỉ lệ".
  - **`4-28`:** dòng mở; $\lVert\Delta\theta\rVert_2$; tiêu đề "… mức thay đổi phân phối hành động".
  - **`4-08`:** "Ký hiệu:" gradient tự nhiên trước mệnh đề.
  - **`5-09`:** không dùng "ứng viên"; nói $\mathcal L^{\mathrm{CPI}}$ là $\widehat{\mathcal L}$ của TRPO.
  - **`4-31`:** tiêu đề "Hàm thay thế, miền tin cậy và gradient tự nhiên"; câu thông điệp lên mặt trang; "nơi sai số của dự báo bị chặn theo KL".
- Nhẹ: theo bảng của các vai (ghi chú diễn giả: "Câu hỏi gợi cho lớp" → "Câu hỏi: … Lời giải: …", bỏ câu metadiscourse và "không chỉ là"; tên tiếng Anh: action distribution, state distribution, discounted visitation frequency; `4-20` "Ý tưởng chứng minh." nếu là phác thảo; `4-06` chứng minh tách dòng có nhãn; `4-09` "cực đại hóa", cuối bộ đệm, $k_{\max}$; `4-30` $\Delta\theta$; `4-14` quy ước $v_\pi(S_T)=0$; `4-11` câu nối, ghi chú "tỉ số chính sách"; `4-31` chấm xanh "bước nhận" nếu là chữ SVG).
- Storyboard §10: bổ sung NT3 ($g^\gamma$, số của `4-04`, `4-07`, `4-17`, `4-21`, bước theo $g$ $1{,}835$ nếu ghi chú chưa có), ghi lệch Taylor trước hình học (cần $F$ trước elip).

**B3. Bác bỏ:**
- Màn 390 px (cách hiển thị chung của deck rl-plan).
- Chuyển "Lưu ý:" của `4-26` xuống sau bước 5 (quyết định trước: đặt ngay sau bước 3 cho gần đối tượng).
- `4-08` số $O(d^2)/O(d^3)$ (ghi chú không có; viết "tốn bộ nhớ và phép tính khi $d$ lớn").
- Vẽ lại miền tròn của H14 thành elip (biểu tượng, giữ).
- H10 thu nhỏ trong cụm lý thuyết (đã có tiền tố tiêu đề).

**B4. Chờ tác giả:** thời lượng mạch 4: storyboard 37,5 phút; cổng khoảng 47,5; mạch truyện khoảng 50 (46–56); cả bài khoảng 132–140 phút. Phương án rút ở cụm lý thuyết (storyboard §5).

## C. Kiểm lại sau B2 (bản `09e40ae9`)

0 chặn, 0 nghiêm trọng, mọi số đúng. Mục B2 nghiêm trọng và trung bình: đạt. Bảy phát hiện trung bình mới và một lỗi trình bày số; quyết định (biên tập viên, lượt C):
1. **`4-08`:** câu "thành phần $s_B$ bị nhân với $\nu^\pi(s_B)$" viết lại: $g_s=F_{ss}(F^{-1}g)_s$ với $F_{ss}=(0{,}025;\,0{,}01)$, thừa số nhỏ hơn chủ yếu do $\nu^\pi(s_B)=0{,}045<0{,}1$; gradient tự nhiên chia cho $F_{ss}$. Viết "$0{,}8/0{,}1=8$ và $3/0{,}1=30$". Ghi chú diễn giả theo. Ghi chú bài giảng dòng ~1714 do người viết ghi chú sửa trước.
2. **`4-07`:** đưa lại "hàm mục tiêu bằng $(1-\gamma)\Delta\mathcal L$" lên mặt trang; lấy chỗ bằng cách bỏ ", không phải trung bình mẫu". Nếu tràn thì báo.
3. **`4-17`:** Lưu ý không dùng ký hiệu $\widehat{\mathcal L}$ ("thì gradient thành …").
4. **`4-12`:** vế Pinsker viết "KL nhỏ kéo theo TV nhỏ (bất đẳng thức Pinsker)", hoặc đưa xuống ghi chú diễn giả.
5. **`4-01`:** hai câu nén viết lại: "Muốn dùng lại lượt đã thu cho một bước dài hơn thì phải biết đi bao xa." và "Theo mô hình của môi trường, $J=2{,}7p_Ap_B+1-p_A$, nên".
6. **`5-09`:** "Hàm thay thế mẫu $\widehat{\mathcal L}$ ở bước 3 của TRPO được ký hiệu là $\mathcal L^{\mathrm{CPI}}$, theo tên phương pháp lặp chính sách bảo thủ (…):".
7. **`4-25`:** Lưu ý giữ hai câu đầu; câu về tính bất biến với cách tham số hóa đã có ở ghi chú diễn giả `4-30`, bỏ khỏi `4-25` (TB13).
8. **Khẩu ngữ:** ghi chú diễn giả `4-01`, `4-11`, `4-24`, `4-27`, `4-28`, `4-08` và mặt trang `4-07` theo bảng của vai kiểm. `<title>` `dong-gop*` "mức thay đổi thực tế" đổi thành "tính trực tiếp".

Đính chính B3: số $O(d^2)/O(d^3)$ có trong ghi chú dòng ~1727 (Schulman 2015, Phụ lục C); giữ ở ghi chú diễn giả `4-08` là đúng.
