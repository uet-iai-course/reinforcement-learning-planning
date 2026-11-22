# Kiểm lại độ chính xác sau vòng sửa 1, deck Bài 11, mạch 1–2 (2026-11-22)

- Vai: người rà độ chính xác toán học và thuật toán (chỉ đọc), cùng vai với `ra-soat-chinh-xac-mach12-2026-11-22.md`; sub-agent `general-purpose`, Opus 5.5.
- Đối tượng: hai section cấp cao đầu của `2627-1/lecture-11-lap-ke-hoach-dua-tren-mo-hinh.html` sau vòng sửa 1 (25 trang: L11-1-01, 1-06, 1-09, 1-07, 1-02, 1-05, 1-03, 1-04; L11-2-00, 2-03, 2-06, 2-13, 2-04, 2-07, 2-16, 2-08, 2-17, 2-11, 2-12, 2-18, 2-14, 2-09, 2-10, 2-15, 2-19) và 14 SVG mới liệt kê trong `sua-vong1-mach12-2026-11-22.md` §3.
- Nguồn đối chiếu: `materials/lec-11/lecture-note.md` (3609690), `exercises.md`; Bài 06, Định nghĩa 06.19.
- Cách kiểm:
  - Tính lại mọi số bằng script Python, dùng lại script của lượt trước (lặp giá trị, Q-learning, Dyna-Q, Bài tập 11.4, độ lệch chuẩn, Dyna-Q+, (2.5)).
  - Đọc tọa độ SVG của hai đồ thị mới.
  - Chụp 1600×900 sau `Reveal.configure({transition:'none'})`: 13 trang, cùng ba trạng thái dựng dần của L11-1-09. Không có lỗi trang, không có `.katex-error`.
  - Ảnh nằm trong scratchpad của phiên, không trong repo.

## 1. Bảy phát hiện của lượt trước

| phát hiện lượt trước | trạng thái | bằng chứng |
|---|---|---|
| Trung bình 1: "Dyna-Q không thử lại $(\mathrm B,\rightarrow)$", "không sửa được" (L11-2-09, 2-14, hình cũ) | đã sửa đúng | L11-2-09 dòng đầu: "Chính sách tham lam không chọn… Chỉ bước $\varepsilon$ thử lại cặp này."; bảng L11-2-14: "không chọn; chỉ bước $\varepsilon$ thử lại"; ghi chú diễn giả L11-2-14 nêu $\varepsilon$-tham lam. Hình cũ không còn dùng. Câu "tương tự Ví dụ 8.2 và 8.3" đã bỏ khỏi ghi chú diễn giả. |
| Trung bình 2: $0{,}729$ không điều kiện (ghi chú diễn giả L11-2-08) | đã sửa đúng | "có thể cho $0{,}729$… khi kết cục gần nhất trên đường ngắn nhất đều là đi đúng (Tình huống 11.2)". L11-2-13 nêu đủ ba điều kiện và trường hợp trượt cho $0$. |
| Nhẹ: "$\hat q_*\ne q_*$ vì…" (L11-2-04) | đã sửa đúng | Câu đã bỏ; dòng mới "$\hat p(\mathrm B\mid\mathrm A,\rightarrow)=1/2$ từ $C=2$ lần thử, còn $p=0{,}8$" khớp ghi chú dòng 249. |
| Nhẹ: "Bước (f) chỉ rút một trong hai kết cục" (L11-2-10) | đã sửa đúng | "Với mô hình đếm, bước (f)…"; ghi chú diễn giả nói rõ mô hình lưu kết cục gần nhất chỉ giữ $(0,\mathrm B)$. |
| Nhẹ: thiếu $\gamma$, bước (f) một tầng (L11-2-08) | đã sửa đúng | Đầu vào có $\gamma\in[0,1)$; (f) chọn trạng thái đã gặp rồi hành động đã thử tại đó, khớp dòng 370, 387. |
| Nhẹ: giả thiết Mệnh đề 11.15(b) (L11-2-15) | đã sửa đúng | Đủ "biến ngẫu nhiên độc lập, cùng kỳ vọng, phương sai $1$, độc lập với việc rút mẫu, không đổi trong $k$ cập nhật", khớp dòng 527 và Điều kiện áp dụng. |
| Nhẹ: Robbins–Monro theo $t$ (ghi chú diễn giả L11-1-02) | đã sửa đúng | $\sum_n\alpha_n(s,a)=\infty$, $\sum_n\alpha_n(s,a)^2<\infty$ hầu chắc chắn với mọi cặp, khớp Định nghĩa 06.19. |

## 2. Phát hiện mới

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa |
|---|---|---|---|---|
| trung bình | L11-1-04, mục tiêu 4 (mặt trang) | "tính số mô phỏng $m=70$ để rollout chọn sai với xác suất không quá $0{,}05$" sai với bốn hành động tại $\mathrm F$. $m=70$ chỉ chặn xác suất đảo thứ tự một cặp, $\downarrow$ xếp trên $\rightarrow$. Để chặn xác suất không chọn hành động tốt nhất trong bốn hành động, cần $m=75$. | Ví dụ 11.14 (dòng 752–761): chặn $\Pr\{\bar G(\downarrow)\ge\bar G(\rightarrow)\}\le e^{-70\Delta^2}=0{,}0496$. Mệnh đề 11.24, Điều kiện áp dụng (dòng ~741): với hơn hai hành động phải cộng các chặn. Bài tập 11.8, lời giải (dòng 1846): $e^{-m\Delta^2}+2e^{-m\Delta'^2}$ bằng $0{,}0616$ tại $m=70$, $0{,}0483$ tại $m=75$; dòng 1848: "Với hai hành động, $m=70$ đã đủ". Tính lại: $\Delta=0{,}20716$, $\Delta'=0{,}388554-0{,}118131=0{,}27042$; $e^{-70\cdot0{,}042913}+2e^{-70\cdot0{,}073128}=0{,}0496+0{,}0120=0{,}0616$. | "…tính số mô phỏng $m=70$ để rollout xếp $\downarrow$ trên $\rightarrow$ với xác suất không quá $0{,}05$", hoặc giữ "chọn sai" và đổi thành $m=75$ (Bài tập 11.8). |
| trung bình | L11-2-04 (hình `hai-loai-bat-dinh-A-slide.svg`, nhãn "lượt 1, C = 2: 0,2828"; ghi chú diễn giả "bằng $0{,}2828$ tại $C=2$ sau lượt thứ nhất") | Trang áp Mệnh đề 11.5 cho chính số đếm của lượt thứ nhất, trong khi số đếm đó vi phạm giả thiết "$C$ chọn trước khi thử" đặt ngay trên trang. Tác tử chỉ thử lại $(\mathrm A,\rightarrow)$ khi lần trước trượt và nó còn ở $\mathrm A$, nên $C(\mathrm A,\rightarrow)$ trong lượt phụ thuộc kết quả các lần thử: thử tới lần đi đúng đầu tiên. Khi đó $\hat p=1/C$, ước lượng chệch, và độ lệch chuẩn của nó không phải $0{,}4/\sqrt2$. | Mệnh đề 11.5, Giả thiết và Điều kiện áp dụng (dòng 264, 269). Phản ví dụ "Bỏ '$C$ cố định trước'" (dòng 286) là cùng loại quy tắc dừng; chính ghi chú diễn giả của trang nêu phản ví dụ đó. Tính lại với $\Pr\{C=k\}=0{,}2^{k-1}\cdot0{,}8$: $\mathbb E\hat p=\mathbb E[1/C]=\tfrac{0{,}8}{0{,}2}\,(-\ln0{,}8)=0{,}8926\ne0{,}8$. Ví dụ 11.4 của ghi chú tránh điều này bằng các số đếm giả định ("Giả sử…") tại $(\mathrm F,\rightarrow)$. | Bỏ chữ "lượt 1" ở mốc $C=2$ và câu "sau lượt thứ nhất" trong ghi chú diễn giả. Ghi mốc là "$C=2$ lần thử ấn định trước". Hoặc trở lại các số đếm giả định của Ví dụ 11.4. Dòng đầu trang ("$\hat p=1/2$ từ $C=2$ lần thử") vẫn đúng như một dữ kiện. |
| nhẹ | L11-2-16, "Diễn giải:" | "$Q(\mathrm F,\rightarrow)$… bằng $0{,}225$ với Dyna-Q ($n=2$)" nêu như kết quả tất định. Thật ra kết quả phụ thuộc giả định của ví dụ về bước chọn cặp: lấy $(\mathrm F,\rightarrow)$ rồi $(\mathrm K,\rightarrow)$. Bước (f) chọn ngẫu nhiên, nên lần chọn khác cho số khác: chọn $(\mathrm A,\rightarrow)$ hai lần cho $0$; đảo thứ tự hai cặp vẫn cho $0{,}3375$. | Ví dụ 11.6, dòng ~355: "Giả sử bước chọn cặp lấy $(\mathrm F,\rightarrow)$ rồi $(\mathrm K,\rightarrow)$". Thuật toán 11.8 bước (f): chọn ngẫu nhiên. | "…bằng $0{,}225$ với Dyna-Q ($n=2$), khi bước chọn cặp lấy $(\mathrm F,\rightarrow)$ rồi $(\mathrm K,\rightarrow)$." |
| nhẹ | L11-1-09, ghi chú diễn giả | Cập nhật lượt bấm thứ hai được gọi là "cập nhật lập kế hoạch đầu tiên của Dyna-Q". Nhưng ở bốn bước thật đầu, Dyna-Q đã chạy $2\times4$ cập nhật lập kế hoạch, mục tiêu đều bằng $0$ (L11-2-07 cũng ghi như vậy). | Ví dụ 11.6, "Bốn bước đầu" (dòng ~345); L11-2-07, hàng 1–4. | "…đó là cập nhật lập kế hoạch đầu tiên của bước thứ năm" hoặc "…cập nhật lập kế hoạch đầu tiên làm đổi bảng". |
| nhẹ | L11-2-09, hình `chuoi-thuong-tham-do-slide.svg` (ô "bước thật: sang C") | Mê cung có trượt, nên khi tác tử chọn $\rightarrow$ tại $\mathrm B$, nó sang $\mathrm C$ với xác suất $0{,}8$. Với xác suất $0{,}2$ nó ở yên, và bước (e) của mô hình tất định lại ghi $(0,\mathrm B)$. Hình nêu kết cục đi đúng như chắc chắn. Diễn giải của Ví dụ 11.8 trong ghi chú cũng lược ý này. | Ví dụ 11.1, Động lực (dòng 86); Thuật toán 11.8 bước (e); ghi chú diễn giả L11-2-14 đã nêu xác suất $0{,}8$ cho $\mathrm B$. | Ô thứ ba: "đi đúng (xác suất $0{,}8$): sang C", hoặc thêm một câu vào ghi chú diễn giả. |
| nhẹ | L11-1-04, ghi chú diễn giả | Câu nêu tính chất cải thiện của rollout, "$0{,}2016$ lên $0{,}8566$", dẫn nguồn "(Ví dụ 11.14, 11.15, 11.16)". Số này nằm ở Ví dụ 11.13 và gắn với Mệnh đề 11.23, không ở 11.14–11.16. | Ví dụ 11.13 (dòng 710–727, diễn giải dòng 725); §6.2 mục 2 dẫn "(Ví dụ 11.13)". | Thêm "Ví dụ 11.13, Mệnh đề 11.23" vào câu và vào dòng Nguồn. |
| nhẹ | L11-1-05, ghi chú diễn giả | "trang đầu mỗi mạch dùng lại sơ đồ này" chưa đúng với deck hiện tại: chỉ L11-2-00 dùng sơ đồ neo, trang tiêu đề mạch 3–6 chưa dùng. Đây là khẳng định về deck, không phải về toán. | `sua-vong1-mach12-2026-11-22.md` §5, gạch đầu thứ 4; `grep so-do-neo` trong deck chỉ ra L11-1-05 và L11-2-00. | Đổi thành "trang đầu mạch 2 dùng lại sơ đồ này", hoặc giữ câu cũ và thêm sơ đồ vào mạch 3–6 khi sửa các mạch đó. |

Tổng phát hiện mới: 0 chặn bàn giao, 0 nghiêm trọng, 2 trung bình, 5 nhẹ.

## 3. Các điểm điều phối viên hỏi riêng

- **(a) "Ý nghĩa:" ở L11-2-13: đúng.**
  - Với $(R,S')\sim\hat p(\cdot,\cdot\mid s,a)$ và $Q$ cố định, $\mathbb E[R+\gamma\max_{a'}Q(S',a')]=\sum_{s',r}\hat p(s',r\mid s,a)[r+\gamma\max_{a'}Q(s',a')]$.
  - Vế phải là toán tử Bellman tối ưu dạng $q$ của MDP của mô hình áp lên $Q$ hiện tại. Dạng $q$ của phương trình Bellman tối ưu ở Kiến thức tiên quyết, dòng 22; phân phối của mẫu ở Bước 2 chứng minh Mệnh đề 11.4, dòng 232.
  - Ghi chú diễn giả viết đúng biểu thức này.
  - Câu không có nguyên văn trong ghi chú, nhưng suy ra trực tiếp từ hai chỗ trên. Không ghi là lỗi. Nếu cần khớp NT2 theo nghĩa hẹp, có thể đề xuất tác giả thêm một câu sau Bước 2 (NT3).
- **(b) L11-2-04 đổi biến cố sang $(\mathrm A,\rightarrow)\to\mathrm B$.**
  - Các số vẫn đúng, vì $p(\mathrm B\mid\mathrm A,\rightarrow)=0{,}8$, bằng $p(\mathrm K\mid\mathrm F,\rightarrow)$. Cụ thể $\sqrt{0{,}16/C}$ cho $0{,}4$; $0{,}2828$; $0{,}0566$, và tọa độ SVG khớp: $y=340-622{,}2\sigma$ cho $164{,}0$ và $304{,}8$; trục log đúng.
  - Ghi chú diễn giả có nói Ví dụ 11.4 tính cùng các số tại $(\mathrm F,\rightarrow)$.
  - Vấn đề duy nhất là gắn mốc $C=2$ với lượt thứ nhất (phát hiện trung bình thứ hai ở trên).
- **(c) Hai trang mục tiêu.**
  - Mục tiêu 1, 2, 3, 5, 6, 7 đúng số và đúng việc. Cụ thể: $0{,}1789\to0{,}0566$ khi $C$ từ $5$ lên $50$; bước 5 sửa $Q(\mathrm K,\rightarrow)$ hai lần, $Q(\mathrm F,\rightarrow)$ một lần và ghi $(\mathrm K,\rightarrow)\mapsto(+1,\mathrm Z)$; $\sqrt{99/1000}=0{,}3146$; $J$: $8\to2{,}88$; vòng kín $1{,}2x-0{,}6x=0{,}6x$; $\omega_1$ là tùy chọn phòng trái tới $\mathrm K$ (Ví dụ 11.24, 11.25); $V_2(\mathrm A)=0{,}6769\cdot0{,}9756=0{,}6604$; Bài tập 11.9–11.11.
  - Mục tiêu 4 sai ở chữ "chọn sai" (phát hiện trung bình thứ nhất ở trên).
  - Số hiệu mới trong ghi chú diễn giả đều tồn tại và đúng nội dung: Ví dụ 11.14, 11.15, 11.16 ($1{,}7558$ ở dòng 848), 11.18 (bản truy hồi ngược dòng 1056), 11.20, 11.23, 11.25, 11.26; Mệnh đề 11.36. Chỉ thiếu Ví dụ 11.13 (phát hiện nhẹ).
  - Ghi chú diễn giả gọi $0{,}8780$ là "hệ số chuyển của một bước đi đúng". Ghi chú bài giảng gọi $\rho$ là "thừa số chiết khấu kỳ vọng" và dùng nó làm $p(\mathrm K\mid\mathrm F,\omega_1)$. Cách gọi chấp nhận được.
- **(d) Dựng dần.**
  - L11-1-09:
    - lượt bấm 0: câu hỏi và năm mục tiêu $0,0,0,0,1$;
    - lượt bấm 1: $Q(\mathrm K,\rightarrow)=0{,}5$, $Q(\mathrm F,\rightarrow)$ vẫn $0$;
    - lượt bấm 2: lớp hình và $0{,}225$.

    Thứ tự này đúng với Q-learning rồi một cập nhật trên mẫu mô hình.
  - L11-2-16: hàng (d) $(\mathrm K,\rightarrow)$ $1/1/0{,}5$ hiện trước, rồi (f) $(\mathrm F,\rightarrow)$ $0{,}45/0{,}45/0{,}225$, rồi (f) $(\mathrm K,\rightarrow)$ $1/0{,}5/0{,}75$, rồi Diễn giải. Thứ tự này đúng (d) → (f) → (f) của Ví dụ 11.6.
  - L11-2-07 (hàng 1–2, 3–4, 5) và L11-2-12 ((d), (f), (f), rồi câu hỏi đảo thứ tự $0{,}10125$) cũng đúng thứ tự.
- **3. Thứ tự mới của mạch 1: không có câu toán nào dẫn tới điều chưa xuất hiện mà sai sự thật.**
  - L11-1-06 dùng $v_*$, đã có từ Bài 04.
  - Ghi chú diễn giả L11-1-06 nói "bảng $Q$… bắt đầu từ $0$ ở trang sau"; trang sau đúng là L11-1-09.
  - L11-1-07 dẫn "cùng năm bước thật" của L11-1-09, đứng trước nó. Khẳng định $\hat p(\mathrm K\mid\mathrm F,\rightarrow)=1$ đúng cho cả mô hình đếm lẫn mô hình lưu kết cục gần nhất.
  - Ghi chú diễn giả L11-1-02 nói "ô $\mathrm K$ cạnh đích $\mathrm Z$ của mê cung hai phòng"; mê cung đã được giới thiệu trước đó.
  - Thuật ngữ đi trước định nghĩa (mô hình đếm, Q-planning ở trang mục tiêu) là việc sư phạm, ngoài vai này.

## 4. Trang và hình đã kiểm

| trang | kết luận | số tính lại |
|---|---|---|
| L11-1-01 | không lỗi | như lượt trước |
| L11-1-06 (`me-cung-hai-phong-slide.svg`) | không lỗi | $v_*$ $0{,}9756/0{,}8566/0{,}7522/0{,}6604$; $0{,}72/0{,}82=0{,}8780$; $q_*(\mathrm F,\rightarrow)=0{,}856633$, $q_*(\mathrm F,\downarrow)=0{,}770970$ |
| L11-1-09 (`luot-mot-q-learning-slide.svg`, `luot-mot-ke-hoach-slide.svg`) | một nhẹ (ghi chú diễn giả) | mục tiêu $0,0,0,0,1$; $0+0{,}5[1+0{,}9\cdot0-0]=0{,}5$; $0+0{,}5[0+0{,}9\cdot0{,}5-0]=0{,}225$ |
| L11-1-07 | không lỗi | $0$ và $0{,}225$; $\hat p(\mathrm K\mid\mathrm F,\rightarrow)=1$, $p=0{,}8$; số của ghi chú diễn giả như lượt trước |
| L11-1-02 (`mo-hinh-hai-dang-slide.svg`) | không lỗi | $(\mathrm K,\rightarrow)$: $(\mathrm Z,+1)$ xác suất $0{,}8$, $(\mathrm K,0)$ xác suất $0{,}2$; giá trị kết thúc $0$ |
| L11-1-05 (`so-do-neo-slide.svg`) | một nhẹ (ghi chú diễn giả, không phải toán) | nhãn bốn nhánh khớp §1.2 và bảng §6.1; ngoặc "tại thời điểm quyết định" gom 3–4 đúng (Định nghĩa 11.21) |
| L11-1-03 | không lỗi | $0{,}1789$, $0{,}0566$; $0{,}54\to0{,}64$; $0{,}3146$ |
| L11-1-04 | một trung bình, một nhẹ | $m\ge\ln20/\Delta^2=69{,}81$; bốn hành động: $0{,}0616$ tại $m=70$, $0{,}0483$ tại $m=75$; các số còn lại như mục 3(c) |
| L11-2-00 (`so-do-neo-mach2-slide.svg`) | không lỗi | — |
| L11-2-03 (`bang-dem-hai-nhanh-slide.svg`) | không lỗi | $C(\mathrm A,\rightarrow)=2$, hai nhánh $1/2$; ba cặp $C=1$; $\hat r(\mathrm K,\rightarrow)=1/1=1$; $2+1+1+1=5$, 4 cặp |
| L11-2-06 (`q-planning-doc-ghi-slide.svg`) | không lỗi | $0{,}9\cdot0{,}5=0{,}45$; $0+0{,}5(0{,}45-0)=0{,}225$ |
| L11-2-13 (`hai-gioi-han-duong-di-slide.svg`) | không lỗi | dải mô hình: $0{,}729;0{,}81;0{,}9;1$ tại A, B, F, K, thưởng $0,0,0,+1$; $0{,}9^3=0{,}729$; nhãn "(kết cục gần nhất: đi đúng)" mang điều kiện; "Ý nghĩa" đúng (mục 3a) |
| L11-2-04 (`hai-loai-bat-dinh-A-slide.svg`) | một trung bình | như mục 3(b); $\mathbb E\hat p$ dưới quy tắc dừng tại lần đi đúng đầu tiên $=0{,}8926$; quy tắc dừng tại lần trượt đầu tiên $=0{,}5976$ |
| L11-2-07 | không lỗi | mô hình sau (e): $(0,\mathrm A)$, ghi đè $(0,\mathrm B)$, thêm $(\mathrm B,\downarrow)$, $(\mathrm F,\rightarrow)$, $(\mathrm K,\rightarrow)$; bước 5: $0{,}5$, $0{,}225$, $0{,}75$ |
| L11-2-16 | một nhẹ | $1/1/0{,}5$; $0{,}45/0{,}45/0{,}225$; $1/0{,}5/0{,}75$; đảo thứ tự $0{,}3375$; cập nhật lập kế hoạch đứng trước (d) cho mục tiêu $0$ |
| L11-2-08 | không lỗi | khớp Thuật toán 11.8 từng dòng; "Lưu ý:" khớp dòng 417 |
| L11-2-17 (`kien-truc-dyna-def-slide.svg`) | không lỗi | nhãn (d) sửa Q, (e) ghi Model, (f) đọc Model, sửa Q, $n$ lần, chọn cặp đã thử; Định nghĩa 11.9 |
| L11-2-11 | không lỗi | không đổi |
| L11-2-12 | không lỗi | $0$; $0{,}675/0{,}45/0{,}45$; $0{,}405/0{,}405/0{,}2025$; đảo thứ tự $0{,}5\cdot0{,}9\cdot0{,}225=0{,}10125$ |
| L11-2-18 | không lỗi | bốn giả thiết của Mệnh đề 11.4 đối chiếu đúng; $\alpha=0{,}5$ hằng: $\sum\alpha^2=\infty$ |
| L11-2-14 (`me-cung-doi-cua-hai-hinh-slide.svg`) | không lỗi | hai đường cùng dài $4$; sau đổi, $\mathrm B$–$\mathrm C$ là cạnh nối duy nhất giữa hai phòng |
| L11-2-09 (`chuoi-thuong-tham-do-slide.svg`) | một nhẹ (hình) | $0{,}01\sqrt{400}=0{,}2$; Dyna-Q $0{,}54/0/0{,}54$; Dyna-Q+ $0{,}74/0{,}2/0{,}64>0{,}6$ |
| L11-2-10 (`so-do-cap-nhat-hai-lan-thu-slide.svg`) | không lỗi | $0{,}9(0{,}5\cdot0{,}6+0{,}5\cdot0{,}4)=0{,}45$; $0{,}54$, $0{,}36$; Ví dụ 11.9 $0{,}36$ |
| L11-2-15 | không lỗi | giả thiết khớp dòng 521–533; $C$ và $k$ phân biệt đúng |
| L11-2-19 (`cap-nhat-mau-sai-so-slide.svg`) | không lỗi | $\sqrt{99/1000}=0{,}3146$; tọa độ SVG ($x=96+170\,k/b$, $y=300-260\cdot$sai số) khớp: $b=2$, $k=1..4$ cho $0{,}7071/0{,}5/0{,}4082/0{,}3536$; đầu đường $b=10$ là $0{,}9487$, $b=100$ là $0{,}9950$; chấm $(0{,}1;\,0{,}3146)$; bậc thang tại $k/b=1$ |

Kết luận: bảy phát hiện của lượt trước đã sửa đúng. Có thêm 2 phát hiện trung bình: mục tiêu 4 dùng $m=70$ cho "chọn sai" trong bốn hành động, và L11-2-04 áp Mệnh đề 11.5 cho số đếm của lượt thứ nhất. Có thêm 5 phát hiện nhẹ. Không có phát hiện chặn bàn giao hay nghiêm trọng. Mọi số còn lại trên trang, trong ghi chú diễn giả và trong 14 hình mới tính lại đúng.
