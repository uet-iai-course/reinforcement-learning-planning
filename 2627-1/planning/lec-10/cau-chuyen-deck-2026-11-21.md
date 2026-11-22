# Câu chuyện của deck Bài 10 (dựng lại sau góp ý của tác giả), 2026-11-21

Bước 1 của quy trình dựng deck (`NGUYEN-TAC-HOC-PHAN.md` §3a.E), viết lại sau lượt duyệt của tác giả. Thay câu chuyện `cau-chuyen-deck-2026-11-20.md` (bản đó còn hành lang, DPO và bảy mạch).

Căn cứ:

- góp ý của tác giả `gop-y-tac-gia-deck-2026-11-20.md` (#1–#28, Trao đổi 1–29) và bản tổng hợp `tong-hop-gop-y-2026-11-21.md` (nhóm lỗi A–H, TB24–TB33, quyết định mục 3 và 3a, danh sách thay đổi mục 4.2);
- quy tắc TB1–TB33 (`NGUYEN-TAC-HOC-PHAN.md` §3a), NT1–NT29 phần không bị thay, VP1–VP25;
- ghi chú `materials/lec-10/lecture-note.md` đang được sửa song song (bỏ §7 DPO, dẫn $J(p)$ của hành lang, "trung bình" → "kỳ vọng", mạch 4 theo bước $(0{,}9;\,0{,}5)$). Khối của ghi chú được dẫn bằng số hiệu và tiêu đề.

Mọi con số dưới đây được tính lại bằng `/tmp/claude-1000/-data-tqlong-lectures/678a7f48-9d80-46cf-a421-67398857f913/scratchpad/deck10-v2/kiem_so.py`.

**Quyết định đã chốt** (không bàn lại; thêm 2026-11-21: luận điểm bìa "Dùng lại lượt đã thu cho những bước cập nhật chính sách lớn mà hàm mục tiêu không giảm." (thay ngày 2026-11-22, quyết định #6 của tác giả, bằng "Kiểm soát mức đổi chính sách để giảm nguy cơ suy giảm khi dùng lại lượt đã thu.", 18 âm tiết), 74 trang đếm và 120 phút là ngoại lệ P6, tinh chỉnh Đ1–Đ13 của `NGUYEN-TAC-HOC-PHAN.md` §3a.F áp cho storyboard): bỏ DPO; tên bài "TRPO và PPO"; sáu mạch đánh số; một ví dụ chung là chuỗi hai trạng thái với một tham số mỗi trạng thái, $p_s=\sigma(\theta_s)$, chính sách cũ $\theta=(0;\,\log2)$, tức $(p_A;\,p_B)=(\tfrac12;\,\tfrac23)$; chính sách ứng viên của mạch 4 là $\tilde\theta=(\log9;\,0)$, tức $\tilde\pi=(0{,}9;\,0{,}5)$ (ký hiệu theo ghi chú: phát biểu tổng quát dùng $\pi'$, chính sách cụ thể của ví dụ dùng $\tilde\pi$; $\pi'=(0{,}6;\,0{,}8)$ của Ví dụ 10.11 không lên trang); bài tập tổng hợp PPO-Clip ở cuối mạch 5; tổng kết định tính.

---

## 1. Câu chuyện của bài

1. Trên chuỗi hai trạng thái, ước lượng REINFORCE của một lượt có kỳ vọng bằng tọa độ gradient $0{,}2$ nhưng phương sai $0{,}69$; với xác suất $\tfrac12$ nó ngược dấu gradient, và một bước dài theo ước lượng đó làm $J$ giảm từ $1{,}4$ về gần $1$.
2. Trừ khỏi lợi tức một đường cơ sở chỉ phụ thuộc trạng thái không làm chệch ước lượng gradient; với đường cơ sở $v_\pi$, hệ số có kỳ vọng có điều kiện bằng lợi thế, phương sai giảm còn $0{,}20$, và sai số TD với $v_\pi$ đúng cho phương sai $0$.
3. Hàm giá trị phải học từ dữ liệu nên có sai số; khi đó ước lượng lợi thế một bước bị chệch ($-0{,}5$ thay cho $0{,}4$) còn ước lượng cả lượt có phương sai lớn ($1{,}62$), và GAE tổ hợp các ước lượng nhiều bước bằng tham số $\lambda$ để cân bằng hai đại lượng.
4. Bổ đề chênh lệch hiệu năng cho thấy đánh giá chính sách mới cần phân bố trạng thái của chính nó; hàm thay thế dùng phân bố của chính sách cũ, khớp $J$ đến bậc một, nhưng với bước tới $(0{,}9;\,0{,}5)$ nó dự báo $J$ tăng $0{,}095$ trong khi $J$ giảm $0{,}085$, nên TRPO tối đa hàm thay thế trong một miền KL trung bình nhỏ.
5. PPO thay ràng buộc KL bằng phép cắt đóng góp của từng mẫu và dùng lại một bộ đệm nhiều lần chỉ với gradient bậc một: trên một bộ đệm hai lượt có lợi thế ước lượng sai dấu, trong ví dụ này phép cắt giữ mức giảm của $J$ ở $0{,}008$ thay cho $0{,}4$, nhưng không chặn KL và không bảo đảm $J$ tăng.

Mạch tổng kết gọi tên ví dụ chung (chuỗi hai trạng thái) mà không nhắc số (Đ13). Câu hỏi trung tâm (trang "Vấn đề trung tâm" của mạch 1): (1) làm thế nào để ước lượng gradient chính sách có phương sai nhỏ mà kỳ vọng không đổi; (2) làm thế nào để dùng lại dữ liệu từ chính sách cũ cho các bước cập nhật hiệu quả, đồng thời kiểm soát nguy cơ suy giảm hiệu năng (bản #8, câu chuẩn của tác giả; trước đó "… cho bước cập nhật dài mà vẫn kiểm soát nguy cơ hàm mục tiêu giảm", và trước nữa "… mà hàm mục tiêu không giảm"). Câu 2–3 trả lời phần (1), câu 4–5 trả lời phần (2).

---

## 2. Câu chuyện của từng mạch

Khuôn mỗi mạch (TB1, TB27): bài toán → trực quan → công cụ → kết quả trên ví dụ → điều còn thiếu. Mạch sau mở bằng điều mạch trước còn thiếu.

### Mạch 1. Giới hạn của REINFORCE (mạch mở đầu, không có trang tiêu đề mạch)

1. Bài toán: REINFORCE cho một ước lượng không chệch của gradient từ mỗi lượt, nhưng chưa rõ một ước lượng như vậy tốt đến đâu trên một lượt cụ thể.
2. Trực quan: chuỗi hai trạng thái được dựng một lần, bằng lời và hình, với tham số $\theta=(\theta_A;\,\theta_B)$, chính sách $p_s=\sigma(\theta_s)$ và $\theta=(0;\,\log2)$; ba loại lượt cho $J=2{,}7p_Ap_B+1-p_A=1{,}4$ và gradient $(0{,}2;\,0{,}3)$.
3. Kết quả trên ví dụ (vấn đề 1): ba loại lượt cho tọa độ $\theta_A$ của ước lượng là $1{,}35$; $0$; $-0{,}5$ với xác suất $\tfrac13$, $\tfrac16$, $\tfrac12$; kỳ vọng $0{,}2$, phương sai $0{,}6925$, và với xác suất $\tfrac12$ ước lượng ngược dấu gradient.
4. Kết quả trên ví dụ (vấn đề 2): bước $\theta\leftarrow\theta+\alpha\widehat g$ theo ước lượng của lượt chọn hành động 2 ở $s_A$ cho $J=1{,}30$ với $\alpha=1$, $J\approx1{,}22$ với $\alpha=2$, và $J\to1$ khi $\alpha\to\infty$.
5. Điều còn thiếu: một ước lượng có phương sai nhỏ hơn mà kỳ vọng giữ nguyên, và một cách chọn bước dài mà $J$ không giảm; đó là hai câu hỏi trung tâm.

### Mạch 2. Đường cơ sở và hàm lợi thế

1. Bài toán: trên chuỗi mọi lợi tức không âm, nên REINFORCE tăng xác suất của mọi hành động đã chọn, kể cả hành động 2 ở $s_A$ với $q_\pi(s_A,2)=1<q_\pi(s_A,1)=1{,}8$.
2. Trực quan: lợi tức từ $s_A$ nhận ba giá trị $0$; $1$; $2{,}7$, có kỳ vọng $v_\pi(s_A)=1{,}4$; hiệu $G_0-1{,}4$ cho biết lượt tốt hơn hay kém hơn mức kỳ vọng.
3. Công cụ: đường cơ sở chỉ phụ thuộc trạng thái không làm chệch ước lượng gradient (mệnh đề, có chứng minh); với $b=v_\pi$, kỳ vọng có điều kiện của hệ số là hàm lợi thế, nên gradient có dạng lợi thế (hệ quả, có ý tưởng chứng minh).
4. Kết quả trên ví dụ: ba hệ số $G_0$, $G_0-v_\pi(S_0)$ và sai số TD $\delta_0$ với $v_\pi$ đúng có cùng kỳ vọng $0{,}2$, phương sai $0{,}6925$; $0{,}2025$; $0$.
5. Điều còn thiếu: $v_\pi$ chưa biết, nên các hệ số này chưa tính được từ dữ liệu.

### Mạch 3. Ước lượng lợi thế: độ chệch và phương sai

1. Bài toán: $v_\pi$ được thay bằng một hàm giá trị học từ dữ liệu (critic), và critic có sai số; với critic $\hat v=(1{,}4;\,1)$, đánh giá thấp $s_B$, cần ước lượng $A_\pi(s_A,1)=0{,}4$.
2. Trực quan: ước lượng một bước $\delta_0$ cho $-0{,}5$ ở mọi lượt (chệch $-0{,}9$, phương sai $0$); ước lượng cả lượt $G_0-\hat v(s_A)$ cho $1{,}3$ hoặc $-1{,}4$ (không chệch, phương sai $1{,}62$).
3. Công cụ: lợi thế $n$ bước và GAE, tổ hợp có trọng số $(1-\lambda)\lambda^{n-1}$, bằng tổng $(\gamma\lambda)^k\delta_{t+k}$ và tính lùi được; GAE không làm chệch gradient khi $\lambda=1$ hoặc critic đúng.
4. Kết quả trên ví dụ: với $\lambda=0{,}5$, kỳ vọng $-0{,}05$, độ chệch $-0{,}45$, phương sai $0{,}405$; tổng quát, độ chệch $-0{,}9(1-\lambda)$ và phương sai $1{,}62\lambda^2$. Thuật toán actor–critic với GAE ghép các bước này.
5. Điều còn thiếu: mọi ước lượng của mạch 2–3 cần lượt của chính sách đang cập nhật, nên mỗi lượt chỉ cho một bước nhỏ.

### Mạch 4. Hàm thay thế và miền tin cậy (TRPO)

Bản theo đề xuất trình bày TRPO của tác giả (`de-xuat-trinh-bay-trpo-2026-11-21.md`), điều phối viên duyệt 2026-11-21; câu 4–5 sửa ngày 2026-11-22 theo nhận xét website (#6, `nhan-xet-website-trpo-2026-11-21.md`); storyboard §3 mạch 4. Bản trước ở mục lịch sử cuối tệp; câu 4–5 của bản 2026-11-21 chép ở cuối mục này.

1. Hiện tượng và câu hỏi: mỗi lượt của mạch trước chỉ cho một bước, và bước dài theo ước lượng của một lượt cũ làm $J$ giảm. Trên đoạn từ $\pi$ tới ứng viên $\tilde\pi=(0{,}9;\,0{,}5)$, $J(\pi_t)=1{,}4+0{,}095t-0{,}18t^2$: hướng này làm $J$ tăng lúc đầu, nhưng $J$ về $1{,}4$ tại $t=\tfrac{19}{36}$ và xuống $1{,}315$ tại $t=1$. Biết hướng làm $J$ tăng chưa cho biết đi bao xa. $\tilde\pi$ đổi cả hành động tại $s_B$ lẫn tần suất tới $s_B$ (trong $100$ lượt, từ $50$ lên $90$), và $J(\tilde\pi)$ chỉ biết sau khi chạy nó. Đánh giá chính sách mới từ lượt của $\pi$ thế nào, và tin được đến đâu?
2. Mô hình: mức thay đổi của $J$ là lợi thế của $\pi$ cộng theo tần suất gặp trạng thái dưới chính sách mới, $1\cdot0{,}32+0{,}81\cdot(-0{,}5)=-0{,}085$ (bổ đề chênh lệch hiệu năng). Hàm thay thế thay tần suất mới bằng tần suất cũ và hiệu chỉnh hành động bằng tỉ số chính sách, nên tính được từ lượt cũ.
3. Kết quả trên ví dụ: hàm thay thế dự báo $+0{,}095$ trong khi $J$ giảm $0{,}085$, toàn bộ sai số nằm ở $s_B$. Trên đoạn từ $\pi$ tới $\tilde\pi$, dự báo tăng như $0{,}095t$ còn sai số tăng như $0{,}18t^2$; hàm thay thế tiếp xúc $J$ tại $\pi$ nên là mô hình cục bộ.
4. Giới hạn thay đổi: cùng bước tham số đổi hành vi rất khác nhau ($\Delta p=0{,}2311$ so với $0{,}0042$), nên khoảng cách đo trên phân phối hành động bằng KL. Bài toán miền tin cậy tối đa hàm thay thế với KL trung bình $\le\kappa$; trên đoạn, $\kappa=0{,}01$ giữ $t\le0{,}515$, nơi $\Delta J>0$. KL nhỏ kéo theo TV nhỏ, phân bố chiếm dụng ít đổi và sai số nhỏ, nhưng cận lỏng: với $\tilde\pi$, phạt $14{,}7$ lớn hơn nhiều mức tăng dự báo $0{,}095$. Bài toán thay phạt bằng ràng buộc, nên giới hạn mức đổi mà không tự bảo đảm $J$ tăng.
5. Giải và thuật toán: TRPO dự báo bằng hàm thay thế, giới hạn mức đổi bằng KL trung bình, rồi tối ưu trong miền tin cậy. Bậc một cho hàm thay thế, bậc hai cho KL, miền thành một elip của ma trận Fisher; bước tối ưu đi theo gradient tự nhiên $F^{-1}g=(8;\,30)$ và đưa $J$ từ $1{,}4$ lên $1{,}807$, thấp hơn $1{,}835$ của bước theo $g$, vì gradient tự nhiên chỉ tối ưu bài toán xấp xỉ. Thuật toán áp $\kappa$ lên KL trung bình trên bộ đệm ($\approx0{,}36$ với $\tilde\pi$), khác KL trung bình có chiết khấu ($0{,}0536$). Điều còn thiếu: mỗi bộ đệm chỉ cho một bước, với gradient liên hợp và tìm kiếm lùi.

Phụ lục (2026-11-22; tên từ bản #8: "Phụ lục: cơ sở lý thuyết của TRPO và PPO"; không thuộc mạch 4, ngoài 120 phút, sau tài liệu tham khảo; phần PPO ở cuối mục mạch 5): các chứng minh nối giới hạn KL của bài toán miền tin cậy với sai số của hàm thay thế, theo thứ tự mắt xích (bổ đề chênh lệch hiệu năng, Pinsker, dịch chuyển phân bố chiếm dụng, định lý chặn cải thiện, ví dụ cận trên chuỗi, cải thiện đơn điệu); storyboard §3, mục "Phụ lục".

*Câu 4–5 bản 2026-11-21 (đã thay):*

> 4. Giới hạn thay đổi: cùng bước tham số đổi hành vi rất khác nhau ($\Delta p=0{,}2311$ so với $0{,}0042$), nên khoảng cách đo trên phân phối hành động bằng KL. Bài toán miền tin cậy tối đa hàm thay thế với KL trung bình $\le\kappa$; trên đoạn, $\kappa=0{,}01$ giữ $t\le0{,}515$, nơi $\Delta J>0$. KL nhỏ kéo theo TV nhỏ, phân bố chiếm dụng ít đổi và sai số nhỏ (cơ sở lý thuyết; với $\tilde\pi$ cận là $-4{,}18$, cận dương chỉ với bước rất ngắn).
>
> 5. Giải và thuật toán: bậc một cho hàm thay thế, bậc hai cho KL, miền tin cậy thành một elip của ma trận Fisher; bước tối ưu đi theo gradient tự nhiên $F^{-1}g=(8;\,30)$, dồn về $\theta_B$, và một bước TRPO đưa $J$ từ $1{,}4$ lên $1{,}807$. Điều còn thiếu: mỗi bộ đệm chỉ cho một bước, với gradient liên hợp và tìm kiếm lùi.

### Mạch 5. Tối ưu chính sách gần kề (PPO)

Bản #8 (2026-11-22) theo nhận xét PPO sau chỉnh sửa (`nhan-xet-ppo-sau-sua-2026-11-22.md`) và quyết định #8: mạch chính 16 trang, phần chuyên sâu (chứng minh dạng theo dấu, phép tính chi tiết trên bộ đệm, điều kiện không chệch của approxKL, Bài tập 10.23) sang phụ lục; storyboard §3 mạch 5. Bản #7 ở mục lịch sử cuối tệp.

1. Bài toán: cần dùng lại dữ liệu từ chính sách cũ để thực hiện các bước cập nhật hiệu quả, chỉ với gradient bậc một, đồng thời kiểm soát nguy cơ suy giảm hiệu năng; TRPO cho mỗi bộ đệm một bước, sau gradient liên hợp và tìm kiếm lùi. Hàm thay thế mẫu $\mathcal L^{\mathrm{CPI}}$ tuyến tính theo tỉ số, nên không tự dừng: với lợi thế đúng, phần của nó tại $s_B$ là $3p_B-2$, tăng tới biên. Trên chuỗi, biên $(1;\,1)$ là chính sách tối ưu, nhưng xa chính sách cũ sai số của dự báo lớn và đổi dấu được ($+0{,}45$ tại $(1;\,1)$, $-0{,}18$ với $\tilde\pi$).
2. Trực quan: mẫu có lợi thế $+1$ không được thưởng thêm khi $\rho>1{,}2$; mẫu có lợi thế $-2$ không được thưởng thêm khi $\rho<0{,}8$; ở phía bất lợi, đóng góp giữ nguyên $\rho A$.
3. Công cụ: hai đường gấp khúc là mục tiêu cắt $\min\bigl(\rho A,\operatorname{clip}(\rho,1-\epsilon,1+\epsilon)A\bigr)$; phép $\min$ giữ phạt của thay đổi bất lợi (chỉ cắt thì $-2{,}4$ thay cho $-2{,}6$); theo dấu của lợi thế, mẫu ngừng đóng góp ở $1+\epsilon$ hoặc $1-\epsilon$.
4. Giới hạn trên ví dụ: bộ đệm hai lượt cho lợi thế ước lượng sai dấu ($-1{,}4$ thay cho $+0{,}4$) dù critic đúng tại $s_A$; tối đa trên bộ đệm cho $J=1$ khi không cắt và $J=1{,}392$ khi có cắt: trong ví dụ này phép cắt làm giảm mức suy giảm, nhưng không sửa lợi thế sai. Trên đoạn phẳng, mục tiêu không đổi mà KL tại $s_B$ tăng: PPO cắt đóng góp của từng mẫu, không cắt chính sách mới.
5. Thực hành và kết luận: một vòng PPO giữ cố định $\log\pi_{\mathrm{old}}$, $\widehat A_t$, $V^{\mathrm{targ}}_t$ và tính lại $\rho_t$ qua $K$ lần qua bộ đệm; hàm mất mát tổng gộp actor, critic, entropy; approxKL, tỉ lệ cắt và tỉ lệ cắt có tác dụng cho biết vòng vừa chạy đổi chính sách bao nhiêu (lô giả định: $50\%$ ngoài khoảng cắt, $25\%$ mất gradient); thuật toán PPO-Clip. Ba đại lượng khép mạch: $\mathcal L^{\mathrm{CLIP}}\le\mathcal L^{\mathrm{CPI}}$ trên cùng dữ liệu, còn giữa $\Delta\mathcal L$ và $\Delta J$ không có thứ tự chung (với $\tilde\pi$: $-0{,}145$; $0{,}095$; $-0{,}085$). Điều còn thiếu chuyển sang tổng kết: không phương pháp nào trong thực hành bảo đảm $J$ tăng.

Phụ lục, phần PPO (bản #8; ngoài 120 phút): chứng minh dạng theo dấu và bốn trường hợp; phép tính tối ưu trên bộ đệm hai lượt; điều kiện để approxKL không chệch; Bài tập 10.23 (một vòng PPO-Clip với lợi thế đúng) với lời giải ba bước: chính sách mới $(0{,}6;\,0{,}8)$; $\mathcal L^{\mathrm{CLIP}}=0{,}200$, $\Delta\mathcal L=0{,}260$, $\Delta J=0{,}296$; sai số $0{,}036$ do số lần thăm $s_B$ tăng.

### Mạch 6. Tổng kết

1. Sơ đồ neo lần cuối chỉ ghi tên khối và công cụ thay thế ở mỗi khối, không có số.
2. Câu trả lời câu hỏi trung tâm là các kết luận định tính kèm điều kiện: đường cơ sở, critic và GAE cho phần (1); hàm thay thế, chặn cải thiện, TRPO và PPO cho phần (2).
3. Hai bảng kết quả và giả thiết, một bảng so sánh REINFORCE, actor–critic, TRPO, PPO-Clip theo quy tắc cập nhật, dữ liệu dùng, cách giữ bước gần, bảo đảm.
4. Câu hỏi tự kiểm tra hỏi khái niệm; bài tập về nhà; tài liệu tham khảo.

---

## 3. Kết quả lên trang (TB28)

*Lưu ý 2026-11-22:* bảng dưới là bản 2026-11-21 trước đề xuất TRPO; trang chứng minh của mạch 4 nay theo storyboard §3 (mạch 4 và mục "Phụ lục": bổ đề chênh lệch hiệu năng `7-01`, Pinsker `7-02`, bổ đề dịch chuyển `7-03`, định lý chặn cải thiện và chứng minh hệ quả theo KL `7-04`, cải thiện đơn điệu `7-06`).

Mọi kết quả mà trang chiếu dùng mang nhãn, giả thiết lấy từ ghi chú (ghi "giả thiết chung" cộng giả thiết riêng, Đ7), kết luận bằng công thức. Chứng minh theo đúng một trong hai dạng (quyết định ở cổng storyboard 2026-11-21): (a) một dòng "Chứng minh." nêu bước then chốt; (b) trang riêng "Ý tưởng chứng minh: …" có bước mang tên của ghi chú và một hộp câu hỏi tự giải thích.

| Mạch | Kết quả (ghi chú) | Nhãn trên trang | Chứng minh trên deck |
|---|---|---|---|
| 2 | Đường cơ sở không làm chệch (Mệnh đề 10.2) | Mệnh đề. | (a) `2-04` |
| 2 | Gradient dạng lợi thế (Mệnh đề 10.5(b), đề xuất N3 thành hệ quả của 10.2) | Hệ quả. | (b) `2-10` |
| 2 | Sai số TD với $v_\pi$ đúng và lợi thế (Mệnh đề 10.8(a)) | Mệnh đề. | (a) `2-07` |
| 3 | Dạng tổng, hai đầu mút, truy hồi của GAE (Mệnh đề 10.14; dùng Bổ đề 10.12) | Mệnh đề. | (b) `3-11` |
| 3 | GAE và gradient, tính không chệch (Mệnh đề 10.15) | Mệnh đề. | (b) `3-12` |
| 4 | Bổ đề chênh lệch hiệu năng (Bổ đề 10.19) | Bổ đề. | (b) `4-14` |
| 4 | Hàm thay thế tiếp xúc $J$ (Mệnh đề 10.22) | Mệnh đề. | (a) `4-17` |
| 4 | Chặn cải thiện (Định lý 10.26; dùng Bổ đề 10.25) | Định lý. | (b) `4-18` |
| 4 | Bất đẳng thức Pinsker (Mệnh đề 10.24(b)) | Mệnh đề. | (a) `4-20` (phép gộp hai nhóm, như ghi chú) |
| 4 | Chặn cải thiện theo KL trung bình (Hệ quả 10.27) | Hệ quả. | (a) `4-21` |
| 4 | KL trung bình bậc hai (Mệnh đề 10.33) | Mệnh đề. | (a) `4-22` |
| 4 | Bước gradient tự nhiên (Mệnh đề 10.34(a)) | Mệnh đề. | (a) `4-08` |
| 5 | Mục tiêu cắt theo dấu của lợi thế (Mệnh đề 10.40) | Mệnh đề. | (a) `5-11` |
| 5 | Phép cắt không chặn KL (Nhận xét 10.42) | Nhận xét. | không cần (nhận xét có ví dụ số) |
| 5 | Hàm mất mát tổng (Định nghĩa 10.46), entropy (Định nghĩa 10.45) | Định nghĩa. | không cần (bản #7, `5-18`) |
| 5 | approxKL, tỉ lệ cắt (Định nghĩa 10.47); tỉ lệ cắt có tác dụng (bản #8) | Định nghĩa. | không cần (`5-19`) |
| 5 | Mục tiêu cắt theo dấu (Mệnh đề 10.40), bản #8 | Mệnh đề. | chứng minh ở phụ lục `7-16` (TB28: phát biểu ở mạch chính) |
| 5 | Chặn dưới bi quan $\mathcal L^{\mathrm{CLIP}}\le\mathcal L^{\mathrm{CPI}}$ (Mệnh đề 10.41), bản #8 | Mệnh đề. | (a) `5-22` |
| phụ lục | approxKL không chệch (Mệnh đề 10.48), bản #8 | Mệnh đề. | (a) `7-18` |

Định nghĩa lên trang: đường cơ sở (10.1), hàm lợi thế (10.4), critic và actor (10.7), lợi thế $n$ bước (10.11), GAE (10.13), $A_\pi(s,\pi')$ (đoạn mở §4.1, đề xuất N8), hàm thay thế và tỉ số chính sách (10.21), phân kỳ KL (10.23; biến phân toàn phần đặt ở dòng "Ký hiệu:" của trang định lý), bài toán miền tin cậy (10.30), mục tiêu PPO-Clip (10.39). Thuật toán lên trang (TB31): actor–critic với GAE (ghép 10.9 và 10.16, đề xuất N7), TRPO (10.37), PPO-Clip (10.49, bản rút gọn).

## 4. Khối của ghi chú không lên trang

| Khối | Lý do |
|---|---|
| Ví dụ 10.1, 10.3, 10.5, 10.17 (bài toán một bước); Ví dụ 10.2, 10.4 (hành lang) | TB25: một ví dụ chung; ghi chú giữ |
| Mệnh đề 10.3 (đường cơ sở hằng tối ưu) | không thuộc câu chuyện; Bài tập 10.4 |
| Thuật toán 10.6 (REINFORCE có đường cơ sở) | trường hợp $\lambda=1$ của thuật toán actor–critic với GAE; ghi chú diễn giả nêu |
| Ví dụ 10.7, Thuật toán 10.9 (actor–critic một bước) | trường hợp $\lambda=0$; câu hỏi nhanh mạch 3 làm một vòng tay |
| Nhận xét 10.10, 10.17; Ví dụ 10.10, Thuật toán 10.16 phần cờ cắt ngắn | ghi chú diễn giả; Bài tập 10.7 |
| Hệ quả 10.20, Nhận xét 10.28, Hệ quả 10.29, 10.31 | ghi chú diễn giả của trang định lý và trang miền tin cậy |
| Ví dụ 10.13–10.16, Thuật toán 10.36, Nhận xét 10.35, 10.38 (bước TRPO tay trên chuỗi ở `4-25` thay cho Ví dụ 10.15, 10.16) | gradient liên hợp nêu tên ở bước của Thuật toán TRPO; ghi chú diễn giả |
| Mệnh đề 10.41, Ví dụ 10.18, 10.19, 10.20–10.23, §6.2 (PPO-Penalty), §6.5, §6.6 (chi tiết cài đặt, hội tụ) | ghi chú diễn giả của trang PPO; ghi chú. Bản #7 (2026-11-22): hàm mất mát tổng, entropy (`5-18`), approxKL, tỉ lệ cắt và ví dụ lô bốn tỉ số của §6.4 (`5-19`) lên trang; PPO-Penalty ở ghi chú diễn giả `5-18` |
| §7 (DPO) | đã bỏ (#27) |
| Tình huống 10.1–10.3 | ghi chú |

## 5. Thông điệp của ví dụ và kiểm từng con số (TB15)

| Mạch | Thông điệp | Số sinh viên nhìn | Kết luận sinh viên rút ra |
|---|---|---|---|
| 1 | Ước lượng một lượt không chệch nhưng phương sai lớn; bước dài theo nó làm $J$ giảm | $1{,}35$; $0$; $-0{,}5$; kỳ vọng $0{,}2$; xác suất ngược dấu $\tfrac12$; $J$: $1{,}4\to1{,}30\to1{,}22\to1$ | đúng thông điệp |
| 2 | Đường cơ sở giữ kỳ vọng, giảm phương sai | phương sai $0{,}69\to0{,}20\to0$, kỳ vọng $0{,}2$ cả ba | đúng; lượt $s_A\xrightarrow1s_B\xrightarrow2$ xấu đi ($0\to-0{,}7$) được nói trên trang để sinh viên không kết luận "mọi lượt đều tốt hơn" |
| 3 | Critic sai: một bước chệch, cả lượt phương sai lớn, $\lambda$ ở giữa | $-0{,}5$ ($-0{,}9$; $0$); $0{,}4$ ($0$; $1{,}62$); $\lambda=0{,}5$: $-0{,}05$ ($-0{,}45$; $0{,}405$) | đúng; lượt (i) với $\lambda=0{,}5$ cho đúng $0{,}4$ do trùng hợp, nên hàng kỳ vọng bắt buộc |
| 4 | Hàm thay thế đúng khi bước ngắn, có thể sai dấu khi bước dài đổi phân bố trạng thái | $+0{,}095$ so với $-0{,}085$; $t=0{,}25$: $0{,}024$ so với $0{,}0125$ | đúng |
| 4 | Cận cải thiện đúng nhưng lỏng; chỉ chứng nhận bước rất ngắn | cận $-4{,}18\le-0{,}085$; $\Delta<0{,}056$ | đúng |
| 5 | Hàm thay thế mẫu không tự dừng; xa chính sách cũ dự báo sai nhiều (bản #7, `5-01`) | $\ell_{s_B}=3p_B-2$; tại $(1;\,1)$: $\Delta\mathcal L=0{,}85$, $\Delta J=1{,}3$; với $\tilde\pi$: $0{,}095$ so với $-0{,}085$ | đúng nếu hộp sai số $+0{,}45$ / $-0{,}18$ đứng trên trang; chỉ nhìn $J=2{,}7$ thì sinh viên có thể kết luận "tối ưu tới biên là tốt" (storyboard §7, `5-01`) |
| 5 | Lợi thế dương ngừng đóng góp trên $1+\epsilon$, lợi thế âm dưới $1-\epsilon$; phía bất lợi giữ $\rho A$ (bản #7) | $1{,}3/1{,}2$; $0{,}7/0{,}7$; $-1{,}4/-1{,}6$; $-2{,}6/-2{,}6$; chỉ cắt: $-2{,}4$, $0{,}8$ | đúng |
| 5 | Lợi thế sai dấu và hàm thay thế tuyến tính theo $\rho$ đẩy chính sách tới biên; phép cắt giới hạn mỗi vòng | không cắt: $J=1$; có cắt: $J=1{,}392$ | đúng |
| 5 | Phép cắt không chặn KL, và dừng cả bước tốt | trên đoạn phẳng ở $s_B$: KL $0{,}011\to0{,}104$ khi $p_B$ từ $\tfrac{11}{15}$ tới $0{,}85$; $J(0{,}4;\,0{,}85)=1{,}518>1{,}392$ | đúng |
| 5 | Chỉ số theo dõi một lô (bản #7, lô giả định) | $\rho=(1{,}05;\,1{,}18;\,1{,}24;\,0{,}70)$: tỉ lệ cắt $50\%$, approxKL $\approx0{,}0243$ | đúng; trang ghi "giả định" và lý do |

## 6. Đề xuất sửa ghi chú (NT3, cho điều phối viên)

Ngoài N1–N6 của bản tổng hợp:

- N7. (Điều phối viên chốt 2026-11-21.) Ghi chú thêm một đoạn không đánh số sau Thuật toán 10.16 mô tả actor–critic với GAE (ghép Thuật toán 10.9 và 10.16); trang `L10-3-10` dẫn "Thuật toán 10.9 và 10.16" làm nguồn.
- N8. (Điều phối viên chốt 2026-11-21.) Không thêm khối định nghĩa (tránh đánh lại số); ghi chú thêm câu $A_\pi(s,\pi')=\sum_a\pi'(a\mid s)q_\pi(s,a)-v_\pi(s)$ vào đoạn mở §4.1; trang chiếu `L10-4-13` vẫn ghi nhãn "Định nghĩa."
- N9. (Điều phối viên chốt 2026-11-21: các số được thêm vào ghi chú.) Bổ sung vào ví dụ tương ứng các số deck dùng mà ghi chú chưa có: $D_{\mathrm{KL}}(s_B)=0{,}0566$, $\bar D_{\mathrm{KL}}=0{,}0536$, phạt dạng KL $14{,}7$ cho bước tới $\tilde\pi$; miền KL $\kappa=0{,}01$ trên đoạn thẳng là $t\le0{,}515$; bước TRPO trên chuỗi với $\kappa=0{,}01$ ($\Delta^*=(0{,}35;\,1{,}30)$, KL thật $0{,}0085$, $J=1{,}807$); trên bộ đệm hai lượt, KL tại $s_B$ $0{,}011\to0{,}104$ và $J(0{,}4;\,0{,}85)=1{,}518$; câu hỏi nhanh actor–critic với GAE ($\theta=(0{,}2;\,\log2+0{,}6)$, $p=(0{,}550;\,0{,}785)$). Các trường hợp khác cấu trúc của Đ2 trên trang chỉ dùng phản ví dụ đã có trong ghi chú (đoạn sau Mệnh đề 10.5, đoạn sau Bổ đề 10.19); thêm số cho ví dụ một bước TRPO (`4-25`: $D_{\mathrm{KL}}=(0{,}0150;\,0{,}156)$ tại $p=(0{,}586;\,0{,}880)$) và nghiệm số $t\approx0{,}515$ của $\bar D_{\mathrm{KL}}(t)=0{,}01$ kèm dòng kiểm.
- N10. (Đã giải quyết theo điều phối viên 2026-11-21.) Ghi chú giữ $\pi'=(0{,}6;\,0{,}8)$ cho Ví dụ 10.11 và gọi bước dài là $\tilde\pi$, $\tilde\theta=(\log9;\,0)$; deck dùng $\pi'$ trong phát biểu tổng quát và $\tilde\pi$ cho chính sách cụ thể của ví dụ. Đánh số ghi chú sau khi bỏ DPO: tổng kết là §7; số bài tập giữ theo BT4: bài softmax là Bài tập 10.22 (mạch 1), bài PPO-Clip là Bài tập 10.23 (cuối mạch 5), số 10.18–10.21 bỏ trống.

---

# Lịch sử: câu chuyện mạch 4 trước đề xuất TRPO (2026-11-21)

Phần dưới là mục "Mạch 4" trước khi thay theo đề xuất trình bày TRPO của tác giả, giữ nguyên chữ, tiêu đề hạ một bậc. Không còn hiệu lực.

#### Mạch 4. Hàm thay thế và miền tin cậy (TRPO)

1. Bài toán: một bước cập nhật dài đề xuất chính sách ứng viên $\tilde\theta=(\log9;\,0)$, tức $\tilde\pi=(0{,}9;\,0{,}5)$; cần đánh giá $J(\tilde\pi)$ từ các lượt của $\pi$, trong khi $\tilde\pi$ thăm $s_B$ với xác suất $0{,}9$ thay cho $0{,}5$.
2. Trực quan: đổi một bước tại $s$ sang $\pi'$ rồi theo $\pi$ cho lợi ích $A_\pi(s,\pi')$; với $\tilde\pi$, lợi ích bằng $0{,}32$ tại $s_A$ và $-0{,}5$ tại $s_B$; bổ đề hiệu hiệu năng cộng các lợi ích này theo số lần thăm kỳ vọng có chiết khấu của chính sách mới, $\eta_{\tilde\pi}=(1;\,0{,}81)$, cho $\Delta J=-0{,}085$.
3. Công cụ: hàm thay thế giữ số lần thăm của $\pi$ nên tính được từ lượt cũ nhờ tỉ số chính sách; với $\tilde\pi$ nó dự báo $+0{,}095$, sai số bằng $\sum_s(\eta_{\tilde\pi}-\eta_\pi)A_\pi(s,\tilde\pi)=-0{,}18$; nó tiếp xúc $J$ tại $\pi$ (cùng giá trị, cùng gradient), và định lý chặn cải thiện chặn sai số theo khoảng cách TV, rồi theo KL trung bình.
4. Kết quả trên ví dụ: trên đoạn từ $\pi$ tới $\tilde\pi$, $\Delta\mathcal L=0{,}095t$ và $\Delta J=0{,}095t-0{,}18t^2$; bước $t=0{,}25$ cho hai số cùng dấu, bước $t=1$ cho hai số trái dấu; cận cải thiện dương chỉ khi bước rất ngắn ($\Delta<0{,}056$ trên bước chỉ đổi $p_B$).
5. Kết quả: bài toán miền tin cậy tối đa hàm thay thế với KL trung bình không vượt $\kappa$; gần chính sách cũ, nghiệm đi theo gradient tự nhiên $F^{-1}g=(8;\,30)$, và TRPO giải xấp xỉ bài toán này. Điều còn thiếu: mỗi bước TRPO cần ma trận Fisher, gradient liên hợp và tìm kiếm lùi, và mỗi bộ đệm chỉ cho một bước.

---

# Lịch sử: câu chuyện mạch 5 trước nhận xét PPO (2026-11-21)

Phần dưới là mục "Mạch 5" trước khi thay theo nhận xét phần PPO (#7, 2026-11-22), giữ nguyên chữ, tiêu đề hạ một bậc. Không còn hiệu lực.

#### Mạch 5. Tối ưu chính sách gần kề (PPO)

1. Bài toán: dùng lại một bộ đệm cho nhiều bước cập nhật, chỉ với gradient bậc một, mà chính sách mới không rời xa chính sách cũ.
2. Trực quan: trên bộ đệm hai lượt $s_A\xrightarrow1s_B\xrightarrow2$, $s_A\xrightarrow2$ với critic $(1{,}4;\,1)$ và $\lambda=1$, lợi thế ước lượng của hành động 1 ở $s_A$ là $-1{,}4$ (lợi thế đúng $+0{,}4$); tối đa hàm thay thế mẫu không ràng buộc đẩy chính sách tới giới hạn $(0;\,1)$, nơi $J=1$.
3. Công cụ: hàm thay thế chỉ đáng tin khi mọi tỉ số chính sách gần $1$, nên mục tiêu cắt bỏ phần lợi của việc đẩy $\rho$ ra ngoài $[1-\epsilon,1+\epsilon]$ và giữ phần thiệt.
4. Kết quả trên ví dụ: với $\epsilon=0{,}2$, vòng trong dừng ở $(0{,}4;\,\tfrac{11}{15})$, $J=1{,}392$, giảm $0{,}008$ thay cho $0{,}4$; phép cắt không chặn KL và cũng dừng cả bước làm $J$ tăng.
5. Thuật toán PPO-Clip, so sánh với TRPO, và một bài tập tổng hợp có lời giải (một vòng PPO-Clip với lợi thế đúng) khép mạch. Điều còn thiếu chuyển sang tổng kết: không phương pháp nào trong thực hành bảo đảm $J$ tăng.

---

# Lịch sử: câu chuyện mạch 5 bản #7 (2026-11-22, trước nhận xét PPO sau chỉnh sửa #8)

Giữ nguyên chữ, tiêu đề hạ một bậc. Không còn hiệu lực.

#### Mạch 5. Tối ưu chính sách gần kề (PPO)

Bản 2026-11-22 theo nhận xét phần PPO (#7, `nhan-xet-ppo-2026-11-22.md`) và quyết định #7 của tác giả (lợi thế đúng tại $s_B$ cho trực giác; lô giả định cho chỉ số); storyboard §3 mạch 5. Bản 2026-11-21 ở mục lịch sử cuối tệp.

1. Bài toán: TRPO cho mỗi bộ đệm một bước, sau gradient liên hợp và tìm kiếm lùi; cần dùng lại một bộ đệm cho nhiều bước gradient bậc một. Hàm thay thế mẫu $\mathcal L^{\mathrm{CPI}}$ là ứng viên trực tiếp, nhưng mỗi mẫu đóng góp tuyến tính theo tỉ số, nên nó không tự dừng: với lợi thế đúng, phần của nó tại $s_B$ là $3p_B-2$, tăng tới biên $p_B=1$. Trên chuỗi, biên $(1;\,1)$ là chính sách tối ưu ($J=2{,}7$), nhưng xa chính sách cũ sai số của dự báo lớn và đổi dấu được: $+0{,}45$ tại $(1;\,1)$, $-0{,}18$ với $\tilde\pi$.
2. Trực quan: mẫu $(s_B,1)$ có lợi thế $+1$, đóng góp $\rho$ tăng mãi khi $p_B$ tăng; mẫu $(s_B,2)$ có lợi thế $-2$, đóng góp $-2\rho$ tăng khi xác suất của hành động 2 giảm. Với $\epsilon=0{,}2$, đóng góp ngừng tăng khi $\rho>1{,}2$ (tức $p_B>0{,}8$) và khi $\rho<0{,}8$ (tức $p_B>\tfrac{11}{15}$); bốn trường hợp cho $1{,}3/1{,}2$; $0{,}7/0{,}7$; $-1{,}4/-1{,}6$; $-2{,}6/-2{,}6$.
3. Công cụ: hai đường gấp khúc là một công thức, $\min\bigl(\rho A,\operatorname{clip}(\rho,1-\epsilon,1+\epsilon)A\bigr)$, tức mục tiêu cắt. Phép $\min$ giữ phạt của thay đổi bất lợi: chỉ cắt thì mẫu $A=-2$, $\rho=1{,}3$ cho $-2{,}4$ thay cho $-2{,}6$. Theo dấu của lợi thế, mẫu ngừng đóng góp ở $1+\epsilon$ hoặc $1-\epsilon$.
4. Kết quả trên ví dụ và giới hạn: bộ đệm hai lượt cho lợi thế ước lượng sai dấu ($-1{,}4$ thay cho $+0{,}4$) dù critic đúng tại $s_A$. Tối đa $\mathcal L^{\mathrm{CPI}}$ trên bộ đệm đưa $J$ về $1$; vòng trong của mục tiêu cắt dừng ở $(0{,}4;\,\tfrac{11}{15})$ với $J=1{,}392$: phép cắt không sửa lợi thế sai, nhưng giới hạn mức giảm. Trên đoạn phẳng, mục tiêu cắt không đổi mà KL tại $s_B$ tăng từ $0{,}011$ lên $0{,}396$: PPO cắt đóng góp của từng mẫu, không cắt chính sách mới.
5. Thuật toán: một vòng PPO giữ cố định bộ đệm, $\log\pi_{\mathrm{old}}$, $\widehat A_t$, $V^{\mathrm{targ}}_t$ và tính lại $\rho_t$ qua $K$ lần qua bộ đệm; hàm mất mát tổng gộp actor, critic và entropy; approxKL, tỉ lệ cắt và entropy cho biết vòng vừa chạy đổi chính sách bao nhiêu (lô giả định: tỉ lệ cắt $50\%$, approxKL $\approx0{,}0243$). Thuật toán PPO-Clip, so sánh với TRPO và một bài tập tổng hợp (một vòng PPO-Clip với lợi thế đúng) khép mạch. Điều còn thiếu chuyển sang tổng kết: không phương pháp nào trong thực hành bảo đảm $J$ tăng.
