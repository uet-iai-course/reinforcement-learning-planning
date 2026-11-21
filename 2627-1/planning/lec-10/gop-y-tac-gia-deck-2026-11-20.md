# Góp ý của tác giả khi duyệt deck 10 (2026-11-20)

Tác giả đi một lượt các trang, trao đổi; điều phối viên ghi từng góp ý ở đây rồi tổng hợp để sửa một thể (một lượt biên tập, rà lại, kiểm cuối). Chưa sửa gì trong deck cho tới khi tác giả nói xong.

| # | Trang | Góp ý của tác giả (nguyên văn) | Chẩn đoán | Hướng sửa đề xuất |
|---|---|---|---|---|
| 1 | L10-1-02 | (ảnh trang) "giải thích" | Mặt trang đưa $\psi(s,1)=(1-p)(1;-1)$, $\psi(s,2)=-p(1;-1)$ mà không có định nghĩa $\psi=\nabla_\theta\log\pi$, không có ý nghĩa (hướng đẩy, độ lớn $1-p$ và $p$). | Thêm $\psi(s,a)=\nabla_\theta\log\pi_\theta(a\mid s)$ vào dòng "Ký hiệu"; một dòng ý nghĩa: chọn 1 đẩy về phía 1 mạnh $1-p$, chọn 2 đẩy ngược mạnh $p$; hai tọa độ ngược dấu. |
| 2 | L10-1-03 | "mô tả đột ngột, tham số \theta, chính sách \pi hiện là gì ?" | Ví dụ dùng đối tượng trước khi dựng: thiếu $\theta$ là hai điểm dùng chung mọi ô (đặc trưng giống nhau), $p=\sigma(\theta_1-\theta_2)$ giống ở mọi ô, $\theta=(0;0)$, mục tiêu $J$, $J(\tfrac12)=-12$, gradient đúng $(2;-2)$, vì sao chỉ theo dõi $\theta_1$. Lời giải không so với gradient đúng (lượt đẩy ngược chiều). Nguồn: ghi chú Ví dụ 10.2 có đủ. | Thêm trang dựng ví dụ trước trang tính; trang tính chỉ còn bảng và câu hỏi; lời giải thêm so sánh với $+2$. Rà mọi ví dụ chạy theo câu "trước phép tính đầu tiên đã dựng tham số, chính sách, mục tiêu chưa". Đề xuất quy tắc TB24 (dựng ví dụ trước khi tính) và vai sinh viên chỉ xem ảnh, không đọc ghi chú. |
| 3 | L10-1-04 (Ba lượt cho ba hướng cập nhật khác nhau) | "nên điền kết quả phép tính vào bảng luôn (song song với việc thể hiện trên đồ thị ở dưới)" | Cột "Phép tính $\widehat g_1$" dừng ở biểu thức; kết quả $-1$, $1$, $-5{,}5$ chỉ có trên trục số bên dưới, sinh viên phải tự cộng hoặc nhìn qua lại (tách chú ý). Thêm: dòng (c) gộp số hạng, khác cách viết (a), (b); cột $G_t$ dùng "$\dots$" nên không dò được từng số hạng; "Nhắc lại" đưa $J(p)$, $J'$ và $\partial p/\partial\theta_1=p(1-p)$ chưa được dựng (thuộc lỗi #2). | Thêm cột kết quả $\widehat g_1$ ($-1$; $1$; $-5{,}5$), hiện cùng mảnh (fragment) với chấm tương ứng trên trục số; viết (c) từng số hạng theo thứ tự bước như (a), (b); ghi đủ $G_t$; chuyển $J(p)$, $J(\tfrac12)=-12$, gradient đúng $2$ sang trang dựng ví dụ (#2), trang này chỉ nhắc một dòng. Quy tắc chung: bảng tính luôn có cột kết quả, khớp với hình. |
| 4 | L10-1-04 (dòng "Nhắc lại: $J(p)=\dots$") | (ảnh dòng $J(p)$) "ngoài ra, công thức của J(p) cũng cần được derive" | $J(p)$ được đưa ra như dữ kiện. Ghi chú cũng không dẫn $J(p)$ với $p$ tổng quát: Ví dụ 10.2 chỉ phát biểu, và §2 (dòng ~292) chỉ giải hệ Bellman tại $p=\tfrac12$. Sinh viên không kiểm được $-12$, $J'=8$, $p^*=2-\sqrt2$. | Sửa ghi chú trước: Ví dụ 10.2 dẫn $J(p)$ từ hệ Bellman với $p$ tổng quát (ba phương trình, khử từng bước), rồi $J(\tfrac12)$, $J'(\tfrac12)$, $p^*$. Deck: trong cụm dựng ví dụ (#2) thêm trang "Ví dụ: hành lang ngắn, tính $J(p)$": hình hành lang có nhãn $p$, $1-p$ trên mũi tên; ba phương trình; mỗi dòng một bước khử; kiểm tại $p=\tfrac12$. Đạo hàm và $\partial p/\partial\theta_1=p(1-p)$ trên trang kế. |
| 5 | Mạch 1 (L10-1-02 → 1-05), so với mạch 2 | "hơn nữa, lúc thì dùng J(p), lúc lại dùng tham số \theta_1, \theta_2" | Hai lỗi chồng nhau. (i) Không có quy ước nào nói $J$ phụ thuộc $\theta$ chỉ qua $p$; trang đổi qua lại giữa $J(p)$, $J'$ và gradient theo $(\theta_1;\theta_2)$. (ii) Tham số hóa không thống nhất giữa hai ví dụ: hành lang dùng hai logit $(\theta_1;\theta_2)$ (vì thế phải "chỉ theo dõi tọa độ $\theta_1$"), chuỗi hai trạng thái dùng một logit mỗi trạng thái, $p_s=\sigma(\theta_s)$. | Đề xuất: hành lang dùng một tham số vô hướng $\theta$, $p=\sigma(\theta)$ (logit $\theta$ cho hành động 1, $0$ cho hành động 2), như chuỗi hai trạng thái; $\psi(s,1)=1-p$, $\psi(s,2)=-p$; gradient $\frac{dJ}{d\theta}=J'(p)\,p(1-p)=2$. Nhân đôi mọi bước học của hành lang để giữ nguyên mọi giá trị $p$, $J$. Quy ước một lần trên trang dựng ví dụ: "cập nhật $\theta$, đọc $p=\sigma(\theta)$; $J$ phụ thuộc $\theta$ qua $p$ nên viết $J(p)$"; mọi bảng cập nhật có đủ cột $\theta$, $p$, $J$. Sửa ghi chú trước (25 chỗ dùng $\theta_1$ hoặc $(2;-2)$; exercises.md 1 chỗ). |
| 6 | L10-2-00 (dòng dẫn mạch 2) và mọi dòng dẫn mạch | (ảnh: "2. So lợi tức với giá trị của trạng thái — Một nửa số lượt trên chuỗi hai trạng thái đẩy chính sách sai hướng.") "câu tóm tắt tối nghĩa, người đọc (sinh viên) làm sao hiểu được" | Câu dẫn viết như lời nhá trước: dùng ví dụ chưa giới thiệu ("chuỗi hai trạng thái"), con số không ngữ cảnh ("một nửa số lượt"), cụm mơ hồ ("sai hướng": so với hướng nào); và nêu triệu chứng thay vì điều sinh viên sẽ biết sau mạch. Năm dòng dẫn còn lại cùng kiểu ("Critic học dở…", "Chỉ chạy Adam trên lượt cũ…", "Ba khối đã sửa của vòng cập nhật…"). | Viết lại cả sáu dòng dẫn: một câu nêu ý chính của mạch bằng từ sinh viên đã có, không nhắc ví dụ, không con số. Mạch 2, ví dụ: "Lợi tức chỉ cho biết hành động tốt hay kém khi so với mức thường đạt ở trạng thái đó." Kiểm bằng câu hỏi: sinh viên chưa học mạch có hiểu câu này không. |
| 7 | L10-2-01 (Ví dụ: chuỗi hai trạng thái (1)) | (ảnh trang) "tôi đọc mà không hiểu gì" | Một trang dồn tám thứ: môi trường (chỉ có hình, không lời), tham số hóa $p_s=\sigma(\theta_s)$, giá trị $p_B=\tfrac23$ không lý do, $J=2{,}7p_Ap_B+1-p_A$ không dẫn, gradient (số $0{,}8$ không giải thích), $v_\pi(s_A)$, $v_\pi(s_B)$ in sẵn trên hình, bảng ba lượt, trung bình và phương sai không phép tính. Ý chính của trang (hành động 2 kém hơn mức thường có nhưng vẫn được tăng xác suất, vì $1>0$) chỉ nằm trong ghi chú người nói; nghĩa của dấu $-0{,}5$ (kéo $p_A$ xuống = tăng xác suất hành động 2) không được nói. Kết luận của mạch ("thưởng 1 < mức thường có 1,4") in sẵn trên hình trước khi vấn đề được đặt. | Tách thành chuỗi trang, mỗi trang một bước: (a) dựng chuỗi bằng lời + hình sạch: xuất phát $s_A$, hành động và thưởng, $\gamma$, tham số $\theta_s$, $p_s=\sigma(\theta_s)$, giá trị đang xét; (b) bảng ba loại lượt (xác suất, $G_0$) → $J=1{,}4$ và công thức $J$ suy từ chính bảng; gradient theo $\theta_A$ hai thừa số, $=0{,}2>0$: nên tăng $p_A$; (c) REINFORCE trên từng loại lượt, thêm cột "đẩy $p_A$" (lên/xuống/đứng yên); trung bình có phép tính; (d) câu hỏi: lượt chọn 2 cho $1<1{,}8$ của hành động 1 mà vẫn kéo $p_A$ xuống, vì mọi lợi tức dương; dẫn tới so với mức thường đạt $v_\pi(s_A)=1{,}4$. Phương sai sang trang so sánh sau. Bỏ chú thích $v_\pi$ và chữ đỏ khỏi hình mở đầu. |
| 8 | Mạch 1 so với mạch 2–5 | "sao không dùng lại ví dụ này ở phía trước, để đỡ mất công giải thích nhiều ví dụ" | Chuỗi hai trạng thái đã là ví dụ chạy của mạch 2–5 (đường cơ sở, critic/GAE, hàm thay thế, bộ đệm PPO); chỉ mạch 1 dùng hành lang. Hai ví dụ nghĩa là hai lần dựng môi trường, hai cách tham số hóa (#5), hai phép dẫn $J$ (#4). | Đề xuất: dùng chuỗi hai trạng thái từ mạch 1, bỏ hành lang khỏi deck. Dựng chuỗi một lần ở mạch 1 (sửa luôn #2, #4, #5, #7a–b). Vấn đề 1 (dao động): bảng ba loại lượt, một nửa xác suất cho $\widehat g_A=-0{,}5$ ngược dấu gradient $0{,}2$. Vấn đề 2 (bước dài): trên chuỗi, đi theo gradient đúng không làm $J$ giảm (đỉnh ở góc $p_A=p_B=1$), nên thay bằng: một bước dài theo ước lượng của một lượt làm $J$ giảm ($\alpha=2$ trên lượt "2": $J$ $1{,}4\to1{,}22$), và bước tới $(1;\,0{,}5)$ làm $J$ giảm $0{,}05$ dù hàm thay thế báo tăng (mạch 4). Mất hình "vượt đỉnh" của hành lang. Ghi chú: §1 cần dựng chuỗi (hiện dựng ở §2, dòng ~473); Ví dụ 10.2 có thể giữ trong ghi chú làm ví dụ bổ sung. Cần tác giả quyết. |
| 9 | Cả deck (quyết định) | "ghi chú giữ vẫn được, nhưng nên dùng 1 ví dụ chung cho nhiều mạch để đỡ công dựng, lựa chọn ví dụ, con số để thể hiện được nhiều ý (dao động lớn, bước dài giảm J)" | Quyết định của tác giả: một ví dụ chung cho nhiều mạch; ghi chú giữ hành lang (Ví dụ 10.2). Ràng buộc toán: trên chuỗi hai trạng thái (một tham số mỗi trạng thái), đi theo gradient đúng không bao giờ làm $J$ giảm; "bước dài giảm $J$" phải đến từ ước lượng nhiễu hoặc từ đánh giá chính sách mới bằng dữ liệu cũ. | Phương án đề xuất (A): giữ chuỗi với số hiện có (đã được vai toán kiểm), dựng ở mạch 1; mạch 1 cho thấy dao động (ba loại lượt) và bước dài giảm $J$ (bước theo lượt "chọn 2": $\alpha=2$ cho $J=1{,}22$; bước càng dài $p_A\to0$, $J\to1$, giảm $0{,}4$); mạch 5 khép vòng: cùng mức giảm $0{,}4$ khi không cắt, $0{,}008$ khi cắt. Mạch 6 dùng $s_B$ của chuỗi làm "hai câu trả lời" ($\pi_{\mathrm{ref}}=(\tfrac23;\tfrac13)$ trùng $p_B$). Phương án B (tham số dùng chung để có đỉnh ở trong) buộc tính lại mọi số của mạch 2–5; không đề xuất. |
| 10 | L10-2-02 (Trừ $v_\pi$ giữ trung bình, giảm dao động) | (ảnh trang) "slide này đưa việc trừ v_\pi một cách đột ngột, không có lý do, hay trực quan gì cả" | Trang mở bằng công cụ ("Hệ số mới: $G_t$ trừ đường cơ sở $b(S_t)=v_\pi(S_t)$") trước lý do; tiêu đề phát biểu kết quả trước khi có vấn đề; $1{,}4$ xuất hiện trong công thức mà không nói đó là mức thường đạt ở $s_A$ và tính thế nào; không có hình; không giải thích vì sao trung bình không đổi; dòng "1, 2" bị phạt $-0{,}7$ không được giải thích. | Chuỗi trang: (a) trực quan: trục số các lợi tức $0$; $1$; $2{,}7$ từ $s_A$ với vạch $v_\pi(s_A)=1{,}4$ = trung bình lợi tức từ $s_A$ (tính: $\tfrac12\cdot0{,}9\cdot2+\tfrac12\cdot1$); bên trái "kém hơn thường", bên phải "tốt hơn thường"; (b) quy tắc: hệ số $G_0-1{,}4$; bảng thêm cột dấu và "đẩy $p_A$"; lượt "chọn 2" nay kéo đúng hướng; lượt "1, 2" bị phạt vì xui ở $s_B$ (phần dao động còn lại, xác suất $\tfrac16$); (c) vì sao trung bình giữ $0{,}2$: $\psi$ có trung bình $0$ ở $s_A$, nên phần trừ $1{,}4\,\psi$ có trung bình $0$; (d) so phương sai $0{,}69\to0{,}20$ có phép tính. Tên "đường cơ sở" đặt sau trực quan. |
| 11 | L10-2-04 và nhiều tiêu đề khác | (ảnh tiêu đề "Trừ một mức của trạng thái không đổi trung bình") "Câu kiểu này là văn nói, cần văn học thuật" | Văn nói: động từ thường thay thuật ngữ ("trừ một mức", "không đổi trung bình", "nơi chính sách tới", "cho lợi", "đi quá xa", "dồn bước"). Khoảng 15 tiêu đề cùng kiểu. Nguyên nhân: hiểu sai VP25/TB ("chỉ dùng từ sinh viên đã có") thành tránh thuật ngữ, rồi diễn giải bằng lời nói thường. | Văn học thuật: thuật ngữ chuẩn sau khi đã định nghĩa (đường cơ sở, kỳ vọng, phương sai, ước lượng chệch, phân bố trạng thái, tỉ số xác suất). Ví dụ: "Đường cơ sở chỉ phụ thuộc trạng thái không làm chệch ước lượng gradient". Rà toàn bộ tiêu đề, dòng dẫn, thân trang theo văn phong học thuật (VP, no-ai-slop) trong lượt sửa; thêm một vai rà văn phong học thuật. |
| 12 | Cả deck (thuật ngữ) | "trung bình --> kì vọng" | Mặt trang dùng "trung bình" 36 lần, "kỳ vọng" 0 lần; ghi chú dùng "kỳ vọng" 71 lần. Deck lệch thuật ngữ của ghi chú và gộp hai khái niệm: kỳ vọng của biến ngẫu nhiên và trung bình của một mẫu hữu hạn. | Kỳ vọng của biến ngẫu nhiên (ước lượng gradient, hệ số, hàm điểm, $\delta_t$, KL theo phân bố trạng thái) viết "kỳ vọng" (chính tả "kỳ" theo P2 của học phần). "Trung bình" chỉ giữ cho trung bình cộng trên mẫu hữu hạn (hai lượt, bộ đệm, hàm thay thế mẫu), viết rõ "trung bình trên $N$ mẫu". Dòng bảng "trung bình; phương sai" → "kỳ vọng; phương sai". Áp cho mặt trang và ghi chú người nói. |
| 13 | L10-2-06 (Hệ số trung bình là lợi thế) | (ảnh trang) "tiêu đề như văn nói; Định nghĩa cũng như văn nói" | Tiêu đề khẩu ngữ và mơ hồ ("hệ số trung bình"). Định nghĩa viết lại bằng lời nói ("đo hành động đó tốt hơn mức thường có bao nhiêu"), trộn diễn giải vào phát biểu, bỏ giả thiết; ghi chú có bản học thuật (Định nghĩa 10.4: "Cho chính sách Markov dừng $\pi$ với … *Hàm lợi thế* … là …"). Phần sau ("Hệ số … có trung bình …", "Còn thiếu: …") cùng kiểu. Hình dùng $1{,}8$, $1{,}4$, $3$, $2$ mà không ghi đó là $q_\pi$, $v_\pi$. | Tiêu đề: "Hàm lợi thế và gradient dạng lợi thế". "Định nghĩa. Cho chính sách $\pi$ với giá trị trạng thái $v_\pi$ và giá trị hành động $q_\pi$. Hàm lợi thế (advantage function) của $\pi$ là $A_\pi(s,a)=q_\pi(s,a)-v_\pi(s)$." "Ý nghĩa: $A_\pi(s,a)>0$ khi thực hiện $a$ tại $s$ rồi theo $\pi$ cho lợi tức kỳ vọng lớn hơn $v_\pi(s)$." "Mệnh đề. $\mathbb E[G_t-v_\pi(S_t)\mid S_t,A_t]=A_\pi(S_t,A_t)$, do đó $\nabla J=\dots$" "Lưu ý: $q_\pi$, $v_\pi$ chưa biết; cần ước lượng $A_\pi$ từ dữ liệu." Hình ghi rõ $q_\pi$, $v_\pi$ và phép tính $q_\pi(s_A,1)=0{,}9\cdot v_\pi(s_B)=1{,}8$. |
| 14 | L10-2-06 (gradient dạng lợi thế) | (ảnh "Hệ số $G_t-v_\pi(S_t)$ có trung bình $A_\pi(S_t,A_t)$, nên gradient chỉ cần lợi thế: $\nabla J=\mathbb E[\sum_t\gamma^tA_\pi(S_t,A_t)\psi_t]$") "khẳng định này cần chứng minh (hệ quả của mệnh đề đường cơ sở)" | Kết quả chính được nêu bằng "nên" không chứng minh; chữ "có trung bình" che mất điều kiện (kỳ vọng có điều kiện theo $(S_t,A_t)$, cần tính Markov). Ghi chú có chứng minh 3 bước (Mệnh đề 10.5(b), Bước 2). | Phát biểu "Hệ quả (gradient dạng lợi thế)" ngay sau mệnh đề đường cơ sở; trang "Ý tưởng chứng minh: gradient dạng lợi thế" 3 bước: (1) Mệnh đề đường cơ sở với $b=v_\pi$; (2) tính chất tháp theo $(H_t,A_t)$, $\psi_t$ và $v_\pi(S_t)$ ra ngoài; (3) tính Markov: $\mathbb E[G_t\mid H_t,A_t]=q_\pi(S_t,A_t)$, rồi $q_\pi-v_\pi=A_\pi$. Kiểm trên chuỗi: $\tfrac12\cdot0{,}4\cdot0{,}5+\tfrac12(-0{,}4)(-0{,}5)=0{,}2$. Đề xuất cho ghi chú: đổi nhãn 10.5(b) thành hệ quả của Mệnh đề 10.2 (tác giả quyết). |
| 15 | L10-2-07, L10-2-08 (cuối mạch 2) và L10-3-01 | (ảnh L10-2-07) "slide này tự nhiên nói đến critic actor rồi kết thúc mạch, có liên quan gì không ?" | Có liên quan nhưng trang không nói. Sau L10-2-06, gradient cần $A_\pi$ mà $q_\pi$ chưa biết; $G_t$ là ước lượng của $q_\pi$ mang nhiễu của mọi bước sau; $R_{t+1}+\gamma v_\pi(S_{t+1})$ chỉ mang nhiễu của một bước, nên $\delta_t$ là cách thứ ba "so lợi tức với giá trị của trạng thái"; trên chuỗi phương sai $0{,}69\to0{,}20\to0$. Trang bỏ câu hỏi dẫn này, đặt tên vai "critic/actor" trước nhu cầu, hình actor/critic nói về việc học $\hat v$ (không dùng ở mạch 2), mệnh đề "$\delta_t$ trung bình bằng lợi thế" không chứng minh. "Critic học dở" là điểm vào của mạch 3, nhưng chỉ nằm ở dòng "Còn thiếu:" của L10-2-08. | Cuối mạch 2 dựng thành chuỗi: câu hỏi ($q_\pi$ chưa biết; $G_t$ mang nhiễu của mọi bước sau) → ý: thay phần sau bước đầu bằng $\gamma v_\pi(S_{t+1})$ → Mệnh đề $\mathbb E[\delta_t\mid S_t,A_t]=A_\pi$ + ý tưởng chứng minh 1 dòng → bảng ba hệ số trên chuỗi, phương sai $0{,}69$; $0{,}20$; $0$ (L10-2-08, đổi tên cột "critic đúng" thành "$v_\pi$ đúng"). Bỏ "critic/actor" khỏi mạch 2. Mạch 3 mở bằng: $v_\pi$ chưa biết → học hàm $\hat v$ (critic), chính sách là actor; critic sai $(1{,}4;1)$ làm $\delta$ chệch (L10-3-01). |
| 16 | L10-2-08 (Với critic đúng, mọi lượt cho cùng tọa độ $0{,}2$) | (ảnh trang) "slide này các con số ở đâu ra ?" | Không số nào có phép tính trên trang: xác suất ($p_Ap_B$, …), cột REINFORCE và "trừ $v_\pi$" chép từ hai trang trước nhưng bỏ cột $G_0$, $\psi_A$; $\delta_0=\pm0{,}4$ chỉ có trên hình của trang trước; $v_\pi(s_A)=1{,}4$, $v_\pi(s_B)=2$ chỉ có trên hình L10-2-01; phương sai $0{,}69$; $0{,}20$; $0$ không được tính ở đâu trên deck. Nửa dưới bị sơ đồ neo chiếm, không liên quan tới bảng. | Bảng đủ cột đầu vào: đường đi, xác suất (có tích), $G_0$, $\psi_A$, rồi ba cột hệ số nhân $\psi_A$; cột $\delta_0$ có phép tính ($0+0{,}9\cdot2-1{,}4$; $1-1{,}4$). Hai dòng cuối: kỳ vọng và phương sai, mỗi ô một phép tính; nếu chật thì tách trang tiếp theo. Sơ đồ neo không đặt chung với bảng tính; dùng ở trang tóm tắt cuối mạch. Quy tắc: mọi số trên trang tính được ngay trên trang hoặc dẫn rõ từ trang liền trước. |
| 17 | L10-3-00 (tiêu đề và dòng dẫn mạch 3); thuật ngữ cả deck | (ảnh "3. Trộn đánh giá một bước và cả lượt / Critic học dở thì đánh giá một bước bị lệch, còn lợi tức cả lượt thì dao động.") "câu tiêu đề và câu tóm tắt đều văn nói" | Văn nói: "trộn", "học dở", "thì … còn … thì", "lệch", "dao động". Dòng dẫn còn dùng "critic" là thuật ngữ mạch này mới giới thiệu (#6, #15). Thuật ngữ cả deck lệch ghi chú: mặt trang "chệch" 0 lần (ghi chú 59), "phương sai" 4 lần (ghi chú 53), "dao động" 12 lần (ghi chú 1). | Tên mạch: "Ước lượng lợi thế: độ chệch và phương sai". Dòng dẫn (18 âm tiết): "Tổ hợp có trọng số các ước lượng lợi thế nhiều bước cân bằng độ chệch và phương sai." Thuật ngữ: "độ chệch"/"chệch" (bias), "phương sai" (variance) thay "lệch", "dao động" trên toàn deck; "lệch" chỉ giữ nghĩa hình học (khoảng cách). |
| 18 | L10-3-01 (Một bước thì lệch, cả lượt thì dao động) | (ảnh trang) "tiêu đề là văn nói" | Đã có trong bảng #11; tác giả nhắc lại trên trang. Tiêu đề khẩu ngữ ("thì … thì") và thiếu điều kiện: ước lượng một bước chỉ chệch khi critic sai. Thân trang: "Critic $\hat v=(1{,}4;1)$" xuất hiện không có lý do vì sao critic sai và sai ở đâu (#15); hình chỉ ghi $\hat v$, $v_\pi$ tại $s_B$. | Tiêu đề: "Với critic sai, ước lượng một bước bị chệch, ước lượng cả lượt có phương sai lớn" (hoặc tách: trang đặt vấn đề "Critic đánh giá thấp $s_B$" và trang kết quả). Thân: một dòng nêu critic học từ dữ liệu nên sai; ở đây đánh giá thấp $s_B$ một đơn vị; hình ghi $\hat v$ và $v_\pi$ ở cả hai trạng thái. |
| 19 | L10-3-01 (ví dụ critic sai) | (ảnh trang có bảng "Lượt | Xác suất | Một bước $\delta_0$") "ví dụ này cũng khó hiểu, các con số lấy ở đâu" | Trang không nói đang ước lượng gì ($A_\pi(s_A,1)=0{,}4$), vì sao chỉ xét lượt chọn 1 ở $s_A$, xác suất $\tfrac23$, $\tfrac13$ là $p_B$, $\hat v=(1{,}4;1)$ là giả định (critic đúng ở $s_A$, thấp ở $s_B$), $0{,}9\cdot1$ dùng $\hat v(s_B)$; dòng (ii) chỉ ghi $-0{,}5$; lợi thế đúng nằm ngoài bảng; cột "cả lượt" và kỳ vọng, độ chệch, phương sai hiện theo mảnh, không phép tính đầy đủ. | Dòng mở: "Ước lượng $A_\pi(s_A,1)=0{,}4$ từ một lượt bắt đầu bằng hành động 1 ở $s_A$; critic học từ ít dữ liệu: đúng ở $s_A$, thấp ở $s_B$ một đơn vị." Bảng: đường đi đầy đủ | xác suất ($p_B$, $1-p_B$) | $R_1$, $R_2$ | một bước $\delta_0=R_1+\gamma\hat v(s_B)-\hat v(s_A)$ | cả lượt $G_0-\hat v(s_A)$ với $G_0=R_1+\gamma R_2$; mỗi ô phép tính đủ. Ba dòng cuối: kỳ vọng ($-0{,}5$; $0{,}4$), độ chệch so với $0{,}4$ ($-0{,}9$; $0$), phương sai ($0$; $1{,}62$). |
| 20 | L10-4-01 | "văn nói" / "không rõ mục đích của slide" | Tiêu đề văn nói. Trang không nêu bài toán (ước lượng $J(\pi')$ từ lượt của $\pi$); câu hỏi nằm ở fragment cuối. $\pi'$ không rõ nguồn gốc, $p'_A=1$ không đạt được với $\theta$ hữu hạn (lặp lỗi #5); cặp $(\tfrac12;\tfrac23)$ và "tỉ lệ lượt tới $s_B$" $=p_A$ chưa giải thích; không nói vì sao nơi tới quan trọng. | Mở bằng bài toán; nêu nguồn $\pi'$ và tham số $\theta'$; bảng xác suất tới và xác suất chọn của hai chính sách kèm $J$; kết luận: dữ liệu cũ phân bố theo $\pi$. Tiêu đề học thuật. |
| 21 | L10-4-02 | "đưa ra khái niệm $A_\pi(s,\pi')$ đột ngột" / "Ý nghĩa của $J(\pi')-J(\pi)$, công thức đó từ đâu ra" | $A_\pi(s,\pi')$ ra không có vấn đề, không có ý nghĩa (lợi ích mỗi lần đổi một bước sang $\pi'$ rồi theo $\pi$). Bổ đề hiệu hiệu năng (ghi chú Bổ đề 10.19, có chứng minh 5 bước) hiện như công thức trần: không nhãn, không giả thiết, không ý nghĩa, không ý tưởng chứng minh. "Số lần $\pi'$ tới" thực ra là số lần thăm có chiết khấu ($0{,}9$ không phải số lần). Văn nói: "Lợi thế cũ chọn theo $\pi'$", "kiểm:", "Công thức đúng, nhưng…". Ghi chú: "lợi thế trung bình" → "kỳ vọng". | Tách 3 trang: (1) $A_\pi(s,\pi')$ từ câu hỏi "đổi một bước tại $s$ được bao nhiêu", tính qua $q_\pi$, $v_\pi$; (2) Bổ đề (hiệu hiệu năng) có giả thiết, Ý nghĩa, định nghĩa $\eta_{\pi'}(s)$; (3) Ý tưởng chứng minh (tổng lồng nhau); bảng ví dụ để sau. |
| 22 | L10-4-04, L10-4-05 (và L10-4-10) | "slide này, và slide sau đó cũng đột ngột đưa ra $\Delta J$, khai triển $J$ … rất khó theo dõi" | $\Delta J$, $\Delta\mathcal L$, $t$ không định nghĩa; đường $p_A=\frac{1+t}2$, $p_B=\frac{4-t}6$ không nói là đoạn từ $\pi$ tới $\pi'$; hai biểu thức theo $t$ không có phép thế; khẳng định "tiếp xúc" (Mệnh đề 10.22) không phát biểu, không chứng minh. Thứ tự ngược: trường hợp riêng (đường thẳng, 4-04) trước dạng tổng quát (khai triển, 4-05). Khai triển $J$ không có bước; ý chính "sai số = số lần tới thêm × lợi ích mỗi lần" chỉ nằm trong ghi chú người nói. Tiêu đề văn nói. | Suy sai số trực tiếp từ bổ đề trừ hàm thay thế: $\Delta J-\Delta\mathcal L=\sum_s(\eta_{\pi'}-\eta_\pi)(s)A_\pi(s,\pi')$, trên chuỗi $=(\gamma\Delta p_A)(3\Delta p_B)$; kiểm bằng khai triển $J$ có bước; phát biểu mệnh đề tiếp xúc như hệ quả; rồi mới thế đường $t$ và vẽ. |
| 23 | L10-4-06 | "phát biểu kiểu văn nói" | Định lý phát biểu bằng lời ("mức tăng hàm thay thế đoán trừ một phạt", "khoảng cách trung bình theo nơi chính sách cũ tới"), công thức chỉ nằm trong ghi chú người nói. "Giả thiết" sai loại (điều kiện áp dụng) và thiếu (MDP hữu hạn, cùng $P$, $\mu_0$, thưởng bị chặn, điều kiện hỗ trợ). Hằng số ghi $1/(1-\gamma)^2$ thay cho $2\gamma\chi/(1-\gamma)^2$. $D_{\mathrm{TV}}$ định nghĩa sau kết luận, không tên. Câu kết không có số trên mặt trang; không ý tưởng chứng minh. | Phát biểu theo Định lý 10.26 (công thức, đủ giả thiết, $D_{\mathrm{TV}}$ và $\nu^\pi$ định nghĩa trước); trang ý tưởng chứng minh từ sai số #22 + Bổ đề 10.25; trang số trên chuỗi (bước $(1;0{,}5)$: cận $-5{,}0$, thật $-0{,}05$; bước chỉ đổi $p_B$: cận dương khi $\Delta<0{,}056$). |
| 24 | L10-4-12 | "nên phát biểu dạng mệnh đề / bổ đề" | Bất đẳng thức Pinsker (ghi chú Mệnh đề 10.24(b)) và đẳng thức $D_{\mathrm{KL}}=\mathbb E_{a\sim\pi}[-\log\rho]$ là kết quả nhưng viết như câu thường, không nhãn, không giả thiết, không lý do. Hệ quả 10.27 (chặn cải thiện dạng KL trung bình), cầu nối sang miền tin cậy, không có trên trang. Lý do chọn KL ("tính được từ lượt cũ") không phân biệt: $D_{\mathrm{TV}}$ cũng tính được từ lượt cũ. Tiêu đề văn nói. Ví dụ KL $=+\infty$ phụ thuộc $p'_A=1$ (#20). | Trang định nghĩa KL + Nhận xét dạng tỉ số; Mệnh đề (Pinsker) có giả thiết, kết luận, Ý nghĩa; Hệ quả (chặn cải thiện theo KL trung bình) có ý tưởng chứng minh 2 bước; ví dụ số trên chuỗi theo phương án #20. |
| 25 | L10-4-03 | "định nghĩa, tiêu đề đang văn nói" / "các số liệu cũng khó theo dõi" | Câu "Hàm thay thế $\mathcal L$ giữ số lần tới của chính sách cũ, nên tính được từ lượt cũ" không phải định nghĩa: không định nghĩa $\mathcal L_\pi(\pi')$ mà chỉ cho hiệu, không nêu lý do thay. Tiêu đề văn nói. Bảng: cột $\eta_{\pi'}$ chép từ trang trước, cột tích với $\eta_{\pi'}$ bị bỏ nên "thật: $-0{,}05$" không có nguồn trong bảng; $0{,}9$ và $0{,}9\cdot0{,}5$ không có công thức ($\gamma p'_A$, $\gamma p_A$); tên cột "số lần … tới" sai đại lượng. Ký hiệu trang chiếu ($\eta$, không chuẩn hóa) khác ghi chú ($\nu$, $\frac1{1-\gamma}$; $\mathcal L_{\theta_{\mathrm{old}}}(\theta)$ lẫn $\mathcal L_\pi(\pi')$). | Định nghĩa đầy đủ $\mathcal L_\pi(\pi')=J(\pi)+\sum_s\eta_\pi(s)A_\pi(s,\pi')$ sau câu lý do (bổ đề cần lượt của $\pi'$); bảng cột đồng nhất: $A_\pi(s,\pi')$, $\eta_\pi(s)$, $\eta_{\pi'}(s)$ có công thức, hai cột tích, cột hiệu; dòng tổng $\Delta\mathcal L$, $\Delta J$, sai số; thống nhất một ký hiệu với ghi chú. |
| 26 | Mạch 5 (L10-5-00 … 5-08); thuật toán toàn bài | "mạch 5 chả hiểu bạn định làm gì luôn" / "mục đích của từng thuật toán không rõ" / "không có cả trình bày liệt kê thuật toán (cả actor-critic của các mạch trước)" / "các slide trình bày kiểu văn nói, không có mục đích rõ ràng, con số đưa ra cũng không hiểu lấy từ đâu" | Mạch không nêu bài toán (TRPO tốn kém mỗi bước; muốn dùng lại bộ đệm nhiều lần chỉ với gradient bậc một). Không có trang "Thuật toán." nào (actor–critic, TRPO, PPO chỉ có sơ đồ khung hoặc không có), không mục đích, đầu vào/đầu ra, tham số, thứ tự bước. Văn nói: lời mở "Chỉ chạy Adam…", "không thưởng thêm", "Phía bất lợi không bị cắt, gradient kéo về", "Quán tính của Adam…". Số: bộ đệm, critic $(1{,}4;1)$, $\widehat A$ với $\lambda=1$, $\rho$ theo $p'$, điểm cực đại, $J$, mốc cắt không có phép tính; 5-04 đổi sang bộ đệm khác ("ba mẫu đúng tần suất") không lý do; "Còn thiếu:" (nhãn không cho phép). | Dựng lại mạch 5 theo bài toán → hàm thay thế mẫu không ràng buộc (tính đủ) → trực giác (hàm thay thế chỉ tin được khi $\rho$ gần 1) → Định nghĩa mục tiêu cắt + bảng hai trường hợp → cùng bộ đệm có cắt (tính đủ) → Nhận xét giới hạn → Thuật toán PPO-Clip → so sánh. Thêm trang "Thuật toán." cho actor–critic (cuối mạch 2/3) và TRPO (mạch 4), mỗi trang mở bằng câu bài toán. |
| 27 | Mạch 6 (DPO); hình neo | "bỏ phần DPO vì sẽ có trong bài 13" / "bỏ DPO trong hình neo" | Quyết định phạm vi của tác giả. | Bỏ mạch 6 khỏi trang chiếu (tên bài, luận điểm, mục tiêu, Nội dung, Vấn đề trung tâm, tổng kết, bài tập về nhà); bỏ khối "phần thưởng"/thẻ "mạch 6" và cột mạch 6 trong mọi hình neo (`so-do-neo-*.svg`), bỏ `so-do-neo-m6-*`; số mạch còn 6. Phạm vi ghi chú §7, bài tập 10.18–10.21, GC-RL-18, BT-RL-10, P1 Mục 7: chốt khi tổng hợp. Đã ghi quyết định vào `NGUYEN-TAC-HOC-PHAN.md`. |
| 28 | Mạch tổng kết (L10-7-00 … 7-05, `so-do-neo-m7*.svg`) | "Mạch tổng kết không nên nói cụ thể ví dụ (các con số) mà cần rút ra kết luận định tính" | Hình neo cuối ghi số ví dụ (phương sai $0{,}69$; $0{,}20$; $0$; "đoán $+0{,}175$, thật $-0{,}05$"; "dừng ở $p=0{,}8$"); "Vấn đề trung tâm" mục 1 dùng số ($0{,}69\to0{,}20$). Thiếu bảng kết quả định tính `Kết quả | Giả thiết không được bỏ | Công thức hoặc thuật toán` và bảng so sánh phương pháp theo quy định học phần. Câu hỏi tự kiểm tra đều là phép tính trên ví dụ. Bài tập tổng hợp (7-03, 7-04) là ví dụ số. | Tổng kết chỉ phát biểu kết luận định tính kèm giả thiết: bảng kết quả, bảng phương pháp (REINFORCE, actor–critic, TRPO, PPO: quy tắc cập nhật, dữ liệu dùng, giữ bước gần bằng gì, bảo đảm), Vấn đề trung tâm dạng điều kiện; hình neo cuối chỉ ghi tên khối và công cụ. Câu hỏi tự kiểm tra hỏi khái niệm. Bài tập tổng hợp: đề xuất chuyển về cuối mạch PPO (cần tác giả chốt vì quy định học phần đặt một bài tập tổng hợp trong mạch kết). |

## Nhật ký trao đổi

Ghi theo thứ tự: lời tác giả (nguyên văn), rồi trả lời của điều phối viên (đầy đủ ý, giữ công thức). Bảng trên là bản tóm tắt để tổng hợp; phần này giữ lập luận.

### Trao đổi 1 — L10-1-02 (Tiên quyết và quy ước)

**Tác giả:** (gửi ảnh dòng "Nhắc lại: với hai hành động và tham số $\theta=(\theta_1;\theta_2)$, xác suất chọn hành động 1 là $p=\sigma(\theta_1-\theta_2)$, và $\psi(s,1)=(1-p)(1;-1)$, $\psi(s,2)=-p(1;-1)$.") "giải thích"

**Điều phối viên:**

1. Hàm điểm là $\psi(s,a)=\nabla_\theta\log\pi_\theta(a\mid s)$: hướng đổi $\theta$ làm xác suất chọn $a$ tăng nhanh nhất.
2. Softmax hai hành động: $p=\pi(1\mid s)=\dfrac{e^{\theta_1}}{e^{\theta_1}+e^{\theta_2}}=\dfrac1{1+e^{-(\theta_1-\theta_2)}}=\sigma(\theta_1-\theta_2)$. Chỉ hiệu $x=\theta_1-\theta_2$ quan trọng.
3. Tính $\psi(s,1)$: $\log\pi(1\mid s)=\log\sigma(x)$; $\frac{d}{dx}\log\sigma(x)=\frac{\sigma(1-\sigma)}{\sigma}=1-p$; $\nabla_\theta x=(1;-1)$; nhân lại được $(1-p)(1;-1)$.
4. Tính $\psi(s,2)$: $\log\pi(2\mid s)=\log(1-\sigma(x))$; đạo hàm theo $x$ là $\frac{-\sigma(1-\sigma)}{1-\sigma}=-p$; được $-p(1;-1)$.
5. Ý nghĩa: hướng $(1;-1)$ là tăng $\theta_1$, giảm $\theta_2$, tức làm hành động 1 dễ được chọn hơn. Chọn 1 thì đẩy về phía 1 với độ lớn $1-p$ (đã gần chắc thì đẩy ít); chọn 2 thì đẩy ngược với độ lớn $p$. Hai tọa độ luôn ngược dấu, nên deck chỉ theo dõi tọa độ $\theta_1$: $+(1-p)$ hoặc $-p$; tại $p=\tfrac12$ là $\pm\tfrac12$ (cột $\psi_t$ của ví dụ hành lang). Kỳ vọng $p(1-p)+(1-p)(-p)=0$, lý do trừ đường cơ sở không làm lệch gradient (mạch 2).

**Chẩn đoán:** mặt trang chỉ ghi "$\psi_t$ là hàm điểm" rồi đưa công thức; không có $\psi=\nabla_\theta\log\pi$, không có ý nghĩa hướng đẩy. Sinh viên quên Bài 9 không biết công thức từ đâu ra.

**Đề xuất:** thêm $\psi(s,a)=\nabla_\theta\log\pi_\theta(a\mid s)$ vào dòng "Ký hiệu"; một dòng ý nghĩa (chọn 1 đẩy về 1 mạnh $1-p$, chọn 2 đẩy ngược mạnh $p$).

### Trao đổi 2 — L10-1-03 (Ví dụ: hành lang ngắn (1))

**Tác giả:** (gửi ảnh trang) "mô tả đột ngột, tham số \theta, chính sách \pi hiện là gì ?"

**Điều phối viên:** Đúng; trang bắt đầu bằng phép tính mà chưa dựng tác tử. Ghi chú (Ví dụ 10.2) có đủ phần dựng, deck đã bỏ đi. Phần thiếu:

- Tham số $\theta=(\theta_1;\theta_2)$: điểm của "sang phải" và "sang trái", dùng chung cho mọi ô vì mọi ô có cùng đặc trưng $\phi(s,1)=(1;0)$, $\phi(s,2)=(0;1)$. Bắt đầu tại $\theta=(0;0)$.
- Chính sách: $\pi_\theta(1\mid s)=\sigma(\theta_1-\theta_2)=p$, giống nhau ở mọi ô (tác tử không biết mình ở ô nào, nên không thể "phải ở $s_1$, trái ở $s_2$"). Tại $\theta=(0;0)$: $p=\tfrac12$, mỗi bước tung đồng xu.
- Mục tiêu: $J=\mathbb E[G_0]$ = trừ số bước kỳ vọng tới đích; $J(p)=-\frac{2(2-p)}{p(1-p)}$, $J(\tfrac12)=-12$; gradient đúng $\nabla J=(2;-2)$: nên tăng $p$.
- Vì sao chỉ theo dõi $\theta_1$: hai tọa độ của $\psi$ luôn ngược dấu.

Thiếu những điều này, "Mọi ô: $p=\tfrac12$" và "Tọa độ $\theta_1$: $\psi_t=\pm\tfrac12$" là dữ kiện rơi từ trên xuống, và lời giải mất điểm chính: lượt này đẩy $p$ xuống trong khi gradient đúng đòi tăng $p$ (hiện tượng phương sai lớn mà mạch muốn cho thấy).

**Nguyên nhân gốc:** ví dụ dùng đối tượng trước khi giới thiệu (cùng lỗi với L10-1-02). Quy trình rà không bắt được vì vai "người thầy" và vai sinh viên đọc cả ghi chú nên tự lấp chỗ trống.

**Đề xuất:** (1) thêm trang dựng ví dụ trước trang này: hình hành lang; $\theta$ hai điểm dùng chung; $p=\sigma(\theta_1-\theta_2)$ giống mọi ô, $\theta=(0;0)\Rightarrow p=\tfrac12$; mục tiêu $J$, $J(\tfrac12)=-12$, gradient đúng $(2;-2)$. (2) Trang tính chỉ còn bảng và câu hỏi; lời giải thêm "lượt cho $-1$, gradient đúng cho $+2$: ngược chiều". (3) Rà cả bốn ví dụ chạy theo câu "trước phép tính đầu tiên đã dựng tham số, chính sách, mục tiêu chưa", bằng vai sinh viên chỉ xem ảnh slide. (4) Quy tắc mới TB24 (dựng ví dụ trước khi tính) và cập nhật quy trình.

### Trao đổi 3 — cách làm việc

**Tác giả:** "tôi sẽ đi một lượt các slide, trao đổi với bạn, sau đó bạn tổng hợp để sửa một thể"; "trong quá trình trao đổi, hãy ghi lại cả những ý kiến của tôi và thảo luận của bạn".

**Điều phối viên:** Không sửa deck cho tới khi tác giả nói xong. Mỗi góp ý: giải thích nếu được hỏi, chẩn đoán nguyên nhân gốc, ghi vào tệp này (bảng tóm tắt + nhật ký trao đổi). Khi xong: tổng hợp thành các loại lỗi và quy tắc mới để tác giả duyệt → sửa ghi chú nếu cần → storyboard → một editor sửa deck → rà lại (vai sinh viên chỉ xem ảnh) → kiểm cuối → commit.

### Trao đổi 4 — L10-1-04 (Ba lượt cho ba hướng cập nhật khác nhau)

**Tác giả:** (gửi ảnh trang: dòng "Nhắc lại" về $J(p)$; bảng Lượt | Hành động | Lợi tức $G_t$ | Phép tính $\widehat g_1$ với ba lượt (a), (b), (c)) "nên điền kết quả phép tính vào bảng luôn (song song với việc thể hiện trên đồ thị ở dưới)"

**Điều phối viên:** Đồng ý. Hiện bảng dừng ở biểu thức, kết quả chỉ nằm trên trục số bên dưới, nên sinh viên phải tự cộng hoặc nhìn qua lại giữa bảng và hình. Kết quả kiểm lại:

- (a) $\tfrac12(-3)-\tfrac12(-2)+\tfrac12(-1)=-1{,}5+1-0{,}5=-1$.
- (b) $-\tfrac12(-4)+\tfrac12(-3)-\tfrac12(-2)+\tfrac12(-1)=2-1{,}5+1-0{,}5=1$.
- (c) $\tfrac12(-5)+\tfrac12(-4)+\tfrac12(-3)-\tfrac12(-2)+\tfrac12(-1)=-2{,}5-2-1{,}5+1-0{,}5=-5{,}5$.

Sửa: thêm cột "$\widehat g_1$" với $-1$, $1$, $-5{,}5$; mỗi ô kết quả hiện cùng mảnh với chấm tương ứng trên trục số, để bảng và hình nói cùng một điều cùng lúc.

Ba điểm phụ trên cùng trang:
1. Dòng (c) viết gộp $\tfrac12(-5-4-3-1)-\tfrac12(-2)$, khác cách viết từng số hạng của (a), (b); sinh viên phải tự tìm bước nào là hành động 2. Nên viết từng số hạng theo thứ tự bước.
2. Cột $G_t$ ghi "$-4,\dots,-1$" và "$-5,\dots,-1$"; nên ghi đủ để dò từng số hạng.
3. Dòng "Nhắc lại" đưa $J(p)$, $J'=8$ và thừa số $p(1-p)$ mà chưa trang nào dựng; đó là phần của trang dựng ví dụ đề xuất ở #2. Trang này chỉ cần nhắc "gradient đúng có tọa độ $\theta_1$ bằng $2$".

**Quy tắc chung rút ra:** bảng tính luôn có cột kết quả; khi hình vẽ cùng số liệu, ô kết quả và phần hình tương ứng hiện cùng lúc.

### Trao đổi 5 — L10-1-04, công thức $J(p)$

**Tác giả:** (gửi ảnh dòng "Nhắc lại: $J(p)=-\frac{2(2-p)}{p(1-p)}$") "ngoài ra, công thức của J(p) cũng cần được derive"

**Điều phối viên:** Đồng ý; hiện $J(p)$ rơi từ trên xuống, và ghi chú cũng chưa dẫn nó với $p$ tổng quát (Ví dụ 10.2 chỉ phát biểu; §2 chỉ giải hệ Bellman tại $p=\tfrac12$). Phép dẫn:

Động lực: ở $s_1$, hành động 1 sang $s_2$, hành động 2 đứng yên; ở $s_2$ hai hành động đảo (1 về $s_1$, 2 sang $s_3$); ở $s_3$, hành động 1 tới đích, hành động 2 về $s_2$. Thưởng $-1$ mỗi bước, $\gamma=1$, đích có giá trị $0$. Viết $v_i=v_\pi(s_i)$:

$$\begin{aligned}v_1&=-1+p\,v_2+(1-p)\,v_1,\\v_2&=-1+p\,v_1+(1-p)\,v_3,\\v_3&=-1+p\cdot0+(1-p)\,v_2.\end{aligned}$$

1. Phương trình 1: $p\,v_1=-1+p\,v_2$, nên $v_1=v_2-\tfrac1p$.
2. Phương trình 3: $v_3=-1+(1-p)\,v_2$.
3. Thế vào phương trình 2: $v_2=-1+p\,v_2-1-(1-p)+(1-p)^2v_2$, tức $v_2\bigl[1-p-(1-p)^2\bigr]=-(3-p)$.
4. $1-p-(1-p)^2=(1-p)\,p$, nên $v_2=-\dfrac{3-p}{p(1-p)}$.
5. $J(p)=v_1=v_2-\dfrac1p=-\dfrac{(3-p)+(1-p)}{p(1-p)}=-\dfrac{2(2-p)}{p(1-p)}$.

Kiểm tại $p=\tfrac12$: $v_2=-\tfrac{2{,}5}{0{,}25}=-10$, $v_1=-12$, $v_3=-1+\tfrac12(-10)=-6$; khớp $v_\pi=(-12;-10;-6)$ ở §2 của ghi chú.

Đạo hàm: với $N=2-p$, $D=p(1-p)$, $J=-2N/D$, $J'=-2\,\dfrac{N'D-ND'}{D^2}=2\,\dfrac{D+N(1-2p)}{D^2}$. Tại $p=\tfrac12$: $1-2p=0$, $D=\tfrac14$, nên $J'=2\cdot\tfrac14\big/\tfrac1{16}=8$. Quy tắc dây chuyền: $\partial J/\partial\theta_1=J'(p)\cdot\partial p/\partial\theta_1=8\cdot p(1-p)=2$. Đỉnh: $J'=0\iff p^2-4p+2=0\iff p^*=2-\sqrt2\approx0{,}586$, $J(p^*)\approx-11{,}66$.

**Đề xuất:** sửa ghi chú trước (Ví dụ 10.2 dẫn $J(p)$ đầy đủ như trên). Deck: trong cụm dựng ví dụ (#2), một trang "Ví dụ: hành lang ngắn, tính $J(p)$" với hình hành lang ghi $p$, $1-p$ trên mũi tên, ba phương trình, mỗi dòng một bước khử, kiểm tại $p=\tfrac12$; trang kế: $J'(\tfrac12)=8$, $\partial p/\partial\theta_1=p(1-p)$, gradient đúng $(2;-2)$, đỉnh $p^*$. Trang ba lượt (L10-1-04) khi đó chỉ nhắc "gradient đúng có tọa độ $\theta_1$ bằng $2$".

**Quy tắc chung rút ra:** công thức dùng làm dữ kiện của ví dụ phải được dẫn (trên trang hoặc trang liền trước) khi sinh viên tự dẫn được bằng công cụ đã có; "Nhắc lại" chỉ dành cho kết quả của bài trước.

### Trao đổi 6 — dùng lẫn $J(p)$ và $(\theta_1;\theta_2)$

**Tác giả:** "hơn nữa, lúc thì dùng J(p), lúc lại dùng tham số \theta_1, \theta_2"

**Điều phối viên:** Đúng, có hai lỗi chồng nhau.

1. **Không có quy ước nối $\theta$ với $p$.** Thứ ta cập nhật là $\theta$, thứ ta đọc và vẽ là $p$, và $J$ phụ thuộc $\theta$ chỉ qua $p$. Deck không nói điều này lần nào, nên L10-1-04, 1-05 nhảy giữa $J(p)$, $J'=8$, "tọa độ $\theta_1$ của gradient" và "gradient $(2;-2)$ từ $\theta=(0;0)$, tức $p=\tfrac12$".
2. **Hai ví dụ dùng hai cách tham số hóa.** Hành lang dùng hai logit $\theta=(\theta_1;\theta_2)$, $p=\sigma(\theta_1-\theta_2)$; hai tọa độ luôn ngược dấu, nên deck phải thêm câu "chỉ theo dõi tọa độ $\theta_1$". Chuỗi hai trạng thái (mạch 2 trở đi, ghi chú dòng 473) dùng một logit mỗi trạng thái, $p_s=\sigma(\theta_s)$, $\psi(s,1)=1-p_s$, $\psi(s,2)=-p_s$. Sinh viên gặp hai quy ước cho cùng một việc.

**Đề xuất:**
- Hành lang dùng một tham số vô hướng $\theta$ (logit $\theta$ cho hành động 1, $0$ cho hành động 2), $p=\sigma(\theta)$, giống chuỗi hai trạng thái. Khi đó $\psi(s,1)=1-p$, $\psi(s,2)=-p$ (trang L10-1-02 bỏ vector $(1;-1)$), và $\dfrac{dJ}{d\theta}=J'(p)\cdot p(1-p)=8\cdot\tfrac14=2$, một số, không còn "tọa độ $\theta_1$".
- Các tổng $\widehat g$ giữ nguyên ($-1$; $1$; $-5{,}5$) vì $\psi=\pm\tfrac12$ vẫn vậy. Riêng bước cập nhật: với hai logit, $\theta_1-\theta_2$ đổi $2\alpha\widehat g$; với một logit, $\theta$ đổi $\alpha\widehat g$. Nhân đôi mọi bước học của hành lang (ví dụ $0{,}05\to0{,}1$, $0{,}1\to0{,}2$) thì mọi giá trị $p$, $J$ trên deck và trong ghi chú giữ nguyên; cần kiểm lại từng số.
- Quy ước nói một lần trên trang dựng ví dụ (#2): "ta cập nhật $\theta$ và đọc $p=\sigma(\theta)$; $J$ phụ thuộc $\theta$ qua $p$, nên viết $J(p)$ và $\frac{dJ}{d\theta}=J'(p)\,p(1-p)$". Mọi bảng cập nhật có đủ cột $\theta$, $p$, $J$; hình $J$ theo $p$ ghi rõ trục.
- Mạch 4 viết $J(\pi)$ (hàm của chính sách). Giữ, vì đó là ký hiệu tổng quát; trên ví dụ, chính sách xác định bởi $(p_A,p_B)$ nên $J(\pi)=J(p_A,p_B)$; nói một câu nối khi chuyển.
- Sửa ghi chú trước: khoảng 25 chỗ dùng $\theta_1$ hoặc $(2;-2)$ trong lecture-note.md, 1 chỗ trong exercises.md (Bài tập 10.10 dùng hành lang).

**Quy tắc chung rút ra:** mỗi bài một cách tham số hóa cho mọi ví dụ; quan hệ giữa tham số được cập nhật và đại lượng được vẽ hoặc đọc (ở đây $\theta$ và $p$) nói rõ một lần, và mọi bảng mang cả hai.

### Trao đổi 7 — L10-2-00, dòng dẫn mạch 2

**Tác giả:** (gửi ảnh trang tiêu đề mạch: "2. So lợi tức với giá trị của trạng thái" / "Một nửa số lượt trên chuỗi hai trạng thái đẩy chính sách sai hướng.") "câu tóm tắt tối nghĩa, người đọc (sinh viên) làm sao hiểu được"

**Điều phối viên:** Đúng. Câu có ba chỗ sinh viên không thể hiểu khi chưa học mạch:

1. "chuỗi hai trạng thái": ví dụ chỉ được giới thiệu ở trang kế.
2. "một nửa số lượt": con số rút từ bảng tính chưa thấy (lượt chọn hành động 2 ở $s_A$, xác suất $\tfrac12$, có $G_0=1$, $\psi_A=-0{,}5$, kéo $p_A$ xuống trong khi gradient đúng theo $\theta_A$ bằng $+0{,}2$).
3. "sai hướng": không nói so với hướng nào.

Hơn nữa câu nêu triệu chứng của một ví dụ, không nêu ý chính của mạch. Ý chính là: khi mọi lợi tức đều dương, REINFORCE tăng xác suất cả hành động kém; sửa bằng cách so lợi tức với mức thường đạt ở trạng thái đó (giá trị của trạng thái).

Câu đề xuất (19 âm tiết): "Lợi tức chỉ cho biết hành động tốt hay kém khi so với mức thường đạt ở trạng thái đó."

Năm dòng dẫn còn lại cùng lỗi: mạch 3 "Critic học dở thì đánh giá một bước bị lệch, còn lợi tức cả lượt thì dao động." (critic chưa được giới thiệu); mạch 4 "Bước lớn chỉ an toàn khi đánh giá được chính sách mới trước khi chạy nó."; mạch 5 "Chỉ chạy Adam trên lượt cũ mà chính sách mới vẫn ở gần chính sách cũ." (câu cụt, khó hiểu); mạch 6 "Không có phần thưởng, chỉ có người chọn câu trả lời tốt hơn."; mạch 7 "Ba khối đã sửa của vòng cập nhật gom lại các câu trả lời của bài." ("ba khối" chỉ có nghĩa với ai nhớ sơ đồ neo). Đề xuất viết lại cả sáu cùng một lượt khi tổng hợp.

**Nguyên nhân gốc:** quy tắc cho dòng dẫn (≤ 25 âm tiết, nêu điều sinh viên biết sau mạch, không lặp mẫu câu) được kiểm theo hình thức (đếm âm tiết, so mẫu câu) mà không kiểm câu có hiểu được với người chưa học mạch không. Cùng họ với lỗi câu bìa (NT11): chỉ dùng từ sinh viên có trước khi học.

**Quy tắc chung rút ra:** dòng dẫn mạch là câu ý chính của mạch, đọc hiểu được trước khi học mạch: không nhắc ví dụ, không con số, không thuật ngữ mạch đó mới giới thiệu.

### Trao đổi 8 — L10-2-01 (Ví dụ: chuỗi hai trạng thái (1))

**Tác giả:** (gửi ảnh trang: hình chuỗi có chú thích $v_\pi(s_A)=\tfrac12\cdot0{,}9\cdot2+\tfrac12\cdot1=1{,}4$, $v_\pi(s_B)=\tfrac23\cdot3=2$, cung đỏ "thưởng 1 < mức thường có 1,4"; bên phải $p_A$, $p_B$, $J$, gradient; bảng ba loại lượt với $G_0$, $\psi_A$, $G_0\psi_A$, dòng "trung bình; phương sai: $0{,}2$ (= gradient đúng); $0{,}69$") "tôi đọc mà không hiểu gì"

**Điều phối viên:** Trang này dồn tám thứ mới vào một khung, không thứ nào được dựng:

1. **Môi trường chỉ có hình, không lời.** Không nói xuất phát ở $s_A$; luật chuyển phải tự đọc từ mũi tên: ở $s_A$, hành động 1 sang $s_B$ thưởng $0$, hành động 2 kết thúc thưởng $1$; ở $s_B$, hành động 1 kết thúc thưởng $3$, hành động 2 kết thúc thưởng $0$. $\gamma=0{,}9$ chỉ xuất hiện trong tiêu đề cột.
2. **Tham số hóa** $p_s=\sigma(\theta_s)$, mỗi trạng thái một tham số, xuất hiện không giới thiệu; $p_B=\tfrac23$ không lý do ($\theta_B=\log2$).
3. **$J=2{,}7p_Ap_B+1-p_A$ không được dẫn.** Dẫn: với xác suất $p_Ap_B$ đi $1,1$, $G_0=0{,}9\cdot3=2{,}7$; với $p_A(1-p_B)$ đi $1,2$, $G_0=0$; với $1-p_A$ đi $2$, $G_0=1$. Cộng lại: $J=2{,}7p_Ap_B+1-p_A=0{,}9+0{,}5=1{,}4$.
4. **Gradient**: $\frac{\partial J}{\partial\theta_A}=\frac{\partial J}{\partial p_A}\cdot\frac{dp_A}{d\theta_A}=(2{,}7p_B-1)\cdot p_A(1-p_A)=(1{,}8-1)\cdot\tfrac14=0{,}2$. Số $0{,}8$ và hai thừa số không được giải thích; ý nghĩa ($0{,}2>0$: nên tăng $p_A$, vì ở $s_A$ hành động 1 cho trung bình $2{,}7\cdot\tfrac23=1{,}8$, hơn $1$ của hành động 2) không có.
5. **Giá trị $v_\pi(s_A)=1{,}4$, $v_\pi(s_B)=2$ in sẵn trên hình**, trước khi giá trị trạng thái là chủ đề; dòng đỏ "thưởng 1 < mức thường có 1,4" là kết luận của cả mạch, in trước khi vấn đề được đặt.
6. **Bảng**: tiêu đề "Hành động ở $s_A$, $s_B$" với dòng "$2$" (lượt kết thúc ngay) khó đọc; $\psi_A=\pm0{,}5$ không nhắc $\psi=1-p_A$ hoặc $-p_A$.
7. **Trung bình và phương sai không có phép tính**: $\tfrac13\cdot1{,}35+\tfrac16\cdot0+\tfrac12\cdot(-0{,}5)=0{,}45-0{,}25=0{,}2$; phương sai $\tfrac13\cdot1{,}35^2+\tfrac12\cdot0{,}5^2-0{,}2^2=0{,}6075+0{,}125-0{,}04=0{,}6925$.
8. **Ý chính của trang chỉ nằm trong ghi chú người nói**: hành động 2 ở $s_A$ cho $1$, kém mức thường có $1{,}4$, nhưng $G_0=1>0$ nên REINFORCE vẫn tăng xác suất của nó; nghĩa của dấu $-0{,}5$ (kéo $p_A$ xuống, tức tăng xác suất hành động 2) không được nói trên trang.

**Đề xuất:** tách thành chuỗi trang, mỗi trang một bước, mỗi bước có phép tính viết đủ:

- (a) **Dựng chuỗi**: hình sạch (không chú thích giá trị, không chữ đỏ) + lời: xuất phát $s_A$; hành động, thưởng; $\gamma=0{,}9$; mỗi trạng thái một tham số, $p_s=\sigma(\theta_s)$ (cùng quy ước với hành lang, #5); đang xét $p_A=\tfrac12$, $p_B=\tfrac23$.
- (b) **Tính $J$ và gradient**: bảng ba loại lượt (đường đi, xác suất, $G_0$) → $J=1{,}4$; công thức $J$ đọc ra từ chính bảng; gradient theo $\theta_A$ với hai thừa số; $0{,}2>0$: nên tăng $p_A$.
- (c) **REINFORCE trên từng loại lượt**: thêm cột "đẩy $p_A$" (lên / đứng yên / xuống); trung bình viết phép tính, bằng $0{,}2$.
- (d) **Đặt vấn đề**: lượt chọn hành động 2 cho $1$, kém $1{,}8$ của hành động 1, mà vẫn kéo $p_A$ xuống, vì mọi lợi tức đều dương; câu hỏi: so với mức nào thì biết hành động tốt hay kém. Từ đây mới đưa $v_\pi(s_A)=1{,}4$.
- Phương sai $0{,}69$ chuyển sang trang so sánh các hệ số (cùng chỗ với $0{,}20$ khi có đường cơ sở).

**Nguyên nhân gốc:** trang được viết như bản tóm tắt của Ví dụ 10.6 trong ghi chú, không như một chuỗi phát triển; quy tắc "mỗi mạch một ví dụ" bị hiểu thành "một trang ví dụ". Kiểm mật độ đếm âm tiết, bỏ qua công thức và bảng, nên trang dày công thức vẫn qua. Vai người thầy và vai sinh viên đọc ghi chú nên không thấy chỗ trống.

**Quy tắc chung rút ra:** mỗi trang chỉ thêm một hoặc hai đối tượng mới (một môi trường, một công thức, một bảng); đếm đối tượng mới, không chỉ đếm âm tiết. Ý chính của trang phải nằm trên mặt trang, không chỉ trong ghi chú người nói. Không in sẵn kết luận lên hình trước khi đặt vấn đề.

### Trao đổi 9 — dùng chuỗi hai trạng thái từ đầu

**Tác giả:** (giữa lúc điều phối viên đang ghi Trao đổi 8) "sao không dùng lại ví dụ này ở phía trước, để đỡ mất công giải thích nhiều ví dụ"

**Điều phối viên:** Nên làm vậy. Chuỗi hai trạng thái đã là ví dụ chạy của mạch 2–5 (đường cơ sở; critic $(1{,}4;1)$ và GAE; hàm thay thế và bước tới $(1;0{,}5)$; bộ đệm hai lượt của PPO). Chỉ mạch 1 dùng hành lang, và chính hành lang gây ra ba góp ý trước: dựng đột ngột (#2), $J(p)$ không dẫn (#4), hai logit khác quy ước (#5). Dùng chuỗi từ đầu thì dựng môi trường một lần, $J$ dẫn trong ba dòng từ bảng ba loại lượt (không cần giải hệ Bellman), một quy ước $p_s=\sigma(\theta_s)$ cho cả bài.

Mạch 1 trên chuỗi, kiểm số:
- **Vấn đề 1 (ước lượng dao động):** ba loại lượt cho $\widehat g_A=1{,}35$; $0$; $-0{,}5$ với xác suất $\tfrac13$, $\tfrac16$, $\tfrac12$; trung bình $0{,}2$ đúng bằng gradient, nhưng một nửa xác suất cho ước lượng ngược dấu. Đây đúng là bảng của L10-2-01, chuyển lên mạch 1.
- **Vấn đề 2 (bước dài làm $J$ giảm):** điểm khác. Trên chuỗi, đi theo gradient đúng không bao giờ làm $J$ giảm, vì $J$ đạt cực đại ở góc $p_A=p_B=1$ (kiểm: $\alpha=1,5,20$ cho $J=1{,}53;\,2{,}04;\,2{,}67$). Hình "vượt đỉnh" của hành lang không có bản tương ứng. Thay bằng hai hiện tượng thật trên chuỗi:
  - bước dài theo ước lượng của một lượt: lượt "chọn 2" ($\widehat g_A=-0{,}5$, $\widehat g_B=0$) với $\alpha=2$ đưa $p_A$ về $0{,}27$, $J$ từ $1{,}4$ xuống $1{,}22$; với $\alpha=1$, $J=1{,}30$. Lượt này có xác suất $\tfrac12$.
  - bước tới $(p_A;p_B)=(1;0{,}5)$: $J=1{,}35<1{,}4$ dù hàm thay thế dựng từ dữ liệu cũ báo tăng $0{,}175$ (đã có ở mạch 4). Hiện tượng này là động lực thật của miền tin cậy.
- **Mất gì:** hình đường cong $J(p)$ có đỉnh ở trong và bước theo gradient đúng vượt đỉnh; ví dụ kinh điển của Sutton và Barto (Ví dụ 13.1). Theo tôi mất này nhỏ hơn cái được, vì vấn đề 2 trên chuỗi dẫn thẳng tới mạch 4–5 bằng cùng số liệu.

**Ghi chú phải sửa trước:** §1 dựng chuỗi hai trạng thái (hiện dựng ở §2, Ví dụ 10.6); Ví dụ 10.2 (hành lang) có thể giữ trong ghi chú làm ví dụ bổ sung hoặc bỏ, tác giả quyết; Bài tập 10.10 dùng hành lang có thể giữ.

**Cần tác giả quyết:** (a) bỏ hành lang khỏi deck; (b) vấn đề 2 của mạch 1 dùng hai hiện tượng trên chuỗi như trên; (c) ghi chú giữ hay bỏ Ví dụ 10.2.

**Quy tắc chung rút ra:** một ví dụ chạy cho cả bài khi một môi trường đủ cho mọi hiện tượng; thêm ví dụ thứ hai chỉ khi có hiện tượng ví dụ thứ nhất không thể hiện được, và ghi lý do trong storyboard.

### Trao đổi 10 — quyết định một ví dụ chung

**Tác giả:** "ghi chú giữ vẫn được, nhưng nên dùng 1 ví dụ chung cho nhiều mạch để đỡ công dựng, lựa chọn ví dụ, con số để thể hiện được nhiều ý (dao động lớn, bước dài giảm J)"

**Điều phối viên:** Ghi nhận quyết định: deck dùng một ví dụ chung; ghi chú giữ hành lang làm ví dụ bổ sung.

Ràng buộc toán khi chọn số: trên chuỗi hai trạng thái với một tham số mỗi trạng thái, $J=1+p_A\,(\gamma\,v_B-1)$ và $v_B$ tăng dọc tia gradient, nên đi theo gradient đúng thì $J$ không bao giờ giảm (kiểm: $\alpha=1,5,20$ cho $J=1{,}53;\,2{,}04;\,2{,}67$). Muốn có "vượt đỉnh" theo gradient đúng phải có tham số dùng chung giữa các trạng thái (như hành lang), tức đổi cả ví dụ và tính lại mọi số của mạch 2–5.

Nhưng hiện tượng mà TRPO và PPO thật sự xử lý không phải vượt đỉnh theo gradient đúng; đó là bước dài dựa trên ước lượng nhiễu hoặc trên dữ liệu của chính sách cũ. Chuỗi hiện có thể hiện cả hai:
- Bước dài theo ước lượng của một lượt: lượt "chọn 2" (xác suất $\tfrac12$) cho $\widehat g=(-0{,}5;\,0)$; $\alpha=1$: $J=1{,}30$; $\alpha=2$: $p_A=0{,}27$, $J=1{,}22$; bước càng dài $p_A\to0$, $J\to1$ (giảm $0{,}4$).
- Đánh giá bằng dữ liệu cũ: bước tới $(1;\,0{,}5)$, hàm thay thế báo tăng $0{,}175$, $J$ thật giảm $0{,}05$ (mạch 4).
- Mạch 5 khép vòng trên đúng con số đó: bộ đệm hai lượt có lợi thế sai dấu, không cắt thì về $(0;1)$, $J$ giảm $0{,}4$; có cắt thì $J=1{,}392$, giảm $0{,}008$.

**Đề xuất (phương án A):** giữ chuỗi và các số hiện có (vai toán đã kiểm cho mạch 2–5); dựng chuỗi ở mạch 1; mạch 1 nêu hai vấn đề trên chuỗi như trên. Mạch 6 (so sánh của người): dùng trạng thái $s_B$ làm "hai câu trả lời", vì ví dụ DPO hiện có $\pi_{\mathrm{ref}}=(\tfrac23;\tfrac13)$ trùng $p_B=\tfrac23$: "giả sử không biết thưởng ở $s_B$, chỉ biết người chọn". Khi đó cả sáu mạch dùng một môi trường. Phương án B (thiết kế lại ví dụ có tham số dùng chung để có vượt đỉnh) không đề xuất vì phải tính lại toàn bộ.

### Trao đổi 11 — L10-2-02 (Trừ $v_\pi$ giữ trung bình, giảm dao động)

**Tác giả:** (gửi ảnh trang: "Hệ số mới: lợi tức $G_t$ trừ đường cơ sở (baseline) $b(S_t)$, ở đây $b(S_t)=v_\pi(S_t)$"; bảng REINFORCE và "trừ $v_\pi$: $(G_0-1{,}4)\psi_A$" với $0{,}65$; $-0{,}7$; $0{,}2$; trung bình, phương sai $0{,}2;0{,}69$ và $0{,}2;0{,}20$; xác suất tọa độ $\theta_A$ âm $\tfrac12$ và $\tfrac16$) "slide này đưa việc trừ v_\pi một cách đột ngột, không có lý do, hay trực quan gì cả"

**Điều phối viên:** Đúng. Trang mở bằng công cụ trước lý do, và tiêu đề phát biểu kết quả trước khi có vấn đề. Phần thiếu:

1. **Lý do.** $G_0$ một mình chỉ nói "dương thì tăng"; ở chuỗi mọi lợi tức $\ge0$, nên lượt "chọn 2" ($G_0=1$) vẫn tăng xác suất hành động 2 dù kém. Câu hỏi đúng là "tốt hơn hay kém hơn mức thường đạt ở $s_A$".
2. **Mức thường đạt** là trung bình lợi tức từ $s_A$ theo chính sách hiện tại, tức $v_\pi(s_A)$: hành động 1 cho trung bình $0{,}9\cdot v_\pi(s_B)=0{,}9\cdot2=1{,}8$ (với $v_\pi(s_B)=\tfrac23\cdot3=2$), hành động 2 cho $1$; $v_\pi(s_A)=\tfrac12\cdot1{,}8+\tfrac12\cdot1=1{,}4$. Trang hiện đưa $1{,}4$ vào công thức mà không nói từ đâu.
3. **Trực quan:** trục số với ba lợi tức $0$, $1$, $2{,}7$ và vạch $1{,}4$; bên phải vạch là "tốt hơn thường" (đẩy lên), bên trái là "kém hơn thường" (đẩy xuống). Hệ số mới $G_0-1{,}4$ là khoảng cách có dấu tới vạch.
4. **Đọc bảng:** lượt "chọn 2": $1-1{,}4=-0{,}4$, nhân $\psi_A=-0{,}5$ được $+0{,}2$: nay kéo $p_A$ lên, đúng hướng. Lượt "1, 2": $0-1{,}4=-1{,}4$, được $-0{,}7$: hành động 1 bị phạt vì xui ở $s_B$; đây là phần dao động còn lại, xác suất $\tfrac16$ (thay cho $\tfrac12$).
5. **Vì sao trung bình không đổi:** phần bị trừ là $1{,}4\,\psi_A$, và $\psi_A$ có trung bình $0$ ở $s_A$: $\tfrac12\cdot0{,}5+\tfrac12\cdot(-0{,}5)=0$. Trang này không nói; trang ý tưởng chứng minh (L10-2-05) nói sau ba trang.
6. **Phương sai** $0{,}69\to0{,}20$ không có phép tính: $\tfrac13\cdot0{,}65^2+\tfrac16\cdot0{,}7^2+\tfrac12\cdot0{,}2^2-0{,}2^2=0{,}1408+0{,}0817+0{,}02-0{,}04=0{,}2025$. Lý do giảm: hệ số mới nằm quanh $0$, lớn nhất $1{,}4$ thay cho $2{,}7$.

**Đề xuất:** chuỗi trang (a) trực quan trục số và cách tính $1{,}4$; (b) quy tắc "hệ số $=G_0-1{,}4$" và bảng có cột dấu, cột "đẩy $p_A$"; (c) trung bình giữ $0{,}2$ vì $\psi$ trung bình $0$ (đưa ý tưởng chứng minh lên ngay đây); (d) so phương sai có phép tính. Tên "đường cơ sở (baseline)" và ký hiệu $b(S_t)$ đặt sau trực quan, khi đã có ví dụ. Tiêu đề trang đầu nêu vấn đề, không nêu kết quả.

**Nguyên nhân gốc:** trang được viết theo thứ tự "công cụ → kết quả" của một bản tóm tắt; quy tắc vấn đề trước công cụ (hành trình khái niệm: vấn đề → trực quan → ví dụ → phát biểu) không được kiểm trên từng trang. Lý do và trực quan nằm trong ghi chú người nói và ghi chú bài giảng.

**Quy tắc chung rút ra:** mỗi công cụ mới xuất hiện trên mặt trang theo thứ tự: vấn đề trên ví dụ → ý trực quan (có hình) → công cụ và tên gọi → kết quả có phép tính. Tiêu đề trang đầu của cụm nêu vấn đề.

### Trao đổi 12 — văn nói trong tiêu đề (L10-2-04)

**Tác giả:** (gửi ảnh tiêu đề "Trừ một mức của trạng thái không đổi trung bình") "Câu kiểu này là văn nói, cần văn học thuật"

**Điều phối viên:** Đúng. Tiêu đề dùng động từ thường thay cho thuật ngữ đã có: "trừ một mức" (đường cơ sở), "của trạng thái" (chỉ phụ thuộc trạng thái), "không đổi trung bình" (không làm chệch, giữ nguyên kỳ vọng). Bản học thuật: **"Đường cơ sở chỉ phụ thuộc trạng thái không làm chệch ước lượng gradient"**.

Cùng kiểu, khoảng 15 tiêu đề khác; đề xuất bản học thuật:

| Trang | Hiện tại | Đề xuất |
|---|---|---|
| L10-2-02 | Trừ $v_\pi$ giữ trung bình, giảm dao động | Đường cơ sở $v_\pi$ giữ nguyên kỳ vọng và giảm phương sai |
| L10-3-01 | Một bước thì lệch, cả lượt thì dao động | Ước lượng một bước bị chệch, ước lượng cả lượt có phương sai lớn |
| L10-4-01 | Bước lớn đổi cả nơi chính sách tới | Bước lớn làm thay đổi phân bố trạng thái |
| L10-4-02 | Hiệu $J$ tính theo nơi chính sách mới tới | Hiệu $J$ là kỳ vọng của lợi thế theo phân bố trạng thái của chính sách mới |
| L10-4-03 | Hàm thay thế dùng nơi chính sách cũ tới | Hàm thay thế dùng phân bố trạng thái của chính sách cũ |
| L10-4-05 | Bước gần thì hàm thay thế sai ít | Sai số của hàm thay thế nhỏ khi bước nhỏ |
| L10-4-08 | Gradient tự nhiên dồn bước về $\theta_B$ | Gradient tự nhiên tập trung bước cập nhật vào $\theta_B$ |
| L10-4-12 | KL đo khoảng cách bằng lượt cũ | Ước lượng KL từ các lượt của chính sách cũ |
| L10-5-01 | Bộ đệm hai lượt đẩy chính sách đi xa và sai hướng | Lợi thế ước lượng sai dấu làm chính sách lệch xa |
| L10-5-02 | Mục tiêu cắt không cho lợi khi đi quá xa | Mục tiêu cắt bỏ lợi ích khi tỉ số xác suất ra ngoài $[1-\epsilon,1+\epsilon]$ |
| L10-5-05 | Có cắt thì $J$ gần như không đổi | Với phép cắt, $J$ chỉ giảm $0{,}008$ |
| L10-6-03 | Phạt KL chọn một điểm giữa tham lam và $\pi_{\mathrm{ref}}$ | Phạt KL cân bằng phần thưởng và độ gần $\pi_{\mathrm{ref}}$ |

(Danh sách đề xuất; trong lượt sửa sẽ rà lại toàn bộ tiêu đề, dòng dẫn và thân trang, và các đề xuất phải khớp với cách dựng mới của các mạch.)

**Nguyên nhân gốc:** VP25 và các quy tắc TB ("chỉ dùng từ sinh viên đã có") bị hiểu thành "tránh thuật ngữ", nên người viết diễn giải bằng lời nói thường ("nơi chính sách tới" thay "phân bố trạng thái"). Cách đúng: định nghĩa thuật ngữ một lần, rồi dùng thuật ngữ đó bằng văn học thuật; từ đơn giản chỉ thay cho thuật ngữ chưa được định nghĩa ở thời điểm đó.

**Quy tắc chung rút ra:** tiêu đề và thân trang dùng văn học thuật: thuật ngữ chuẩn đã định nghĩa, câu khẳng định đầy đủ chủ ngữ–vị ngữ, không dùng cấu trúc khẩu ngữ ("thì … thì", "đi quá xa", "cho lợi"). Thêm vai rà văn phong học thuật vào quy trình.

### Trao đổi 13 — "trung bình" → "kỳ vọng"

**Tác giả:** "trung bình --> kì vọng"

**Điều phối viên:** Đồng ý. Mặt trang dùng "trung bình" 36 lần và "kỳ vọng" 0 lần, trong khi ghi chú dùng "kỳ vọng" 71 lần; deck vừa lệch thuật ngữ của ghi chú, vừa gộp hai khái niệm khác nhau:

- **Kỳ vọng** của biến ngẫu nhiên: "$\mathbb E[\widehat g]=\nabla J$", "hàm điểm có kỳ vọng $0$ tại mỗi trạng thái", "hệ số $G_t-v_\pi(S_t)$ có kỳ vọng có điều kiện bằng $A_\pi(S_t,A_t)$", "$\delta_t$ có kỳ vọng bằng lợi thế", "KL kỳ vọng theo phân bố trạng thái của chính sách cũ" (L10-1-02, 1-04, 2-01…2-08, 4-06, 4-07, 5-08, 7-02).
- **Trung bình mẫu**, trung bình cộng trên một tập hữu hạn: trung bình của hai lượt ở L10-3-04 ($(2\cdot0{,}94-1{,}22)/3$), hàm thay thế mẫu trên bộ đệm ở L10-5-01, L10-4-11. Giữ "trung bình", viết rõ "trung bình trên $N$ mẫu" hoặc "trung bình trên bộ đệm".

Dòng bảng "trung bình; phương sai" thành "kỳ vọng; phương sai". Chính tả theo tham số P2 của học phần: "kỳ vọng".

**Quy tắc chung rút ra:** "kỳ vọng" cho biến ngẫu nhiên, "trung bình (trên … mẫu)" cho tập hữu hạn; deck dùng đúng thuật ngữ của ghi chú.

### Trao đổi 14 — L10-2-06 (Hệ số trung bình là lợi thế)

**Tác giả:** (gửi ảnh trang: hình chuỗi với nhãn "2: 1 − 1,4 = −0,4", "1: 1,8 − 1,4 = +0,4", "1: 3 − 2 = +1", "2: 0 − 2 = −2"; "Định nghĩa. Lợi thế (advantage) của hành động $a$ tại $s$ đo hành động đó tốt hơn mức thường có bao nhiêu: $A_\pi(s,a)=q_\pi(s,a)-v_\pi(s)$.") "tiêu đề như văn nói; Định nghĩa cũng như văn nói"

**Điều phối viên:** Đúng.

1. **Tiêu đề** "Hệ số trung bình là lợi thế": khẩu ngữ, và mơ hồ ("hệ số trung bình" đọc như "hệ số ở mức trung bình"). Ý muốn nói là kỳ vọng có điều kiện của hệ số $G_t-v_\pi(S_t)$ bằng lợi thế. Đề xuất: "Hàm lợi thế và gradient dạng lợi thế".
2. **Định nghĩa** bị viết lại bằng lời nói: "đo hành động đó tốt hơn mức thường có bao nhiêu" trộn diễn giải vào phát biểu và bỏ giả thiết. Ghi chú đã có bản học thuật (Định nghĩa 10.4). Đề xuất mặt trang:
   - "**Định nghĩa.** Cho chính sách $\pi$ với giá trị trạng thái $v_\pi$ và giá trị hành động $q_\pi$. Hàm lợi thế (advantage function) của $\pi$ là $A_\pi(s,a)=q_\pi(s,a)-v_\pi(s)$."
   - "**Ý nghĩa:** $A_\pi(s,a)>0$ khi thực hiện $a$ tại $s$ rồi theo $\pi$ cho lợi tức kỳ vọng lớn hơn $v_\pi(s)$."
3. **Phần sau trên cùng trang** (hiện theo mảnh): "Hệ số $G_t-v_\pi(S_t)$ có trung bình $A_\pi(S_t,A_t)$, nên gradient chỉ cần lợi thế" và "Còn thiếu: $q_\pi$ và $v_\pi$ chưa biết." cùng kiểu. Đề xuất: "**Mệnh đề.** $\mathbb E[G_t-v_\pi(S_t)\mid S_t,A_t]=A_\pi(S_t,A_t)$; do đó $\nabla J=\mathbb E\bigl[\sum_t\gamma^tA_\pi(S_t,A_t)\psi_t\bigr]$." và "**Lưu ý:** $q_\pi$, $v_\pi$ chưa biết; cần ước lượng $A_\pi$ từ dữ liệu." ("Còn thiếu:" không thuộc danh sách nhãn được phép.)
4. **Hình**: nhãn "1: 1,8 − 1,4 = +0,4" dùng $q_\pi(s_A,1)=1{,}8$ và $v_\pi(s_A)=1{,}4$ mà không ghi tên; $1{,}8=0{,}9\cdot v_\pi(s_B)=0{,}9\cdot2$ không được tính. Đề xuất nhãn dạng "$q=1{,}8$, $A=+0{,}4$" và một dòng tính $q_\pi$ trên trang (hoặc ở trang trực quan của đường cơ sở, #10, nơi $1{,}8$ và $1{,}4$ đã được tính).

**Nguyên nhân gốc:** yêu cầu "đưa ra cách hiểu dễ dàng" bị hiểu thành viết lại phát biểu hình thức bằng lời thường. Cách đúng: phát biểu (Định nghĩa, Mệnh đề, Định lý) giữ dạng học thuật như ghi chú, đủ giả thiết, rút gọn nếu cần; cách hiểu dễ nằm ở trực quan và ví dụ trước phát biểu, và ở dòng "Ý nghĩa:" sau phát biểu, không trộn vào phát biểu.

**Quy tắc chung rút ra:** khối Định nghĩa/Mệnh đề/Định lý trên trang chiếu lấy từ phát biểu của ghi chú (có thể rút gọn, không diễn giải lại); diễn giải tách sang "Ý nghĩa:". Tiêu đề trang định nghĩa là tên khái niệm; chỉ trang kết quả mới dùng tiêu đề dạng khẳng định, và khẳng định đó phải là văn học thuật.

### Trao đổi 15 — chứng minh gradient dạng lợi thế (L10-2-06)

**Tác giả:** (gửi ảnh "Hệ số $G_t-v_\pi(S_t)$ có trung bình $A_\pi(S_t,A_t)$, nên gradient chỉ cần lợi thế: $\nabla J=\mathbb E\bigl[\sum_t\gamma^tA_\pi(S_t,A_t)\psi_t\bigr]$.") "khẳng định này cần chứng minh (hệ quả của mệnh đề đường cơ sở)"

**Điều phối viên:** Đúng. Trang nêu kết quả chính bằng một chữ "nên"; chữ "có trung bình" còn che mất điều kiện thật (kỳ vọng có điều kiện theo $(S_t,A_t)$, dùng tính Markov). Ghi chú có chứng minh (Mệnh đề 10.5(b), Bước 2); trang chiếu cần phát biểu và ý tưởng chứng minh.

**Hệ quả (gradient dạng lợi thế).** Dưới giả thiết của mệnh đề đường cơ sở, $\nabla J=\mathbb E\bigl[\sum_t\gamma^tA_\pi(S_t,A_t)\,\psi_t\bigr]$.

**Ý tưởng chứng minh** ($H_t$ là lịch sử tới $S_t$):

1. Mệnh đề đường cơ sở với $b=v_\pi$: $\nabla J=\sum_t\gamma^t\,\mathbb E\bigl[(G_t-v_\pi(S_t))\,\psi_t\bigr]$.
2. Tính chất tháp theo $(H_t,A_t)$: $\psi_t$ và $v_\pi(S_t)$ là hàm của $(H_t,A_t)$ nên ra ngoài, được $\mathbb E\bigl[(\mathbb E[G_t\mid H_t,A_t]-v_\pi(S_t))\,\psi_t\bigr]$.
3. Tính Markov: $\mathbb E[G_t\mid H_t,A_t]=q_\pi(S_t,A_t)$; và $q_\pi-v_\pi=A_\pi$ theo định nghĩa. $\square$

Kiểm trên chuỗi, tọa độ $\theta_A$ (chỉ bước $t=0$ ở $s_A$): $\tfrac12\cdot(+0{,}4)\cdot(+0{,}5)+\tfrac12\cdot(-0{,}4)\cdot(-0{,}5)=0{,}1+0{,}1=0{,}2$, đúng gradient.

Ý nghĩa của bước 3: lợi tức $G_t$ của một lượt là $q_\pi(S_t,A_t)$ cộng nhiễu có kỳ vọng $0$; thay $G_t$ bằng $A_\pi$ là bỏ nhiễu đó và bỏ mức chung $v_\pi$. Đây là lý do mạch 3 tìm cách ước lượng $A_\pi$.

**Đề xuất:** trang "Hệ quả" ngay sau mệnh đề đường cơ sở và trang ý tưởng chứng minh của nó (L10-2-05); trang "Ý tưởng chứng minh: gradient dạng lợi thế" 3 bước như trên, có dòng kiểm trên chuỗi. Ghi chú hiện xếp kết quả này là Mệnh đề 10.5(b); đề xuất (tác giả quyết) phát biểu lại thành hệ quả của Mệnh đề 10.2 cho khớp.

**Quy tắc chung rút ra:** mọi kết quả trên mặt trang có nhãn (Mệnh đề/Hệ quả/Định lý) và có ý tưởng chứng minh; không suy ra kết quả bằng "nên" trong câu dẫn.

### Trao đổi 16 — critic và actor ở cuối mạch 2 (L10-2-07)

**Tác giả:** (gửi ảnh L10-2-07 "Critic đánh giá hành động ngay sau một bước": "Nhắc lại: sai số TD $\delta_t=R_{t+1}+\gamma\hat v(S_{t+1})-\hat v(S_t)$" với ngoặc dưới "lợi tức một bước", "mức của trạng thái"; "Critic là hàm giá trị $\hat v$ dùng để đánh giá hành động qua trạng thái kế tiếp. Chính sách gọi là actor."; hộp "Khi $\hat v=v_\pi$, $\delta_t$ trung bình bằng lợi thế của hành động vừa chọn."; hình $s_A$, $s_B$, $\delta_t=0+0{,}9\cdot2-1{,}4=0{,}4=A_\pi(s_A,1)$, hai hộp actor/critic) "slide này tự nhiên nói đến critic actor rồi kết thúc mạch, có liên quan gì không ?"

**Điều phối viên:** Có liên quan, nhưng trang không nói ra mối liên hệ.

**Mạch logic đúng của cuối mạch 2.** Trang trước (L10-2-06) cho $\nabla J=\mathbb E[\sum_t\gamma^tA_\pi\psi_t]$, nhưng $q_\pi$, $v_\pi$ chưa biết. Có hai cách ước lượng $q_\pi(S_t,A_t)$:
- $G_t$: không chệch, nhưng mang nhiễu của mọi bước sau $t$;
- $R_{t+1}+\gamma v_\pi(S_{t+1})$: kỳ vọng có điều kiện cũng bằng $q_\pi(S_t,A_t)$ (phương trình Bellman), nhưng chỉ mang nhiễu của một bước.

Trừ $v_\pi(S_t)$ ở cả hai, cách thứ hai cho $\delta_t=R_{t+1}+\gamma v_\pi(S_{t+1})-v_\pi(S_t)$, với $\mathbb E[\delta_t\mid S_t,A_t]=q_\pi(S_t,A_t)-v_\pi(S_t)=A_\pi(S_t,A_t)$. Đây là cách thứ ba "so lợi tức với giá trị của trạng thái" (lợi tức một bước thay cho lợi tức cả lượt), nên đúng chủ đề của mạch. Trên chuỗi, tọa độ $\theta_A$ có phương sai $0{,}69$ (REINFORCE) → $0{,}20$ (trừ $v_\pi$) → $0$ (dùng $\delta_0$ với $v_\pi$ đúng): mọi lượt cho đúng $0{,}2$, vì $\delta_0$ không còn chứa phần ngẫu nhiên ở $s_B$. Đó là đỉnh của mạch 2 (L10-2-08).

**Trang hiện tại hỏng ở đâu:**
1. Không có câu hỏi dẫn ("$q_\pi$ chưa biết; $G_t$ mang nhiễu của mọi bước sau; có ước lượng nào ít nhiễu hơn?"). Trang mở bằng "Nhắc lại: sai số TD", nên sai số TD hiện ra như một chủ đề mới.
2. Tên vai "critic", "actor" được đặt trước khi có nhu cầu. Ở mạch 2, $\hat v=v_\pi$ là giá trị đúng; chưa có gì phải học, nên chưa cần tên "critic". Tên "actor" không được dùng lại trong mạch.
3. Hình hai hộp actor/critic ("hệ số của hàm điểm", "sai lệch để học $\hat v$") nói về việc học $\hat v$, điều mạch 2 không làm.
4. "Khi $\hat v=v_\pi$, $\delta_t$ trung bình bằng lợi thế" là mệnh đề không chứng minh (lại "trung bình", #12). Chứng minh một dòng: $\mathbb E[R_{t+1}+\gamma v_\pi(S_{t+1})\mid S_t,A_t]=q_\pi(S_t,A_t)$.
5. "mức của trạng thái" trong ngoặc dưới là văn nói (#11).
6. Lối sang mạch 3 ("critic phải học từ dữ liệu, và critic học dở thì $\delta_t$ lệch") chỉ nằm ở dòng "Còn thiếu:" của L10-2-08.

**Đề xuất:**
- Cuối mạch 2: câu hỏi dẫn → ý thay phần sau bước đầu bằng $\gamma v_\pi(S_{t+1})$ → "Mệnh đề. $\mathbb E[\delta_t\mid S_t,A_t]=A_\pi(S_t,A_t)$" với ý tưởng chứng minh một dòng → bảng ba hệ số trên chuỗi (L10-2-08), phương sai $0{,}69$; $0{,}20$; $0$, cột ghi "$\delta_0$ với $v_\pi$" thay cho "critic đúng".
- Bỏ "critic", "actor" khỏi mạch 2. Mạch 3 mở bằng nhu cầu: $v_\pi$ chưa biết, nên học một hàm $\hat v$ từ dữ liệu, gọi là critic, còn chính sách gọi là actor; critic sai, như $\hat v=(1{,}4;1)$ so với $(1{,}4;2)$, làm $\delta$ chệch (L10-3-01). Hình actor/critic chuyển sang đó, nếu giữ.
- Dòng dẫn mạch 2 (#6) và tên mạch nên nói cả ba cách so: lợi tức cả lượt trừ $v_\pi$, lợi tức một bước trừ $v_\pi$.

**Nguyên nhân gốc:** trang được xếp theo thứ tự khái niệm của ghi chú (Định nghĩa critic, Mệnh đề 10.8, Thuật toán 10.9) chứ không theo câu hỏi của mạch; tên gọi đặt trước nhu cầu; lối nối sang mạch sau nằm ở một dòng "Còn thiếu:" thay vì là câu hỏi mở mạch sau.

**Quy tắc chung rút ra:** một khái niệm hoặc tên vai chỉ xuất hiện ở mạch có nhu cầu dùng nó; trang mở cụm khái niệm bằng câu hỏi mà cụm trả lời; cuối mạch nêu kết quả đạt được và điều còn thiếu, và mạch sau mở bằng chính điều còn thiếu đó.

### Trao đổi 17 — nguồn các con số ở L10-2-08

**Tác giả:** (gửi ảnh L10-2-08: bảng "Hành động ở $s_A$, $s_B$ | Xác suất | REINFORCE | trừ $v_\pi$ | $\delta_0\psi_A$, critic đúng" với ba dòng; hộp "Tọa độ $\theta_A$: trung bình $0{,}2$ ở cả ba cột. Phương sai $0{,}69$; $0{,}20$; $0$."; "Còn thiếu: critic phải học từ dữ liệu, và critic học dở thì $\delta_t$ lệch."; sơ đồ neo vòng cập nhật) "slide này các con số ở đâu ra ?"

**Điều phối viên:** Mọi số trên trang đều đúng nhưng không số nào được tính trên trang. Nguồn:

- **Giá trị trạng thái:** $v_\pi(s_B)=\tfrac23\cdot3+\tfrac13\cdot0=2$; $v_\pi(s_A)=\tfrac12\,(0+0{,}9\cdot2)+\tfrac12\cdot1=1{,}4$ (chỉ có trên hình của L10-2-01).
- **Xác suất:** đi $1,1$: $p_Ap_B=\tfrac12\cdot\tfrac23=\tfrac13$; đi $1,2$: $\tfrac12\cdot\tfrac13=\tfrac16$; đi $2$: $1-p_A=\tfrac12$.
- **Cột REINFORCE** $G_0\psi_A$: $G_0=0{,}9\cdot3=2{,}7$; $0$; $1$; $\psi_A=1-p_A=+0{,}5$ khi chọn 1, $-p_A=-0{,}5$ khi chọn 2: $1{,}35$; $0$; $-0{,}5$ (L10-2-01).
- **Cột trừ $v_\pi$** $(G_0-1{,}4)\psi_A$: $1{,}3\cdot0{,}5=0{,}65$; $-1{,}4\cdot0{,}5=-0{,}7$; $(-0{,}4)(-0{,}5)=0{,}2$ (L10-2-02).
- **Cột $\delta_0$:** $\delta_0=R_1+\gamma v_\pi(S_1)-v_\pi(s_A)$. Chọn 1: $0+0{,}9\cdot2-1{,}4=0{,}4$, giống nhau ở hai lượt đầu vì $\delta_0$ chỉ nhìn bước đầu; chọn 2: $1+0-1{,}4=-0{,}4$ (trạng thái kết thúc có giá trị $0$). Nhân $\psi_A$: $0{,}2$ ở cả ba dòng.
- **Kỳ vọng:** $\tfrac13\cdot1{,}35+\tfrac16\cdot0+\tfrac12\cdot(-0{,}5)=0{,}2$; $\tfrac13\cdot0{,}65+\tfrac16\cdot(-0{,}7)+\tfrac12\cdot0{,}2=0{,}2$; $0{,}2$.
- **Phương sai** $=\mathbb E[X^2]-0{,}2^2$: $\tfrac13\cdot1{,}8225+\tfrac12\cdot0{,}25-0{,}04=0{,}6925$; $\tfrac13\cdot0{,}4225+\tfrac16\cdot0{,}49+\tfrac12\cdot0{,}04-0{,}04=0{,}2025$; $0$. Ba số này không được tính ở đâu trên deck.

**Trang hỏng ở đâu:** bảng chép kết quả của hai trang trước nhưng bỏ cột đầu vào ($G_0$, $\psi_A$); cột $\delta_0$ không có phép tính; giá trị $v_\pi$ chỉ nằm trên hình của trang khác; phương sai không có phép tính. Nửa dưới là sơ đồ neo vòng cập nhật, không giúp đọc bảng mà còn tranh chỗ. Thêm: tiêu đề văn nói (#11), "trung bình" (#12), "critic đúng" và "Còn thiếu:" (#15).

**Đề xuất:** bảng đủ cột: đường đi | xác suất | $G_0$ | $\psi_A$ | $G_0\psi_A$ | $(G_0-1{,}4)\psi_A$ | $\delta_0$ | $\delta_0\psi_A$, cột $\delta_0$ ghi phép tính; hai dòng cuối "kỳ vọng" và "phương sai", mỗi ô một phép tính; nếu không vừa thì tách một trang tiếp theo cho kỳ vọng và phương sai. Giá trị $v_\pi$ nhắc lại trên trang ("$v_\pi=(1{,}4;\,2)$"). Sơ đồ neo chuyển sang một trang tóm tắt cuối mạch.

**Quy tắc chung rút ra:** mọi số trên trang tính được ngay trên trang, hoặc lấy từ trang liền trước và được nhắc lại kèm tên đại lượng; bảng so sánh nhiều phương pháp giữ cột đầu vào. Hình trang trí hoặc sơ đồ tổng quát không đặt chung với bảng tính.

### Trao đổi 18 — tiêu đề và dòng dẫn mạch 3

**Tác giả:** (gửi ảnh trang tiêu đề mạch 3: "3. Trộn đánh giá một bước và cả lượt" / "Critic học dở thì đánh giá một bước bị lệch, còn lợi tức cả lượt thì dao động.") "câu tiêu đề và câu tóm tắt đều văn nói"

**Điều phối viên:** Đúng.

- **Tên mạch** "Trộn đánh giá một bước và cả lượt": "trộn", "đánh giá một bước", "cả lượt" là lời nói thay cho "tổ hợp có trọng số", "ước lượng lợi thế một bước", "ước lượng từ lợi tức cả lượt". Đề xuất: **"Ước lượng lợi thế: độ chệch và phương sai"** (tránh trùng tiêu đề trang nội dung đầu "Ước lượng lợi thế tổng quát").
- **Dòng dẫn** "Critic học dở thì đánh giá một bước bị lệch, còn lợi tức cả lượt thì dao động.": khẩu ngữ ("học dở", "thì … còn … thì"), và dùng "critic", thuật ngữ mạch này mới giới thiệu (#6, #15). Đề xuất (18 âm tiết): **"Tổ hợp có trọng số các ước lượng lợi thế nhiều bước cân bằng độ chệch và phương sai."** Câu chỉ dùng "lợi thế" (mạch 2), "độ chệch", "phương sai" (thống kê đã học).

**Thuật ngữ cả deck:** mặt trang dùng "lệch" 12 lần và "chệch" 0 lần (ghi chú: "chệch" 59 lần), "dao động" 12 lần và "phương sai" 4 lần (ghi chú: "phương sai" 53 lần, "dao động" 1 lần). Deck đã thay thuật ngữ thống kê bằng lời thường. Đề xuất: "độ chệch"/"chệch" cho bias, "phương sai" cho variance trên toàn deck; "lệch" chỉ giữ cho nghĩa khoảng cách ("lệch xa $2$"), và cân nhắc thay bằng "cách".

**Quy tắc chung rút ra:** tên mạch là cụm danh từ học thuật; dòng dẫn là câu học thuật; thuật ngữ thống kê (kỳ vọng, phương sai, độ chệch) dùng đúng tên, không thay bằng lời thường (cùng nhóm #11, #12).

### Trao đổi 19 — tiêu đề L10-3-01

**Tác giả:** (gửi ảnh L10-3-01 "Một bước thì lệch, cả lượt thì dao động": hình chuỗi với $\hat v=1$, $v_\pi=2$ ở $s_B$; "Critic $\hat v=(1{,}4;\,1)$, giá trị thật $(1{,}4;\,2)$. Hai lượt cùng chọn 1 ở $s_A$, lợi thế đúng $0{,}4$.") "tiêu đề là văn nói"

**Điều phối viên:** Đúng; trang này đã nằm trong bảng đề xuất của #11, nay chỉnh thêm. Tiêu đề vừa khẩu ngữ ("thì … thì", "lệch", "dao động") vừa thiếu điều kiện: ước lượng một bước chỉ chệch khi critic sai. Đề xuất: **"Với critic sai, ước lượng một bước bị chệch, ước lượng cả lượt có phương sai lớn"**; nếu dài, tách thành trang đặt vấn đề (critic đánh giá thấp $s_B$) và trang kết quả.

Thân trang cùng lỗi #15: "Critic $\hat v=(1{,}4;1)$" hiện ra không có lý do. Cần một dòng: critic là hàm học từ dữ liệu nên có sai số; ở đây nó đánh giá thấp $s_B$ một đơn vị ($1$ thay cho $2$), còn $s_A$ đúng. Hình nên ghi $\hat v$ và $v_\pi$ ở cả hai trạng thái, không chỉ $s_B$.

### Trao đổi 20 — các con số của L10-3-01

**Tác giả:** (gửi ảnh L10-3-01 có bảng "Lượt | Xác suất | Một bước $\delta_0$": "(i) $s_B$: 1, thưởng 3 | $2/3$ | $0+0{,}9\cdot1-1{,}4=-0{,}5$"; "(ii) $s_B$: 2, thưởng 0 | $1/3$ | $-0{,}5$") "ví dụ này cũng khó hiểu, các con số lấy ở đâu"

**Điều phối viên:** Nguồn từng số:

- **Đại lượng cần ước lượng:** lợi thế $A_\pi(s_A,1)=q_\pi(s_A,1)-v_\pi(s_A)=0{,}9\cdot2-1{,}4=0{,}4$ (mạch 2). Vì vậy chỉ xét các lượt bắt đầu bằng hành động 1 ở $s_A$. Trang không nói mục tiêu này; "lợi thế đúng $0{,}4$" nằm ở câu dẫn, ngoài bảng.
- **Giá trị thật** $(1{,}4;\,2)$: $v_\pi(s_A)$, $v_\pi(s_B)$ của mạch 2.
- **Critic $\hat v=(1{,}4;\,1)$:** giá trị giả định của một critic học chưa tốt: đúng ở $s_A$, đánh giá thấp $s_B$ một đơn vị. Trang không nói đây là giả định và vì sao chọn.
- **Xác suất** $\tfrac23$, $\tfrac13$: sau khi tới $s_B$, chọn hành động 1 với $p_B=\tfrac23$ (thưởng $3$), hành động 2 với $1-p_B=\tfrac13$ (thưởng $0$).
- **Ước lượng một bước:** $\delta_0=R_1+\gamma\hat v(S_1)-\hat v(s_A)=0+0{,}9\cdot\hat v(s_B)-1{,}4=0+0{,}9\cdot1-1{,}4=-0{,}5$. Cả hai lượt cho cùng $-0{,}5$ vì $\delta_0$ không nhìn những gì xảy ra ở $s_B$. Kỳ vọng $-0{,}5$, sai dấu so với $0{,}4$: độ chệch $-0{,}9=\gamma\,(\hat v(s_B)-v_\pi(s_B))=0{,}9\cdot(-1)$. Phương sai $0$.
- **Ước lượng cả lượt** (cột hiện sau): $G_0-\hat v(s_A)$ với $G_0=R_1+\gamma R_2$: lượt (i) $0{,}9\cdot3-1{,}4=1{,}3$; lượt (ii) $0-1{,}4=-1{,}4$. Kỳ vọng $\tfrac23\cdot1{,}3+\tfrac13\cdot(-1{,}4)=0{,}4$: không chệch, vì không dùng $\hat v(s_B)$. Hai lượt cách nhau $2{,}7$; phương sai $\tfrac23\cdot\tfrac13\cdot2{,}7^2=1{,}62$.

**Trang hỏng ở đâu:** không nêu đại lượng cần ước lượng; critic sai xuất hiện không lý do; xác suất không nói là $p_B$; công thức $\delta_0$ không ghi $\hat v$ ở đâu dùng; dòng (ii) chỉ ghi kết quả; đường đi ghi nửa chừng ("$s_B$: 1, thưởng 3"); cột so sánh và độ chệch, phương sai hiện theo mảnh, thiếu phép tính.

**Đề xuất:**
- Dòng mở: "Ước lượng $A_\pi(s_A,1)=0{,}4$ từ một lượt bắt đầu bằng hành động 1 ở $s_A$. Critic học từ ít dữ liệu: $\hat v(s_A)=1{,}4$ đúng, $\hat v(s_B)=1$ thấp hơn $v_\pi(s_B)=2$."
- Bảng: đường đi đầy đủ ($s_A\xrightarrow{1}s_B\xrightarrow{1}$ kết thúc) | xác suất ($p_B=\tfrac23$; $1-p_B=\tfrac13$) | $R_1$, $R_2$ | một bước $\delta_0=R_1+\gamma\hat v(s_B)-\hat v(s_A)$ | cả lượt $G_0-\hat v(s_A)$; mỗi ô ghi phép tính đủ.
- Ba dòng cuối: kỳ vọng ($-0{,}5$ | $0{,}4$); độ chệch so với $0{,}4$ ($-0{,}9$ | $0$); phương sai ($0$ | $1{,}62$). Câu hỏi dẫn sang GAE ở dưới bảng.
- Có thể tách hai trang: trang dựng (mục tiêu, critic sai, hình có $\hat v$ và $v_\pi$ ở cả hai trạng thái) và trang bảng.

**Quy tắc chung rút ra:** ví dụ nêu rõ đại lượng cần tính (giá trị đúng để so) trước bảng; mọi giá trị giả định ghi là giả định kèm lý do chọn; mọi xác suất ghi nguồn ($p_B$, $1-p_B$).

### Trao đổi 21 — L10-4-01 (mục #20)

**Tác giả:** (ảnh trang "Bước lớn đổi cả nơi chính sách tới") "văn nói" / "không rõ mục đích của slide".

**Điều phối:**
- *Vai trò dự kiến của trang:* mở mạch 4. Chính sách mới thay đổi không chỉ xác suất chọn hành động mà cả phân bố trạng thái; lượt của chính sách cũ chỉ phản ánh phân bố của $\pi$. Trang sau (Bổ đề hiệu hiệu năng) và trang hàm thay thế dùng chính hai chính sách này.
- *Vì sao không rõ mục đích:*
  1. Không nêu bài toán. Câu "Đoán $J$ của chính sách mới từ lượt của chính sách cũ thế nào?" là fragment cuối, sau hình và kết luận.
  2. $\pi'$ không có nguồn gốc: không nói vì sao xét $p'_A=1$, $p'_B=0{,}5$. Hơn nữa $p'_A=1$ không ứng với $\theta$ hữu hạn trong tham số hóa $p_s=\sigma(\theta_s)$ (cùng lỗi #5).
  3. Ký hiệu cặp $(\tfrac12;\tfrac23)$ chưa nói là $(p_A;p_B)$; "tỉ lệ lượt tới $s_B$" bằng $p_A$ không được giải thích.
  4. Không nói vì sao nơi tới quan trọng: $J(\pi)$, $J(\pi')$ không có trên trang, nên kết luận "chọn kém hơn" không dẫn tới hệ quả nào.
- *Văn nói:* "Bước lớn đổi cả nơi chính sách tới", "tới $s_B$ ở một nửa số lần", "ở mọi lượt". Đề xuất tiêu đề: "Chính sách mới thay đổi phân bố trạng thái" hoặc "Đánh giá chính sách mới từ lượt của chính sách cũ".
- *Đề xuất cấu trúc:*
  - Dòng bài toán: "Cho các lượt sinh bởi $\pi$. Cần ước lượng $J(\pi')$ trước khi chạy $\pi'$."
  - Nguồn của $\pi'$: bước dài theo ước lượng một lượt ở mạch 1 (lượt "chọn 2 ở $s_B$" đẩy $p_B$ xuống, hệ số dương ở $s_A$ đẩy $p_A$ lên), ghi cả $\theta'$.
  - Bảng hai cột $\pi$, $\pi'$: $p_A$, $p_B$, $\Pr(\text{tới } s_B)=p_A$, $J=2{,}7p_Ap_B+1-p_A$.
  - Kết luận: $\pi'$ tới $s_B$ nhiều hơn và ở $s_B$ chọn hành động 1 ít hơn; lượt của $\pi$ chỉ cho thấy $s_B$ với xác suất $p_A$.
- *Phương án số (tác giả chọn):*
  - (a) Giữ $\pi'=(1;\,0{,}5)$: $J(\pi')=1{,}35$, hiệu thật $-0{,}05$, hàm thay thế $+0{,}175$; chấp nhận $\theta'_A=+\infty$ (giới hạn), phải nói rõ.
  - (b) $\theta'=(\log9;\,0)$, tức $\pi'=(0{,}9;\,0{,}5)$: $J(\pi')=2{,}7\cdot0{,}45+0{,}1=1{,}315$, hiệu thật $-0{,}085$. Kiểm bằng bổ đề: $A_\pi(s_A,\pi')=0{,}9\cdot0{,}4-0{,}1\cdot0{,}4=0{,}32$; $A_\pi(s_B,\pi')=-0{,}5$; số lần $\pi'$ tới $s_B$ là $0{,}9\cdot0{,}9=0{,}81$; $0{,}32-0{,}405=-0{,}085$. Hàm thay thế: $0{,}32-0{,}5\cdot0{,}45=+0{,}095$. Vẫn trái dấu, $\theta'$ hữu hạn, nhưng phải tính lại mạch 4–5.
- *Quy tắc chung:* trang mở mạch nêu bài toán ở câu đầu; mọi đối tượng mới (chính sách $\pi'$) có nguồn gốc và tham số trong cùng một tham số hóa; trang ví dụ cho đủ đại lượng để kết luận có hệ quả đo được.

### Trao đổi 22 — L10-4-02 (mục #21)

**Tác giả:** (ảnh trang "Hiệu $J$ tính theo nơi chính sách mới tới") "đưa ra khái niệm $A_\pi(s,\pi')$ đột ngột" / "Ý nghĩa của $J(\pi')-J(\pi)$, công thức đó từ đâu ra".

**Điều phối:**
- *$A_\pi(s,\pi')$ đột ngột.* Trang mở bằng ký hiệu, không có câu hỏi dẫn tới nó. Câu hỏi tự nhiên: "Tại $s$, chọn một hành động theo $\pi'$ rồi từ bước sau theo $\pi$; so với theo $\pi$ ngay từ đầu, được thêm bao nhiêu?" Đáp số là
  $$A_\pi(s,\pi')=\sum_a\pi'(a\mid s)\,q_\pi(s,a)-v_\pi(s)=\sum_a\pi'(a\mid s)A_\pi(s,a).$$
  Trên chuỗi (dùng $q_\pi$, $v_\pi$ đã có ở mạch 2): $s_A$: $1\cdot1{,}8+0\cdot1-1{,}4=0{,}4$; $s_B$: $0{,}5\cdot3+0{,}5\cdot0-2=-0{,}5$. Dạng qua $q_\pi$, $v_\pi$ dễ hiểu hơn dạng tổng lợi thế.
- *Ý nghĩa của $J(\pi')-J(\pi)$:* mức tăng hàm mục tiêu khi thay $\pi$ bằng $\pi'$. Bổ đề hiệu hiệu năng (ghi chú, Bổ đề 10.19) nói: mức tăng bằng tổng, trên các lần $\pi'$ thăm trạng thái (trọng số $\gamma^t$), của lợi ích một bước $A_\pi(s,\pi')$. Trực giác trong ghi chú: "nếu $\pi'$ chọn hành động có lợi thế dương ở những trạng thái nó hay thăm, thì $\pi'$ tốt hơn $\pi$".
- *Công thức từ đâu ra:* trang không có nhãn, giả thiết, ý nghĩa hay chứng minh. Ghi chú có chứng minh 5 bước; ý tưởng gọn:
  1. $A_\pi(S_t,A_t)$ có kỳ vọng (theo bước chuyển) bằng $R_{t+1}+\gamma v_\pi(S_{t+1})-v_\pi(S_t)$, không phụ thuộc chính sách đang chạy.
  2. Cộng dọc một lượt của $\pi'$ với trọng số $\gamma^t$: các số hạng $v_\pi$ triệt tiêu lồng nhau, còn $G_0-v_\pi(S_0)$.
  3. Lấy kỳ vọng theo $\pi'$: $J(\pi')-J(\pi)$. Gom theo trạng thái được dạng trên trang.
- *Lỗi phụ:* "số lần $\pi'$ tới $s$" thực ra là số lần thăm kỳ vọng có chiết khấu $\eta_{\pi'}(s)=\sum_t\gamma^t\Pr_{\pi'}(S_t=s)$ (ghi chú dùng $\eta$); $0{,}9$ ở $s_B$ là $\gamma\cdot1$, không phải số lần. Văn nói: "Lợi thế cũ chọn theo $\pi'$", "Nhắc lại: lợi thế cũ", "kiểm:", "Công thức đúng, nhưng…". Ghi chú viết "lợi thế trung bình" (dòng 59, 911, Ví dụ 10.11) → "kỳ vọng" (#12).
- *Đồng bộ ghi chú:* Ví dụ 10.11 của ghi chú mở bằng $\pi'=(0{,}6;\,0{,}8)$ ($\Delta J=0{,}296$), cặp $(1;\,0{,}5)$ chỉ ở đoạn "Hai bước trên một đường thẳng"; trang chiếu chỉ dùng $(1;\,0{,}5)$. Theo quyết định một ví dụ chung, cần thống nhất $\pi'$ (xem #20, phương án (a)/(b)).
- *Đề xuất:* tách thành
  1. Trang "Lợi ích của một bước đổi chính sách": câu hỏi, định nghĩa $A_\pi(s,\pi')$ (dạng $q_\pi-v_\pi$), hai số trên chuỗi.
  2. Trang "Bổ đề (hiệu hiệu năng)": giả thiết (cùng động lực, cùng phân phối đầu, $\gamma<1$), định nghĩa $\eta_{\pi'}$, kết luận, "Ý nghĩa:".
  3. Trang "Ý tưởng chứng minh: bổ đề hiệu hiệu năng" (3 bước trên).
  4. Trang bảng kiểm trên chuỗi (giữ bảng hiện tại, cột "$\eta_{\pi'}(s)$", dòng kiểm bằng $J=2{,}7p_Ap_B+1-p_A$).
- *Quy tắc chung:* ký hiệu mới đi sau câu hỏi nó trả lời và kèm ý nghĩa; công thức kết quả mang nhãn, giả thiết, ý nghĩa và ý tưởng chứng minh (cùng nhóm E với #14); tiêu đề cột đúng tên đại lượng.

### Trao đổi 23 — L10-4-04, L10-4-05 (mục #22)

**Tác giả:** (ảnh trang "Hàm thay thế tiếp xúc $J$ tại chính sách cũ") "slide này, và slide sau đó cũng đột ngột đưa ra $\Delta J$, khai triển $J$ … rất khó theo dõi".

**Điều phối:**
- *L10-4-04, những gì thiếu:*
  1. $\Delta J$, $\Delta\mathcal L$ và $t$ không định nghĩa. Cần: $\Delta J=J(\pi')-J(\pi)$, $\Delta\mathcal L=\mathcal L_\pi(\pi')-J(\pi)$.
  2. Đường $p_A=\frac{1+t}2$, $p_B=\frac{4-t}6$ không nói là đoạn thẳng từ $\pi=(\tfrac12;\tfrac23)$ ($t=0$) tới $\pi'=(1;0{,}5)$ ($t=1$).
  3. Không có phép thế: $J=2{,}7\cdot\frac{(1+t)(4-t)}{12}+1-\frac{1+t}2=1{,}4+0{,}175t-0{,}225t^2$. Đường $\Delta\mathcal L=0{,}175t$ trên hình không có nguồn: $1\cdot0{,}8\cdot\frac t2+0{,}45\cdot3\cdot(-\frac t6)=0{,}4t-0{,}225t$.
  4. Khẳng định "bằng $J$ và cùng độ dốc" là Mệnh đề 10.22 của ghi chú, nhưng trang chỉ có một dòng, không phát biểu, không lý do.
  5. Điểm $t=0{,}4$ không có lý do chọn; nhãn hình "đoán", "thật" là văn nói.
- *L10-4-05, những gì thiếu:*
  1. Khai triển $J$ quanh $(\tfrac12;\tfrac23)$ không có bước: $2{,}7(\tfrac12+\Delta p_A)(\tfrac23+\Delta p_B)+\tfrac12-\Delta p_A=1{,}4+0{,}8\Delta p_A+1{,}35\Delta p_B+2{,}7\Delta p_A\Delta p_B$.
  2. Việc phần bậc nhất trùng $\Delta\mathcal L$ chỉ được khẳng định bằng một câu dày.
  3. Ý chính nằm trong ghi chú người nói, không ở mặt trang: sai số $2{,}7\Delta p_A\Delta p_B=(\gamma\Delta p_A)\cdot A_\pi(s_B,\pi')$, tức số lần tới $s_B$ tăng thêm nhân lợi ích mỗi lần. Đây chính là điều trang L10-4-01 muốn nói.
  4. Thứ tự ngược: trường hợp riêng (đường thẳng theo $t$) đứng trước dạng tổng quát (khai triển theo $\Delta p_A$, $\Delta p_B$).
  5. Tiêu đề "Bước gần thì hàm thay thế sai ít" là văn nói.
- *Đề xuất chuỗi lập luận* (sau bổ đề hiệu hiệu năng và định nghĩa hàm thay thế, #21):
  1. **Sai số của hàm thay thế.** Trừ hai công thức (chỉ khác số lần tới):
     $$\Delta J-\Delta\mathcal L=\sum_s\bigl(\eta_{\pi'}(s)-\eta_\pi(s)\bigr)\,A_\pi(s,\pi').$$
     Trên chuỗi chỉ $s_B$ đổi số lần tới: $\eta_{\pi'}(s_B)-\eta_\pi(s_B)=\gamma\Delta p_A$, và $A_\pi(s_B,\pi')=3\Delta p_B$. Vậy sai số $=2{,}7\Delta p_A\Delta p_B$. "Kiểm tra:" khai triển $J$ có bước như trên.
  2. **Mệnh đề (hàm thay thế tiếp xúc $J$).** Cả hai thừa số cùng cỡ độ dài bước, nên sai số cỡ bình phương độ dài bước; do đó $\mathcal L_\pi(\pi)=J(\pi)$ và hai gradient bằng nhau tại chính sách cũ. Ý tưởng chứng minh theo đúng bước 1, có nhãn.
  3. **Minh họa trên đoạn thẳng** từ $\pi$ tới $\pi'$: thế $\Delta p_A=\frac t2$, $\Delta p_B=-\frac t6$ vào bước 1: $\Delta\mathcal L=0{,}175t$, sai số $-0{,}225t^2$. Hình hiện tại giữ nguyên, nhãn "hàm thay thế", "giá trị thật"; ghi lý do điểm $t=0{,}4$ (bước ngắn, cùng dấu) và $t=1$ (bước dài, trái dấu).
  4. **Câu hỏi nhanh** bước $(0{,}6;\,0{,}7)$ giữ nguyên (sai số giảm $25$ lần). Dòng "Còn thiếu:" là nhãn không cho phép, đổi thành câu chuyển sang định lý chặn.
- *Lợi ích:* sai số được giải thích bằng đúng ý của trang mở mạch (chính sách mới tới $s_B$ nhiều hơn, ở đó kém hơn), không cần "khai triển $J$" như một mẹo riêng của ví dụ, và dạng tổng quát dẫn thẳng tới định lý chặn cải thiện (phạt theo khoảng cách).
- *Quy tắc chung:* ký hiệu $\Delta$ phải định nghĩa; đại lượng vẽ trên hình phải có phép tính ở trang đó hoặc trang trước; dạng tổng quát trước, trường hợp riêng sau; ý chính lên mặt trang, ghi chú người nói chỉ bổ sung; tiêu đề nêu kết quả thì trang phải phát biểu và lý giải kết quả đó.

### Trao đổi 24 — L10-4-06 (mục #23)

**Tác giả:** (ảnh trang "Sai số của hàm thay thế bị chặn theo khoảng cách") "phát biểu kiểu văn nói".

**Điều phối:**
- *Văn nói ở đâu:* kết luận viết bằng lời ("không nhỏ hơn mức tăng hàm thay thế đoán trừ một phạt", "Phạt tỉ lệ với khoảng cách trung bình theo nơi chính sách cũ tới"); "đoán", "phạt", "nơi chính sách cũ tới" không phải thuật ngữ. Công thức thật chỉ ở ghi chú người nói.
- *Sai về nội dung:*
  1. "Giả thiết: lợi thế và số lần tới của chính sách cũ được tính chính xác" là điều kiện áp dụng, không phải giả thiết. Giả thiết của Định lý 10.26: MDP hữu hạn, cùng $P$ và $\mu_0$, $|R_{t+1}|\le R_{\max}$, $0\le\gamma<1$, hai chính sách Markov dừng, điều kiện hỗ trợ $\pi'(a\mid s)>0\Rightarrow\pi(a\mid s)>0$.
  2. Hằng số là $C=2\gamma\chi_{\pi'}/(1-\gamma)^2$ với $\chi_{\pi'}=\max_s|A_\pi(s,\pi')|$, không phải $1/(1-\gamma)^2$.
  3. $D_{\mathrm{TV}}$ (biến phân toàn phần) hiện sau kết luận, không có tên; $\nu^\pi$ (phân bố chiếm dụng chuẩn hóa) không định nghĩa trên trang.
  4. Câu kết "phạt vượt mức đoán, trừ khi bước rất ngắn" không có số trên mặt trang (số $-0{,}89$, $\Delta<0{,}056$ chỉ ở ghi chú người nói, và dùng bước $(0{,}6;0{,}8)$ khác ví dụ chung).
- *Đề xuất phát biểu:*
  > **Định nghĩa.** Khoảng cách biến phân toàn phần tại $s$: $D_{\mathrm{TV}}(s)=\tfrac12\sum_a|\pi'(a\mid s)-\pi(a\mid s)|$.
  >
  > **Định lý (chặn cải thiện).** **Giả thiết:** như bổ đề hiệu hiệu năng; thêm $\pi'(a\mid s)>0\Rightarrow\pi(a\mid s)>0$. **Kết luận:** với $\chi_{\pi'}=\max_s|A_\pi(s,\pi')|$,
  > $$J(\pi')-J(\pi)\ge\bigl[\mathcal L_\pi(\pi')-J(\pi)\bigr]-\frac{2\gamma\chi_{\pi'}}{(1-\gamma)^2}\,\mathbb E_{S\sim\nu^\pi}\bigl[D_{\mathrm{TV}}(S)\bigr].$$
  > **Ý nghĩa:** nếu số hạng phạt nhỏ hơn mức tăng của hàm thay thế thì $J$ tăng.
- *Ý tưởng chứng minh (nối với #22):*
  1. Sai số $\Delta J-\Delta\mathcal L=\frac1{1-\gamma}\sum_s(\nu^{\pi'}-\nu^\pi)(s)\,A_\pi(s,\pi')$.
  2. $|A_\pi(s,\pi')|\le\chi_{\pi'}$.
  3. Bổ đề 10.25: $\lVert\nu^{\pi'}-\nu^\pi\rVert_1\le\frac{2\gamma}{1-\gamma}\mathbb E_{\nu^\pi}[D_{\mathrm{TV}}]$. Ghép ba bước.
- *Ví dụ trên chuỗi (trang riêng, dùng ví dụ chung):*
  - Bước $(1;0{,}5)$: $\chi=\max(0{,}4;\,0{,}5)=0{,}5$, $C=2\cdot0{,}9\cdot0{,}5/0{,}01=90$; $\nu^\pi=(0{,}1;\,0{,}045)$, $D_{\mathrm{TV}}=(0{,}5;\,\tfrac16)$, kỳ vọng $0{,}0575$; phạt $5{,}175$; cận $0{,}175-5{,}175=-5$, thật $-0{,}05$. Cận đúng nhưng rất lỏng.
  - Bước chỉ đổi $p_B$ một lượng $\Delta>0$: $\Delta\mathcal L=1{,}35\Delta$, $\chi=3\Delta$, $\mathbb E_{\nu^\pi}D_{\mathrm{TV}}=0{,}045\Delta$, phạt $24{,}3\Delta^2$. Cận dương khi $\Delta<1{,}35/24{,}3\approx0{,}056$. Đây là con số cho câu "trừ khi bước rất ngắn".
- *Quy tắc chung:* định lý trên trang chiếu phát biểu bằng công thức, lấy giả thiết và hằng số từ ghi chú; mọi đại lượng trong kết luận định nghĩa trước kết luận; câu "Ý nghĩa:" có số minh họa trên mặt trang, không chỉ trong ghi chú người nói.

### Trao đổi 25 — L10-4-12 (mục #24)

**Tác giả:** (ảnh trang "KL đo khoảng cách bằng lượt cũ") "nên phát biểu dạng mệnh đề / bổ đề".

**Điều phối:**
- *Các kết quả đang viết như câu thường:*
  1. Đẳng thức $D_{\mathrm{KL}}(s)=\mathbb E_{a\sim\pi}[-\log\rho]$: hệ quả trực tiếp của định nghĩa $\rho=\pi'/\pi$; nên là "Nhận xét." một dòng.
  2. "Khoảng cách của định lý không vượt $\sqrt{D_{\mathrm{KL}}/2}$": bất đẳng thức Pinsker, ghi chú Mệnh đề 10.24(b). Cần nhãn, giả thiết (hai phân phối trên tập hữu hạn), kết luận đủ cả hai chiều KL.
  3. Thiếu hẳn Hệ quả 10.27 của ghi chú: thay $D_{\mathrm{TV}}$ bằng KL trong định lý chặn cải thiện,
     $$J(\pi')-J(\pi)\ge\bigl[\mathcal L_\pi(\pi')-J(\pi)\bigr]-\frac{2\gamma\chi_{\pi'}}{(1-\gamma)^2}\sqrt{\tfrac12\bar D_{\mathrm{KL}}},\quad\bar D_{\mathrm{KL}}=\mathbb E_{S\sim\nu^\pi}[D_{\mathrm{KL}}(S)].$$
     Đây mới là lý do trang tồn tại: miền tin cậy (trang sau) ràng buộc đúng $\bar D_{\mathrm{KL}}$. Ý tưởng chứng minh: (i) Pinsker theo từng trạng thái; (ii) Jensen cho hàm lõm $\sqrt{\cdot}$: $\mathbb E\sqrt{X}\le\sqrt{\mathbb E X}$.
- *Lý do chọn KL chưa đúng:* "KL tính được từ lượt cũ" không phân biệt KL với $D_{\mathrm{TV}}$ ($D_{\mathrm{TV}}(s)=\tfrac12\mathbb E_{a\sim\pi}|1-\rho|$ cũng tính được từ lượt cũ). Lý do thật: KL trơn theo $\theta$ (khả vi, có ma trận Hessian dùng ở TRPO), còn $|\cdot|$ không khả vi; và Pinsker cho phép giữ cận cải thiện.
- *Ví dụ:* $D_{\mathrm{KL}}(s_A)=+\infty$ phụ thuộc $p'_A=1$ (giới hạn $\theta'_A\to\infty$, #20). Theo phương án (b) $\pi'=(0{,}9;\,0{,}5)$: $D_{\mathrm{KL}}(s_A)=\tfrac12\log\tfrac{0{,}5}{0{,}9}+\tfrac12\log\tfrac{0{,}5}{0{,}1}\approx0{,}511$, $D_{\mathrm{TV}}(s_A)=0{,}4\le\sqrt{0{,}511/2}\approx0{,}505$ (kiểm Pinsker). Ý "KL phạt nặng khi chính sách mới gần bỏ một hành động" vẫn giữ được bằng một dòng: $p'_A\to1$ thì $D_{\mathrm{KL}}(s_A)\to\infty$ trong khi $D_{\mathrm{TV}}\to0{,}5$.
- *Tiêu đề:* "KL đo khoảng cách bằng lượt cũ" là văn nói và không chính xác (KL không phải khoảng cách). Đề xuất: "Phân kỳ Kullback–Leibler và bất đẳng thức Pinsker"; trang hệ quả: "Chặn cải thiện theo KL trung bình".
- *Đề xuất cấu trúc:*
  1. Định nghĩa KL tại $s$ (chiều $\pi\Vert\pi'$) + Nhận xét dạng tỉ số + số trên chuỗi.
  2. Mệnh đề (bất đẳng thức Pinsker) + Ý nghĩa + kiểm số tại $s_A$.
  3. Hệ quả (chặn cải thiện theo KL trung bình) + ý tưởng chứng minh 2 bước + "Ý nghĩa: giữ $\bar D_{\mathrm{KL}}$ nhỏ thì phạt nhỏ", dẫn sang miền tin cậy.
- *Quy tắc chung:* mọi khẳng định toán học dùng ở trang sau (bất đẳng thức, đẳng thức không hiển nhiên) mang nhãn Mệnh đề/Bổ đề/Hệ quả/Nhận xét với giả thiết; lý do chọn một công cụ phải là tính chất phân biệt nó với công cụ thay thế.

### Trao đổi 26 — L10-4-03 (mục #25)

**Tác giả:** (ảnh trang "Hàm thay thế dùng nơi chính sách cũ tới") "định nghĩa, tiêu đề đang văn nói" / "các số liệu cũng khó theo dõi".

**Điều phối:**
- *Định nghĩa văn nói và chưa là định nghĩa:* câu "Hàm thay thế $\mathcal L$ giữ số lần tới của chính sách cũ, nên tính được từ lượt cũ" trộn lý do, cách dựng và tính chất; công thức chỉ cho hiệu $\mathcal L_\pi(\pi')-J(\pi)$, không cho $\mathcal L_\pi(\pi')$. Đề xuất:
  - Dòng lý do: "Vế phải của bổ đề hiệu hiệu năng cần $\eta_{\pi'}$, tức cần chạy $\pi'$. Thay $\eta_{\pi'}$ bằng $\eta_\pi$."
  - **Định nghĩa.** Hàm thay thế (surrogate objective) của $\pi'$ quanh $\pi$:
    $$\mathcal L_\pi(\pi')=J(\pi)+\sum_s\eta_\pi(s)\,A_\pi(s,\pi'),\qquad\eta_\pi(s)=\sum_t\gamma^t\Pr_\pi(S_t=s).$$
  - "Ý nghĩa:" mọi đại lượng ở vế phải là của $\pi$, nên $\mathcal L_\pi(\pi')$ tính được từ lượt của $\pi$ (dạng tỉ số ở trang sau).
- *Tiêu đề:* "Hàm thay thế dùng nơi chính sách cũ tới" → "Hàm thay thế" hoặc "Định nghĩa hàm thay thế".
- *Số liệu khó theo dõi, vì:*
  1. Cột $A_\pi(s,\pi')$ và "số lần $\pi'$ tới" chép từ trang trước, không nhắc nguồn.
  2. $0{,}9$ và $0{,}9\cdot0{,}5$ không có công thức: trên chuỗi, $\eta(s_A)=1$ (chỉ thăm ở $t=0$), $\eta(s_B)=\gamma\cdot\Pr(\text{tới }s_B)=\gamma p_A$; với $\pi'$: $0{,}9\cdot1$, với $\pi$: $0{,}9\cdot0{,}5$.
  3. Có cột tích với $\eta_\pi$ nhưng không có cột tích với $\eta_{\pi'}$, nên "thật: $-0{,}05$" đứng dưới cột $\eta_{\pi'}$ mà không có phép cộng nào cho ra nó.
  4. Tên cột "số lần … tới" sai đại lượng ($0{,}45$ không phải số lần), như #21.
- *Đề xuất bảng* (cột đồng nhất, dùng lại ở trang sai số #22):

  | $s$ | $A_\pi(s,\pi')$ | $\eta_{\pi'}(s)$ | $\eta_\pi(s)$ | $\eta_{\pi'}A_\pi$ | $\eta_\pi A_\pi$ | $(\eta_{\pi'}-\eta_\pi)A_\pi$ |
  |---|---|---|---|---|---|---|
  | $s_A$ | $0{,}4$ | $1$ | $1$ | $0{,}4$ | $0{,}4$ | $0$ |
  | $s_B$ | $-0{,}5$ | $\gamma p'_A=0{,}9$ | $\gamma p_A=0{,}45$ | $-0{,}45$ | $-0{,}225$ | $-0{,}225$ |
  | tổng | | | | $\Delta J=-0{,}05$ | $\Delta\mathcal L=+0{,}175$ | sai số $-0{,}225$ |

  Cột cuối nối thẳng sang trang sai số (#22): chỉ $s_B$ đổi trọng số, và ở đó $A_\pi(s_B,\pi')<0$. (Số theo phương án (a) của #20; phương án (b) cho $0{,}32$; $0{,}81$; $0{,}405$; $\Delta J=-0{,}085$, $\Delta\mathcal L=0{,}095$.)
- *Ký hiệu chưa thống nhất với ghi chú:* trang chiếu dùng số lần thăm có chiết khấu không chuẩn hóa (ghi chú gọi $\eta$), ghi chú phát biểu bằng $\nu$ chuẩn hóa kèm $\frac1{1-\gamma}$, và viết cả $\mathcal L_{\theta_{\mathrm{old}}}(\theta)$ lẫn $\mathcal L_\pi(\pi')$. Cần chọn một dạng cho cả hai (đề xuất: $\eta$ trên chuỗi vì số gọn, ghi chú nêu quan hệ $\eta=\nu/(1-\gamma)$ một lần) — cùng nhóm B (#5, một tham số hóa).
- *Quy tắc chung:* định nghĩa phát biểu đối tượng (không chỉ hiệu hay tính chất), lý do đứng trước, tính chất đứng sau dưới "Ý nghĩa:"; bảng so sánh hai đại lượng có đủ cột cho cả hai phép tính; mỗi số trong bảng có công thức hoặc nguồn.

### Trao đổi 27 — Mạch 5 và cách trình bày thuật toán (mục #26)

**Tác giả:** "mạch 5 chả hiểu bạn định làm gì luôn" / "mục đích của từng thuật toán không rõ" / "không có cả trình bày liệt kê thuật toán (cả actor-critic của các mạch trước)" / "các slide trình bày kiểu văn nói, không có mục đích rõ ràng, con số đưa ra cũng không hiểu lấy từ đâu".

**Điều phối:**
- *Mục đích dự kiến của mạch 5 (không có trên trang):* TRPO cho bước an toàn gần đúng, nhưng mỗi bước cần ma trận độ cong $F$, gradient liên hợp và tìm theo đường; mỗi bộ đệm chỉ cho một bước. PPO giữ ý "hàm thay thế chỉ tin được gần chính sách cũ" nhưng thay ràng buộc KL bằng phép cắt tỉ số, nên chỉ cần gradient bậc một và dùng lại bộ đệm $K$ lần.
- *Mục đích từng thuật toán (cần một câu bài toán mở mỗi trang thuật toán):*
  - Actor–critic: giảm phương sai của REINFORCE bằng critic và cập nhật từ hệ số lợi thế (mạch 2–3).
  - TRPO: tối đa hàm thay thế trong miền KL để mức giảm $J$ bị chặn (mạch 4).
  - PPO-Clip: xấp xỉ miền tin cậy bằng mục tiêu cắt, chi phí như một bước gradient, dùng lại bộ đệm (mạch 5).
- *Thiếu trang "Thuật toán.":* actor–critic không có; TRPO (L10-4-09) và PPO (L10-5-07) chỉ là sơ đồ khung. Theo CLAUDE.md học phần: tính tay một vòng trước, rồi đầu vào, đầu ra, giả thiết, khởi tạo, tham số, quy tắc cập nhật, thứ tự bước, điều kiện dừng; ví dụ tay, công thức và mã giả khớp nhau. Đề xuất ba trang:
  1. **Thuật toán (actor–critic với GAE).** Đầu vào: $\pi_\theta$, $\hat v_w$, $\gamma$, $\lambda$, bước $\alpha_\theta$, $\alpha_w$. Lặp: thu $N$ lượt bằng $\pi_\theta$; tính $\delta_t$, $\widehat A_t$; $\theta\leftarrow\theta+\alpha_\theta\frac1N\sum_t\widehat A_t\psi_\theta(S_t,A_t)$; $w$ hồi quy $\hat v_w(S_t)$ về $\widehat A_t+\hat v_w(S_t)$. Đầu ra: $\theta$, $w$.
  2. **Thuật toán (TRPO).** Như trên nhưng bước $\theta$: tính $g$; giải $Fx=g$ bằng gradient liên hợp; bước $\sqrt{2\kappa/x^\top Fx}\,x$; tìm theo đường đến khi $\bar D_{\mathrm{KL}}\le\kappa$ và hàm thay thế tăng.
  3. **Thuật toán (PPO-Clip).** Như actor–critic nhưng: lưu $\pi_{\mathrm{old}}(A_t\mid S_t)$; lặp $K$ lần qua bộ đệm, chia lô nhỏ, mỗi lô một bước gradient trên $\frac1{|B|}\sum\min(\rho_t\widehat A_t,\operatorname{clip}(\rho_t,1\pm\epsilon)\widehat A_t)$ trừ mất mát critic; tùy chọn dừng sớm theo KL ước lượng. Tham số $\epsilon$, $K$, cỡ lô.
- *Từng trang mạch 5:*
  - L10-5-00: lời mở "Chỉ chạy Adam trên lượt cũ mà…" văn nói, "Adam" chưa giới thiệu.
  - L10-5-01: không nói mục đích (tối đa hàm thay thế mẫu không ràng buộc thì đi tới đâu). Số không nguồn: bộ đệm hai lượt từ đâu; critic $(1{,}4;1)$ là critic sai của mạch 3; "GAE với $\lambda=1$" nghĩa là $\widehat A_t=G_t-\hat v(S_t)$, nên $s_A$ hành động 1: $G_0=0+0{,}9\cdot0=0$, $\widehat A=-1{,}4$; $\rho=p'_A/p_A=2p'_A$; trung bình theo mẫu tại $s_A$: $\tfrac12[-2{,}8p'_A+(-0{,}8+0{,}8p'_A)]=-0{,}4-p'_A$; cực đại tại $(0;1)$, $J=2{,}7\cdot0+1-0=1$. Lại tham số hóa theo $p'$ (#5).
  - L10-5-02: mục tiêu cắt đưa ra không có lý do từ 5-01 (tỉ số không bị chặn nên hàm thay thế mẫu thưởng việc đi xa, đúng vùng mà mạch 4 nói hàm thay thế sai); ba câu "không thưởng thêm", "Phía bất lợi không bị cắt, gradient kéo về" văn nói. Đề xuất: "Định nghĩa." + bảng hai trường hợp $\widehat A>0$, $\widehat A<0$ với khoảng $\rho$ mà $\ell^{\mathrm{CLIP}}$ hằng.
  - L10-5-03: $\rho=1{,}3\Rightarrow p_B\approx0{,}57$ không có phép tính ($\rho=(1-p)/\tfrac13$).
  - L10-5-04: đổi sang bộ đệm khác ("ba mẫu đúng tần suất") không lý do; công thức nén.
  - L10-5-05: "dừng ở $p_A=0{,}4$, $p_B\approx0{,}73$" không có phép tối đa (tại $s_A$: trên $[0{,}4;0{,}5]$ tổng $=-0{,}8-2p'_A$, dưới $0{,}4$ số hạng hành động 2 không bị cắt nên giảm; tại $s_B$: hằng từ $p'_B=\tfrac{11}{15}$). "Còn thiếu:" là nhãn không cho phép.
  - L10-5-06: "Quán tính của Adam và các lô nhỏ khác vẫn đẩy…" văn nói.
  - L10-5-07: thuật toán chỉ có hình; "Critic hồi quy về $\widehat A_t+\hat v_{\mathrm{old}}(S_t)$" không giải thích.
  - L10-5-08: dòng cuối "cả hai cần một hàm phần thưởng" dẫn sang DPO, nay bỏ (#27).
- *Cấu trúc đề xuất mạch 5:* (1) bài toán: chi phí TRPO và nhu cầu dùng lại bộ đệm; (2) tối đa hàm thay thế mẫu không ràng buộc trên bộ đệm hai lượt, tính đủ, $J$ giảm $0{,}4$; (3) trực giác: chỉ tin hàm thay thế khi $\rho$ gần 1; (4) Định nghĩa mục tiêu cắt + bảng trường hợp + hình; (5) cùng bộ đệm có cắt, tính đủ, $J=1{,}392$; (6) Nhận xét: phép cắt không chặn KL và có thể dừng cả bước tốt; (7) Thuật toán PPO-Clip; (8) so sánh TRPO–PPO. Một bộ đệm cho cả mạch.
- *Quy tắc chung:* mỗi mạch thuật toán mở bằng bài toán mà thuật toán trước để lại; mỗi thuật toán có trang "Thuật toán." dạng liệt kê (không chỉ sơ đồ) với câu bài toán, đầu vào, đầu ra, tham số, các bước đánh số; một bộ dữ liệu cho cả mạch, đổi dữ liệu phải nêu lý do.

### Trao đổi 28 — Bỏ DPO (mục #27)

**Tác giả:** "bỏ phần DPO vì sẽ có trong bài 13" / "bỏ DPO trong hình neo".

**Điều phối:** ghi nhận quyết định, đã thêm vào `NGUYEN-TAC-HOC-PHAN.md` (sau mục P1 Bài 10 Mục 7). Hệ quả cho trang chiếu: tên bài "TRPO và PPO"; luận điểm bìa, mục tiêu, "Nội dung", "Vấn đề trung tâm", bảng tổng kết, bài tập về nhà bỏ phần DPO; số mạch còn 6 (mạch tổng kết thành 6). Hình neo: `so-do-neo-m1.svg` có thẻ "mạch 6 ở khối phần thưởng" và cột liệt kê sáu mạch, `so-do-neo-m7*.svg` có khối phần thưởng/RLHF; bỏ khối phần thưởng khỏi vòng (hoặc để khối cố định không đánh dấu), bỏ `so-do-neo-m6-*`. Trang chỉ mục `index.html` (thẻ Bài 10 ghi "TRPO, PPO và DPO") cũng đổi. Cần chốt khi tổng hợp: ghi chú §7, bài tập 10.18–10.21 của ghi chú, bài tập trong `exercises.md` liên quan DPO, các ngoại lệ GC-RL-18, BT-RL-10, P1 Mục 7 — chuyển sang Bài 13 hay giữ trong ghi chú Bài 10.

### Trao đổi 29 — Mạch tổng kết (mục #28)

**Tác giả:** "Mạch tổng kết không nên nói cụ thể ví dụ (các con số) mà cần rút ra kết luận định tính".

**Điều phối:**
- *Chỗ đang dùng số:* hình neo cuối `so-do-neo-m7*.svg` (dòng "phương sai 0,69, 0,20, 0", "hàm thay thế đoán +0,175, thật −0,05", "dừng ở p = 0,8"); "Vấn đề trung tâm" mục 1 ("hạ phương sai từ $0{,}69$ xuống $0{,}20$"); ba câu hỏi tự kiểm tra đều là phép tính trên chuỗi; bài tập tổng hợp 7-03/7-04 là một ví dụ số.
- *Thiếu phần định tính mà quy định học phần yêu cầu:* bảng `Kết quả | Giả thiết không được bỏ | Công thức hoặc thuật toán` và bảng `Phương pháp | Quy tắc cập nhật | Dữ liệu dùng | Điều kiện dừng` cho bài nhiều thuật toán.
- *Đề xuất nội dung định tính:*
  1. Bảng kết quả: đường cơ sở chỉ phụ thuộc trạng thái không đổi kỳ vọng gradient (giả thiết: không phụ thuộc hành động); dạng lợi thế của gradient (hệ quả); $\delta_t$ với $v_\pi$ đúng là ước lượng không chệch của lợi thế, với critic sai thì chệch; GAE: $\lambda$ cân bằng chệch và phương sai; bổ đề hiệu hiệu năng (chính xác, cần quỹ đạo chính sách mới); hàm thay thế khớp $J$ đến bậc một tại chính sách cũ; chặn cải thiện (cận dưới, phạt theo khoảng cách, thừa số $1/(1-\gamma)^2$).
  2. Bảng phương pháp: REINFORCE, actor–critic, TRPO, PPO-Clip theo các cột quy tắc cập nhật, dữ liệu dùng (một lượt / một bộ đệm một lần / $K$ lần), cách giữ bước gần, bảo đảm.
  3. Vấn đề trung tâm: các câu trả lời có điều kiện, không số.
  4. Hình neo cuối: chỉ tên khối và công cụ thay thế (critic, GAE, hàm thay thế + KL, mục tiêu cắt), không dòng số.
  5. Câu hỏi tự kiểm tra hỏi khái niệm: vì sao đường cơ sở không được phụ thuộc hành động; khi nào $\lambda=1$ được ưa hơn; vì sao hàm thay thế sai khi bước dài; phép cắt có chặn KL không.
- *Cần tác giả chốt:* quy định học phần (CLAUDE.md, mạch kết) đặt một bài tập tổng hợp có lời giải trong mạch kết; bài tập này tất yếu có số. Đề xuất chuyển bài tập PPO-Clip về cuối mạch PPO, mạch tổng kết chỉ giữ phần định tính và trang bài tập về nhà; hoặc giữ bài tập trong mạch kết như ngoại lệ đã ghi.
- *Quy tắc chung:* mạch tổng kết phát biểu kết luận định tính kèm giả thiết; số của ví dụ chỉ ở các mạch nội dung.
