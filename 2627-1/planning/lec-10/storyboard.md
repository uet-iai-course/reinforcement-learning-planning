# Storyboard Bài 10: TRPO, PPO và DPO (dựng lại theo TB1–TB23)

Bước 3–4 của quy trình dựng deck (`rl-plan/NGUYEN-TAC-HOC-PHAN.md`, mục 3a.E), viết ngày 2026-11-20, thay toàn bộ storyboard cũ (101 trang, tám mạch; bản cũ còn trong git và trong bản sao lưu của điều phối viên). Đầu vào chuẩn:

- câu chuyện đã duyệt `planning/lec-10/cau-chuyen-deck-2026-11-20.md` (tác giả "Duyệt", 2026-11-20; mười quyết định cuối tệp);
- ghi chú và bài tập sau khi sửa ví dụ (commit `cb593b3`): `materials/lec-10/lecture-note.md`, `materials/lec-10/exercises.md`;
- quy tắc TB1–TB23 (mục 3a của `NGUYEN-TAC-HOC-PHAN.md`), phần NT1–NT29 không bị thay (`NGUYEN-TAC-TRANG-CHIEU.md`), VP25;
- mẫu trình bày `nhat-ky/su-pham-trinh-bay-2026-11-20/phan-tich-slide-mau.md` (mục 3.1–3.8) và hai báo cáo phân tích deck cũ.

Mọi con số dưới đây có trong ghi chú; các số dùng để vẽ hình mà ghi chú không ghi (điểm trên đường cong) được tính lại trong `/tmp/claude-1000/-data-tqlong-lectures/678a7f48-9d80-46cf-a421-67398857f913/scratchpad/deck10/storyboard/so.py` và chỉ dùng để vẽ, không ghi lên hình.

**Quy ước của tệp.**

- Mã trang theo lược đồ của mục 5 `NGUYEN-TAC-HOC-PHAN.md`: mạch k có tiền tố `L10-k-`; bìa `L10-1-01`; trang tiêu đề mạch `L10-k-00`, `id="mach-k"`; các trang khác `L10-k-mm` từ `01`. Deck dựng lại, nên không giữ mã cũ (bảng đối chiếu ở mục 7).
- Mỗi trang có các mục: **Câu** (câu của câu chuyện mà trang phục vụ, mục 1), **Biết thêm** (TB4: "sau trang này sinh viên biết thêm …"), **1 phút** (TB23: sinh viên lần đầu học thấy gì trong một phút), **Mới** (phần tử mới duy nhất, TB11), **Ý chính** và chỗ đặt (TB8), **Mặt trang** (đúng chữ dự kiến; số âm tiết ước lượng theo khoảng trắng, không tính tiêu đề, KaTeX, ô số của bảng, nhãn hình), **Hình** (TB10) hoặc lý do không hình, **Dựng dần** (TB17), **Ghi chú diễn giả** (lời giảng dự kiến, TB9), **Nguồn** (khối của ghi chú), **Bố cục** (phác ASCII cho trang có hình, bảng tính hay dựng dần).
- Chữ trong ngoặc kép ở mục "Mặt trang" là chữ lên trang, viết theo VP25 và `no-ai-slop` chế độ Edit; người dựng deck chỉ được rút, không được thêm ý.
- Màu nhấn mang một nghĩa trong cả bài (TB18), luôn kèm nét hoặc nhãn (NT25): **đỏ** = hỏng, sai chiều; **cam, nét đứt** = lệch (độ chệch, dự đoán của hàm thay thế); **xanh, nét liền** = đúng, giá trị thật; **tím** = đại lượng mới, đang bàn trên trang (kể cả khối đang học trên sơ đồ neo, chính sách mới, phần khác nhau giữa hai công thức, $F^{-1}g$, $\pi^*$, $\beta\log\mathcal Z$). Sửa theo cổng 2026-11-20.
- Số trang theo P6 với TB17: chuỗi trang dựng dần liên tiếp cùng bố cục tính một trang.

---

## 1. Câu chuyện của bài (đã duyệt, chép nguyên)

1. Trên hành lang ngắn, ba lượt REINFORCE cho ba hướng cập nhật khác nhau (tọa độ thứ nhất $-5{,}5$; $-1$; $1$, trong khi gradient đúng là $2$), và một bước theo đúng gradient nhưng quá dài kéo $J$ từ $-12$ xuống khoảng $-21$.
2. So lợi tức với giá trị của trạng thái thì hướng trung bình giữ nguyên mà dao động giảm; nếu một hàm giá trị (critic) đánh giá đúng, mỗi bước cho ngay hệ số đúng: trên chuỗi hai trạng thái, cả ba loại lượt cùng cho $0{,}2$.
3. Critic học dở thì đánh giá một bước bị lệch, còn lợi tức cả lượt không lệch nhưng dao động; GAE trộn hai cách bằng một tham số $\lambda$.
4. Muốn đi bước lớn bằng dữ liệu cũ, ta đoán $J$ của chính sách mới bằng hàm thay thế; trên chuỗi, hàm thay thế báo tăng $0{,}175$ trong khi $J$ thật giảm $0{,}05$, nên chỉ được tin nó khi chính sách mới ở gần chính sách cũ: đó là miền tin cậy, mà TRPO giải bằng gradient tự nhiên.
5. PPO giữ chính sách mới ở gần bằng cách cắt tỉ số xác suất, nên chỉ cần Adam: trên $s_B$, mục tiêu cắt nằm ngang từ $p=0{,}8$.

   *Sửa theo cổng (2026-11-20, lệch so với câu chuyện đã duyệt):* câu 5 thành "Lợi thế ước lượng từ ít lượt có thể sai dấu, và tối đa hàm thay thế mẫu thì đi tới tận biên: trên chuỗi, một bộ đệm hai lượt đẩy $p_A$ về $0$ và $J$ giảm $0{,}4$. PPO cắt tỉ số xác suất nên chỉ cần Adam: với cùng bộ đệm, vòng dừng ở $(0{,}4;\,0{,}73)$ và $J$ chỉ giảm $0{,}008$; trên $s_B$, mục tiêu cắt nằm ngang từ $p=0{,}8$."
6. Khi chỉ có người so sánh hai câu trả lời, ta khớp phần thưởng từ các so sánh và phạt việc rời mô hình ban đầu; RLHF (dùng PPO) và DPO (một hàm mất mát phân loại) cùng đi tới một chính sách, trên ví dụ là $(\tfrac45;\tfrac15)$.

Trong các mục trang dưới đây, "Câu k" chỉ câu thứ k ở trên; "Câu M" chỉ phần mở đầu của câu chuyện (câu hỏi trung tâm, mục tiêu, nội dung), "Câu T" chỉ phần tổng kết.

---

## 2. Bảng mạch

| Mạch | Câu hỏi của mạch | Câu chuyện của mạch (3–5 câu) | Ví dụ chạy | Đầu vào | Đầu ra | Trang đếm / thật | Phút |
|---|---|---|---|---|---|---|---|
| 1. Mở đầu | (trung tâm) 1. Làm sao ước lượng gradient ít dao động hơn? 2. Làm sao đi bước lớn mà $J$ không giảm? | Trên hành lang, mọi ô cùng $p=\tfrac12$, gradient đúng $(2;-2)$. Ba lượt cho tọa độ thứ nhất $-1$; $1$; $-5{,}5$: hai lượt đẩy $p$ xuống. Bước đúng hướng $\alpha=0{,}1$ đưa $J$ từ $-12$ lên $-11{,}7$; bước $\alpha=0{,}5$ vượt đỉnh $p^*\approx0{,}59$ và kéo $J$ xuống $-21{,}3$. Còn thiếu: ước lượng ít dao động, và cách chọn bước dài không vượt đỉnh. | hành lang ngắn (Ví dụ 10.2, đoạn sau Ví dụ 10.2) | REINFORCE, $\widehat g$, hàm điểm softmax (Bài 09) | hai câu hỏi trung tâm, sơ đồ neo năm khối | 8 / 8 | 12 |
| 2. So lợi tức với giá trị của trạng thái | Làm sao để mỗi lượt chỉ tăng xác suất của hành động tốt hơn mức thường có ở trạng thái, mà trung bình vẫn bằng gradient? | Lượt $s_A\xrightarrow2$ (xác suất $\tfrac12$) nhận thưởng $1$ và đẩy $p_A$ xuống, dù $1<v(s_A)=1{,}4$. Trừ $v(S_t)$ khỏi lợi tức: trung bình giữ $0{,}2$ vì $\sum_a\pi\psi=0$, phương sai $0{,}69\to0{,}20$. Hệ số trung bình là lợi thế $q-v$; critic cho nó ngay sau một bước bằng $\delta_t$. Với critic đúng, ba loại lượt cùng cho $0{,}2$, phương sai $0$. Còn thiếu: critic phải học, và học dở thì sao. | chuỗi hai trạng thái, chính sách cũ $(\tfrac12;\tfrac23)$ (Ví dụ 10.6) | $\widehat g$ của REINFORCE, hai câu hỏi trung tâm | cột $G_t\to G_t-v\to\delta_t$; khối ③ "critic" và ④ $\delta_t$ của sơ đồ neo | 7 / 9 | 19 |
| 3. Trộn đánh giá một bước và cả lượt | Có cách nào ít lệch hơn đánh giá một bước mà ít dao động hơn lợi tức cả lượt không? | Critic $(1{,}4;1)$ đánh giá thấp $s_B$. Hai lượt từ $(s_A,1)$: một bước cho $-0{,}5$ ở cả hai (đều, sai dấu so với $0{,}4$); cả lượt cho $1{,}3$ hoặc $-1{,}4$ (trung bình đúng, dao động). GAE cộng các $\delta$ với trọng số $(\gamma\lambda)^k$, tính lùi được. $\lambda=0{,}5$: $0{,}4$ hoặc $-0{,}95$, trung bình $-0{,}05$; độ lệch $-0{,}9(1-\lambda)$, khoảng cách $2{,}7\lambda$. Còn thiếu: mỗi lượt vẫn chỉ cho một bước cập nhật nhỏ. | chuỗi, critic $(1{,}4;1)$, hai lượt (Ví dụ 10.8, 10.9, đoạn sau Ví dụ 10.10) | $\delta_t$, critic, $G_t-\hat v$ | $\widehat A_t$, công thức tính lùi; ④ thành $\widehat A_t$ | 6 / 6 | 12 |
| 4. Đánh giá chính sách mới bằng dữ liệu cũ | Đoán $J$ của chính sách mới từ dữ liệu của chính sách cũ thế nào, và tin được đến đâu? | Chính sách $(1;0{,}5)$ tới $s_B$ ở mọi lượt, chính sách cũ chỉ một nửa. Hiệu $J$ bằng lợi thế cũ cộng theo nơi chính sách mới tới: $0{,}4-0{,}45=-0{,}05$. Hàm thay thế dùng nơi chính sách cũ tới: $0{,}4-0{,}225=+0{,}175$, đoán sai chiều; sai số $2{,}7\Delta p_A\Delta p_B$ nhỏ khi bước ngắn. Vì vậy tối đa hàm thay thế trong miền KL nhỏ; TRPO đi theo $F^{-1}g=(8;30)$, dồn bước về $\theta_B$. Còn thiếu: mỗi bước TRPO cần bộ máy bậc hai, và như cài đặt nó không còn bảo đảm $J$ tăng. | chuỗi, bước $(1;0{,}5)$ và $(0{,}7;0{,}6)$ (Ví dụ 10.11, 10.12; đoạn cuối Mục 5.2) | GAE, lợi thế cũ $(0{,}4;-0{,}4)$, $(1;-2)$; hành lang $J(p)$ | hàm thay thế, miền tin cậy, TRPO; ⑤ thành "tối đa hàm thay thế trong miền tin cậy" | 9 / 10 | 22 |
| 5. Giữ chính sách mới gần chính sách cũ | Sửa hàm mục tiêu thế nào để Adam không đẩy chính sách đi quá xa trên một bộ đệm nhỏ? | (sửa theo cổng) Với critic $(1{,}4;1)$, $\lambda=1$, bộ đệm hai lượt $s_A\xrightarrow1s_B\xrightarrow2$, $s_A\xrightarrow2$ chấm hành động 1 ở $s_A$ là $-1{,}4$ (đúng: $+0{,}4$); hàm thay thế mẫu đẩy $p_A$ về $0$, $p_B$ về $1$, và $J$ giảm $0{,}4$. Cắt tỉ số $\rho$ vào $[0{,}8;1{,}2]$ rồi lấy giá trị nhỏ hơn: bỏ phần thưởng của việc đi xa, giữ phần phạt. Trên $s_B$ với ba mẫu đúng tần suất, mục tiêu cắt nằm ngang từ $p=0{,}8$. Với bộ đệm xui, vòng dừng ở $(0{,}4;\,0{,}73)$ và $J$ chỉ giảm $0{,}008$. Còn thiếu: cắt không chặn KL ($0{,}049\to0{,}10$ khi tham số trôi từ $0{,}8$ tới $0{,}85$), nên PPO đo approxKL; và cả TRPO lẫn PPO cần một hàm phần thưởng. | chuỗi với bộ đệm hai lượt (đề xuất sửa ghi chú G2, G3); $s_B$ với bộ đệm $1,1,2$ (Ví dụ 10.17, 10.18, 10.20, 10.21) | hàm thay thế, lợi thế GAE với critic $(1{,}4;1)$, tỉ số lấy mẫu quan trọng (Bài 06) | mục tiêu cắt, vòng PPO; ⑤ thành "tối đa mục tiêu cắt, nhiều lượt qua dữ liệu" | 8 / 9 | 16 |
| 6. Học từ so sánh của người | Chính sách mới nên chọn mỗi câu trả lời với xác suất bao nhiêu, và có cần một vòng học tăng cường để tìm nó không? | Mô hình hiện tại trả lời $y_1$, $y_2$ với $(\tfrac23;\tfrac13)$; người chọn $y_1$ bốn lần, $y_2$ hai lần. Bradley–Terry cho $\hat r=(\log2;0)$; tham lam bỏ hẳn $y_2$, nên trừ $\beta$ lần KL tới mô hình ban đầu: nghiệm $(\tfrac45;\tfrac15)$ với $\beta=1$. RLHF tới đó bằng PPO (tại nghiệm hai câu cùng phần thưởng $0{,}51$, PPO đứng yên); DPO viết phần thưởng theo chính sách và học thẳng bằng hồi quy logistic: $0{,}67\to0{,}74\to\dots\to0{,}8$. Còn thiếu: người luôn chọn một phía thì cả hai con đường đẩy $\pi(y_2)$ về $0$. | lời nhắc có hai câu trả lời, $\pi_{\mathrm{ref}}=(\tfrac23;\tfrac13)$, sáu so sánh (Ví dụ 10.23–10.28) | PPO, phạt KL, hồi quy logistic (học máy) | $\pi^*\propto\pi_{\mathrm{ref}}e^{\hat r/\beta}$, hai con đường; ① thành "phần thưởng học từ so sánh, trừ phạt KL", mũi tên DPO | 10 / 10 | 22 |
| 7. Tổng kết | (trả lời câu hỏi trung tâm) | Sơ đồ neo lần cuối, mỗi khối một công thức và một con số. Ba câu trả lời. Một bài tổng hợp trên chuỗi: một vòng PPO-Clip dừng ở $(0{,}6;0{,}8)$, hàm thay thế đoán $0{,}26$, thật $0{,}296$. Câu hỏi tự kiểm tra về hành vi trên ví dụ, bài tập về nhà, tài liệu. | chuỗi hai trạng thái (Bài tập 10.23, §8.4) | đầu ra của mạch 2–6 | ý mang về | 8 / 8 | 9 |
| **Tổng** | | | | | | **56 / 60** | **112 + 8 phút câu hỏi nhanh = 120** |

Tám phút còn lại chia cho sáu câu hỏi nhanh và hai lần dừng hỏi lớp ở trạm dừng (khoảng một phút mỗi lần). 56 trang đếm, đúng "khoảng 56 trang đếm" của quyết định 10 (vượt mức mặc định 45–55 của P6 một trang); 60 trang thật, bằng trần 60. Lý do: ba chủ đề và năm mạch nội dung, cộng trang trạm dừng mới `L10-5-05` của cổng. Ba chuỗi trang dựng dần cùng bố cục tính một trang mỗi chuỗi: `L10-2-01`–`L10-2-03`, `L10-4-02`–`L10-4-03`, `L10-5-02`–`L10-5-03`.

Khối "Giả thiết:/Kết luận:" (TB7): ba khối, `L10-2-04` (Mệnh đề 10.2), `L10-4-06` (Định lý 10.26), `L10-6-04` (Định lý 10.57). Trang ý tưởng chứng minh duy nhất: `L10-2-05` ($\sum_a\pi\psi=0$, quyết định 7). Câu hỏi nhanh (TB22), mỗi mạch nội dung một câu: `L10-1-03`, `L10-2-03`, `L10-3-04`, `L10-4-05`, `L10-5-03`, `L10-6-09`. Trạm dừng (TB5): `L10-1-06`, `L10-2-08`, `L10-3-05`, `L10-4-05`, `L10-4-09`, `L10-5-05`, `L10-5-08`, `L10-6-08`. Trang kết quả có phần tử mới (không tính là trạm dừng): `L10-2-06`, `L10-6-04`.

---

## 3. Sơ đồ neo (TB2) và trạng thái ở từng mạch

**Hình "vòng cập nhật chính sách"**, năm khối, nhãn bằng lời; tệp gốc `img/lec-10/so-do-neo-vong-cap-nhat.svg`, mỗi trạng thái một tệp `so-do-neo-m1.svg` … `so-do-neo-m7.svg` (mục 6). Bản đầy đủ ở `L10-1-08` ("Nội dung"); bản thu nhỏ trên mỗi trang tiêu đề mạch (khối của mạch tô tím, viền đậm; khối khác xám mờ); bản cuối ở `L10-7-01`. Khối mạch đang học được tô trên trang tiêu đề mạch với nhãn cũ và một dấu "?"; nhãn mới chỉ hiện ở trạm dừng cuối mạch, nơi kết quả đã có.

```
 ┌───────────────┐       ┌──────────────────────────────┐
 │ ① Phần thưởng  │ ────▶ │ ② Thu lượt bằng chính sách cũ │ ◀───────────┐
 └───────────────┘       └──────────────────────────────┘             │
                                     │                                  │ chính sách mới
                                     ▼                                  │ thành chính sách cũ
 ┌ ─ ─ ─ ─ ─ ─ ─ ┐       ┌──────────────────────────────┐             │
   ③ (chưa có)    ─ ─ ▶ │ ④ Hệ số của mỗi bước: G_t     │             │
 └ ─ ─ ─ ─ ─ ─ ─ ┘       └──────────────────────────────┘             │
                                     │                                  │
                                     ▼                                  │
                         ┌──────────────────────────────┐             │
                         │ ⑤ Cập nhật: một bước gradient │ ────────────┘
                         └──────────────────────────────┘
```

| Mạch | Trang tiêu đề mạch: khối tô | Thay đổi, hiện ở trang | Nhãn sau thay đổi |
|---|---|---|---|
| 1 | (bản đầy đủ ở `L10-1-08`) | hai dấu "?" đỏ, ở ④ "dao động" và ở ⑤ "bước dài làm $J$ giảm" (`L10-1-08`) | như hình trên |
| 2 | ③ và ④ | `L10-2-08`: ③ thành khối liền; ④ ghi dãy $G_t\to G_t-v(S_t)\to\delta_t$ | ③ "critic $\hat v$"; ④ "hệ số: $\delta_t$" |
| 3 | ④ | `L10-3-05`: ④ thêm $\widehat A_t$ "trộn bằng $\lambda$" | ④ "hệ số: $\widehat A_t$" |
| 4 | ⑤ | `L10-4-09`: ⑤ mở thành vòng TRPO; thêm mũi tên ② → ⑤ "dùng lại dữ liệu cũ" | ⑤ "tối đa hàm thay thế trong miền tin cậy (TRPO)" |
| 5 | ⑤ | `L10-5-07`: ⑤ mở thành vòng PPO | ⑤ "tối đa mục tiêu cắt, nhiều lượt qua dữ liệu (PPO)" |
| 6 | ① | `L10-6-05`: ① đổi nhãn; `L10-6-08`: thêm mũi tên nét đứt "DPO" từ "so sánh của người" thẳng tới ⑤, bỏ qua ②–④ | ① "phần thưởng học từ so sánh, trừ phạt KL (RLHF)" |
| 7 | cả hình | `L10-7-01`: mỗi khối một công thức và một con số của ví dụ chạy; ④ và ⑤ có dãy thẳng hàng các bước đổi, phần đổi tô tím | mục `L10-7-01` |

Trang "Nội dung" ghi tên mạch 2–7 cạnh khối mà mạch đổi, để sơ đồ neo cũng là bảng nội dung (P5: trang khung chung là sơ đồ neo, TB2).

---

## 4. Ví dụ chạy và thông điệp (TB14–TB16)

| Mạch | Ví dụ | Thông điệp (một câu) | Số trên trang | Bẫy cần tránh (từ câu chuyện, mục 4.1) |
|---|---|---|---|---|
| 1 | hành lang, ba lượt, hai bước | Một lượt cho một hướng ngẫu nhiên; bước đúng hướng mà dài vẫn làm $J$ giảm. | $-1$; $1$; $-5{,}5$ quanh $2$; $-12\to-11{,}7$; $-12\to-21{,}3$ | không dùng hành lang cho đường cơ sở (trên hành lang, trừ $v_\pi$ làm lượt (b) đổi chiều) |
| 2 | chuỗi, ba loại lượt | So với giá trị của trạng thái, hệ số ít dao động mà trung bình giữ nguyên; critic đúng cho hệ số đúng ngay. | cột $1{,}35;0;-0{,}5$ → $0{,}65;-0{,}7;0{,}2$ → $0{,}2;0{,}2;0{,}2$; trung bình $0{,}2$; phương sai $0{,}69$; $0{,}20$; $0$; xác suất sai dấu $\tfrac12$; $\tfrac16$; $0$ | ghi phương sai cả cột và xác suất sai dấu, vì lượt thứ hai xấu đi ($0\to-0{,}7$); chỉ tọa độ $\theta_A$ |
| 3 | chuỗi, critic $(1{,}4;1)$, hai lượt | Một bước: đều nhưng lệch; cả lượt: không lệch nhưng dao động; $\lambda$ ở giữa. | $-0{,}5;-0{,}5$; $1{,}3;-1{,}4$; $0{,}4;-0{,}95$; trung bình $-0{,}5$; $-0{,}05$; $0{,}4$ | hàng "trung bình" bắt buộc, vì lượt (i) với $\lambda=0{,}5$ cho đúng $0{,}4$ do trùng hợp |
| 4 | chuỗi, bước $(1;0{,}5)$, $(0{,}7;0{,}6)$ | Hàm thay thế đoán đúng khi bước ngắn, có thể sai chiều khi bước dài đổi nơi chính sách tới. | $+0{,}175$ so với $-0{,}05$; $+0{,}07$ so với $+0{,}034$; $(8;30)$ | ghi "tại $p'_A=1$, KL ở $s_A$ vô hạn" ở ghi chú diễn giả của `L10-4-07` |
| 5 | chuỗi, bộ đệm hai lượt; $s_B$ với bộ đệm $1,1,2$ | Lợi thế ước lượng từ ít lượt sai dấu đẩy chính sách đi xa; cắt giới hạn mỗi vòng đi bao xa, nhưng không chặn KL. | $-1{,}4$ so với $+0{,}4$; không cắt $J$ giảm $0{,}4$, có cắt giảm $0{,}008$; $3p-2$; mốc $0{,}73$, $0{,}8$; mức phẳng $0{,}27$; KL $0{,}049\to0{,}10$ | trên $s_B$ đứng riêng, hàm thay thế bằng đúng $J-J_{\mathrm{old}}$, nên ví dụ $s_B$ chỉ dùng để xem cơ chế, không làm hiện tượng (cổng 2026-11-20) |
| 6 | lời nhắc, sáu so sánh | Hai con đường khác nhau tới cùng một chính sách. | $\tfrac46\to\hat r=(\log2;0)\to(\tfrac45;\tfrac15)$; phần thưởng đã trừ KL $0{,}51$ ở cả hai câu; DPO $0{,}67\to0{,}74\to0{,}77\to0{,}78\to0{,}79\to0{,}8$ | không đưa hai vòng PPO của Ví dụ 10.27 lên trang (vòng 1 dừng ở $0{,}8$ do trùng hợp $\tfrac23\cdot1{,}2$) |

---

## 5. Các trang

### Mạch 1. Mở đầu (`id="mach-1"`, 8 trang, 12 phút)

Không có trang tiêu đề mạch (NT10, mạch mở đầu). Thứ tự theo TB19, TB20: bìa, một trang chữ (tiên quyết), ví dụ, hiện tượng thứ hai, câu hỏi trung tâm, mục tiêu, nội dung cùng sơ đồ neo. Hai trang chữ trước ví dụ đầu tiên.

#### `L10-1-01` · Bìa

- **Câu:** M. **Biết thêm:** tên bài và việc bài làm, bằng một dòng.
- **1 phút:** Bài này sửa hai điểm yếu của REINFORCE, rồi học chính sách cả khi phần thưởng chỉ đến từ so sánh của người.
- **Mới:** không. **Ý chính:** luận điểm một dòng (NT11, NT-RL-8).
- **Mặt trang:** "Học tăng cường" · "Bài 10" · "TRPO, PPO và DPO" · luận điểm "Sửa hai điểm yếu của REINFORCE, rồi học được cả khi chỉ có so sánh của người." (17 âm tiết; điều phối viên chốt 2026-11-20) · "Trường Đại học Công nghệ, Đại học Quốc gia Hà Nội" · "Năm học 2026–2027, học kỳ 1". Không tên giảng viên.
- **Hình:** không (bìa).
- **Ghi chú diễn giả:** "Bài trước dừng ở REINFORCE: mỗi lượt cho một mẫu không chệch của gradient. Hôm nay ta xem hai điểm yếu của nó trên một ví dụ nhỏ, sửa từng điểm, rồi áp cùng công cụ cho bài toán mà phần thưởng chỉ biết qua so sánh của người, như khi tinh chỉnh mô hình ngôn ngữ."
- **Nguồn:** ghi chú, đoạn mở §1.1.

#### `L10-1-02` · Tiên quyết và quy ước

- **Câu:** 1. **Biết thêm:** đúng hai công thức của Bài 09 mà mạch 1 dùng.
- **1 phút:** REINFORCE nhân hàm điểm với lợi tức, và trung bình của nó đúng bằng gradient; với hai hành động, hàm điểm có hai tọa độ ngược dấu.
- **Mới:** tên "hệ số" (số nhân với hàm điểm), dùng trong cả bài. **Ý chính:** dòng "Trung bình của $\widehat g$ trên nhiều lượt bằng $\nabla J$." (dòng thứ hai, chữ thường; trang nhắc lại không cần hộp).
- **Mặt trang** (≈ 50 âm tiết):
  - "Nhắc lại: REINFORCE thu một lượt bằng chính sách hiện tại, rồi đi một bước theo"
    $$\widehat g=\sum_t\gamma^t\,\underbrace{G_t}_{\text{lợi tức từ bước }t\text{: hệ số}}\,\underbrace{\psi_t}_{\text{hàm điểm}}.$$
  - "Ký hiệu: số nhân với hàm điểm ở bước $t$ gọi là hệ số của bước đó. Ở REINFORCE, hệ số là $G_t$."
  - "Trung bình của $\widehat g$ trên nhiều lượt bằng $\nabla J$."
  - "Nhắc lại: với hai hành động, $p$ là xác suất chọn hành động 1,"
    $$\psi(s,1)=(1-p)\,(1;\,-1),\qquad\psi(s,2)=-p\,(1;\,-1).$$
- **Hình:** không; lý do: trang chỉ nhắc hai công thức, hình hành lang đứng ở trang sau, nơi nó được dùng.
- **Ghi chú diễn giả:** "Hai công thức này là tất cả những gì mạch đầu cần. Hàm điểm của softmax hai hành động có hai tọa độ ngược dấu, nên trên ví dụ ta chỉ theo dõi tọa độ thứ nhất. Đặc trưng của mỗi hành động là vector đơn vị, nên $p=\sigma(\theta_1-\theta_2)$."
- **Nguồn:** Kiến thức tiên quyết (Định lý 09.23, Hệ quả 09.26, Mệnh đề 09.16).

#### `L10-1-03` · Ví dụ: hành lang ngắn (1)

- **Câu:** 1. **Biết thêm:** cách tính tọa độ thứ nhất của $\widehat g$ trên một lượt, và lượt ngắn nhất đẩy $p$ xuống.
- **1 phút:** Trên lượt sang phải, sang trái, sang phải, mọi lợi tức đều âm, nên REINFORCE giảm xác suất của mọi hành động đã chọn, và tổng là $-1$: $p$ giảm.
- **Mới:** $\widehat g_1$, tọa độ thứ nhất của $\widehat g$ ($p$ tăng khi $\widehat g_1>0$).
- **Ý chính:** hộp "Lời giải:" (fragment): "$p$ giảm, vì $\widehat g_1=-1$. Mọi lợi tức đều âm, nên hành động nào được chọn cũng bị giảm xác suất. Hành động 1 bị giảm nhiều hơn."
- **Mặt trang** (≈ 38 âm tiết ngoài bảng):
  - Dòng dữ kiện: "Mọi ô: $p=\tfrac12$, mỗi bước thưởng $-1$, $\gamma=1$. Chọn hành động 1 (sang phải) cho $\psi_1=+\tfrac12$, hành động 2 cho $-\tfrac12$. $p$ tăng khi $\widehat g_1>0$."
  - Bảng (khuôn bảng tính của cả bài, mỗi hàng một bước):

    | $t$ | ô | hành động | $G_t$ | $\psi_1$ | $G_t\psi_1$ |
    |---|---|---|---|---|---|
    | 0 | $s_1$ | 1 | $-3$ | $+\tfrac12$ | $-1{,}5$ |
    | 1 | $s_2$ | 2 | $-2$ | $-\tfrac12$ | $+1$ |
    | 2 | $s_3$ | 1 | $-1$ | $+\tfrac12$ | $-0{,}5$ |
    | | | | | **tổng** $\widehat g_1$ | **$-1$** |
  - Hộp "Câu hỏi: Lượt này đẩy $p$ lên hay xuống?"
  - Hộp "Lời giải:" như trên.
- **Hình:** hành lang bốn ô (vẽ lại `img/lec-09/short-corridor.svg` theo nhãn ≥ 20 px), đường đi của lượt: ba mũi tên đánh số $t=0,1,2$ từ $s_1$ tới $s_4$; ô $s_2$ viền nét đứt ghi "đảo hành động". Chiếm nửa trái, khoảng 45% thân trang. Tệp `hanh-lang-mot-luot.svg` (mục 6).
- **Dựng dần:** (0) hình, dữ kiện, ba cột đầu và cột $G_t$, hộp câu hỏi; (1) cột $\psi_1$; (2) cột $G_t\psi_1$ và hàng tổng, ô tổng khung đỏ; (3) hộp lời giải.
- **Ghi chú diễn giả:** "Để lớp đoán trước khi lật cột cuối. Đọc từng hàng: lợi tức từ bước $t$ là số bước còn lại với dấu trừ. Nhầm lẫn hay gặp: nghĩ rằng hành động dẫn tới đích phải được thưởng; ở đây mọi lợi tức âm nên mọi hành động bị phạt, chỉ khác nhau mức phạt."
- **Nguồn:** Ví dụ 10.2, lượt (a) và đoạn "Diễn giải".
- **Bố cục:**

```
┌──────────────────────────────────────────────────────────────┐
│ Ví dụ: hành lang ngắn (1)                                    │
├───────────────────────────┬──────────────────────────────────┤
│  [s1]→[s2┊]→[s3]→[s4]      │ Mọi ô: p=½, thưởng −1, γ=1 …     │
│   t=0   t=1   t=2          │ ┌──┬──┬───┬───┬────┬──────┐      │
│  (s2 viền đứt: đảo)        │ │t │ô │h.đ│G_t│ψ₁  │G_tψ₁ │      │
│                            │ │0 │s1│ 1 │−3 │+½  │−1,5  │ (2)  │
│                            │ │1 │s2│ 2 │−2 │−½  │+1    │      │
│                            │ │2 │s3│ 1 │−1 │+½  │−0,5  │      │
│                            │ │  │  │   │   │tổng│[−1]  │      │
│                            │ └──┴──┴───┴───┴────┴──────┘      │
├───────────────────────────┴──────────────────────────────────┤
│ Câu hỏi: Lượt này đẩy p lên hay xuống?   │ Lời giải: … (3)   │
└──────────────────────────────────────────────────────────────┘
```

#### `L10-1-04` · Ba lượt cho ba hướng cập nhật khác nhau

- **Câu:** 1. **Biết thêm:** mỗi lượt cho một hướng khác, có lượt ngược chiều gradient; trung bình trên mọi lượt có thể có mới bằng gradient đúng.
- **1 phút:** Ba chấm của ba lượt rơi ở $-1$, $1$, $-5{,}5$, xa vạch $2$ của gradient đúng; trung bình trên mọi lượt có thể có vẫn bằng $2$, nhưng từng lượt thì rất nhiễu.
- **Mới:** không (cùng phép tính của trang trước trên hai lượt nữa). **Ý chính:** tiêu đề; hộp "Mỗi lượt lệch xa $2$. Trung bình trên mọi lượt có thể có vẫn bằng $2$." (TB8, TB15: sinh viên không được đọc hình thành "REINFORCE lệch").
- **Mặt trang** (≈ 45 âm tiết ngoài bảng):
  - Dòng dữ kiện: "Hàm mục tiêu của hành lang: $J(p)=-2(2-p)/\bigl(p(1-p)\bigr)$. Tại $p=\tfrac12$: $J=-12$, $J'=8$, $\partial p/\partial\theta_1=p(1-p)=\tfrac14$, nên gradient đúng có tọa độ thứ nhất $8\cdot\tfrac14=2$."
  - Bảng (cùng cách tính của trang trước, một hàng mỗi lượt):

    | Lượt | Hành động | Lợi tức $G_0,\dots,G_{T-1}$ | Phép tính $\widehat g_1$ |
    |---|---|---|---|
    | (a) | $1,2,1$ | $-3,-2,-1$ | $\tfrac12(-3)-\tfrac12(-2)+\tfrac12(-1)$ |
    | (b) | $2,1,2,1$ | $-4,-3,-2,-1$ | $-\tfrac12(-4)+\tfrac12(-3)-\tfrac12(-2)+\tfrac12(-1)$ |
    | (c) | $1,1,1,2,1$ | $-5,-4,-3,-2,-1$ | $\tfrac12(-5-4-3-1)-\tfrac12(-2)$ |
  - Hộp như trên.
- **Hình:** trục số $\widehat g_1$ từ $-6$ tới $3$, cao khoảng 120 px CSS; ba chấm tròn ghi "(a) $-1$", "(b) $1$", "(c) $-5{,}5$" (ba màu trùng nhãn lượt trong bảng, kèm chữ); vạch đứng xanh, nét liền, ở $2$, hai nhãn "gradient đúng $2$" và "= trung bình của mọi lượt". Trải ngang dưới bảng. Kết quả của mỗi hàng chỉ ở trên trục, không lặp trong bảng (TB10). Tệp `hanh-lang-ba-luot.svg`.
- **Dựng dần:** (0) dòng dữ kiện, bảng, trục và vạch $2$; (1) chấm (a) (đã tính ở trang trước); (2) hàng (b) và chấm (b); (3) hàng (c) và chấm (c); (4) hộp.
- **Ghi chú diễn giả:** "Lượt (b) chọn sang trái hai lần với lợi tức lớn, nên đẩy $p$ lên; lượt (c) chọn sang phải bốn lần nên kéo $p$ xuống mạnh. Ba lượt ở đây có xác suất $\tfrac18$, $\tfrac1{16}$, $\tfrac1{32}$; các lượt dài hơn và hiếm hơn kéo trung bình lên đúng $2$. Lượt (c) đi một bước học $0{,}1$ thì $p$ rơi xuống $0{,}25$ và $J$ xuống $-18{,}7$."
- **Nguồn:** Ví dụ 10.2 (dữ kiện: $J(p)$, $J'(\tfrac12)=8$, $\partial p/\partial\theta_1=\tfrac14$; bảng ba lượt; "Ước lượng"; "Cập nhật theo lượt (c)"); Hệ quả 09.26 (trung bình bằng gradient).
- **Bố cục:**

```
┌──────────────────────────────────────────────────────────────┐
│ Ba lượt cho ba hướng cập nhật khác nhau                      │
├──────────────────────────────────────────────────────────────┤
│ J(p)=…; tại p=½: J=−12, J'=8, ∂p/∂θ₁=p(1−p)=¼, gradient đúng 2│
│ Lượt │ Hành động │ Lợi tức   │ Phép tính ĝ₁                   │
│ (a)  │ 1,2,1     │ −3,−2,−1  │ ½(−3)−½(−2)+½(−1)              │
│ (b)  │ 2,1,2,1   │ −4,…,−1   │ …                        (2)   │
│ (c)  │ 1,1,1,2,1 │ −5,…,−1   │ …                        (3)   │
├──────────────────────────────────────────────────────────────┤
│ −6   −5   −4  −3  −2  −1   0   1   2   3   → ĝ₁   (cao 120px) │
│  ●(c)                  ●(a)  ●(b) ┃xanh: gradient đúng 2        │
│                                   ┃= trung bình của mọi lượt   │
├──────────────────────────────────────────────────────────────┤
│ [hộp] Mỗi lượt lệch xa 2. Trung bình … vẫn bằng 2.   (4)      │
└──────────────────────────────────────────────────────────────┘
```

#### `L10-1-05` · Bước đúng hướng mà dài làm $J$ giảm

- **Câu:** 1. **Biết thêm:** ngay cả hướng đúng cũng hỏng khi bước quá dài, vì $J$ chỉ gần tuyến tính quanh chính sách cũ.
- **1 phút:** Trên đường cong $J(p)$ có đỉnh ở $p\approx0{,}59$: bước nhỏ dừng trước đỉnh và đưa $J$ lên $-11{,}7$, bước lớn đi xa qua đỉnh tới $p\approx0{,}88$ và $J$ rơi xuống $-21{,}3$.
- **Mới:** không. **Ý chính:** tiêu đề; hộp: "$J$ chỉ gần tuyến tính trong một lân cận nhỏ của chính sách cũ."
- **Mặt trang** (≈ 30 âm tiết): "Hai bước theo đúng gradient $(2;-2)$ từ $\theta=(0;0)$, tức $p=\tfrac12$, với $p=\sigma(\theta_1-\theta_2)$." · hộp như trên. Phép tính của mỗi bước ghi cạnh mũi tên trên hình.
- **Hình:** đồ thị $J(p)$ trên $p\in[0{,}2;0{,}95]$, trục tung từ $-25$ tới $-10$. Điểm đen $p=0{,}5$, nhãn "$J=-12$"; điểm đỉnh $p^*\approx0{,}59$, nhãn "đỉnh". Mũi tên xanh, nét liền, dừng trước đỉnh ở $p\approx0{,}55$, nhãn "bước học $0{,}05$: $p=\sigma(0{,}2)\approx0{,}55$, $J\approx-11{,}7$". Mũi tên đỏ, nét đậm, tới $p\approx0{,}88$, nhãn "bước học $0{,}5$: $p=\sigma(2)\approx0{,}88$, $J\approx-21{,}3$". Chiếm khoảng 60% thân trang. Tệp `hanh-lang-J-hai-buoc.svg`; bản thu nhỏ dùng lại ở `L10-1-06`, `L10-4-01`.
- **Dựng dần:** (0) đường cong và điểm $p=0{,}5$; (1) mũi tên xanh; (2) mũi tên đỏ; (3) hộp.
- **Ghi chú diễn giả:** "Hỏi lớp trước bước (2): bước dài gấp mười lần thì $J$ tăng nhiều hơn không? Gradient chỉ cho độ dốc tại điểm hiện tại; qua đỉnh, độ dốc đổi dấu. Bước $0{,}1$ đã vượt đỉnh một chút ($p\approx0{,}599$) dù $J$ vẫn tăng; bước $0{,}05$ cho hình rõ hơn. Trên mạng nơ-ron, ta không vẽ được đường cong này, nên cần một cách biết bước nào còn tin được."
- **Nguồn:** ghi chú §1.1, đoạn "Giới hạn thứ hai" sau Ví dụ 10.2 (hai bước học; bước nhỏ theo đề xuất sửa ghi chú G1, mục 11); Ví dụ 10.2, "Diễn giải" ($p^*=2-\sqrt2$).
- **Bố cục:**

```
┌──────────────────────────────────────────────────────────────┐
│ Bước đúng hướng mà dài làm J giảm                            │
├──────────────────────────────────────────────────────────────┤
│ Hai bước theo đúng gradient (2;−2) từ θ=(0;0), tức p=½ …     │
│  J                                                           │
│ −10┤          đỉnh p*≈0,59                                   │
│    │      ●─→● xanh: 0,05 → p≈0,55, J≈−11,7 (trước đỉnh)      │
│ −15┤    ●J=−12 ╲                                             │
│    │  ╱         ╲ ━━━━━━━━━━━→ ● đỏ: 0,5 → p≈0,88, J≈−21,3    │
│ −25┼──────────────────────────────── p                       │
├──────────────────────────────────────────────────────────────┤
│ [hộp] J chỉ gần tuyến tính trong một lân cận nhỏ …           │
└──────────────────────────────────────────────────────────────┘
```

#### `L10-1-06` · Vấn đề trung tâm

- **Câu:** M (trạm dừng của mạch 1). **Biết thêm:** hai câu hỏi của cả bài, mỗi câu gắn với một hình vừa xem.
- **1 phút:** Từ hai hình, bài đặt hai câu hỏi: làm sao để hướng ít dao động, và làm sao đi bước lớn mà $J$ không giảm.
- **Mới:** không. **Ý chính:** hộp "Câu hỏi:".
- **Mặt trang** (≈ 22 âm tiết): hai hình thu nhỏ đặt ngang (trục số của `L10-1-04`, đồ thị của `L10-1-05`), dưới mỗi hình một nhãn "dao động", "bước dài". Hộp "Câu hỏi: 1. Làm sao ước lượng gradient ít dao động hơn? 2. Làm sao đi bước lớn mà $J$ không giảm?"
- **Hình:** hai bản thu nhỏ, mỗi bản khoảng 40% chiều ngang; không hình mới.
- **Dựng dần:** không.
- **Ghi chú diễn giả:** "Câu trả lời theo mạch, chỉ ở lời giảng: mạch 2 và 3 trả lời câu 1 bằng đường cơ sở, critic và GAE; mạch 4 và 5 trả lời câu 2 bằng hàm thay thế, miền tin cậy, TRPO và PPO. Mạch 6 dùng các công cụ đó khi phần thưởng chỉ biết qua so sánh của người, một câu hỏi mà ví dụ hành lang chưa đặt ra."
- **Nguồn:** ghi chú §1.1, đoạn "bài toán trung tâm của chương" (hai phần đầu; phần thứ ba mở mạch 6, quyết định 8).

#### `L10-1-07` · Mục tiêu học tập

- **Câu:** M. **Biết thêm:** năm việc sinh viên làm được sau bài, mỗi mạch một việc.
- **1 phút:** Năm sản phẩm kiểm được, mỗi dòng một mạch, bằng lời thường.
- **Mới:** không. **Ý chính:** danh sách.
- **Mặt trang** (≈ 95 âm tiết, trang mục tiêu): "Sau bài này, sinh viên có thể:"
  1. "Giảm dao động của ước lượng gradient mà giữ nguyên trung bình."
  2. "Trộn đánh giá một bước với lợi tức cả lượt bằng một tham số, và tính hệ số trên một lượt."
  3. "Đoán mức thay đổi của $J$ khi đổi chính sách, chỉ bằng dữ liệu cũ, và nói khi nào phép đoán sai."
  4. "Giữ chính sách mới gần chính sách cũ bằng phép cắt tỉ số xác suất, và tìm chính sách mà vòng cập nhật dừng lại."
  5. "Tìm chính sách tốt nhất khi chỉ có các lần người so sánh hai câu trả lời."
- **Hình:** không; lý do: trang danh sách (TB19).
- **Ghi chú diễn giả:** "Danh sách đầy đủ chín mục tiêu ở đầu ghi chú, gồm cả các chứng minh. Trên lớp, mỗi dòng ứng với một mạch và một phép tính trên ví dụ."
- **Nguồn:** Mục tiêu học tập 1–9 của ghi chú (gom theo mạch: 1–2 → dòng 1; 3 → 2; 4–5 → 3; 6–7 → 4; 8–9 → 5).

Năm dòng theo TB19 (3–5 dòng, mỗi mạch một dòng; điều phối viên chấp nhận 2026-11-20).

#### `L10-1-08` · Nội dung

- **Câu:** M. **Biết thêm:** vòng năm khối mà mọi phương pháp của bài sửa một hoặc hai chỗ, và mạch nào sửa khối nào.
- **1 phút:** Mọi thuật toán của bài là một vòng thu lượt, tính hệ số, cập nhật; hai dấu "?" đỏ là hai chỗ hỏng vừa thấy; mỗi mạch sửa một hoặc hai khối.
- **Mới:** sơ đồ neo. **Ý chính:** hình (hai dấu "?" đỏ ở ④ và ⑤).
- **Mặt trang** (≈ 50 âm tiết, trang nội dung): sơ đồ neo đầy đủ bên trái; bên phải, cột tên mạch, mỗi tên nối bằng đường mảnh tới khối nó đổi: "2. So lợi tức với giá trị của trạng thái" → ③, ④; "3. Trộn đánh giá một bước và cả lượt" → ④; "4. Đánh giá chính sách mới bằng dữ liệu cũ" → ⑤; "5. Giữ chính sách mới gần chính sách cũ" → ⑤; "6. Học từ so sánh của người" → ①; "7. Tổng kết". Dấu "?" đỏ ở ④ ghi "dao động", ở ⑤ ghi "bước dài làm $J$ giảm".
- **Hình:** `so-do-neo-m1.svg`, khoảng 55% thân trang (mục 3).
- **Dựng dần:** không.
- **Ghi chú diễn giả:** "Đây là vòng của REINFORCE: phần thưởng, thu lượt, hệ số là lợi tức, một bước gradient, rồi chính sách mới thành chính sách cũ. Khối ③ còn trống. Hệ số là số nhân với hàm điểm; ở REINFORCE đó là lợi tức. Đầu mỗi mạch sẽ hiện lại hình này, tô khối mạch sửa; cuối mạch, khối đó có nhãn mới."
- **Nguồn:** hình `central-problem.svg` của ghi chú §1.1 (ba hàng mục), sắp lại thành vòng.
- **Bố cục:**

```
┌──────────────────────────────────────────────────────────────┐
│ Nội dung                                                     │
├──────────────────────────────────┬───────────────────────────┤
│ ①Phần thưởng → ②Thu lượt ◀──┐    │ 2. So lợi tức … ──→ ③④     │
│                  ↓            │    │ 3. Trộn … ──────→ ④        │
│ ┊③ chưa có┊ ─→ ④Hệ số: G_t ?đỏ│    │ 4. Đánh giá … ──→ ⑤        │
│                  ↓            │    │ 5. Giữ … ───────→ ⑤        │
│             ⑤Một bước ?đỏ ───┘    │ 6. Học từ so sánh → ①      │
│                                  │ 7. Tổng kết               │
└──────────────────────────────────┴───────────────────────────┘
```

### Mạch 2. So lợi tức với giá trị của trạng thái (`id="mach-2"`, 9 trang thật, 7 trang đếm, 19 phút)

Ví dụ chạy: chuỗi hai trạng thái, chính sách cũ $p_A=\tfrac12$, $p_B=\tfrac23$, $\gamma=0{,}9$. Một khuôn bảng cho cả mạch (NT-RL-5, TB16): hàng là ba loại lượt, cột theo thứ tự tính, cột kết quả thêm dần. `L10-2-01` → `L10-2-03` là chuỗi trang liên tiếp cùng bố cục (tính một trang).

#### `L10-2-00` · Trang tiêu đề mạch 2 (điểm vào mạch 2)

- **Câu:** 2. **Biết thêm:** việc của mạch, bằng một hiện tượng.
- **1 phút:** Mạch này sửa khối hệ số và thêm khối thứ ba trên vòng cập nhật, vì một nửa số lượt đẩy chính sách sai hướng.
- **Mới:** không. **Ý chính:** dòng dẫn.
- **Mặt trang:** `span.strand-number` "2." · `h2` "So lợi tức với giá trị của trạng thái" · `p.strand-lead` "Một nửa số lượt trên chuỗi hai trạng thái đẩy chính sách sai hướng." (15 âm tiết). Không `p.strand-keys` (các thuật ngữ của mạch chưa được dạy, TB11).
- **Hình:** sơ đồ neo thu nhỏ `so-do-neo-m2-vao.svg`: ③ và ④ tô tím, ④ còn nhãn "$G_t$" kèm "?"; khối khác mờ (TB2, NT12 sửa theo TB).
- **Ghi chú diễn giả:** "Mạch trước cho thấy một lượt REINFORCE là một mẫu ồn của gradient. Mạch này giữ nguyên trung bình mà giảm độ ồn: so lợi tức với mức thường có ở trạng thái, rồi để một hàm giá trị đánh giá hành động ngay sau một bước. Kết quả chuyển sang mạch sau là hệ số $\delta_t$ và câu hỏi khi hàm giá trị học dở."
- **Nguồn:** ghi chú §2, đoạn mở.

#### `L10-2-01` · Ví dụ: chuỗi hai trạng thái (1)

- **Câu:** 2. **Biết thêm:** REINFORCE thưởng cả hành động kém hơn mức thường có, khi phần thưởng của nó dương.
- **1 phút:** Lượt "ở $s_A$ chọn 2, nhận 1" xảy ra một nửa số lần và tăng xác suất của hành động 2, dù thưởng $1$ ít hơn mức $1{,}4$ thường có ở $s_A$; trung bình của cột vẫn bằng gradient đúng $0{,}2$.
- **Mới:** chuỗi hai trạng thái (đối tượng). **Ý chính:** hàng thứ ba tô đỏ kèm nhãn "tăng xác suất hành động 2, dù $1<1{,}4$"; hộp "Câu hỏi:".
- **Mặt trang** (≈ 45 âm tiết ngoài bảng):
  - Dòng dữ kiện: "$\gamma=0{,}9$, chính sách cũ $p_A=\tfrac12$, $p_B=\tfrac23$. Tại $s_A$: $\psi_A=+0{,}5$ khi chọn 1, $-0{,}5$ khi chọn 2. Gradient đúng theo $\theta_A$: $p_A(1-p_A)(2{,}7p_B-1)=0{,}25\cdot0{,}8=0{,}2$."
  - Bảng:

    | Loại lượt | Xác suất | $G_0$ | $\psi_A$ | tọa độ $\theta_A$ của $\widehat g$, REINFORCE: $G_0\psi_A$ |
    |---|---|---|---|---|
    | $s_A\xrightarrow1s_B\xrightarrow1$ | $\tfrac13$ | $0{,}9\cdot3=2{,}7$ | $+0{,}5$ | $1{,}35$ |
    | $s_A\xrightarrow1s_B\xrightarrow2$ | $\tfrac16$ | $0$ | $+0{,}5$ | $0$ |
    | $s_A\xrightarrow2$ | $\tfrac12$ | $1$ | $-0{,}5$ | **$-0{,}5$** (đỏ) |
    | trung bình | | | | $0{,}2$ (= gradient đúng) |
    | phương sai | | | | $0{,}69$ |
  - Hộp "Câu hỏi: Làm sao để mỗi lượt chỉ tăng xác suất của hành động tốt hơn mức thường có ở trạng thái, mà trung bình vẫn bằng gradient?"
- **Hình:** chuỗi hai trạng thái (vẽ lại `two-state-chain.svg`, nhãn ≥ 20 px): ô $s_A$ ghi "$v_\pi(s_A)=\tfrac12\cdot0{,}9\cdot2+\tfrac12\cdot1=1{,}4$", ô $s_B$ ghi "$v_\pi(s_B)=\tfrac23\cdot3=2$"; cung "1, thưởng 0" từ $s_A$ sang $s_B$, cung "2, thưởng 1" từ $s_A$ tới ô kết thúc (cung này đỏ, nhãn "$1<1{,}4$"); hai cung từ $s_B$ "1, thưởng 3", "2, thưởng 0". Nửa trái, khoảng 40% thân trang. Tệp `chuoi-gia-tri.svg`.
- **Dựng dần:** (0) hình, dữ kiện, bảng tới cột $\psi_A$; (1) cột REINFORCE, hai hàng trung bình, phương sai; (2) tô đỏ hàng ba và hộp câu hỏi.
- **Ghi chú diễn giả:** "Ba loại lượt phủ mọi khả năng, với xác suất $\tfrac12\cdot\tfrac23$, $\tfrac12\cdot\tfrac13$ và $\tfrac12$. Trung bình của cột là $0{,}2$, đúng tọa độ $\theta_A$ của gradient $(0{,}2;0{,}3)$: REINFORCE không lệch, chỉ nhiễu. Hỏi lớp: hành động 2 ở $s_A$ tốt hay kém? Nó cho $1$, còn trung bình ở $s_A$ là $1{,}4$, nên kém; REINFORCE vẫn tăng xác suất của nó vì $1>0$. Tọa độ $\theta_B$ ở ghi chú; phương sai của nó không đổi qua các cột."
- **Nguồn:** Ví dụ 10.6 (giá trị, gradient, bảng ba loại lượt, đoạn sau bảng).
- **Bố cục:**

```
┌──────────────────────────────────────────────────────────────┐
│ Ví dụ: chuỗi hai trạng thái (1)                              │
├───────────────────────┬──────────────────────────────────────┤
│  [s_A v=1,4]─1,0─▶[s_B v=2]─1,3─▶■   │ γ=0,9; p_A=½, p_B=⅔ …  │
│      │               └─2,0─▶■        │ Loại │xs │G₀ │ψ_A│REINF│
│      └─2,1 (đỏ: 1<1,4)─▶■            │ A1B1 │⅓ │2,7│+½ │1,35 │
│                                      │ A1B2 │⅙ │0  │+½ │0    │
│                                      │ A2   │½ │1  │−½ │−0,5▌│ đỏ
│                                      │ tb 0,2 · ps 0,69         │
├───────────────────────┴──────────────────────────────────────┤
│ Câu hỏi: Làm sao để mỗi lượt chỉ tăng xác suất …              │
└──────────────────────────────────────────────────────────────┘
```

#### `L10-2-02` · Trừ giá trị của trạng thái: trung bình giữ, dao động giảm

- **Câu:** 2. **Biết thêm:** trừ $v_\pi(S_t)$ khỏi lợi tức sửa chiều của lượt $s_A\xrightarrow2$, giữ trung bình $0{,}2$, hạ phương sai.
- **1 phút:** Cột mới "trừ $v_\pi$" có cùng trung bình $0{,}2$, phương sai $0{,}20$ thay cho $0{,}69$, và lượt sai dấu chỉ còn một phần sáu.
- **Mới:** đường cơ sở (baseline) $b(S_t)$, mức trừ khỏi lợi tức.
- **Ý chính:** tiêu đề; hộp "Trung bình vẫn $0{,}2$; phương sai giảm từ $0{,}69$ xuống $0{,}20$." (không dấu chấm phẩy trên mặt trang: viết thành hai câu).
- **Mặt trang** (≈ 30 âm tiết ngoài bảng):
  - Công thức: $$\text{hệ số mới}=\underbrace{G_t}_{\text{lợi tức}}-\underbrace{b(S_t)}_{\text{đường cơ sở, ở đây }v_\pi(S_t)}$$
  - Bảng của `L10-2-01` thêm cột "tọa độ $\theta_A$, trừ $v_\pi$: $(G_0-1{,}4)\psi_A$": $1{,}3\cdot0{,}5=0{,}65$; $-1{,}4\cdot0{,}5=-0{,}7$; $(-0{,}4)(-0{,}5)=0{,}2$ (xanh); trung bình $0{,}2$; phương sai $0{,}20$; thêm hàng "xác suất hệ số âm": $\tfrac12$ → $\tfrac16$.
  - Hộp: "Trung bình vẫn $0{,}2$. Phương sai giảm từ $0{,}69$ xuống $0{,}20$."
- **Hình:** chuỗi của `L10-2-01` thu thành dải ngang cao khoảng 110 px CSS phía trên bảng (bảng cần chiều ngang); cột $\psi_A$ chuyển thành dòng dữ kiện; ô mới của hàng ba tô xanh. Không đổi màu cung (không mang ý mới).
- **Dựng dần:** (0) bố cục của trang trước với công thức; (1) cột mới; (2) hàng xác suất âm và hộp.
- **Ghi chú diễn giả:** "Lượt thứ hai xấu đi, từ $0$ xuống $-0{,}7$: đường cơ sở không làm mọi lượt đúng chiều. Điều nó làm là gom các lượt lại gần trung bình: phương sai của cả cột giảm, và xác suất một lượt cho hệ số âm giảm từ một nửa xuống một phần sáu."
- **Nguồn:** Ví dụ 10.6 (cột "trừ $v_\pi$", hai phương sai, xác suất hệ số âm); Định nghĩa 10.1.

#### `L10-2-03` · Câu hỏi nhanh: trừ mức của hành động

- **Câu:** 2. **Biết thêm:** mức trừ phải không phụ thuộc hành động đang chọn; trừ $q$ làm trung bình thành $0$.
- **1 phút:** Thử trừ $q(s_A,A_0)$: cột mới có trung bình $0$ thay cho $0{,}2$, nên mức trừ không được phụ thuộc hành động.
- **Mới:** không (dùng $q_\pi$ đã biết). **Ý chính:** hộp "Lời giải:".
- **Mặt trang** (≈ 30 âm tiết ngoài bảng):
  - Dòng: "Nhắc lại: $q_\pi(s_A,1)=0{,}9\cdot2=1{,}8$, $q_\pi(s_A,2)=1$."
  - Bảng của `L10-2-02` thêm cột "trừ $q_\pi$: $(G_0-q_\pi(s_A,A_0))\psi_A$" với ba ô "?" đỏ; fragment điền $(2{,}7-1{,}8)\cdot0{,}5=0{,}45$; $(0-1{,}8)\cdot0{,}5=-0{,}9$; $(1-1)(-0{,}5)=0$; trung bình $\tfrac13\cdot0{,}45-\tfrac16\cdot0{,}9=0$.
  - Hộp "Câu hỏi: Trừ $q_\pi(S_t,A_t)$ thay cho $v_\pi(S_t)$ có giữ trung bình $0{,}2$ không?"
  - Hộp "Lời giải: Không, trung bình thành $0$. Mức $q_\pi(S_t,A_t)$ phụ thuộc hành động vừa chọn."
- **Hình:** dải chuỗi 110 px của `L10-2-02`.
- **Dựng dần:** (0) câu hỏi và cột "?"; (1) ba ô và trung bình; (2) lời giải.
- **Ghi chú diễn giả:** "Cho lớp một phút. Trừ $q$ của chính hành động vừa chọn thì hệ số chỉ còn phần ngẫu nhiên của phần đuôi lượt; thông tin về việc hành động nào tốt hơn mất hết. Đây là giả thiết mà mệnh đề ở trang sau đặt lên đường cơ sở."
- **Nguồn:** ghi chú §2.1, phản ví dụ "Bỏ đường cơ sở không phụ thuộc hành động" (dạng trên chuỗi do câu chuyện mạch 2 tính, `cau-chuyen-deck-2026-11-20.md` mục 4.2).
- **Bố cục** (cũng là bố cục của `L10-2-02`, bỏ cột cuối): bảng sáu cột (loại lượt, xác suất, $G_0$, ba cột tọa độ $\theta_A$), nhãn hàng giữ mũi tên ở cỡ chữ của bảng; các ô chỉ ghi phép tính ngắn; phải đo trên ảnh 1600×900, không tràn.

```
┌──────────────────────────────────────────────────────────────┐
│ Câu hỏi nhanh: trừ mức của hành động                         │
├──────────────────────────────────────────────────────────────┤
│ [dải chuỗi 110px: s_A ─1,0─▶ s_B ─1,3 / 2,0─▶ ■ ; s_A ─2,1─▶ ■] │
│ Nhắc lại: q_π(s_A,1)=0,9·2=1,8, q_π(s_A,2)=1. ψ_A=±0,5.       │
│ Loại lượt   │xs│G₀ │REINF│trừ v_π│trừ q_π                       │
│ s_A→1 s_B→1 │⅓ │2,7│1,35 │0,65   │?→(2,7−1,8)·0,5=0,45          │
│ s_A→1 s_B→2 │⅙ │0  │0    │−0,7   │?→(0−1,8)·0,5=−0,9            │
│ s_A→2       │½ │1  │−0,5 │0,2    │?→(1−1)(−0,5)=0               │
│ trung bình  │  │   │0,2  │0,2    │?→0                       (1) │
├───────────────────────────────┬──────────────────────────────┤
│ Câu hỏi: Trừ q_π … giữ 0,2?    │ Lời giải: Không … (2)         │
└───────────────────────────────┴──────────────────────────────┘
```

#### `L10-2-04` · Trừ một mức của trạng thái không đổi trung bình

- **Câu:** 2. **Biết thêm:** kết quả chung: mọi đường cơ sở chỉ phụ thuộc trạng thái giữ kỳ vọng của gradient.
- **1 phút:** Miễn là mức trừ chỉ phụ thuộc trạng thái và lượt do chính chính sách sinh ra, ước lượng mới vẫn có trung bình bằng gradient.
- **Mới:** mệnh đề đường cơ sở (một trong ba khối "Giả thiết:/Kết luận:" của bài).
- **Ý chính:** tiêu đề.
- **Mặt trang** (≈ 40 âm tiết):
  - "Mệnh đề (đường cơ sở)."
  - "Giả thiết: $b$ chỉ phụ thuộc trạng thái, không phụ thuộc hành động đang chọn. Lượt do chính $\pi_\theta$ sinh ra."
  - "Kết luận:" $$\mathbb E\Bigl[\sum_t\gamma^t\bigl(G_t-b(S_t)\bigr)\psi_t\Bigr]=\nabla J.$$
  - "Ý nghĩa: cột "trừ $v_\pi$" là trường hợp $b=v_\pi$; cột "trừ $q_\pi$" vi phạm giả thiết thứ nhất."
- **Hình:** không; lý do: bằng chứng là bảng của ba trang trước, trang này chỉ phát biểu điều bảng đã cho thấy.
- **Dựng dần:** không.
- **Ghi chú diễn giả:** "Đây là Mệnh đề 10.2 của ghi chú; giả thiết kỹ thuật (đường cơ sở bị chặn, bốn giả thiết của định lý gradient chính sách) ở đó. Mệnh đề chỉ nói về trung bình: một đường cơ sở chọn dở, như $b=3$ trên bài toán một bước của ghi chú, làm phương sai tăng. Bỏ giả thiết thứ hai, chẳng hạn chọn hành động đều thay cho theo $\pi_\theta$, thì kỳ vọng cũng lệch."
- **Nguồn:** Mệnh đề 10.2 (Giả thiết, Kết luận, Phạm vi); đoạn phản ví dụ sau chứng minh.

#### `L10-2-05` · Ý tưởng chứng minh: đường cơ sở

- **Câu:** 2. **Biết thêm:** lý do một dòng: hàm điểm có trung bình $0$ tại mỗi trạng thái.
- **1 phút:** Tổng có trọng số của các hàm điểm là gradient của tổng xác suất, tức gradient của $1$, nên bằng $0$; trên $s_A$, $\tfrac12\cdot0{,}5+\tfrac12\cdot(-0{,}5)=0$.
- **Mới:** đẳng thức $\sum_a\pi\psi=0$ (trang ý tưởng chứng minh duy nhất của bài, quyết định 7).
- **Ý chính:** hộp "Hàm điểm có trung bình $0$ tại mỗi trạng thái, nên phần bị trừ có trung bình $0$."
- **Mặt trang** (≈ 35 âm tiết):
  - $$\sum_a\underbrace{\pi(a\mid s)\,\psi(s,a)}_{=\nabla_\theta\pi(a\mid s)}=\nabla_\theta\underbrace{\sum_a\pi(a\mid s)}_{=1}=0.$$
  - "Trên $s_A$: $\tfrac12\cdot0{,}5+\tfrac12\cdot(-0{,}5)=0$."
  - "$b(s)$ không đổi theo hành động, nên ra ngoài tổng: $\sum_a\pi(a\mid s)\,b(s)\,\psi(s,a)=b(s)\cdot0$."
  - hộp như trên.
- **Hình:** không; lý do: một đẳng thức với một phép kiểm số; vẽ hai mũi tên $\pm0{,}5$ không thêm gì cho dòng kiểm số.
- **Dựng dần:** fragment theo ba dòng: đẳng thức; kiểm số; phép đưa $b(s)$ ra ngoài; rồi hộp.
- **Ghi chú diễn giả:** "Cùng một dòng này còn dùng hai lần: lợi thế có trung bình $0$ theo chính sách, và GAE với $\lambda=1$ không làm lệch gradient. Với $q_\pi(S_t,A_t)$ thì bước đưa ra ngoài tổng không làm được, vì mức trừ đổi theo $a$. Chứng minh đủ ba bước, với tính chất tháp, ở ghi chú."
- **Nguồn:** chứng minh Mệnh đề 10.2, Bước 2; Mệnh đề 09.17.

#### `L10-2-06` · Hệ số trung bình là lợi thế

- **Câu:** 2. **Biết thêm:** hệ số "lợi tức trừ giá trị" có trung bình là lợi thế $q_\pi-v_\pi$, và gradient chỉ cần lợi thế.
- **1 phút:** Trên chuỗi, mỗi cung ghi lợi thế của hành động: $+0{,}4$ và $-0{,}4$ ở $s_A$, $+1$ và $-2$ ở $s_B$; hành động tốt hơn mức thường có thì lợi thế dương.
- **Mới:** hàm lợi thế $A_\pi$.
- **Ý chính:** tiêu đề; định nghĩa một câu.
- **Mặt trang** (≈ 45 âm tiết):
  - "Định nghĩa. Lợi thế (advantage) của hành động $a$ tại $s$ đo hành động đó tốt hơn mức thường có bao nhiêu:" $$A_\pi(s,a)=q_\pi(s,a)-v_\pi(s).$$
  - "Hệ số $G_t-v_\pi(S_t)$ có trung bình $A_\pi(S_t,A_t)$, nên gradient chỉ cần lợi thế:" $$\nabla J=\mathbb E\Bigl[\sum_t\gamma^t\,A_\pi(S_t,A_t)\,\psi_t\Bigr].$$
  - "Còn thiếu: $q_\pi$ và $v_\pi$ chưa biết." (trang kết quả, không tính là trạm dừng)
- **Hình:** chuỗi của `L10-2-01`, mỗi cung ghi lợi thế cạnh phép tính: "$1{,}8-1{,}4=+0{,}4$", "$1-1{,}4=-0{,}4$", "$3-2=+1$", "$0-2=-2$"; cung lợi thế dương nét liền xanh, âm nét đứt đỏ. Bên trái, khoảng 40%. Tệp `chuoi-loi-the.svg`.
- **Dựng dần:** (0) định nghĩa và hình; (1) câu và công thức gradient; (2) dòng "Còn thiếu".
- **Ghi chú diễn giả:** "Cùng một trạng thái, lợi thế và giá trị hành động xếp các hành động theo cùng thứ tự; lợi thế chỉ trừ đi mức chung. Kiểm nhanh: $\tfrac12\cdot0{,}4+\tfrac12\cdot(-0{,}4)=0$ và $\tfrac23\cdot1+\tfrac13\cdot(-2)=0$, đúng đẳng thức của trang trước. Trên bài toán thật, ta không biết $q_\pi$, $v_\pi$, nên cần ước lượng lợi thế từ dữ liệu."
- **Nguồn:** Định nghĩa 10.4, Mệnh đề 10.5 (câu lời thường, câu chuyện mục 5); Ví dụ 10.6 (lợi thế).

#### `L10-2-07` · Critic đánh giá hành động ngay sau một bước

- **Câu:** 2. **Biết thêm:** sai số TD với một hàm giá trị đúng cho ngay lợi thế của hành động vừa chọn, không cần chờ hết lượt.
- **1 phút:** Từ $s_A$ chọn 1 sang $s_B$: $0+0{,}9\cdot2-1{,}4=0{,}4$, đúng lợi thế; hàm giá trị dùng theo cách này gọi là critic.
- **Mới:** critic (và tên actor cho chính sách).
- **Ý chính:** tiêu đề; câu "Khi $\hat v=v_\pi$, $\delta_t$ trung bình bằng lợi thế của hành động vừa chọn."
- **Mặt trang** (≈ 40 âm tiết):
  - "Nhắc lại: sai số TD"
    $$\delta_t=\underbrace{R_{t+1}+\gamma\,\hat v(S_{t+1})}_{\text{lợi tức một bước}}-\underbrace{\hat v(S_t)}_{\text{mức của trạng thái}}.$$
  - "Critic là hàm giá trị $\hat v$ dùng để đánh giá hành động qua trạng thái kế tiếp. Chính sách gọi là actor."
  - "Khi $\hat v=v_\pi$, $\delta_t$ trung bình bằng lợi thế của hành động vừa chọn."
- **Hình:** một bước chuyển: ô $s_A$ ("$\hat v=1{,}4$") —cung "hành động 1, thưởng 0"→ ô $s_B$ ("$\hat v=2$"); dưới cung ghi phép tính "$0+0{,}9\cdot2-1{,}4=0{,}4=A_\pi(s_A,1)$"; mũi tên từ $\delta_t$ tới khối "actor" (nhãn "hệ số của hàm điểm") và tới khối "critic" (nhãn "sai lệch để học $\hat v$"). Khoảng 45% thân trang, bên phải. Tệp `critic-mot-buoc.svg`.
- **Dựng dần:** (0) công thức và hình bước chuyển; (1) định nghĩa; (2) câu kết luận.
- **Ghi chú diễn giả:** "Đường cơ sở chỉ đánh giá trạng thái trước khi chọn hành động; critic đánh giá cả trạng thái sau, nên chấm được hành động. Cùng số $\delta_t$ làm hai việc: hệ số cho actor, sai lệch cho critic học (TD(0) của Bài 07). Với hành động 2 ở $s_A$: $1-1{,}4=-0{,}4$. Nhầm lẫn hay gặp: lấy kỳ vọng của $\delta_t$ chỉ theo trạng thái, khi đó nó bằng $0$."
- **Nguồn:** Định nghĩa 10.7, Mệnh đề 10.8(a) (câu lời thường), đoạn sau Mệnh đề 10.8; hình `actor-critic-advantage.svg` của ghi chú (rút gọn).
- **Bố cục:**

```
┌──────────────────────────────────────────────────────────────┐
│ Critic đánh giá hành động ngay sau một bước                  │
├──────────────────────────────┬───────────────────────────────┤
│ Nhắc lại: sai số TD           │ [s_A v̂=1,4] ─1, thưởng 0─▶ [s_B v̂=2] │
│ δ_t = R+γv̂(S') − v̂(S)         │      0 + 0,9·2 − 1,4 = 0,4       │
│      └lợi tức 1 bước┘ └mức┘   │            = A_π(s_A,1)          │
│ Critic là … Actor …   (1)     │   δ_t ──▶ actor │ ──▶ critic      │
│ Khi v̂=v_π, δ_t trung bình … (2)│                                │
└──────────────────────────────┴───────────────────────────────┘
```

#### `L10-2-08` · Với critic đúng, mọi lượt cho cùng tọa độ $0{,}2$

- **Câu:** 2 (trạm dừng cuối mạch 2). **Biết thêm:** so ba cách lập hệ số trên cùng ba loại lượt: cùng trung bình, phương sai của tọa độ $\theta_A$ $0{,}69\to0{,}20\to0$.
- **1 phút:** Ba cột cùng trung bình $0{,}2$; với critic đúng, mọi lượt cho đúng $0{,}2$ ở tọa độ $\theta_A$; vòng cập nhật giờ có khối critic và hệ số $\delta_t$.
- **Mới:** không (gom ý). **Ý chính:** dòng lớn dưới bảng "Tọa độ $\theta_A$: trung bình $0{,}2$ ở cả ba cột. Phương sai $0{,}69$; $0{,}20$; $0$." (TB18: kết luận đặt ngoài bảng, chữ lớn).
- **Mặt trang** (≈ 45 âm tiết ngoài bảng):
  - Bảng khuôn của mạch, cột "tọa độ $\theta_A$ của $\widehat g$" với ba cách lập hệ số: "REINFORCE" ($1{,}35$; $0$; $-0{,}5$), "trừ $v_\pi$" ($0{,}65$; $-0{,}7$; $0{,}2$), "$\delta_0$, critic đúng" với phép tính trong ô: $0{,}4\cdot0{,}5=0{,}2$; $0{,}4\cdot0{,}5=0{,}2$; $(-0{,}4)(-0{,}5)=0{,}2$.
  - Dòng lớn như trên.
  - Dòng nhỏ: "Ở $s_B$, hành động vẫn ngẫu nhiên: phương sai của tọa độ $\theta_B$ giữ $0{,}18$."
  - "Còn thiếu: critic phải học từ dữ liệu, và critic học dở thì $\delta_t$ lệch."
- **Hình:** sơ đồ neo thu nhỏ `so-do-neo-m2-ra.svg` ở dải dưới cạnh dòng "Còn thiếu" (cao khoảng 140 px CSS): ③ thành khối liền "critic $\hat v$", ④ ghi "hệ số: $G_t\to G_t-v_\pi(S_t)\to\delta_t$". Bảng là bằng chứng chính.
- **Dựng dần:** (0) bảng hai cột cũ; (1) cột $\delta_0$; (2) dòng lớn và dòng $\theta_B$; (3) sơ đồ neo và dòng "Còn thiếu".
- **Ghi chú diễn giả:** "Hai lượt đầu có cùng $\delta_0$, vì $\delta_0$ chỉ nhìn bước đầu. Phần ngẫu nhiên ở $s_B$ không còn đi vào hệ số của $s_A$. Ở $s_B$, hành động tại chính $s_B$ còn ngẫu nhiên, nên critic đúng không xóa được dao động của tọa độ $\theta_B$. Trên bài toán lớn, critic là một mạng học song song với chính sách, và nó không bao giờ đúng hẳn; mạch sau xem điều đó làm hỏng gì."
- **Nguồn:** Ví dụ 10.6 (cột $\delta_t$; phương sai $\theta_B$ $0{,}18$); Thuật toán 10.9 (chỉ dòng ④ của sơ đồ neo, câu chuyện mục 5).
- **Bố cục:**

```
┌──────────────────────────────────────────────────────────────┐
│ Với critic đúng, mọi lượt cho cùng tọa độ 0,2                │
├──────────────────────────────────────────────────────────────┤
│ Loại lượt        │ xs │ REINF │ trừ v_π │ δ₀, critic đúng      │
│ s_A→1 s_B→1      │ ⅓  │ 1,35  │ 0,65    │ 0,4·0,5=0,2          │
│ s_A→1 s_B→2      │ ⅙  │ 0     │ −0,7    │ 0,4·0,5=0,2          │
│ s_A→2            │ ½  │ −0,5  │ 0,2     │ (−0,4)(−0,5)=0,2     │
│ Tọa độ θ_A: trung bình 0,2 ở cả ba cột. Phương sai 0,69; 0,20; 0│
│ Ở s_B, hành động vẫn ngẫu nhiên: phương sai θ_B giữ 0,18.     │
├────────────────────────────────┬─────────────────────────────┤
│ [neo nhỏ: ③ critic → ④ G→G−v→δ]│ Còn thiếu: critic phải học …  │
└────────────────────────────────┴─────────────────────────────┘
```

### Mạch 3. Trộn đánh giá một bước và cả lượt (`id="mach-3"`, 6 trang, 12 phút)

Ví dụ chạy: cùng chuỗi, critic cố định $\hat v=(1{,}4;\,1)$ (đúng ở $s_A$, đánh giá thấp $s_B$; giá trị thật $(1{,}4;\,2)$), hai lượt cùng bắt đầu bằng hành động 1 ở $s_A$. Khuôn bảng: hàng là hai lượt, cột là cách ước lượng.

#### `L10-3-00` · Trang tiêu đề mạch 3 (điểm vào mạch 3)

- **Câu:** 3. **Biết thêm:** việc của mạch: critic học dở làm đánh giá một bước lệch.
- **1 phút:** Mạch này sửa lại khối hệ số, vì critic học dở thì cách đánh giá một bước bị lệch.
- **Mới:** không. **Ý chính:** dòng dẫn.
- **Mặt trang:** "3." · "Trộn đánh giá một bước và cả lượt" · `p.strand-lead` "Critic học dở thì đánh giá một bước bị lệch, còn lợi tức cả lượt thì dao động." (17 âm tiết).
- **Hình:** sơ đồ neo thu nhỏ `so-do-neo-m3-vao.svg`: ④ tô tím, nhãn "$\delta_t$ ?".
- **Ghi chú diễn giả:** "Mạch trước có hai cách lập hệ số: lợi tức cả lượt trừ giá trị, không lệch nhưng ồn; và $\delta_t$ một bước, ít ồn và đúng khi critic đúng. Critic thật luôn sai một chút. Mạch này đặt hai cách cạnh nhau trên cùng một critic sai, rồi trộn chúng bằng một tham số. Đầu ra là $\widehat A_t$ và công thức tính lùi mà PPO dùng."
- **Nguồn:** ghi chú §2.4 đoạn cuối, §3 đoạn mở.

#### `L10-3-01` · Một bước thì lệch, cả lượt thì dao động

- **Câu:** 3. **Biết thêm:** trên cùng một critic sai, hai cách cũ hỏng theo hai kiểu khác nhau.
- **1 phút:** Lợi thế đúng là $0{,}4$; cột một bước cho $-0{,}5$ ở cả hai lượt (đều mà sai dấu), cột cả lượt cho $1{,}3$ và $-1{,}4$ (trung bình đúng mà cách nhau $2{,}7$).
- **Mới:** không (dùng $\delta_t$ và $G_t-\hat v$ đã có). **Ý chính:** tiêu đề.
- **Mặt trang** (≈ 30 âm tiết ngoài bảng):
  - Dòng dữ kiện: "Critic $\hat v=(1{,}4;\,1)$, giá trị thật $(1{,}4;\,2)$. Hai lượt cùng chọn 1 ở $s_A$. Lợi thế đúng: $A_\pi(s_A,1)=0{,}4$."
  - Bảng:

    | Lượt | Xác suất | Một bước $\delta_0$ | Cả lượt $G_0-\hat v(s_A)$ |
    |---|---|---|---|
    | (i) $s_B$ chọn 1, thưởng 3 | $\tfrac23$ | $0+0{,}9\cdot1-1{,}4=-0{,}5$ | $0{,}9\cdot3-1{,}4=1{,}3$ |
    | (ii) $s_B$ chọn 2, thưởng 0 | $\tfrac13$ | $-0{,}5$ | $0-1{,}4=-1{,}4$ |
    | trung bình | | $-0{,}5$ | $\tfrac23\cdot1{,}3-\tfrac13\cdot1{,}4=0{,}4$ |
  - Cột "một bước" viền cam nét đứt, nhãn "lệch: sai dấu"; cột "cả lượt" nền sọc, nhãn "dao động: cách nhau $2{,}7$".
  - Hộp "Câu hỏi: Có cách nào ít lệch hơn một bước mà ít dao động hơn cả lượt không?"
- **Hình:** chuỗi thu nhỏ (khoảng 30%), ô $s_B$ ghi hai số "$\hat v=1$" (cam, nét đứt) và "$v_\pi=2$" (xanh); bảng là bằng chứng chính. Tệp `chuoi-critic-sai.svg`.
- **Dựng dần:** (0) dữ kiện, hình, cột "một bước"; (1) cột "cả lượt"; (2) hàng trung bình, hai nhãn, hộp câu hỏi.
- **Ghi chú diễn giả:** "Critic đánh giá thấp $s_B$ một đơn vị, nên mục tiêu một bước thấp $0{,}9$, và hành động tốt bị coi là kém. Theo ghi chú, độ lệch là $\gamma e(s_B)-e(s_A)=-0{,}9$. Gradient theo $\theta_A$ dùng $\delta$ khi đó trung bình $-0{,}025$, ngược dấu $0{,}2$. Cột cả lượt không phụ thuộc $\hat v(s_B)$ nên không lệch, nhưng mang cả phần ngẫu nhiên ở $s_B$."
- **Nguồn:** đoạn mở §3; Ví dụ 10.8 (hai lượt, bảng); Ví dụ 10.7 "Diễn giải" (độ lệch $-0{,}9$); Mệnh đề 10.8(b) (câu lời thường).
- **Bố cục:**

```
┌──────────────────────────────────────────────────────────────┐
│ Một bước thì lệch, cả lượt thì dao động                      │
├─────────────────┬────────────────────────────────────────────┤
│ [s_A 1,4]→[s_B  │ Critic (1,4;1), thật (1,4;2) … đúng 0,4       │
│  v̂=1 cam        │ Lượt │ xs │┊một bước δ₀┊│▒cả lượt▒         │
│  v_π=2 xanh]    │ (i)  │ ⅔  │┊0+0,9·1−1,4=−0,5┊│▒0,9·3−1,4=1,3▒│
│                 │ (ii) │ ⅓  │┊−0,5┊        │▒0−1,4=−1,4▒     │
│                 │ tb   │    │┊−0,5┊        │▒0,4▒            │
│                 │       lệch: sai dấu     dao động: cách 2,7  │
├─────────────────┴────────────────────────────────────────────┤
│ Câu hỏi: Có cách nào ít lệch hơn … ?                          │
└──────────────────────────────────────────────────────────────┘
```

#### `L10-3-02` · Ước lượng lợi thế tổng quát

- **Câu:** 3. **Biết thêm:** GAE cộng các sai số TD phía sau với trọng số $(\gamma\lambda)^k$; $\lambda=0$ là một bước, $\lambda=1$ là cả lượt.
- **1 phút:** Trên dòng thời gian của lượt (i), $\delta_0=-0{,}5$ và $\delta_1=2$; GAE lấy $\delta_0$ cộng $\gamma\lambda$ lần $\delta_1$, nên $\lambda$ trượt từ một bước ($-0{,}5$) tới cả lượt ($1{,}3$).
- **Mới:** $\lambda$ và ước lượng $\widehat A_t$ (GAE).
- **Ý chính:** công thức có nhãn và hai nhãn đầu mút "$\lambda=0$: một bước", "$\lambda=1$: cả lượt".
- **Mặt trang** (≈ 30 âm tiết):
  - "Ước lượng lợi thế tổng quát (generalized advantage estimation, GAE) cộng các sai số TD phía sau với trọng số giảm dần:"
    $$\widehat A_t=\underbrace{\delta_t}_{\text{một bước}}+\gamma\lambda\,\delta_{t+1}+(\gamma\lambda)^2\,\delta_{t+2}+\cdots$$
  - Ba ô dưới công thức, mỗi ô một giá trị của $\lambda$ trên lượt (i): "$\lambda=0$: $-0{,}5$ (một bước)" · "$\lambda=0{,}5$: $-0{,}5+0{,}45\cdot2=0{,}4$" · "$\lambda=1$: $-0{,}5+0{,}9\cdot2=1{,}3$ (cả lượt)".
- **Hình:** dòng thời gian của lượt (i): $t=0$ ô $s_A$ → $t=1$ ô $s_B$ → ô kết thúc; trên mũi tên thứ nhất "$\delta_0=0+0{,}9\cdot1-1{,}4=-0{,}5$", trên mũi tên thứ hai "$\delta_1=3-1=2$"; dưới mỗi mũi tên một ô trọng số "$1$", "$\gamma\lambda$". Trải ngang trên công thức, khoảng 40% thân trang. Tệp `gae-dong-thoi-gian.svg`.
- **Dựng dần:** (0) hình và câu định nghĩa; (1) công thức; (2) ba ô $\lambda$, lần lượt từ trái sang phải.
- **Ghi chú diễn giả:** "Hệ số cả lượt bằng tổng các $\delta$ có chiết khấu khi critic giữ cố định; GAE chỉ thêm $\lambda^k$ để giảm dần phần đuôi. $\lambda$ nhỏ dựa nhiều vào critic, $\lambda$ gần $1$ dựa nhiều vào phần thưởng thật. Ghi chú viết dạng tương đương bằng lợi tức $n$ bước."
- **Nguồn:** Định nghĩa 10.13, Mệnh đề 10.14(a), (b) (câu lời thường); Ví dụ 10.8 (dòng kiểm tra lại); Bổ đề 10.12 (ở lại ghi chú).
- **Bố cục:**

```
┌──────────────────────────────────────────────────────────────┐
│ Ước lượng lợi thế tổng quát                                  │
├──────────────────────────────────────────────────────────────┤
│  t=0 [s_A] ──δ₀=0+0,9·1−1,4=−0,5──▶ t=1 [s_B] ──δ₁=3−1=2──▶ ■ │
│              trọng số 1                   trọng số γλ          │
├──────────────────────────────────────────────────────────────┤
│ GAE cộng các sai số TD phía sau … (0)                         │
│   Â_t = δ_t + γλ δ_{t+1} + (γλ)² δ_{t+2} + …   (1)            │
│ [λ=0: −0,5] [λ=0,5: −0,5+0,45·2=0,4] [λ=1: −0,5+0,9·2=1,3] (2)│
└──────────────────────────────────────────────────────────────┘
```

#### `L10-3-03` · Tính lùi từ cuối lượt

- **Câu:** 3. **Biết thêm:** mọi $\widehat A_t$ của một lượt tính được bằng một lượt quét lùi.
- **1 phút:** Bắt đầu từ bước cuối, $\widehat A_1=\delta_1=2$, rồi $\widehat A_0=-0{,}5+0{,}45\cdot2=0{,}4$: mỗi bước chỉ cần $\delta$ của nó và $\widehat A$ của bước sau.
- **Mới:** công thức truy hồi.
- **Ý chính:** công thức truy hồi có nhãn.
- **Mặt trang** (≈ 20 âm tiết):
  - $$\widehat A_t=\underbrace{\delta_t}_{\text{bước này}}+\gamma\lambda\,\underbrace{\widehat A_{t+1}}_{\text{đã tính}},\qquad\widehat A=0\text{ sau bước kết thúc}.$$
  - "Trong cài đặt, mỗi đoạn thu được quét lùi một lần."
- **Hình:** dòng thời gian của `L10-3-02`, chỉ với số của lượt (i), thêm hai mũi tên cong quay ngược từ phải sang trái: "$\widehat A_1=\delta_1=2$", rồi "$\widehat A_0=-0{,}5+0{,}45\cdot2=0{,}4$". Khoảng 45%. Tệp `gae-tinh-lui.svg`.
- **Dựng dần:** (0) công thức; (1) mũi tên $\widehat A_1$; (2) mũi tên $\widehat A_0$; (3) dòng cài đặt.
- **Ghi chú diễn giả:** "Đây là Mệnh đề 10.14(c). Truy hồi cho phép tính mọi hệ số với chi phí tỉ lệ độ dài đoạn. Thuật toán PPO ở mạch 5 thu dữ liệu thành các đoạn $h$ bước trên nhiều môi trường; ở biên một đoạn, lượt chưa kết thúc và critic cho giá trị của trạng thái cuối, như câu hỏi ở trang sau. Thuật toán đầy đủ với hai loại cờ ở ghi chú."
- **Nguồn:** Mệnh đề 10.14(c); Thuật toán 10.16 (ở lại ghi chú, câu chuyện mục 5).
- **Bố cục:**

```
┌──────────────────────────────────────────────────────────────┐
│ Tính lùi từ cuối lượt                                        │
├──────────────────────────────────────────────────────────────┤
│ Â_t = δ_t + γλ Â_{t+1},  Â = 0 sau bước kết thúc       (0)   │
│        └bước này┘  └đã tính┘                                  │
│  t=0 [s_A] ──δ₀=−0,5──▶ t=1 [s_B] ──δ₁=2──▶ ■                 │
│        ◀────────── Â₀=−0,5+0,45·2=0,4 (2) ◀── Â₁=2 (1)         │
├──────────────────────────────────────────────────────────────┤
│ Trong cài đặt, mỗi đoạn thu được quét lùi một lần.     (3)   │
└──────────────────────────────────────────────────────────────┘
```

#### `L10-3-04` · Câu hỏi nhanh: lượt bị cắt vì hết giờ

- **Câu:** 3. **Biết thêm:** cắt ngắn không phải kết thúc: trạng thái cuối còn tương lai, nên giữ phần $\gamma\hat v$.
- **1 phút:** Lượt dừng ở $s_B$ vì hết giờ; $s_B$ vẫn còn tương lai, nên dùng $0{,}9\,\hat v(s_B)$; ghi nhầm là kết thúc thì hệ số lệch thêm, xuống $-1{,}4$.
- **Mới:** không (cờ kết thúc và cờ cắt ngắn đã có ở Bài 08). **Ý chính:** hộp "Lời giải:".
- **Mặt trang** (≈ 60 âm tiết):
  - "Nhắc lại (Bài 08): kết thúc thì tương lai bằng $0$. Cắt vì giới hạn thời gian thì tương lai còn, chỉ không được thu."
  - Hộp "Câu hỏi: Lượt bị cắt vì hết giờ ngay khi vừa tới $s_B$. Hệ số của $s_A$ dùng $0{,}9\,\hat v(s_B)$ hay $0$?"
  - Hộp "Lời giải: Dùng $0{,}9\,\hat v(s_B)$, vì $s_B$ còn tương lai: $\delta_0=0+0{,}9\cdot1-1{,}4=-0{,}5$. Số này còn lệch vì critic sai. Ghi nhầm là kết thúc cho $0-1{,}4=-1{,}4$, lệch thêm vì bỏ cả tương lai."
- **Hình:** dòng thời gian của `L10-3-02` dừng ở $s_B$, cờ "hết giờ" cắm trên ô $s_B$; ô kết thúc mờ, nét đứt. Khoảng 40%. Tệp `gae-cat-ngan.svg`.
- **Dựng dần:** (0) nhắc lại, hình, câu hỏi; (1) lời giải.
- **Ghi chú diễn giả:** "Lỗi này hay gặp trong cài đặt: môi trường báo hết giờ bằng cùng một cờ với kết thúc. Khi đó critic học rằng các trạng thái gần giới hạn thời gian không có tương lai, và actor bị phạt ở các bước đó dù chúng không khác các bước khác."
- **Nguồn:** đoạn sau Ví dụ 10.10 (trường hợp chuỗi, câu chuyện quyết định 3); Nhận xét 10.17 ý 2; Tình huống 10.2.
- **Bố cục:**

```
┌──────────────────────────────────────────────────────────────┐
│ Câu hỏi nhanh: lượt bị cắt vì hết giờ                        │
├──────────────────────────────────────────────────────────────┤
│ Nhắc lại (Bài 08): kết thúc … Cắt vì giới hạn thời gian …    │
│  t=0 [s_A] ──1, thưởng 0──▶ t=1 [s_B ⚑hết giờ] ┄┄▶ ┊■┊ (mờ)    │
├──────────────────────────────────────────────────────────────┤
│ Câu hỏi: … dùng 0,9 v̂(s_B) hay 0?                              │
│ Lời giải: Dùng 0,9 v̂(s_B) … −0,5 … Ghi nhầm … −1,4 …   (1)   │
└──────────────────────────────────────────────────────────────┘
```

#### `L10-3-05` · $\lambda$ đổi độ lệch lấy dao động

- **Câu:** 3 (trạm dừng cuối mạch 3). **Biết thêm:** trên cả hai lượt, $\lambda=0{,}5$ có độ lệch và dao động nằm giữa hai đầu; khi nào GAE không làm lệch gradient; điều mạch sau sửa.
- **1 phút:** Thêm cột $\lambda=0{,}5$: hai lượt cho $0{,}4$ và $-0{,}95$, trung bình $-0{,}05$; lệch ít hơn một bước, dao động ít hơn cả lượt; khối hệ số của vòng giờ là $\widehat A_t$.
- **Mới:** không (gom ý). **Ý chính:** tiêu đề; hộp "Với $\lambda=1$ trên lượt đầy đủ, hoặc khi critic đúng, GAE không làm lệch gradient."
- **Mặt trang** (≈ 35 âm tiết ngoài bảng):
  - Bảng của `L10-3-01`, chèn cột giữa "$\lambda=0{,}5$" chỉ ghi kết quả (phép tính đã có ở `L10-3-02`): (i) $0{,}4$; (ii) $-0{,}95$. Hàng "trung bình": $-0{,}5$; $-0{,}05$; $0{,}4$. Hàng "khoảng cách hai lượt": $0$; $1{,}35$; $2{,}7$. Các ô của hai cột cũ cũng chỉ ghi kết quả.
  - Hộp như trên.
  - Dòng: "Còn thiếu: mỗi lượt vẫn chỉ dùng cho một bước cập nhật nhỏ."
- **Hình:** sơ đồ neo thu nhỏ `so-do-neo-m3-ra.svg` ở dải dưới, cạnh dòng "Còn thiếu" (cao khoảng 140 px CSS): ④ ghi "$\widehat A_t$, trộn bằng $\lambda$". Bảng là bằng chứng chính.
- **Dựng dần:** (0) bảng của `L10-3-01` (chỉ kết quả); (1) cột giữa; (2) hai hàng cuối; (3) hộp; (4) sơ đồ neo và dòng "Còn thiếu".
- **Ghi chú diễn giả:** "Lượt (i) cho đúng $0{,}4$ chỉ do trùng hợp; trung bình trên hai lượt là $-0{,}05$, vẫn lệch. Tổng quát, độ lệch là $-0{,}9(1-\lambda)$ và khoảng cách là $2{,}7\lambda$. Bảo đảm của hộp là Mệnh đề 10.15; ngoài hai trường hợp đó, gradient có thể lệch: với $\lambda=0{,}5$, tọa độ $\theta_A$ trung bình là $0{,}0875$ thay cho $0{,}2$. Thực hành thường chọn $\lambda=0{,}95$."
- **Nguồn:** Ví dụ 10.8 (bảng, "Diễn giải"), Ví dụ 10.9; Mệnh đề 10.15 (câu lời thường); $\lambda=0{,}95$ theo bảng siêu tham số của §6.4.
- **Bố cục:**

```
┌──────────────────────────────────────────────────────────────┐
│ λ đổi độ lệch lấy dao động                                   │
├──────────────────────────────────────────────────────────────┤
│ Lượt      │ xs │┊một bước┊│ λ=0,5 │▒cả lượt▒│                  │
│ (i)       │ ⅔  │┊ −0,5   ┊│  0,4  │▒ 1,3   ▒│                  │
│ (ii)      │ ⅓  │┊ −0,5   ┊│ −0,95 │▒ −1,4  ▒│                  │
│ trung bình│    │┊ −0,5   ┊│ −0,05 │▒ 0,4   ▒│                  │
│ khoảng cách│   │┊ 0      ┊│ 1,35  │▒ 2,7   ▒│                  │
│ [hộp] Với λ=1 trên lượt đầy đủ, hoặc khi critic đúng, …      │
├────────────────────────────────┬─────────────────────────────┤
│ [sơ đồ neo nhỏ: ④ Â_t, trộn λ] │ Còn thiếu: mỗi lượt vẫn chỉ … │
└────────────────────────────────┴─────────────────────────────┘
```

### Mạch 4. Đánh giá chính sách mới bằng dữ liệu cũ (`id="mach-4"`, 10 trang thật, 9 trang đếm, 22 phút)

Ví dụ chạy: chuỗi, chính sách cũ $\pi=(\tfrac12;\tfrac23)$ với $J=1{,}4$, lợi thế cũ $A_\pi(s_A,\cdot)=(0{,}4;-0{,}4)$, $A_\pi(s_B,\cdot)=(1;-2)$; chính sách mới dọc đường thẳng tới $(1;\,0{,}5)$. `L10-4-02` và `L10-4-03` là chuỗi trang cùng bố cục (tính một trang). Khuôn bảng: hàng là trạng thái, cột theo thứ tự tính.

#### `L10-4-00` · Trang tiêu đề mạch 4 (điểm vào mạch 4)

- **Câu:** 4. **Biết thêm:** việc của mạch: đánh giá một chính sách trước khi chạy nó.
- **1 phút:** Mạch này sửa khối cập nhật: muốn đi bước lớn thì phải đoán được chính sách mới tốt hay xấu từ lượt cũ.
- **Mới:** không. **Ý chính:** dòng dẫn.
- **Mặt trang:** "4." · "Đánh giá chính sách mới bằng dữ liệu cũ" · `p.strand-lead` "Muốn đi bước lớn, phải đánh giá chính sách mới trước khi chạy nó." (14 âm tiết).
- **Hình:** `so-do-neo-m4-vao.svg`: ⑤ tô tím, nhãn "một bước gradient ?".
- **Ghi chú diễn giả:** "Hai mạch trước cho một hệ số ít ồn, nhưng mỗi lô dữ liệu vẫn chỉ cho một bước nhỏ, vì hành lang đã cho thấy bước dài có thể làm $J$ giảm. Mạch này tìm một công thức đoán $J$ của chính sách mới từ dữ liệu cũ, xem nó sai khi nào, và dẫn tới miền tin cậy cùng TRPO."
- **Nguồn:** ghi chú §3.3 đoạn cuối, §4 đoạn mở.

#### `L10-4-01` · Bước lớn đổi cả nơi chính sách tới

- **Câu:** 4. **Biết thêm:** dữ liệu cũ cho biết lợi thế cũ và nơi chính sách cũ tới, không cho biết nơi chính sách mới tới; chính sách mới có thể dồn vào nơi nó kém.
- **1 phút:** Chính sách mới $(1;\,0{,}5)$ tới $s_B$ ở mọi lượt, gấp đôi chính sách cũ, mà ở $s_B$ nó chọn hành động tốt ít hơn ($0{,}5<\tfrac23$); lượt cũ không thấy điều đó.
- **Mới:** ký hiệu chính sách mới $\pi'$ với $p'_A$, $p'_B$.
- **Ý chính:** câu trên mặt trang "Chính sách mới tới $s_B$ gấp đôi, và ở $s_B$ nó chọn hành động tốt ít hơn chính sách cũ ($0{,}5<\tfrac23$)." (TB3, TB8); hộp "Câu hỏi:".
- **Mặt trang** (≈ 50 âm tiết):
  - "Lượt của chính sách cũ $(\tfrac12;\,\tfrac23)$ tới $s_B$ ở một nửa số lần. Chính sách mới $\pi'$ với $p'_A=1$, $p'_B=0{,}5$ tới $s_B$ ở mọi lượt."
  - "Chính sách mới tới $s_B$ gấp đôi, và ở $s_B$ nó chọn hành động tốt ít hơn chính sách cũ ($0{,}5<\tfrac23$)."
  - Hộp "Câu hỏi: Đoán $J$ của chính sách mới từ lượt của chính sách cũ thế nào, và tin được đến đâu?"
- **Hình:** trái, bản thu nhỏ đồ thị hành lang `hanh-lang-J-hai-buoc.svg` chỉ giữ mũi tên đỏ, nhãn "bước dài qua đỉnh" (25%); phải, chuỗi thu nhỏ và hai thanh ngang "tỉ lệ lượt tới $s_B$": "chính sách cũ $0{,}5$" (xám), "chính sách mới $1$" (tím), cạnh thanh mới nhãn đỏ "ở đây chọn kém hơn", khoảng 40%. Tệp `chuoi-ti-le-toi-sB.svg`.
- **Dựng dần:** (0) hình hành lang thu nhỏ; (1) chuỗi, hai thanh và câu thứ nhất; (2) câu thứ hai và nhãn đỏ; (3) hộp câu hỏi.
- **Ghi chú diễn giả:** "Ở hành lang, ta vẽ được $J(p)$; trên bài toán thật thì không. Dữ liệu cũ cho lợi thế cũ ở những trạng thái chính sách cũ hay tới. Chính sách mới có thể dồn vào trạng thái mà ở đó nó kém, như $s_B$ ở đây."
- **Nguồn:** §4 đoạn mở và hình `policy-update-feedback.svg`; Ví dụ 10.11, "Hai bước trên một đường thẳng" và đoạn sau ("gấp đôi chính sách cũ").
- **Bố cục:**

```
┌──────────────────────────────────────────────────────────────┐
│ Bước lớn đổi cả nơi chính sách tới                           │
├──────────────────┬───────────────────────────────────────────┤
│ [J(p) nhỏ,       │  [s_A]──1──▶[s_B]   tỉ lệ lượt tới s_B:     │
│  mũi tên đỏ      │              cũ  ███████░░░░░░░ 0,5         │
│  qua đỉnh]       │              mới ██████████████ 1 ← đỏ: ở đây│
│                  │                                 chọn kém hơn│
├──────────────────┴───────────────────────────────────────────┤
│ Lượt của chính sách cũ … ở mọi lượt.                          │
│ Chính sách mới tới s_B gấp đôi, và ở s_B nó chọn …            │
│ Câu hỏi: Đoán J của chính sách mới … tin được đến đâu?        │
└──────────────────────────────────────────────────────────────┘
```

#### `L10-4-02` · Hiệu $J$ bằng lợi thế cũ cộng theo nơi chính sách mới tới

- **Câu:** 4. **Biết thêm:** công thức chính xác cho hiệu $J$: lợi thế cũ, chọn theo $\pi'$, cộng theo số lần $\pi'$ tới mỗi trạng thái.
- **1 phút:** Tại $s_A$, $\pi'$ được lợi $0{,}4$; tại $s_B$ nó thiệt $0{,}5$ và tới đó $0{,}9$ lần (có chiết khấu); tổng $0{,}4-0{,}45=-0{,}05$, đúng bằng $1{,}35-1{,}4$.
- **Mới:** lợi thế trung bình $A_\pi(s,\pi')=\sum_a\pi'(a\mid s)A_\pi(s,a)$ (số lần tới viết bằng lời, không đặt ký hiệu).
- **Ý chính:** tiêu đề; dòng kiểm "$J(\pi')=2{,}7\cdot0{,}5=1{,}35$, nên hiệu thật là $-0{,}05$."
- **Mặt trang** (≈ 40 âm tiết ngoài bảng):
  - $$J(\pi')-J(\pi)=\sum_s\ \bigl(\text{số lần }\pi'\text{ tới }s\text{, nhân }\gamma^t\bigr)\times\underbrace{A_\pi(s,\pi')}_{\text{lợi thế cũ, chọn theo }\pi'}$$
  - Bảng:

    | Trạng thái | $A_\pi(s,\pi')$ | số lần $\pi'$ tới | tích |
    |---|---|---|---|
    | $s_A$ | $1\cdot0{,}4+0\cdot(-0{,}4)=0{,}4$ | $1$ | $0{,}4$ |
    | $s_B$ | $0{,}5\cdot1+0{,}5\cdot(-2)=-0{,}5$ | $0{,}9\cdot1=0{,}9$ | $-0{,}45$ |
    | | | **tổng** | **$-0{,}05$** |
  - "Nhắc lại: lợi thế cũ $(0{,}4;\,-0{,}4)$ ở $s_A$, $(1;\,-2)$ ở $s_B$; $J=2{,}7\,p_Ap_B+1-p_A$."
  - Dòng kiểm như trên.
- **Hình:** không hình riêng; bảng là bằng chứng (phép tính về mỗi trạng thái nằm trong hàng của nó, TB10). Không chuỗi thu nhỏ (giữ chỗ cho `L10-4-03`).
- **Dựng dần:** (0) công thức và dòng nhắc lại; (1) hàng $s_A$; (2) hàng $s_B$; (3) tổng và dòng kiểm.
- **Ghi chú diễn giả:** "Đây là bổ đề hiệu hiệu năng, Bổ đề 10.19, viết bằng số lần thăm không chuẩn hóa ($\eta$ trong bảng ký hiệu của ghi chú); ghi chú dùng phân bố chiếm dụng $\nu$ và thừa số $1/(1-\gamma)$, cùng một đại lượng. Chính sách mới tới $s_B$ với xác suất $p'_A=1$ ở bước $1$, nhân $\gamma=0{,}9$. Công thức chính xác nhưng cần nơi $\pi'$ tới, tức phải chạy $\pi'$."
- **Nguồn:** Bổ đề 10.19 (câu lời thường); Ví dụ 10.11 (số của bước $(1;0{,}5)$, dòng kiểm tra lại $J=1{,}35$; công thức $J=2{,}7p_Ap_B+1-p_A$); bảng ký hiệu ($\eta$).
- **Bố cục:**

```
┌──────────────────────────────────────────────────────────────┐
│ Hiệu J bằng lợi thế cũ cộng theo nơi chính sách mới tới      │
├──────────────────────────────────────────────────────────────┤
│ J(π')−J(π) = Σ_s (số lần π' tới s, nhân γ^t) × A_π(s,π')      │
│ Nhắc lại: lợi thế cũ (0,4;−0,4), (1;−2); J = 2,7p_Ap_B+1−p_A   │
│ ┌──────┬──────────────────────┬─────────────┬────────┐        │
│ │ s_A  │ 1·0,4+0·(−0,4)=0,4   │ 1           │ 0,4    │        │
│ │ s_B  │ 0,5·1+0,5·(−2)=−0,5  │ 0,9·1=0,9   │ −0,45  │        │
│ │      │                      │ tổng        │[−0,05] │        │
│ └──────┴──────────────────────┴─────────────┴────────┘        │
│ J(π') = 2,7·0,5 = 1,35, nên hiệu thật là −0,05.               │
└──────────────────────────────────────────────────────────────┘
```

#### `L10-4-03` · Hàm thay thế dùng nơi chính sách cũ tới

- **Câu:** 4. **Biết thêm:** thay số lần tới của $\pi'$ bằng của $\pi$ được một đại lượng tính được từ lượt cũ, và trên bước này nó đoán sai chiều.
- **1 phút:** Thay cột "số lần $\pi'$ tới" bằng "số lần $\pi$ tới" ($0{,}9\to0{,}45$): tổng thành $+0{,}175$, trong khi $J$ thật giảm $0{,}05$.
- **Mới:** hàm thay thế $\mathcal L_\pi(\pi')$.
- **Ý chính:** hộp "Hàm thay thế báo tăng $0{,}175$, còn $J$ thật giảm $0{,}05$."
- **Mặt trang** (≈ 40 âm tiết ngoài bảng):
  - "Hàm thay thế $\mathcal L$ giữ số lần tới của chính sách cũ, nên tính được từ lượt cũ:"
    $$\mathcal L_\pi(\pi')-J(\pi)=\sum_s\ \bigl(\text{số lần }{\color{purple}\pi}\text{ tới }s\bigr)\times A_\pi(s,\pi').$$
  - Bảng của `L10-4-02` bỏ cột "tích" cũ, giữ năm cột: trạng thái; $A_\pi(s,\pi')$; "số lần $\pi'$ tới" ($1$; $0{,}9$); "số lần $\pi$ tới" ($1$; $0{,}9\cdot0{,}5=0{,}45$, tím); "tích với số lần $\pi$" ($0{,}4$; $-0{,}225$); hàng tổng: thật $-0{,}05$ (giữ ở hàng tổng của cột cũ) và hàm thay thế **$+0{,}175$** (cam).
  - Hộp như trên.
- **Hình:** như `L10-4-02` (không hình riêng, không chuỗi thu nhỏ).
- **Dựng dần:** (0) bảng của trang trước và câu; (1) công thức; (2) hai cột mới; (3) hộp.
- **Ghi chú diễn giả:** "Trên bài toán thật, phần $\sum_a\pi'(a\mid s)A_\pi(s,a)$ tính từ hành động của chính sách cũ bằng tỉ số $\pi'/\pi$, như lấy mẫu quan trọng ở Bài 06; ta dùng lại tỉ số này ở mạch 5. Hàm thay thế bỏ qua đúng một điều: chính sách mới tới $s_B$ gấp đôi, ở nơi nó kém hơn."
- **Nguồn:** Định nghĩa 10.21; Ví dụ 10.11 (tổng dùng xác suất cũ $0{,}175$).
- **Bố cục:**

```
┌──────────────────────────────────────────────────────────────┐
│ Hàm thay thế dùng nơi chính sách cũ tới                      │
├──────────────────────────────────────────────────────────────┤
│ Hàm thay thế L giữ số lần tới của chính sách cũ, …           │
│ L_π(π')−J(π) = Σ_s (số lần π tới s) × A_π(s,π')         (1)  │
│ ┌────┬───────────┬──────────┬───────────┬─────────────┐      │
│ │ s  │ A_π(s,π') │ π' tới   │ π tới (tím)│ tích với π  │ (2)  │
│ │ s_A│ 0,4       │ 1        │ 1          │ 0,4         │      │
│ │ s_B│ −0,5      │ 0,9      │ 0,45       │ −0,225      │      │
│ │    │ thật: −0,05          │ thay thế:  │ [+0,175]cam │      │
│ └────┴───────────┴──────────┴───────────┴─────────────┘      │
│ [hộp] Hàm thay thế báo tăng 0,175, còn J thật giảm 0,05. (3)  │
└──────────────────────────────────────────────────────────────┘
```

#### `L10-4-04` · Hàm thay thế tiếp xúc $J$ tại chính sách cũ

- **Câu:** 4. **Biết thêm:** dọc một đường đổi chính sách, hàm thay thế là tiếp tuyến của $J$: đúng gần chính sách cũ, sai xa dần.
- **1 phút:** Đường thẳng cam và parabol xanh chung điểm, chung độ dốc tại chính sách cũ; tại $(0{,}7;\,0{,}6)$ cả hai còn dương, tại $(1;\,0{,}5)$ chúng trái dấu.
- **Mới:** không (hình của hai đại lượng đã có). **Ý chính:** tiêu đề; câu "Tại chính sách cũ, hàm thay thế bằng $J$ và có cùng độ dốc."
- **Mặt trang** (≈ 30 âm tiết): "Chính sách đi từ $(\tfrac12;\,\tfrac23)$ tới $(1;\,0{,}5)$ theo tham số $t\in[0;1]$." · câu ý chính.
- **Hình:** đồ thị theo $t\in[0;1]$, trục hoành ghi thêm ba chính sách dưới $t=0$, $0{,}4$, $1$: "$(\tfrac12;\tfrac23)$", "$(0{,}7;0{,}6)$", "$(1;0{,}5)$". Đường cam, nét đứt, "$\Delta\mathcal L=0{,}175\,t$"; parabol xanh, nét liền, "$\Delta J=0{,}175\,t-0{,}225\,t^2$". Điểm $t=0{,}4$: nhãn "đoán $0{,}07$ · thật $0{,}034$"; điểm $t=1$ (vạch đỏ): "đoán $0{,}175$ · thật $-0{,}05$". Trục tung từ $-0{,}06$ tới $0{,}2$, đường $0$ đậm. Khoảng 65% thân trang. Tệp `ham-thay-the-tiep-xuc.svg`; dùng lại ở `L10-4-07`.
- **Dựng dần:** (0) hai đường; (1) điểm $t=0{,}4$; (2) điểm $t=1$; (3) câu ý chính.
- **Ghi chú diễn giả:** "Hỏi lớp trước bước (2): ở $t=1$, hàm thay thế nói tăng $0{,}175$; thật thì sao? $J$ lớn nhất khoảng $0{,}034$ ở $t\approx0{,}39$ và về $0$ ở $t=\tfrac79$. Mệnh đề 10.22 nói hai hàm khớp đến bậc một tại chính sách cũ; nó không nói gì về bước hữu hạn."
- **Nguồn:** Ví dụ 10.11, "Hai bước trên một đường thẳng"; Mệnh đề 10.22 (câu lời thường).
- **Bố cục:**

```
┌──────────────────────────────────────────────────────────────┐
│ Hàm thay thế tiếp xúc J tại chính sách cũ                    │
├──────────────────────────────────────────────────────────────┤
│ 0,2 ┤                                  ╱ cam ΔL=0,175t          │
│     │                     ╱      ●đoán 0,175                  │
│ 0,1 ┤          ╱  ●đoán 0,07                                  │
│     │    ╱ ⌒⌒⌒⌒●thật 0,034⌒⌒╲  xanh ΔJ                         │
│  0 ━┿━━━━━━━━━━━━━━━━━━━━━━━━━━━━╲━━━━━━━━━━━━━━              │
│     │                               ●đỏ thật −0,05            │
│     0          0,4                1   t                      │
│   (½;⅔)     (0,7;0,6)          (1;0,5)                       │
├──────────────────────────────────────────────────────────────┤
│ Tại chính sách cũ, hàm thay thế bằng J và có cùng độ dốc.    │
└──────────────────────────────────────────────────────────────┘
```

#### `L10-4-05` · Bước gần thì hàm thay thế sai ít

- **Câu:** 4 (trạm dừng; câu hỏi nhanh). **Biết thêm:** sai số của hàm thay thế đến từ việc chính sách mới đổi nơi nó tới; giữ chính sách mới gần thì nơi tới đổi ít, và sai số nhỏ.
- **1 phút:** $\Delta J$ bằng hàm thay thế cộng một số hạng tích $2{,}7\,\Delta p_A\Delta p_B$; ở bước $(1;\,0{,}5)$ nó là $-0{,}225$, ở bước gần $(0{,}6;\,0{,}7)$ chỉ còn $0{,}009$.
- **Mới:** $\Delta p_A$, $\Delta p_B$ (mức đổi của hai xác suất).
- **Ý chính:** tiêu đề; câu "Sai số đến từ việc chính sách mới đổi nơi nó tới. Chính sách mới gần thì nơi tới đổi ít."
- **Mặt trang** (≈ 55 âm tiết):
  - "Với $\Delta p_A=p'_A-\tfrac12$, $\Delta p_B=p'_B-\tfrac23$:"
    $$\Delta J=\underbrace{0{,}8\,\Delta p_A+1{,}35\,\Delta p_B}_{\text{hàm thay thế}}+\underbrace{2{,}7\,\Delta p_A\,\Delta p_B}_{\text{sai số}}.$$
  - Dòng nguồn: "Từ bảng: $A_\pi(s_A,\pi')=0{,}8\,\Delta p_A$, $A_\pi(s_B,\pi')=3\,\Delta p_B$, số lần $\pi$ tới $s_B$ là $0{,}45$. Ở bước $(1;\,0{,}5)$: sai số $2{,}7\cdot0{,}5\cdot(-\tfrac16)=-0{,}225$."
  - Câu ý chính.
  - Hộp "Câu hỏi: Bước $(0{,}6;\,0{,}7)$ ở gần chính sách cũ. Hàm thay thế đoán $\Delta J$ bao nhiêu, và sai bao nhiêu?"
  - Hộp "Lời giải: $\Delta\mathcal L=0{,}8\cdot0{,}1+1{,}35\cdot\tfrac1{30}=0{,}125$. Sai số $2{,}7\cdot0{,}1\cdot\tfrac1{30}=0{,}009$, nên $\Delta J=0{,}134$."
  - "Còn thiếu: gần đến mức nào."
- **Hình:** không; lý do: trạm dừng là một công thức (TB5); hình của kết quả vừa ở trang trước.
- **Dựng dần:** (0) công thức và dòng nguồn; (1) câu ý chính; (2) câu hỏi; (3) lời giải; (4) dòng "Còn thiếu".
- **Ghi chú diễn giả:** "Số hạng tích là $\gamma\,\Delta p_A\,A_\pi(s_B,\pi')$: mỗi lượt có thêm $\Delta p_A$ lần tới $s_B$, mỗi lần mang $\gamma A_\pi(s_B,\pi')$. Ở bước gần, cả hai thừa số nhỏ, nên tích rất nhỏ. Kiểm bước $(1;0{,}5)$: $0{,}4-0{,}225-0{,}225=-0{,}05$. Trường hợp riêng bước chỉ đổi $p_B$ ở câu hỏi tự kiểm tra cuối bài."
- **Nguồn:** Ví dụ 10.11, "Mọi chính sách mới trên chuỗi" và "Hai bước trên một đường thẳng"; §8.4 câu 2 (bước $(0{,}6;0{,}7)$: $0{,}125$, $0{,}134$).
- **Bố cục:**

```
┌──────────────────────────────────────────────────────────────┐
│ Bước gần thì hàm thay thế sai ít                             │
├──────────────────────────────────────────────────────────────┤
│ ΔJ = 0,8Δp_A + 1,35Δp_B + 2,7Δp_AΔp_B                         │
│      └──hàm thay thế──┘   └─sai số─┘                           │
│ Từ bảng: … Ở bước (1;0,5): sai số … = −0,225                 │
│ Sai số đến từ … Chính sách mới gần thì nơi tới đổi ít.  (1)   │
├───────────────────────────────┬──────────────────────────────┤
│ Câu hỏi: Bước (0,6;0,7) … (2)  │ Lời giải: ΔL=0,125 … 0,009 (3)│
├───────────────────────────────┴──────────────────────────────┤
│ Còn thiếu: gần đến mức nào.                              (4) │
└──────────────────────────────────────────────────────────────┘
```

#### `L10-4-06` · Sai số của hàm thay thế bị chặn theo khoảng cách hai chính sách

- **Câu:** 4. **Biết thêm:** cận dưới cho $J$ mới: dự đoán của hàm thay thế trừ một phạt theo khoảng cách hai chính sách; cận đó rất bảo thủ.
- **1 phút:** Nếu chính sách mới chỉ khác một chút, $J$ mới không thấp hơn dự đoán quá một phạt; nhưng hệ số của phạt lớn, nên trên chuỗi cận chỉ dương với bước rất nhỏ.
- **Mới:** định lý chặn cải thiện (khối "Giả thiết:/Kết luận:" thứ hai); khoảng cách viết bằng lời.
- **Ý chính:** tiêu đề.
- **Mặt trang** (≈ 50 âm tiết):
  - "Định lý (chặn cải thiện)."
  - "Giả thiết: lợi thế và số lần tới của chính sách cũ được tính chính xác. Hai chính sách chạy trên cùng môi trường, $\gamma<1$."
  - "Kết luận:" $$J(\pi')-J(\pi)\ \ge\ \underbrace{\mathcal L_\pi(\pi')-J(\pi)}_{\text{dự đoán của hàm thay thế}}\ -\ \underbrace{C\times\bigl(\text{khoảng cách trung bình giữa }\pi\text{ và }\pi'\bigr)}_{\text{phạt, hệ số }C\text{ rất lớn}}$$
  - "Ý nghĩa: trên chuỗi, cận dương chỉ khi bước rất nhỏ, chẳng hạn chỉ tăng $p_B$ thêm dưới $0{,}056$."
- **Hình:** không; lý do: phát biểu của điều mà `L10-4-04` đã cho thấy; hình cận dưới trên cùng trục sẽ nằm xa dưới trục ($-0{,}76$ ở $t=0{,}4$) và che hình chính.
- **Dựng dần:** (0) khối; (1) dòng "Ý nghĩa".
- **Ghi chú diễn giả:** "Đây là Định lý 10.26. Khoảng cách là biến phân toàn phần giữa hai phân phối hành động, trung bình theo nơi chính sách cũ tới. Hằng $C=2\gamma\chi/(1-\gamma)^2$, với $\chi$ là lợi thế trung bình lớn nhất; với $\gamma=0{,}9$, thừa số $1/(1-\gamma)^2$ đã là $100$. Ở bước $(0{,}6;0{,}8)$ của ghi chú, $J$ thật tăng $0{,}296$ mà cận dưới là $-0{,}89$. Cận dương với bước chỉ đổi $p_B$ khi $\Delta p<1{,}35/24{,}3\approx0{,}056$."
- **Nguồn:** Định lý 10.26 (Giả thiết, Kết luận, Phạm vi); Định nghĩa 10.23 (chỉ ở ghi chú diễn giả); Ví dụ 10.12; Hệ quả 10.27 (ở lại ghi chú).

#### `L10-4-07` · Miền tin cậy: tối đa hàm thay thế trong vùng KL nhỏ

- **Câu:** 4. **Biết thêm:** bài toán miền tin cậy: tin hàm thay thế chỉ trong một vùng KL quanh chính sách cũ; bước hỏng của ví dụ nằm ngoài mọi vùng như vậy.
- **1 phút:** Trên hình của hàm thay thế và $J$, chỉ giữ đoạn gần chính sách cũ, nơi hai đường còn sát nhau; điểm $(1;\,0{,}5)$ có KL vô hạn ở $s_A$, nên không vùng KL nào chứa nó.
- **Mới:** miền tin cậy với bán kính $\kappa$.
- **Ý chính:** tiêu đề; nhãn trên hình ở điểm $t=1$ "KL ở $s_A$ vô hạn: ngoài mọi miền tin cậy".
- **Mặt trang** (≈ 50 âm tiết):
  - "KL chặn được khoảng cách ở trang trước, và tính được từ lượt cũ."
  - $$\max_\theta\ \mathcal L_{\theta_{\mathrm{old}}}(\theta)\quad\text{với}\quad\underbrace{\text{KL trung bình}(\pi_{\mathrm{old}}\Vert\pi_\theta)}_{\text{theo nơi chính sách cũ tới}}\le\underbrace{\kappa}_{\text{bán kính}}$$
  - "Tối đa cận dưới cho bước gần bằng $0$. Ràng buộc KL cho bước lớn hơn, nhưng chỉ chặn được mức giảm của $J$."
- **Hình:** đồ thị `ham-thay-the-tiep-xuc.svg` (khoảng 45%), thêm dải tím nhạt trên đoạn $t$ gần $0$, nhãn "miền tin cậy"; phần còn lại mờ, nhãn "ngoài miền"; ở điểm $t=1$ nhãn đỏ "KL ở $s_A$ vô hạn: ngoài mọi miền tin cậy". Không ghi giá trị $\kappa$ (ghi chú không có KL dọc đường này; dải chỉ minh họa).
- **Dựng dần:** (0) hình với dải; (1) câu nối và công thức; (2) nhãn ở $t=1$; (3) câu cuối.
- **Ghi chú diễn giả:** "KL đo theo chiều cũ‖mới, trung bình theo trạng thái chính sách cũ tới. Tại $(1;0{,}5)$, chính sách mới không chọn hành động 2 ở $s_A$, nên KL tại đó là vô hạn, trong khi khoảng cách biến phân chỉ là $0{,}5$. Hệ quả 10.29 cho cải thiện đơn điệu khi tối đa cận dưới; Hệ quả 10.31 cho mức giảm tối đa của bước miền tin cậy, cỡ $\sqrt{2\kappa}$."
- **Nguồn:** Định nghĩa 10.30; Hệ quả 10.27 (KL chặn khoảng cách), 10.29, 10.31 (câu lời thường); đoạn sau Định nghĩa 10.23 (KL vô hạn ở $s_A$ tại $(1;0{,}5)$).
- **Bố cục:**

```
┌──────────────────────────────────────────────────────────────┐
│ Miền tin cậy: tối đa hàm thay thế trong vùng KL nhỏ          │
├──────────────────────────────┬───────────────────────────────┤
│ [đồ thị L và J, dải tím      │ KL chặn được khoảng cách …     │
│  "miền tin cậy" ở t nhỏ,      │ max_θ L(θ) với KL tb ≤ κ        │
│  phần còn lại mờ;             │ Tối đa cận dưới … gần bằng 0.  │
│  t=1: "KL ở s_A vô hạn"]      │ Ràng buộc KL … chỉ chặn …      │
└──────────────────────────────┴───────────────────────────────┘
```

#### `L10-4-08` · Gradient tự nhiên dồn bước về $\theta_B$

- **Câu:** 4 ("TRPO giải bằng gradient tự nhiên"). **Biết thêm:** gần chính sách cũ, miền tin cậy là một elip; bước tốt nhất trong elip nghiêng về tham số mà KL ít nhạy, khác gradient thường.
- **1 phút:** Elip KL kéo dài theo $\theta_B$ vì $s_B$ ít được tới; mũi tên của bước tốt nhất nghiêng hẳn về $\theta_B$ so với mũi tên gradient.
- **Mới:** độ cong $F$ của KL và hướng gradient tự nhiên $F^{-1}g$ (một ý: đo bước bằng độ cong của KL).
- **Ý chính:** tiêu đề; hình.
- **Mặt trang** (≈ 40 âm tiết):
  - $$\text{KL trung bình}\approx\tfrac12\,\Delta^\top\underbrace{F}_{\text{độ cong của KL}}\,\Delta,\qquad\text{bước tốt nhất}\ \propto\ \underbrace{F^{-1}g}_{\text{gradient tự nhiên}}$$
  - "Trên chuỗi, $F$ ở mỗi trạng thái là tần suất tới trạng thái đó nhân $p(1-p)$. $s_B$ được tới ít hơn, nên KL ít nhạy với $\theta_B$, và bước tốt nhất nghiêng về $\theta_B$."
- **Hình:** mặt phẳng $(\Delta_A,\Delta_B)$, elip tâm gốc, bán trục theo $\Delta_B$ dài gấp $\sqrt{2{,}5}\approx1{,}6$ lần bán trục theo $\Delta_A$; hai mũi tên từ tâm tới biên elip: "$g$" (xám, hướng $(2;3)$), "$F^{-1}g$" (tím, hướng $(8;30)$). Không ghi số trên trục và trên mũi tên. Khoảng 45%, bên phải. Tệp `elip-gradient-tu-nhien.svg`.
- **Dựng dần:** (0) công thức thứ nhất và elip; (1) mũi tên $g$; (2) công thức thứ hai và mũi tên $F^{-1}g$; (3) câu.
- **Ghi chú diễn giả:** "Số cụ thể, để đọc: $F=\operatorname{diag}(0{,}1\cdot\tfrac14;\ 0{,}045\cdot\tfrac29)=\operatorname{diag}(0{,}025;0{,}01)$, với $0{,}1$, $0{,}045$ là tần suất chiết khấu tới $s_A$, $s_B$; gradient $g=(0{,}2;0{,}3)$ và $F^{-1}g=(8;30)$. Nhầm lẫn hay gặp: đo bước bằng khoảng cách Euclid trên tham số. Cùng bước $+1$ trên logit cho KL $0{,}12$ tại $p=0{,}5$ nhưng chỉ $0{,}0037$ tại $p=0{,}99$ (Ví dụ 10.13). Độ dài bước $\sqrt{2\kappa/(g^\top F^{-1}g)}$ ở ghi chú."
- **Nguồn:** Mệnh đề 10.33, 10.34 (câu lời thường); đoạn cuối §5.2 ($F$, $F^{-1}g$ trên chuỗi); Ví dụ 10.13 (chỉ ở ghi chú diễn giả).
- **Bố cục:**

```
┌──────────────────────────────────────────────────────────────┐
│ Gradient tự nhiên dồn bước về θ_B                            │
├───────────────────────────────┬──────────────────────────────┤
│ KL tb ≈ ½ ΔᵀFΔ   bước ∝ F⁻¹g    │        Δ_B                    │
│        └độ cong┘   └g. tự nhiên┘│     ╭───┼───╮  ↗F⁻¹g (tím)     │
│ Trên chuỗi, F ở mỗi trạng thái │    │    ┼──↗ g (xám)          │
│ là tần suất tới … nhân p(1−p). │     ╰───┼───╯   Δ_A           │
│ s_B được tới ít hơn, nên …     │   (elip dài theo Δ_B)         │
└───────────────────────────────┴──────────────────────────────┘
```

#### `L10-4-09` · TRPO: một bước gần đúng, kiểm lại trên dữ liệu

- **Câu:** 4 (trạm dừng cuối mạch 4). **Biết thêm:** vòng TRPO thật và cái giá của nó; TRPO như cài đặt không còn bảo đảm $J$ tăng.
- **1 phút:** Khối cập nhật của vòng giờ là bốn bước: tính $g$, giải $Fx=g$ chỉ bằng tích $Fv$, bước tới biên elip, rồi thu ngắn tới khi KL và hàm thay thế trên dữ liệu đạt yêu cầu.
- **Mới:** TRPO (tên thuật toán; các bước là ghép của ba trang trước).
- **Ý chính:** hộp "TRPO như cài đặt dùng ước lượng và nghiệm gần đúng, nên không còn bảo đảm $J$ tăng."
- **Mặt trang** (≈ 40 âm tiết ngoài hình):
  - Hộp như trên.
  - "Còn thiếu: mỗi bước cần khoảng mười tích $Fv$ và một lượt tìm kiếm lùi."
- **Hình:** sơ đồ neo `so-do-neo-m4-ra.svg` ở nửa trái (khoảng 45%), ⑤ tô tím với nhãn "tối đa hàm thay thế trong miền tin cậy (TRPO)", mũi tên mới ② → ⑤ "dùng lại dữ liệu cũ". Từ ⑤, một mũi tên sang nửa phải mở vòng trong bốn khung xếp 2×2 (đọc theo chiều kim đồng hồ), nhãn mỗi khung ≤ 6 từ: "$g$ từ lợi thế GAE" → "giải $Fx=g$, chỉ cần $Fv$" → "bước tới biên elip" → "tìm kiếm lùi: kiểm KL, hàm thay thế". Chi tiết "KL mẫu $\le\kappa$ và hàm thay thế mẫu tăng" ở ghi chú diễn giả.
- **Dựng dần:** (0) sơ đồ neo với ⑤ tô; (1)–(4) bốn khung của vòng trong; (5) hộp và dòng "Còn thiếu".
- **Ghi chú diễn giả:** "Tìm kiếm lùi thu ngắn bước tới khi KL trung bình mẫu không vượt $\kappa$ và hàm thay thế mẫu tăng. So với định lý, TRPO thay năm điểm: trung bình trên bộ đệm thay cho kỳ vọng có chiết khấu; lợi thế GAE thay cho lợi thế đúng; hàm thay thế bậc một và KL bậc hai; gradient liên hợp dừng sớm; ràng buộc KL trung bình thay cho phạt khoảng cách. Hai vòng gradient liên hợp tính tay ở ghi chú, Ví dụ 10.16."
- **Nguồn:** Thuật toán 10.36, 10.37 (dạng sơ đồ); Nhận xét 10.38; đoạn cuối §5.2 (chi phí, khoảng mười tích Fisher–vector).
- **Bố cục:**

```
┌──────────────────────────────────────────────────────────────┐
│ TRPO: một bước gần đúng, kiểm lại trên dữ liệu               │
├─────────────────────────────┬────────────────────────────────┤
│ ①→②Thu lượt ◀──────┐         │ ┌──────────────┐ ┌────────────┐ │
│    │ ╲dùng lại       │         │ │g từ lợi thế  │→│giải Fx=g,  │ │
│ ③→④Â_t ╲dữ liệu cũ  │         │ │GAE       (1) │ │chỉ cần Fv(2)│ │
│    ↓     ↘           │  ───▶   │ └──────────────┘ └────────────┘ │
│ ⑤[miền tin cậy, TRPO]┘         │ ┌──────────────┐ ┌────────────┐ │
│   (tím)                      │ │tìm kiếm lùi: │←│bước tới    │ │
│                              │ │kiểm KL, h.t.t│ │biên elip(3)│ │
│                              │ └──────────(4)─┘ └────────────┘ │
├─────────────────────────────┴────────────────────────────────┤
│ [hộp] TRPO như cài đặt … không còn bảo đảm J tăng.       (5)  │
│ Còn thiếu: mỗi bước cần khoảng mười tích Fv …                 │
└──────────────────────────────────────────────────────────────┘
```

### Mạch 5. Giữ chính sách mới gần chính sách cũ (`id="mach-5"`, 9 trang thật, 8 trang đếm, 16 phút)

Ví dụ chạy (sửa theo cổng 2026-11-20): chuỗi hai trạng thái với critic $(1{,}4;1)$ của mạch 3, $\lambda=1$, và một bộ đệm nhỏ có hai lượt, $s_A\xrightarrow1s_B\xrightarrow2$ và $s_A\xrightarrow2$ (`L10-5-01`, `L10-5-05`); $\epsilon=0{,}2$. Để thấy cơ chế cắt, `L10-5-04` và `L10-5-06` xét riêng trạng thái $s_B$ của cùng chuỗi với bộ đệm ba mẫu đúng tần suất (ghi chú gọi là "bài toán một bước": chính sách cũ $(\tfrac23;\tfrac13)$, hành động $1,1,2$, lợi thế $1,1,-2$). Một đồ thị theo $p$ dùng cho `L10-5-04`, `L10-5-06`. `L10-5-02` và `L10-5-03` là chuỗi trang cùng bố cục (tính một trang).

#### `L10-5-00` · Trang tiêu đề mạch 5 (điểm vào mạch 5)

- **Câu:** 5. **Biết thêm:** việc của mạch: giữ bước gần mà không cần bộ máy bậc hai.
- **1 phút:** Mạch này thay cách TRPO giữ chính sách mới ở gần bằng một cách chỉ cần Adam.
- **Mới:** không. **Ý chính:** dòng dẫn.
- **Mặt trang:** "5." · "Giữ chính sách mới gần chính sách cũ" · `p.strand-lead` "Giữ chính sách mới ở gần chính sách cũ mà chỉ dùng Adam." (13 âm tiết).
- **Hình:** `so-do-neo-m5-vao.svg`: ⑤ tô tím, nhãn "miền tin cậy (TRPO) ?".
- **Ghi chú diễn giả:** "TRPO cho một bước lớn nhưng tốn: gradient liên hợp, tìm kiếm lùi, và không hợp với mạng dùng chung tham số giữa chính sách và critic. Hàm thay thế chỉ đáng tin gần chính sách cũ vì hai lý do: nơi chính sách tới đổi (mạch 4), và lợi thế chỉ là ước lượng từ ít lượt (trang sau). Mạch này đưa giới hạn khoảng cách vào chính hàm mục tiêu, để vài lượt Adam trên dữ liệu tự dừng. Đầu ra là vòng PPO, dùng lại ở mạch sau."
- **Nguồn:** đoạn cuối §5.2; đoạn mở §6.

#### `L10-5-01` · Bộ đệm hai lượt đẩy chính sách đi xa và sai hướng

- **Câu:** 5 (hiện tượng mở mạch, sửa theo cổng). **Biết thêm:** lợi thế ước lượng từ ít lượt có thể sai dấu; tối đa hàm thay thế mẫu không ràng buộc khi đó đi tới tận biên và làm $J$ giảm $0{,}4$.
- **1 phút:** Một lượt xui làm hành động tốt ở $s_A$ bị chấm $-1{,}4$; hàm thay thế mẫu đẩy $p_A$ về $0$, và $J$ rơi từ $1{,}4$ xuống $1$; không có gì giữ Adam dừng sớm.
- **Mới:** không (tỉ số lấy mẫu quan trọng nhắc lại từ Bài 06; lợi thế ước lượng từ mạch 3). **Ý chính:** tiêu đề; dòng "$J$ thật tại $(0;\,1)$ là $1$: giảm $0{,}4$."; hộp "Câu hỏi:".
- **Mặt trang** (≈ 60 âm tiết ngoài bảng):
  - Dòng dữ kiện: "Chuỗi, critic $(1{,}4;\,1)$, $\lambda=1$. Bộ đệm có hai lượt: $s_A\xrightarrow1s_B\xrightarrow2$ (lợi tức $0$) và $s_A\xrightarrow2$ (lợi tức $1$)."
  - "Nhắc lại (Bài 06): mẫu của chính sách cũ đánh giá chính sách mới qua tỉ số $\rho=\pi'(a\mid s)/\pi_{\mathrm{old}}(a\mid s)$. Hàm thay thế mẫu là trung bình của $\rho\,\widehat A$."
  - Bảng:

    | Trạng thái | Mẫu: lợi thế ước lượng | Lợi thế đúng | Hàm thay thế mẫu | Tối đa tại |
    |---|---|---|---|---|
    | $s_A$ | hành động 1: $0-1{,}4=-1{,}4$ (đỏ); hành động 2: $1-1{,}4=-0{,}4$ | $+0{,}4$; $-0{,}4$ | $\tfrac12\bigl[2p'_A(-1{,}4)+2(1-p'_A)(-0{,}4)\bigr]=-0{,}4-p'_A$ | $p'_A=0$ |
    | $s_B$ | hành động 2: $0-1=-1$ | $-2$ | $3(1-p'_B)\cdot(-1)$ | $p'_B=1$ |
  - "$J$ thật tại $(0;\,1)$ là $1$: giảm $0{,}4$."
  - Hộp "Câu hỏi: Sửa hàm mục tiêu thế nào để Adam không đẩy chính sách đi quá xa trên một bộ đệm nhỏ?"
- **Hình:** chuỗi thu nhỏ (khoảng 25%, góc trái trên) với hai lượt của bộ đệm vẽ bằng hai đường màu: $s_A\to s_B\to$ "thưởng $0$" và $s_A\to$ "thưởng $1$"; không hình riêng cho kết quả (bảng là bằng chứng). Tệp `chuoi-bo-dem-hai-luot.svg`.
- **Dựng dần:** (0) hình, dữ kiện, nhắc lại; (1) hai cột đầu của bảng; (2) cột lợi thế đúng (ô $-1{,}4$ so với $+0{,}4$ tô đỏ); (3) hai cột cuối và dòng $J$; (4) hộp câu hỏi.
- **Ghi chú diễn giả:** "Bộ đệm này gặp một lần trong sáu: lượt $s_A\xrightarrow1s_B\xrightarrow2$ có xác suất $\tfrac16$, lượt $s_A\xrightarrow2$ có $\tfrac12$. Lợi thế GAE với $\lambda=1$ không lệch trung bình (mạch 3), nhưng trên một bộ đệm nhỏ nó có thể sai dấu. Ở mạch 4, hàm thay thế chỉ đúng gần chính sách cũ; ở đây thêm lý do thứ hai: lợi thế chỉ là ước lượng. Hàm thay thế mẫu tuyến tính theo $p'$, nên Adam đi tới tận biên. TRPO giữ bước nhỏ bằng ràng buộc KL; mạch này làm việc đó chỉ bằng hàm mục tiêu."
- **Nguồn:** đề xuất sửa ghi chú G2 (mục 11): đoạn mới mở §6.1; Ví dụ 10.8 (critic $(1{,}4;1)$, lượt (ii): $G_0-\hat v(s_A)=-1{,}4$, $\delta_1=-1$); Định nghĩa 10.21 (tỉ số, hàm thay thế mẫu).
- **Bố cục:**

```
┌──────────────────────────────────────────────────────────────┐
│ Bộ đệm hai lượt đẩy chính sách đi xa và sai hướng             │
├───────────────┬──────────────────────────────────────────────┤
│ [chuỗi nhỏ,   │ Chuỗi, critic (1,4;1), λ=1. Bộ đệm có hai lượt … │
│  hai lượt     │ Nhắc lại (Bài 06): … tỉ số ρ … trung bình ρÂ     │
│  hai màu]     │                                                │
├───────────────┴──────────────────────────────────────────────┤
│ Trạng thái│ Mẫu: Â ước lượng     │ đúng      │ h.t.t. mẫu  │ tối đa│
│ s_A       │ 1: −1,4 đỏ; 2: −0,4  │ +0,4;−0,4 │ −0,4−p'_A   │ p'_A=0│
│ s_B       │ 2: −1                │ −2        │ −3(1−p'_B)  │ p'_B=1│
│ J thật tại (0;1) là 1: giảm 0,4.                         (3)  │
├──────────────────────────────────────────────────────────────┤
│ Câu hỏi: Sửa hàm mục tiêu thế nào để Adam không …        (4)  │
└──────────────────────────────────────────────────────────────┘
```

#### `L10-5-02` · Mục tiêu cắt bỏ phần thưởng của việc đi quá xa

- **Câu:** 5. **Biết thêm:** công thức mục tiêu cắt và cách đọc nó theo dấu của lợi thế.
- **1 phút:** Với lợi thế dương, đường đi lên tới $\rho=1{,}2$ rồi nằm ngang; với lợi thế âm, đường nằm ngang tới $\rho=0{,}8$ rồi đi xuống; đoạn ngang có gradient $0$.
- **Mới:** phép cắt với bán kính $\epsilon$ (mục tiêu PPO-Clip).
- **Ý chính:** tiêu đề; câu "Phía bất lợi không bị cắt."
- **Mặt trang** (≈ 40 âm tiết):
  - "Nhắc lại (Bài 06): tỉ số $\rho=\pi_\theta(a\mid s)/\pi_{\mathrm{old}}(a\mid s)$."
  - $$\ell^{\mathrm{CLIP}}=\min\Bigl(\underbrace{\rho\,\widehat A}_{\text{hàm thay thế}},\ \underbrace{\operatorname{clip}(\rho,1-\epsilon,1+\epsilon)\,\widehat A}_{\text{tỉ số bị kẹp vào }[0{,}8;\,1{,}2]}\Bigr)$$
  - "Lợi thế dương: không thưởng thêm khi $\rho>1+\epsilon$. Lợi thế âm: không thưởng thêm khi $\rho<1-\epsilon$. Phía bất lợi không bị cắt."
- **Hình:** hai khung cạnh nhau theo Hình 1 của bài báo PPO (vẽ lại `ppo-clipping-signs.svg`, bỏ bốn điểm mẫu, nhãn ≥ 20 px): khung trái "$\widehat A>0$": đường liền đi lên tới $\rho=1{,}2$ rồi ngang, đoạn ngang tô sọc "gradient $0$"; khung phải "$\widehat A<0$": ngang tới $\rho=0{,}8$ (sọc, "gradient $0$") rồi đi xuống; đường mảnh nét đứt $\rho\widehat A$ ở cả hai khung. Trục hoành có vạch $0{,}8$, $1$, $1{,}2$. Khoảng 45%, nửa dưới. Tệp `ppo-cat-hai-dau.svg`.
- **Dựng dần:** (0) nhắc lại và công thức; (1) khung trái và câu thứ nhất; (2) khung phải và câu thứ hai; (3) câu "Phía bất lợi không bị cắt."
- **Ghi chú diễn giả:** "Phép lấy nhỏ hơn làm mục tiêu bi quan: nó bỏ phần tăng khi tỉ số ra ngoài theo hướng có lợi, giữ phần giảm khi tỉ số đi theo hướng bất lợi. Nhầm lẫn hay gặp: mọi mẫu ngoài khoảng đều có gradient $0$; điều đó chỉ đúng phía có lợi. CPI là tên của mục tiêu không cắt trong bài báo; trên trang ta gọi nó là hàm thay thế."
- **Nguồn:** Định nghĩa 10.39; Mệnh đề 10.40 (câu lời thường, câu chuyện mục 5); hình `ppo-clipping-signs.svg` của ghi chú.
- **Bố cục:**

```
┌──────────────────────────────────────────────────────────────┐
│ Mục tiêu cắt bỏ phần thưởng của việc đi quá xa               │
├──────────────────────────────────────────────────────────────┤
│ Nhắc lại: ρ = π_θ/π_old                                      │
│ ℓ = min( ρÂ , clip(ρ,1−ε,1+ε)Â )                              │
│        └h.thay thế┘ └kẹp vào [0,8;1,2]┘                        │
├──────────────────────────────┬───────────────────────────────┤
│ Â>0      ____▒▒▒▒ g=0          │ Â<0  ▒▒▒▒____                  │
│        ╱  1,2                  │       0,8    ╲                 │
│ Lợi thế dương: … (1)          │ Lợi thế âm: … (2)              │
├──────────────────────────────┴───────────────────────────────┤
│ Phía bất lợi không bị cắt. (3)                                │
└──────────────────────────────────────────────────────────────┘
```

#### `L10-5-03` · Câu hỏi nhanh: mẫu lợi thế âm với $\rho=1{,}3$

- **Câu:** 5. **Biết thêm:** khi chính sách đi theo hướng bất lợi, phép cắt không chặn; gradient kéo nó trở lại.
- **1 phút:** Mẫu hành động 2 có $\rho=1{,}3$ nằm trên đoạn dốc của khung phải, nên không bị cắt và vẫn có gradient.
- **Mới:** không. **Ý chính:** hộp "Lời giải:".
- **Mặt trang** (≈ 45 âm tiết):
  - Hộp "Câu hỏi: Mẫu chọn hành động 2 (lợi thế $-2$) có $\rho=1{,}3$, tức $p$ đã giảm còn $0{,}57$. Với $\epsilon=0{,}2$, mẫu có bị cắt không?"
  - Hộp "Lời giải: Không. $\min(-2\cdot1{,}3;\,-2\cdot1{,}2)=-2{,}6$ giữ nhánh không cắt, nên gradient khác $0$ kéo $p$ trở lại."
- **Hình:** như `L10-5-02`; trên khung phải thêm điểm "?" đỏ ở $\rho=1{,}3$; fragment lời giải thay "?" bằng điểm vuông trên đoạn dốc, nhãn "$-2{,}6$".
- **Dựng dần:** (0) câu hỏi và điểm "?"; (1) lời giải và điểm vuông.
- **Ghi chú diễn giả:** "$\rho(2)=1{,}3$ nghĩa là xác suất của hành động 2 tăng từ $\tfrac13$ lên $0{,}433$, tức $p$ giảm còn $0{,}567$. Hành động kém được chọn nhiều hơn, nên mục tiêu phải phạt đủ. Ví dụ 10.18 của ghi chú có bốn mẫu cho cả bốn trường hợp."
- **Nguồn:** Mệnh đề 10.40(b), (d); Ví dụ 10.18 (mẫu $(-2;1{,}3)$).

#### `L10-5-04` · Trên $s_B$, mục tiêu cắt nằm ngang từ $p=0{,}8$

- **Câu:** 5. **Biết thêm:** cơ chế dừng của mục tiêu cắt, xem trên một trạng thái với bộ đệm đúng tần suất: gradient bằng $0$ từ $p=0{,}8$.
- **1 phút:** Hàm thay thế $3p-2$ tăng tới $p=1$; đường gấp khúc trùng nó tới $p\approx0{,}73$, gập lần hai ở $p=0{,}8$ rồi nằm ngang ở $0{,}27$; hai mốc là hai lúc một nhóm mẫu chạm biên.
- **Mới:** không (áp công thức trên ví dụ). **Ý chính:** tiêu đề; câu "Mục tiêu cắt nằm dưới hàm thay thế và trùng nó quanh chính sách cũ."
- **Mặt trang** (≈ 50 âm tiết):
  - "Để thấy cơ chế, xét riêng $s_B$ với ba mẫu đúng tần suất của chính sách cũ $(\tfrac23;\,\tfrac13)$: hành động $1,1,2$, lợi thế đúng $1,1,-2$. Hàm thay thế mẫu: $\tfrac13\bigl[1{,}5p+1{,}5p-2\cdot3(1-p)\bigr]=3p-2$."
  - "$\rho(1)=1{,}5p$ chạm $1{,}2$ tại $p=0{,}8$. $\rho(2)=3(1-p)$ chạm $0{,}8$ tại $p\approx0{,}73$."
  - Câu ý chính.
  - Nhãn trên hình (không tính âm tiết): "$p\approx0{,}73$: mẫu hành động 2 chạm $\rho=0{,}8$" · "$p=0{,}8$: hai mẫu hành động 1 chạm $\rho=1{,}2$" · "mức phẳng $\tfrac13(2{,}4-1{,}6)\approx0{,}27$".
- **Hình:** đồ thị theo $p\in[\tfrac23;1]$, trục tung $[0;1]$; đường cam nét đứt "$3p-2$"; đường gấp khúc xanh, nét liền đậm: trùng $3p-2$ trên $[\tfrac23;\,0{,}73]$, đoạn $p-0{,}53$ trên $[0{,}73;\,0{,}8]$, ngang $0{,}27$ từ $0{,}8$; hai vạch đứng mảnh ở $0{,}73$ và $0{,}8$; điểm $p=\tfrac23$ "chính sách cũ". Khoảng 55%. Tệp `ppo-sB-do-thi.svg` (bản b).
- **Dựng dần:** (0) dữ kiện và đường cam; (1) đoạn trùng và mốc $0{,}73$; (2) đoạn giữa và mốc $0{,}8$; (3) đoạn ngang, mức $0{,}27$, câu ý chính.
- **Ghi chú diễn giả:** "Trên một trạng thái với bộ đệm đúng tần suất, hàm thay thế bằng đúng $J-J_{\mathrm{old}}$, nên đi tới $p=1$ không hại; ta dùng ví dụ này chỉ để xem đường gấp khúc. Đọc theo $p$ tăng dần: mẫu hành động 2 có lợi thế âm, nó ngừng được thưởng thêm khi $\rho(2)$ xuống $0{,}8$; hai mẫu hành động 1 ngừng được thưởng thêm khi $\rho(1)$ lên $1{,}2$. Tại $p=0{,}75$, gradient theo logit là $0{,}1875$ với mục tiêu cắt, $0{,}5625$ không cắt."
- **Nguồn:** Ví dụ 10.17 (dữ kiện, "Mục tiêu không cắt", "Mục tiêu cắt", "Diễn giải"); hình `ppo-one-step-plateau.svg` của ghi chú; Mệnh đề 10.41 (câu lời thường); Ví dụ 10.20 (gradient tại $0{,}75$).
- **Bố cục:**

```
┌──────────────────────────────────────────────────────────────┐
│ Trên s_B, mục tiêu cắt nằm ngang từ p=0,8                    │
├──────────────────────────────┬───────────────────────────────┤
│ 1 ┤                 ╱ cam 3p−2 │ Để thấy cơ chế, xét riêng s_B  │
│   │            ╱               │ … hàm thay thế mẫu 3p−2        │
│0,27┤──────┏━━━━━━━ xanh phẳng   │ ρ(1)=1,5p chạm 1,2 tại 0,8.    │
│   │   ╱┃ ┃                     │ ρ(2)=3(1−p) chạm 0,8 tại 0,73. │
│ 0 ┼─●╱─┃─┃──────── p            │                               │
│   ⅔  0,73 0,8                  │                               │
├──────────────────────────────┴───────────────────────────────┤
│ Mục tiêu cắt nằm dưới hàm thay thế và trùng nó quanh … (3)    │
└──────────────────────────────────────────────────────────────┘
```

#### `L10-5-05` · Trên bộ đệm hai lượt, phép cắt giữ $J$ gần như không đổi

- **Câu:** 5 (trạm dừng; quay lại hiện tượng mở mạch). **Biết thêm:** phép cắt không sửa lợi thế sai, nhưng giới hạn mỗi vòng đi bao xa: $J$ giảm $0{,}008$ thay cho $0{,}4$.
- **1 phút:** Với cùng bộ đệm xui, không cắt thì $p_A$ về $0$ và $J$ giảm $0{,}4$; có cắt thì $p_A$ dừng ở $0{,}4$, $p_B$ ở $0{,}73$, và $J$ gần như không đổi.
- **Mới:** không (gom ý). **Ý chính:** tiêu đề; hộp "Phép cắt không sửa được lợi thế sai, nhưng giới hạn mỗi vòng đi bao xa."
- **Mặt trang** (≈ 45 âm tiết ngoài bảng):
  - Bảng (bộ đệm của `L10-5-01`, $\epsilon=0{,}2$):

    | Trạng thái | Không cắt, dừng ở | Có cắt, dừng ở | Mốc |
    |---|---|---|---|
    | $s_A$ | $p_A=0$ | $p_A=0{,}4$ | $\rho(1)=2p_A$ chạm $0{,}8$ |
    | $s_B$ | $p_B=1$ | $p_B\approx0{,}73$ | $\rho(2)=3(1-p_B)$ chạm $0{,}8$ |
    | $J$ thật | $1$ (giảm $0{,}4$) | $2{,}7\cdot0{,}4\cdot\tfrac{11}{15}+0{,}6=1{,}392$ (giảm $0{,}008$) | |
  - Hộp như trên.
  - "Còn thiếu: gradient bằng $0$ chưa chắc giữ tham số đứng yên."
- **Hình:** sơ đồ neo không dùng ở đây; không hình riêng; lý do: bảng so hai cột trên cùng bộ đệm là bằng chứng (TB10, bảng so sánh).
- **Dựng dần:** (0) bảng cột "không cắt"; (1) cột "có cắt" và cột mốc; (2) hàng $J$; (3) hộp và dòng "Còn thiếu".
- **Ghi chú diễn giả:** "Tại $s_A$ cả hai lợi thế ước lượng đều âm; mẫu hành động 1 ngừng bị phạt thêm khi $\rho(1)$ xuống $0{,}8$, tức $p_A=0{,}4$; dưới đó, mẫu hành động 2 đi theo hướng bất lợi và không bị cắt, nên mục tiêu giảm. Tại $s_B$, một mẫu hành động 2 ngừng được thưởng khi $\rho(2)=0{,}8$, tức $p_B=\tfrac{11}{15}$. Với lợi thế đúng, hàm thay thế tại điểm dừng chỉ báo $+0{,}01$: bước nhỏ nên sai số nhỏ, như mạch 4."
- **Nguồn:** đề xuất sửa ghi chú G3 (mục 11): đoạn mới sau Ví dụ 10.18; Mệnh đề 10.40.
- **Bố cục:**

```
┌──────────────────────────────────────────────────────────────┐
│ Trên bộ đệm hai lượt, phép cắt giữ J gần như không đổi        │
├──────────────────────────────────────────────────────────────┤
│ Trạng thái │ Không cắt │ Có cắt      │ Mốc                     │
│ s_A        │ p_A=0     │ p_A=0,4     │ ρ(1)=2p_A chạm 0,8  (1) │
│ s_B        │ p_B=1     │ p_B≈0,73    │ ρ(2)=3(1−p_B) chạm 0,8  │
│ J thật     │ 1 (−0,4)đỏ│ ≈1,392 (−0,008) xanh             (2) │
├──────────────────────────────────────────────────────────────┤
│ [hộp] Phép cắt không sửa được lợi thế sai, nhưng giới hạn …   │
│ Còn thiếu: gradient bằng 0 chưa chắc giữ tham số …       (3)  │
└──────────────────────────────────────────────────────────────┘
```

#### `L10-5-06` · Phép cắt không chặn KL

- **Câu:** 5 ("Còn thiếu" của mạch). **Biết thêm:** gradient bằng $0$ không giữ tham số đứng yên; KL vẫn tăng, nên PPO đo approxKL và dừng sớm.
- **1 phút:** Trên đoạn phẳng, tham số vẫn trôi từ $p=0{,}8$ tới $0{,}85$; mục tiêu không đổi, gradient bằng $0$, nhưng KL tăng từ $0{,}049$ lên $0{,}10$.
- **Mới:** approxKL (ước lượng KL trên bộ đệm).
- **Ý chính:** tiêu đề; hộp "PPO đo approxKL và dừng sớm khi nó vượt ngưỡng."
- **Mặt trang** (≈ 40 âm tiết):
  - "KL tới chính sách cũ: $\tfrac23\log\dfrac{2/3}{p}+\tfrac13\log\dfrac{1/3}{1-p}$."
  - "Quán tính của Adam và các mini-batch khác vẫn đẩy tham số vào đoạn phẳng."
  - Hộp "PPO đo approxKL, một ước lượng KL trên bộ đệm, và dừng sớm khi nó vượt ngưỡng."
- **Hình:** đồ thị của `L10-5-04` (bản c), hai điểm trên đoạn ngang xanh: $p=0{,}8$ nhãn "KL $0{,}049$" và $p=0{,}85$ nhãn "KL $0{,}10$", cả hai ghi "gradient $0$"; mũi tên đỏ nối hai điểm, nhãn "tham số vẫn trôi". Khoảng 55%.
- **Dựng dần:** (0) hình với điểm $0{,}8$; (1) mũi tên và điểm $0{,}85$; (2) câu và hộp.
- **Bố cục:**

```
┌──────────────────────────────────────────────────────────────┐
│ Phép cắt không chặn KL                                       │
├──────────────────────────────┬───────────────────────────────┤
│ 0,27┤──────●━━━━━━▶●  (xanh)   │ KL tới chính sách cũ: …        │
│     │  KL 0,049   KL 0,10     │ Quán tính của Adam … đoạn phẳng│
│     │  gradient 0 · đỏ: trôi  │ [hộp] PPO đo approxKL …        │
│   ⅔ ┼────0,8────0,85──── p    │                               │
└──────────────────────────────┴───────────────────────────────┘
```
- **Ghi chú diễn giả:** "Mục tiêu cắt chỉ bỏ động lực đẩy tỉ số ra ngoài khoảng; nó không ngăn tỉ số ra ngoài. Với bộ đệm đúng tần suất, approxKL bằng KL thật: $0{,}04873$ tại $p=0{,}8$ và $0{,}1042$ tại $p=0{,}85$. Tỉ lệ mẫu bị cắt ở $p=0{,}85$ là ba trên ba. Biến thể PPO-Penalty phạt KL với hệ số tự chỉnh; chi tiết ở ghi chú."
- **Nguồn:** Nhận xét 10.42; đoạn sau Định nghĩa 10.23 (KL $0{,}04873$ tại $(0{,}8;0{,}2)$), Ví dụ 10.21 ($0{,}1042$); Định nghĩa 10.47, Mệnh đề 10.48 (câu lời thường); §6.2 (PPO-Penalty, một câu ở ghi chú diễn giả).

#### `L10-5-07` · Một vòng PPO dùng mỗi lô dữ liệu nhiều lần

- **Câu:** 5. **Biết thêm:** vòng PPO đầy đủ: thu, GAE, vài epoch Adam trên một hàm mất mát ba số hạng.
- **1 phút:** Khối cập nhật của vòng giờ là $K$ lượt qua cùng bộ đệm, mỗi lô nhỏ một bước Adam trên hàm mất mát gồm mục tiêu cắt, mất mát của critic và thưởng entropy.
- **Mới:** hàm mất mát tổng.
- **Ý chính:** câu "Mỗi lô dữ liệu cho nhiều bước gradient thay cho một."
- **Mặt trang** (≈ 30 âm tiết ngoài hình):
  - $$L=-\underbrace{\mathcal L^{\mathrm{CLIP}}}_{\text{actor}}+c_1\underbrace{L^V}_{\text{critic hồi quy về }\widehat A_t+\hat v(S_t)}-c_2\underbrace{\mathcal H}_{\text{thưởng entropy: giữ chính sách đủ ngẫu nhiên}}$$
  - "$c_1$, $c_2$ là hai trọng số. Mỗi lô dữ liệu cho nhiều bước gradient thay cho một."
- **Hình:** sơ đồ neo `so-do-neo-m5-ra.svg` ở nửa trái: nhãn ⑤ "tối đa mục tiêu cắt, nhiều lượt qua dữ liệu (PPO)"; ④ ghi "$\widehat A_t$ (GAE)". Từ ⑤ một mũi tên sang nửa phải mở vòng trong ba khung xếp dọc: "$K$ lượt qua bộ đệm (epoch), mỗi lượt chia lô nhỏ (mini-batch)" → "một bước Adam trên $L$" → "approxKL vượt ngưỡng thì dừng". Khoảng 55%.
- **Dựng dần:** (0) sơ đồ neo; (1) vòng trong; (2) công thức; (3) câu.
- **Bố cục:**

```
┌──────────────────────────────────────────────────────────────┐
│ Một vòng PPO dùng mỗi lô dữ liệu nhiều lần                    │
├──────────────────────────────┬───────────────────────────────┤
│ ①→②Thu lượt ◀──────┐          │ ┌ K lượt qua bộ đệm (epoch), ┐ │
│ ③→④Â_t (GAE)       │          │ │ chia lô nhỏ (mini-batch)   │ │
│     ↓              │   ───▶   │ └─────────────┬─────────────┘ │
│ ⑤[mục tiêu cắt, PPO]┘ (tím)    │   một bước Adam trên L        │
│                              │   approxKL vượt ngưỡng: dừng   │
├──────────────────────────────┴───────────────────────────────┤
│ L = −L^CLIP + c₁L^V − c₂H  (ba ngoặc dưới)              (2)   │
│ c₁, c₂ là hai trọng số. Mỗi lô dữ liệu cho nhiều bước …  (3)  │
└──────────────────────────────────────────────────────────────┘
```
- **Ghi chú diễn giả:** "Ba thứ giữ cố định trong cả $K$ epoch: log-xác suất cũ, lợi thế, mục tiêu của critic; ba thứ tính lại ở mỗi mini-batch: log-xác suất mới, tỉ số, giá trị của critic. Ví dụ 10.20 của ghi chú tính một mini-batch: $-0{,}2167+2{,}04-0{,}0056=1{,}8177$. Bảng siêu tham số và chi tiết cài đặt ở ghi chú."
- **Nguồn:** Định nghĩa 10.46; Thuật toán 10.49 (dạng sơ đồ); Ví dụ 10.20 (ghi chú diễn giả); §6.4–6.6 ở lại ghi chú.

#### `L10-5-08` · TRPO và PPO cùng giữ bước gần, khác cách giữ

- **Câu:** 5 (trạm dừng cuối mạch 5). **Biết thêm:** so hai cách giữ bước gần trên ba tiêu chí, và điều cả hai còn cần.
- **1 phút:** TRPO giữ gần bằng ràng buộc KL và tìm kiếm lùi, PPO bằng phép cắt và approxKL; PPO rẻ hơn; cả hai không bảo đảm $J$ tăng, và cả hai cần một hàm phần thưởng.
- **Mới:** không (gom ý). **Ý chính:** dòng "Còn thiếu: cả hai cần một hàm phần thưởng."
- **Mặt trang** (bảng so sánh, ≈ 50 âm tiết):

  | | TRPO | PPO |
  |---|---|---|
  | Giữ gần bằng | ràng buộc KL trung bình, tìm kiếm lùi | cắt tỉ số trong mục tiêu, approxKL |
  | Mỗi lô dữ liệu cho | một bước, khoảng mười tích $Fv$ | $K$ epoch bước Adam trên mini-batch |
  | Bảo đảm $J$ tăng | không, như cài đặt | không |

  "Còn thiếu: cả hai cần một hàm phần thưởng."
- **Hình:** không; lý do: bảng so sánh 2 phương pháp × 3 tiêu chí (TB10 cho phép bảng khi so sánh; NT-RL "Tables").
- **Dựng dần:** (0) bảng; (1) dòng "Còn thiếu".
- **Ghi chú diễn giả:** "Kết quả hội tụ hiện có của PPO-Clip chỉ nói về điểm dừng trong một mô hình đơn giản hóa không có Adam và mini-batch (Nhận xét 10.51, đọc thêm). Mạch sau bỏ giả thiết rằng môi trường cho phần thưởng."
- **Nguồn:** §6.3 đoạn "Trong thực hành"; bảng §8.2 (hai hàng TRPO, PPO); Nhận xét 10.51.

### Mạch 6. Học từ so sánh của người (`id="mach-6"`, 10 trang, 22 phút)

Ví dụ chạy: một lời nhắc, hai câu trả lời $y_1$, $y_2$; mô hình hiện tại (chính sách tham chiếu) $\pi_{\mathrm{ref}}=(\tfrac23;\tfrac13)$, cùng xác suất với $s_B$ ở mạch 5 (quyết định 9); sáu so sánh, bốn lần chọn $y_1$; $\beta=1$. Hai con đường (RLHF với PPO, DPO) tới cùng $\pi^*=(\tfrac45;\tfrac15)$.

#### `L10-6-00` · Trang tiêu đề mạch 6 (điểm vào mạch 6)

- **Câu:** 6. **Biết thêm:** việc của mạch: học khi không có hàm phần thưởng.
- **1 phút:** Mạch này thay khối phần thưởng, vì nhiều bài toán không có phần thưởng, chỉ có người chọn câu trả lời tốt hơn.
- **Mới:** không. **Ý chính:** dòng dẫn.
- **Mặt trang:** "6." · "Học từ so sánh của người" · `p.strand-lead` "Không có phần thưởng, chỉ có người chọn câu trả lời tốt hơn." (13 âm tiết).
- **Hình:** `so-do-neo-m6-vao.svg`: ① tô tím, nhãn "phần thưởng ?".
- **Ghi chú diễn giả:** "PPO cần một hàm phần thưởng. Khi tinh chỉnh một mô hình ngôn ngữ, ta chỉ có người đọc hai câu trả lời và chọn câu tốt hơn. Mạch này học một phần thưởng từ các lần chọn, thêm phạt rời mô hình ban đầu, rồi so hai cách tìm chính sách tốt nhất: chạy PPO, hoặc học thẳng bằng một hàm mất mát phân loại."
- **Nguồn:** đoạn cuối §1.1 (phần thứ ba của bài toán trung tâm); §7 đoạn mở.

#### `L10-6-01` · Một lời nhắc, hai câu trả lời, sáu lần chọn

- **Câu:** 6. **Biết thêm:** dữ liệu của bài toán: xác suất của mô hình hiện tại và sáu lần chọn, không có phần thưởng.
- **1 phút:** Mô hình hiện tại trả lời bằng câu 1 với xác suất $\tfrac23$, câu 2 với $\tfrac13$; người chọn câu 1 bốn lần, câu 2 hai lần; mô hình mới nên chọn thế nào?
- **Mới:** đối tượng mới (lời nhắc, câu trả lời). **Ý chính:** hộp "Câu hỏi:".
- **Mặt trang** (≈ 50 âm tiết):
  - "Một mô hình ngôn ngữ nhận một lời nhắc (prompt) và đáp bằng câu trả lời (response) 1 hay 2, với xác suất $\tfrac23$ và $\tfrac13$. Không có hàm phần thưởng. Sáu lần, người đọc hai câu và chọn câu tốt hơn."
  - Hộp "Câu hỏi: Mô hình mới nên chọn mỗi câu với xác suất bao nhiêu? Có cần một vòng học tăng cường để tìm nó không?"
- **Hình:** thẻ "lời nhắc" ở trên; hai thẻ "câu trả lời 1", "câu trả lời 2" bên dưới, mỗi thẻ có thanh xác suất "$\tfrac23$", "$\tfrac13$"; dưới thẻ 1 bốn dấu chọn, dưới thẻ 2 hai dấu chọn (cùng hình dạng, đếm được), nhãn "6 lần người chọn". Không ký hiệu (TB3). Khoảng 50%. Tệp `loi-nhac-hai-cau-tra-loi.svg`.
- **Dựng dần:** (0) lời nhắc, hai thẻ và xác suất; (1) sáu dấu chọn; (2) hộp câu hỏi.
- **Ghi chú diễn giả:** "Đây là bài toán một bước: trạng thái là lời nhắc, hành động là cả câu trả lời. Với mô hình thật, câu trả lời là một chuỗi token và tập câu trả lời rất lớn, nhưng mọi công thức của mạch giữ nguyên. Cùng xác suất $\tfrac23$, $\tfrac13$ như $s_B$ ở mạch trước."
- **Nguồn:** §7.1 đoạn mở và "Câu hỏi"; Định nghĩa 10.52 (ở lại ghi chú); Ví dụ 10.23.

#### `L10-6-02` · Khớp phần thưởng để xác suất chọn bằng tỉ lệ $\tfrac46$

- **Câu:** 6 ("ta khớp phần thưởng từ các so sánh"). **Biết thêm:** mô hình Bradley–Terry nối phần thưởng với xác suất người chọn; trên ví dụ, $\hat r=(\log2;\,0)$.
- **1 phút:** Xác suất người chọn câu 1 là $\sigma$ của hiệu phần thưởng; tỉ lệ $\tfrac46=\tfrac23$ cho hiệu $\log2$.
- **Mới:** mô hình Bradley–Terry và mô hình phần thưởng $\hat r$ (ký hiệu $y_1$, $y_2$ cho hai câu).
- **Ý chính:** tiêu đề; dòng kết quả "$\hat r=(\log2;\,0)$".
- **Mặt trang** (≈ 40 âm tiết):
  - "Ký hiệu: $y_1$, $y_2$ là hai câu trả lời. Mô hình Bradley–Terry: người chọn câu có phần thưởng cao hơn thường xuyên hơn, và chỉ hiệu phần thưởng có vai trò."
  - $$\Pr(y_1\text{ được chọn})=\sigma\bigl(\underbrace{\hat r(y_1)-\hat r(y_2)}_{\text{hiệu phần thưởng}}\bigr),\qquad\sigma(z)=\frac1{1+e^{-z}}.$$
  - "Hợp lý cực đại cho $\sigma(\Delta\hat r)=\tfrac46$, tức $\Delta\hat r=\log2$. Chọn $\hat r(y_2)=0$: $\hat r=(\log2;\,0)$."
- **Hình:** đường $\sigma(z)$ trên $z\in[-3;3]$; đường ngang nét đứt ở $\tfrac23$, nhãn "tỉ lệ $\tfrac46$", gặp đường cong tại $z=\log2\approx0{,}69$, vạch đứng xuống trục, nhãn "$\Delta\hat r=\log2$". Khoảng 40%, bên phải. Tệp `bradley-terry-sigmoid.svg`; dùng lại ở `L10-6-09`.
- **Dựng dần:** (0) mô hình và đường cong; (1) đường ngang và kết quả.
- **Ghi chú diễn giả:** "Mất mát Bradley–Terry là hồi quy logistic trên hiệu phần thưởng: tại hiệu $0$ nó bằng $\log2=0{,}693$, cực tiểu $0{,}6365$ tại hiệu $\log2$. Chỉ hiệu được xác định, nên ta cố định $\hat r(y_2)=0$. Nếu người luôn chọn một phía, không có hiệu hữu hạn nào khớp; câu hỏi cuối mạch quay lại điều này."
- **Nguồn:** Định nghĩa 10.53; Mệnh đề 10.54 (câu lời thường); Ví dụ 10.24.

#### `L10-6-03` · Phạt KL chọn một điểm giữa tham lam và mô hình ban đầu

- **Câu:** 6 ("và phạt việc rời mô hình ban đầu"). **Biết thêm:** chính sách tối đa $\hat r$ thành tất định và đi xa mô hình ban đầu; trừ $\beta$ lần KL thì tổng có đỉnh ở giữa.
- **1 phút:** Đường $J_1$ theo xác suất chọn $y_1$: bằng $0{,}462$ ở mô hình ban đầu, $0{,}288$ ở chính sách tham lam, và có đỉnh ở giữa, khoảng $0{,}51$.
- **Mới:** mục tiêu có phạt KL $J_\beta$ (với chính sách tham chiếu $\pi_{\mathrm{ref}}$ là mô hình hiện tại).
- **Ý chính:** tiêu đề; hình.
- **Mặt trang** (≈ 40 âm tiết):
  - $$J_\beta(\pi)=\underbrace{\mathbb E_{y\sim\pi}\,\hat r(y)}_{\text{phần thưởng}}-\beta\,\underbrace{D_{\mathrm{KL}}(\pi\Vert\pi_{\mathrm{ref}})}_{\text{rời mô hình ban đầu}}$$
  - "$\pi_{\mathrm{ref}}=(\tfrac23;\,\tfrac13)$ là mô hình hiện tại, giữ cố định. Lấy $\beta=1$. Với $p=\pi(y_1)$:" $J_1(p)=p\log2-p\log\dfrac{p}{2/3}-(1-p)\log\dfrac{1-p}{1/3}$.
  - "Chính sách tham lam $(1;\,0)$ bỏ hẳn $y_2$ và trả KL $\log\tfrac32=0{,}405$."
- **Hình:** đường $J_1(p)$ trên $p\in[\tfrac23;1]$, trục tung $[0{,}25;0{,}55]$ (vẽ theo công thức; điểm vẽ, không ghi: $0{,}483$ tại $0{,}7$; $0{,}503$ tại $0{,}75$; $0{,}502$ tại $0{,}85$; $0{,}474$ tại $0{,}9$; $0{,}417$ tại $0{,}95$). Ba điểm có nhãn: $p=\tfrac23$ "mô hình ban đầu: $\tfrac23\log2=0{,}462$"; $p=1$ "tham lam: $\log2-\log\tfrac32=0{,}288$" (đỏ); đỉnh (tím) "đỉnh $\approx0{,}51$" không ghi hoành độ (trang sau tính ra). Khoảng 50%. Tệp `phat-kl-duong-J1.svg`.
- **Dựng dần:** (0) công thức và dòng $\pi_{\mathrm{ref}}$; (1) đường cong với điểm mô hình ban đầu; (2) điểm tham lam và câu; (3) đỉnh.
- **Ghi chú diễn giả:** "Với mô hình ngôn ngữ, chính sách tham lam theo $\hat r$ có thể sinh câu khác xa các câu mà $\hat r$ đã được khớp, nơi $\hat r$ không đáng tin. Phạt KL giữ chính sách gần mô hình ban đầu; $\beta$ là giá của mỗi đơn vị KL. KL ở đây lấy theo chính sách đang tối ưu, $D_{\mathrm{KL}}(\pi\Vert\pi_{\mathrm{ref}})$. Hỏi lớp: đỉnh ở đâu? Trang sau cho công thức."
- **Nguồn:** §7.2 đoạn mở; Ví dụ 10.25 (công thức $J_1$, hai hàng $\pi_{\mathrm{ref}}$ và tham lam); Định nghĩa 10.56.
- **Bố cục:**

```
┌──────────────────────────────────────────────────────────────┐
│ Phạt KL chọn một điểm giữa tham lam và mô hình ban đầu        │
├───────────────────────────────┬──────────────────────────────┤
│ J_β(π) = E r̂ − β KL(π‖π_ref)    │ 0,55┤     ●tím đỉnh ≈0,51       │
│        └p.thưởng┘ └rời m.h.b.đ┘ │     │  ╱      ╲                 │
│ π_ref=(⅔;⅓) … β=1. Với p=π(y₁): │0,46 ●m.h.b.đ   ╲                │
│ J₁(p) = …                      │     │            ╲              │
│ Tham lam (1;0) bỏ hẳn y₂ …     │0,29┤             ●đỏ tham lam  │
│                               │     ⅔                1  p      │
└───────────────────────────────┴──────────────────────────────┘
```

#### `L10-6-04` · Nghiệm có phạt KL: $\pi^*\propto\pi_{\mathrm{ref}}\,e^{\hat r/\beta}$

- **Câu:** 6 (trang kết quả; "cùng đi tới một chính sách"). **Biết thêm:** mục tiêu có phạt KL có nghiệm dạng đóng; trên ví dụ, $(\tfrac45;\,\tfrac15)$.
- **1 phút:** Nhân xác suất ban đầu với $e^{\hat r/\beta}$ rồi chuẩn hóa: $(\tfrac43;\,\tfrac13)$ chia $\tfrac53$ thành $(\tfrac45;\,\tfrac15)$; $\beta$ nhỏ đi xa mô hình ban đầu hơn.
- **Mới:** định lý nghiệm có phạt KL (khối "Giả thiết:/Kết luận:" thứ ba).
- **Ý chính:** tiêu đề.
- **Mặt trang** (≈ 40 âm tiết):
  - "Định lý (nghiệm có phạt KL)."
  - "Giả thiết: $\beta>0$. Chính sách được chọn tự do cho mỗi lời nhắc."
  - "Kết luận: $J_\beta$ lớn nhất tại" $$\pi^*(y)=\frac{\pi_{\mathrm{ref}}(y)\,e^{\hat r(y)/\beta}}{\mathcal Z},\qquad\mathcal Z=\sum_y\pi_{\mathrm{ref}}(y)\,e^{\hat r(y)/\beta}.$$
  - "Với $\beta=1$: $\pi_{\mathrm{ref}}e^{\hat r}=(\tfrac43;\,\tfrac13)$, $\mathcal Z=\tfrac53$, $\pi^*=(\tfrac45;\,\tfrac15)$."
  - "Còn thiếu: với mô hình ngôn ngữ, $\mathcal Z$ là tổng trên mọi câu trả lời, không tính được."
- **Hình:** biểu đồ cột hai nhóm ($y_1$, $y_2$): cột xám $\pi_{\mathrm{ref}}$ ($\tfrac23$; $\tfrac13$), cột tím $\pi^*$ với $\beta=1$ ($0{,}8$; $0{,}2$); hai cột mảnh, nhạt, cho $\beta=\tfrac12$ ($0{,}89$; $0{,}11$) và $\beta=2$ ($0{,}74$; $0{,}26$), nhãn "$\beta$ nhỏ: đi xa mô hình ban đầu". Khoảng 40%, bên phải. Tệp `nghiem-phat-kl-cot.svg`.
- **Dựng dần:** (0) khối; (1) dòng tính và cột $\beta=1$; (2) cột $\beta=\tfrac12$, $\beta=2$; (3) dòng "Còn thiếu".
- **Ghi chú diễn giả:** "Đây là Định lý 10.57; giá trị tối ưu là $\beta\log\mathcal Z=\log\tfrac53=0{,}511$, đúng $J_1$ của hàng ba ở trang trước. Với mọi $\beta>0$, $\pi^*(y_2)>0$: phạt KL giữ mọi câu mà mô hình ban đầu có thể sinh. $\beta\to\infty$ cho $\pi^*\to\pi_{\mathrm{ref}}$, $\beta\to0$ cho chính sách tham lam."
- **Nguồn:** Định lý 10.57 (Giả thiết, Kết luận (b), (d)); Ví dụ 10.26.
- **Bố cục:**

```
┌──────────────────────────────────────────────────────────────┐
│ Nghiệm có phạt KL: π* ∝ π_ref e^{r̂/β}                          │
├──────────────────────────────────┬───────────────────────────┤
│ Định lý (nghiệm có phạt KL).      │  y₁: ▓▓▓▓ ⅔  ████ 0,8       │
│ Giả thiết: β>0. Chính sách …      │      (β=½: 0,89; β=2: 0,74) │
│ Kết luận: π*(y)=π_ref e^{r̂/β}/Z   │  y₂: ▓▓ ⅓    █ 0,2          │
│ β=1: (4/3;1/3), Z=5/3, π*=(⅘;⅕)    │  xám π_ref · tím π*        │
├──────────────────────────────────┴───────────────────────────┤
│ Còn thiếu: với mô hình ngôn ngữ, Z … không tính được.          │
└──────────────────────────────────────────────────────────────┘
```

#### `L10-6-05` · RLHF tìm $\pi^*$ bằng PPO trên phần thưởng đã trừ KL

- **Câu:** 6 ("RLHF (dùng PPO)"). **Biết thêm:** quy trình RLHF trên sơ đồ neo và lý do nó dừng ở $\pi^*$: tại đó hai câu có cùng phần thưởng đã trừ KL.
- **1 phút:** Khối phần thưởng của vòng giờ là "mô hình phần thưởng trừ phạt KL"; tại $(0{,}8;\,0{,}2)$ hai câu cùng nhận $0{,}51$, lợi thế bằng $0$, PPO đứng yên.
- **Mới:** RLHF và phần thưởng đã trừ KL $\tilde r$.
- **Ý chính:** tiêu đề; dòng kiểm "Hai câu cùng phần thưởng, lợi thế bằng $0$, PPO đứng yên."
- **Mặt trang** (≈ 45 âm tiết ngoài hình):
  - "Học tăng cường từ phản hồi con người (reinforcement learning from human feedback, RLHF) chạy PPO với phần thưởng"
    $$\tilde r(y)=\underbrace{\hat r(y)}_{\text{mô hình phần thưởng}}-\beta\,\underbrace{\log\frac{\pi(y)}{\pi_{\mathrm{ref}}(y)}}_{\text{phạt rời mô hình ban đầu}}.$$
  - "Tại $\pi^*=(0{,}8;\,0{,}2)$: $\tilde r(y_1)=\log2-\log1{,}2=0{,}51$ và $\tilde r(y_2)=0-\log0{,}6=0{,}51$. Hai câu cùng phần thưởng, lợi thế bằng $0$, PPO đứng yên."
- **Hình:** sơ đồ neo `so-do-neo-m6-rlhf.svg`: ① mở thành hai khung nối tiếp "so sánh của người → mô hình phần thưởng $\hat r$" và "trừ phạt KL tới $\pi_{\mathrm{ref}}$"; một khung nhỏ bên trái "tinh chỉnh có giám sát → $\pi_{\mathrm{ref}}$ (đóng băng)"; nhãn ① "phần thưởng học từ so sánh, trừ phạt KL (RLHF)"; ⑤ giữ "PPO"; nhãn góc "bốn mô hình trong bộ nhớ: $\pi_\theta$, $\pi_{\mathrm{ref}}$, $\hat r$, critic". Khoảng 50%.
- **Dựng dần:** (0) sơ đồ neo với ① mở; (1) công thức; (2) dòng kiểm.
- **Ghi chú diễn giả:** "Ba giai đoạn theo InstructGPT: tinh chỉnh có giám sát cho mô hình ban đầu, khớp mô hình phần thưởng từ so sánh, rồi PPO. Lưu ý hai chính sách khác nhau: chính sách cũ của PPO đổi sau mỗi vòng, chính sách tham chiếu thì cố định. Phép cắt đo tỉ số tới chính sách cũ; điểm dừng do $\pi_{\mathrm{ref}}$ và $\hat r$ quyết định. Hai vòng PPO tính tay ở Ví dụ 10.27 của ghi chú."
- **Nguồn:** Thuật toán 10.61 (dạng sơ đồ); Ví dụ 10.26 (phần thưởng đã trừ KL $0{,}5108$), Ví dụ 10.27 (vòng 2, chỉ phần đứng yên; vòng 1 ở lại ghi chú theo mục 4 của tệp này); Nhận xét 10.58.

#### `L10-6-06` · Đổi biến: phần thưởng viết theo chính sách

- **Câu:** 6 ("DPO … một hàm mất mát phân loại"; phần đổi biến). **Biết thêm:** lật công thức nghiệm, phần thưởng thành log-tỉ số của chính sách cộng một hằng; hằng đó triệt tiêu trong phép so sánh.
- **1 phút:** Ba hàng có nhãn bên trái: mục tiêu, nghiệm, đổi chiều; khi so hai câu, $\beta\log\mathcal Z$ trừ nhau mất, nên so sánh chỉ cần chính sách.
- **Mới:** phép đổi biến phần thưởng ↔ chính sách.
- **Ý chính:** hộp cuối "Trong phép so sánh hai câu, $\beta\log\mathcal Z$ triệt tiêu."
- **Mặt trang** (≈ 30 âm tiết):
  - Ba hàng, cột nhãn bên trái (theo CS234 bài 8 tr. 46–55, `phan-tich-slide-mau.md` mục 3.5):
    - "mục tiêu có phạt KL": $\max_\pi\ \mathbb E_\pi\,r-\beta\,D_{\mathrm{KL}}(\pi\Vert\pi_{\mathrm{ref}})$
    - "nghiệm": $\pi^*=\pi_{\mathrm{ref}}\,e^{r/\beta}/\mathcal Z$
    - "đổi chiều": $r(y)=\beta\log\dfrac{\pi^*(y)}{\pi_{\mathrm{ref}}(y)}+\beta\log\mathcal Z$
  - "Trên ví dụ, với $r=\hat r$ và $\beta=1$: $\log1{,}2+\log\tfrac53=0{,}18+0{,}51=0{,}69=\hat r(y_1)$. Hiệu hai câu: $\log1{,}2-\log0{,}6=\log2$, không chứa $\mathcal Z$." (công thức nội dòng, không thêm dòng hiển thị)
  - Hộp như trên.
- **Hình:** không hình riêng; lý do: trang là một dẫn xuất ba dòng dựng dần, cột nhãn và mũi tên chú thích là phần trực quan (mẫu CS234). Ngoại lệ TB12 có lý do: ba dòng hiển thị, dựng dần, mỗi dòng một nhãn bước (TB12 cho phép dẫn xuất nhiều dòng dựng dần).
- **Dựng dần:** (0) hàng 1; (1) hàng 2; (2) hàng 3 với $\beta\log\mathcal Z$ tô tím; (3) dòng ví dụ; (4) hộp.
- **Ghi chú diễn giả:** "Hàng ba nói: mỗi chính sách là nghiệm có phạt KL của phần thưởng $\beta\log(\pi/\pi_{\mathrm{ref}})$, cộng một hằng chỉ phụ thuộc lời nhắc (Mệnh đề 10.63). Bradley–Terry chỉ dùng hiệu phần thưởng giữa hai câu của cùng lời nhắc, nên hằng đó không bao giờ cần tính."
- **Nguồn:** §7.4 đoạn mở (phép tính trên ví dụ); Mệnh đề 10.63 (câu lời thường).
- **Bố cục:**

```
┌──────────────────────────────────────────────────────────────┐
│ Đổi biến: phần thưởng viết theo chính sách                   │
├────────────────────┬─────────────────────────────────────────┤
│ mục tiêu có phạt KL│ max_π E_π r − β KL(π‖π_ref)        (0)   │
│ nghiệm             │ π* = π_ref e^{r/β} / Z              (1)   │
│ đổi chiều          │ r = β log(π*/π_ref) + [β log Z]tím  (2)   │
├────────────────────┴─────────────────────────────────────────┤
│ Trên ví dụ: log(0,8/(2/3)) + log(5/3) = 0,69 = r̂(y₁) …  (3)  │
│ [hộp] Trong phép so sánh hai câu, β log Z triệt tiêu.   (4)  │
└──────────────────────────────────────────────────────────────┘
```

#### `L10-6-07` · DPO học thẳng chính sách bằng hồi quy logistic

- **Câu:** 6 ("DPO (một hàm mất mát phân loại)"). **Biết thêm:** hàm mất mát DPO là mất mát Bradley–Terry với phần thưởng ngầm của chính sách; trên ví dụ, các bước đưa $\pi(y_1)$ từ $0{,}67$ về $0{,}8$.
- **1 phút:** Thay $\hat r$ trong mất mát Bradley–Terry bằng $\beta\log(\pi_\theta/\pi_{\mathrm{ref}})$ được một hồi quy logistic trên chính sách; các bước hạ gradient đưa $\pi(y_1)$ từ $0{,}67$ lên $0{,}74$, $0{,}77$, rồi $0{,}795$ sau năm bước, tiến về $0{,}8$.
- **Mới:** hàm mất mát DPO.
- **Ý chính:** tiêu đề; hình.
- **Mặt trang** (≈ 35 âm tiết):
  - "Tối ưu ưu tiên trực tiếp (Direct Preference Optimization, DPO) cực tiểu hóa, trên mọi lần so sánh với câu được chọn $y_w$ và câu bị loại $y_l$:"
    $$L^{\mathrm{DPO}}=-\,\text{trung bình}\ \log\sigma\Bigl(\underbrace{\beta\log\tfrac{\pi_\theta(y_w)}{\pi_{\mathrm{ref}}(y_w)}}_{\text{phần thưởng ngầm của câu được chọn}}-\underbrace{\beta\log\tfrac{\pi_\theta(y_l)}{\pi_{\mathrm{ref}}(y_l)}}_{\text{của câu bị loại}}\Bigr)$$
  - "Bước học $1$ từ $\pi_\theta=\pi_{\mathrm{ref}}$: $\pi_\theta(y_1)=0{,}67\to0{,}74$."
- **Hình:** đồ thị $\pi_\theta(y_1)$ theo số bước $0$–$5$: sáu điểm nối nét liền, chỉ ghi nhãn ở bước $0$ ($0{,}67$), $1$ ($0{,}74$), $2$ ($0{,}77$), $5$ ($0{,}795$) cùng mũi tên "$\to0{,}8$"; đường ngang tím nét đứt ở $0{,}8$, nhãn "$\pi^*(y_1)=0{,}8$". Khoảng 40%, nửa dưới bên phải. Tệp `dpo-cac-buoc.svg`.
- **Dựng dần:** (0) câu tên và công thức; (1) dòng bước một và điểm bước $0$, $1$; (2) các điểm còn lại và đường $0{,}8$.
- **Ghi chú diễn giả:** "Bước đầu: mọi trọng số bằng $\sigma(0)=\tfrac12$, gradient theo logit là $(-\tfrac16;\tfrac16)$, nên logit của $y_1$ tăng $\tfrac16$, của $y_2$ giảm $\tfrac16$. DPO chỉ cần hai mô hình, chính sách và mô hình tham chiếu, và không sinh câu mới trong lúc học. Cực tiểu của $L^{\mathrm{DPO}}$ là $0{,}6365$, đúng cực tiểu của mất mát Bradley–Terry."
- **Nguồn:** Định nghĩa 10.64; Ví dụ 10.28 (bước một, bước 2–5, cực tiểu); Mệnh đề 10.66 (ở lại ghi chú).

#### `L10-6-08` · Hai con đường tới cùng chính sách $(\tfrac45;\,\tfrac15)$

- **Câu:** 6 (trạm dừng cuối của phần chính). **Biết thêm:** RLHF và DPO là hai cách đi tới cùng nghiệm, khác nhau ở số mô hình và dữ liệu; điều kiện quyết định.
- **1 phút:** Từ cùng sáu lần chọn, đường trên đi qua mô hình phần thưởng và PPO, đường dưới đi thẳng bằng DPO; cả hai gặp nhau ở $(\tfrac45;\,\tfrac15)$.
- **Mới:** không (gom ý). **Ý chính:** tiêu đề; câu "Điều kiện quyết định: mỗi cặp câu được chọn theo cả hai chiều ít nhất một lần."
- **Mặt trang** (≈ 25 âm tiết ngoài hình): câu điều kiện quyết định.
- **Hình:** sơ đồ neo `so-do-neo-m6-ra.svg`: từ khung "so sánh của người", đường liền đi qua ① (mô hình phần thưởng, trừ phạt KL) → ② → ③ (critic) → ④ → ⑤ (PPO), ghi "bốn mô hình, sinh câu trong lúc học"; đường nét đứt "DPO" đi thẳng tới ⑤, ghi "hai mô hình, dữ liệu cố định"; hai đường gặp ở khung đậm "$\pi^*=(\tfrac45;\,\tfrac15)$". Khoảng 60%.
- **Dựng dần:** (0) đường trên; (1) đường dưới; (2) khung gặp nhau và câu điều kiện.
- **Ghi chú diễn giả:** "Định lý 10.65 của ghi chú ghép các điều kiện: tập câu trả lời hữu hạn, mô hình tham chiếu dương, chính sách chọn tự do, và mất mát Bradley–Terry có đúng một lớp cực tiểu. Trên ví dụ, điều kiện cuối là có ít nhất một lần chọn mỗi phía. Bảng so sánh đầy đủ hai con đường ở §7.5."
- **Nguồn:** Định lý 10.65 (câu lời thường, câu chuyện mục 5); hình `rlhf-dpo-hai-con-duong.svg` và bảng §7.5 của ghi chú.

#### `L10-6-09` · Câu hỏi nhanh: người luôn chọn một phía

- **Câu:** 6 ("Còn thiếu"). **Biết thêm:** với ưu tiên tất định, cả hai con đường đẩy câu thua về xác suất $0$ với mọi $\beta$; và mỗi con đường hỏng ở đâu ngoài dữ liệu.
- **1 phút:** Sáu trên sáu chọn $y_1$ thì đường ngang ở $1$ không bao giờ gặp đường cong $\sigma$: hiệu phần thưởng tăng vô hạn, $\pi^*\to(1;\,0)$.
- **Mới:** không. **Ý chính:** hộp "Lời giải:".
- **Mặt trang** (≈ 55 âm tiết):
  - Hộp "Câu hỏi: Nếu cả sáu lần người đều chọn $y_1$, $\hat r$ và $\pi^*$ ra sao?"
  - Hộp "Lời giải: Hiệu $\hat r(y_1)-\hat r(y_2)$ tăng vô hạn, nên $\pi^*\to(1;\,0)$ với mọi $\beta$. DPO cũng đẩy $\pi_\theta(y_2)$ về $0$."
  - "Còn thiếu: DPO không đánh giá câu trả lời ngoài dữ liệu. RLHF đánh giá chúng bằng $\hat r$, có thể sai ở đó."
- **Hình:** đường $\sigma$ của `L10-6-02` (thu nhỏ, khoảng 35%), thêm đường ngang đỏ nét đứt ở $1$, nhãn "tỉ lệ $\tfrac66$", không cắt đường cong.
- **Dựng dần:** (0) câu hỏi và hình; (1) lời giải; (2) dòng "Còn thiếu".
- **Ghi chú diễn giả:** "Sáu lần chọn cùng một phía là chuyện thường khi dữ liệu ít. Phạt KL không cứu được, vì phần thưởng khớp được đã vô hạn. Gheshlaghi Azar và cộng sự lập luận rằng RLHF thực tế tránh được nhờ mô hình phần thưởng được điều chuẩn, nhưng đó không phải định lý. Tình huống 10.5 của ghi chú phân tích trường hợp này."
- **Nguồn:** Mệnh đề 10.54(c); Nhận xét 10.69 ý 2, 3; Tình huống 10.5; câu chuyện mạch 6 (câu hỏi nhanh).

### Mạch 7. Tổng kết (`id="mach-7"`, 8 trang, 9 phút)

Theo TB21: sơ đồ neo lần cuối; trả lời câu hỏi trung tâm bằng ba câu khẳng định; câu hỏi tự kiểm tra về hành vi trên ví dụ; một bài tổng hợp có lời giải và trang bài tập về nhà; tài liệu tham khảo. Không bảng giả thiết (ở §8.1 của ghi chú). Bảng thẳng hàng các quy tắc cập nhật nằm ngay trên khối ④ và ⑤ của sơ đồ neo cuối (TB21 cho bài nhiều thuật toán cùng khung), không thành trang riêng.

#### `L10-7-00` · Trang tiêu đề mạch 7 (điểm vào mạch 7)

- **Câu:** T. **Biết thêm:** mạch gom ý, không ý mới.
- **1 phút:** Mạch cuối đặt lại năm khối của vòng cập nhật, mỗi khối với một công thức và một con số.
- **Mới:** không. **Ý chính:** dòng dẫn.
- **Mặt trang:** "7." · "Tổng kết" · `p.strand-lead` "Mỗi khối của vòng cập nhật nhận một công thức và một con số." (14 âm tiết).
- **Hình:** `so-do-neo-m7-vao.svg`: cả năm khối tô tím nhạt.
- **Ghi chú diễn giả:** "Năm mạch nội dung đổi lần lượt khối hệ số, khối cập nhật và khối phần thưởng của cùng một vòng. Mạch này gom các thay đổi đó, trả lời hai câu hỏi đầu bài và câu hỏi về so sánh, rồi giao bài tổng hợp trên chuỗi hai trạng thái."
- **Nguồn:** §8 của ghi chú.

#### `L10-7-01` · Vòng cập nhật chính sách sau năm mạch

- **Câu:** T (sơ đồ neo lần cuối). **Biết thêm:** cả bài trên một hình: mỗi khối một công thức chủ chốt và một số của ví dụ chạy; hai dãy thẳng hàng cho hệ số và cho bước cập nhật.
- **1 phút:** Hệ số đi từ $G_t$ tới $\widehat A_t$, phương sai của tọa độ $\theta_A$ từ $0{,}69$ xuống $0$; bước cập nhật đi từ một bước gradient tới mục tiêu cắt; phần thưởng có thể học từ so sánh.
- **Mới:** không. **Ý chính:** hình.
- **Mặt trang:** chữ là nhãn hình (không tính âm tiết):
  - ① "phần thưởng của môi trường, hoặc học từ so sánh và trừ phạt KL: $\pi^*\propto\pi_{\mathrm{ref}}e^{\hat r/\beta}$ · ví dụ $(\tfrac45;\tfrac15)$"
  - ② "thu lượt bằng chính sách cũ"
  - ③ "critic $\hat v$: $\delta_t=R_{t+1}+\gamma\hat v(S_{t+1})-\hat v(S_t)$"
  - ④ dãy thẳng hàng, phần đổi tô tím: "$G_t$ → $G_t-\hat v(S_t)$ → $\delta_t$ → $\widehat A_t=\sum_k(\gamma\lambda)^k\delta_{t+k}$" · dưới dãy: "phương sai của tọa độ $\theta_A$ trên chuỗi $0{,}69$ → $0{,}20$ → $0$ (critic đúng)"
  - ⑤ dãy thẳng hàng: "một bước gradient → tối đa $\mathcal L$ với KL $\le\kappa$ (TRPO) → tối đa $\min(\rho\widehat A,\operatorname{clip}(\rho)\widehat A)$ (PPO)" · dưới dãy: "hàm thay thế báo $+0{,}175$, thật $-0{,}05$ · trên $s_B$ dừng ở $p=0{,}8$"
  - mũi tên nét đứt "DPO" từ "so sánh của người" tới ⑤.
- **Hình:** `so-do-neo-m7.svg`, khoảng 80% thân trang. Nhãn ≥ 20 px trên ảnh 1600×900; nếu không đủ chỗ, rút số của ví dụ trước, không thu chữ.
- **Dựng dần:** (0) năm khối trống nhãn mới; (1) dãy ④; (2) dãy ⑤; (3) ① và mũi tên DPO.
- **Ghi chú diễn giả:** "Đọc theo vòng. Khối ④ là câu trả lời cho dao động: so với giá trị của trạng thái, đánh giá bằng critic, trộn bằng $\lambda$. Khối ⑤ là câu trả lời cho bước dài: đoán bằng hàm thay thế, chỉ tin trong miền gần, giữ gần bằng KL hay bằng phép cắt. Khối ① đổi khi không có phần thưởng. PPO dùng ④ dạng GAE và ⑤ dạng cắt."
- **Nguồn:** câu chuyện mục 3 (bảng trạng thái sơ đồ neo, hàng 7); §8.2 của ghi chú (quy tắc cập nhật).

#### `L10-7-02` · Vấn đề trung tâm

- **Câu:** T (trả lời câu hỏi trung tâm). **Biết thêm:** ba câu trả lời có điều kiện, nói bằng lời.
- **1 phút:** Hai câu hỏi đầu bài (và câu hỏi về so sánh) có ba câu trả lời, mỗi câu nói rõ điều kiện quyết định.
- **Mới:** không. **Ý chính:** ba câu.
- **Mặt trang** (≈ 95 âm tiết, trang tổng kết): dòng xám nhắc hai câu hỏi của `L10-1-06`; rồi:
  1. "Trừ khỏi lợi tức một mức chỉ phụ thuộc trạng thái giữ trung bình của gradient và giảm dao động. Critic và GAE giảm dao động thêm, nhưng lệch khi critic sai và $\lambda<1$."
  2. "Hàm thay thế đoán đúng $J$ của chính sách mới khi chính sách mới gần chính sách cũ. TRPO giữ bước trong một miền KL, PPO cắt tỉ số xác suất. Cả hai cho bước lớn hơn REINFORCE, nhưng không bảo đảm $J$ tăng."
  3. "Khi chỉ có so sánh của người, RLHF và DPO cùng nhắm tới $\pi^*\propto\pi_{\mathrm{ref}}e^{\hat r/\beta}$, nếu mỗi cặp câu được chọn theo cả hai chiều."
- **Hình:** không; lý do: trang câu trả lời (TB21 (2)); hình tổng ở trang trước.
- **Dựng dần:** fragment theo ba câu.
- **Ghi chú diễn giả:** "Câu 1 ứng với mạch 2, 3; câu 2 với mạch 4, 5; câu 3 với mạch 6. Bảng kết quả và giả thiết đầy đủ ở §8.1 của ghi chú; trên lớp, chỉ cần nhớ điều kiện quyết định của mỗi câu: mức trừ không phụ thuộc hành động, chính sách mới gần chính sách cũ, mỗi cặp được chọn theo cả hai chiều."
- **Nguồn:** §8.3 của ghi chú (sáu phần, gom thành ba câu).

#### `L10-7-03` · Bài tập: một vòng PPO-Clip trên chuỗi hai trạng thái

- **Câu:** T (bài tổng hợp nối mạch 2, 4, 5; quyết định 6). **Biết thêm:** đề bài tổng hợp.
- **1 phút:** Chạy một vòng PPO-Clip trên chính chuỗi của bài: tìm chính sách nơi vòng dừng, rồi so mức tăng mà hàm thay thế đoán với mức tăng thật.
- **Mới:** không. **Ý chính:** hộp "Câu hỏi:".
- **Mặt trang** (≈ 70 âm tiết, trang đề):
  - Hộp "Câu hỏi: Chuỗi hai trạng thái, chính sách cũ $(\tfrac12;\,\tfrac23)$, lợi thế đúng $(0{,}4;\,-0{,}4)$ ở $s_A$ và $(1;\,-2)$ ở $s_B$. Một vòng PPO-Clip với $\epsilon=0{,}2$ tăng mục tiêu cắt tới đầu đoạn phẳng, các mẫu có đúng tần suất của chính sách cũ. (a) Vòng dừng ở chính sách nào? (b) Hàm thay thế đoán $J$ tăng bao nhiêu? $J$ thật tăng bao nhiêu?"
- **Hình:** chuỗi thu nhỏ `chuoi-loi-the.svg` (khoảng 30%), để có lợi thế trên các cung.
- **Dựng dần:** không.
- **Ghi chú diễn giả:** "Bài kiểm ba năng lực: tìm mốc cắt theo dấu lợi thế, tính hàm thay thế bằng bảng của mạch 4, và tính $J$ thật. Gợi ý: tham số của hai trạng thái tách nhau, nên xét từng trạng thái; khi $p$ tăng, tìm lúc từng nhóm mẫu chạm biên. Câu (c), (d) của bài đầy đủ ở Bài tập 10.23 trong ghi chú."
- **Nguồn:** Bài tập 10.23 (câu (a), (b); gợi ý).

#### `L10-7-04` · Bài tập: một vòng PPO-Clip trên chuỗi hai trạng thái, lời giải

- **Câu:** T. **Biết thêm:** lời giải từng bước; hàm thay thế đoán thấp hơn mức tăng thật $0{,}036$, đúng số hạng tích của mạch 4.
- **1 phút:** Vòng dừng ở $(0{,}6;\,0{,}8)$; hàm thay thế đoán $0{,}26$, thật $0{,}296$; phần chênh $0{,}036$ là số lần thăm $s_B$ tăng thêm, ở nơi chính sách mới tốt hơn.
- **Mới:** không. **Ý chính:** dòng "Kết luận:" ngoài bảng, chữ lớn.
- **Mặt trang** (≈ 60 âm tiết ngoài bảng, trang lời giải):
  - "Lời giải:"
  - Bảng (mỗi hàng một trạng thái):

    | Trạng thái | Tỉ số | Mốc cắt | Dừng ở |
    |---|---|---|---|
    | $s_A$ | $\rho(1)=2p_A$, $\rho(2)=2(1-p_A)$ | cùng chạm $1{,}2$ và $0{,}8$ tại $p_A=0{,}6$ | $p_A=0{,}6$ |
    | $s_B$ | $\rho(1)=1{,}5p_B$, $\rho(2)=3(1-p_B)$ | $0{,}73$ rồi $0{,}8$, như mạch 5 | $p_B=0{,}8$ |
  - "(b) Hàm thay thế: $0{,}8\cdot0{,}1+1{,}35\cdot\tfrac2{15}=0{,}08+0{,}18=0{,}26$. $J$ thật: $2{,}7\cdot0{,}6\cdot0{,}8+0{,}4=1{,}696$, tăng $0{,}296$."
  - "Kết luận: hàm thay thế đoán thấp $2{,}7\cdot0{,}1\cdot\tfrac2{15}=0{,}036$, vì chính sách mới tới $s_B$ nhiều hơn và tốt hơn ở đó."
- **Hình:** không; lý do: lời giải theo bảng hai trạng thái, hình của mục tiêu cắt tại $s_B$ đã có ở `L10-5-04`.
- **Dựng dần:** (0) hàng $s_A$; (1) hàng $s_B$; (2) dòng (b); (3) kết luận.
- **Ghi chú diễn giả:** "Tại $s_A$, hai nhóm mẫu chạm biên cùng lúc vì chính sách cũ chọn hai hành động bằng nhau. Mục tiêu cắt tại điểm dừng là $0{,}2$, thấp hơn hàm thay thế $0{,}26$: phép cắt luôn bi quan. Lỗi hay gặp: dừng ở $p_B=0{,}73$, nơi chỉ mẫu hành động 2 chạm biên."
- **Nguồn:** Bài tập 10.23, lời giải câu (a), (b), (d).

#### `L10-7-05` · Câu hỏi tự kiểm tra

- **Câu:** T. **Biết thêm:** ba câu hỏi về hành vi trên ví dụ, tự trả lời được bằng phép tính của bài.
- **1 phút:** Ba câu, mỗi câu một mạch, hỏi một con số trên chuỗi hoặc trên $s_B$.
- **Mới:** không. **Ý chính:** danh sách.
- **Mặt trang** (≈ 75 âm tiết):
  - "Câu hỏi: trả lời bằng phép tính trên các ví dụ của bài."
  1. "Trên chuỗi với critic $(1{,}4;\,1)$ và $\lambda=0{,}8$, hai lượt (i), (ii) cho hệ số GAE tại bước $0$ bằng bao nhiêu? Trung bình lệch bao nhiêu so với $0{,}4$?"
  2. "Bước $(0{,}5;\,1)$ chỉ đổi $p_B$. Vì sao hàm thay thế đoán đúng $\Delta J$, dù bước xa?"
  3. "Trên $s_B$ với $\epsilon=0{,}1$, mục tiêu cắt hết tăng từ $p$ nào?"
- **Hình:** không; lý do: trang câu hỏi.
- **Dựng dần:** không.
- **Ghi chú diễn giả:** "Lời giải ngắn, cho sinh viên tự kiểm: (1) $\gamma\lambda=0{,}72$: $-0{,}5+0{,}72\cdot2=0{,}94$ và $-0{,}5-0{,}72=-1{,}22$, trung bình $0{,}22$, lệch $-0{,}18=-0{,}9(1-\lambda)$; (2) $\Delta p_A=0$ nên chính sách mới tới $s_B$ như chính sách cũ, sai số $2{,}7\,\Delta p_A\Delta p_B=0$ và $\Delta J=\Delta\mathcal L=0{,}45$; (3) $p=\tfrac23\cdot1{,}1\approx0{,}73$. Lời giải đầy đủ ở §8.4 của ghi chú (sau khi sửa theo đề xuất G4)."
- **Nguồn:** §8.4 của ghi chú (câu 3; câu 1, 2 theo đề xuất sửa ghi chú G4, mục 11). Câu dẫn theo TB21 (3), bỏ "nêu kết quả đã dùng" của NT-RL-9 (mục 6 của `NGUYEN-TAC-HOC-PHAN.md`).

#### `L10-7-06` · Bài tập về nhà

- **Câu:** T. **Biết thêm:** bài nào thuộc mạch nào, và nơi mở ghi chú và tệp bài tập.
- **1 phút:** Bảng mạch–bài tập và hai liên kết.
- **Mới:** không. **Ý chính:** bảng.
- **Mặt trang** (bảng, ≈ 40 âm tiết):

  | Mạch | Bài tập |
  |---|---|
  | 2. So lợi tức với giá trị của trạng thái | 10.14; ghi chú: 10.1, 10.4, 10.5, 10.10 |
  | 3. Trộn đánh giá một bước và cả lượt | 10.13, 10.15; ghi chú: 10.6, 10.7 |
  | 4. Đánh giá chính sách mới bằng dữ liệu cũ | 10.16, 10.17; ghi chú: 10.8, 10.9, 10.11 |
  | 5. Giữ chính sách mới gần chính sách cũ | 10.14; ghi chú: 10.2, 10.12 |
  | 6. Học từ so sánh của người | 10.22; ghi chú: 10.18–10.21 |
  | 7. Tổng kết | ghi chú: 10.3, 10.23 |

  Dòng liên kết: "Ghi chú bài giảng · Bài tập" (`material-viewer.html?doc=materials/lec-10/lecture-note.md&deck=lecture-10-trpo-va-ppo.html`, `…exercises.md…`).
- **Hình:** không; lý do: trang bảng.
- **Ghi chú diễn giả:** "Bài tập 10.13–10.17 và 10.22 ở tệp bài tập, lấy từ Sutton và Barto; các bài khác ở cuối ghi chú. Bài 10.14 dùng cho cả mạch đường cơ sở và mạch PPO, vì nó là biến điều khiển không đổi kỳ vọng."
- **Nguồn:** bảng mở đầu của `exercises.md`; §8.5 của ghi chú (gộp mạch TRPO vào mạch 4).

#### `L10-7-07` · Tài liệu tham khảo

- **Câu:** T. **Biết thêm:** nguồn của bài và bài tiếp theo.
- **1 phút:** Năm nguồn chính và liên kết sang Bài 11.
- **Mặt trang:**
  - "Sutton, R. S., Barto, A. G. *Reinforcement Learning: An Introduction*, ấn bản 2, 2018, §7.1, §12.1–12.3, §13.4–13.5."
  - "Schulman và cộng sự. Trust Region Policy Optimization, 2015; Generalized Advantage Estimation, 2016; Proximal Policy Optimization Algorithms, 2017."
  - "Ouyang và cộng sự. Training language models to follow instructions with human feedback, 2022."
  - "Rafailov và cộng sự. Direct Preference Optimization, 2023."
  - "Tạ Việt Cường. Bài giảng 10, học phần AIT3007, 2025–2026."
  - "Bài tiếp theo: Bài 11, Lập kế hoạch dựa trên mô hình" (liên kết `lecture-11-lap-ke-hoach-dua-tren-mo-hinh.html`).
- **Hình:** không.
- **Ghi chú diễn giả:** "Danh sách đủ 25 tài liệu và số mục, số trang đã đối chiếu ở cuối ghi chú. Các phần TRPO, GAE, PPO, DPO không có trong sách của Sutton và Barto; đọc thẳng các bài báo, bắt đầu từ mục 2–3 của mỗi bài."
- **Nguồn:** "Hướng dẫn đọc thêm và tài liệu tham khảo" của ghi chú (mục 1, 2, 5, 6, 7, 18, 19).

---

## 6. Danh sách hình mới cho người vẽ

Mọi hình là SVG trong `2627-1/img/lec-10/`, có `role="img"` và `aria-label` (VP10); nhãn ≥ 20 px đo trên ảnh 1600×900 (TB10); màu theo quy ước ở đầu tệp, luôn kèm nét hoặc nhãn (NT25); dấu thập phân là dấu phẩy; chữ trong hình theo VP25. Hình cũ của deck (`central-problem-slide.svg`, `ppo-data-pipeline.svg`, `trpo-trust-region.svg`) không dùng nữa; hình của ghi chú giữ nguyên.

| # | Tệp | Nội dung | Dùng ở |
|---|---|---|---|
| 1 | `hanh-lang-mot-luot.svg` | hành lang bốn ô (vẽ lại `img/lec-09/short-corridor.svg`), ô $s_2$ viền nét đứt "đảo hành động", đường đi của lượt (a) với ba mũi tên đánh số $t=0,1,2$ | `L10-1-03` |
| 2 | `hanh-lang-ba-luot.svg` | trục số $\widehat g_1$ từ $-6$ tới $3$; ba chấm (a) $-1$, (b) $1$, (c) $-5{,}5$ (ba màu, kèm chữ); vạch đỏ ở $2$ "gradient đúng"; ba lớp để dựng dần | `L10-1-04`, thu nhỏ ở `L10-1-06` |
| 3 | `hanh-lang-J-hai-buoc.svg` | đồ thị $J(p)=-2(2-p)/(p(1-p))$ trên $[0{,}2;0{,}95]$, trục tung $[-25;-10]$; điểm $p=0{,}5$ ($-12$), đỉnh $p^*\approx0{,}59$; mũi tên xanh dừng trước đỉnh ở $(0{,}55;\,-11{,}7)$ (bước $0{,}05$), mũi tên đỏ tới $(0{,}88;\,-21{,}3)$, nhãn phép tính cạnh mũi tên; điểm vẽ (không ghi): $J(0{,}3)=-16{,}2$, $J(0{,}4)=-13{,}3$, $J(0{,}7)=-12{,}4$, $J(0{,}8)=-15$, $J(0{,}9)=-24{,}4$ | `L10-1-05`, thu nhỏ ở `L10-1-06`, `L10-4-01` |
| 4 | bộ sơ đồ neo `so-do-neo-*.svg` | một khung năm khối (mục 3), mười bốn trạng thái: `m1` (đủ, hai "?" đỏ, cột tên mạch), `m2-vao`, `m2-ra`, `m3-vao`, `m3-ra`, `m4-vao`, `m4-ra` (⑤ mở thành vòng TRPO bốn khung, mũi tên ②→⑤), `m5-vao`, `m5-ra` (⑤ mở thành vòng PPO), `m6-vao`, `m6-rlhf` (① mở thành "so sánh → $\hat r$ → trừ phạt KL", khung "tinh chỉnh có giám sát → $\pi_{\mathrm{ref}}$"), `m6-ra` (hai con đường gặp ở $\pi^*=(\tfrac45;\tfrac15)$), `m7-vao`, `m7` (mỗi khối một công thức, hai dãy thẳng hàng ở ④, ⑤); vị trí khối giữ nguyên ở mọi trạng thái | `L10-1-08`, mọi `L10-k-00`, `L10-2-08`, `L10-3-05`, `L10-4-09`, `L10-5-07`, `L10-6-05`, `L10-6-08`, `L10-7-01` |
| 5 | `chuoi-gia-tri.svg` | chuỗi hai trạng thái (vẽ lại `two-state-chain.svg`), ô ghi $v_\pi$ kèm phép tính, cung "2, thưởng 1" đỏ nhãn "$1<1{,}4$"; biến thể cung xanh "giờ đẩy $p_A$ lên" | `L10-2-01`–`L10-2-03` |
| 6 | `chuoi-loi-the.svg` | chuỗi, mỗi cung ghi lợi thế với phép tính ($+0{,}4$, $-0{,}4$, $+1$, $-2$); dương nét liền xanh, âm nét đứt đỏ | `L10-2-06`, `L10-7-03` |
| 7 | `critic-mot-buoc.svg` | một bước chuyển $s_A\to s_B$ với $\hat v$ hai đầu, phép tính $\delta$ dưới cung, $\delta_t$ tỏa hai mũi tên tới "actor" và "critic" | `L10-2-07` |
| 8 | `chuoi-critic-sai.svg` | chuỗi thu nhỏ, ô $s_B$ có hai số: "$\hat v=1$" (cam, nét đứt), "$v_\pi=2$" (xanh) | `L10-3-01` |
| 9 | `gae-dong-thoi-gian.svg` | dòng thời gian lượt (i): $s_A\to s_B\to$ kết thúc, $\delta_0=-0{,}5$, $\delta_1=2$ với phép tính, ô trọng số $1$, $\gamma\lambda$ | `L10-3-02` |
| 10 | `gae-tinh-lui.svg` | hình 9 thêm hai mũi tên quay ngược: $\widehat A_1=2$, $\widehat A_0=-0{,}5+0{,}45\cdot2=0{,}4$ | `L10-3-03` |
| 11 | `gae-cat-ngan.svg` | dòng thời gian dừng ở $s_B$, cờ "hết giờ", ô kết thúc mờ nét đứt | `L10-3-04` |
| 12 | `chuoi-ti-le-toi-sB.svg` | chuỗi thu nhỏ và hai thanh ngang "tỉ lệ lượt tới $s_B$": cũ $0{,}5$ (xám), mới $1$ (tím) | `L10-4-01` |
| 13 | `ham-thay-the-tiep-xuc.svg` | theo $t\in[0;1]$: đường cam nét đứt $0{,}175t$, parabol xanh $0{,}175t-0{,}225t^2$; điểm $t=0{,}4$ ("đoán $0{,}07$ · thật $0{,}034$"), $t=1$ ("đoán $0{,}175$ · thật $-0{,}05$", đỏ); trục hoành ghi ba chính sách; biến thể có dải tím "miền tin cậy" ở $t$ nhỏ và phần còn lại mờ | `L10-4-04`, `L10-4-07` |
| 14 | `elip-gradient-tu-nhien.svg` | mặt phẳng $(\Delta_A,\Delta_B)$, elip bán trục theo $\Delta_B$ dài gấp $1{,}6$ lần theo $\Delta_A$; mũi tên "$g$" hướng $(2;3)$ xám, "$F^{-1}g$" hướng $(8;30)$ tím, cả hai tới biên; không số trên trục | `L10-4-08` |
| 15 | `ppo-sB-do-thi.svg` (hai bản b, c) | theo $p\in[\tfrac23;1]$, trục tung $[0;1]$: (b) đường cam nét đứt $3p-2$ và đường gấp khúc xanh, mốc $0{,}73$, $0{,}8$, mức phẳng $0{,}27$, điểm "chính sách cũ" ở $\tfrac23$; không dải "vùng đáng tin" (cổng); (c) thêm hai điểm trên đoạn ngang $p=0{,}8$ "KL $0{,}049$", $p=0{,}85$ "KL $0{,}10$", cả hai "gradient $0$", mũi tên đỏ "tham số vẫn trôi" | `L10-5-04`, `L10-5-06` |
| 16 | `ppo-cat-hai-dau.svg` | hai khung $\widehat A>0$, $\widehat A<0$ theo $\rho$ (vẽ lại `ppo-clipping-signs.svg`, bỏ bốn điểm mẫu), đoạn phẳng tô sọc "gradient $0$", vạch $0{,}8$, $1$, $1{,}2$; biến thể có điểm "?" rồi điểm vuông "$-2{,}6$" ở $\rho=1{,}3$ khung phải | `L10-5-02`, `L10-5-03` |
| 17 | `loi-nhac-hai-cau-tra-loi.svg` | thẻ "lời nhắc", hai thẻ câu trả lời có thanh xác suất $\tfrac23$, $\tfrac13$, bốn và hai dấu chọn | `L10-6-01` |
| 18 | `bradley-terry-sigmoid.svg` | đường $\sigma(z)$, $z\in[-3;3]$; đường ngang $\tfrac23$ gặp tại $z=\log2$; biến thể có đường ngang đỏ ở $1$ "tỉ lệ $\tfrac66$" không cắt | `L10-6-02`, `L10-6-09` |
| 19 | `nghiem-phat-kl-cot.svg` | cột $\pi_{\mathrm{ref}}$ ($\tfrac23$; $\tfrac13$) xám, $\pi^*$ với $\beta=1$ ($0{,}8$; $0{,}2$) tím, hai cột nhạt $\beta=\tfrac12$ ($0{,}89$; $0{,}11$), $\beta=2$ ($0{,}74$; $0{,}26$) | `L10-6-04` |
| 20 | `dpo-cac-buoc.svg` | $\pi_\theta(y_1)$ theo bước $0$–$5$ ($0{,}667$; $0{,}736$; $0{,}768$; $0{,}783$; $0{,}791$; $0{,}795$), nhãn chỉ ở bước $0$, $1$, $2$, $5$ và mũi tên "$\to0{,}8$"; đường ngang tím nét đứt $0{,}8$ "$\pi^*(y_1)$" | `L10-6-07` |
| 21 | `chuoi-bo-dem-hai-luot.svg` | chuỗi thu nhỏ, hai lượt của bộ đệm vẽ bằng hai đường màu: $s_A\to s_B\to$ "thưởng $0$", $s_A\to$ "thưởng $1$" | `L10-5-01` |
| 22 | `phat-kl-duong-J1.svg` | đường $J_1(p)=p\log2-p\log\frac{p}{2/3}-(1-p)\log\frac{1-p}{1/3}$ trên $[\tfrac23;1]$, trục tung $[0{,}25;0{,}55]$; ba điểm: mô hình ban đầu $0{,}462$, tham lam $0{,}288$ (đỏ), đỉnh tím "$\approx0{,}51$" không ghi hoành độ; điểm vẽ: $0{,}483$ ($0{,}7$), $0{,}503$ ($0{,}75$), $0{,}502$ ($0{,}85$), $0{,}474$ ($0{,}9$), $0{,}417$ ($0{,}95$) | `L10-6-03` |

Tổng: 21 hình nội dung mới và bộ sơ đồ neo (một khung, 14 trạng thái). Đề xuất cho người vẽ: dựng bộ sơ đồ neo bằng một script sinh 14 tệp từ một khung chung (trong `tools/courses/rl-plan/`), để vị trí khối trùng nhau tuyệt đối giữa các trang.

---

## 7. Đối chiếu mã trang cũ → mới

Deck cũ có 136 mã, tám mạch (`L10-1xx` … `L10-6xx`, `L10-Dxx`, `L10-7xx`). "bỏ" nghĩa là nội dung ở lại ghi chú (câu chuyện mục 5, "Ở lại ghi chú"); số trong ngoặc là khối của ghi chú.

| Mã cũ | Mã mới | Ghi chú |
|---|---|---|
| `L10-101` | `L10-1-01` | bìa, luận điểm mới |
| `L10-102`, `L10-103` | `L10-1-02` | chỉ hai công thức của mạch 1 |
| `L10-104`, `L10-104b` | `L10-1-07` | năm dòng lời thường |
| `L10-105` | `L10-1-08` | nội dung cùng sơ đồ neo |
| `L10-107`, `L10-107b` | `L10-1-03` | bảng từng bước của một lượt |
| `L10-107c` | `L10-1-04` | ba lượt; số của lượt (c) ở ghi chú diễn giả |
| `L10-108` | `L10-1-05` | |
| `L10-109` | `L10-1-06` | |
| `L10-110` | bỏ | thay bằng sơ đồ neo `L10-1-08` |
| `L10-200` | `L10-2-00` | |
| `L10-201`, `L10-203` | `L10-2-01`, `L10-2-02` | |
| `L10-204` | `L10-2-04` | |
| `L10-205` | `L10-2-05` | chứng minh thành ý tưởng chứng minh |
| `L10-207`, `L10-208` | `L10-2-06` | |
| `L10-209` | bỏ | Thuật toán 10.6; dòng ④ của sơ đồ neo |
| `L10-210` | bỏ | Bài tập 10.1; câu hỏi nhanh `L10-2-03` thay |
| `L10-212`, `L10-212b`, `L10-213` | `L10-2-07` | |
| `L10-214`, `L10-214b` | `L10-2-01` | |
| `L10-214c` | `L10-2-06` | |
| `L10-214d`, `L10-214e` | bỏ | Ví dụ 10.7 (hai bước actor–critic) |
| `L10-214f` | `L10-2-08` | |
| `L10-215` | bỏ | Thuật toán 10.9; dòng ④ của sơ đồ neo |
| `L10-300` | `L10-3-00` | |
| `L10-302`, `L10-303` | `L10-3-02` | |
| `L10-304` | `L10-3-02`, `L10-3-03` | dạng tổng; truy hồi |
| `L10-306` | `L10-3-05` | |
| `L10-307`, `L10-307b`, `L10-307c` | bỏ | Ví dụ 10.10; câu hỏi nhanh `L10-3-04` trên chuỗi thay |
| `L10-308` | `L10-3-03` | Thuật toán 10.16 ở ghi chú |
| `L10-309`, `L10-309b` | bỏ | Bài tập 10.7 |
| `L10-400` | `L10-4-00` | |
| `L10-401` | `L10-4-01` | |
| `L10-403` | `L10-4-02` | |
| `L10-404` | bỏ | chứng minh Bổ đề 10.19 |
| `L10-405` | `L10-4-03` | |
| `L10-406` | `L10-4-04` | |
| `L10-407` | `L10-4-06`, `L10-4-07` | TV ở khối chặn cải thiện; KL ở miền tin cậy |
| `L10-408` | `L10-4-06` | |
| `L10-409` | bỏ | chứng minh Định lý 10.26 |
| `L10-410`, `L10-410b`, `L10-410c` | `L10-4-02`, `L10-4-03`, `L10-4-05` | |
| `L10-410d` | `L10-4-06` | dòng "Ý nghĩa" |
| `L10-411`, `L10-412`, `L10-412b` | `L10-4-07` | Hệ quả 10.29, 10.31 thành một câu |
| `L10-413`, `L10-414`, `L10-414b`, `L10-414c` | bỏ | Bài tập 10.11 |
| `L10-500` | bỏ | mạch TRPO gộp vào mạch 4 (quyết định 2) |
| `L10-502`, `L10-502b`, `L10-503` | `L10-4-08` | |
| `L10-505`, `L10-505b`, `L10-505c` | bỏ | Ví dụ 10.16 |
| `L10-506`, `L10-507`, `L10-508` | `L10-4-09` | |
| `L10-509`, `L10-510`, `L10-510b` | bỏ | Bài tập 10.8 |
| `L10-600` | `L10-5-00` | |
| `L10-601` | `L10-5-01` | hiện tượng mới (bộ đệm hai lượt trên chuỗi), sửa theo cổng |
| `L10-603`, `L10-604` | `L10-5-02` | |
| `L10-606` | `L10-5-04` | |
| `L10-607`, `L10-608` | bỏ | PPO-Penalty, một câu ở ghi chú diễn giả `L10-5-06` |
| `L10-609` | `L10-5-07` | |
| `L10-610`, `L10-610b`–`L10-610e` | bỏ | Ví dụ 10.20; số ở ghi chú diễn giả `L10-5-04`–`L10-5-07` |
| `L10-611`, `L10-611b` | `L10-5-06` | |
| `L10-612`, `L10-613` | `L10-5-07` | |
| `L10-615`, `L10-617b`, `L10-618` | bỏ | §6.4–6.6 |
| `L10-616` | `L10-5-08` | |
| `L10-619`, `L10-620`, `L10-620b` | bỏ | Bài tập 10.12 |
| `L10-D00` | `L10-6-00` | |
| `L10-D01` | `L10-6-01` | |
| `L10-D02`, `L10-D02b` | `L10-6-02` | |
| `L10-D03` | `L10-6-03` | |
| `L10-D04`, `L10-D06` | `L10-6-04` | |
| `L10-D05` | bỏ | ý tưởng chứng minh Định lý 10.57 (một trang ý tưởng chứng minh mỗi bài) |
| `L10-D07`, `L10-D07b` | bỏ | dạng mức token, Bổ đề 10.59 |
| `L10-D08`, `L10-D09` | `L10-6-05` | chỉ phần PPO đứng yên ở $\pi^*$ |
| `L10-D10` | `L10-6-06` | |
| `L10-D11`, `L10-D14`, `L10-D15` | `L10-6-07` | |
| `L10-D12`, `L10-D16` | `L10-6-08` | |
| `L10-D13` | bỏ | ý tưởng chứng minh Định lý 10.65 |
| `L10-D17` | `L10-6-09` | |
| `L10-D18` | bỏ | Bài tập 10.18 |
| `L10-700` | `L10-7-00` | `id="mach-8"` thành `id="mach-7"` |
| `L10-701`, `L10-702`, `L10-702b`–`L10-702d`, `L10-703`, `L10-703b`, `L10-704`, `L10-704b` | `L10-7-01` | bảng ở §8.1–8.2 của ghi chú |
| `L10-705`, `L10-706` | bỏ | Tình huống 10.1 |
| `L10-707` | `L10-7-02` | |
| `L10-708` | `L10-7-05` | |
| `L10-709` | `L10-7-06` | |
| `L10-710` | `L10-7-07` | |
| (không có) | `L10-2-03`, `L10-3-01`, `L10-3-04`, `L10-4-05`, `L10-5-03`, `L10-5-05`, `L10-7-03`, `L10-7-04` | trang mới (câu hỏi nhanh, hiện tượng, trạm dừng, bài tổng hợp) |

### Liên kết sâu cần sửa (không thuộc phạm vi tệp này; ghi để điều phối viên giao)

- `materials/lec-10/exercises.md`, bảng mở đầu (dòng 7–14): liên kết `lecture-10-trpo-va-ppo.html#/N/1` theo chỉ số mạch, không theo `data-slide-id`. Với bảy mạch, bảng thành bảy hàng:

  | Mạch | Mở phần | Bài tập |
  |---|---|---|
  | 1. Mở đầu | `#/1/1` | — |
  | 2. So lợi tức với giá trị của trạng thái | `#/2/1` | 10.14; ghi chú: 10.1, 10.4, 10.5, 10.10 |
  | 3. Trộn đánh giá một bước và cả lượt | `#/3/1` | 10.13, 10.15; ghi chú: 10.6, 10.7 |
  | 4. Đánh giá chính sách mới bằng dữ liệu cũ | `#/4/1` | 10.16, 10.17; ghi chú: 10.8, 10.9, 10.11 |
  | 5. Giữ chính sách mới gần chính sách cũ | `#/5/1` | 10.14; ghi chú: 10.2, 10.12 |
  | 6. Học từ so sánh của người | `#/6/1` | 10.22; ghi chú: 10.18–10.21 |
  | 7. Tổng kết | `#/7/1` | ghi chú: 10.3, 10.23 |

  Liên kết `#/8/1` cũ sẽ hỏng; `#/5/1`, `#/6/1`, `#/7/1` cũ sẽ trỏ sang mạch khác.
- `index.html` (dòng 323–331): chỉ liên kết tệp deck và trình xem, không có `#/`; tên tệp deck giữ `lecture-10-trpo-va-ppo.html`, nên không cần sửa.
- Ghi chú §8.5 liên kết trình xem, không liên kết trang; không cần sửa.

---

## 8. Chỗ lệch so với câu chuyện đã duyệt và lý do

1. **Tên mạch bằng lời thường.** Câu chuyện đặt tên mạch theo thuật ngữ ("Đường cơ sở và critic", "Ước lượng lợi thế tổng quát", "Hàm thay thế, miền tin cậy và TRPO", "PPO: mục tiêu cắt", "Học từ so sánh: RLHF và DPO"). Tên mạch xuất hiện ở trang "Nội dung" và trang tiêu đề mạch, trước trang dạy thuật ngữ; TB11 cấm thuật ngữ của bài trước trang dạy nó. Storyboard dùng tên bằng lời thường (mục 2); tên phương pháp xuất hiện ở trang dạy nó. Cần điều phối viên chốt (câu hỏi 1). Điều phối viên chấp nhận (2026-11-20); tên mạch 5 đổi thành "Giữ chính sách mới gần chính sách cũ" ("phép cắt" là thuật ngữ của mạch).
2. **Mạch 1 có 8 trang thay vì 7.** Ví dụ hành lang tách thành bảng từng bước của một lượt (`L10-1-03`) và trang ba lượt (`L10-1-04`), theo yêu cầu của tác giả cho `L10-106`, `L10-107` cũ (TB16: sinh viên tự tính lại từng bước).
3. **Mục tiêu học tập năm dòng thay vì bốn** (TB19: 3–5 dòng, mỗi mạch một dòng; bài có năm mạch nội dung). Điều phối viên chấp nhận 2026-11-20; không coi là ngoại lệ của TB13.
4. **Mạch 2: câu hỏi nhanh "trừ $q$" đứng trước mệnh đề**, làm trang thứ ba của chuỗi bảng (`L10-2-01`–`L10-2-03`), để sinh viên thấy giả thiết "không phụ thuộc hành động" trên số trước khi đọc mệnh đề. Ý "critic sai cho $\delta_0=-0{,}5$" của câu chuyện mạch 2 chuyển thành trang mở mạch 3 (`L10-3-01`), vì đó chính là hiện tượng mở mạch 3; mạch 2 kết bằng dòng "Còn thiếu". Thêm trạm dừng giữa mạch ở `L10-2-06`.
5. **Mạch 4: dải miền tin cậy không ghi $\kappa$.** Ghi chú không có KL dọc đường $t$, nên hình chỉ minh họa; số KL dọc đường (đã tính trong `so.py`) không lên trang.
6. **Mạch 5: hình hai khung theo dấu lợi thế** chuyển từ trạm dừng sang trang định nghĩa `L10-5-02` (hình là bằng chứng của định nghĩa) và dùng lại cho câu hỏi nhanh; trạm dừng là đồ thị trên $s_B$ và bảng so sánh.
7. **Mạch 6: sơ đồ ba giai đoạn RLHF và sơ đồ hai con đường vẽ trên sơ đồ neo** (TB2: dùng lại sơ đồ neo), thay cho hai hình riêng.
8. **Mạch 7: bảng thẳng hàng nằm trên sơ đồ neo cuối** (một trang thay hai); câu hỏi tự kiểm tra và bài tập về nhà tách hai trang (bảng sáu hàng cùng ba câu hỏi không vừa một trang). Mạch 7 có 8 trang thay vì 7.
9. **Số trang:** 56 đếm, 60 thật (câu chuyện: 56, 60). Sau cổng: thêm `L10-5-05`.
10. **Ví dụ 10.13** (cùng bước logit, KL $0{,}12$ và $0{,}0037$) chỉ ở ghi chú diễn giả `L10-4-08`; trang đã có lý do trên chuỗi ($s_B$ ít được tới). Đề xuất 8 của câu chuyện (gọi trạng thái của Ví dụ 10.13 là $s_B$) chưa có trong ghi chú; storyboard không phụ thuộc vào nó.
11. **Mạch 5, hiện tượng mở mạch (cổng, nghiêm trọng).** Trên $s_B$ đứng riêng, hàm thay thế mẫu bằng đúng $J-J_{\mathrm{old}}$, nên "tăng mãi" không phải lỗi. Với lợi thế đúng, tối đa hàm thay thế trên chính sách dạng bảng là bước cải thiện chính sách tham lam và không làm $J$ giảm; vì vậy hiện tượng đúng phải đến từ lợi thế ước lượng (cách (b) của điều phối viên). Hiện tượng mới: chuỗi, critic $(1{,}4;1)$, $\lambda=1$, bộ đệm hai lượt; không cắt, $J$ giảm $0{,}4$; có cắt, giảm $0{,}008$ (`L10-5-01`, trang mới `L10-5-05`). Cần sửa ghi chú trước (G2, G3, mục 11). Câu 5 của câu chuyện bài và câu chuyện mạch 5 đổi theo (mục 1, mục 2).
12. **Mạch 1, bước nhỏ:** bước học $0{,}1$ của ghi chú cho $p\approx0{,}599$, đã qua đỉnh $p^*\approx0{,}586$; storyboard dùng bước $0{,}05$ ($p\approx0{,}55$, $J\approx-11{,}7$) theo đề xuất G1.
13. **Mạch 4, câu hỏi nhanh:** đổi sang bước gần $(0{,}6;\,0{,}7)$ (sai số $0{,}009$); câu hỏi về bước $(0{,}5;\,1)$ chuyển thành câu tự kiểm tra 2, hỏi đúng lý do (G4).
14. **Mạch 6:** `L10-6-03` thay bảng ba chính sách bằng đường $J_1(p)$; điểm $(0{,}8;\,0{,}2)$ chỉ hiện ở `L10-6-04`, nơi nó được tính.

---

## 9. Kiểm theo quy tắc trên storyboard (tự kiểm của người viết, chưa thay vai duyệt)

- TB1, TB4: mỗi trang có dòng "Câu" và "Biết thêm"; đọc lướt các dòng "Biết thêm" của một mạch cho một lập luận. Không trang nào thiếu câu.
- TB2: sơ đồ neo ở `L10-1-08`, trên sáu trang tiêu đề mạch, ở sáu trạm dừng hoặc trang thuật toán (`L10-2-08`, `L10-3-05`, `L10-4-09`, `L10-5-07`, `L10-6-05`, `L10-6-08`) và ở `L10-7-01`.
- TB3: trang mở mỗi mạch (`L10-2-01`, `L10-3-01`, `L10-4-01`, `L10-5-01`, `L10-6-01`) có hình hoặc bảng của ví dụ chạy và hộp "Câu hỏi:"; không định nghĩa, không tên phương pháp mới (`L10-2-01` giới thiệu đối tượng chuỗi, `L10-6-01` đối tượng lời nhắc). Hiện tượng mở mạch 5 có thật trên ví dụ: bộ đệm hai lượt làm $J$ giảm $0{,}4$ (sửa theo cổng).
- TB5: trạm dừng ở mục 2; mỗi mạch kết bằng một trạm dừng (mạch 3 đã đổi thứ tự theo cổng); `L10-2-06`, `L10-6-04` là trang kết quả, không tính là trạm dừng.
- TB7: ba khối "Giả thiết:/Kết luận:", một trang ý tưởng chứng minh; các kết quả khác là một câu lời thường theo câu chuyện mục 5.
- TB11: mỗi trang ghi đúng một phần tử mới; nơi có hai (ký hiệu đi cùng khái niệm của nó, như $\pi_{\mathrm{ref}}$ với $J_\beta$, $y_w$, $y_l$ với hàm mất mát DPO) đã ghi ở mục "Mới". Các trang có thể vượt bốn ký hiệu nội dòng: `L10-1-02`, `L10-4-08`, `L10-6-07` (người dựng đếm trên HTML).
- TB12: ba dòng dẫn xuất dựng dần ở `L10-6-06`, mỗi dòng một nhãn, dòng ví dụ là công thức nội dòng (điều phối viên chấp nhận 2026-11-20).
- TB13: không câu nào trên mặt trang nối hai khẳng định bằng dấu chấm phẩy (dấu chấm phẩy chỉ ngăn tọa độ, theo quy ước của ghi chú); năm dòng mục tiêu theo TB19.
- TB14–TB16: một ví dụ chạy mỗi mạch; mọi số có đường tính trên trang hoặc trang trước; các số chỉ ở ghi chú diễn giả không cần cho mặt trang.
- TB17: ba chuỗi trang cùng bố cục; mọi thuật toán và dẫn xuất từ ba bước dựng dần bằng fragment.
- TB18: tím mang một nghĩa, "đại lượng mới, đang bàn"; đỏ hỏng, cam lệch, xanh đúng (quy ước đầu tệp, sửa theo cổng).
- TB19: hai trang chữ trước ví dụ đầu (bìa, tiên quyết); hiện tượng mở bài đứng trước "Vấn đề trung tâm".
- TB21: mạch tổng kết 8 trang, không bảng giả thiết.
- TB22: sáu câu hỏi nhanh, lời giải ở fragment.
- TB23: mỗi trang có dòng "1 phút".
- NT-RL-10: ghi chú diễn giả của `L10-7-03` nêu năng lực và có "Gợi ý:" (người dựng viết thành dòng mở "Gợi ý:").
- Khung kỹ thuật theo P7 (deck 01), chân trang "Học tăng cường · Học kỳ 1, 2026–2027 · Bài 10", `data-lecture="10"`; không `style=""` trừ khi một trang cần (ghi ngoại lệ NT28).

---


## 10. Câu hỏi cho điều phối viên (sau cổng)

Câu hỏi 1–3 của bản trước đã được trả lời (tên mạch lời thường, mạch 5 đổi tên; câu bìa; năm mục tiêu và ba dòng ở `L10-6-06` được chấp nhận). Còn lại:

1. **Sửa `exercises.md`** (bảng bảy mạch ở mục 7, tên mạch 5 mới): giao cho ai, trong commit nào?
2. **Bộ sơ đồ neo 14 trạng thái:** script sinh SVG trong `tools/courses/rl-plan/` hay vẽ tay?
3. **Đề xuất sửa ghi chú G1–G4 (mục 11)** phải xong, rà toán và commit trước khi viết HTML (quyết định 6 của tác giả: ghi chú sửa trước, cùng số với deck).
4. **Tệp quy tắc:** câu "lưu ý cho người dựng" trong TB15 của `quy-tac-trinh-bay.md` vẫn sai (câu chuyện mục 4.1).

---

## 11. Đề xuất sửa ghi chú (để điều phối viên giao trước khi viết deck)

Số đã tính lại bằng Python (`/tmp/claude-1000/-data-tqlong-lectures/678a7f48-9d80-46cf-a421-67398857f913/scratchpad/deck10/storyboard/sua.py`). Không đánh số khối mới, nên không đổi số hiệu nào của ghi chú.

**G1. §1.1, đoạn "Giới hạn thứ hai", gạch đầu dòng thứ nhất (dòng 173).** Bước nhỏ hiện tại cũng vượt đỉnh ($p=\sigma(0{,}4)=0{,}5987>p^*=0{,}5858$), nên hình không đối lập được hai bước.

- Cũ: "$\alpha=0{,}1$ cho $\theta=(0{,}2;\,-0{,}2)$, $p=\sigma(0{,}4)\approx0{,}60$ và $J\approx-11{,}7$, tức $J$ tăng;"
- Mới: "$\alpha=0{,}05$ cho $\theta=(0{,}1;\,-0{,}1)$, $p=\sigma(0{,}2)\approx0{,}55$, chưa tới $p^*\approx0{,}59$, và $J\approx-11{,}72$, tức $J$ tăng;"
- Số: $\sigma(0{,}2)=0{,}5498$; $J(0{,}5498)=-11{,}718$. Gạch đầu dòng $\alpha=0{,}5$ và câu sau giữ nguyên. Không chỗ nào khác của ghi chú và `exercises.md` dùng $\sigma(0{,}4)$ hay $-11{,}7$.

**G2. §6.1, đoạn mới chèn giữa câu đầu của đoạn mở §6.1 (dòng 1647, "Hàm thay thế mẫu … bảo đảm khớp.") và câu "Về mặt ý tưởng, ta cắt …".** Hiện tượng mở mạch PPO phải có thật; trên bài toán một bước, hàm thay thế mẫu bằng đúng $J-J_{\mathrm{old}}$.

- Mới: "Hàm thay thế cũng chỉ đáng tin khi lợi thế được ước lượng tốt. Trên chuỗi hai trạng thái với critic $\hat v=(1{,}4;\,1)$ của Mục 3 và $\lambda=1$, giả sử bộ đệm chỉ có hai lượt: $s_A\xrightarrow1s_B\xrightarrow2$, với lợi tức $0$, và $s_A\xrightarrow2$, với lợi tức $1$; bộ đệm này xảy ra với xác suất $2\cdot\tfrac16\cdot\tfrac12=\tfrac16$. Lợi thế ước lượng là $0-1{,}4=-1{,}4$ cho hành động 1 tại $s_A$, $1-1{,}4=-0{,}4$ cho hành động 2 tại $s_A$ và $\delta_1=0-1=-1$ cho hành động 2 tại $s_B$, trong khi lợi thế đúng là $0{,}4$, $-0{,}4$ và $-2$. Với $\rho_s(a)=\pi_\theta(a\mid s)/\pi_{\mathrm{old}}(a\mid s)$, hàm thay thế mẫu tại $s_A$ là $\tfrac12\bigl[2p_A\cdot(-1{,}4)+2(1-p_A)\cdot(-0{,}4)\bigr]=-0{,}4-p_A$, và tại $s_B$ là $3(1-p_B)\cdot(-1)$. Cực đại hóa không ràng buộc đẩy $p_A$ về $0$ và $p_B$ về $1$, nơi $J=1$, tức $J$ giảm $0{,}4$ so với $J(\pi_{\mathrm{old}})=1{,}4$. Tại $s_A$, ước lượng với $\lambda=1$ không chệch vì $\hat v(s_A)=v_\pi(s_A)$, nhưng trên một bộ đệm nhỏ nó sai dấu, và hàm thay thế mẫu tuyến tính theo tỉ số nên không có gì giữ bước gần chính sách cũ."
- Số: lượt (ii) của Ví dụ 10.8 cho $G_0-\hat v(s_A)=-1{,}4$, $\delta_1=-1$; $J(0;1)=1$.

**G3. §6.1, đoạn mới sau Ví dụ 10.18 và hình hai khung, trước câu "Mệnh đề sau so mục tiêu cắt với mục tiêu không cắt." (dòng 1728).**

- Mới: "Trở lại bộ đệm hai lượt ở đầu mục, với $\epsilon=0{,}2$. Tại $s_A$, mỗi mẫu có trọng số $\tfrac12$ và cả hai lợi thế ước lượng đều âm, nên theo Mệnh đề 10.40(b), mục tiêu cắt là $\tfrac12\bigl[-1{,}4\max(2p_A;\,0{,}8)-0{,}4\max(2-2p_A;\,0{,}8)\bigr]$. Khi $p_A$ giảm từ $\tfrac12$, mẫu hành động 1 chạm biên $\rho=0{,}8$ tại $p_A=0{,}4$; dưới mức đó, chỉ mẫu hành động 2 còn đổi, theo hướng bất lợi và không bị cắt, nên mục tiêu cắt tại $s_A$ lớn nhất ở $p_A=0{,}4$. Tại $s_B$, mẫu duy nhất đóng góp $-\max(3-3p_B;\,0{,}8)$, nằm ngang từ $p_B=\tfrac{11}{15}\approx0{,}733$. Vòng trong dừng ở $(0{,}4;\,\tfrac{11}{15})$, với $J=2{,}7\cdot0{,}4\cdot\tfrac{11}{15}+0{,}6=1{,}392$: $J$ giảm $0{,}008$, thay cho $0{,}4$ khi không cắt. Phép cắt không sửa lợi thế sai; nó giới hạn mỗi vòng đi bao xa."
- Số: Python cho điểm dừng $p_A=0{,}4$, $p_B=0{,}7334$, $J=1{,}3921$, $\Delta J=-0{,}0079$; với lợi thế đúng, hàm thay thế tại điểm dừng báo $+0{,}01$.

**G4. §8.4 Câu hỏi tự kiểm tra.**

- Câu 1, cũ: "… lượt $s_A\xrightarrow1s_B\xrightarrow1$ cho hệ số GAE tại bước $0$ bằng bao nhiêu khi $\lambda=1$, và khi $\lambda=0$?" (hai số đã có trên trang `L10-3-02`, chỉ kiểm trí nhớ).
- Câu 1, mới: "Trên chuỗi hai trạng thái với critic $\hat v=(1{,}4;\,1)$ và $\lambda=0{,}8$, hai lượt (i), (ii) của Ví dụ 10.8 cho hệ số GAE tại bước $0$ bằng bao nhiêu? Trung bình lệch bao nhiêu so với lợi thế đúng $0{,}4$?" Lời giải ngắn: "$\gamma\lambda=0{,}72$: lượt (i) $-0{,}5+0{,}72\cdot2=0{,}94$, lượt (ii) $-0{,}5-0{,}72=-1{,}22$; trung bình $\tfrac23\cdot0{,}94-\tfrac13\cdot1{,}22=0{,}22$, lệch $-0{,}18=-0{,}9(1-\lambda)$ (Ví dụ 10.8)."
- Câu 2 giữ nguyên (bước $(0{,}6;\,0{,}7)$; deck dùng làm câu hỏi nhanh `L10-4-05`).
- Thêm câu 4: "Trên chuỗi hai trạng thái, bước $(0{,}5;\,1)$ chỉ đổi $p_B$. Vì sao hàm thay thế đoán đúng mức tăng của $J$, dù bước xa chính sách cũ?" Lời giải ngắn: "$\Delta p_A=0$, nên chính sách mới tới $s_B$ với cùng xác suất $0{,}5$ như chính sách cũ, và sai số $2{,}7\,\Delta p_A\Delta p_B$ bằng $0$: $\Delta J=\mathcal L-J=1{,}35\cdot\tfrac13=0{,}45$ (Ví dụ 10.11, 10.12). Hàm thay thế chỉ sai khi chính sách mới đổi nơi nó tới."
- Deck `L10-7-05` dùng câu 1 mới, câu 4, câu 3.

---

## 12. Phác bố cục bổ sung (cổng: các trang có hình, bảng tính hay dựng dần còn thiếu phác)

Khung 1280×720 CSS; nhãn ≥ 16 px CSS (≥ 20 px trên ảnh 1600×900). Các trang `L10-2-03`, `L10-3-03`–`L10-3-05`, `L10-4-01`–`L10-4-03`, `L10-4-05`, `L10-4-07`, `L10-4-09`, `L10-5-01`, `L10-5-04`–`L10-5-07`, `L10-6-03` đã có phác trong mục của trang.

`L10-1-06` · Vấn đề trung tâm

```
┌──────────────────────────────────────────────────────────────┐
│ Vấn đề trung tâm                                             │
├──────────────────────────────┬───────────────────────────────┤
│ [trục số ba lượt, thu nhỏ]    │ [đồ thị J(p) hai bước, thu nhỏ] │
│        dao động              │          bước dài              │
├──────────────────────────────┴───────────────────────────────┤
│ Câu hỏi: 1. Làm sao ước lượng gradient ít dao động hơn?       │
│          2. Làm sao đi bước lớn mà J không giảm?              │
└──────────────────────────────────────────────────────────────┘
```

`L10-2-02` · Trừ giá trị của trạng thái

```
┌──────────────────────────────────────────────────────────────┐
│ Trừ giá trị của trạng thái: trung bình giữ, dao động giảm     │
├──────────────────────────────────────────────────────────────┤
│ [dải chuỗi 110px]                                            │
│ hệ số mới = G_t − b(S_t)   (ngoặc dưới: lợi tức; đường cơ sở)  │
│ Loại lượt   │xs│G₀ │REINF │ trừ v_π: (G₀−1,4)ψ_A        (1)   │
│ s_A→1 s_B→1 │⅓ │2,7│1,35  │ 1,3·0,5=0,65                       │
│ s_A→1 s_B→2 │⅙ │0  │0     │ −1,4·0,5=−0,7                      │
│ s_A→2       │½ │1  │−0,5  │ (−0,4)(−0,5)=0,2 xanh              │
│ tb 0,2 · ps 0,69 · xs âm ½ │ tb 0,2 · ps 0,20 · xs âm ⅙   (2)   │
├──────────────────────────────────────────────────────────────┤
│ [hộp] Trung bình vẫn 0,2. Phương sai giảm từ 0,69 xuống 0,20. │
└──────────────────────────────────────────────────────────────┘
```

`L10-2-06` · Hệ số trung bình là lợi thế

```
┌──────────────────────────────────────────────────────────────┐
│ Hệ số trung bình là lợi thế                                  │
├─────────────────────────┬────────────────────────────────────┤
│ [s_A]─1: 1,8−1,4=+0,4─▶ │ Định nghĩa. Lợi thế … A_π=q_π−v_π     │
│     └─2: 1−1,4=−0,4─▶■  │                                    │
│ [s_B]─1: 3−2=+1──▶■     │ Hệ số G_t−v_π có trung bình A_π …  │
│     └─2: 0−2=−2──▶■     │ ∇J = E[Σ γ^t A_π ψ_t]          (1)  │
│ (dương xanh, âm đỏ đứt)  │ Còn thiếu: q_π và v_π chưa biết. (2)│
└─────────────────────────┴────────────────────────────────────┘
```

`L10-5-03` · Câu hỏi nhanh: mẫu lợi thế âm với $\rho=1{,}3$

```
┌──────────────────────────────────────────────────────────────┐
│ Câu hỏi nhanh: mẫu lợi thế âm với ρ=1,3                       │
├──────────────────────────────┬───────────────────────────────┤
│ Â>0 (khung trái, mờ)          │ Â<0  ▒▒▒▒____                  │
│                              │      0,8    ╲   ?đỏ→■ −2,6 (1) │
│                              │              ╲  ρ=1,3          │
├──────────────────────────────┴───────────────────────────────┤
│ Câu hỏi: Mẫu chọn hành động 2 … có bị cắt không?             │
│ Lời giải: Không. min(−2·1,3; −2·1,2)=−2,6 …               (1) │
└──────────────────────────────────────────────────────────────┘
```

`L10-6-01` · Một lời nhắc, hai câu trả lời, sáu lần chọn

```
┌──────────────────────────────────────────────────────────────┐
│ Một lời nhắc, hai câu trả lời, sáu lần chọn                  │
├──────────────────────────────┬───────────────────────────────┤
│        [ lời nhắc ]           │ Một mô hình ngôn ngữ nhận …    │
│      ↙             ↘          │ Không có hàm phần thưởng.     │
│ [câu trả lời 1] [câu trả lời 2]│ Sáu lần, người đọc hai câu … │
│  ████ ⅔          ██ ⅓         │                               │
│  ✓✓✓✓            ✓✓      (1)  │                               │
├──────────────────────────────┴───────────────────────────────┤
│ Câu hỏi: Mô hình mới nên chọn … Có cần một vòng …?        (2) │
└──────────────────────────────────────────────────────────────┘
```

`L10-6-02` · Khớp phần thưởng để xác suất chọn bằng tỉ lệ $\tfrac46$

```
┌──────────────────────────────────────────────────────────────┐
│ Khớp phần thưởng để xác suất chọn bằng tỉ lệ 4/6              │
├──────────────────────────────┬───────────────────────────────┤
│ Ký hiệu: y₁, y₂ … Bradley–Terry│ 1 ┤          ____               │
│ Pr(y₁ được chọn)=σ(r̂(y₁)−r̂(y₂))│ ⅔ ┤┄┄┄┄┄┄●╱ tỉ lệ 4/6            │
│        └hiệu phần thưởng┘      │   │    ╱┊                     │
│ Hợp lý cực đại: σ(Δr̂)=4/6 …  │ 0 ┼──╱───┊──────── z            │
│ r̂ = (log 2; 0)          (1)   │      Δr̂=log 2           (1)    │
└──────────────────────────────┴───────────────────────────────┘
```

`L10-6-05` · RLHF tìm $\pi^*$ bằng PPO trên phần thưởng đã trừ KL

```
┌──────────────────────────────────────────────────────────────┐
│ RLHF tìm π* bằng PPO trên phần thưởng đã trừ KL               │
├──────────────────────────────────────┬───────────────────────┤
│ [tinh chỉnh có giám sát → π_ref đóng băng]                    │
│ ①[so sánh của người → r̂] → [trừ phạt KL tới π_ref] (tím)     │
│        ↓                              │ bốn mô hình trong bộ  │
│ ②Thu lượt → ③critic → ④Â_t → ⑤PPO ─┐ │ nhớ: π_θ, π_ref, r̂,   │
│ ▲───────────────────────────────────┘ │ critic                │
├──────────────────────────────────────┴───────────────────────┤
│ RLHF chạy PPO với r̃(y) = r̂(y) − β log(π(y)/π_ref(y))    (1)  │
│ Tại π*=(0,8;0,2): r̃(y₁)=0,51, r̃(y₂)=0,51 … PPO đứng yên. (2)  │
└──────────────────────────────────────────────────────────────┘
```

`L10-6-07` · DPO học thẳng chính sách bằng hồi quy logistic

```
┌──────────────────────────────────────────────────────────────┐
│ DPO học thẳng chính sách bằng hồi quy logistic               │
├──────────────────────────────────────────────────────────────┤
│ Tối ưu ưu tiên trực tiếp (DPO) cực tiểu hóa, … y_w, y_l:      │
│ L^DPO = −tb log σ( β log π_θ(y_w)/π_ref(y_w) − β log … )      │
│                    └ph.thưởng ngầm câu được chọn┘ └câu bị loại┘│
├───────────────────────────────┬──────────────────────────────┤
│ Bước học 1 từ π_θ=π_ref:       │0,8 ┄┄┄┄┄┄┄┄┄┄┄┄┄ π*(y₁) tím   │
│ π_θ(y₁)=0,67→0,74         (1)  │    ●0,77 ● ● ●0,795 →0,8      │
│                               │   ●0,74                       │
│                               │  ●0,67   bước 0 1 2 … 5   (2) │
└───────────────────────────────┴──────────────────────────────┘
```

`L10-6-08` · Hai con đường tới cùng chính sách $(\tfrac45;\,\tfrac15)$

```
┌──────────────────────────────────────────────────────────────┐
│ Hai con đường tới cùng chính sách (⅘; ⅕)                     │
├──────────────────────────────────────────────────────────────┤
│ [so sánh của người] ──liền──▶ ①r̂, trừ KL → ② → ③ → ④ → ⑤PPO ─┐ │
│        │                 "bốn mô hình, sinh câu trong lúc học" │ │
│        └┄┄┄┄ DPO (đứt) ┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄▶ ⑤ ──────┤ │
│              "hai mô hình, dữ liệu cố định"                  ▼ │
│                                        [ π* = (⅘; ⅕) ] đậm    │
├──────────────────────────────────────────────────────────────┤
│ Điều kiện quyết định: mỗi cặp câu được chọn theo cả hai chiều… │
└──────────────────────────────────────────────────────────────┘
```

`L10-6-09` · Câu hỏi nhanh: người luôn chọn một phía

```
┌──────────────────────────────────────────────────────────────┐
│ Câu hỏi nhanh: người luôn chọn một phía                      │
├──────────────────────────┬───────────────────────────────────┤
│ 1 ┤┄┄┄┄┄┄┄┄┄┄ đỏ: tỉ lệ 6/6│ Câu hỏi: Nếu cả sáu lần … ra sao?  │
│   │        ____          │ Lời giải: Hiệu r̂(y₁)−r̂(y₂) tăng   │
│ ⅔ ┤┄┄┄┄●╱  (không cắt)    │ vô hạn … π*→(1;0) …          (1)  │
│ 0 ┼──╱──────── z          │                                   │
├──────────────────────────┴───────────────────────────────────┤
│ Còn thiếu: DPO không đánh giá … RLHF đánh giá … có thể sai.(2)│
└──────────────────────────────────────────────────────────────┘
```

`L10-7-01` · Vòng cập nhật chính sách sau năm mạch. Năm khối xếp như sơ đồ neo; ④ và ⑤ là hai khối rộng, mỗi khối một dãy thẳng hàng, phần đổi tô tím, một dòng số nhỏ ở dưới. Ước lượng chiều cao: ① và ② một hàng 90 px; ③ cạnh ④ 150 px; ⑤ 150 px; tổng khoảng 420 px trong thân 560 px, nhãn 18 px CSS.

```
┌──────────────────────────────────────────────────────────────┐
│ Vòng cập nhật chính sách sau năm mạch                        │
├──────────────────────────────────────────────────────────────┤
│ ①phần thưởng của môi trường, hoặc học từ so sánh và trừ KL:   │
│   π*∝π_ref e^{r̂/β} · ví dụ (⅘;⅕)    ──▶ ②thu lượt bằng c.s. cũ │
│ ┄┄ DPO (đứt) từ "so sánh của người" ┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┐      │
│ ③critic v̂:           ④ hệ số: G_t → G_t−v̂ → δ_t → Â_t=Σ(γλ)^kδ │
│  δ_t=R+γv̂(S')−v̂(S) ─▶   tọa độ θ_A: phương sai 0,69→0,20→0     │
│                      ⑤ cập nhật: một bước → max L, KL≤κ (TRPO) │
│                         → max min(ρÂ, clip(ρ)Â) (PPO) ◀┄┄┄┄┄┘  │
│                         đoán +0,175, thật −0,05 · s_B dừng 0,8 │
│ ⑤ ──────────────────────────────────▶ ② (chính sách mới …)    │
└──────────────────────────────────────────────────────────────┘
```

Nếu ảnh 1600×900 cho nhãn dưới 20 px, tách thành hai trang theo TB21: `L10-7-01` sơ đồ neo với một công thức mỗi khối, và một trang "Các bước đổi của hệ số và của bước cập nhật" với hai dãy thẳng hàng; số trang đếm thành 57.

`L10-7-04` · Bài tập, lời giải

```
┌──────────────────────────────────────────────────────────────┐
│ Bài tập: một vòng PPO-Clip trên chuỗi hai trạng thái, lời giải│
├──────────────────────────────────────────────────────────────┤
│ Lời giải:                                                    │
│ Trạng thái │ Tỉ số               │ Mốc cắt            │ Dừng ở │
│ s_A        │ ρ(1)=2p_A, ρ(2)=…   │ cùng chạm tại 0,6  │ 0,6 (0)│
│ s_B        │ ρ(1)=1,5p_B, …      │ 0,73 rồi 0,8       │ 0,8 (1)│
│ (b) Hàm thay thế: 0,08+0,18=0,26. J thật: 1,696, tăng 0,296.(2)│
├──────────────────────────────────────────────────────────────┤
│ Kết luận: hàm thay thế đoán thấp 0,036, vì … (lớn)        (3) │
└──────────────────────────────────────────────────────────────┘
```

---

## 13. Sửa theo cổng (2026-11-20)

Căn cứ: `/tmp/claude-1000/-data-tqlong-lectures/678a7f48-9d80-46cf-a421-67398857f913/scratchpad/deck10/cong-storyboard.md` (kết luận "đạt có điều kiện") và quyết định của điều phối viên. Bản trước cổng: `/tmp/claude-1000/-data-tqlong-lectures/678a7f48-9d80-46cf-a421-67398857f913/scratchpad/deck10/storyboard/storyboard-truoc-cong.md`. Mã trang dưới đây là mã sau khi sửa.

| Phát hiện của cổng (mã cũ) | Mức | Sửa |
|---|---|---|
| `L10-5-01` vấn đề không có thật | nghiêm trọng | Hiện tượng mới trên chuỗi với bộ đệm hai lượt (critic $(1{,}4;1)$, $\lambda=1$): không cắt, $J$ giảm $0{,}4$. Thêm trạm dừng `L10-5-05`: có cắt, vòng dừng ở $(0{,}4;\,0{,}73)$, $J$ giảm $0{,}008$. `L10-5-04` ghi rõ $s_B$ chỉ để xem cơ chế; bỏ dải "vùng đáng tin". Mã cũ `L10-5-05`–`L10-5-07` thành `L10-5-06`–`L10-5-08`. Câu 5 của câu chuyện bài, câu chuyện mạch 5, mục 2, mục 4 sửa theo. Đề xuất ghi chú G2, G3. |
| `L10-1-04` dễ đọc thành "REINFORCE lệch" | nghiêm trọng | Hộp "Mỗi lượt lệch xa $2$. Trung bình trên mọi lượt có thể có vẫn bằng $2$."; vạch $2$ thành xanh, nhãn "= trung bình của mọi lượt"; $\partial p/\partial\theta_1=p(1-p)=\tfrac14$ lên dòng dữ kiện. |
| `L10-4-05` câu hỏi nhanh chỉ ngược thông điệp | nghiêm trọng | Tiêu đề "Bước gần thì hàm thay thế sai ít"; câu hỏi nhanh đổi sang bước $(0{,}6;\,0{,}7)$ (sai số $0{,}009$ so với $0{,}225$); câu về bước $(0{,}5;\,1)$ thành câu tự kiểm tra 2 ở `L10-7-05`, hỏi đúng lý do. Đề xuất G4. |
| `L10-1-05` bước nhỏ cũng vượt đỉnh | trung bình | Bước nhỏ $0{,}05$: $p\approx0{,}55$, trước đỉnh, $J\approx-11{,}7$. Đề xuất G1. |
| "hệ số" chưa định nghĩa | trung bình | `L10-1-02` định nghĩa "hệ số" (số nhân với hàm điểm); cột mạch 2 gọi là "tọa độ $\theta_A$ của $\widehat g$"; tiêu đề `L10-2-08` "Với critic đúng, mọi lượt cho cùng tọa độ $0{,}2$"; `L10-2-01` có hàng "trung bình $0{,}2$ (= gradient đúng)" và phép tính gradient. |
| "phương sai $0$" chỉ đúng ở $\theta_A$ | trung bình | `L10-2-08`, `L10-7-01` ghi "tọa độ $\theta_A$"; `L10-2-08` thêm dòng "phương sai của tọa độ $\theta_B$ giữ $0{,}18$". |
| Mạch 3 không kết bằng trạm dừng | trung bình | Thứ tự mới: `L10-3-01`, `L10-3-02`, `L10-3-03` (tính lùi), `L10-3-04` (câu hỏi nhanh), `L10-3-05` (trạm dừng, sơ đồ neo, "Còn thiếu"). |
| `L10-3-04`, `L10-5-06` (cũ; nay `L10-3-03`, `L10-5-07`) thuật ngữ chưa dạy | trung bình | `L10-3-03`: "Trong cài đặt, mỗi đoạn thu được quét lùi một lần."; `L10-5-07`: nhãn critic "hồi quy về $\widehat A_t+\hat v(S_t)$", entropy "giữ chính sách đủ ngẫu nhiên", $c_1$, $c_2$ gọi tên, epoch và mini-batch kèm tên Việt, bỏ $hN$. |
| `L10-4-01` dữ kiện chưa phải vấn đề | trung bình | Câu lên mặt trang "Chính sách mới tới $s_B$ gấp đôi, và ở $s_B$ nó chọn hành động tốt ít hơn chính sách cũ ($0{,}5<\tfrac23$)." và nhãn đỏ trên thanh. |
| Mạch 4 nhiều ký hiệu | trung bình | Bỏ $\eta$ (số lần tới viết bằng lời), $D_{\mathrm{TV}}$ (lời, định nghĩa ở ghi chú diễn giả), $\bar D_{\mathrm{KL}}$ (viết "KL trung bình"), các số của $F$ (ghi chú diễn giả). |
| `L10-4-06`, `L10-4-07` | trung bình | Phạt viết bằng lời, "hệ số $C$ rất lớn"; câu nối "KL chặn được khoảng cách ở trang trước, và tính được từ lượt cũ."; câu cuối tách hai câu; nhãn "KL ở $s_A$ vô hạn: ngoài mọi miền tin cậy" lên hình. |
| `L10-4-08` số không nguồn | trung bình | Mặt trang chỉ giữ câu "$F$ ở mỗi trạng thái là tần suất tới nhân $p(1-p)$" và hình hướng; các số $F$, $g$, $F^{-1}g$ ở ghi chú diễn giả. |
| `L10-5-05` (nay `L10-5-06`) đọc sai đồ thị | trung bình | Trôi từ $p=0{,}8$ (KL $0{,}049$) tới $0{,}85$ (KL $0{,}10$), cả hai trên đoạn phẳng, gradient $0$. |
| `L10-6-03` số chưa tính | trung bình | Thay bảng bằng đường $J_1(p)$; tiêu đề "Phạt KL chọn một điểm giữa tham lam và mô hình ban đầu"; đỉnh không ghi hoành độ. |
| Màu tím nhiều nghĩa | trung bình | Quy ước đầu tệp: tím = đại lượng mới, đang bàn. |
| Bố cục tràn `2-03`, `3-03`, `4-03`, `4-09`, `7-01`; 20 trang thiếu phác | trung bình | `2-02`, `2-03`: chuỗi thành dải 110 px; `3-05`: ô chỉ ghi kết quả, sơ đồ neo xuống dải dưới; `4-03`: bỏ chuỗi thu nhỏ và cột tích cũ; `4-09`: vòng trong 2×2, nhãn ≤ 6 từ; `7-01`: phác và phương án tách. Phác bổ sung ở mục 12 và trong mục của trang. |
| `L10-1-01` câu bìa | nhẹ | "Sửa hai điểm yếu của REINFORCE, rồi học được cả khi chỉ có so sánh của người." |
| `L10-2-01` nhãn | nhẹ | Nhãn "$\tfrac12\cdot0{,}9\cdot2+\tfrac12\cdot1=1{,}4$"; hàng ba "tăng xác suất hành động 2, dù $1<1{,}4$". |
| `L10-2-06`, `L10-6-04` gọi là trạm dừng | nhẹ | Gọi là trang kết quả; danh sách trạm dừng ở mục 2 sửa. |
| `L10-3-05` (nay `L10-3-04`) | nhẹ | Lời giải thêm "Số này còn lệch vì critic sai … lệch thêm vì bỏ cả tương lai." |
| `L10-6-07` dãy hiển thị | nhẹ | Nhãn ở bước $0$, $1$, $2$, $5$ ($0{,}795$) và "$\to0{,}8$". |
| `L10-6-08` | nhẹ | Đường RLHF đi qua ③. |
| `L10-6-06` | nhẹ | Dòng ví dụ nội dòng, $\log1{,}2$ thay `\dfrac`, ghi "với $r=\hat r$". |
| `L10-7-04` | nhẹ | "Lời giải:". |
| `L10-7-05` | nhẹ | Câu 1 hỏi $\lambda=0{,}8$ (đọc từ quy luật, không nhớ lại số trên trang); câu 2 hỏi lý do của bước $(0{,}5;1)$. |
| `L10-1-08`, `L10-1-07` | nhẹ | "một hoặc hai khối"; mục tiêu 1 bỏ "trên một chuỗi hai trạng thái", mục tiêu 4 "tìm chính sách mà vòng cập nhật dừng lại". |
| Tên mạch 5 | (quyết định) | "Giữ chính sách mới gần chính sách cũ" ở mọi chỗ. |

Số trang sau sửa: 56 đếm, 60 thật; mạch 5 có 9 trang thật (8 đếm), 16 phút; mạch 7 còn 9 phút.

## 14. Sửa theo năm vai rà (2026-11-20, biên tập viên)

Căn cứ: năm báo cáo rà trên bản đóng băng (sinh viên, chuyên gia, toán, sư phạm, mạch truyện) và chín quyết định của điều phối viên. Nhật ký đầy đủ (mỗi phát hiện, quyết định, lý do, trang đổi) ở thư mục rà của phiên. Ghi chú bài giảng và bài tập không đổi.

### 14.1 Mã trang hiện hành (62 trang, 7 mạch)

| Mạch | Mã trang theo thứ tự trình chiếu | Số trang |
|---|---|---|
| 1 | `L10-1-01` … `L10-1-08` | 8 |
| 2 | `L10-2-00` … `L10-2-08` | 9 |
| 3 | `L10-3-00`, `3-01`, `3-02`, `3-05`, `3-04` | 5 |
| 4 | `L10-4-00`, `4-01`, `4-02`, `4-03`, **`4-11`**, `4-04`, `4-05`, `4-10`, `4-06`, **`4-12`**, `4-07`, `4-08`, `4-09` | 13 |
| 5 | `L10-5-00` … `L10-5-08` | 9 |
| 6 | `L10-6-00` … `L10-6-09` | 10 |
| 7 | `L10-7-00` … `L10-7-07` | 8 |

### 14.2 Mã bỏ, thêm, đổi chỗ (cộng dồn từ sau cổng storyboard)

| Mã | Thay đổi | Đợt | Lý do |
|---|---|---|---|
| `L10-3-03` | bỏ | sửa theo người thầy | gộp vào `3-02` (dựng dần tính lùi) |
| `L10-4-10` | thêm sau `4-05` | sửa theo người thầy | tách câu hỏi nhanh bước gần khỏi trạm dừng `4-05` |
| `L10-4-11` | thêm sau `4-03` | năm vai rà | dạy tỉ số chính sách $\rho$ và $\pi_{\mathrm{old}}$ trước khi mạch 5 dùng (quyết định 6; SV, SP, MT) |
| `L10-4-12` | thêm sau `4-06` | năm vai rà | định nghĩa KL bằng công thức và lý do KL vô hạn trước miền tin cậy (quyết định 5) |
| `L10-3-05` ↔ `L10-3-04` | đổi chỗ | năm vai rà | câu hỏi nhanh kiểm lại trạm dừng trên $\lambda$ mới; "Còn thiếu" sang `3-04`; `3-05` thêm sơ đồ neo `m3-ra` (MT) |

Không dùng lại mã đã bỏ. Mạch 4 dài 13 trang: trạm dừng `4-05` (trang 6 của mạch) và `4-09` (cuối mạch).

### 14.3 Trang đổi nội dung mặt trang

`1-01` (luận đề một ý, 20 âm tiết), `1-03`, `1-04`, `1-07`, `2-01`, `2-02`, `2-07`, `3-01`, `3-02`, `3-04`, `3-05`, `4-01`, `4-02`, `4-03`, `4-04`, `4-05`, `4-06`, `4-07`, `4-08`, `4-09`, `4-10`, `5-00`, `5-01`, `5-02`, `5-03`, `5-04`, `5-05`, `5-06`, `5-07`, `5-08`, `6-01`, `6-03`, `6-04`, `6-05`, `6-06`, `6-07`, `6-08`, `6-09`, `7-00`, `7-01` (hình, alt), `7-02`, `7-05`, `7-07`; trang mới `4-11`, `4-12`. Hình đổi (không đổi mã trang): `1-08` (`m1`), `5-00`, `6-00`, `7-00` (thu nhỏ), `6-05` (`m6-rlhf`). Chỉ đổi ghi chú diễn giả: `1-02`, `1-08`, `2-00`, `2-03`, `2-04`, `3-00`, `4-00`.

### 14.4 Mạch 4 sau sửa (câu "sau trang này sinh viên biết thêm")

- `4-11`: hàm thay thế tính được từ hành động của chính sách cũ nhờ tỉ số $\rho=\pi'/\pi_{\mathrm{old}}$ (bảng $s_B$ cho lại $-0{,}5$).
- `4-06`: cận cải thiện bằng lời; khoảng cách biến phân viết ra; thừa số $1/(1-\gamma)^2=100$ làm phạt vượt mức đoán trừ khi bước rất ngắn.
- `4-12`: KL bằng công thức, tính được từ lượt cũ, chặn khoảng cách của định lý; bước $(1;0{,}5)$ có KL vô hạn tại $s_A$ vì bỏ hẳn hành động 2.
- `4-07`: miền tin cậy là bài toán $\max\mathcal L$ với $\overline D_{\mathrm{KL}}\le\kappa$.
- `4-08`: $F_s$ = tần suất tới × $p(1-p)$ có số trên mặt trang; gradient tự nhiên $(8;30)$ dồn về $\theta_B$.
- `4-09`: TRPO ghép ba thứ trên; khung "tính gần đúng gradient tự nhiên", "thu ngắn bước tới khi KL ≤ κ và hàm thay thế tăng" thay "tích $Fv$", "tìm kiếm lùi"; "Còn thiếu" nói chi phí, dẫn vào `5-01` ("Bỏ ràng buộc KL, chỉ chạy Adam").

### 14.5 Ngoại lệ mật độ (âm tiết theo `deck_lint`, sau sửa)

| Trang | Âm tiết | Trần | Lý do |
|---|---|---|---|
| `L10-1-02` | 66 | 60 | không đổi mặt trang trong đợt này; hai công thức tiên quyết |
| `L10-4-06` | 68 | 60 | khối định lý; giữ dòng định nghĩa khoảng cách theo SV, SP |
| `L10-5-08` | 66 | 80 | bảng so sánh |
| `L10-6-01` | 72 | 60 | trang mở mạch có dữ kiện và câu hỏi (bản đóng băng 85) |
| `L10-6-09` | 65 | 60 | thêm điều kiện cả hai chiều theo quyết định 3 |
| `L10-7-02` | 93 | 80 | trang trả lời câu hỏi trung tâm, bốn câu (thêm câu critic/GAE của mạch 3 và "chính sách chọn tự do" theo lượt rà lại; bản đóng băng 117), 1,16 lần trần |
| `L10-7-06` | 63 | 80 | bảng bài tập về nhà |
| `L10-7-07` | 94 | — | danh mục tài liệu, thêm ba bài theo chuyên gia |

### 14.6 Đề xuất sửa ghi chú (NT3, chưa làm)

1. §8.4 câu 3 dùng $\beta=2$, đọc thẳng được từ hình nghiệm có phạt KL; deck hỏi $\beta=4$ (đáp số $(0{,}70;\,0{,}30)$). Đề xuất đổi câu §8.4 theo, hoặc tác giả chọn giữ $\beta=2$ và deck quay lại.
2. Ví dụ 10.23 (tùy chọn): tỉ lệ người chọn $\tfrac46$ trùng xác suất $\tfrac23$ của mô hình; deck bỏ câu phủ định, giữ số. Nếu muốn tránh trùng hẳn, đổi số lần chọn trong ghi chú trước (SP).
3. Bảng thuật ngữ `outline.md`: thêm "lô nhỏ (mini-batch)", "lần qua bộ đệm (epoch)", "chính sách tham chiếu" cho $\pi_{\mathrm{ref}}$ theo cách deck dùng (CG).

### 14.7 Vòng sửa chân trang (2026-11-20)

`footer_check` về 0 bằng bố cục: `1-03`, `2-01`, `3-01` (ảnh 345 px, nhãn hình lớn hơn), `3-05` (bảng gọn một hàng), `4-10` ("Còn thiếu" xuống ghi chú diễn giả), `5-01` (bảng thêm cột $\rho\widehat A$, dòng hàm thay thế mẫu còn một dòng; âm tiết dưới trần), `5-02`, `6-07`. Không đổi số, ý hay mã trang; vẫn 62 trang.

### 14.8 Lượt sửa cuối sau rà lại (2026-11-20)

- `L10-7-02`: bốn câu trả lời: đường cơ sở (giữ $0{,}69\to0{,}20$ và "mức khác có thể làm nó tăng"), critic một bước và GAE trộn bằng $\lambda$ (lệch khi critic sai và $\lambda<1$), hàm thay thế và TRPO/PPO, RLHF ≡ DPO với Bradley–Terry, $\pi_{\mathrm{ref}}$ cố định, dương trên mọi câu, chính sách chọn tự do.
- Nhẹ: `4-11` thêm "(probability ratio)"; `4-06`, `5-04`, `2-01` công thức nội dòng không ngắt; `4-08` viết $1-\gamma=0{,}1$ trên mặt trang, trục elip $\Delta\theta_A$, $\Delta\theta_B$; `4-10` "Còn thiếu" trở lại mặt trang (cột trái); `5-03` "$p_B$"; nhãn "dùng lại / lượt / vừa thu" ba dòng, không đè đường nối (m4-ra, m5-ra, m5/m6/m7-vao, m6-rlhf, m6-ra).
- `exercises.md`: bảng "Mạch | Mở phần | Bài tập" theo 7 mạch, liên kết `#/1/1` … `#/7/1`, bài tập khớp `L10-7-06`.

### 14.9 Thời lượng (62 trang, 120 phút)

Bảng ở mục 2 tính cho 60 trang và tách 8 phút câu hỏi nhanh. Bảng dưới thay nó: phút từng trang, đã gồm câu hỏi nhanh (3 phút mỗi câu) và hỏi lớp ở trạm dừng. Không bỏ hay gộp trang.

| Mạch | Phút từng trang | Tổng |
|---|---|---|
| 1 | 1-01 0,5 · 1-02 1,5 · 1-03 3 · 1-04 2 · 1-05 2 · 1-06 1 · 1-07 0,5 · 1-08 1,5 | 12 |
| 2 | 2-00 0,5 · 2-01 2,5 · 2-02 2 · 2-03 3 · 2-04 1,5 · 2-05 1,5 · 2-06 1,5 · 2-07 2 · 2-08 2 | 16,5 |
| 3 | 3-00 0,5 · 3-01 2 · 3-02 3 · 3-05 2 · 3-04 3 | 10,5 |
| 4 | 4-00 0,5 · 4-01 1,5 · 4-02 2,5 · 4-03 2 · 4-11 2 · 4-04 1,5 · 4-05 3 · 4-10 3 · 4-06 2 · 4-12 2 · 4-07 1,5 · 4-08 2,5 · 4-09 2,5 | 26,5 |
| 5 | 5-00 0,5 · 5-01 3 · 5-02 2,5 · 5-03 3 · 5-04 2,5 · 5-05 3 · 5-06 2 · 5-07 2,5 · 5-08 1,5 | 20,5 |
| 6 | 6-00 0,5 · 6-01 1,5 · 6-02 2 · 6-03 2 · 6-04 2,5 · 6-05 2 · 6-06 2 · 6-07 2,5 · 6-08 3 · 6-09 3 | 21 |
| 7 | 7-00 0,5 · 7-01 2,5 · 7-02 2 · 7-03 2 · 7-04 3 · 7-05 1,5 · 7-06 1 · 7-07 0,5 | 13 |
| **Tổng** | 62 trang | **120** |

So với bảng cũ: mạch 1 giữ 12; mạch 2 giảm 2,5 (trang định nghĩa, ý tưởng chứng minh ngắn); mạch 3 giảm 1,5 (bỏ `3-03` từ trước); mạch 4 tăng 4,5 (hai trang mới `4-11`, `4-12`); mạch 5 tăng 4,5 và mạch 6 giảm 1 (câu hỏi nhanh và trạm dừng nay tính trong mạch); mạch 7 tăng 4 (bài tổng hợp có lời giải trên trang). Trang đếm theo P6: 58 (ba chuỗi dựng dần cùng bố cục tính một trang mỗi chuỗi).
