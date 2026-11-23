# Rà độ chính xác mạch 2, Bài 11, sau lượt viết lại P1 (2026-11-23)

- **Vai:** người rà độ chính xác toán học và thuật toán (chỉ đọc). Sub-agent `general-purpose`, Opus 5.5.
- **Đối tượng:** toàn bộ 19 trang mạch 2 theo `sua-m2-p1-2026-11-23.md` (mặt trang, ghi chú diễn giả, alt) và 24 SVG mạch 2 dùng.
  - Thứ tự trang: 2-00, 2-03, 2-06, 2-04, 2-17, 2-07, 2-20, 2-16, 2-08, 2-13, 2-11, 2-12, 2-18, 2-14, 2-09, 2-10, 2-21, 2-15, 2-19.
- **Nguồn:** `materials/lec-11/lecture-note.md` (3609690).
- **Cách kiểm:**
  - Đọc từng trang, nhãn SVG và ghi chú diễn giả.
  - Tính lại các số.
  - Sinh lại 100 giá trị của 2-21 bằng đúng hàm vẽ (`random.Random(11)`, `gauss(0,1)`, `randrange(100)` trong `hinh_m2_p1.py`).
  - Chụp 1600×900 chín trang (`Reveal.configure({transition:'none'})`, `Reveal.slide(h,v,99)`): không lỗi trang, không `.katex-error`. Ảnh nằm trong scratchpad của phiên.

## 1. Phát hiện

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa |
|---|---|---|---|---|
| nhẹ | L11-2-06, dòng "Ví dụ tính tay giữ kết cục gần nhất; ở $(\mathrm F,\rightarrow)$ hai cách lưu trùng nhau…" | Câu đứng ngay dưới Ví dụ 11.3 nên đọc như mô tả mô hình của Ví dụ 11.3. Thực ra Ví dụ 11.3 trong ghi chú dùng **mô hình đếm**. Mô hình giữ kết cục gần nhất là của Ví dụ 11.6 (Dyna-Q). Số $0{,}225$ không đổi, vì ở $(\mathrm F,\rightarrow)$ hai cách cho cùng thẻ, nhưng tên mô hình gán cho ví dụ bị sai. | Ví dụ 11.3, Dữ kiện (dòng 175): "mô hình đếm của Ví dụ 11.2 trả $(R,S')=(0,\mathrm K)$, lần thử duy nhất của cặp này". Ví dụ 11.6, Dữ kiện (dòng 344): "mô hình tất định lưu kết quả gần nhất". | "Ở $(\mathrm F,\rightarrow)$, mô hình đếm và mô hình giữ kết cục gần nhất trùng nhau vì mới có một lần quan sát; ví dụ Dyna-Q sau dùng cách giữ kết cục gần nhất." |
| nhẹ | L11-2-14, hộp đầu trang ("Nhắc lại: nhờ mô hình, Dyna-Q đưa giá trị từ $\mathrm K$ về $\mathrm F$ ngay lượt đầu.") | Câu nêu kết quả như điều Dyna-Q luôn làm được. Kết quả chỉ có khi bước chọn cặp ở bước 5 lấy $(\mathrm F,\rightarrow)$. 2-16 và ghi chú diễn giả 2-16 đã nêu đúng điều kiện này: chọn $(\mathrm A,\rightarrow)$ hai lần thì $Q(\mathrm F,\rightarrow)$ vẫn bằng $0$. | Ví dụ 11.6 (dòng ~355): "Giả sử bước chọn cặp lấy $(\mathrm F,\rightarrow)$ rồi $(\mathrm K,\rightarrow)$". Thuật toán 11.8, bước (f): chọn ngẫu nhiên. | "Nhắc lại: trong ví dụ, nhờ mô hình, Dyna-Q đưa giá trị từ $\mathrm K$ về $\mathrm F$ ngay lượt đầu." |
| nhẹ | L11-2-14, ghi chú diễn giả ("kết quả đó dựa vào mô hình đúng với môi trường") | Mô hình của lượt thứ nhất không đúng với môi trường. Mô hình giữ kết cục gần nhất bỏ qua trượt ($\hat p(\mathrm K\mid\mathrm F,\rightarrow)=1$ so với $p=0{,}8$), và chính các trang mạch 1 và 2-04 đã nhấn điểm này. Ý muốn nói là mô hình ghi đúng cấu trúc của môi trường lúc đó: cửa $\mathrm F$–$\mathrm K$ mở, kết cục đi đúng có thật. | Ví dụ 11.2, §2.3 đoạn mở (dòng 249); Tình huống 11.2 (mô hình tất định là mô hình sai). | "…kết quả đó dựa vào mô hình ghi đúng các chuyển đã thấy trước khi môi trường đổi, nên câu hỏi tiếp theo là môi trường đổi thì sao." |
| nhẹ | L11-2-09, hình `chuoi-thuong-tham-do-slide.svg`, mốc đầu "cửa B–C mở" | $\mathrm B$–$\mathrm C$ là **tường** được dỡ; "cửa" trong mê cung này là cạnh $\mathrm F$–$\mathrm K$. Gọi "cửa B–C" lệch với Ví dụ 11.1, Ví dụ 11.7 và với chính 2-14 ("tường $\mathrm B$–$\mathrm C$ mở"). Người đọc dễ nhầm với "cửa $\mathrm F$–$\mathrm K$ đóng" của cùng sự kiện. | Ví dụ 11.1 (dòng 84): "Tường ngăn B với C; cạnh F–K là cửa". Ví dụ 11.7 (dòng 426): "cửa F–K bị chặn, còn tường B–C được dỡ". | Đổi nhãn thành "tường B–C mở". |
| nhẹ | L11-2-21, ghi chú diễn giả (câu cuối: "sai số căn bình phương trung bình là căn của trung bình bình phương độ dài đó") | Hình giữ cố định một bộ 100 giá trị nhánh, nên lặp lại "lần làm thử" chỉ lấy trung bình theo các lượt rút. Kết quả là RMSE có điều kiện $\sigma/\sqrt k$ của bộ giá trị này. Với bộ seed 11, $\sigma^2=0{,}8831$ nên RMSE có điều kiện là $0{,}2972$. Đại lượng (2.5) ở trang sau còn lấy trung bình theo giá trị nhánh, với $\mathbb E\sigma^2=0{,}99$, nên bằng $0{,}3146$. Câu đầu ghi chú, "đúng giả thiết của mệnh đề", cũng hơi rộng: hình là một lần thể hiện của giả thiết (b) và minh họa phần (a). Mặt trang không có số nên không sai. | Mệnh đề 11.15: (a) "với mọi giá trị cố định của các $y_{s'}$… $\sigma^2/k$"; Bước 3: "$\mathbb E[(Q_k-\bar y)^2\mid y]=\sigma^2/k$. Lấy kỳ vọng theo $y$…". Tính lại: trung bình 100 nhánh $0{,}2552$, trung bình 10 lượt rút $0{,}4848$, độ dài đoạn $0{,}2296$, $\sigma^2=0{,}8831$, $\sqrt{0{,}8831/10}=0{,}2972$. | "…Lặp lại với cùng 100 giá trị thì căn trung bình bình phương độ dài đoạn là $\sigma/\sqrt k$ của bộ giá trị này; (2.5) lấy thêm trung bình theo giá trị nhánh." |

Tổng: 0 chặn bàn giao, 0 nghiêm trọng, 0 trung bình, 5 nhẹ.

## 2. Các điểm điều phối viên hỏi riêng

- **2-03.**
  - Hộp câu hỏi của mạch đúng ý §1.2, đoạn cuối, và §2.2, đoạn mở.
  - Bảng đếm dạng thẻ đúng. $(\mathrm A,\rightarrow)$ có $C=2$, gồm thẻ ① "thưởng 0, ở lại A" và thẻ ② "thưởng 0, sang B", mỗi thẻ $1/2$. Ba cặp còn lại mỗi cặp một thẻ, tần suất $1$; $(\mathrm K,\rightarrow)$ có "thưởng +1, vào Z".
  - Chú thích "p̂ đếm thẻ theo ô tới, r̂ lấy trung bình R" khớp (2.1).
  - Dải F, K, Z: "bước 4: K còn 0", "bước 5: K lên 0,5", đúng.
  - Bỏ nhãn "Ví dụ 11.2" và tên thứ hai "maximum-likelihood model" không làm sai nghĩa. NT2 đòi số và khẳng định đúng, truy được về ghi chú. Hình vẫn là dữ kiện của Ví dụ 11.2, ghi chú diễn giả có nguồn, và một tên tiếng Anh ở lần đầu là đủ theo VP2. Không tính là phát hiện độ chính xác.
- **2-06.** "Trả nguyên một thẻ $(R,S')=(0,\mathrm K)$" đúng: rút một lần thử cũ giữ $R$ và $S'$ cùng nhau (dòng 193). Ba lớp hình đúng: K = 0,5; "mô hình trả thưởng 0, đến K", "đọc"; "ghi", "0 → 0,225". Thuật toán 11.3 đúng câu chữ ghi chú. Câu "hai cách lưu trùng ở $(\mathrm F,\rightarrow)$" đúng; chỉ có tên mô hình gán cho ví dụ cần sửa (phát hiện 1).
- **2-04.**
  - Khung trái "lượt đã quan sát" đúng: $\hat p(\mathrm B\mid\mathrm A,\rightarrow)=1/2$, "C = 2 vì lần đầu trượt, không chọn trước".
  - Khung phải đúng: ấn định $C=2$, $p=0{,}8$; ba cột $0{,}04;0{,}32;0{,}64$; độ lệch chuẩn $\sqrt{0{,}72-0{,}64}=0{,}2828$.
  - Nhãn trục "độ lệch chuẩn = √phương sai" đúng và giải thích được vì sao Định nghĩa 11.6 dùng $p(1-p)$ mà hình vẽ $0{,}4$.
  - Ghi chú diễn giả có $\mathbb E\hat p=0{,}8926$ (quy tắc dừng của lượt) và $0{,}5976$ (dừng ở lần trượt đầu); cả hai đúng.
- **2-13** (nay đứng sau Dyna-Q).
  - Dải mô hình "luôn đi tới ô kế": $1;\,0{,}9;\,0{,}81;\,0{,}729$, "× 0,9 mỗi bước", đúng. Trên mô hình tất định không trượt, mỗi bước nhân $\gamma=0{,}9$.
  - Dải mê cung thật: $0{,}9756;\,0{,}8566;\,0{,}7522;\,0{,}6604$, "× 0,72/0,82 ≈ 0,8780", đúng.
  - $v_*(\mathrm A)=0{,}9756\cdot(0{,}72/0{,}82)^3$: dùng $0{,}975610$ thì được $0{,}66044$; dùng hệ số làm tròn thì $0{,}9756\cdot0{,}8780^3=0{,}6603$, như ghi chú diễn giả nói.
  - "Luôn đi tới ô kế" là một mô hình đủ mọi cặp, nên $\hat q_*$ xác định. Ghi chú diễn giả vẫn nêu ba điều kiện của Tình huống 11.2.
  - Câu "Bài tập ngay sau kiểm các giả thiết này trên Dyna-Q" đúng với thứ tự mới.
- **2-12.**
  - Bảng hai thứ tự đúng. F trước: đọc $0{,}45$, $Q(\mathrm B,\downarrow)=0{,}5\cdot0{,}9\cdot0{,}45=0{,}2025$. B trước: đọc $0{,}225$, $0{,}10125$.
  - Hàng câu hỏi đặt trước hàng $(\mathrm B,\downarrow)$; hàng (d) ghi "giá trị cũ ở B" đúng.
- **2-18.**
  - Kết luận "một cập nhật chỉ cần mô hình ở cặp đang chọn; bảo đảm hội tụ cần cả bốn điều kiện cho cả quá trình, ví dụ không thỏa" đúng. Thuật toán 11.3, bước 2–3, chỉ gọi mô hình tại cặp được chọn. Mệnh đề 11.4 cần bốn giả thiết, và ví dụ chắc chắn không thỏa "mô hình cố định" và Robbins–Monro.
  - Các ô bảng đúng.
- **2-14, 2-10, hộp "Nhắc lại / Câu hỏi".**
  - 2-10 đúng: cập nhật lập kế hoạch lấy mục tiêu từ mô hình; cặp nhiều thẻ thì mở mọi thẻ (cập nhật kỳ vọng) hay rút một (cập nhật mẫu), khớp §2.6.
  - 2-14: vế "Câu hỏi" đúng; vế "Nhắc lại" thiếu điều kiện về lần chọn cặp (phát hiện 2).
- **2-09.**
  - Dòng thời gian đúng về số: $0{,}54$ trước, $0{,}6$ dẫn đầu, $0{,}64$ sau; thưởng $0{,}01\sqrt{400}=0{,}2$; mục tiêu $0{,}74$. Hai nhánh $0{,}8$/$0{,}2$ và "ℓ ← 0" khớp Định nghĩa 11.11.
  - Phạm vi "cặp đã lưu" đúng với ví dụ, vì $(\mathrm B,\rightarrow)$ đã có trong mô hình. Định nghĩa 11.11 còn cho bước (f) chọn cả hành động chưa thử với mô hình khởi tạo; ghi chú diễn giả nêu điều này. Không mâu thuẫn.
  - Chỉ có nhãn "cửa B–C" lệch (phát hiện 4).
- **2-21.**
  - Cách trình bày đúng với giả thiết của Mệnh đề 11.15(b) khi hiểu là một lần thể hiện. 100 giá trị được rút độc lập từ chuẩn tắc, tức cùng kỳ vọng và phương sai $1$. Các giá trị giữ cố định trong lúc rút, tức "không đổi trong $k$ cập nhật". Lượt rút có hoàn lại, tức "$k$ mẫu độc lập theo $\hat p$ đồng khả năng".
  - Vạch cam là $Q_{10}$ với $\alpha_j=1/j$; vạch xanh là $\bar y$.
  - Mặt trang không ghi số, nên không có khẳng định sai. Chỉ câu cuối ghi chú diễn giả cần nói rõ lấy trung bình theo gì (phát hiện 5).
  - Bộ seed 11: mười lượt rút không trùng thẻ (chỉ số 16, 17, 23, 47, 49, 58, 61, 73, 75, 79). Câu "một thẻ có thể bị rút hai lần" vẫn đúng như khả năng chung.
- **2-19.**
  - Nhãn đúng: "k/b: số lần rút từ mô hình chia b"; "kỳ vọng: chưa đủ nhánh, sai số giả định 1" (Phạm vi của Mệnh đề 11.15); "100/100 lượt: tính đúng mục tiêu kỳ vọng"; "b = 2, k = 2: RMSE 0,5"; "10/100 lượt đánh giá; sai số 0,3146".
  - Dòng "Lưu ý" phân biệt $k$ với $C$ đúng.

## 3. Các trang khác đã kiểm, không lỗi

| trang | số và khẳng định đã kiểm |
|---|---|
| L11-2-00 (`so-do-neo-mach2-slide.svg`) | không đổi |
| L11-2-17 (`kien-truc-dyna-def-slide.svg`) | Ba vùng "mê cung thật / bảng Q, chính sách / mô hình". (d) sửa Q, (e) ghi mô hình, (f) đọc mô hình, sửa Q; $n$ lần. Ví dụ đổi sang bước thật $(\mathrm K,\rightarrow,+1,\mathrm Z)$: sau (d) và (e), tác tử đã ở $\mathrm Z$ khi (f) cập nhật $Q(\mathrm F,\rightarrow)$. Khớp Ví dụ 11.6 và Thuật toán 11.8, vì (f) chạy trong cùng vòng, trước khi lượt mới bắt đầu. |
| L11-2-07 (`hai-cach-luu-slide.svg`) | Bảng năm bước. Bước 5: $0{,}5$; $0{,}225$; $0{,}75$. Hai thẻ ①② đúng. Ghi chú diễn giả không còn nhắc Mệnh đề 11.4 trước khi giới thiệu nó. |
| L11-2-20 (5 lớp `dyna-ba-vung-*`) | Lớp đầu: mô hình có ba cặp $(\mathrm A,\rightarrow)\mapsto(0,\mathrm B)$, $(\mathrm B,\downarrow)\mapsto(0,\mathrm F)$, $(\mathrm F,\rightarrow)\mapsto(0,\mathrm K)$; $Q=0$; tác tử ở $\mathrm K$. (d): vào $\mathrm Z$, $Q(\mathrm K,\rightarrow)=0{,}5$. (e): ghi $(\mathrm K,\rightarrow)\mapsto(+1,\mathrm Z)$. (f) lần 1: đọc $0{,}5$ ở K, $0{,}225$. (f) lần 2: $0{,}75$. Thứ tự (d), (e), (f), (f) đúng Thuật toán 11.8. Nhãn "thứ tự chọn trong lần chạy đã chọn; tác tử vẫn ở Z" đúng. |
| L11-2-16 | Không đổi; $1/1/0{,}5$; $0{,}45/0{,}45/0{,}225$; $1/0{,}5/0{,}75$. |
| L11-2-08 | Không đổi; khớp Thuật toán 11.8 và dòng 193, 417. |
| L11-2-11 | Không đổi; dữ kiện trùng Bài tập 11.4. |
| L11-2-10 (`so-do-cap-nhat-hai-lan-thu-slide.svg`) | "mở cả hai thẻ: 2 lần đánh giá", mục tiêu $0{,}45$; "rút một thẻ: 1 lần đánh giá", $0{,}54$ hoặc $0{,}36$; $(0{,}54+0{,}36)/2=0{,}45$. Các giá trị max Q ghi là giả sử. |
| L11-2-15 | Không đổi; giả thiết và ý tưởng chứng minh như lượt trước. |

Kết luận: mạch 2 sau lượt P1 đúng về toán ở mọi số, công thức và thứ tự cập nhật. Có 5 phát hiện nhẹ:

- gán sai mô hình cho Ví dụ 11.3 (2-06);
- hai câu thiếu điều kiện hoặc diễn đạt quá ở 2-14 (một trên mặt trang, một trong ghi chú diễn giả);
- nhãn "cửa B–C" ở 2-09;
- câu về RMSE trong ghi chú diễn giả 2-21.
