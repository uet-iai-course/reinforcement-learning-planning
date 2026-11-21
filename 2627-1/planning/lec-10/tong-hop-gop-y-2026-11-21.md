# Tổng hợp góp ý của tác giả về deck 10 (2026-11-21)

Nguồn: `gop-y-tac-gia-deck-2026-11-20.md`, mục #1–#28, Trao đổi 1–29. Tác giả yêu cầu (2026-11-21): "Hãy tổng hợp các thảo luận để đưa ra danh sách nguyên tắc mới, danh sách các thay đổi, rồi tiến hành sửa".

## 1. Nhóm lỗi gốc

| Nhóm | Mục | Lỗi gốc |
|---|---|---|
| A. Dùng trước khi dựng | #1, #2, #4, #7, #20, #21 | Ví dụ, ký hiệu, đối tượng ($\psi$, $\theta$, $J$, $\pi'$, $A_\pi(s,\pi')$) xuất hiện trước khi được dựng hoặc định nghĩa; công thức dùng làm dữ kiện không được dẫn. |
| B. Ví dụ và tham số hóa | #5, #8, #9, #20, #25 | Hai ví dụ, hai cách tham số hóa; $J(p)$ lẫn $\theta$; $\pi'$ không có tham số; $\eta$ (trang chiếu) khác $\nu$ (ghi chú). |
| C. Thứ tự phát triển, nối mạch | #6, #10, #15, #22, #26 | Công cụ trước lý do; tên vai trước nhu cầu; trường hợp riêng trước dạng tổng quát; mạch không nêu bài toán; dòng dẫn mạch tối nghĩa. |
| D. Văn phong, thuật ngữ | #11, #12, #13, #17, #18, #20, #23, #25, #26 | Văn nói ở tiêu đề, dòng dẫn, định nghĩa, phát biểu; "trung bình" thay "kỳ vọng"; "lệch/dao động" thay "chệch/phương sai"; nhãn "Còn thiếu:" không cho phép. Gốc: hiểu VP25/TB13 ("chỉ dùng từ sinh viên đã có") thành tránh thuật ngữ. |
| E. Kết quả không phát biểu, không chứng minh | #14, #21, #22, #23, #24, #25 | Bổ đề, mệnh đề, định lý viết thành câu thường, không nhãn, thiếu giả thiết, không ý tưởng chứng minh; TB7 giới hạn 3–4 khối và 1 trang ý tưởng chứng minh làm trầm trọng thêm. |
| F. Bảng, hình, số liệu | #3, #16, #19, #22, #25, #26 | Số không có phép tính trên trang; bảng thiếu cột đầu vào hoặc cột kết quả; tên cột sai đại lượng; đổi bộ dữ liệu giữa chừng. |
| G. Thuật toán | #26 | Không có trang "Thuật toán." nào; actor–critic, TRPO, PPO chỉ có sơ đồ khung. |
| H. Phạm vi và tổng kết | #27, #28 | Bỏ DPO (sang Bài 13); tổng kết dùng số của ví dụ thay vì kết luận định tính. |
| Quy trình | Trao đổi 2, 19 | Người rà ("người thầy", sinh viên) đọc ghi chú nên tự lấp chỗ trống; đếm mật độ bỏ qua công thức, bảng nên trang dồn vẫn đạt. |

## 2. Nguyên tắc mới (TB24–TB33) và các nguyên tắc cũ được sửa

Ghi vào `NGUYEN-TAC-HOC-PHAN.md` §3a, mục F (người dùng 2026-11-21). Mỗi quy tắc nêu mục góp ý làm căn cứ.

- **TB24. Dựng ví dụ trước khi tính** (#2, #4, #7). Trước phép tính đầu tiên trên một ví dụ: môi trường (trạng thái, hành động, phần thưởng, chiết khấu, kết thúc) bằng lời và hình; tham số hóa chính sách; giá trị tham số và chính sách hiện tại; hàm mục tiêu và các giá trị dùng sau, mỗi công thức được dẫn (không đưa làm dữ kiện). Một trang dựng không quá hai đối tượng mới.
- **TB25. Một ví dụ chung cho cả bài, một cách tham số hóa** (#5, #8, #9, #20, #25; thay TB14 "mỗi mạch một ví dụ chạy"). Chọn đối tượng và con số để một ví dụ thể hiện được nhiều ý của bài. Mọi chính sách trong bài viết theo cùng một tham số; đối tượng mới (chính sách mới, critic sai, bộ đệm) có nguồn gốc nêu trên trang; giá trị giới hạn (tham số vô hạn) ghi rõ là giới hạn. Ký hiệu trùng với ghi chú. Ghi chú có thể giữ ví dụ khác; trang chiếu chỉ để lại một câu kết quả của chúng.
- **TB26. Văn học thuật** (#11, #12, #13, #17, #18, #23, #25; sửa cách hiểu VP25, TB13). Tiêu đề, dòng dẫn, định nghĩa, phát biểu dùng thuật ngữ chuẩn đã định nghĩa (đường cơ sở, kỳ vọng, phương sai, ước lượng chệch, phân bố trạng thái, tỉ số xác suất, số lần thăm có chiết khấu), không diễn giải bằng khẩu ngữ ("trừ một mức", "nơi chính sách tới", "đoán/thật", "học dở", "đi quá xa", "dồn bước"). "Kỳ vọng" cho biến ngẫu nhiên, "trung bình trên $N$ mẫu" cho mẫu hữu hạn. VP25 nghĩa là không dùng thuật ngữ trước khi định nghĩa, không phải tránh thuật ngữ. Chỉ dùng nhãn được phép (không "Còn thiếu:", "kiểm:").
- **TB27. Bài toán → trực quan → định nghĩa → kết quả → ví dụ** (#10, #15, #21, #22, #26). Mỗi khái niệm mở bằng câu hỏi nó trả lời; trực quan trên ví dụ chung trước tên và công thức; tên vai (critic, actor) giới thiệu đúng nơi cần; dạng tổng quát trước trường hợp riêng; mạch sau mở bằng điều mạch trước còn thiếu.
- **TB28. Kết quả phát biểu đầy đủ, có ý tưởng chứng minh** (#13, #14, #21, #23, #24; thay TB7 phần "3–4 khối", "tối đa một trang ý tưởng chứng minh", "kết quả khác nêu bằng một câu lời thường"). Mọi kết quả mà trang chiếu dùng mang nhãn (Định nghĩa., Mệnh đề., Bổ đề., Hệ quả., Định lý., Nhận xét.), giả thiết lấy từ ghi chú, kết luận bằng công thức, dòng "Ý nghĩa:" có số minh họa trên mặt trang. Mỗi bổ đề, mệnh đề, định lý, hệ quả có trang "Ý tưởng chứng minh: …" (3–5 bước) hoặc, khi chứng minh một dòng, dòng "Chứng minh." trên cùng trang. Mọi đại lượng trong kết luận được định nghĩa trước kết luận. Định nghĩa phát biểu chính đối tượng, lý do trước, tính chất sau.
- **TB29. Mọi số có đường tính trên trang** (#3, #16, #19, #22, #25, #26; tăng cường TB16). Mỗi số tính được trên trang đó hoặc trang ngay trước. Trước bảng nêu đại lượng cần tính và giá trị đúng để so. Giá trị giả định ghi "giả định" kèm lý do. Xác suất ghi nguồn ($p_B$, $1-p_B$). Bảng có đủ cột đầu vào, cột phép tính và cột kết quả, đồng bộ với hình; bảng so hai đại lượng có đủ cột cho cả hai; tên cột đúng tên đại lượng; dòng cuối kỳ vọng, độ chệch, phương sai có phép tính. Một bộ dữ liệu cho một mạch; đổi dữ liệu phải nêu lý do.
- **TB30. Dòng dẫn mạch và trang mở mạch** (#6, #17, #20, #26; sửa TB3 phần dòng dẫn). Dòng dẫn là một câu học thuật nêu điều sinh viên biết sau mạch, đọc hiểu được trước khi học mạch: không ví dụ chưa giới thiệu, không số không ngữ cảnh. Câu đầu của trang mở mạch nêu bài toán của mạch.
- **TB31. Mỗi thuật toán có trang "Thuật toán." dạng liệt kê** (#26). Câu bài toán (giới hạn của phương pháp trước), "Đầu vào:", "Đầu ra:", tham số, các bước đánh số theo thứ tự thực hiện, khớp ví dụ tay và ghi chú (Thuật toán 10.6, 10.9, 10.16, 10.37, 10.49). Sơ đồ khung chỉ bổ sung.
- **TB32. Tổng kết định tính** (#28; thay TB21 mục (1), (3), (4)). Mạch tổng kết không dùng số của ví dụ: sơ đồ neo cuối chỉ ghi tên khối và công cụ; câu trả lời câu hỏi trung tâm là kết luận định tính kèm điều kiện; bảng phương pháp (quy tắc cập nhật, dữ liệu dùng, cách giữ bước gần, bảo đảm); câu hỏi tự kiểm tra hỏi khái niệm. Bài tập tổng hợp có lời giải đặt ở cuối mạch nội dung cuối (thay TB22 câu "chỉ còn một bài tổng hợp ở tổng kết").
- **TB33. Rà soát** (Trao đổi 2, 19; sửa §3a.E). Vai sinh viên chỉ xem ảnh mặt trang, không đọc ghi chú, storyboard hay ghi chú diễn giả; thêm vai rà văn học thuật (TB26, `no-ai-slop` Detect); số đo mật độ không thay phép thử "mỗi số có đường tính trên trang" (TB29) và "một trang không quá hai đối tượng mới" (TB11, TB24).

## 3. Quyết định đã có của tác giả

- Một ví dụ chung (chuỗi hai trạng thái) cho mọi mạch của trang chiếu; ghi chú giữ hành lang (Ví dụ 10.2) và dẫn $J(p)$ (#4, #9).
- "trung bình" → "kỳ vọng" (#12).
- Văn học thuật (#11).
- Gradient dạng lợi thế là hệ quả của mệnh đề đường cơ sở, có chứng minh (#14).
- Bỏ DPO khỏi trang chiếu và hình neo; sẽ có ở Bài 13 (#27).
- Tổng kết định tính (#28).

## 3a. Quyết định của tác giả khi duyệt bản tổng hợp (2026-11-21)

- DPO: "Bỏ luôn khỏi ghi chú" — cắt §7, bài tập củng cố 10.18–10.21, bài DPO trong `exercises.md`; lưu phần cắt ở `dpo-chuyen-sang-bai-13.md`; GC-RL-18, BT-RL-10, P1 Mục 7 hết hiệu lực cho Bài 10.
- Chính sách mới của mạch 4: phương án (b), $\theta'=(\log9;\,0)$, $\pi'=(0{,}9;\,0{,}5)$: $J(\pi')=1{,}315$, $\Delta J=-0{,}085$, $\Delta\mathcal L=+0{,}095$; trên đoạn từ $\pi$ tới $\pi'$: $\Delta\mathcal L=0{,}095t$, $\Delta J=0{,}095t-0{,}18t^2$. Ghi chú mạch 4 tính lại theo bước này.
- Bài tập tổng hợp PPO-Clip: cuối mạch PPO.

## 4. Danh sách thay đổi

### 4.1 Ghi chú bài giảng (sửa trước, NT3)

- N1. Ví dụ 10.2: dẫn $J(p)=-\frac{2(2-p)}{p(1-p)}$ từ hệ Bellman với $p$ tổng quát, rồi $J(\tfrac12)=-12$, $J'(\tfrac12)=8$, $p^*=2-\sqrt2$ (#4).
- N2. Ví dụ 10.6 (chuỗi hai trạng thái): dẫn $J=2{,}7p_Ap_B+1-p_A$, $v_\pi$, $q_\pi$, gradient $(0{,}2;0{,}3)$ đủ bước; nếu §1 cần (trang chiếu mạch 1 dùng chuỗi), thêm đoạn ngắn về bước dài theo ước lượng một lượt (giữ số đã kiểm: $\alpha=1$: $J=1{,}30$; $\alpha=2$: $J=1{,}22$; $\alpha\to\infty$: $J\to1$) (#8, #9).
- N3. Mệnh đề 10.5(b): nêu rõ là hệ quả của Mệnh đề 10.2 và chứng minh theo hướng đó, không đổi số hiệu (#14).
- N4. "trung bình" → "kỳ vọng" ở mọi chỗ nói kỳ vọng (dòng 59, 911, Ví dụ 10.11 "Lợi thế trung bình theo $\pi'$", …); giữ "trung bình" cho trung bình mẫu (#12, #21).
- N5. Một câu nối $\eta=\nu/(1-\gamma)$ khi phát biểu Bổ đề 10.19 và Định nghĩa 10.21, để trang chiếu dùng $\eta$ trên chuỗi (#25).
- N6. Kiểm các số trang chiếu sẽ dùng có trong ghi chú (bộ đệm hai lượt mạch 5, $J=1$ và $1{,}392$; chặn cải thiện cho bước $(1;0{,}5)$: cận $-5$; bước chỉ đổi $p_B$: $\Delta<0{,}056$; $D_{\mathrm{KL}}(s_A)$); thiếu thì bổ sung vào ví dụ tương ứng.

### 4.2 Trang chiếu (một người biên tập, theo storyboard mới)

Cấu trúc mới: mở đầu + 5 mạch nội dung + tổng kết (6 mạch đánh số).

- Mở đầu: bìa "TRPO và PPO", luận điểm không nhắc DPO; tiên quyết có định nghĩa và ý nghĩa $\psi$ (#1); mục tiêu, Nội dung, sơ đồ neo không DPO (#27).
- Mạch 1 (giới hạn của REINFORCE): dựng chuỗi hai trạng thái (môi trường, $p_s=\sigma(\theta_s)$, $\theta=(0;\log2)$, dẫn $J$, gradient); ba loại lượt, bảng ước lượng REINFORCE đủ cột và kết quả, kỳ vọng, phương sai; bước dài theo ước lượng một lượt làm $J$ giảm. Bỏ hành lang (#2–#5, #7–#9).
- Mạch 2 (đường cơ sở và hàm lợi thế): trực quan trục số lợi tức với $v_\pi(s_A)=1{,}4$; Mệnh đề đường cơ sở + ý tưởng chứng minh; bảng ví dụ; Định nghĩa hàm lợi thế (học thuật); Hệ quả gradient dạng lợi thế + ý tưởng chứng minh; câu hỏi dẫn sang ước lượng một bước $\delta_t$ (với $v_\pi$ đúng, phương sai $0$), bảng đủ cột. Bỏ actor/critic khỏi mạch 2 (#10–#16).
- Mạch 3 (ước lượng lợi thế: độ chệch và phương sai): critic học từ dữ liệu nên sai (giả định $\hat v=(1{,}4;1)$, lý do); bảng một bước / cả lượt với mục tiêu $0{,}4$, kỳ vọng, độ chệch, phương sai; GAE (định nghĩa, mệnh đề, ví dụ); Thuật toán actor–critic với GAE (#15, #17–#19, #26).
- Mạch 4 (hàm thay thế và miền tin cậy): bài toán + $\pi'$ có nguồn gốc ($\theta'_A\to\infty$ ghi rõ là giới hạn, theo quyết định ở mục 5); $A_\pi(s,\pi')$; Bổ đề hiệu hiệu năng + ý tưởng chứng minh + bảng; Định nghĩa hàm thay thế + bảng đủ cột; dạng tỉ số; sai số $\sum_s(\eta_{\pi'}-\eta_\pi)A_\pi(s,\pi')$ + Mệnh đề tiếp xúc; minh họa trên đoạn thẳng; câu hỏi nhanh; $D_{\mathrm{TV}}$ + Định lý chặn cải thiện (công thức) + ý tưởng chứng minh + số; KL + Mệnh đề Pinsker + Hệ quả chặn theo KL; miền tin cậy; gradient tự nhiên; Thuật toán TRPO (#20–#25).
- Mạch 5 (PPO): bài toán (chi phí TRPO, dùng lại bộ đệm); tối đa hàm thay thế mẫu không ràng buộc trên bộ đệm hai lượt, tính đủ; trực giác; Định nghĩa mục tiêu cắt + bảng hai trường hợp; cùng bộ đệm có cắt, tính đủ; Nhận xét giới hạn; Thuật toán PPO-Clip; so sánh TRPO–PPO; bài tập tổng hợp PPO-Clip có lời giải (#26, #28).
- Mạch 6 (tổng kết): sơ đồ neo cuối không số; kết luận định tính có điều kiện; bảng phương pháp; câu hỏi tự kiểm tra về khái niệm; bài tập về nhà (bỏ bài DPO); tài liệu tham khảo (#28).
- Toàn deck: tiêu đề, dòng dẫn học thuật (TB26, TB30); "kỳ vọng"; "chệch/phương sai"; bỏ "Còn thiếu:"; ghi chú diễn giả theo TB9.
- Hình: sơ đồ neo bỏ khối/thẻ DPO và cột mạch 6, đánh lại số mạch; hình neo cuối bỏ dòng số; hình mới cho dựng chuỗi, trục số lợi tức; nhãn hình học thuật ("hàm thay thế", "giá trị thật"); bỏ `so-do-neo-m6-*` và hình hành lang khỏi deck.

### 4.3 Tệp khác

- `index.html`: thẻ Bài 10 "TRPO và PPO", mô tả bỏ DPO.
- `exercises.md`: bảng `Mạch | Mở phần | Bài tập` theo số mạch mới; bài liên quan DPO theo quyết định ở mục 5.
- `outline.md`, `storyboard.md`, `cau-chuyen-deck-2026-11-20.md` (bản mới), `review-log.md`.
- `NGUYEN-TAC-HOC-PHAN.md`: TB24–TB33, đối chiếu TB3, TB7, TB13, TB14, TB21, TB22.

## 5. Quy trình sửa

1. Ghi TB24–TB33 vào `NGUYEN-TAC-HOC-PHAN.md`.
2. Người viết ghi chú sửa N1–N6 → rà toán → điều phối duyệt.
3. Người lập kế hoạch viết lại câu chuyện và storyboard theo mục 4.2 (có cột "sinh viên thấy gì trong 1 phút", nguồn mỗi số) → cổng storyboard.
4. Hình (SVG) → một người biên tập dựng lại deck theo storyboard, từng mạch.
5. Rà lại: sinh viên (chỉ ảnh), toán, văn học thuật (`no-ai-slop` Detect), mạch truyện, chuyên gia RL → biên tập sửa → rà lại phần sửa → kiểm cuối (trình duyệt hai cỡ, lint) → commit, push.
