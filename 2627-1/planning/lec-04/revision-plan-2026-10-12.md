# Kế hoạch sửa Bài 04 theo chuẩn 2026-10-12

Tôi chỉ đọc, không sửa, tạo, xóa tệp nào và không commit. Báo cáo dựa trên các tệp sau:
- `AGENTS.md` (đọc đủ các mục được giao) và `CLAUDE.md`.
- Hai mẫu `materials/_templates/{lecture-note,exercises}.md`.
- Deck `2627-1/lecture-04-giai-mdp-bang-quy-hoach-dong.html`: 45 trang, 7 `<section>` ngoài, chưa có trang tiêu đề mạch, không có thuộc tính `id`.
- Ghi chú `materials/lec-04/lecture-note.md`: 687 dòng.
- Các ô Markdown và output của notebook `thuc-hanh-cartpole-quy-hoach-dong.ipynb`.
- Các tệp `planning/lec-04/{outline,storyboard,review-log,analysis}.md`.
- Hai đề `RL-hk2-2025-2026/resources/hw3.pdf` và `hw04.pdf`.
- Sản phẩm mẫu ở `math-4-AI` Bài 07, chỉ để học cách trình bày.

Mật độ đo bằng `scratchpad/density.py`. Các phép tính số dưới đây tôi đã tính lại độc lập.

**Phát hiện chính**
1. Có 15 trang vượt 60 âm tiết. Bốn trang vượt 90 âm tiết, tức hơn 1,5 lần trần: E01 (123), F01 (103), F03 (98), G05 (100). Ngoài ra:
   - 21 trang có hơn 6 dòng hoặc có dòng dài hơn 20 âm tiết;
   - 9 trang có hơn 3 khối công thức;
   - 17 trang có hơn 1 khung.
2. Thiếu toàn bộ cấu trúc mới:
   - không có trang tiêu đề mạch;
   - không có các trang "Tiên quyết và quy ước", "Nội dung" đánh số và "Vấn đề trung tâm";
   - không có bảng tổng kết `Kết quả | Giả thiết | Công thức` và các trang kết luận mới.
3. Không cụm khái niệm nào có bài tập với "Lời giải:" trên mặt trang. Bảy trang "Kiểm tra …" để lời giải trong ghi chú diễn giả với nhãn "Lời giải.".
4. Ghi chú bài giảng dùng bộ số khác deck: thưởng $(2,-1,5,10)$, $\gamma=0{,}5$, lưới thưởng $24$. Thứ tự mục cũng khác deck: $v_*$ và $T_*$ đứng trước đánh giá chính sách.
5. Ghi chú viết hoàn toàn ở giọng khách quan, có 0 lần "chúng ta/ta" và nhiều câu lấy ghi chú làm chủ ngữ. Ghi chú thiếu:
   - Bản đồ chủ đề;
   - các môi trường có số hiệu;
   - đoạn "Trong thực hành";
   - Tình huống áp dụng;
   - Tóm tắt chương;
   - Bài tập củng cố có lời giải.
6. Thuật ngữ lệch giữa các tài liệu:
   - "lượt" (deck, ghi chú) so với "lượt quét" (notebook, Bài 05);
   - "tổng thưởng chiết khấu" (Bài 03, 04) so với "lợi tức" (Bài 05, mẫu);
   - "quy tắc phá hòa" (deck) so với "quy tắc giữ hòa" (ghi chú, notebook);
   - "giá trị tiếp nối" (deck) so với "giá trị tiếp diễn" (ghi chú).

---

## A. Deck

### A1. Bảng mạch hiện tại → đề xuất

Giữ 7 mạch, nằm trong khoảng 5–7. Không gộp C với D. Lý do: nguồn tách cải thiện (tr. 19–21) khỏi lặp chính sách (tr. 20, 33–34), và Sutton–Barto tách §4.2 khỏi §4.3. Thứ tự theo Sutton–Barto chương 4 đã được người dùng duyệt (outline.md, dòng 7). Trang tiêu đề mạch dùng mã `<tiền tố>00`; chưa có mã nào trùng.

| N | Hiện tại | Tên mạch đề xuất | Dòng dẫn (âm tiết) | Từ khóa (≤5) | Trang tiêu đề | id |
|---|---|---|---|---|---|---|
| 1 | A. Mở đầu, A01–A05 | Mở đầu | Không có; bìa là trang tiêu đề mạch | — | L04-A01 (bìa) | không gán |
| 2 | B. Đánh giá chính sách, B01–B08 | Đánh giá chính sách | "Muốn so sánh các hành động, trước hết phải tính giá trị của chính sách đang dùng từ mô hình." (20) | Bài toán dự đoán · Toán tử $T_\pi$ · Lượt quét đồng bộ · Phần dư Bellman · Tính co | L04-B00 | `mach-2` |
| 3 | C. Cải thiện, C01–C07 | Cải thiện chính sách | "Muốn có chính sách tốt hơn, phải đổi hành động theo giá trị nhìn trước một bước." (17) | Giá trị hành động · Giá trị nhìn trước · Chính sách tham lam · Định lý cải thiện chính sách | L04-C00 | `mach-3` |
| 4 | D. Lặp chính sách, D01–D06 | Lặp chính sách | "Muốn tìm chính sách tối ưu, phải xen kẽ đánh giá chính xác và cải thiện cho đến khi chính sách ổn định." (23) | Chính sách ổn định · Quy tắc giữ hòa · Phương trình Bellman tối ưu · Dừng hữu hạn | L04-D00 | `mach-4` |
| 5 | E. Lặp giá trị, E01–E08 | Lặp giá trị | "Muốn bỏ bước đánh giá đầy đủ ở mỗi vòng, phải gộp cải thiện với một lượt quét thành phép cực đại." (23) | Toán tử $T_*$ · Tính co · Hội tụ hình học · Ngưỡng phần dư | L04-E00 | `mach-5` |
| 6 | F. Quy hoạch động trong thực hành, F01–F06 | Lịch cập nhật và giới hạn của mô hình bảng | "Muốn giảm chi phí mỗi lượt quét, phải chọn lịch sao cho mọi trạng thái được cập nhật vô hạn lần." (21) | Chi phí một lượt quét · Cập nhật tại chỗ · Quy hoạch động bất đồng bộ · GPI · CartPole rời rạc hóa | L04-F00 | `mach-6` |
| 7 | G. Tổng hợp và bài tập, G01–G05 | Tổng hợp và vận dụng | "Muốn dùng các kết quả của quy hoạch động, phải kiểm đủ mô hình đã biết, tập hữu hạn và $\gamma<1$." (≈20) | Giả thiết không được bỏ · Chứng nhận tối ưu · Câu hỏi tự kiểm tra · Dự đoán phi mô hình | L04-G00 | `mach-7` |

Ba trang đầu mạch có tiêu đề trùng hoặc gần trùng tên mạch, phải đổi tên:
- B01 "Bài toán đánh giá chính sách" → "Giá trị dài hạn của chính sách cố định".
- D01 "Chu trình lặp chính sách" → "Đánh giá lại sau mỗi lần cải thiện".
- G01 → "Tổng kết".

Ghi chú diễn giả của từng trang tiêu đề mạch (40–100 âm tiết) nêu ba điều: điều kế thừa, nhiệm vụ của mạch và điều giao cho mạch sau.
- B00: kế thừa $p$, $\pi_0$ và phương trình Bellman kỳ vọng của Bài 03. Giao $v_{\pi_0}=(10,11)$ và chặn phần dư.
- C00: kế thừa $v_{\pi_0}$. Giao $\pi_1=(a,b)$ và nhu cầu đánh giá lại.
- D00: kế thừa định lý cải thiện. Giao $(\pi_*,v_*)=((b,b),(27,30))$ và chi phí của đánh giá đầy đủ.
- E00: kế thừa nhu cầu cắt ngắn đánh giá. Giao $T_*$, ngưỡng $\eta=(1-\gamma)\varepsilon$ và chi phí một lượt quét.
- F00: kế thừa $T_\pi,T_*$. Giao điều kiện lịch và điều kiện mô hình.
- G00: thu hồi vấn đề trung tâm.

### A2. Mạch mở đầu và mạch kết luận

**Mạch mở đầu.** Thứ tự đề xuất gồm 8 trang, khoảng 12 phút.

1. **L04-A01 Bìa.** Thiếu câu luận đề: hộp hiện tại "Tính giá trị và lựa chọn chính sách từ mô hình môi trường đã biết." là cụm nhiệm vụ, không phải câu trần thuật nêu kết quả.
   - Đề xuất câu luận đề: "Với mô hình đã biết và $\gamma<1$, giá trị và chính sách tối ưu là điểm bất động của toán tử Bellman, tính được bằng phép lặp."
   - Dòng chủ đề viết "quá trình quyết định Markov (Markov decision process, MDP)".
2. **L04-A01b Tiên quyết và quy ước (mới).** Lấy nội dung từ A03 và từ ghi chú diễn giả của A03.
   - "Nhắc lại:" MDP hữu hạn có tính Markov và $p(s',r\mid s,a)$; lợi tức (return) $G_t=R_{t+1}+\gamma G_{t+1}$; $v_\pi(s)=\mathbb E_\pi[G_t\mid S_t=s]$, $q_\pi$ và phương trình Bellman kỳ vọng (Bài 03).
   - "Ký hiệu:" $\mathcal S$ là tập hữu hạn các trạng thái chưa kết thúc, $V(s_{\mathrm{term}})=0$; $\mathcal A(s)$ hữu hạn; $\pi(a\mid s)$ là chính sách dừng; $t$ đếm bước tương tác, $k$ đếm lượt quét, $i$ đếm vòng cải thiện; $\mathbb E_\pi$ lấy theo $\pi$ và $p$; $0\le\gamma<1$.
   - Bài 03 chưa có số hiệu, nên chưa dẫn được "Định lý 03.k" và phải phát biểu lại kết quả.
3. **L04-A02 Mục tiêu học tập** (tách từ A02). Mỗi mục tiêu ứng với một sản phẩm kiểm tra được:
   - (1) Tính một lượt quét đánh giá và giá trị chính xác của chính sách; chặn sai số bằng phần dư. Sản phẩm: Bài tập 04.1.
   - (2) Tính $q_\pi$, lập chính sách tham lam với quy tắc giữ hòa và giải thích vì sao giá trị không giảm. Sản phẩm: 04.2.
   - (3) Chạy lặp chính sách tới chính sách ổn định; phân biệt chứng nhận tối ưu với dừng theo bảng gần đúng. Sản phẩm: 04.3.
   - (4) Chạy lặp giá trị, trích chính sách tham lam và chọn $\eta=(1-\gamma)\varepsilon$. Sản phẩm: 04.4.
   - (5) So sánh cập nhật đồng bộ, tại chỗ và bất đồng bộ; nêu điều kiện bao phủ và điều kiện mô hình khi áp dụng cho CartPole rời rạc hóa. Sản phẩm: 04.5 và Tình huống 04.1–04.2.
4. **L04-A02b Nội dung (mới).** Đánh số 1–7 với tên trùng bảng A1, kèm dòng "Đọc trước: Sutton và Barto (2018), §4.1–4.4".
5. **L04-A03 Vấn đề trung tâm** (viết lại A03).
   - Dòng bài toán: "Nhu cầu: từ $p$ đã biết, tìm $\pi$ có $v_\pi(s)$ lớn nhất tại mọi $s$". Dòng này báo trước $v_*$, nên D04 không phải mở bằng định nghĩa.
   - Năm dòng trả lời có điều kiện, mỗi mạch 2–6 một dòng:
     - $v_\pi$ là điểm bất động duy nhất của $T_\pi$ khi $\gamma<1$;
     - chính sách tham lam theo $q_\pi$ không kém $\pi$;
     - đánh giá chính xác và giữ hòa cho dừng hữu hạn tại chính sách tối ưu;
     - $\Delta_*(V)\le(1-\gamma)\varepsilon$ bảo đảm sai số không quá $\varepsilon$;
     - lịch bất đồng bộ hội tụ khi mọi trạng thái được cập nhật vô hạn lần, và vẫn cần $p$ cùng tập hữu hạn.
   - Kèm hình `dp04-roadmap.svg`.
   - Giữ dưới 60 âm tiết; nếu vượt, ghi ngoại lệ trong storyboard.
6. **L04-A03b Cấu trúc một phép cập nhật quy hoạch động (mới, khung chung, bốn dòng).**
   - Mục tiêu một bước $r+\gamma V(s')$, lấy kỳ vọng theo $p$.
   - Gộp hành động bằng trung bình theo $\pi$ hoặc bằng cực đại.
   - Lịch đồng bộ, tại chỗ hoặc bất đồng bộ.
   - Dừng theo phần dư hoặc theo chính sách ổn định.
7. **L04-A04 Ví dụ: mô hình hai trạng thái** (sửa).
8. **L04-A05 Bài tập: lợi tức từ $s_1$** (sửa).

**Mạch kết luận.** Gồm 10 trang, khoảng 18 phút, không đưa khái niệm mới.

1. **L04-G00** Trang tiêu đề mạch.
2. **L04-G01 Tổng kết.** Bảng `Kết quả | Giả thiết không được bỏ | Công thức hoặc thuật toán`, trần 80 âm tiết. Nếu vượt trần thì tách ba hàng mỗi trang.

| Kết quả | Giả thiết không được bỏ | Công thức hoặc thuật toán |
|---|---|---|
| Đánh giá chính sách | MDP hữu hạn, thưởng bị chặn, $\gamma<1$, $\pi$ dừng, $p$ đã biết | $v_\pi=T_\pi v_\pi$; $(I-\gamma P_\pi)v_\pi=r_\pi$ |
| Chặn sai số theo phần dư | $\gamma<1$; phần dư đo trên chính bảng trả về | $\lVert V-v\rVert_\infty\le\Delta(V)/(1-\gamma)$ |
| Định lý cải thiện | $v_\pi$ chính xác; $\pi'$ tham lam theo $q_\pi$ | $v_{\pi'}\ge v_\pi$ |
| Lặp chính sách | Đánh giá chính xác; quy tắc giữ hòa; tập hành động hữu hạn | Dừng sau tối đa $\prod_s\lvert\mathcal A(s)\rvert$ vòng tại $\pi_*$ |
| Lặp giá trị | $T_*$ co (như trên) | $\lVert V_k-v_*\rVert\le\gamma^k\lVert V_0-v_*\rVert$; dừng khi $\Delta_*\le(1-\gamma)\varepsilon$ |
| Bất đồng bộ | Mọi trạng thái chưa kết thúc được cập nhật vô hạn lần | $V(s)\leftarrow(T_*V)(s)$ theo lịch |

3. **L04-G02 Khung chung.** Bảng `Phương pháp | Quy tắc cập nhật | Dữ liệu dùng | Điều kiện dừng`.

| Phương pháp | Quy tắc cập nhật | Dữ liệu dùng | Điều kiện dừng |
|---|---|---|---|
| Đánh giá chính sách | $V\leftarrow T_\pi V$ | $p,\pi$ | $\Delta_\pi\le\eta$ hoặc hết $K$ |
| Lặp chính sách | Giải $v_\pi$; tham lam | $p$ | $\pi'=\pi$ hoặc hết $I_{\max}$ |
| Lặp giá trị | $V\leftarrow T_*V$ | $p$ | $\Delta_*\le\eta$ hoặc hết $K$ |
| Bất đồng bộ | $V(s)\leftarrow(T_*V)(s)$ | $p$, lịch | Kiểm $\Delta_*$ tại mốc |

4. **L04-G02b Hội tụ.** Bảng `Phương pháp | Giả thiết không được bỏ | Kết luận`.

| Phương pháp | Giả thiết không được bỏ | Kết luận |
|---|---|---|
| Đánh giá chính sách | $\gamma<1$ | Hội tụ hình học về $v_\pi$ |
| Lặp chính sách | Đánh giá chính xác, giữ hòa | Dừng hữu hạn tại chính sách tối ưu |
| Lặp giá trị | $\gamma<1$ | Hội tụ về $v_*$, có chặn phần dư |
| Bất đồng bộ | Mỗi trạng thái được cập nhật vô hạn lần | $V\to v_*$ |

5. **L04-G04 / G04b Bài tập: chứng nhận nghiệm tối ưu.** Đây là bài tập tổng hợp, có trang "Lời giải:" trên mặt trang.
6. **L04-G06 Trả lời vấn đề trung tâm (mới).**
   - Kết luận có điều kiện: với MDP hữu hạn, thưởng bị chặn, $\gamma<1$ và $p$ đã biết, việc chọn chuỗi quyết định thay được bằng bài toán điểm bất động $v_*=T_*v_*$, và chính sách tham lam theo $v_*$ là tối ưu.
   - Dòng "Nguồn: Tạ Việt Cường, Bài 04, tr. 7–9, 31–34; Sutton và Barto (2018), §4.1–4.4".
7. **L04-G07 Câu hỏi tự kiểm tra (mới).** Mở bằng "Câu hỏi: trả lời và nêu kết quả đã dùng.", gồm bốn câu:
   - (1) $12{,}9$ có phải $v_{(a,b)}(s_1)$ không. Phân biệt $q_\pi$ với $v_{\pi'}$.
   - (2) Chính sách không đổi sau cải thiện theo bảng gần đúng đã được chứng nhận tối ưu chưa.
   - (3) Phần dư bằng 0 trên mô hình CartPole 324 ô chứng nhận điều gì. Câu này lấy từ F06 và G04.
   - (4) Chặn $\Delta/(1-\gamma)$ có còn dùng được khi $\gamma=1$ không.
8. **L04-G03 Bài tập: dãy năm ô trơn trượt** (bài tự làm).
9. **L04-G05 Bài tập về nhà và tài liệu đọc.** Gồm:
   - bảng `Mạch | Bài tập` theo phần C;
   - dòng "Tài liệu đọc: Sutton và Barto (2018), §4.1–4.8";
   - dòng "Ghi chú bài giảng · Bài tập";
   - một dòng nối sang Bài 05: "khi không có $p$, kỳ vọng trong $T_\pi$ được thay bằng mẫu chuyển".

### A3. Bảng từng trang (đủ 45 trang)

Ký hiệu trong cột âm tiết: âm tiết (dòng / âm tiết dòng dài nhất / số công thức / số khung). Khung được đếm gồm `.card`, `.box` và `.check`.

| Mã | Âm tiết | Vấn đề theo chuẩn mới | Quyết định | Đề xuất cụ thể |
|---|---|---|---|---|
| A01 | 46 (5/15/0/1) | Không có câu luận đề; dòng "MDP" đứng rời, thiếu thuật ngữ gốc | sửa | Câu luận đề ở A2; ghi chú 40–100 âm tiết, mở bằng kết quả Bài 03 |
| A02 | 55 (9/8/0/2) | 9 dòng, 2 khung; gộp "Nội dung" với "Mục tiêu"; hình 4 khối không đánh số khớp 7 mạch; mục tiêu không gắn sản phẩm; tiên quyết đặt sai chỗ; ghi chú dùng từ quy trình "mạch" | tách | Tách thành A02 "Mục tiêu học tập" và A02b "Nội dung"; tiên quyết chuyển sang A01b |
| A03 | **76** (8/17/2/2) | Vượt trần; "Quy hoạch động: nhóm thuật toán…" dùng dấu hai chấm thay "là"; nhãn "Dữ kiện", "Bài toán điều khiển" ngoài danh sách; ghi chú 202 âm tiết | tách | Tách thành A01b (Nhắc lại, Ký hiệu) và A03 (Vấn đề trung tâm); câu "Quy hoạch động là…" và quy ước $\mathcal S^+$ chuyển vào ghi chú; mỗi trang ≤60 |
| A04 | 55 (7/**24**/0/1) | 7 dòng; dòng 24 âm tiết; thiếu "Ví dụ:"; gọi bằng viết tắt | sửa | Tiêu đề "Ví dụ: mô hình hai trạng thái"; "$\pi_0=(a,a)$: chọn $a$ ở cả hai trạng thái."; câu "Bài toán tiếp diễn" vào ghi chú |
| A05 | 36 (4/14/1/1) | "Kiểm tra …"; $G_t$ dùng trước khi nhắc lại; nhãn "Lời giải."; thiếu "Gợi ý:"; thuật ngữ chưa thống nhất | sửa | "Bài tập: lợi tức từ $s_1$"; lời giải $2+0{,}9+0{,}81=3{,}71$ hiện bằng fragment "Lời giải:" |
| B01 | 46 (2/**28**/1/1) | Mở khái niệm bằng định nghĩa "Bài toán dự đoán: …"; không có "Nhu cầu:" và ví dụ có số; tiêu đề gần trùng tên mạch; $V(s')$ dùng trước khi định nghĩa | sửa | Tiêu đề "Giá trị dài hạn của chính sách cố định"; "Nhu cầu: tính $v_{\pi_0}(s_0)$ khi lợi tức gồm vô hạn số hạng" + "Trực quan." + hình cập nhật kỳ vọng; thuật ngữ "đánh giá chính sách (policy evaluation)" và "cập nhật kỳ vọng (expected update)" vào ghi chú |
| B02 | 54 (8/**27**/2/3) | 8 dòng, 3 khung; thiếu "Ví dụ:"; "lượt" mơ hồ | sửa | "Ví dụ: mô hình hai trạng thái, hai lượt quét"; khuôn bảng cố định "Lượt quét \| $V_k(s_0)$ \| $V_k(s_1)$", dùng lại ở B07, E02, E06; một câu kết luận |
| B03 | 52 (2/**30**/**4**/2) | 4 công thức; dòng 30; kết quả của Bài 03 trình bày như mới | sửa | "Nhắc lại: phương trình Bellman kỳ vọng"; 1 khối tổng quát và 1 khối `aligned` cho $\pi_0$; câu "Hai thẻ trên…" vào ghi chú |
| B04 | 32 (5/16/**4**/2) | 4 công thức; nhãn thẻ ngoài danh sách; dòng "Đã tính" thừa; ghi chú 235 âm tiết chứa ví dụ chính sách ngẫu nhiên | sửa | "Định nghĩa." $T_\pi$ (toán tử Bellman, Bellman operator) + một `aligned` cho $V_{k+1}=T_\pi V_k$ và $v_\pi=T_\pi v_\pi$; ví dụ ngẫu nhiên đều chuyển sang ghi chú bài giảng |
| B05 | **78** (6/23/0/0) | Vượt trần; trộn định nghĩa, ví dụ và giả mã; "Phần dư: Δ=…"; thiếu "Thuật toán." và "Đầu ra:" | tách | B05 "Phần dư Bellman" (Định nghĩa "gọi là phần dư Bellman (Bellman residual)", Ví dụ $\Delta_{\pi_0}(V_1)=0{,}9$, ≈35 âm tiết); B05b "Thuật toán: đánh giá chính sách đồng bộ" (Đầu vào/Đầu ra/4 bước, ≤8 dòng, ≈50) |
| B06 | 55 (4/18/**4**/0) | Nhãn "Tính co." ngoài danh sách; 4 công thức; định lý và hệ quả cùng trang; thiếu "Ý nghĩa:" | tách | B06 "Định lý." (giả thiết trên mặt trang; co; nghiệm duy nhất; hội tụ) + "Chứng minh." một dòng + "(Mệnh đề 04.4)"; B06b "Hệ quả." chặn phần dư + "Ý nghĩa:" + $0{,}81/0{,}1=8{,}1$ |
| B07 | 36 (**8**/19/2/1) | 8 dòng; giải hệ đã có ở Bài 03 | sửa | "Ví dụ: mô hình hai trạng thái, giá trị chính xác của $\pi_0$"; giữ bảng (thêm hàng $v_{\pi_0}$) và hệ `aligned`; "Diễn giải: sau hai lượt quét sai số còn $8{,}1$"; ma trận để ở ghi chú |
| B08 | 32 (**9**/8/0/1) | 9 dòng do lặp bảng dữ kiện; "Kiểm tra …"; không có "Lời giải:" trên mặt trang | tách | B08 "Bài tập: lượt quét thứ ba và chặn sai số" (dữ kiện một dòng, "Câu hỏi:" ba ý, ghi chú có "Gợi ý:"); B08b "Lời giải:" $V_3=(2{,}71;3{,}71)$, $\Delta=0{,}81$, chặn $8{,}1$ bằng sai số thật. Trùng Bài tập 04.1 |
| C01 | **83** (8/19/0/3) | Vượt trần; 3 khung; nhãn "Bài toán điều khiển:"; định nghĩa giá trị nhìn trước bằng dấu ":" | tách | C01 "Đổi một hành động tại $s_1$": "Nhu cầu:" + "Trực quan." hai dòng (≈35); công thức giá trị nhìn trước chuyển sang C03; thêm "điều khiển (control)" |
| C02 | 32 (5/14/2/3) | 3 khung; thiếu "Ví dụ:" | sửa | "Ví dụ: hai nhánh tại $s_1$"; bảng "Nhánh \| Thưởng \| Tiếp nối \| Nhìn trước" (11; 12,9); "Kết luận: $12{,}9>11$" |
| C03 | 29 (2/20/**4**/1) | 4 công thức; "Định nghĩa. $q_\pi=\mathbb E…$:" dùng "=" thay "là"; $q_\pi$ đã có ở Bài 03 | sửa | "Nhắc lại: giá trị hành động" ("gọi là"); ≤3 khối; "Ví dụ." $q_{\pi_0}(s_1,b)=12{,}9$; thuật ngữ "nhìn trước một bước (one-step lookahead)" |
| C04 | **84** (3/**37**/0/1) | Vượt trần; định nghĩa tham lam, định lý và lập luận cùng trang; quy tắc giữ hòa chỉ có ở ghi chú và D02 | tách | C04 "Chính sách tham lam" (Định nghĩa, "tham lam (greedy)", quy tắc giữ hòa); C04b "Định lý cải thiện chính sách" (Giả thiết, Kết luận, "Ý nghĩa:", "(Định lý 04.12)"); lập luận max ≥ trung bình vào ghi chú |
| C05 | 42 (**8**/9/2/2) | 8 dòng, 2 thẻ với nhãn ngoài danh sách; tiêu đề không theo dạng "Chứng minh: …" | sửa | "Chứng minh: định lý cải thiện chính sách"; ba dòng "Bước 1–3" (bất đẳng thức đầu; tính đơn điệu; giới hạn nhờ Mệnh đề 04.4) |
| C06 | 51 (**8**/14/2/3) | 8 dòng, 3 khung; thiếu "Ví dụ:" | sửa | "Ví dụ: mô hình hai trạng thái, lần cải thiện thứ nhất"; bảng $q_{\pi_0}$ + dòng $\pi_1=(a,b)$, $v_{\pi_1}=(10,30)$; "Diễn giải:"; câu về $s_0$ vào ghi chú |
| C07 | 32 (5/13/0/1) | "Kiểm tra …"; không có lời giải trên mặt trang | tách | "Bài tập: cải thiện từ $\pi_1$" + C07b "Lời giải:" $10$ và $27$, chọn $b$. Trùng Bài tập 04.2 |
| D01 | 45 (2/**36**/0/1) | Dòng 36; tiêu đề gần trùng tên mạch; nêu tên thuật toán trước nhu cầu | sửa | "Đánh giá lại sau mỗi lần cải thiện"; "Nhu cầu: $v_{\pi_1}\ne v_{\pi_0}$ nên lựa chọn tại $s_0$ phải xét lại"; dòng "Lặp chính sách (policy iteration) là…" ≤20 âm tiết; $i$, $k$ đưa vào "Ký hiệu:" |
| D02 | 51 (**9**/**31**/0/2) | 9 dòng; "Chính sách ổn định:" định nghĩa bằng dấu hai chấm; định nghĩa nằm lẫn trong trang ví dụ | tách | D02 "Ví dụ: mô hình hai trạng thái, ba vòng lặp chính sách" (bảng); D02b "Chính sách ổn định" (Định nghĩa + kiểm tra $q_{\pi_2}=25{,}3/27/26{,}3/30$) |
| D03 | **70** (6/19/0/0) | Vượt trần; thiếu "Thuật toán.", "Đầu ra:"; lời giải thích ngân sách dài | sửa | "Thuật toán." + Đầu vào/Đầu ra + 4 bước ≤8 dòng (≈50); nhãn "chưa ổn định" giải thích trong ghi chú; "(Thuật toán 04.16)" |
| D04 | 49 (4/16/2/1) | Khái niệm trọng tâm $v_*$ mở bằng định nghĩa trên trang kết quả; hộp chứa chứng minh nhiều câu; tiêu đề dạng câu | tách | D04 "Phương trình Bellman tối ưu" (Định nghĩa $v_*$ đã báo trước ở A03 + "Định lý." + "Ví dụ." $(b,b),(27,30)$; nói rõ "trên lớp chính sách dừng, mở rộng ở Định lý 04.23"); D04b "Chứng minh: tính tối ưu của chính sách ổn định" ba bước |
| D05 | **76** (7/23/1/3) | Vượt trần; 3 khung; hai luận điểm | tách | D05 "Mệnh đề." dừng hữu hạn ($\prod_s\lvert\mathcal A(s)\rvert$, tăng nghiêm, không lặp lại) + "Chứng minh." một dòng; phần đánh giá gần đúng thành "Lưu ý:" đưa vào dữ kiện D06 |
| D06 | 45 (**10**/12/0/1) | 10 dòng (bảng lặp lại); không có lời giải trên mặt trang | tách | "Bài tập: kết luận dừng từ bảng gần đúng" + D06b "Lời giải:" (nhìn trước $1,0,2,3$ → $(a,b)$; $v_{(a,b)}=(10,30)\ne(27,30)$). Trùng Bài tập 04.3 |
| E01 | **123** (8/**46**/0/**4**) | Hơn 2 lần trần (nghiêm trọng); dòng 46; 4 khung | tách | E01 "Chi phí của đánh giá đầy đủ": "Nhu cầu:" + $10\cdot0{,}9^k\le0{,}1\Rightarrow k=44$ + $O(n^3)$ (≈40); E01b "Ý tưởng lặp giá trị": "Trực quan." ba dòng + "lặp giá trị (value iteration)" (≈45) |
| E02 | 49 (6/**26**/2/1) | Dòng 26; thiếu "Ví dụ:" | sửa | "Ví dụ: mô hình hai trạng thái, hai lượt quét lặp giá trị"; bảng "Trạng thái \| Nhánh $a$ \| Nhánh $b$ \| Cực đại"; câu so sánh $(1,2)$ với $(1,3)$ ≤20 âm tiết |
| E03 | 46 (4/20/**4**/2) | 4 công thức; nhãn thẻ ngoài danh sách | sửa | "Định nghĩa." $Q_V$ (1 khối) + `aligned` $T_*V=\max_aQ_V$, $V_{k+1}=T_*V_k$; định nghĩa $\Delta_*$ đưa lên đây; "Lưu ý: $Q_V=q_\pi$ chỉ khi $V=v_\pi$"; "toán tử Bellman tối ưu (Bellman optimality operator)" |
| E04 | **71** (6/17/0/1) | Vượt trần; lặp gần nguyên văn giả mã B05 | sửa | "Thuật toán: lặp giá trị đồng bộ" ≤8 dòng, bước 2 viết "như Thuật toán 04.8 với $T_*$"; thêm bước trích $\pi_V$ (≈50) |
| E05 | 55 (3/20/**4**/1) | 4 công thức; thiếu nhãn "Định lý."; nhận xét phạm vi đặt cùng định lý | sửa | "Định lý." Giả thiết/Kết luận (≤2 khối) + "(Mệnh đề 04.22, Hệ quả 04.24)"; "Lưu ý:" chặn chứa $v_*$ chưa biết; ví dụ $30\cdot0{,}9^k$ vào ghi chú |
| E06 | **65** (**10**/12/0/0) | Vượt trần; 10 dòng; thiếu "Ví dụ:"; gọi "lưới" cho đối tượng một chiều; ứng dụng đứng trước hình thức E07 | tách | E06 "Ví dụ: dãy năm ô" (hình + 4 dòng dữ kiện); E06b "Ví dụ: dãy năm ô, bốn lượt quét" (bảng $V_0$–$V_4$, "Diễn giải: $V_5=V_4$ nên $V_4=v_*$"); đặt sau E07 |
| E07 | 50 (6/15/3/**3**) | 3 khung; hệ quả hình thức đứng sau ứng dụng | sửa | "Hệ quả." $\lVert V-v_*\rVert\le\Delta_*/(1-\gamma)$; "Ý nghĩa:" $\eta=(1-\gamma)\varepsilon$; "Ví dụ." $V_1$: $\Delta=2{,}7$, chặn 27 bằng sai số thật; chuyển lên trước E06 |
| E08 | 47 (5/**21**/0/1) | Dòng 21; không có lời giải trên mặt trang | tách | "Bài tập: điểm bất động trên dãy năm ô" + E08b "Lời giải:" (bảng 4 ô × 2 nhánh; $T_*V_4=V_4$; đi phải). Trùng Bài tập 04.4 |
| F01 | **103** (6/**41**/0/1) | Hơn 1,5 lần trần (nghiêm trọng); dòng 41 | tách | F01 "Chi phí một lượt quét": "Ký hiệu:" $n,m,d$ + bảng hai hàng (≤40); câu "hai hướng giảm…" thành dòng "Nhu cầu:" mở F02; giải thích $P$, $\bar r$ và khử Gauss vào ghi chú |
| F02 | 55 (5/**21**/0/1) | Dòng 21; "Tại chỗ: …" định nghĩa bằng dấu hai chấm; thiếu "Ví dụ:" | sửa | "Ví dụ: cập nhật tại chỗ (in-place)"; "Cập nhật tại chỗ là …"; hai kết quả $(1;2{,}9)$ và $(1,2)$; một lượt quét trên dãy năm ô |
| F03 | **98** (6/**27**/0/1) | Hơn 1,5 lần trần (nghiêm trọng); trộn thuật toán, định lý và ví dụ | tách | F03 "Thuật toán: lặp giá trị bất đồng bộ" ≤8 dòng; F03b "Hội tụ của quy hoạch động bất đồng bộ (asynchronous DP)": "Định lý." với giả thiết cập nhật vô hạn lần + "Ví dụ." lịch $c_4$–$c_1$ cho $\Delta_*=0$ |
| F04 | 55 (**8**/17/0/**4**) | 8 dòng, 4 khung; viết tắt "GPI" thiếu thuật ngữ gốc | sửa | "lặp chính sách tổng quát (generalized policy iteration, GPI)"; bảng 3 hàng "Phương pháp \| Mức hoàn tất đánh giá"; một dòng "Kết luận:" |
| F05 | 55 (4/**22**/1/1) | Dòng 22; chưa nối với bài thực hành | sửa | "Ví dụ: CartPole rời rạc hóa"; thêm dòng "Trong bài thực hành, $\hat p$ ước lượng từ 200 bước mô phỏng cho mỗi cặp ô–hành động"; dòng cuối ≤20 âm tiết |
| F06 | **74** (7/**27**/0/**3**) | Vượt trần; 3 khung; hai câu hỏi khác chủ đề | tách | "Bài tập: lịch bỏ sót một trạng thái" + F06b "Lời giải:" ($V(s_0)\to10$, $V(s_1)=0$; vi phạm điều kiện cập nhật vô hạn lần). Trùng Bài tập 04.5. Câu CartPole chuyển sang G07 |
| G01 | 72 (6/**26**/2/3) | Trang tổng kết (trần 80) nhưng 3 khung; chuỗi mũi tên "→" bị cấm; không theo khuôn bảng; ghi chú có lời chỉ đường "ở trang sau" | sửa | Thay bằng bảng "Tổng kết" ở A2; bỏ "ở trang sau" |
| G02 | **93** (6/19/0/0) | Vượt trần 80 của bảng so sánh; cột chưa theo khuôn | tách | G02 (khung chung) và G02b (hội tụ) như ở A2 |
| G03 | 55 (6/19/0/0) | "Bài tập lưới ngẫu nhiên" thiếu dấu hai chấm; ghi chú thiếu "Gợi ý:" và câu năng lực | sửa | "Bài tập: dãy năm ô trơn trượt" (bài tự làm); thêm "Gợi ý:"; nguồn "hw04.pdf, Bài 10"; ánh xạ Bài tập 04.13 |
| G04 | 51 (**9**/19/0/1) | 9 dòng (lặp bảng); không có lời giải trên mặt trang; câu 3 khác chủ đề | tách | "Bài tập: chứng nhận nghiệm tối ưu" + G04b "Lời giải:" ($T_*U=(27,30)$, $\Delta_*(U)=17$, chặn 170, sai số thật 17; $T_*V=V$); câu 3 chuyển sang G07. Trùng Bài tập 04.6 |
| G05 | **100** (**8**/15/0/1) | Vượt trần 80; thiếu bảng `Mạch \| Bài tập`; thiếu "Tài liệu đọc:" dạng tác giả–năm–mục | sửa | "Bài tập về nhà và tài liệu đọc" như A2; chi tiết Ví dụ 4.1 và Bài tập 4.3–4.4 vào ghi chú diễn giả |

**Lỗi chung ở mọi trang.**
- Không có trang nào có "ta thấy", "rõ ràng", "chúng ta" hay "hãy" trên mặt trang.
- Không ghi chú nào mở bằng "Trang này", và không có mã nội bộ hay thời lượng trên mặt trang.
- 16 ghi chú dài hơn 150 âm tiết (mức nhẹ): A03, B04, B05, C04, D02, D03, D04, D05, E01, E03, E04, F03, F04, G01, G04, G05. Sau khi tách trang, đưa về 40–150 âm tiết.
- Thuật ngữ tiếng Anh ở lần đầu chỉ có "policy iteration" và "value iteration". Cần bổ sung: policy evaluation, expected update, sweep, Bellman operator, Bellman residual, greedy, policy improvement theorem, Bellman optimality operator, contraction, in-place, asynchronous DP, generalized policy iteration, tie-breaking.

**Quy ước mã cho trang mới.**
- Trang tách và trang lời giải dùng hậu tố `b` (ví dụ L04-B05b, L04-B08b).
- Trang tiêu đề mạch dùng L04-X00.
- Trang mới ở mạch 7 dùng L04-G06, L04-G07.

**Tổng số trang và thời lượng.** Tổng dự kiến khoảng 71 trang. Phân bổ thời lượng: 12 / 20 / 17 / 16 / 22 / 15 / 18 phút, tổng 120 phút.

### A4. Cụm khái niệm và sáu bước

| Cụm | Vấn đề | Trực giác | Ví dụ | Hình thức / thuật toán | Ứng dụng | Kiểm tra | Bước thiếu hoặc lệch |
|---|---|---|---|---|---|---|---|
| Nhắc mô hình và lợi tức (rút gọn) | A03 | A04 | A04 | A01b (Nhắc lại) | A05 | A05 | Hợp lệ khi ghi trong storyboard là cụm rút gọn |
| KN1 Đánh giá chính sách (thuật toán) | B01 | B01 | B02: tính tay hai lượt quét, trước giả mã B05b | B03–B06b | B07 | B08/B08b | Mở bằng định nghĩa ("Bài toán dự đoán: …"); thiếu "Nhu cầu:" có số; chưa có lời giải trên mặt trang |
| KN2 Cải thiện chính sách | C01 | C01 | C02 | C03 (nhắc lại $q$), C04/C04b, C05 | C06 | C07/C07b | Thiếu lời giải trên mặt trang; quy tắc giữ hòa dùng trước khi được định nghĩa |
| KN3 Lặp chính sách (thuật toán) | D01 | D01 (chu trình) | D02: tính tay ba vòng, trước giả mã D03 | D02b, D03, D04, D05 | D04 (chứng nhận $(b,b)$) | D06/D06b | Khái niệm $v_*$ mở bằng định nghĩa ở D04; sửa bằng cách đặt nhu cầu ở A03 và ví dụ D02 trước D04 |
| KN4 Lặp giá trị (thuật toán) | E01 | E01b | E02: tính tay hai lượt quét, trước giả mã E04 | E03, E04, E05, E07 | E06/E06b (dãy năm ô) | E08/E08b | Thứ tự hiện tại đặt E07 (hình thức) sau E06 (ứng dụng); đưa E07 lên trước E06 |
| KN5 Quy hoạch động bất đồng bộ (thuật toán) | F01 | F02 | F02: tính tay một lượt tại chỗ, trước F03 | F03, F03b | F03b (lịch $c_4$–$c_1$) | F06/F06b | Đạt sau khi tách |
| KN6 GPI (khái niệm phụ, rút gọn) | F04 | F04 (hình) | Dùng lại lặp chính sách và lặp giá trị đã tính | F04 | — | G07 | Ghi "rút gọn" trong storyboard |
| KN7 Mô hình bảng của CartPole (ứng dụng giới hạn) | F05 | F05 (hình) | 324 ô | Ánh xạ rời rạc hóa (trong ghi chú) | Tình huống 04.1 | G07 câu (3) | Thiếu nối với số liệu của notebook |

Cả bốn thuật toán đều có bước tính tay trước giả mã. Với E04, ví dụ E02, công thức E03 và giả mã cho cùng kết quả; điều này đã đúng và cần giữ khi sửa.

### A5. Ví dụ xuyên suốt

Các ví dụ hiện có đều truy nguyên được về nguồn và giữ nguyên dữ kiện, chỉ đổi tên gọi theo đối tượng:
- Hai trạng thái $s_0,s_1$ (tr. 17–18 của nguồn; hw04 Bài 1): thưởng 1/0/2/3, $\gamma=0{,}9$. Dùng ở A04–G04, mỗi lần trả lời một câu hỏi mới. Đổi tên "MDP hai trạng thái" thành **"mô hình hai trạng thái"**.
- Dãy năm ô (tr. 25–28): đổi "lưới năm ô" thành **"dãy năm ô"**.
- Dãy năm ô có trượt (hw04 Bài 10): đổi "lưới ngẫu nhiên" thành **"dãy năm ô trơn trượt"**.
- CartPole 324 ô (tr. 35–37): gọi là **"CartPole rời rạc hóa"**.

Mô hình hai trạng thái không phải phiên bản thu nhỏ của CartPole. Thứ tự ưu tiên đặt nguồn ở mức 2, trên chuẩn "ví dụ xuyên suốt", nên vẫn giữ hai ví dụ nguồn làm trục chính. Có ba cách nối với notebook:
- **(a) Tính tay trên CartPole.** Ô $s_h=71$ của notebook có $V_2(s_h)=1+0{,}99(1-0{,}435)=1{,}55935$ và $V_3(s_h)=1{,}91635$, đạt tại hành động 1. Đây là một bước tính tay có thật, dùng được làm Ví dụ trong ghi chú và một dòng ở F05.
- **(b) Cùng quy ước kết thúc.** Thưởng $+1$ mỗi bước và $V(s_{\mathrm{term}})=0$ giống quy ước của dãy năm ô.
- **(c) Số liệu chạy đối chiếu với kết quả lý thuyết.** Lặp chính sách ổn định sau 6 vòng; lặp giá trị cần 736 lượt quét so với chặn 917; tổng thưởng 343,4 ± 9,2 so với 22,5 của chính sách ngẫu nhiên và 43,6 của chính sách theo dấu góc.

---

## B. Ghi chú bài giảng

### B1. Đối chiếu mục hiện có

Cấu trúc đích:
- `# Bài 04 — Giải MDP bằng quy hoạch động`;
- phần đầu: Giới thiệu, Mục tiêu, Tiên quyết, Bảng ký hiệu, Bản đồ chủ đề;
- `## 1.`–`## 5.` ứng với mạch 2–6 của deck;
- phần cuối: Tình huống áp dụng và ứng dụng, Tóm tắt chương, Bài tập củng cố, Hướng dẫn đọc thêm và tài liệu tham khảo.

| Mục hiện có (dòng) | Đích mới | Ghi chú |
|---|---|---|
| `#` "Ghi chú chuyên sâu về quy hoạch động" (1) và đoạn mở (5) | Tiêu đề; Giới thiệu | Đổi tiêu đề. Đoạn 5 lấy tài liệu làm chủ ngữ và tham chiếu bộ trang chiếu: bỏ |
| `## 1.` Mục tiêu, giả thiết và mô hình hai trạng thái (9) | Tách ra phần đầu và Mục 1 | Không còn là mục nội dung |
| `###` Mục tiêu và tiên quyết (11) | Mục tiêu học tập (danh sách); Kiến thức tiên quyết | Hiện là văn xuôi; thiếu số hiệu |
| `###` Giả thiết làm việc và bảng ký hiệu (17) | Bảng ký hiệu (3 cột) và đoạn quy ước | Giả thiết chung đưa vào câu trước bảng |
| `###` Cấu trúc ghi chú (40) | Bỏ; thay bằng Bản đồ chủ đề và đoạn đọc hình roadmap ở đầu Mục 1 | Lấy tài liệu làm chủ ngữ |
| `###` Mô hình hai trạng thái (44) | Mục 1, bài toán mở đầu | Đổi sang bộ số của deck |
| `###` Giá trị của hai chính sách tại trạng thái khởi đầu (59) | Mục 1, Ví dụ 04.1 | Bốn công thức khối rời (63–75) gộp thành `aligned` có câu dẫn |
| `::: exercise` (81) | Mục 2, Bài tập | Chuyển vì nội dung là nhìn trước một bước |
| `## 2.` Giá trị hành động, giá trị tối ưu và hai toán tử Bellman (99) | Chia cho Mục 2 ($q$, $Q_V$), Mục 3 ($v_*$, Bellman tối ưu), Mục 4 ($T_*$) | Đổi thứ tự: khái niệm tối ưu đang đứng trước đánh giá chính sách |
| `###` Tách hành động đầu và phần tiếp diễn (101) | Mục 2, Trực giác | — |
| `###` Giá trị nhìn trước $Q_V$ từ một bảng giá trị (105) | Mục 2, Ví dụ trước Định nghĩa 04.10 | Đang để công thức trước bảng số: đảo lại |
| `###` Định nghĩa $Q_V$ và quan hệ với $q_\pi$ (120) | Mục 2, Định nghĩa 04.10 và đoạn móc nối | — |
| `###` Giá trị tối ưu và cận trên nhỏ nhất (128) | Mục 3, Định nghĩa 04.14 | Đang mở bằng định nghĩa; dòng 136 thiếu căn cứ |
| `###` Phương trình Bellman tối ưu (138) | Mục 3, Định lý 04.18 | — |
| `###` Phân biệt max và argmax (150) | Mục 2, Nhận xét sau Định nghĩa 04.11 | — |
| `###` Hai toán tử Bellman (158) | $T_\pi$ sang Mục 1 (Định nghĩa 04.1); $T_*$ sang Mục 4 (Định nghĩa 04.20) | — |
| `::: exercise` (168) | Mục 4, Bài tập củng cố | — |
| `## 3.` Đánh giá giá trị của một chính sách cố định (184) | `## 1. Đánh giá chính sách` | Phải mở bằng kết quả Bài 03 và bài toán có số |
| `###` Giá trị dài hạn của $\pi_0$ (186) | Mục 1, Vấn đề và Trực giác | — |
| `###` Hai phương trình Bellman và nghiệm chính xác (190) | Mục 1, Ví dụ 04.3 | Nhắc lại Bài 03 |
| `###` Dạng ma trận và tính khả nghịch (202) | Mục 1, Mệnh đề 04.6 và proof chia bước | Dòng 216 là một đoạn dài: tách thành bước |
| `###` Xấp xỉ bằng các lượt quét đồng bộ (218) | Mục 1, Ví dụ 04.2 | Phải đứng trước Định nghĩa 04.1 |
| `###` Hai lịch cập nhật (231) | Mục 1, Nhận xét 04.9; phần lịch sang Mục 5 | Dòng 233 nhiều ý |
| `###` Quy trình đánh giá chính sách (235) | Mục 1, Thuật toán 04.8 trong khối `algorithm` | — |
| `::: exercise` (248) | Mục 1, Bài tập 04.1 | Đổi sang dữ kiện B08 |
| `## 4.` Cải thiện chính sách và lặp chính sách (264) | `## 2.` và `## 3.` | Tách theo mạch 3 và mạch 4 |
| `###` Cải thiện hành động tại $s_1$ (266) | Mục 2, Vấn đề và Ví dụ 04.4 | Đoạn nêu nhầm lẫn thường gặp tốt: giữ |
| `###` Cải thiện bằng phép nhìn trước một bước (274) | Mục 2, Ví dụ 04.5 | — |
| `###` Đánh giá lại $\pi_1$ và $\pi_2$ (285) | Mục 3, Ví dụ 04.6 | — |
| `###` Quy tắc tham lam với điều khoản giữ hòa (297) | Mục 2, Định nghĩa 04.11 và Bổ đề 04.3 | Đoạn đơn điệu (305) chuyển thành Bổ đề 04.3 ở Mục 1 |
| `###` Định lý cải thiện chính sách (307) | Mục 2, Định lý 04.12 và proof | Định lý hiện ở dạng "**Định lý.**" trong đoạn văn, chưa có 4 phần |
| `###` Quy trình lặp chính sách (333) | Mục 3, Thuật toán 04.16; dòng 331 thành Mệnh đề 04.17 | — |
| `::: exercise` (344) | Mục 2, Bài tập 04.2 | — |
| `## 5.` Lặp giá trị (360) | `## 4. Lặp giá trị` | — |
| `###` Chi phí đánh giá từng chính sách (362) | Mục 4, Vấn đề | Thêm ví dụ 44 lượt quét |
| `###` Một lượt quét đầu tiên (370) | Mục 4, Ví dụ 04.8 | Thêm hai lượt quét trên mô hình hai trạng thái trước dãy năm ô |
| `###` Giá trị lan dần từ đích (383) | Mục 4, Ví dụ 04.9 | Áp dụng sau phần hình thức |
| `###` Quy tắc lặp giá trị (404) | Mục 4, Định nghĩa 04.20 | Công thức đứng ngay sau heading, không có câu dẫn |
| `###` Quy trình lặp giá trị có kiểm tra dừng (416) | Mục 4, Thuật toán 04.26 | — |
| `###` Trích chính sách từ cùng bảng giá trị (427) | Mục 4, Nhận xét 04.27 | Công thức đứng ngay sau heading |
| `###` Chi phí của một lượt tính (439) | Mục 5, Mệnh đề 04.28 | — |
| `::: exercise` (455) | Mục 4, Bài tập 04.4 hoặc phần củng cố | — |
| `## 6.` Tính co và các bảo đảm hội tụ (479) | Phân tán sang Mục 1 (co của $T_\pi$, Banach, chặn phần dư) và Mục 4 (co của $T_*$, tồn tại, hội tụ hình học) | Thiếu mục tương ứng một mạch; mở bằng định nghĩa chuẩn |
| `###` Chuẩn vô cùng (481) | Mục 1, Định nghĩa 04.2 và Ví dụ | — |
| `###` Chứng minh tính co của $T_*$ (503) | Mục 4, Bổ đề 04.21 và Mệnh đề 04.22 | Bước chưa in đậm |
| `###` Định lý Banach (527) | Mục 1, Định lý 04.5 | Chưa có chứng minh và chưa có nguồn có số trang |
| `###` $\bar V$ chặn mọi chính sách (533) | Mục 4, chứng minh Định lý 04.23 (Bước 1) | Bất đẳng thức `aligned` chưa có cột căn cứ |
| `###` Đạt cận trên và $\bar V=v_*$ (561) | Mục 4, Định lý 04.23 (Bước 2) | — |
| `###` Hội tụ hình học (573) | Mục 4, Hệ quả 04.24 | Số 64 tự đặt; đổi thành $30\cdot0{,}9^k$ |
| `###` Phần dư Bellman và ngưỡng dừng (585) | Mục 1, Hệ quả 04.7 cho $\Delta_\pi$; Mục 4, Hệ quả 04.25 cho $\Delta_*$ | Dòng 587 là câu mảnh |
| `###` Giới hạn của mô hình dạng bảng: CartPole (605) | Mục 5, Ví dụ 04.12, Nhận xét 04.32 và Tình huống 04.2 | — |
| `::: exercise` (617) | Mục 4, phần củng cố | — |
| `## 7.` Chọn quy trình và đánh giá kết quả (631) | Tóm tắt chương và Mục 5 | Không ứng với mạch nào |
| `###` Bảng so sánh ba phương pháp (633) | Tóm tắt chương (bảng khung chung) | Dòng 643 là đoạn nhiều ý |
| `###` Lời giải cho bài toán hai trạng thái (645) | Mục 3, ứng dụng (Ví dụ 04.6, chứng nhận $Q_{v_*}$) | — |
| `::: exercise` (664) | Mục 4, phần củng cố | — |
| `###` Bài tập tự luyện (676) | Bài tập củng cố và `exercises.md` | Đang chỉ dẫn tới PDF; không có hint và solution |
| `##` Tài liệu tham khảo (682) | Hướng dẫn đọc thêm và tài liệu tham khảo | Bỏ các liên kết `../RL-hk2-2025-2026/` (dòng 678, 686, 687) và liên kết tới deck (685); ghi mục nào dựa trên nguồn nào |

**Đối chiếu 11 thành phần bắt buộc.**

| # | Thành phần | Tình trạng |
|---|---|---|
| 1 | Tiêu đề | Sai tên |
| 2 | Giới thiệu | Có nhưng sai: lấy tài liệu làm chủ ngữ |
| 3 | Mục tiêu học tập | Ở dạng văn xuôi, có 3 năng lực |
| 4 | Kiến thức tiên quyết | Văn xuôi, không có số hiệu |
| 5 | Bảng ký hiệu | 2 cột, 12 dòng |
| 6 | Bản đồ chủ đề | Thiếu; chỉ có comment `note-topic-id` |
| 7 | Các mục nội dung | Không ứng với mạch; Mục 1 không có hình cấu trúc chương |
| 8 | Tình huống áp dụng và ứng dụng | Thiếu |
| 9 | Tóm tắt chương | Thiếu |
| 10 | Bài tập củng cố | Chỉ có danh sách tham chiếu PDF |
| 11 | Đọc thêm và tài liệu tham khảo | Có nhưng sai dạng |

**Bản đồ chủ đề đề xuất.**
- **Cốt lõi:** đánh giá chính sách (Mục 1), cải thiện chính sách (Mục 2), lặp chính sách (Mục 3), lặp giá trị (Mục 4).
- **Cầu nối:** nhắc lại phương trình Bellman kỳ vọng và $q_\pi$ của Bài 03 (Mục 1–2); chuẩn vô cùng và định lý Banach (Mục 1).
- **Bổ sung:**
  - tồn tại chính sách tối ưu trên lớp chính sách phụ thuộc lịch sử (Mục 4; Puterman §6.2; hw3 Bài 3);
  - dạng ma trận (hw3 Bài 6);
  - quy hoạch động bất đồng bộ, GPI và CartPole rời rạc hóa (Mục 5; notebook).
- **Đọc thêm:** lặp chính sách cải biên (Puterman §6.5; notebook nhiệm vụ 7); chặn Singh–Yee (notebook 7.5); trường hợp $\gamma=1$ (Sutton–Barto, Ví dụ 4.1).

### B2. Kế hoạch đánh số môi trường

Dùng ba bộ đếm riêng:
- **Bộ đếm chung** (Định nghĩa, Định lý, Mệnh đề, Bổ đề, Hệ quả, Nhận xét, Thuật toán): 04.1 đến 04.32.
- **Ví dụ:** Ví dụ 04.1 đến 04.13.
- **Bài tập:** Bài tập 04.k, dùng chung với `exercises.md`.

Trong bảng, "dòng" là vị trí nội dung đang nằm ngầm trong văn bản hiện tại.

| Mục | Khối `:::` và số hiệu |
|---|---|
| 1. Đánh giá chính sách | `example` 04.1 (lợi tức từ $s_1$: 3,71); `example` 04.2 (hai lượt quét $(1,2)$, $(1{,}9;2{,}9)$); `definition` 04.1 (toán tử $T_\pi$, lượt quét đồng bộ; dòng 158–164); `definition` 04.2 (chuẩn vô cùng, phần dư $\Delta_\pi$; 481–485, 599); `lemma` 04.3 (tính đơn điệu của $T_\pi$; 305); `proposition` 04.4 ($T_\pi$ co; 525); `theorem` 04.5 (Banach trên $(\mathbb R^n,\lVert\cdot\rVert_\infty)$; 527–531; chứng minh ngoài phạm vi, kèm nguồn có trang); `proposition` 04.6 (dạng ma trận, $I-\gamma P_\pi$ khả nghịch; 202–216); `corollary` 04.7 (chặn $\Delta_\pi/(1-\gamma)$ và chặn cho $W$; 599–603); `algorithm` 04.8 (đánh giá chính sách đồng bộ; 235–246); `example` 04.3 ($v_{\pi_0}=(10,11)$ so với bảng lặp); `remark` 04.9 (đồng bộ và tại chỗ; bootstrapping; kết thúc lượt khác dừng thuật toán; 231–233, 246) |
| 2. Cải thiện chính sách | `example` 04.4 (hai nhánh tại $s_1$: 11 và 12,9); `definition` 04.10 ($Q_V$, $Q_{v_\pi}=q_\pi$; 120–126); `definition` 04.11 (chính sách tham lam, quy tắc giữ hòa; 297–303, 150–156); `theorem` 04.12 (cải thiện chính sách; 307–329), `proof` chia bước; `example` 04.5 ($\pi_1=(a,b)$, $v_{\pi_1}=(10,30)$); `remark` 04.13 (12,9 không phải $v_{\pi_1}(s_1)$; 272) |
| 3. Lặp chính sách | `example` 04.6 (ba vòng, $(27,30)$, bảng $Q_{v_*}$; 285–295, 645–662); `definition` 04.14 ($v_*$, $q_*$ lấy sup trên $\Pi$, chính sách tối ưu; 128–136); `definition` 04.15 (chính sách ổn định); `algorithm` 04.16 (lặp chính sách; 333–342); `proposition` 04.17 (dừng hữu hạn; 331); `theorem` 04.18 (phương trình Bellman tối ưu; chính sách ổn định là tối ưu trên lớp chính sách dừng; 138–148); `remark` 04.19 (đánh giá gần đúng không chứng nhận; nội dung D05–D06) |
| 4. Lặp giá trị | `example` 04.7 (44 lượt quét); `example` 04.8 (hai lượt quét $(1,3)$, $(2{,}7;5{,}7)$); `definition` 04.20 ($T_*$, $\Delta_*$; 404–412); `lemma` 04.21 ($\lvert\max x-\max y\rvert\le\max\lvert x-y\rvert$; 509–513); `proposition` 04.22 ($T_*$ co; 503–523); `theorem` 04.23 (tồn tại chính sách tối ưu dừng, xác định; $\bar V=v_*$ kể cả trên lớp phụ thuộc lịch sử; 533–571); `corollary` 04.24 (hội tụ hình học; 573–583); `corollary` 04.25 (chặn theo $\Delta_*$, $\eta=(1-\gamma)\varepsilon$; 585–599); `algorithm` 04.26 (lặp giá trị có kiểm tra dừng; 416–425); `example` 04.9 (dãy năm ô, $V_4=v_*$); `remark` 04.27 ($\pi_V$ có thể đã tối ưu khi bảng còn xa nghiệm; $V_k$ không là giá trị của chính sách nào; 412, 427–435) |
| 5. Lịch cập nhật và giới hạn | `proposition` 04.28 (chi phí $O(n^2m)$, $O(nmd)$, $O(n^3)$; 439–451); `example` 04.10 (tại chỗ: $(1;2{,}9)$; dãy năm ô một lượt); `algorithm` 04.29 (lặp giá trị bất đồng bộ; hiện chưa có trong ghi chú); `theorem` 04.30 (hội tụ bất đồng bộ; chứng minh ngoài phạm vi, nguồn có trang); `definition` 04.31 (GPI); `example` 04.11 (CartPole 324 ô); `example` 04.12 (một lượt quét tại ô 71 của notebook); `remark` 04.32 (gộp ô không bảo đảm Markov; tách sai số lặp khỏi sai số mô hình; 605–615) |
| Tình huống áp dụng | `application` Tình huống 04.1, 04.2 (và 04.3 nếu dùng); `example` 04.13 dự phòng |

### B3. Bảng kiểm "Tiêu chuẩn thứ nhất" và "Trình bày sáng sủa"

| Tiêu chí | Vi phạm (dòng) | Cách sửa |
|---|---|---|
| Giọng kể "chúng ta/ta" | Toàn tệp dùng giọng khách quan: 0 lần "chúng ta" và 0 lần "ta". Ví dụ dòng 188 "Xét chính sách $\pi_0$…", dòng 227 "Lượt một: …" | "chúng ta" cho câu kế hoạch và lựa chọn ("Để so sánh các hành động, chúng ta cần $v_{\pi_0}$"); "ta" trong tính toán ("Thế $x=10$, ta được $y=11$"); giữ câu khách quan trong các khối hình thức |
| Tài liệu làm chủ ngữ | Dòng 5 "Ghi chú bổ sung … Nội dung gồm…"; dòng 13 "Ghi chú phát triển ba năng lực"; dòng 19 "Các kết quả trong ghi chú dùng…"; dòng 42 "Ghi chú gồm bảy phần"; dòng 69 "Phần này chiết khấu…" (chủ ngữ mơ hồ) | Viết lại với chủ ngữ là đối tượng toán học hoặc "chúng ta" |
| Vấn đề trước công cụ | §2 mở bằng công thức $Q_V$ trước bảng số (dòng 109 trước 113); dòng 128–136 mở $v_*$ bằng định nghĩa; §6 mở bằng định nghĩa chuẩn (481–485); §7 mở bằng bảng (635) | Mỗi `##` mở bằng bài toán có số (ví dụ: "Tại $s_0$, $a$ cho 1 còn $b$ cho 0 nhưng dẫn tới $s_1$…") |
| Công thức có câu dẫn và câu đọc | Dòng 63–75: bốn khối số học rời; dòng 406 và 430: công thức đứng ngay sau heading; dòng 491–499: bốn khối liền nhau với câu mảnh "nên chênh còn 2" | Gộp thành `aligned` có câu dẫn; thêm câu đọc sau công thức |
| Câu mảnh và dòng "Liên hệ:" | Dòng 587 "Định nghĩa phần dư"; các dòng 79, 166, 260, 356, 381, 414, 437, 453 dạng "Khái niệm/Thuật toán/Cơ chế liên quan: …; Sutton–Barto…" | Bỏ; nguồn chuyển sang "Hướng dẫn đọc thêm" và dẫn tại chỗ trong câu |
| Bước suy diễn có căn cứ | Dòng 136 ("Tính chất Markov cho phép… dẫn tới $v_*=\max q_*$" không có chứng minh, dựa vào kết quả sau); dòng 328 (chuyển giới hạn không nêu căn cứ); dòng 529 (Banach không chứng minh, không có nguồn trang); dòng 545–549 (`aligned` không có cột căn cứ) | Thêm `&&\text{(…)}` cho từng dấu; với Banach ghi "Chứng minh nằm ngoài phạm vi học phần" kèm nguồn có trang; $v_*=\max q_*$ chuyển thành hệ quả của Định lý 04.23 |
| Tham chiếu ra ngoài tệp | Dòng 5 (bộ trang chiếu, $\gamma=0{,}9$); dòng 685–687 và 678 (liên kết tới deck và tới `../RL-hk2-2025-2026/*.pdf`, hỏng khi phát hành); tham chiếu tiến "phần 6" ở các dòng 134, 148, 156, 164, 179, 244, 331, 425 | Dẫn bằng số hiệu; tham chiếu tiến phải nêu điều đang tạm chấp nhận; bỏ liên kết tới tệp nguồn chưa theo dõi |
| Một ý một đoạn | Dòng 216 (ma trận cộng chứng minh khả nghịch trong một đoạn khoảng 150 từ); dòng 233 (lịch, điều kiện hội tụ và ngân sách); dòng 643 (bảng chọn phương pháp, mô hình, bootstrapping) | Tách đoạn, mỗi đoạn tối đa khoảng 4 câu |
| Chứng minh theo bước | Proof 311–329 không có nhãn bước; 509–523 viết "Bước một/hai" trong văn xuôi; 533–571 không có nhãn | Dùng `**Bước k (…)**` trên dòng riêng |
| Phát biểu tách 4 phần | Dòng 309: định lý trong đoạn văn | Khối `theorem` gồm Giả thiết, Kết luận, Điều kiện áp dụng, Phạm vi |
| Đọc bằng lời và "Bỏ giả thiết" | Định lý cải thiện và tính co chưa có danh sách "Bỏ <giả thiết>: phản ví dụ" | Ví dụ: bỏ đánh giá chính xác → D06 ($(a,b)$ tham lam theo $V=0$ nhưng không tối ưu); bỏ $\gamma<1$ → Sutton–Barto Ví dụ 4.1 hoặc chặn $1/(1-\gamma)$ mất nghĩa; bỏ điều kiện bao phủ → F06 ($V(s_0)\to10$) |
| Hình được đọc | Dòng 57 (`two-state.svg`) và 229 (`policy-evaluation.svg`) không có đoạn đọc | Thêm đoạn nói cần nhìn gì trên hình; đổi sang `dp04-*.svg` của deck |
| Ngoặc lồng | Dòng 77 "($10 = 0{,}5\cdot20$, với 20 là …)" | Tách thành câu riêng |
| Nhầm lẫn thường gặp | Đã có ở dòng 272 và 150–156: giữ | Bổ sung cho $T_\pi$ (đọc ô mới trong cùng lượt), phần dư (khác sai số thật) và GPI |

### B4. Phần cần thêm

**Đoạn móc nối.**
- Khái niệm với khái niệm: $T_\pi$ với phương trình Bellman kỳ vọng của Bài 03; $Q_V$ với $q_\pi$; $T_*$ với $T_\pi$ (cực đại thay cho trung bình); bất đồng bộ với đồng bộ.
- Kết quả với kết quả: Định lý 04.12 cần Bổ đề 04.3 và Mệnh đề 04.4; Mệnh đề 04.17 suy từ phần tăng nghiêm của 04.12; Hệ quả 04.25 là phiên bản $T_*$ của Hệ quả 04.7.
- Thuật toán với thuật toán: lặp giá trị là lặp chính sách với một lượt quét đánh giá; bất đồng bộ là lặp giá trị với lịch tổng quát.
- Mở chương dẫn Bài 03; kết chương dẫn Bài 05–06.

**Đoạn "Trong thực hành", dùng số liệu của notebook.**
- **Sau Thuật toán 04.8.**
  - $V$ có cỡ $(n,)$ với $n=324$, `V_plus` cỡ $(n+1,)$.
  - Giải đúng hệ cho $\lVert T_\pi v-v\rVert=2{,}1\cdot10^{-14}$.
  - Với $\eta=10^{-4}$, thuật toán dừng ở $k=218$ với sai số thật $2{,}2\cdot10^{-3}$, dưới chặn $9{,}6\cdot10^{-3}$.
  - Với $K=100$, nhãn là "hết ngân sách", chặn 1,85 trong khi sai số thật 0,42.
- **Sau Định lý 04.12.** 173 ô đổi hành động sau lần cải thiện đầu; phép kiểm $v_{\pi_1}\ge v_{\pi_0}$ đúng tại mọi ô.
- **Sau Thuật toán 04.16.** Số ô đổi hành động qua các vòng là 173, 87, 23, 10, 1, 0; $\Delta_*(v_\pi)=4\cdot10^{-14}$; với $I_{\max}=2$, nhãn là "chưa chứng nhận".
- **Sau Hệ quả 04.24–04.25.**
  - Số lượt quét đo được so với chặn theo $\gamma^k$: 65 so với 66 khi $\gamma=0{,}9$; 736 so với 917 khi $\gamma=0{,}99$.
  - $\lVert V-v_*\rVert=7{,}84\cdot10^{-3}\le9{,}88\cdot10^{-3}$.
  - $\pi_V$ trùng chính sách của lặp chính sách; có 3 ô gần hòa.
- **Sau Định lý 04.30.** Notebook có sẵn `value_iteration_in_place` (nhiệm vụ 6).
- **Sau Nhận xét 04.32.** Dự đoán 84,47 so với thực tế 95,38; thay hạt giống mô hình cho tổng thưởng 219–500; 98/100 lượt kết thúc vì $\lvert x\rvert>2{,}4$.

**Tình huống áp dụng.**
- **Tình huống 04.1 (gắn bài thực hành): lập kế hoạch trên CartPole rời rạc hóa.**
  - Mô hình hóa thành MDP $(\mathcal S^+,\{0,1\},\hat p,\hat r,0{,}99)$.
  - Kiểm giả thiết trên MDP ước lượng: hữu hạn, $\hat r=1$ bị chặn, $\gamma<1$.
  - Áp dụng Thuật toán 04.16 và 04.26.
  - Kết quả: 343,4 ± 9,2 so với 22,5 và 43,6.
- **Tình huống 04.2 (giả thiết không thỏa): chứng nhận Bellman trên mô hình gộp không chuyển sang môi trường liên tục.**
  - Giả thiết bị vi phạm: tính Markov khi gộp ô; mô hình chỉ là ước lượng; cắt ngắn ở 500 bước.
  - Hậu quả quan sát được: độ lệch 10,9 giữa dự đoán và thực tế; thay hạt giống mô hình cho 219–500.
- **Tình huống 04.3 (tùy chọn):** $\gamma=1$ theo Sutton–Barto Ví dụ 4.1.

**Các phần còn lại.**
- Mỗi `##` kết bằng đoạn văn xuôi gồm ba điều: đã thu được gì (có số hiệu), còn thiếu gì, mục sau làm gì.
- **Tóm tắt chương:** một đoạn 5–8 câu; định nghĩa và kết quả theo mục; công thức cần nhớ ($T_\pi$, $T_*$, chặn phần dư, $\eta=(1-\gamma)\varepsilon$); giả thiết hay bị bỏ quên (đánh giá chính xác, giữ hòa, bao phủ, mô hình đúng, $\gamma<1$).
- **Bài tập củng cố ba mức** (không trùng `exercises.md`):
  - nhận biết: hw3 Bài 1 ($v_\pi$ so với $q_\pi$), Bài 2 (Bellman đánh giá so với Bellman tối ưu);
  - tính toán hoặc chứng minh: hw3 Bài 5 ($v_\pi=\sum_a\pi q_\pi$), Bài 3 (tồn tại chính sách tối ưu, dựa vào Định lý 04.23);
  - vận dụng: hw3 Bài 4 (đồng bộ và bất đồng bộ), Bài 8 ([Tìm hiểu] trạng thái liên tục).

**Độ dài.** Hiện có khoảng 9 700 từ văn xuôi (10 921 token kể cả công thức), trong khoảng 8 000–20 000 nhưng thiếu các thành phần trên. Đích khoảng 16 000–18 000 từ:
- cộng khoảng 1 200 từ cho phần đầu;
- cộng khoảng 4 000 từ cho móc nối, "Trong thực hành", đọc bằng lời và nhận xét ở năm mục;
- cộng khoảng 1 500 từ cho tình huống;
- cộng khoảng 600 từ cho tóm tắt;
- cộng khoảng 1 500 từ cho bài tập củng cố;
- trừ khoảng 800 từ siêu ngôn ngữ và lặp.

### B5. Giáo trình cần đối chiếu (ghi vào review-log cho từng mục)

Kho không có bản Puterman, Bertsekas, Szepesvári hay Sutton–Barto, nên số trang (trừ các trang Sutton–Barto deck đã dẫn) phải được xác minh trước khi ghi.

| Mục | Giáo trình và vị trí |
|---|---|
| 1. Đánh giá chính sách | Sutton–Barto (2018) §3.5 và §4.1 tr. 74–76 (đánh giá lặp, tại chỗ, Ví dụ 4.1); Puterman (1994) §6.1 (đánh giá, dạng ma trận, chuỗi Neumann); Szepesvári (2010) Phụ lục A (ánh xạ co, Banach); *Học máy thống kê* ch. 06, mục "Thuật toán tối ưu quy hoạch động", tiểu mục "Giá trị tối ưu" (giọng kể; bảng tương ứng $V^\pi$, $T(s,a,s')$, $R(s,a,s')$) |
| 2. Cải thiện chính sách | Sutton–Barto §4.2 tr. 76–79, công thức (4.7)–(4.9), Bài tập 4.3; Puterman §6.4 (bước cải thiện); *Học máy thống kê* tiểu mục "Giá trị trạng thái – hành động" |
| 3. Lặp chính sách | Sutton–Barto §4.3 tr. 80–82, Bài tập 4.4 (giữ hòa); Puterman §6.2 (phương trình tối ưu) và §6.4 (hội tụ hữu hạn); Bertsekas (2019), chương bài toán vô hạn bước có chiết khấu (số mục cần xác minh); *Học máy thống kê* "Thuật toán lặp chính sách" |
| 4. Lặp giá trị | Sutton–Barto §4.4 tr. 82–84, (4.10); Puterman §6.3. Lưu ý: điều kiện dừng của Puterman nhắm chính sách $\varepsilon$-tối ưu, khác chặn giá trị $\eta=(1-\gamma)\varepsilon$ của bài, cần ghi rõ. Thêm Szepesvári Phụ lục A; *Học máy thống kê* "Thuật toán lặp giá trị" (chứng minh co) |
| 5. Lịch cập nhật và giới hạn | Sutton–Barto §4.5–4.7 tr. 85–88; Bertsekas và Tsitsiklis (1996), Chương 2 (hội tụ bất đồng bộ, cần xác minh; Sutton–Barto dẫn Bertsekas và Tsitsiklis 1989); Puterman §6.5 (lặp chính sách cải biên, đọc thêm); notebook |
| Tình huống và Ứng dụng | Notebook các mục 5–8; Sutton–Barto Ví dụ 4.1; Bài 05 (TD), Bài 06 (điều khiển phi mô hình), Bài 08 (DQN: mục tiêu $r+\gamma\max Q$ là phiên bản lấy mẫu của $T_*$) |

### B6. Bảng ký hiệu đề xuất và các chỗ lệch

**Bảng ký hiệu (3 cột, khoảng 22 dòng).**

| Ký hiệu | Ý nghĩa | Miền hoặc kiểu |
|---|---|---|
| $\mathcal S$, $n$ | Tập trạng thái chưa kết thúc; $n=\lvert\mathcal S\rvert$ | Hữu hạn |
| $s_{\mathrm{term}}$, $\mathcal S^+$ | Trạng thái kết thúc; $\mathcal S\cup\{s_{\mathrm{term}}\}$ | — |
| $\mathcal A(s)$, $m$ | Tập hành động hợp lệ tại $s$; $m=\max_s\lvert\mathcal A(s)\rvert$ | Hữu hạn, khác rỗng |
| $\mathcal R$ | Tập phần thưởng | Hữu hạn, bị chặn |
| $S_t, A_t, R_{t+1}$ | Trạng thái, hành động, phần thưởng | $t\in\mathbb N$ là bước tương tác |
| $p(s',r\mid s,a)$ | Mô hình chuyển–thưởng | Phân phối trên $\mathcal S^+\times\mathcal R$ |
| $P(s'\mid s,a)$, $\bar r(s,a)$ | Xác suất chuyển biên; thưởng kỳ vọng | $[0,1]$; $\mathbb R$ |
| $\gamma$ | Hệ số chiết khấu | $[0,1)$ |
| $G_t$ | Lợi tức | Biến ngẫu nhiên thực |
| $\pi(a\mid s)$, $\pi(s)$ | Chính sách Markov dừng; dạng xác định | Phân phối trên $\mathcal A(s)$ |
| $\Pi$ | Lớp mọi chính sách, kể cả phụ thuộc lịch sử | — |
| $v_\pi$, $q_\pi$ | Giá trị trạng thái và giá trị hành động | $\mathbb R^n$; $\mathbb R$ trên các cặp $(s,a)$ |
| $v_*$, $q_*$, $\pi_*$ | Giá trị tối ưu; chính sách tối ưu | — |
| $V$, $V_k$, $W$ | Bảng giá trị; bảng sau $k$ lượt quét; bảng tạm | $\mathbb R^n$, mở rộng bằng 0 tại $s_{\mathrm{term}}$ |
| $k$, $i$ | Chỉ số lượt quét; chỉ số vòng cải thiện | $\mathbb N$ |
| $Q_V(s,a)$ | Giá trị nhìn trước từ bảng $V$ | $\mathbb R$ |
| $T_\pi$, $T_*$ | Toán tử Bellman đánh giá và tối ưu | $\mathbb R^n\to\mathbb R^n$ |
| $P_\pi$, $r_\pi$ | Ma trận chuyển và vectơ thưởng dưới $\pi$ | $n\times n$; $\mathbb R^n$ |
| $\lVert\cdot\rVert_\infty$ | Chuẩn vô cùng | — |
| $\Delta_\pi(V)$, $\Delta_*(V)$ | Phần dư Bellman | $\ge0$ |
| $\eta$, $\varepsilon$ | Ngưỡng phần dư; sai số yêu cầu | $>0$ |
| $K$, $I_{\max}$, $\pi_V$ | Ngân sách lượt quét; ngân sách vòng; chính sách tham lam theo $V$ | — |

Sau bảng, nêu ba tương ứng:
- với *Học máy thống kê*: $V^\pi$, $Q^\pi$, $T(s,a,s')$, $R(s,a,s')$ và $\mathcal T$;
- với notebook: $\hat p(s'\mid s,a)$, $\hat r(s,a)$, $n=324$;
- $\theta$ là góc của cột CartPole, nên ngưỡng phần dư dùng ký hiệu $\eta$.

**Các chỗ lệch.**
1. **Bộ số.** Ghi chú dùng $(2,-1,5,10)$, $\gamma=0{,}5$, lưới thưởng 24 và chặn 64; deck dùng $(1,0,2,3)$, $\gamma=0{,}9$, thưởng 10. Đề xuất ghi chú dùng bộ số của deck và nguồn. Cần hỏi người dùng (xem D).
2. **Định nghĩa $v_*$.** Ghi chú lấy $\sup$ trên $\Pi$ kể cả chính sách phụ thuộc lịch sử; deck D04 lấy $\max$ trên chính sách dừng. Thống nhất theo cách của ghi chú, deck ghi "mở rộng ở Định lý 04.23".
3. **"Lượt".** Deck và ghi chú dùng "lượt" cho sweep; notebook và Bài 05 dùng "lượt" cho episode và "lượt quét" cho sweep. Đổi deck và ghi chú sang "lượt quét".
4. **Lợi tức.** Bài 03, deck và ghi chú Bài 04 dùng "tổng thưởng chiết khấu"; Bài 05 và mẫu dùng "lợi tức". Đề xuất "lợi tức (return), còn gọi là tổng thưởng chiết khấu".
5. **Quy tắc hòa.** Deck viết "quy tắc phá hòa"; ghi chú và notebook viết "quy tắc giữ hòa". Đề xuất "quy tắc giữ hòa (tie-breaking)".
6. **Giá trị tiếp nối.** Deck viết "giá trị tiếp nối"; ghi chú viết "giá trị tiếp diễn". Chọn một cách gọi.
7. **Ký hiệu xác suất chuyển biên.** Ghi chú dòng 449 viết $p(s'\mid s,a)$ và $r(s,a)$, trùng chữ với $p(s',r\mid s,a)$. Đổi sang $P$ và $\bar r$ như deck F01.
8. **Nguồn bài tập.** Ghi chú dẫn hw3 (Bài 3, 6, 7, 9); deck G03 dẫn hw04 "tr. 1". Cả hai đều hợp lệ: hw3 là "Giải bài toán MDP", còn hw04 có Bài 1 (hai trạng thái) và Bài 10 (dãy trơn trượt). Ghi số bài cụ thể.
9. **Tên $\pi_0$.** Notebook gọi $\pi_0$ là luật theo dấu góc, trùng tên với $\pi_0=(a,a)$ của deck. Trong Tình huống gọi là "chính sách theo dấu góc".
10. **Tham chiếu từ Bài 05.** Ghi chú Bài 05 dòng 431 viết "quy ước Bài 04". Sau khi đánh số, cập nhật thành số hiệu (ngoài phạm vi đợt này, ghi nhật ký).

---

## C. Bài tập (`exercises.md` mới)

Bộ đếm Bài tập dùng chung với ghi chú. Bài 04.1–04.6 giữ số hiệu và lời giải của ghi chú, trùng trang chiếu. Bài 04.7–04.9 nằm ở phần Bài tập củng cố của ghi chú, không chép lại. Bài 04.10–04.15 chỉ có trong tệp này.

| Số hiệu | Mạch | Mức | Đối tượng / dữ kiện tóm tắt | Trùng trang chiếu hay mới | Năng lực đo |
|---|---|---|---|---|---|
| 04.1 | 2 | Tính toán | Mô hình hai trạng thái, $V_2=(1{,}9;2{,}9)$ → $V_3=(2{,}71;3{,}71)$, $\Delta=0{,}81$, chặn 8,1 bằng sai số thật | Trùng B08/B08b | Lượt quét đồng bộ; chặn phần dư |
| 04.10 | 2 | Chứng minh | Dạng ma trận và tính khả nghịch của $I-\gamma P_\pi$; kiểm trên $\pi_0$ ra $(10,11)$ (hw3 Bài 6) | Mới | Chứng minh qua hệ thuần nhất |
| 04.2 | 3 | Tính toán | $v_{\pi_1}=(10,30)$ → $q(s_0,a)=10$, $q(s_0,b)=27$, chọn $b$ | Trùng C07/C07b | Cải thiện tham lam |
| 04.11 | 3 | Chứng minh | Tính đơn điệu của $T_\pi$ và $T_*$ (hw3 Bài 7) | Mới | Dùng giả thiết xác suất không âm và $\gamma\ge0$ |
| 04.3 | 4 | Nhận biết / tính toán | $\pi=(a,b)$ với bảng $V=(0,0)$ → nhìn trước $1,0,2,3$; kết luận "tối ưu" sai | Trùng D06/D06b | Phân biệt dừng gần đúng với chứng nhận |
| 04.12 | 4 | Tính toán | MDP ba trạng thái ngẫu nhiên (hw3 Bài 9), $\gamma=0{,}9$. Lặp giá trị: $V_1=(1,2,2)$, chính sách tham lam $(b,a,a)$. Lặp chính sách từ $\pi_0=(b,a,b)$: $v_{\pi_0}=(10,11,9)$, $\pi_1=(b,a,a)$ (đã tính lại) | Mới | Lặp chính sách trên mô hình ngẫu nhiên |
| 04.4 | 5 | Tính toán | Dãy năm ô, $V_4=(4{,}58;6{,}2;8;10;0)$ → $T_*V_4=V_4$, $\Delta_*=0$, đi phải | Trùng E08/E08b | Toán tử $T_*$; điểm bất động |
| 04.13 | 5 | Vận dụng | Dãy năm ô trơn trượt (hw04 Bài 10; xác suất 0,8/0,1/0,1): $V_1=(-1;-1;-1;7{,}8;0)$, $V_2(c_3)=4{,}436$; chọn $\eta$ cho $\varepsilon=0{,}1$ | Trùng đề G03 (bài tự làm) | Lập kỳ vọng từ mô hình ngẫu nhiên; chọn ngưỡng |
| 04.5 | 6 | Tính toán | Chỉ cập nhật $s_0$ → $V(s_0)\to10$, $V(s_1)=0$ | Trùng F06/F06b | Điều kiện bao phủ của lịch bất đồng bộ |
| 04.14 | 6 | Vận dụng, [Lập trình] | Notebook mục 7.4 và nhiệm vụ 5: số lượt quét theo $\gamma\in\{0{,}9;0{,}95;0{,}99;0{,}995\}$ so với chặn $\gamma^k$ (65/66, 143/149, 736/917, 1315/1976) | Mới | Đối chiếu bảo đảm lý thuyết với số đo |
| 04.15 | 6 | Vận dụng, [Lập trình] | Notebook nhiệm vụ 7: lặp chính sách cải biên với $m\in\{1,5,20\}$; số vòng và số phép áp dụng toán tử; bảo đảm dừng hữu hạn mất khi đánh giá không chính xác | Mới | Vai trò của đánh giá chính xác |
| 04.6 | 7 | Vận dụng (tổng hợp) | $U=(10,30)$, $V=(27,30)$ → $T_*U=(27,30)$, $\Delta_*(U)=17$, chặn 170; $T_*V=V$ | Trùng G04/G04b | Chứng nhận tối ưu; phân biệt chặn với sai số thật |

Bảng trên phủ đủ năm mạch nội dung 2–6 và mạch 7. Có bốn bài vận dụng: 04.13, 04.14, 04.15 và 04.6. Theo mẫu, tệp mở bằng bảng `Mạch | Mở phần | Bài tập` với liên kết `#/N/1`.

---

## D. Rủi ro, thứ tự thực hiện và câu hỏi cho người dùng

### Thứ tự thực hiện

Theo `prompt_lecture_note_deck.md`, làm theo ba giai đoạn tuần tự.

1. **Giai đoạn I: ghi chú.**
   - Viết lại `lecture-note.md` theo B1–B6.
   - Tác tử rà toán tính lại mọi số: $(10,11)$, $(10,30)$, $(27,30)$, $V_{1..4}$ của dãy năm ô, 44 lượt quét, 3,71; hw3 Bài 9; số liệu dãy trơn trượt.
   - Kiểm tra theo bảng "Kiểm định ghi chú bài giảng"; viewer không có lỗi KaTeX.
   - Commit `feat(materials-04)`.
2. **Giai đoạn II: deck.** Thực hiện A1–A5. Thêm 6 trang tiêu đề mạch và khoảng 20 trang mới hoặc trang tách. Đồng bộ outline, storyboard (ghi số âm tiết trước và sau cho 15 trang) và review-log. Chạy Playwright ở 1600×900 và 390×844, kiểm `#/N` khớp trang "Nội dung".
3. **Giai đoạn III: `exercises.md`.** Viết bộ bài ở phần C. Lời giải các bài trùng trang chiếu phải cho cùng kết quả với trang. Cập nhật index: nhóm **Bài tập** chỉ hiện liên kết sau khi tệp đạt kiểm định.

### Rủi ro

- **Rủi ro 1: đổi bộ số của ghi chú.** Việc này đảo quyết định đã chấp nhận ngày 2026-09-28 (review-log dòng 118, 673) và làm 5 SVG của ghi chú hết dùng: `two-state.svg`, `policy-evaluation.svg`, `gridworld.svg`, `convergence.svg`, `cartpole.svg`. Có thể thay bằng `dp04-*.svg`; riêng `convergence.svg` cần vẽ lại theo $30\cdot0{,}9^k$.
- **Rủi ro 2: 120 phút với khoảng 71 trang.** Nếu vượt thời lượng, chuyển B07 (ma trận), D05 và F04 sang ghi chú.
- **Rủi ro 3: Bài 03 chưa đánh số.** Các dòng "Nhắc lại:" phải phát biểu lại kết quả, chưa dẫn được số hiệu 03.k.
- **Rủi ro 4: thuật ngữ.** Đổi "lợi tức", "lượt quét" và "giữ hòa" chạm tới tính nhất quán với Bài 03, nhưng không sửa Bài 03 trong đợt này.
- **Rủi ro 5: số trang trong giáo trình.** Không xác minh được trong kho.

Không cần ngoại lệ raster: mọi hình đã là SVG hoặc vẽ lại được.

### Câu hỏi cho người dùng

1. Có đồng ý cho ghi chú bỏ bộ số riêng ($\gamma=0{,}5$) và dùng bộ số của deck cùng nguồn không? Đề xuất là đồng ý, vì chuẩn mới coi deck là bản tóm lược của ghi chú và yêu cầu ví dụ xuyên suốt.
2. Chọn thuật ngữ nào: "lợi tức (return)" hay "tổng thưởng chiết khấu"; "quy tắc giữ hòa" hay "quy tắc phá hòa"?
3. Có cần nâng cấp ghi chú Bài 03 có số hiệu trước để Bài 04 dẫn được "Định lý 03.k" không, hay tạm phát biểu lại?
4. Kho không có Puterman, Bertsekas, Szepesvári hay Sutton–Barto. Có chấp nhận dẫn ở mức chương và mục không, hay người dùng cung cấp bản sách để ghi số trang?
5. Có chấp nhận deck tăng lên khoảng 71 trang không, hay muốn chuyển thêm nội dung (ma trận, GPI, chi phí) sang ghi chú để giữ khoảng 60 trang?
6. Bài 10 của hw04 (tệp mang tên "Đánh giá chính sách", tuần 4) và Bài 3–9 của hw3 có được dùng làm nguồn chính thức cho `exercises.md` không?