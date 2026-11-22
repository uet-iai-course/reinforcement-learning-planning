# Kiểm lại độ chính xác sau vòng sửa 2, deck Bài 11, mạch 1–2 (2026-11-22)

- Vai: người rà độ chính xác toán học và thuật toán (chỉ đọc), cùng vai với hai báo cáo trước; sub-agent `general-purpose`, Opus 5.5.
- Đối tượng: hai section đầu của `2627-1/lecture-11-lap-ke-hoach-dua-tren-mo-hinh.html` sau vòng sửa 2, theo `sua-vong2-mach12-2026-11-22.md`.
  - Trang đã kiểm: 1-02, 1-03, 1-04, 1-05, 1-06, 1-07, 1-09, 2-03, 2-07, 2-08, 2-09, 2-10, 2-13, 2-14, 2-15, 2-16, 2-17, 2-18, 2-19. Tôi cũng đọc lại 2-04, 2-06, 2-11, 2-12 để đối chiếu.
  - Hình: 3 SVG mới và 11 SVG sửa.
- Nguồn đối chiếu: `materials/lec-11/lecture-note.md` (3609690).
- Cách kiểm:
  - Đọc từng trang và ghi chú diễn giả.
  - Tính lại số bằng script của hai lượt trước.
  - Đọc nhãn và tọa độ SVG.
  - Chụp 1600×900 mười trang (`Reveal.configure({transition:'none'})`, `Reveal.slide(h,v,99)`): không lỗi trang, không `.katex-error`. Ảnh nằm trong scratchpad của phiên.

## 1. Bảy phát hiện của lượt kiểm lại trước

| phát hiện | trạng thái | bằng chứng |
|---|---|---|
| Trung bình, L11-1-04 mục tiêu 4 ("$m=70$… chọn sai") | đã sửa đúng | Mặt trang: "rollout xếp $\downarrow$ trên $\rightarrow$ với xác suất không quá $0{,}05$". Ghi chú diễn giả: $\Delta=0{,}2072$, $m=70$ cho $0{,}0496$ (Ví dụ 11.14); bốn hành động cần $m=75$, chặn $0{,}0483$ (Bài tập 11.8, dòng 1846). Tính lại: $e^{-70\cdot0{,}042913}=0{,}0496$; $e^{-75\cdot0{,}042913}+2e^{-75\cdot0{,}073128}=0{,}0400+0{,}0083=0{,}0483$. |
| Trung bình, L11-2-04 mốc "lượt 1, C = 2" | đã sửa đúng | Hình ghi "C = 2: 0,2828" và dưới trục "C = 2 lần thử ấn định trước: 0,2828 là độ lệch chuẩn của p̂ qua các nhóm hai lần thử". Dòng đầu chỉ so $\lvert0{,}5-0{,}8\rvert=0{,}3$, không áp Mệnh đề 11.5. Ghi chú diễn giả nói rõ số đếm của lượt thứ nhất không thỏa giả thiết và cho $\mathbb E\hat p=0{,}8926$ (đúng: $4\cdot(-\ln0{,}8)=0{,}89257$). Tọa độ điểm không đổi: $(172{,}6;\,164{,}0)$, $(584;\,304{,}8)$. |
| Nhẹ, L11-2-16 Diễn giải | đã sửa đúng | "khi bước chọn cặp lấy $(\mathrm F,\rightarrow)$ rồi $(\mathrm K,\rightarrow)$…". Ghi chú diễn giả: chọn $(\mathrm A,\rightarrow)$ hai lần cho $0$, đúng vì $\max_aQ(\mathrm B,a)=0$. |
| Nhẹ, L11-1-09 "cập nhật lập kế hoạch đầu tiên" | đã sửa đúng | "…đầu tiên của bước thứ năm trong Dyna-Q". |
| Nhẹ, L11-2-09 hình chuỗi | đã sửa đúng | "thử →: sang C với xác suất 0,8", "(e) ghi kết cục quan sát". Ghi chú diễn giả nêu trường hợp trượt $0{,}2$: mô hình ghi lại $(0,\mathrm B)$, $\ell$ về $0$, khớp Định nghĩa 11.11. |
| Nhẹ, L11-1-04 nguồn $0{,}2016\to0{,}8566$ | đã sửa đúng | "(Mệnh đề 11.23, Ví dụ 11.13)". |
| Nhẹ, L11-1-05 "trang đầu mỗi mạch" | đã sửa đúng | "trang đầu mạch 2 dùng lại sơ đồ này". |

## 2. Phát hiện mới

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa |
|---|---|---|---|---|
| nhẹ | L11-2-18, hàng "mọi cặp chọn vô hạn lần"; ghi chú diễn giả "Ba giả thiết đầu hỏng vì mô hình học dần" | Mặt trang ghi "chưa có bảo đảm: (f) chỉ chọn trong các cặp đã thử". Đúng là bước (f) không tự bảo đảm điều này. Nhưng ghi chú diễn giả kết luận giả thiết này "hỏng", và kết luận đó không đúng trong giới hạn. Với $\varepsilon>0$, mê cung hữu hạn và mọi ô tới được từ $\mathrm A$, mọi cặp hầu chắc chắn được thử thật sau hữu hạn bước. Sau đó, mỗi bước (f) chọn mỗi cặp đã thử với xác suất dương, nên mỗi cặp được chọn vô hạn lần, hầu chắc chắn. Các giả thiết thật sự hỏng là "mô hình cố định" và Robbins–Monro; "xác định ở mọi cặp" chỉ hỏng ở thời điểm đang xét. | Thuật toán 11.8 bước (b), (f) (dòng 383, 387); Nhận xét 11.10 (dòng 414) chỉ nêu cặp chưa thử giữ giá trị khởi tạo và mô hình đổi sau mỗi bước thật; lời giải Bài tập 11.4 câu (b) (dòng 1776) nêu "mô hình chỉ xác định ở bốn cặp đã thử và đổi sau mỗi bước thật", "$\alpha=0{,}5$ hằng", không nói về "vô hạn lần". | Ghi chú diễn giả: "Giả thiết 'vô hạn lần' không do bước (f) bảo đảm; nó chỉ thỏa khi bước $\varepsilon$ đưa tác tử thử mọi cặp. Giả thiết hỏng chắc chắn là 'mô hình cố định' và Robbins–Monro." Mặt trang có thể giữ nguyên, hoặc ghi "chỉ thỏa nhờ bước $\varepsilon$; (f) chỉ chọn trong các cặp đã thử". |
| nhẹ | L11-2-08, dòng "Lưu ý:" | "(f) rút một cặp $(R,S')$ đã quan sát" không nói phân phối rút. Rút đều trên các kết cục *khác nhau* chỉ trùng $\hat p$ khi các số đếm bằng nhau. Ví dụ, với $C(\mathrm A,\rightarrow,\mathrm A)=1$, $C(\mathrm A,\rightarrow,\mathrm B)=4$, $\hat p(\mathrm B\mid\mathrm A,\rightarrow)=0{,}8$, còn rút đều trên hai kết cục cho $0{,}5$. Ý ghép cặp $(R,S')$ thì đúng. | Câu sau Định nghĩa 11.2 (dòng 193): "rút một mẫu theo nó là rút đều một lần thử cũ của cặp"; "Trong thực hành" sau Nhận xét 11.10 (dòng 417): "(f) rút $(\tilde R,\tilde S')$ theo $\hat p$". | "…(f) rút đều một lần thử cũ, tức một cặp $(R,S')$ theo $\hat p$." |
| nhẹ | L11-2-10 (mặt trang và hình `so-do-cap-nhat-hai-lan-thu-slide.svg`, nhãn "cả hai cây: mô hình đếm của (A,→) sau lượt thứ nhất") | Các giá trị $\max_aQ(\mathrm B,a)=0{,}6$ và $\max_aQ(\mathrm A,a)=0{,}4$ là giá trị giả định của Ví dụ 11.10. Thế nhưng chúng đứng cạnh nhãn "sau lượt thứ nhất". Sau lượt thứ nhất, bảng thật có $Q(\mathrm A,\cdot)=Q(\mathrm B,\cdot)=0$ (Ví dụ 11.6: chỉ $\mathrm K$, $\mathrm F$ khác $0$), nên người đọc có thể hiểu $0{,}6$ và $0{,}4$ là giá trị sau lượt. | Ví dụ 11.10, Dữ kiện (dòng 496): "giả sử $\max_aQ(\mathrm B,a)=0{,}6$, $\max_aQ(\mathrm A,a)=0{,}4$". | Thêm "giả sử" trên mặt trang ("Ví dụ 11.10: $b=2$; giả sử $\max_aQ(\mathrm B,a)=0{,}6$, $\max_aQ(\mathrm A,a)=0{,}4$"), hoặc đổi nhãn hình thành "mô hình đếm của (A,→) sau lượt thứ nhất; giá trị max Q giả định". |
| nhẹ | L11-2-15, dòng "Chứng minh." | Dòng chứng minh chỉ nêu Bước 1 ("$Q$ là trung bình của $k$ mục tiêu mẫu"). Bước quyết định ra $\sqrt{(b-1)/(bk)}$ là $\mathbb E\sigma^2=(b-1)/b$, rồi lấy kỳ vọng có điều kiện; bước này chỉ có ở ghi chú diễn giả. Với nhãn "Chứng minh.", dòng này chưa đủ để suy ra kết luận trên trang. | Chứng minh Mệnh đề 11.15, Bước 1–3 (dòng ~536–545). | Hoặc bổ sung: "…nên $\mathbb E(Q_k-\bar y)^2=\sigma^2/k$; với $b$ giá trị độc lập phương sai $1$, $\mathbb E\sigma^2=(b-1)/b$." Hoặc đổi nhãn thành "Ý tưởng chứng minh:" (NT19). |

Tổng phát hiện mới: 0 chặn bàn giao, 0 nghiêm trọng, 0 trung bình, 4 nhẹ.

## 3. Bốn điểm điều phối viên hỏi riêng

- **L11-1-06, dòng $v(d)=0{,}8\gamma\,v(d-1)+0{,}2\gamma\,v(d)$ với $d\ge2$: đúng.**
  - Dòng này trùng (dòng 89–90) $v(d)=0{,}72\,v(d-1)+0{,}18\,v(d)$, với $0{,}72=0{,}8\gamma$, $0{,}18=0{,}2\gamma$, nên $v(d)=\tfrac{0{,}72}{0{,}82}v(d-1)=0{,}8780\,v(d-1)$.
  - Nó cũng khớp $\rho=\tfrac{0{,}8\gamma}{1-0{,}2\gamma}=0{,}8780$ ở dòng 1338.
  - Trang giới hạn đúng ở $d\ge2$. Với $d=1$ có thêm phần thưởng: $v(1)=0{,}8+0{,}18\,v(1)$, ghi ở ghi chú diễn giả $0{,}8/0{,}82=0{,}9756$.
  - Lặp giá trị tới hội tụ cho lại $0{,}9756$; $0{,}8566$; $0{,}7522$; $0{,}6604$. Lớp `me-cung-gia-tri-slide.svg` ghi đúng các số này ở đúng ô.
- **L11-2-15, giả thiết: đúng với Mệnh đề 11.15(b).** Giá trị kế $y_{s'}=\gamma\max_{a'}Q(s',a')$ (dòng 523) là biến ngẫu nhiên độc lập, cùng kỳ vọng, phương sai $1$, độc lập với việc rút mẫu (dòng 527), không đổi trong $k$ cập nhật (Điều kiện áp dụng). Ghi chú diễn giả nói rõ phương sai $1$ áp cho $y_{s'}$ đã gồm $\gamma$. Chỉ có dòng "Chứng minh." thiếu bước (nhẹ, ở trên).
- **L11-2-08, rút kết cục ghép cặp $(R,S')$: đúng về ý.** Rút đều một lần thử cũ trả cặp $(R,S')$ theo phân phối thực nghiệm chung, đúng với dòng 193. Câu chữ thiếu "đều/theo $\hat p$" (nhẹ, ở trên).
- **L11-2-18, "chưa có bảo đảm mọi cặp được chọn vô hạn lần":** mặt trang đúng theo nghĩa bước (f) không tự bảo đảm. Ghi chú diễn giả quá tay khi gọi giả thiết này là "hỏng" (nhẹ, ở trên).

## 4. Trang và hình đã kiểm

| trang | kết luận | số và nhãn đã kiểm |
|---|---|---|
| L11-1-06 (`me-cung-luat-slide.svg`, `me-cung-gia-tri-slide.svg`) | không lỗi | luật $0{,}8/0{,}2$, $\gamma=0{,}9$, đích $+1$; $v_*$ bốn mức; $0{,}72/0{,}82=0{,}8780$; đường ngắn nhất A→B→F→K→Z dài 4 |
| L11-1-09 (`luot-mot-q-learning-slide.svg`, `luot-mot-ql-ket-qua-slide.svg`, `luot-mot-ke-hoach-slide.svg`) | không lỗi | mục tiêu $0,0,0,0,1$; bước 4: $0+0{,}9\cdot0=0$; bước 5: $0+0{,}5[1-0]=0{,}5$; mô hình: $0{,}9\cdot0{,}5=0{,}45$, $0+0{,}5[0{,}45-0]=0{,}225$; nhãn "S′ = K, R = 0; mục tiêu 0,45"; thứ tự lượt bấm đúng |
| L11-1-07 | không lỗi | $0$ và $0{,}225$; một lần thử $(\mathrm F,\rightarrow)$ tới $\mathrm K$: $\hat p=1$, $p=0{,}8$; ghi chú diễn giả: Q-learning để bốn hành động tại $\mathrm F$ hòa ($Q(\mathrm F,\cdot)=0$), bảng sau cập nhật chọn $\rightarrow$ |
| L11-1-02 (`mo-hinh-hai-dang-slide.svg`) | không lỗi | $(\mathrm Z,+1)$: $0{,}8$; $(\mathrm K,0)$: $0{,}2$; "MDP hữu hạn (mạch 2, 3, 5)" khớp Bảng ký hiệu; Robbins–Monro theo cặp |
| L11-1-05 (`so-do-neo-slide.svg`) | không lỗi | nhánh 3 "chọn hành động kế tiếp", nhánh 4 "thực hiện hành động đầu tiên" (Định nghĩa 11.37, Thuật toán 11.38), nhánh 5 "chuyển tiếp kéo dài nhiều bước" (§5.1–5.2) |
| L11-1-03 | không lỗi | $C$ gấp $10$: độ lệch chuẩn giảm $\sqrt{10}=3{,}162$ lần, $0{,}1789\to0{,}0566$; mục tiêu 2 ở ghi chú diễn giả: (d) $0{,}5$, (e) $(\mathrm K,\rightarrow)\mapsto(+1,\mathrm Z)$, (f) $0{,}225$ rồi $0{,}75$; $0{,}54\to0{,}64$; $0{,}3146$ |
| L11-1-04 | không lỗi | như mục 1; $1{,}4481$, $1{,}7558$, $(8;\,4)$, $2{,}88$, $0{,}6x$, $0{,}8780$, $V_2(\mathrm A)=0{,}6604$ |
| L11-2-03 (`bang-dem-hai-nhanh-slide.svg`) | không lỗi | "mô hình đếm: 5 bước thật, 4 cặp đã thử"; $1/2$, $1/2$; $C=1$ ba cặp; $\hat r=1$ |
| L11-2-04 (`hai-loai-bat-dinh-A-slide.svg`) | không lỗi | như mục 1 |
| L11-2-13 (`hai-gioi-han-duong-di-slide.svg`) | không lỗi | "Ý nghĩa" $\mathbb E_{\hat p}[R+\gamma\max_{a'}Q(S',a')]$ là vế phải toán tử Bellman tối ưu dạng $q$ của mô hình áp lên $Q$ hiện tại (dòng 22, 232); dải "mô hình đủ các cặp, cố định, kết cục lưu đều đi đúng": $0{,}729;0{,}81;0{,}9;1$; Diễn giải có đủ điều kiện |
| L11-2-07 | không lỗi | mô hình sau (e) từng bước; "(mô hình đếm: A:1, B:1)" đúng; bước 5: $0{,}5$, $0{,}225$, $0{,}75$ |
| L11-2-16 | không lỗi | ô đóng khung $0{,}5$ ở (d) và trong mục tiêu (f) đầu; $1/1/0{,}5$; $0{,}45/0{,}45/0{,}225$; $1/0{,}5/0{,}75$; đảo thứ tự $0{,}3375$ |
| L11-2-17 (`kien-truc-dyna-def-slide.svg`) | không lỗi | ví dụ $(\mathrm A,\rightarrow,0,\mathrm B)$ rồi (f) lấy $(\mathrm F,\rightarrow)$ khớp dữ kiện Bài tập 11.4; Định nghĩa 11.9 |
| L11-2-08 | một nhẹ | Thuật toán 11.8 khớp từng dòng |
| L11-2-12 | không lỗi | không đổi; $0$; $0{,}45$; $0{,}2025$; $0{,}10125$ |
| L11-2-18 | một nhẹ (ghi chú diễn giả) | các hàng còn lại đúng; $\sum\alpha^2=\infty$ |
| L11-2-14 | không lỗi | cột "kết cục khi đi đúng": $(\mathrm F,\rightarrow)$ ở yên (cửa đóng), $(\mathrm B,\rightarrow)$ sang $\mathrm C$ |
| L11-2-09 (`chuoi-thuong-tham-do-slide.svg`) | không lỗi | $0{,}01\sqrt{400}=0{,}2$; $0{,}54/0/0{,}54$; $0{,}74/0{,}2/0{,}64$ |
| L11-2-10 (`so-do-cap-nhat-hai-lan-thu-slide.svg`) | một nhẹ | $0{,}45$; $0{,}54$; $0{,}36$; $b=2$ |
| L11-2-15 | một nhẹ | giả thiết như mục 3 |
| L11-2-19 (`cap-nhat-mau-sai-so-slide.svg`) | không lỗi | $\sqrt{99/1000}=0{,}3146$; tọa độ $x=96+170\,k/b$, $y=300-260\cdot$sai số: $b=2$, $k=1..4$ cho $116{,}2/170/193{,}9/208{,}1$; chấm xanh $(113;\,218{,}2)$; chấm xám $(1;0)$ tại $(266;300)$; nhãn "mức 1 là sai số ban đầu giả định" khớp Phạm vi của Mệnh đề 11.15 |

Kết luận: bảy phát hiện của lượt kiểm lại trước đã sửa đúng, kể cả hai phát hiện trung bình. Vòng 2 không sinh phát hiện chặn bàn giao, nghiêm trọng hay trung bình nào. Có 4 phát hiện nhẹ, đều ở câu chữ hoặc nhãn: một câu ghi chú diễn giả quá tay (2-18), phân phối rút ở bước (f) (2-08), thiếu "giả sử" (2-10), dòng chứng minh chưa đủ bước (2-15). Mọi số, công thức và nhãn trong 14 hình đều khớp ghi chú.
