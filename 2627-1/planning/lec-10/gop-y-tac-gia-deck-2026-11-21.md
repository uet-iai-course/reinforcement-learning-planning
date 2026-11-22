# Góp ý của tác giả về deck 10 bản 469a3d5 (2026-11-21)

Tác giả xem deck đã dựng lại (commit `469a3d5`) và góp ý theo từng trang. Mỗi góp ý ghi nguyên văn, kèm quyết định xử lý.

| # | Trang | Góp ý (nguyên văn) | Xử lý |
|---|---|---|---|
| 1 | `L10-3-10` (Thuật toán actor–critic với GAE) | "cần có công thức của \delta_t" | Bước 2 ghi $\delta_t=R_{t+1}+\gamma(1-Z_{t+1})\,\hat v(S_{t+1},w_{\mathrm{old}})-\hat v(S_t,w_{\mathrm{old}})$. Cùng lỗi ở bước 2 của `4-09` (TRPO) và `5-07` (PPO-Clip): "$\widehat A_t$ bằng GAE" không có công thức, nên hai trang này cũng ghi công thức. Quy tắc chung ghi vào `NGUYEN-TAC-HOC-PHAN.md`, phần tinh chỉnh TB31: mọi đại lượng một bước thuật toán tính ra đều có công thức trong bước đó. |
| 2 | `L10-3-10` (bước 4) và các trang trước | "công thức cập nhật w cũng chưa nói ở các slide trước" | Đúng: quy tắc cập nhật critic xuất hiện lần đầu ở lời giải `3-04` và ở `3-10` mà không có trang nào dựng nó (TB24). Thêm trang mới `L10-3-13` "Cập nhật critic" đặt ngay trước `3-04`: bài toán, mục tiêu, mất mát, bước cập nhật, ví dụ trên lượt (i). |
| 3 | `L10-3-10` | "tại sao dùng A_t+v làm target" | Vì $\widehat A_t+\hat v(S_t,w_{\mathrm{old}})=G^\lambda_t$, tức lợi tức λ (định nghĩa GAE ở `3-02`: $\widehat A_t=G^\lambda_t-\hat v(S_t)$). Critic hồi quy về lợi tức λ: $\lambda=0$ cho mục tiêu TD $R_{t+1}+\gamma\hat v(S_{t+1})$, $\lambda=1$ cho lợi tức Monte Carlo $G_t$, cùng sự cân bằng độ chệch–phương sai như hệ số của actor. Trên lượt (i), $\lambda=0{,}5$: $0{,}4+1{,}4=1{,}8=G^{0{,}5}_0$; tại $s_B$: $2+1=3=G_1$. Nội dung này vào trang `3-13`. Căn cứ ghi chú: Thuật toán 10.6 và đoạn "Trong thực hành" (bước hạ gradient của mất mát bình phương), §3.3 bước 4 ($V^{\mathrm{targ}}_t$), dòng "hồi quy critic về lợi tức λ cắt". |
| 4 | thuật ngữ (`4-02`, `4-14`, `4-15`, …) | "HIỆU HIỆU NĂNG --> sai phân hiệu năng, có được không ?"; sau khi nghe đề xuất: "dùng 'chênh lệch hiệu năng'" | Đổi "bổ đề hiệu hiệu năng" thành "bổ đề chênh lệch hiệu năng" ở deck, ghi chú, `outline.md` và các phần hiện hành của storyboard. Quyết định ghi thành VP-RL-10 trong `NGUYEN-TAC-HOC-PHAN.md`. |
| 5 | mạch 4 (TRPO) và ghi chú §4–§5 | "hãy tham khảo đề xuất trình bày mạch về TRPO này và chỉnh sửa" (tệp `De_xuat_trinh_bay_TRPO.docx`, văn bản ở `de-xuat-trinh-bay-trpo-2026-11-21.md`) | Tác giả chọn: sửa cả ghi chú §4 theo đề xuất; trang ý tưởng chứng minh gom thành cụm "Cơ sở lý thuyết" sau trang "Vì sao giới hạn KL kiểm soát sai số". Quy trình: ghi chú §4–§5 → storyboard mạch 4 → hình → deck → năm vai rà → sửa → kiểm cuối. Chi tiết ở mục "Đề xuất TRPO" bên dưới. |

## Đề xuất TRPO (#5): nội dung chính và hình

Thứ tự đề xuất: hiện tượng → câu hỏi → trực giác → mô hình → chứng minh → thuật toán. Hai vấn đề tách bạch: ước lượng gradient tốt (đường cơ sở, critic, GAE; mạch 2–3) và dùng gradient tốt (hướng và độ dài bước; TRPO).

Hai mươi trang chính, năm cụm:
- A. Động cơ: (1) biết hướng đi lên nhưng chưa biết đi bao xa; (2) đánh giá chính sách trước khi thực thi; (3) đổi chính sách cũng làm đổi dữ liệu.
- B. Hàm thay thế: (4) hiệu năng thay đổi vì những yếu tố nào (ba thành phần); (5) bổ đề chênh lệch hiệu năng; (6) đại lượng chưa biết ($\eta_{\pi'}$); (7) giữ nguyên phân bố trạng thái cũ; (8) hiệu chỉnh phân phối hành động (tỉ số); (9) hàm thay thế đã sửa gì, chưa sửa gì.
- C. Từ hàm thay thế đến miền tin cậy: (10) dự báo tốt nhưng thực tế xấu (đóng góp từng trạng thái); (11) khi nào hàm thay thế đáng tin (độ dài bước); (12) thay đổi tham số khác thay đổi hành vi (sigmoid); (13) đo thay đổi chính sách bằng KL; (14) bài toán tối ưu miền tin cậy; (15) vì sao giới hạn KL kiểm soát sai số (chuỗi KL → TV → dịch chuyển phân bố chiếm dụng → sai số).
- D. Giải bài toán TRPO: (16) xấp xỉ bậc một và bậc hai; (17) hình học miền tin cậy (tròn so với ellipse); (18) hướng và độ dài bước tối ưu (gradient tự nhiên).
- E. Từ lý thuyết đến thuật toán: (19) một vòng TRPO; (20) TRPO giải quyết gì, còn khó khăn gì, chuyển sang PPO.

Hình trong đề xuất (dựng lại thành SVG, không dùng ảnh raster):
1. Năm bước: đánh giá chính sách mới (PDL) → dùng lại dữ liệu cũ (hàm thay thế, tỉ số) → nhận diện sai số (phân bố trạng thái) → giới hạn thay đổi (KL, miền tin cậy) → tìm bước tối ưu (Fisher, tìm kiếm lùi).
2. Gradient đúng nhưng bước dài làm giảm hiệu năng.
3. Chuỗi hai trạng thái.
4. Luồng 100 lượt: cũ $(0{,}5;\tfrac23)$: 50 tới $s_B$ (33 nhận 3, 17 nhận 0), 50 nhận 1; mới $(0{,}9;0{,}5)$: 90 tới $s_B$ (45 nhận 3, 45 nhận 0), 10 nhận 1.
5. Ba thành phần: phân bố trạng thái $\eta_{\pi'}$ (chưa biết, thay bằng $\eta_\pi$), phân bố hành động $\pi'(a\mid s)$ (hiệu chỉnh bằng tỉ số), lợi thế cũ $A_\pi$ (ước lượng bằng critic/GAE).
6. Đóng góp từng trạng thái: dự báo $0{,}320$ và $-0{,}225$, tổng $+0{,}095$; thực tế $0{,}320$ và $-0{,}405$, tổng $-0{,}085$.
7. Đường dự báo $0{,}095t$ và thực tế $0{,}095t-0{,}18t^2$, vùng KL $\le0{,}01$; bảng $t=0;0{,}25;0{,}5;1$: dự báo $0;0{,}02375;0{,}0475;0{,}095$, thực tế $0;0{,}0125;0{,}0025;-0{,}085$, sai số $0;0{,}01125;0{,}045;0{,}18$.
8. Sigmoid: bước $0\to1$ làm $p$ tăng $0{,}231$; bước $5\to6$ làm $p$ tăng $0{,}0042$.
9. KL của ba chính sách Bernoulli so với $0{,}5$: $0{,}6$ cho $0{,}0204$, $0{,}9$ cho $0{,}5108$.
10. Chuỗi KL nhỏ → TV nhỏ (Pinsker) → phân bố chiếm dụng ít thay đổi (chặn dịch chuyển) → sai số hàm thay thế được kiểm soát (chặn hiệu năng).
11. Miền Euclid (tròn) với hướng $g$; miền KL (ellipse) với hướng $F^{-1}g$; đường đồng mức của $g^\top\Delta\theta$.
12. Tỉ trọng hai thành phần: gradient thường $40\%/60\%$, gradient tự nhiên $21\%/79\%$ ($g=(0{,}2;0{,}3)$, $F^{-1}g=(8;30)$).
13. Vòng TRPO: thu bộ đệm → critic, GAE, lưu phân phối hành động cũ → tính $g$, giải $Fx=g$ bằng gradient liên hợp → bước ứng viên theo KL bậc hai → kiểm hàm thay thế và KL mẫu (không đạt: thu nhỏ bước) → nhận bước.
14. Ba trực giác: hàm thay thế (dự báo cục bộ), miền tin cậy (giới hạn thay đổi), gradient tự nhiên (hướng theo hình học KL).

Điều phối viên đã kiểm các số mới: KL $0{,}0204$, $0{,}5108$; $\Delta p$ $0{,}2311$, $0{,}0042$; tỉ trọng $8/38=21\%$, $30/38=79\%$; bảng độ dài bước tại $t=0{,}5$.

## Nhận xét website TRPO (#6, 2026-11-22)

| # | Trang | Góp ý (nguyên văn) | Xử lý |
|---|---|---|---|
| 6 | mạch 4, bìa, `1-06`, `6-11`, `6-18` | "Tham khảo các nhận xét này" (tệp `Nhan_xet_website_TRPO_sau_chinh_sua.docx`, văn bản ở `nhan-xet-website-trpo-2026-11-21.md`) | Tác giả chọn (2026-11-22): (1) chứng minh dài chuyển sang mạch "Phụ lục" cuối deck; (2) bìa: "Kiểm soát mức đổi chính sách để giảm nguy cơ suy giảm khi dùng lại lượt đã thu." (18 âm tiết); (3) nâng trần ghi chú lên 33 000 từ (GC-RL-19) để thêm đoạn ba tầng và đoạn hai cách lấy trung bình KL. Năm đề xuất: (1) chuẩn hóa phát biểu bảo đảm cải thiện (bìa, câu hỏi 2 ở `1-06`, `6-11`, `6-18`); (2) sơ đồ tổng thể TRPO ngay sau bài toán miền tin cậy; (3) chứng minh sang phụ lục; (4) câu hỏi nhanh "vì sao gradient tự nhiên cho $J$ thấp hơn" với bảng ba tầng: xấp xỉ tuyến tính $g^\top\Delta$ $0{,}460$ (gradient tự nhiên) so với $0{,}422$ (theo $g$), hàm thay thế $\Delta\mathcal L$ $0{,}357$ so với $0{,}361$, $J$ $1{,}807$ so với $1{,}835$; (5) hai cách lấy trung bình KL: $\bar D_{\mathrm{KL}}=\sum_s\nu^\pi(s)D_{\mathrm{KL}}(s)=0{,}0536$ (tổng trọng số $0{,}145$) và trung bình trên bộ đệm với tần suất mẫu $(\tfrac23;\tfrac13)$: $\widehat D=0{,}359$; $\nu^\pi$ chuẩn hóa $(0{,}690;0{,}310)$ cho $0{,}370$. Điều phối viên đã tính các số. |
