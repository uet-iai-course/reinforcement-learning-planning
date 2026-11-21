# Storyboard Bài 10: TRPO và PPO (dựng lại sau góp ý của tác giả, 2026-11-21)

Bước 3–4 của quy trình dựng deck (`NGUYEN-TAC-HOC-PHAN.md` §3a.E). Thay phần hiện hành của storyboard 2026-11-20; bản cũ giữ ở cuối tệp, mục "Lịch sử (bản 2026-11-20)".

**Đầu vào chuẩn.** Câu chuyện `planning/lec-10/cau-chuyen-deck-2026-11-21.md`; góp ý `gop-y-tac-gia-deck-2026-11-20.md` (#1–#28); tổng hợp `tong-hop-gop-y-2026-11-21.md`; quy tắc TB1–TB33 (§3a), NT1–NT29 phần không bị thay, VP1–VP25; ghi chú `materials/lec-10/lecture-note.md` (bản đã sửa ngày 2026-11-21: bỏ DPO, tổng kết là §7, bài tập PPO-Clip là Bài tập 10.23, `exercises.md` có Bài tập 10.13–10.17 và 10.22, số 10.18–10.21 bỏ trống theo BT4); tinh chỉnh Đ1–Đ13 của TB24–TB33 (`NGUYEN-TAC-HOC-PHAN.md` §3a.F, khối "Tinh chỉnh TB24–TB33", tác giả 2026-11-21). Mọi số được tính lại trong `/tmp/claude-1000/-data-tqlong-lectures/678a7f48-9d80-46cf-a421-67398857f913/scratchpad/deck10-v2/kiem_so.py`.

**Quy ước của tệp.**

- Mã trang theo §5 `NGUYEN-TAC-HOC-PHAN.md`: tiền tố `L10-k-`, bìa `L10-1-01`, trang tiêu đề mạch `L10-k-00`, `id="mach-k"`. Trang giữ cùng chức năng giữ mã cũ; trang mới lấy số kế tiếp số lớn nhất đã dùng trong mạch, không dùng lại mã đã bỏ. Riêng mạch 6 (tổng kết): tiền tố `L10-6-` trước đây thuộc mạch DPO; `L10-6-00` buộc phải dùng lại cho trang tiêu đề mạch, các trang khác lấy `L10-6-10` trở đi để không trùng mã DPO cũ trong nhật ký.
- Mỗi trang có: **Câu** (câu của câu chuyện mạch, `cau-chuyen-deck-2026-11-21.md` §2), **Nhãn** (khối có nhãn trên trang), **Mặt trang** (chữ trong ngoặc kép là chữ lên trang, dạng cuối, đã qua `no-ai-slop` chế độ Edit; người dựng chỉ được rút, không thêm ý), **Dựng dần**, **1 phút** (TB23), **Mới** (≤ 2 phần tử, TB11, TB24), **Nguồn số** (phép tính hoặc trang trước, TB29), **Hình**, **Ghi chú nguồn** (khối của ghi chú, để ở ghi chú diễn giả), **Diễn giả** (ý của ghi chú diễn giả, TB9), **Phút**.
- Ký hiệu theo ghi chú (TB25): phát biểu tổng quát dùng $\pi$ (chính sách cũ) và $\pi'$ (chính sách mới bất kỳ); chính sách ứng viên cụ thể của ví dụ là $\tilde\theta=(\log9;\,0)$, $\tilde\pi=(0{,}9;\,0{,}5)$. Số lần thăm kỳ vọng có chiết khấu $\eta_\pi(s)=\sum_t\gamma^t\Pr_\pi(S_t=s,\,t<T)$ trên trang chiếu; phân bố chiếm dụng chuẩn hóa $\nu^\pi=(1-\gamma)\eta_\pi$ chỉ xuất hiện ở trang định lý chặn cải thiện và các trang KL (như ghi chú, N5).
- Văn học thuật (TB26): "kỳ vọng" cho biến ngẫu nhiên, "trung bình trên bộ đệm" cho mẫu hữu hạn; "chệch", "độ chệch", "phương sai"; không "trung bình" thay "kỳ vọng", không "lệch", "dao động", "đoán/thật", "nơi chính sách tới", "Còn thiếu:", "kiểm:". Nhãn chỉ trong danh sách của `CLAUDE.md` học phần.
- Màu nhấn (TB18, NT25, mỗi màu kèm nét hoặc nhãn): **đỏ** = ngược dấu, sai chiều; **cam, nét đứt** = đại lượng chệch hoặc hàm thay thế; **xanh, nét liền** = giá trị đúng, $J$ thật; **tím** = đại lượng mới của trang, khối đang học trên sơ đồ neo.
- Giả thiết chung (Đ7): phát biểu một lần ở `1-02` với tên "giả thiết chung"; mỗi kết quả ghi "Giả thiết: giả thiết chung; thêm …".
- Dòng phân biệt thuật ngữ (Đ4) dùng nhãn "Lưu ý:" ở trang dùng thuật ngữ lần đầu; dòng tương ứng ký hiệu ↔ số sau kết quả (Đ6) mở bằng "Ở đây".
- Bước của chứng minh trên trang (dòng "Chứng minh." hay trang "Ý tưởng chứng minh") mang đúng số và tên bước của chứng minh trong ghi chú (Đ8); trang ý tưởng chứng minh có một hộp "Câu hỏi:" tự giải thích cho bước then chốt, lời giải ở mảnh sau (Đ9).
- Phép tính cùng khuôn trong bảng ghi đủ ở hàng đầu, từ hàng thứ hai chỉ ghi kết quả hoặc "như hàng trên" (Đ10).
- Trang thuật toán nhóm bước dưới tên mục tiêu con in đậm (**Thu lượt**, **Ước lượng lợi thế**, **Cập nhật actor**, **Cập nhật critic**, …); ví dụ tay đứng trước và dùng cùng tên (Đ12).
- Mật độ: ≤ 6 dòng nội dung, ≤ 2 công thức hiển thị (TB12), ≤ 2 khối có nhãn (TB13), một khối có số hiệu mỗi trang (TB6). Ngoại lệ ghi ở mục 7.

---

## 1. Bản đồ mạch

| Mạch | Tên (`h2`) | Dòng dẫn `p.strand-lead` (âm tiết) | Chức năng | Đầu vào | Đầu ra | Trang tiêu đề mạch | Trang | Phút |
|---|---|---|---|---|---|---|---|---|
| 1 | (mở đầu) Giới hạn của REINFORCE | không có (mạch mở đầu) | dựng ví dụ chung; cho thấy hai giới hạn; nêu câu hỏi trung tâm | REINFORCE, hàm điểm, $J$ (Bài 09); giá trị trạng thái (Bài 03) | chuỗi hai trạng thái, $J=1{,}4$, gradient $(0{,}2;\,0{,}3)$; phương sai $0{,}6925$; bước dài làm $J$ giảm; hai câu hỏi | không (bìa `L10-1-01`) | 11 | 17 |
| 2 | Đường cơ sở và hàm lợi thế | "So lợi tức với giá trị của trạng thái giữ nguyên kỳ vọng của ước lượng gradient và giảm phương sai." (22) | giảm phương sai mà giữ kỳ vọng khi biết $v_\pi$ | ba loại lượt, phương sai $0{,}6925$, câu hỏi (1) | đường cơ sở, $A_\pi$, gradient dạng lợi thế, $\delta_t$ với $v_\pi$; phương sai $0{,}69\to0{,}20\to0$; $v_\pi$ chưa biết | `L10-2-00`, `id="mach-2"` | 11 | 18 |
| 3 | Ước lượng lợi thế: độ chệch và phương sai | "Tổ hợp có trọng số các ước lượng lợi thế nhiều bước cân bằng độ chệch và phương sai." (19) | ước lượng lợi thế khi hàm giá trị phải học | $A_\pi$, $\delta_t$, gradient dạng lợi thế | critic, actor; GAE; $\lambda$ cân bằng chệch–phương sai; thuật toán actor–critic với GAE; mỗi lượt một bước nhỏ | `L10-3-00`, `id="mach-3"` | 13 | 21,5 |
| 4 | Hàm thay thế và miền tin cậy | "Chính sách mới được đánh giá từ dữ liệu của chính sách cũ với sai số nhỏ khi hai chính sách gần nhau." (23) | đánh giá chính sách mới bằng dữ liệu cũ; chặn sai số; TRPO | GAE, critic, câu hỏi (2), lượt của $\pi$ | luồng 100 lượt (phân phối hành động, phân bố trạng thái), bổ đề chênh lệch hiệu năng, hàm thay thế, tỉ số chính sách, sai số bậc hai theo độ dài bước, KL, bài toán miền tin cậy, cơ sở lý thuyết (Pinsker, bổ đề dịch chuyển, chặn cải thiện, cải thiện đơn điệu), gradient tự nhiên, TRPO; chi phí bậc hai | `L10-4-00`, `id="mach-4"` | 28 | 37,5 |
| 5 | Tối ưu chính sách gần kề (PPO) | "PPO cắt tỉ số chính sách để dùng lại một bộ đệm nhiều lần bằng gradient bậc một." (18) | thay ràng buộc KL bằng phép cắt; dùng lại bộ đệm | hàm thay thế, tỉ số chính sách, critic $(1{,}4;\,1)$, chi phí TRPO | mục tiêu cắt, PPO-Clip, so sánh TRPO–PPO, bài tập tổng hợp | `L10-5-00`, `id="mach-5"` | 14 | 17 (+3,5 bài tập) |
| 6 | Tổng kết | "Mỗi phương pháp của bài giảm phương sai hoặc giới hạn bước cập nhật dưới những giả thiết riêng." (19) | kết luận định tính kèm điều kiện | đầu ra mạch 1–5 | sơ đồ neo cuối, câu trả lời có điều kiện, bảng kết quả, bảng phương pháp | `L10-6-00`, `id="mach-6"` | 10 | 11 |
| **Tổng** | | | | | | | **87** | **122 (+3,5 bài tập)** |

Năm dòng dẫn khác mẫu câu (NT12) và chỉ dùng thuật ngữ của mạch trước hoặc tiên quyết (Đ11): "giá trị của trạng thái", "lợi tức", "kỳ vọng" (Bài 03, 09); "lợi thế" (mạch 2), "độ chệch", "phương sai" (mạch 1); "chính sách cũ/mới" (mạch 1); "tỉ số chính sách" (mạch 4), "bộ đệm" (Bài 08, mạch 4); "phương sai", "bước cập nhật" (mạch 1). Các mẫu câu (đồng bộ với deck, 2026-11-21): "So … giữ nguyên … và giảm …", "Tổ hợp … cân bằng …", "… được đánh giá từ … khi …", "PPO (…) cắt … để …", "Mỗi phương pháp … giảm … hoặc …". Tên tiếng Anh đầy đủ của PPO đứng ở mục 5 của danh sách `1-08` (lần đầu); dòng dẫn mạch 5 và `5-07` không lặp lại (G3). Không dòng nào nhắc ví dụ hay số (TB30); "lợi thế" (mạch 3) và "tỉ số chính sách" (mạch 5) được dạy ở mạch trước. Không `p.strand-keys` (thuật ngữ của mạch chưa được dạy ở điểm vào mạch, TB11).

"Nội dung" (`L10-1-08`) và `#/N`: 1. Giới hạn của REINFORCE · 2. Đường cơ sở và hàm lợi thế · 3. Ước lượng lợi thế: độ chệch và phương sai · 4. Hàm thay thế và miền tin cậy · 5. Tối ưu chính sách gần kề (Proximal Policy Optimization, PPO) · 6. Tổng kết.

## 2. Sơ đồ neo (TB2)

Bốn khối, nhãn bằng lời, không còn khối "Phần thưởng" và thẻ mạch DPO (#27):

```
┌──────────────────────────────┐
│ Thu lượt bằng chính sách cũ   │ ◀──────────────────────┐
└──────────────────────────────┘                        │ chính sách mới
              │                                          │ thành chính sách cũ
              ▼                                          │
┌ ─ ─ ─ ─ ─ ─ ┐    ┌──────────────────────────────┐     │
  (chưa có)   ─ ─▶ │ Hệ số của mỗi bước: G_t       │     │
└ ─ ─ ─ ─ ─ ─ ┘    └──────────────────────────────┘     │
                                  │                      │
                                  ▼                      │
                   ┌──────────────────────────────┐     │
                   │ Cập nhật: một bước gradient   │ ────┘
                   └──────────────────────────────┘
```

| Tệp | Dùng ở | Trạng thái |
|---|---|---|
| `so-do-neo-m1.svg` | `L10-1-08` | bản đủ; dấu "?" đỏ ở "Hệ số" ("phương sai lớn") và ở "Cập nhật" ("bước dài làm $J$ giảm"); thẻ "mạch 2" ở "Hệ số", "mạch 3" ở khối nét đứt và "Hệ số", "mạch 4, 5" ở "Cập nhật"; cột phải liệt kê mạch 2–6 đúng tên mục 1 |
| `so-do-neo-m2-vao.svg` | `L10-2-00` | "Hệ số: $G_t$" tô tím, "?"; khối khác mờ |
| `so-do-neo-m3-vao.svg` | `L10-3-00` | "Hệ số: $G_t-v_\pi(S_t)$, $\delta_t$ với $v_\pi$"; khối nét đứt tô tím, nhãn "$v_\pi$ chưa biết ?" |
| `so-do-neo-m4-vao.svg` | `L10-4-00` | khối liền "Critic $\hat v$"; "Hệ số: $\widehat A_t$ (GAE)"; "Cập nhật" tô tím, "?" |
| `so-do-neo-m5-vao.svg` | `L10-5-00` | "Cập nhật: tối đa hàm thay thế trong miền tin cậy (TRPO)" tô tím, "?"; mũi tên mờ "Thu lượt" → "Cập nhật", nhãn "dùng lại lượt vừa thu" |
| `so-do-neo-tong-ket-vao.svg` | `L10-6-00` | bản cuối thu nhỏ |
| `so-do-neo-tong-ket.svg` (+ `-buoc0`, `-buoc1`) | `L10-6-10` | bản cuối, không số (#28); tên khối trùng tên mục tiêu con của ba trang thuật toán (Đ12): **Thu lượt** (bằng chính sách cũ), **Cập nhật critic** ($\hat v$), **Ước lượng lợi thế** (hệ số của mỗi bước), **Cập nhật actor** |

Từ `so-do-neo-m4-vao.svg` (sau khi lợi thế đã dạy), khối hệ số ghi "Ước lượng lợi thế: $\widehat A_t$ (GAE)" và khối critic ghi "Cập nhật critic: $\hat v$", để trùng tên nhóm bước của `3-10`, `4-09`, `5-07` (Đ12). Trước đó giữ "Hệ số của mỗi bước" (TB11: chưa dạy "lợi thế").

---

## 3. Các trang

**Bản hiện hành (2026-11-21, sau hai lượt sửa theo năm vai).** Chữ trên mặt trang lấy theo deck `lecture-10-trpo-va-ppo.html`; các mục dưới đây giữ câu, nguồn số, hình và ghi chú nguồn. Thay đổi chữ của từng trang ghi ở §10 ("Lượt sửa theo năm vai", "Lượt sửa thứ hai"). Tiêu đề mục đã đồng bộ với `h2` của deck.

### Mạch 1. Giới hạn của REINFORCE (`id="mach-1"`, 11 trang, 17 phút)

Thứ tự: `1-01` → `1-02` → `1-09` → `1-10` → `1-11` → `1-04` → `1-12` → `1-05` → `1-06` → `1-07` → `1-08`. Mã bỏ: `1-03` (hành lang). Mã mới: `1-12` (câu hỏi nhanh, B5; đặt giữa `1-04` và `1-05` theo E1). Ba trang dựng ví dụ `1-09`–`1-11` là TB24 (#2, #4, #5, #7, #8); hai trang hiện tượng `1-04`, `1-05` đứng trước "Vấn đề trung tâm" (TB19, TB20).

#### `L10-1-01` · TRPO và PPO (bìa; giữ mã)

- **Câu:** bài. **Nhãn:** không.
- **Mặt trang:** "Học tăng cường · Bài 10"; `h1` "TRPO và PPO"; luận điểm "Dùng lại lượt đã thu cho những bước cập nhật chính sách lớn mà hàm mục tiêu không giảm." (19 âm tiết, một câu, không `<br>`, chỉ từ sinh viên có trước bài, NT11); "Trường Đại học Công nghệ, Đại học Quốc gia Hà Nội"; "Năm học 2026–2027, học kỳ 1".
- **1 phút:** Bài nói về các bước cập nhật chính sách lớn trên dữ liệu đã thu mà hàm mục tiêu không giảm.
- **Mới:** không. **Nguồn số:** không. **Hình:** không.
- **Diễn giả:** hai phần của bài: giảm phương sai của ước lượng gradient (mạch 2–3) là điều kiện để bước cập nhật dựa trên ước lượng có nghĩa; giới hạn bước cập nhật (mạch 4–5). Tên đầy đủ: tối ưu chính sách miền tin cậy (TRPO), tối ưu chính sách gần kề (PPO). Ghi chú nguồn: đoạn mở §1.
- **Phút:** 0,5.

#### `L10-1-02` · Tiên quyết và quy ước (giữ mã; sửa #1)

- **Câu:** bài. **Nhãn:** "Nhắc lại:" (hai dòng), "Ý nghĩa:", "Ký hiệu:".
- **Mặt trang:**
  - "Nhắc lại: REINFORCE thu một lượt bằng chính sách $\pi_\theta$ rồi cập nhật $\theta\leftarrow\theta+\alpha\widehat g$ với" $$\widehat g=\sum_{t=0}^{T-1}\gamma^t\,G_t\,\psi_\theta(S_t,A_t),\qquad\mathbb E[\widehat g]=\nabla_\theta J(\theta).$$
  - "Nhắc lại: hàm điểm (score function) là" $$\psi_\theta(s,a)=\nabla_\theta\log\pi_\theta(a\mid s).$$
  - "Ý nghĩa: $\psi_\theta(s,a)$ là hướng đổi $\theta$ làm log-xác suất chọn $a$ tại $s$ tăng nhanh nhất. Bước $\alpha G_t\psi_t$ tăng xác suất của $A_t$ khi $G_t>0$ và giảm khi $G_t<0$."
  - "Ký hiệu: $J(\theta)=\mathbb E[G_0]$. Số nhân với $\psi_t$ ở bước $t$ gọi là hệ số của bước đó. Ở REINFORCE, hệ số là $\gamma^tG_t$."
  - "Lưu ý: kỳ vọng $\mathbb E$ lấy theo phân phối của lượt sinh bởi $\pi_\theta$, không phải trung bình trên các lượt đã thu. Một ước lượng không chệch khi kỳ vọng của nó bằng đại lượng cần ước lượng. Phương sai là kỳ vọng của bình phương khoảng cách tới kỳ vọng." (Đ4; chuyển từ `1-04`)
  - "Giả thiết chung: MDP hữu hạn có tính Markov; mọi chính sách dùng cùng động lực $P$ và cùng phân phối đầu $\mu_0$; $|R_{t+1}|\le R_{\max}$; $0\le\gamma<1$; chính sách Markov dừng, $\pi_\theta>0$ và khả vi theo $\theta$." (Đ7; gồm các giả thiết của định lý gradient chính sách, Bài 09)
- **Dựng dần:** (0) hai dòng "Nhắc lại:"; (1) "Ý nghĩa:"; (2) "Ký hiệu:", "Lưu ý:"; (3) "Giả thiết chung:".
- **1 phút:** REINFORCE nhân hàm điểm với lợi tức; hàm điểm là hướng làm xác suất của hành động đã chọn tăng, và hệ số dương tăng xác suất đó.
- **Mới:** không (nhắc lại Bài 09). **Nguồn số:** không. **Hình:** không.
- **Ghi chú nguồn:** Kiến thức tiên quyết (Thuật toán 09.25, Hệ quả 09.26, Định nghĩa 09.15).
- **Diễn giả:** $\mathbb E[\widehat g]=\nabla J$ đúng dưới bốn giả thiết (G1)–(G4) của định lý gradient chính sách (Bài 09); giả thiết chung trên trang gồm các giả thiết đó (độ dài lượt bị chặn đúng trên chuỗi) và các giả thiết của bổ đề chênh lệch hiệu năng (mạch 4); mọi kết quả sau gọi tên nó thay vì chép lại. Hệ số là đại lượng mà mạch 2–3 thay thế. Hỏi lớp: nếu mọi lợi tức đều dương thì REINFORCE làm gì với hành động kém.
- **Phút:** 2.

#### `L10-1-09` · Ví dụ: chuỗi hai trạng thái (1) (mã mới; #2, #7a, #8)

- **Câu:** 2 (mạch 1). **Nhãn:** không ("Ví dụ:" ở tiêu đề).
- **Mặt trang:**
  - "Lượt bắt đầu ở $s_A$ và kết thúc sau một hoặc hai bước; $\gamma=0{,}9$."
  - "Tại $s_A$: hành động 1 chuyển sang $s_B$, phần thưởng $0$. Hành động 2 kết thúc lượt, phần thưởng $1$."
  - "Tại $s_B$: hành động 1 kết thúc, phần thưởng $3$. Hành động 2 kết thúc, phần thưởng $0$."
  - "Chính sách có một tham số cho mỗi trạng thái, $\theta=(\theta_A;\,\theta_B)$. Xác suất chọn hành động 1 tại $s$ là" $$p_s=\pi_\theta(1\mid s)=\sigma(\theta_s),\qquad\sigma(x)=\frac1{1+e^{-x}}.$$
  - "Chính sách hiện tại: $\theta=(0;\,\log2)$, nên $p_A=\sigma(0)=\tfrac12$, $p_B=\sigma(\log2)=\tfrac23$."
  - "Ta cập nhật $\theta$ và đọc chính sách qua $(p_A;\,p_B)$; $J$ phụ thuộc $\theta$ qua $(p_A;\,p_B)$."
- **Dựng dần:** (0) hình `-buoc0` và ba dòng môi trường; (1) dòng tham số hóa, hình đầy đủ (xác suất trên mũi tên); (2) dòng chính sách hiện tại và quy ước.
- **1 phút:** Chuỗi có hai trạng thái, hai hành động mỗi trạng thái, mỗi trạng thái một tham số; chính sách hiện tại chọn hành động 1 với xác suất $\tfrac12$ ở $s_A$, $\tfrac23$ ở $s_B$.
- **Mới:** môi trường; tham số hóa $p_s=\sigma(\theta_s)$ (hai đối tượng, TB24).
- **Nguồn số:** $\sigma(\log2)=1/(1+\tfrac12)=\tfrac23$, tính trên trang.
- **Hình:** mới `chuoi-hai-trang-thai-buoc0.svg` (môi trường sạch: ô $s_A$ ghi "xuất phát", ô $s_B$, hai ô kết thúc xám; cung ghi "1, thưởng 0", "2, thưởng 1", "1, thưởng 3", "2, thưởng 0"; không giá trị, không chữ đỏ, #7) và `chuoi-hai-trang-thai.svg` (thêm dưới nhãn mỗi cung xác suất chọn: "$p_A$", "$1-p_A$", "$p_B$", "$1-p_B$"). Nửa trái, khoảng 45% thân trang, nhãn ≥ 20 px ở 1600×900.
- **Ghi chú nguồn:** Ví dụ 10.6, đoạn "Dữ kiện".
- **Diễn giả:** đây là chính sách softmax của Bài 09 với logit $\theta_s$ cho hành động 1 và $0$ cho hành động 2; với hai hành động, softmax là hàm logistic của hiệu hai logit (Bài tập 10.22). Mọi ví dụ của bài dùng chuỗi này và cách tham số hóa này. Ghi chú còn hành lang ngắn (Ví dụ 10.2) và bài toán một bước làm ví dụ bổ sung.
- **Phút:** 2.

#### `L10-1-10` · Ví dụ: chuỗi hai trạng thái (2) (mã mới; #4, #7b)

- **Câu:** 2. **Nhãn:** "Diễn giải:".
- **Mặt trang:**
  - "Tính $J=\mathbb E[G_0]$ từ ba loại lượt, với $G_0=R_1+\gamma R_2$:"

    | Loại lượt | Xác suất | $G_0$ |
    |---|---|---|
    | $s_A\xrightarrow1s_B\xrightarrow1$ | $p_Ap_B=\tfrac12\cdot\tfrac23=\tfrac13$ | $0+0{,}9\cdot3=2{,}7$ |
    | $s_A\xrightarrow1s_B\xrightarrow2$ | $p_A(1-p_B)=\tfrac12\cdot\tfrac13=\tfrac16$ | $0+0{,}9\cdot0=0$ |
    | $s_A\xrightarrow2$ | $1-p_A=\tfrac12$ | $1$ |
  - $$J=2{,}7\,p_Ap_B+1-p_A=2{,}7\cdot\tfrac13+\tfrac12=1{,}4.$$
  - "Diễn giải: $J$ là giá trị của trạng thái xuất phát, $v_\pi(s_A)=1{,}4$. Từ $s_B$, $v_\pi(s_B)=\tfrac23\cdot3+\tfrac13\cdot0=2$."
- **Dựng dần:** (0) bảng, cột xác suất; (1) cột $G_0$; (2) công thức $J$; (3) "Diễn giải:".
- **1 phút:** Ba loại lượt phủ mọi khả năng; cộng xác suất nhân lợi tức được $J=2{,}7p_Ap_B+1-p_A=1{,}4$.
- **Mới:** $J$ của chuỗi; $v_\pi$ trên chuỗi (nhắc lại khái niệm Bài 03).
- **Nguồn số:** mọi ô tính trong ô; $J$ từ bảng.
- **Hình:** `chuoi-hai-trang-thai.svg` thu nhỏ, góc trái trên (cùng hình trang trước; không lặp bảng).
- **Ghi chú nguồn:** Ví dụ 10.6, "Giá trị" và "Gradient tính trực tiếp".
- **Diễn giả:** $J$ viết theo $(p_A;\,p_B)$ vì chuỗi có ba loại lượt; không cần giải hệ Bellman. $v_\pi(s_B)=2$ và $q_\pi(s_A,1)=0{,}9\cdot2=1{,}8$ dùng ở trang sau và ở mạch 2.
- **Phút:** 1,5.

#### `L10-1-11` · Ví dụ: chuỗi hai trạng thái (3) (mã mới; #1, #7b)

- **Câu:** 2. **Nhãn:** "Diễn giải:".
- **Mặt trang:**
  - "Với $\mathrm dp_s/\mathrm d\theta_s=p_s(1-p_s)$, gradient tại $\theta=(0;\,\log2)$:" $$\frac{\partial J}{\partial\theta_A}=(2{,}7p_B-1)\,p_A(1-p_A)=0{,}8\cdot\tfrac14=0{,}2,\qquad\frac{\partial J}{\partial\theta_B}=2{,}7p_A\cdot p_B(1-p_B)=1{,}35\cdot\tfrac29=0{,}3.$$
  - "Hàm điểm: $\log\sigma(\theta_s)$ có đạo hàm $1-p_s$, $\log(1-\sigma(\theta_s))$ có đạo hàm $-p_s$, nên" $$\psi(s,1)=(1-p_s)\,e_s,\qquad\psi(s,2)=-p_s\,e_s,$$ "với $e_A=(1;\,0)$, $e_B=(0;\,1)$. Tại $s_A$: $\psi_A=+0{,}5$ khi chọn 1, $-0{,}5$ khi chọn 2."
  - "Diễn giải: $\partial J/\partial\theta_A=0{,}2>0$, nên tăng $p_A$ làm $J$ tăng: tại $s_A$, hành động 1 cho lợi tức kỳ vọng $q_\pi(s_A,1)=0{,}9\cdot2=1{,}8$, hành động 2 cho $1$."
- **Dựng dần:** (0) gradient; (1) hàm điểm; (2) "Diễn giải:".
- **1 phút:** Gradient bằng $(0{,}2;\,0{,}3)$, nên cần tăng cả $p_A$ lẫn $p_B$; chọn hành động 1 đẩy $\theta_s$ lên một lượng $1-p_s$, chọn hành động 2 đẩy xuống một lượng $p_s$.
- **Mới:** gradient của chuỗi; dạng hàm điểm trên chuỗi.
- **Nguồn số:** $p_A$, $p_B$ từ `1-09`; $J$ từ `1-10`; $2{,}7\cdot\tfrac23-1=0{,}8$; $\tfrac12\cdot2{,}7=1{,}35$; $\tfrac23\cdot\tfrac13=\tfrac29$; $v_\pi(s_B)=2$ từ `1-10`.
- **Hình:** không (hai công thức; hình không thêm ý).
- **Ghi chú nguồn:** Ví dụ 10.6, "Gradient tính trực tiếp"; Mệnh đề 09.16.
- **Diễn giả:** hai tọa độ của $\psi$ tách theo trạng thái, nên tọa độ $\theta_A$ chỉ nhận đóng góp của bước tại $s_A$. Kỳ vọng của $\psi$ tại mỗi trạng thái bằng $0$: $p(1-p)+(1-p)(-p)=0$; mạch 2 dùng tính chất này. Độ lớn $1-p_s$: hành động đã gần chắc chắn được chọn thì bị đẩy ít.
- **Phút:** 2.

#### `L10-1-04` · Ước lượng REINFORCE không chệch nhưng có phương sai lớn (giữ mã, chức năng "vấn đề 1"; #3, #7c, #12)

- **Câu:** 3 (mạch 1). **Nhãn:** "Nhắc lại:"; hộp ý chính.
- **Mặt trang:**
  - "Nhắc lại: $\theta=(0;\,\log2)$, $(p_A;\,p_B)=(\tfrac12;\,\tfrac23)$, $J=1{,}4$, $\partial J/\partial\theta_A=0{,}2$. Tại $s_A$, $\psi_A=+0{,}5$ khi chọn 1 và $-0{,}5$ khi chọn 2." (Đ1)
  - "Tọa độ $\theta_A$ của $\widehat g$ chỉ có số hạng $t=0$: $\widehat g_A=G_0\,\psi_A$."

    | Loại lượt | Xác suất | $G_0$ | $\psi_A$ | $\widehat g_A=G_0\psi_A$ | $p_A$ |
    |---|---|---|---|---|---|
    | $s_A\xrightarrow1s_B\xrightarrow1$ | $p_Ap_B=\tfrac13$ | $2{,}7$ | $+0{,}5$ | $2{,}7\cdot0{,}5=1{,}35$ | tăng |
    | $s_A\xrightarrow1s_B\xrightarrow2$ | $p_A(1-p_B)=\tfrac16$ | $0$ | $+0{,}5$ | $0$ | không đổi |
    | $s_A\xrightarrow2$ | $1-p_A=\tfrac12$ | $1$ | $-0{,}5$ | **$-0{,}5$** (đỏ) | giảm |
    | kỳ vọng | | | | $\tfrac13\cdot1{,}35+\tfrac16\cdot0+\tfrac12\cdot(-0{,}5)=0{,}2$ | |
    | phương sai | | | | $\tfrac13\cdot1{,}35^2+\tfrac12\cdot0{,}5^2-0{,}2^2=0{,}6925$ | |
  - Hộp: "Kỳ vọng bằng $\partial J/\partial\theta_A=0{,}2$, nhưng với xác suất $\tfrac12$ một lượt cho ước lượng ngược dấu gradient."
- **Dựng dần:** (0) nhắc lại, dòng mở, bảng đến cột $\psi_A$, trục số trống; (1)–(3) mỗi mảnh một hàng: ô $\widehat g_A$, ô "$p_A$" và chấm tương ứng trên trục số hiện cùng lúc (#3); (4) hai hàng kỳ vọng, phương sai và vạch kỳ vọng trên trục; (5) hộp. Hàng 2–3 chỉ ghi kết quả của tích (Đ10).
- **Bố cục:** bảng bên trái (khoảng 70% bề rộng), trục số đặt đứng bên phải (khoảng 25%), giá trị tăng từ dưới lên; hộp dưới cùng, rộng hết trang.
- **1 phút:** Ba loại lượt cho ba ước lượng $1{,}35$; $0$; $-0{,}5$. Kỳ vọng đúng bằng gradient $0{,}2$, nhưng một nửa số lượt kéo $p_A$ ngược chiều.
- **Mới:** bảng ước lượng theo loại lượt (một đối tượng). Dòng phân biệt "không chệch", "phương sai" (Đ4) đặt ở "Lưu ý:" của `1-02`.
- **Nguồn số:** xác suất (dạng tích), $G_0$ từ `1-10`; $\psi_A$ từ `1-11`; $0{,}2$ từ `1-11`; phép tính trong ô.
- **Hình:** mới `reinforce-truc-so.svg` (+ `-buoc0` … `-buoc3`), **trục đứng**: trục từ $-1$ (dưới) tới $1{,}5$ (trên); vạch $0$; chấm tại $1{,}35$ (nhãn "$\tfrac13$"), $0$ ("$\tfrac16$"), $-0{,}5$ ("$\tfrac12$", đỏ); diện tích chấm tỉ lệ xác suất; bản đủ thêm vạch ngang xanh nét liền tại $0{,}2$, nhãn "kỳ vọng $=0{,}2$", và vùng dưới $0$ tô nhạt, nhãn "ngược dấu gradient". Bên phải bảng, rộng khoảng 25%.
- **Ghi chú nguồn:** Ví dụ 10.6, bảng "Ba loại lượt" và đoạn sau bảng.
- **Diễn giả:** "không chệch" (Bài 09) là khẳng định về kỳ vọng trên nhiều lượt; trên một lượt, ước lượng là một trong ba số. Tọa độ $\theta_B$ (ghi chú): $0{,}9$; $0$; $0$, kỳ vọng $0{,}3$, phương sai $0{,}18$. Lượt thứ ba kéo $p_A$ xuống vì $G_0=1>0$; mạch 2 xử lý chính hiện tượng này.
- **Phút:** 3.

#### `L10-1-12` · Câu hỏi nhanh: bước dài theo lượt $s_A\xrightarrow1s_B\xrightarrow1$ (mã mới; B5, E1; TB22)

- **Câu:** 4 (mạch 1), phần đối chiếu. **Nhãn:** "Nhắc lại:", "Câu hỏi:", "Lời giải:" (hộp, mảnh 1).
- **Mặt trang:** Nhắc lại $\theta=(0;\,\log2)$, $p_s=\sigma(\theta_s)$, $J=2{,}7p_Ap_B+1-p_A=1{,}4$, bước $\theta\leftarrow\theta+\alpha\widehat g$ (hai câu). Câu hỏi (G2): lượt $s_A\xrightarrow1s_B\xrightarrow1$ cho $\widehat g=(G_0\psi_A;\,\gamma G_1\psi_B)=(2{,}7\cdot0{,}5;\,0{,}9\cdot3\cdot\tfrac13)=(1{,}35;\,0{,}9)$; với $\alpha=1$, $J$ tăng hay giảm? Lời giải: tăng; cả hai tọa độ dương nên $p_A$, $p_B$ cùng tăng, $J$ tăng theo $p_B$ và tăng theo $p_A$ khi $2{,}7p_B>1$ (đúng với $p_B\ge\tfrac23$); kiểm bằng số $p=(0{,}794;\,0{,}831)$, $J=1{,}988\gt1{,}4$.
- **1 phút:** Cùng độ dài bước, lượt này kéo $J$ lên, lượt $s_A\xrightarrow2$ ở trang sau kéo $J$ xuống.
- **Nguồn số:** Ví dụ 10.6; $\sigma(1{,}35)=0{,}794$, $\sigma(\log2+0{,}9)=0{,}831$.
- **Ghi chú nguồn:** §2.4 (Ví dụ 10.6). **Diễn giả:** cách tính hai tọa độ của $\widehat g$; dự đoán dấu trước khi tính. **Phút:** 1.

#### `L10-1-05` · Bước dài theo lượt $s_A\xrightarrow2$ làm $J$ giảm (giữ mã, chức năng "vấn đề 2"; #8, #9; tiêu đề theo G1)

- **Câu:** 4 (mạch 1). **Nhãn:** không; hộp ý chính.
- **Mặt trang:**
  - "Lượt $s_A\xrightarrow2$ (xác suất $\tfrac12$) cho $\widehat g=(-0{,}5;\,0)$. Bước $\theta\leftarrow\theta+\alpha\widehat g$ chỉ đổi $\theta_A=-0{,}5\alpha$. Với $p_B=\tfrac23$, $J=1+0{,}8\,p_A$."

    | $\alpha$ | $\theta_A$ | $p_A=\sigma(\theta_A)$ | $J=1+0{,}8p_A$ |
    |---|---|---|---|
    | $0$ | $0$ | $0{,}5$ | $1{,}4$ |
    | $1$ | $-0{,}5$ | $0{,}378$ | $1{,}30$ |
    | $2$ | $-1$ | $0{,}269$ | $1{,}22$ |
    | $\to\infty$ | $\to-\infty$ | $\to0$ | $\to1$ |
  - Hộp (hiện hành, G1): "Cùng $\alpha$, chiều đổi của $J$ phụ thuộc lượt đã thu. Với lượt $s_A\xrightarrow2$, $J$ giảm $0{,}4$ khi $\alpha\to\infty$. Sau một bước, lượt đã thu là lượt của chính sách cũ và $\widehat g$ tính từ nó mất tính không chệch, nên REINFORCE dùng mỗi lượt cho đúng một bước." Dòng gradient đúng nằm ở ghi chú diễn giả (B1).
  - "Trên chuỗi, mỗi trạng thái có tham số riêng, và bước theo gradient đúng $(0{,}2;\,0{,}3)$ không làm $J$ giảm: $\alpha=1$ cho $p=(0{,}550;\,0{,}730)$, $J=2{,}7p_Ap_B+1-p_A=1{,}53$, còn $\alpha=2$ cho $p=(0{,}599;\,0{,}785)$, $J=1{,}67$. $J$ trong bảng giảm vì bước dựa vào ước lượng của một lượt." (Đ2: tính chất chỉ đúng trên chuỗi; TB29)
- **Dựng dần:** (0) dòng mở và hàng $\alpha=0$; (1) hàng $\alpha=1$ cùng điểm trên đồ thị; (2) hàng $\alpha=2$; (3) hàng giới hạn và đường tiệm cận; (4) hộp; (5) dòng đối chiếu với gradient đúng.
- **1 phút:** Một lượt xấu cùng bước học lớn đưa $p_A$ về gần $0$ và $J$ từ $1{,}4$ về gần $1$.
- **Mới:** bước theo ước lượng một lượt (một đối tượng).
- **Nguồn số:** $\widehat g_A=-0{,}5$ từ `1-04`; $\widehat g_B=\gamma G_1\psi_B=0$ vì lượt không tới $s_B$ (ghi trên trang bằng "$(-0{,}5;\,0)$", lý do trong ghi chú diễn giả); $J=2{,}7\cdot\tfrac23p_A+1-p_A=1+0{,}8p_A$ (thay $p_B=\tfrac23$ vào `1-10`); $\sigma(-0{,}5)=0{,}3775$, $\sigma(-1)=0{,}2689$; $1+0{,}8\cdot0{,}3775=1{,}302$, $1+0{,}8\cdot0{,}2689=1{,}215$.
- **Hình:** mới `buoc-dai-mot-luot.svg`: đồ thị $J$ theo $\alpha\in[0,8]$, đường xanh nét liền $J=1+0{,}8\,\sigma(-0{,}5\alpha)$; điểm tại $\alpha=1$ ($1{,}30$), $\alpha=2$ ($1{,}22$); đường ngang nét đứt $J=1$ "giới hạn"; đường ngang mảnh $1{,}4$ "chính sách hiện tại". Nửa phải.
- **Ghi chú nguồn:** Ví dụ 10.6, đoạn "Bước dài theo ước lượng của một lượt"; §1.1, đoạn "Giới hạn thứ hai".
- **Diễn giả:** $p$ ở dòng gradient đúng: $(\sigma(0{,}2\alpha);\,\sigma(\log2+0{,}3\alpha))$. Bước dài chỉ nguy hiểm khi nó dựa vào một ước lượng nhiễu hoặc vào dữ liệu của chính sách cũ. REINFORCE dùng mỗi lượt cho đúng một bước, vì sau bước đó lượt đã thuộc chính sách cũ. Trên hành lang của ghi chú, bước theo gradient đúng mà dài cũng làm $J$ giảm (vượt đỉnh); chuỗi không có hiện tượng đó vì mỗi trạng thái có tham số riêng.
- **Phút:** 2,5.

#### `L10-1-06` · Vấn đề trung tâm (giữ mã)

- **Câu:** bài. **Nhãn:** "Câu hỏi:".
- **Mặt trang:** hai hình thu nhỏ cạnh nhau, chú thích "phương sai lớn", "bước dài theo lượt $s_A\to2$ làm $J$ giảm" (G1); hộp "Câu hỏi:" với danh sách: 1. "Làm thế nào để ước lượng gradient chính sách có phương sai nhỏ mà kỳ vọng không đổi?" 2. "Làm thế nào để dùng lượt của chính sách cũ cho bước cập nhật dài mà hàm mục tiêu không giảm?"
- **1 phút:** Câu 1 đến từ bảng ba ước lượng REINFORCE, câu 2 từ hai bước dài trên chuỗi (`1-12`, `1-05`).
- **Mới:** không. **Nguồn số:** không số trên trang.
- **Hình:** mới `reinforce-truc-so-nho.svg`, `buoc-dai-mot-luot-nho.svg` (bản thu nhỏ, nhãn lớn hơn, bỏ số phụ).
- **Ghi chú nguồn:** §1.1, đoạn "bài toán trung tâm".
- **Diễn giả:** câu trả lời theo mạch: mạch 2 (đường cơ sở, lợi thế) và mạch 3 (critic, GAE) cho câu 1; mạch 4 (hàm thay thế, miền tin cậy, TRPO) và mạch 5 (PPO) cho câu 2 (NT11: câu trả lời từng mạch chỉ ở ghi chú diễn giả).
- **Phút:** 1.

#### `L10-1-07` · Mục tiêu học tập (giữ mã)

- **Mặt trang:** "Sau bài này, sinh viên có thể:" 1. "Giảm phương sai của ước lượng gradient chính sách mà giữ nguyên kỳ vọng." 2. "Ước lượng mức tốt hơn của một hành động khi hàm giá trị phải học từ dữ liệu, và tính độ chệch, phương sai của ước lượng." 3. "Đánh giá chính sách mới từ lượt của chính sách cũ và chặn sai số của phép đánh giá." 4. "Thực hiện nhiều bước cập nhật trên cùng một bộ đệm mà chính sách mới không rời xa chính sách cũ." (bốn dòng, mỗi mạch nội dung một dòng, không thuật ngữ chưa dạy, TB19; khoảng 70 âm tiết ≤ 80).
- **1 phút:** Bốn việc làm được sau bài, mỗi việc một mạch.
- **Ghi chú nguồn:** Mục tiêu học tập 1–7 của ghi chú (bản sau khi bỏ DPO). **Diễn giả:** đối chiếu với danh sách đầy đủ của ghi chú. **Phút:** 0,5.

#### `L10-1-08` · Nội dung (giữ mã)

- **Mặt trang:** sơ đồ neo đầy đủ `so-do-neo-m1.svg` (mục 2); cột phải của hình là danh sách đánh số 1–6 đúng tên mục 1 (không lặp danh sách bằng chữ HTML).
- **1 phút:** Vòng cập nhật có ba khối và một chỗ trống; mạch 2–3 sửa khối hệ số và lấp chỗ trống, mạch 4–5 sửa khối cập nhật.
- **Mới:** sơ đồ neo. **Hình:** `so-do-neo-m1.svg` (sửa, mục 6).
- **Diễn giả:** đọc vòng: thu lượt bằng chính sách cũ, tính hệ số mỗi bước, cập nhật, chính sách mới thành chính sách cũ. Hai dấu "?" là hai câu hỏi trung tâm. **Phút:** 1.

---

### Mạch 2. Đường cơ sở và hàm lợi thế (`id="mach-2"`, 11 trang, 18 phút)

Thứ tự: `2-00` → `2-01` → `2-04` → `2-02` → `2-03` → `2-06` → `2-09` → `2-10` → `2-07` → `2-08` → `2-11`. Mã bỏ: `2-05` (ý tưởng chứng minh đường cơ sở, gộp thành dòng "Chứng minh." của `2-04`). Hành trình: bài toán và trực quan `2-01` → định nghĩa `2-01` (mảnh cuối) → kết quả `2-04` → ví dụ `2-02` → kiểm giả thiết `2-03` → định nghĩa $A_\pi$ `2-06` → hệ quả `2-09`, `2-10` → câu hỏi dẫn và mệnh đề $\delta_t$ `2-07` → ví dụ `2-08` → trạm dừng `2-11`. Không có "critic", "actor" trong mạch (#15).

#### `L10-2-00` · Đường cơ sở và hàm lợi thế (trang tiêu đề mạch; điểm vào mạch 2; giữ mã)

- **Mặt trang:** `span.strand-number` "2."; `h2` "Đường cơ sở và hàm lợi thế"; `p.strand-lead` "Hiệu giữa lợi tức và giá trị của trạng thái cho biết hành động tốt hơn hay kém hơn mức kỳ vọng." Không `p.strand-keys`.
- **Hình:** `so-do-neo-m2-vao.svg`. **1 phút:** mạch này sửa khối hệ số.
- **Diễn giả (40–100 âm tiết):** "Mạch trước cho thấy ước lượng REINFORCE không chệch nhưng có phương sai lớn, vì lợi tức dương tăng xác suất của mọi hành động đã chọn. Mạch này so lợi tức với giá trị của trạng thái, giữ nguyên kỳ vọng và giảm phương sai. Đầu ra là gradient dạng lợi thế và sai số TD với $v_\pi$ đúng; điều còn lại là $v_\pi$ chưa biết." **Phút:** 0,5.

#### `L10-2-01` · REINFORCE tăng xác suất của hành động kém khi lợi tức dương (giữ mã, chức năng mở mạch; #10, #7d)

- **Câu:** 1–2 (mạch 2). **Nhãn:** "Câu hỏi:", "Định nghĩa." (mảnh cuối).
- **Mặt trang:**
  - "Trên chuỗi mọi lợi tức không âm. Lượt $s_A\xrightarrow2$ có $G_0=1>0$ nên tăng xác suất hành động 2, dù $q_\pi(s_A,2)=1<q_\pi(s_A,1)=1{,}8$."
  - Hộp "Câu hỏi: so lợi tức với mức nào thì biết hành động đã chọn tốt hay kém?"
  - "Lợi tức từ $s_A$ có kỳ vọng $v_\pi(s_A)=\tfrac13\cdot2{,}7+\tfrac16\cdot0+\tfrac12\cdot1=1{,}4$. Hiệu $G_0-1{,}4$ dương khi lượt tốt hơn mức kỳ vọng, âm khi kém hơn."
  - "**Định nghĩa.** Đường cơ sở (baseline) là một hàm bị chặn $b:\mathcal S\to\mathbb R$. Ước lượng có đường cơ sở là" $$\widehat g_b=\sum_{t=0}^{T-1}\gamma^t\bigl(G_t-b(S_t)\bigr)\,\psi_t .$$
- **Dựng dần:** (0) dòng bài toán, hộp câu hỏi; (1) trục số và dòng $v_\pi(s_A)$; (2) nhãn "kém hơn mức kỳ vọng" / "tốt hơn mức kỳ vọng" trên trục; (3) định nghĩa.
- **1 phút:** Lượt chọn hành động 2 nhận $1$, ít hơn mức kỳ vọng $1{,}4$ ở $s_A$, nên lẽ ra phải giảm xác suất của hành động 2; trừ $1{,}4$ khỏi lợi tức cho đúng dấu đó.
- **Mới:** so với $v_\pi(s_A)$ (trực quan); đường cơ sở (định nghĩa).
- **Nguồn số:** $G_0$, xác suất từ `1-10`; $q_\pi(s_A,1)=1{,}8$ từ `1-11`; $1{,}4$ tính trên trang, trùng $J$ của `1-10`.
- **Hình:** mới `truc-so-loi-tuc.svg` (+ `-buoc0`): trục ngang $0$ đến $3$; ba chấm $0$ ("$\tfrac16$", đường đi $s_A\xrightarrow1s_B\xrightarrow2$), $1$ ("$\tfrac12$", $s_A\xrightarrow2$), $2{,}7$ ("$\tfrac13$", $s_A\xrightarrow1s_B\xrightarrow1$); vạch tím đứng tại $1{,}4$, nhãn "$v_\pi(s_A)=1{,}4$"; bản đủ thêm mũi tên có dấu từ vạch tới mỗi chấm, nhãn "$-1{,}4$", "$-0{,}4$", "$+1{,}3$", và hai nhãn vùng "kém hơn mức kỳ vọng" (trái), "tốt hơn mức kỳ vọng" (phải). Nửa phải, khoảng 40%.
- **Ghi chú nguồn:** §2.1 đoạn mở; Định nghĩa 10.1 (bỏ phần đường cơ sở ngẫu nhiên).
- **Diễn giả:** tên "đường cơ sở" đặt sau khi đã thấy vạch $1{,}4$. Đường cơ sở chỉ được phụ thuộc trạng thái; trang sau cho biết vì sao. Đường cơ sở ngẫu nhiên (ghi chú) không cần cho bài.
- **Phút:** 2,5.

#### `L10-2-04` · Đường cơ sở chỉ phụ thuộc trạng thái không làm chệch ước lượng gradient (giữ mã; #11, TB28)

- **Câu:** 3. **Nhãn:** "Mệnh đề.", "Giả thiết:", "Kết luận:", "Chứng minh.", "Ý nghĩa:".
- **Mặt trang:**
  - "**Mệnh đề** (đường cơ sở). Giả thiết: giả thiết chung. Thêm: lượt sinh bởi $\pi_\theta$, $b$ bị chặn và chỉ phụ thuộc trạng thái. Kết luận:" $$\mathbb E\Bigl[\sum_t\gamma^t\,b(S_t)\,\psi_t\Bigr]=0,\qquad\text{do đó}\quad\mathbb E[\widehat g_b]=\nabla_\theta J(\theta).$$
  - "Chứng minh. Khi biết lịch sử $H_t$, $b(S_t)$ là hằng, nên $\mathbb E[b(S_t)\psi_t\mid H_t]=b(S_t)\,\nabla_\theta\sum_a\pi_\theta(a\mid S_t)=0$."
  - "Ý nghĩa: trên $s_A$, $\tfrac12\cdot0{,}5+\tfrac12\cdot(-0{,}5)=0$, nên trừ $1{,}4\,\psi_A$ không đổi kỳ vọng $0{,}2$."
- **Dựng dần:** (0) mệnh đề; (1) chứng minh; (2) ý nghĩa.
- **1 phút:** Trừ một hàm của trạng thái khỏi lợi tức không đổi kỳ vọng của ước lượng, vì hàm điểm có kỳ vọng $0$ tại mỗi trạng thái.
- **Mới:** mệnh đề đường cơ sở.
- **Nguồn số:** $\psi_A=\pm0{,}5$ từ `1-11`; $0{,}2$ từ `1-04`.
- **Hình:** không. **Ghi chú nguồn:** Mệnh đề 10.2; dòng "Chứng minh." là Bước 2 (kỳ vọng có điều kiện của một số hạng) của chứng minh trong ghi chú; Mệnh đề 09.17.
- **Diễn giả:** Bước 1 của ghi chú tách $\widehat g_b=\widehat g-\sum_t\gamma^tb(S_t)\psi_t$; Bước 3 lấy kỳ vọng và cộng theo $t$. "Không phụ thuộc hành động" nghĩa là không phụ thuộc $A_t$ khi đã biết $H_t$, không phải độc lập với $A_t$. Bỏ giả thiết: $b(S_0,A_0)=r(A_0)$ cho ước lượng $\equiv0$ (ghi chú). Bảo đảm thuộc về kỳ vọng; phương sai có thể tăng với đường cơ sở xấu (Ví dụ 10.3).
- **Phút:** 1,5.

#### `L10-2-02` · Trên chuỗi, đường cơ sở $v_\pi$ giữ nguyên kỳ vọng và giảm phương sai (giữ mã; #10, #12)

- **Câu:** 4 (mạch 2). **Nhãn:** không; hộp ý chính.
- **Mặt trang:**
  - "Ở đây $b=v_\pi$, $b(s_A)=1{,}4$, chỉ có bước $t=0$, $\psi_0=\psi_A$. Tọa độ $\theta_A$ của $\widehat g_b$ là $(G_0-1{,}4)\,\psi_A$." (Đ6)

    | Loại lượt | Xác suất | $G_0-1{,}4$ | $\psi_A$ | $(G_0-1{,}4)\psi_A$ | $p_A$ |
    |---|---|---|---|---|---|
    | $s_A\xrightarrow1s_B\xrightarrow1$ | $p_Ap_B=\tfrac13$ | $2{,}7-1{,}4=1{,}3$ | $+0{,}5$ | $1{,}3\cdot0{,}5=0{,}65$ | tăng |
    | $s_A\xrightarrow1s_B\xrightarrow2$ | $p_A(1-p_B)=\tfrac16$ | $-1{,}4$ | $+0{,}5$ | **$-0{,}7$** (đỏ) | giảm |
    | $s_A\xrightarrow2$ | $1-p_A=\tfrac12$ | $-0{,}4$ | $-0{,}5$ | $0{,}2$ | tăng |
    | kỳ vọng | | | | $\tfrac13\cdot0{,}65-\tfrac16\cdot0{,}7+\tfrac12\cdot0{,}2=0{,}2$ | |
    | phương sai | | | | $\tfrac13\cdot0{,}65^2+\tfrac16\cdot0{,}7^2+\tfrac12\cdot0{,}2^2-0{,}2^2=0{,}2025$ | |
  - Hộp: "Kỳ vọng giữ $0{,}2$, phương sai giảm từ $0{,}6925$ xuống $0{,}2025$. Lượt chọn hành động 2 nay giảm xác suất của nó. Lượt $s_A\xrightarrow1s_B\xrightarrow2$ bị phạt vì phần thưởng $0$ ở $s_B$."
  - "Phương sai giảm trên chuỗi này. Mệnh đề chỉ bảo đảm kỳ vọng, và một đường cơ sở khác có thể làm phương sai tăng." (Đ2)
- **Dựng dần:** (0) dòng mở, bảng đến cột $\psi_A$; (1) cột tích và cột $p_A$; (2) hai hàng cuối; (3) hộp.
- **1 phút:** Trừ $1{,}4$ làm lượt chọn hành động kém nhận hệ số âm; kỳ vọng giữ $0{,}2$, phương sai giảm hơn ba lần, nhưng một lượt có xác suất $\tfrac16$ vẫn đẩy sai chiều.
- **Mới:** bảng với đường cơ sở (một đối tượng; cùng khuôn bảng `1-04`, NT-RL-5).
- **Nguồn số:** $G_0$ từ `1-10`; $1{,}4$ từ `2-01`; $\psi_A$ từ `1-11`; $0{,}6925$ từ `1-04` (nhắc kèm tên "phương sai của REINFORCE"); phép tính trong ô.
- **Hình:** không (bảng là bằng chứng; trục số của `2-01` thu nhỏ ở góc nếu còn chỗ, không bắt buộc).
- **Ghi chú nguồn:** Ví dụ 10.6, cột "trừ $v_\pi$" và đoạn sau bảng.
- **Diễn giả:** xác suất một lượt cho tọa độ âm: $\tfrac12$ (REINFORCE) → $\tfrac16$. Hệ số mới nằm quanh $0$, lớn nhất $1{,}4$ về độ lớn, thay cho $2{,}7$. Phương sai giảm ở ví dụ này; mệnh đề chỉ bảo đảm kỳ vọng.
- **Phút:** 2.

#### `L10-2-03` · Câu hỏi nhanh: đường cơ sở phụ thuộc hành động (giữ mã; TB22)

- **Câu:** 3 (kiểm giả thiết). **Nhãn:** "Nhắc lại:", "Câu hỏi:", "Lời giải:".
- **Mặt trang:**
  - "Nhắc lại: $q_\pi(s_A,1)=1{,}8$, $q_\pi(s_A,2)=1$; $\psi_A=\pm0{,}5$."

    | Loại lượt | Xác suất | $G_0$ | $(G_0-1{,}4)\psi_A$ | $(G_0-q_\pi(s_A,A_0))\psi_A$ |
    |---|---|---|---|---|
    | $s_A\xrightarrow1s_B\xrightarrow1$ | $p_Ap_B=\tfrac13$ | $2{,}7$ | $0{,}65$ | **?** → $(2{,}7-1{,}8)\cdot0{,}5=0{,}45$ |
    | $s_A\xrightarrow1s_B\xrightarrow2$ | $p_A(1-p_B)=\tfrac16$ | $0$ | $-0{,}7$ | **?** → $(0-1{,}8)\cdot0{,}5=-0{,}9$ |
    | $s_A\xrightarrow2$ | $1-p_A=\tfrac12$ | $1$ | $0{,}2$ | **?** → $(1-1)(-0{,}5)=0$ |
    | kỳ vọng | | | $0{,}2$ | **?** → $\tfrac13\cdot0{,}45-\tfrac16\cdot0{,}9+0=0$ |
  - "Câu hỏi: trừ $q_\pi(S_t,A_t)$ thay cho $v_\pi(S_t)$ có giữ kỳ vọng $0{,}2$ không?"
  - "Lời giải: không. Kỳ vọng thành $0$. $q_\pi(S_t,A_t)$ phụ thuộc hành động đã chọn, trái giả thiết của mệnh đề đường cơ sở."
- **Dựng dần:** (0) bảng với các dấu "?" đỏ và câu hỏi; (1) điền cột cuối và lời giải.
- **1 phút:** Đường cơ sở phụ thuộc hành động làm chệch ước lượng: kỳ vọng $0$ thay cho $0{,}2$.
- **Mới:** không. **Nguồn số:** $q_\pi$ từ `1-11`; cột thứ tư từ `2-02`.
- **Hình:** không. **Ghi chú nguồn:** đoạn sau Mệnh đề 10.2 ("Bỏ đường cơ sở không phụ thuộc hành động").
- **Diễn giả:** năng lực kiểm tra: nhận ra giả thiết quyết định của mệnh đề (NT-RL-10). "Gợi ý: tính cột cuối cho từng hàng như hai cột trước." Hệ số $G_0-q_\pi(S_0,A_0)$ chỉ còn phần ngẫu nhiên sau bước đầu, kỳ vọng $0$ khi biết $(S_0,A_0)$.
- **Phút:** 2.

#### `L10-2-06` · Hàm lợi thế (giữ mã; #13)

- **Câu:** 3. **Nhãn:** "Định nghĩa.", "Ý nghĩa:".
- **Mặt trang:**
  - "Khi biết $(S_t,A_t)=(s,a)$, lợi tức $G_t$ có kỳ vọng $q_\pi(s,a)$, nên hệ số $G_t-v_\pi(S_t)$ có kỳ vọng có điều kiện $q_\pi(s,a)-v_\pi(s)$."
  - "**Định nghĩa.** Cho chính sách Markov dừng $\pi$ với giá trị trạng thái $v_\pi$ và giá trị hành động $q_\pi$. Hàm lợi thế (advantage function) của $\pi$ là" $$A_\pi(s,a)=q_\pi(s,a)-v_\pi(s).$$
  - "Ý nghĩa: $A_\pi(s,a)>0$ khi thực hiện $a$ tại $s$ rồi theo $\pi$ cho lợi tức kỳ vọng lớn hơn $v_\pi(s)$. Lợi thế là đại lượng của chính sách, xác định bởi kỳ vọng. Hiệu $G_t-v_\pi(S_t)$ trên một lượt là một ước lượng của nó." (Đ4, gộp vào "Ý nghĩa:" để trang có hai khối có nhãn)
  - "Trên chuỗi: $A_\pi(s_A,\cdot)=(1{,}8-1{,}4;\,1-1{,}4)=(0{,}4;\,-0{,}4)$, $A_\pi(s_B,\cdot)=(3-2;\,0-2)=(1;\,-2)$."
- **Dựng dần:** (0) dòng lý do; (1) định nghĩa, ý nghĩa; (2) dòng số và hình.
- **1 phút:** Lợi thế của hành động là giá trị hành động trừ giá trị trạng thái; tại $s_A$ hành động 1 có lợi thế $+0{,}4$, hành động 2 có $-0{,}4$.
- **Mới:** hàm lợi thế.
- **Nguồn số:** $q_\pi(s_A,1)=1{,}8$, $v_\pi(s_A)=1{,}4$, $v_\pi(s_B)=2$ từ `1-10`, `1-11`; $q_\pi(s_B,\cdot)=(3;\,0)$ vì lượt kết thúc sau bước ở $s_B$.
- **Hình:** sửa `chuoi-loi-the.svg`: dưới ô $s_A$ ghi "$v_\pi=1{,}4$", dưới ô $s_B$ ghi "$v_\pi=2$"; nhãn cung dạng "1: $q_\pi=1{,}8$, $A_\pi=+0{,}4$", "2: $q_\pi=1$, $A_\pi=-0{,}4$", "1: $q_\pi=3$, $A_\pi=+1$", "2: $q_\pi=0$, $A_\pi=-2$" (#13: ghi rõ $q_\pi$, $v_\pi$); cung lợi thế dương xanh nét liền, âm đỏ nét đứt. Nửa phải.
- **Ghi chú nguồn:** đoạn mở §2.3; Định nghĩa 10.4 và đoạn sau; Ví dụ 10.6 "Lợi thế".
- **Diễn giả:** quy ước $A_\pi=0$ tại trạng thái hấp thụ. Kỳ vọng của $A_\pi(s,\cdot)$ theo $\pi(\cdot\mid s)$ bằng $0$: $\tfrac12\cdot0{,}4-\tfrac12\cdot0{,}4=0$, $\tfrac23\cdot1-\tfrac13\cdot2=0$ (Mệnh đề 10.5(a)). Lợi thế xếp hành động theo cùng thứ tự với $q_\pi$.
- **Phút:** 1,5.

#### `L10-2-09` · Gradient dạng lợi thế (mã mới; #14)

- **Câu:** 3. **Nhãn:** "Hệ quả.", "Giả thiết:", "Kết luận:", "Ý nghĩa:".
- **Mặt trang:**
  - "**Hệ quả** (gradient dạng lợi thế). Giả thiết: giả thiết chung. Thêm: lợi thế $A_\pi$ là của chính $\pi=\pi_\theta$. Kết luận:" $$\nabla_\theta J(\theta)=\mathbb E\Bigl[\sum_{t=0}^{T-1}\gamma^t\,A_\pi(S_t,A_t)\,\psi_t\Bigr].$$
  - "Ý nghĩa: hướng tăng của $J$ là kỳ vọng của các hàm điểm, mỗi hàm điểm nhân với lợi thế của hành động đã chọn."
  - "Ở đây chỉ bước $t=0$ góp vào tọa độ $\theta_A$: $A_\pi(s_A,A_0)=\pm0{,}4$, $\psi_0=\pm0{,}5$, nên $\tfrac12\cdot0{,}4\cdot0{,}5+\tfrac12\cdot(-0{,}4)\cdot(-0{,}5)=0{,}2$." (Đ6)
  - "Lợi thế phải là của chính $\pi_\theta$. Với lợi thế của chính sách khác, $\sum_a\pi_\theta(a\mid s)A(s,a)$ không còn bằng $0$: trên bài toán một bước của ghi chú, lợi thế của chính sách đều cho $0{,}5$." (Đ2: giả thiết bị vi phạm)
- **Dựng dần:** (0) hệ quả; (1) ý nghĩa và dòng số; (2) dòng giả thiết bị vi phạm.
- **1 phút:** Gradient chỉ cần lợi thế của hành động đã chọn; trên chuỗi công thức cho lại $0{,}2$.
- **Mới:** gradient dạng lợi thế.
- **Nguồn số:** $A_\pi(s_A,\cdot)$ từ `2-06`; $\psi_A$ từ `1-11`; xác suất $\tfrac12$ là $p_A$, $1-p_A$; $0{,}2$ từ `1-11`; số $0{,}5$ là phản ví dụ của ghi chú (đoạn sau Mệnh đề 10.5, "Bỏ $A_\pi$ là của chính $\pi_\theta$": $\tfrac23\cdot1{,}5-\tfrac13\cdot1{,}5=0{,}5$).
- **Hình:** không. **Ghi chú nguồn:** Mệnh đề 10.5(b) (đề xuất N3: hệ quả của Mệnh đề 10.2); Ví dụ 10.6 "Gradient theo Mệnh đề 10.5(b)"; đoạn sau Mệnh đề 10.5.
- **Diễn giả:** tọa độ $\theta_B$: $0{,}9\cdot\tfrac12\bigl(\tfrac23\cdot1\cdot\tfrac13+\tfrac13\cdot(-2)(-\tfrac23)\bigr)=0{,}3$. Dạng chiếm dụng với $\tfrac1{1-\gamma}$ và $\nu^\pi$ ở ghi chú. $q_\pi$ và $v_\pi$ chưa biết, nên $A_\pi$ phải được ước lượng từ dữ liệu; trang `2-11` nêu điều này trên mặt trang.
- **Phút:** 1,5.

#### `L10-2-10` · Ý tưởng chứng minh: gradient dạng lợi thế (mã mới; #14)

- **Câu:** 3. **Nhãn:** "Ý tưởng chứng minh." (tiêu đề), "Ký hiệu:", "Câu hỏi:".
- **Mặt trang** (tên bước theo chứng minh Mệnh đề 10.5 trong ghi chú, Đ8; số bước của ghi chú bắt đầu từ 2 nên trên trang chỉ ghi tên bước):
  - "Ký hiệu: $H_t$ là lịch sử tới $S_t$."
  - "Đường cơ sở $b=v_\pi$: $\nabla_\theta J=\sum_t\gamma^t\,\mathbb E\bigl[(G_t-v_\pi(S_t))\,\psi_t\bigr]$."
  - "Tính chất tháp theo $(H_t,A_t)$: $\psi_t$ và $v_\pi(S_t)$ là hàm của $(H_t,A_t)$, nên ra ngoài kỳ vọng có điều kiện:" $$\mathbb E\bigl[(G_t-v_\pi(S_t))\psi_t\bigr]=\mathbb E\bigl[(\mathbb E[G_t\mid H_t,A_t]-v_\pi(S_t))\,\psi_t\bigr].$$
  - "Tính Markov: $\mathbb E[G_t\mid H_t,A_t]=q_\pi(S_t,A_t)$, và $q_\pi-v_\pi=A_\pi$. $\square$"
  - Hộp "Câu hỏi: vì sao bước tính Markov cần chính sách Markov dừng?" → mảnh sau: "Để phần tương lai của lượt, khi biết $(H_t,A_t)$, chỉ phụ thuộc $(S_t,A_t)$. Khi đó kỳ vọng của $G_t$ là $q_\pi(S_t,A_t)$." (Đ9)
- **Dựng dần:** từng bước một mảnh; câu hỏi; lời giải câu hỏi.
- **1 phút:** Ba bước: đường cơ sở $v_\pi$, tính chất tháp, tính Markov.
- **Mới:** không (lập luận). **Nguồn số:** không.
- **Hình:** không. **Ghi chú nguồn:** Mệnh đề 10.5, chứng minh Bước 2 (Mệnh đề 10.2 với $b=v_\pi$), Bước 3 (tính chất tháp theo $(H_t,A_t)$), Bước 4 (tính Markov).
- **Diễn giả:** Bước 1 của ghi chú là kết luận $\sum_a\pi(a\mid s)A_\pi(s,a)=0$, đã nêu ở `2-06`. Bước tính Markov cho nghĩa: $G_t$ bằng $q_\pi(S_t,A_t)$ cộng một phần ngẫu nhiên có kỳ vọng $0$; thay $G_t$ bằng $A_\pi$ là bỏ phần đó và bỏ mức chung $v_\pi$.
- **Phút:** 2.

#### `L10-2-07` · Sai số TD với $v_\pi$ là ước lượng không chệch của lợi thế (giữ mã, chức năng "đánh giá sau một bước"; #15)

- **Câu:** 4 (mạch 2). **Nhãn:** "Nhắc lại:", "Mệnh đề.", "Chứng minh.", "Lưu ý:" (ngoại lệ TB13, §7).
- **Mặt trang:**
  - "$G_t$ có kỳ vọng có điều kiện $q_\pi(S_t,A_t)$ nhưng chứa mọi phần thưởng ngẫu nhiên sau bước $t$. $R_{t+1}+\gamma v_\pi(S_{t+1})$ có cùng kỳ vọng có điều kiện và chỉ chứa phần ngẫu nhiên của một bước."
  - "Nhắc lại: sai số TD (Bài 05) với giá trị $v_\pi$, $v_\pi=0$ tại trạng thái kết thúc:" $$\delta_t=R_{t+1}+\gamma\,v_\pi(S_{t+1})-v_\pi(S_t).$$
  - "**Mệnh đề.** Giả thiết: giả thiết chung. Thêm: giá trị dùng trong $\delta_t$ là $v_\pi$ đúng. Kết luận: $\mathbb E[\delta_t\mid S_t=s,A_t=a]=A_\pi(s,a)$."
  - "Chứng minh. Phương trình Bellman cho $\mathbb E[R_{t+1}+\gamma v_\pi(S_{t+1})\mid s,a]=q_\pi(s,a)$, rồi trừ $v_\pi(s)$."
  - "Lưu ý: điều kiện theo cặp $(S_t,A_t)$. Theo riêng $S_t$, $\mathbb E[\delta_t\mid S_t]=0$." (Đ2: biến thể)
  - "Trên chuỗi, chọn 1 tại $s_A$ cho $\delta_0=0+0{,}9\cdot2-1{,}4=0{,}4$, chọn 2 cho $\delta_0=1+0-1{,}4=-0{,}4$."
- **Dựng dần:** (0) hai câu bài toán; (1) nhắc lại; (2) mệnh đề, chứng minh; (3) lưu ý; (4) dòng số và hình.
- **1 phút:** Thay phần sau bước đầu của lợi tức bằng $\gamma v_\pi(S_{t+1})$ cho sai số TD, vẫn có kỳ vọng bằng lợi thế; trên chuỗi $\delta_0$ bằng đúng lợi thế $\pm0{,}4$.
- **Mới:** mệnh đề sai số TD và lợi thế (sai số TD là nhắc lại).
- **Nguồn số:** $v_\pi$ từ `1-10`; $A_\pi(s_A,\cdot)$ từ `2-06`.
- **Hình:** mới `sai-so-td-mot-buoc.svg` (thay `critic-mot-buoc.svg`, #15): ô $s_A$ ghi "$v_\pi=1{,}4$", cung "1, thưởng 0" sang ô $s_B$ ghi "$v_\pi=2$"; khung trên cung: "$\delta_0=0+0{,}9\cdot2-1{,}4=0{,}4=A_\pi(s_A,1)$"; cung "2, thưởng 1" tới ô kết thúc, khung "$\delta_0=1-1{,}4=-0{,}4=A_\pi(s_A,2)$"; không có khung actor, critic. Nửa phải, khoảng 40%.
- **Ghi chú nguồn:** Mệnh đề 10.8(a) và đoạn sau; dòng "Chứng minh." là Bước 1 (kỳ vọng của mục tiêu một bước) của ghi chú; đoạn cuối §2.4.
- **Diễn giả:** sai số TD là cách thứ ba so lợi tức với giá trị của trạng thái: lợi tức một bước thay cho lợi tức cả lượt. Mặt nạ kết thúc: $v_\pi=0$ tại trạng thái kết thúc. Mệnh đề 10.8(b) của ghi chú cho độ chệch khi giá trị sai; mạch 3 dùng nó.
- **Phút:** 1,5.

#### `L10-2-08` · Ba hệ số của hàm điểm trên chuỗi hai trạng thái (giữ mã; #16)

- **Câu:** 4. **Nhãn:** "Nhắc lại:".
- **Mặt trang:**
  - "Nhắc lại: $v_\pi=(1{,}4;\,2)$; $\psi_A=+0{,}5$ khi chọn 1, $-0{,}5$ khi chọn 2. Tọa độ $\theta_A$ của ba ước lượng:"

    | Loại lượt | Xác suất | $G_0\psi_A$ | $(G_0-1{,}4)\psi_A$ | $\delta_0$ | $\delta_0\psi_A$ |
    |---|---|---|---|---|---|
    | $s_A\xrightarrow1s_B\xrightarrow1$ | $p_Ap_B=\tfrac13$ | $2{,}7\cdot0{,}5=1{,}35$ | $1{,}3\cdot0{,}5=0{,}65$ | $0+0{,}9\cdot2-1{,}4=0{,}4$ | $0{,}2$ |
    | $s_A\xrightarrow1s_B\xrightarrow2$ | $p_A(1-p_B)=\tfrac16$ | $0$ | $-0{,}7$ | như hàng trên, $0{,}4$ | $0{,}2$ |
    | $s_A\xrightarrow2$ | $1-p_A=\tfrac12$ | $-0{,}5$ | $0{,}2$ | $1-1{,}4=-0{,}4$ | $0{,}2$ |
  - "$\delta_0$ chỉ dùng bước đầu, nên hai lượt đầu cho cùng $\delta_0$: phần ngẫu nhiên ở $s_B$ không còn trong hệ số."
- **Dựng dần:** (0) nhắc lại, bảng đến cột thứ tư; (1) cột $\delta_0$; (2) cột $\delta_0\psi_A$ và dòng cuối. Hai cột giữa ghi đủ phép tính ở hàng đầu, các hàng sau chỉ ghi kết quả đã tính ở `1-04`, `2-02` (Đ10); hàng ba của cột $\delta_0$ ghi đủ vì khác khuôn.
- **1 phút:** Với $v_\pi$ đúng, cả ba loại lượt cho cùng tọa độ $0{,}2$.
- **Mới:** cột $\delta_0$ (một đối tượng; giữ cột đầu vào của hai trang trước, #16).
- **Nguồn số:** mọi ô có phép tính; $v_\pi$ nhắc lại.
- **Hình:** không (không đặt sơ đồ neo cạnh bảng tính, #16).
- **Ghi chú nguồn:** Ví dụ 10.6, bảng "Ba loại lượt" và đoạn sau bảng.
- **Diễn giả:** "$\delta_0$ với $v_\pi$ đúng", không gọi là critic (#15). Tọa độ $\theta_B$ của ba ước lượng có cùng phương sai $0{,}18$ (ghi chú), vì lượt kết thúc ngay sau $s_B$.
- **Phút:** 1,5.

#### `L10-2-11` · Ba ước lượng có cùng kỳ vọng và phương sai giảm dần (mã mới; trạm dừng TB5; #16)

- **Câu:** 4–5. **Nhãn:** không; hộp.
- **Mặt trang:**

  "Xác suất ba loại lượt: $p_Ap_B=\tfrac13$, $p_A(1-p_B)=\tfrac16$, $1-p_A=\tfrac12$."

  | Hệ số | Kỳ vọng | Phương sai | Xác suất ngược dấu |
  |---|---|---|---|
  | $G_0$ | $\tfrac13\cdot1{,}35+\tfrac12\cdot(-0{,}5)=0{,}2$ | $\tfrac13\cdot1{,}35^2+\tfrac12\cdot0{,}5^2-0{,}2^2=0{,}6925$ | $\tfrac12$ |
  | $G_0-v_\pi(s_A)$ | $\tfrac13\cdot0{,}65-\tfrac16\cdot0{,}7+\tfrac12\cdot0{,}2=0{,}2$ | $\tfrac13\cdot0{,}65^2+\tfrac16\cdot0{,}7^2+\tfrac12\cdot0{,}2^2-0{,}2^2=0{,}2025$ | $\tfrac16$ |
  | $\delta_0$ với $v_\pi$ | $0{,}2$ | $0$ | $0$ |
  - Hộp: "Ba hệ số có cùng kỳ vọng bằng gradient. Hai hệ số sau cần $v_\pi$, và $v_\pi$ chưa biết khi chỉ có dữ liệu."
- **Dựng dần:** (0) hàng $G_0$; (1) hàng thứ hai; (2) hàng thứ ba; (3) hộp.
- **1 phút:** Kỳ vọng giữ $0{,}2$; phương sai $0{,}69\to0{,}20\to0$; mọi cải tiến đều cần $v_\pi$.
- **Mới:** không (gom kết quả; ba ước lượng đã trình bày riêng ở `1-04`, `2-02`, `2-07`, nay trên cùng bảng, cùng tên cột, Đ3). **Nguồn số:** cột tích từ `2-08`; phép tính trong ô.
- **Hình:** không. **Ghi chú nguồn:** Ví dụ 10.6, hai hàng cuối bảng và đoạn sau bảng.
- **Diễn giả:** kết quả mạch: đường cơ sở giữ kỳ vọng; lợi thế là kỳ vọng có điều kiện của hệ số; sai số TD với giá trị đúng loại phần ngẫu nhiên sau một bước. Mạch sau thay $v_\pi$ bằng một hàm học từ dữ liệu.
- **Phút:** 1,5.

---

### Mạch 3. Ước lượng lợi thế: độ chệch và phương sai (`id="mach-3"`, 13 trang, 21,5 phút)

Thứ tự: `3-00` → `3-01` → `3-06` → `3-07` → `3-02` → `3-08` → `3-11` → `3-05` → `3-09` → `3-12` → `3-13` → `3-04` → `3-10`. Mã mới `3-13` (góp ý tác giả #2, #3: dựng quy tắc cập nhật critic trước khi dùng). Mã mới thêm ở cổng: `3-11`, `3-12` (trang ý tưởng chứng minh, TB28). Mã bỏ: `3-03` (đã bỏ từ trước, không dùng lại). Hành trình: bài toán (critic có sai số) `3-01` → hiện tượng chệch/phương sai trên ví dụ `3-06` → công cụ `3-07`, `3-02` → kết quả `3-08`, `3-09` → ví dụ $\lambda$ `3-05` → một vòng tay `3-04` → thuật toán `3-10` (TB31). Critic, actor giới thiệu ở `3-01` (#15).

#### `L10-3-00` · Ước lượng lợi thế: độ chệch và phương sai (trang tiêu đề mạch; điểm vào mạch 3; giữ mã; #17)

- **Mặt trang:** "3."; `h2` "Ước lượng lợi thế: độ chệch và phương sai"; `p.strand-lead` "Tổ hợp có trọng số các ước lượng lợi thế nhiều bước cân bằng độ chệch và phương sai."
- **Hình:** `so-do-neo-m3-vao.svg`.
- **Diễn giả:** "Mạch trước cho các hệ số không chệch khi biết $v_\pi$. Trong thực hành $v_\pi$ được thay bằng một hàm học từ dữ liệu, có sai số. Mạch này đo độ chệch và phương sai của các ước lượng lợi thế khi đó và đưa ra GAE cùng thuật toán actor–critic với GAE." **Phút:** 0,5.

#### `L10-3-01` · Critic và actor (giữ mã, chức năng mở mạch; #15, #18, #19)

- **Câu:** 1 (mạch 3). **Nhãn:** "Định nghĩa.".
- **Mặt trang:**
  - "$v_\pi$ chưa biết, nên được thay bằng một hàm giá trị $\hat v(s,w)$ học từ dữ liệu."
  - "**Định nghĩa.** Hàm $\hat v(\cdot,w)$ gọi là critic khi nó đánh giá hành động $A_t$ qua mục tiêu một bước $R_{t+1}+\gamma(1-Z_{t+1})\,\hat v(S_{t+1},w)$, trong đó $Z_{t+1}=1$ khi $S_{t+1}$ là trạng thái kết thúc. Chính sách $\pi_\theta$ gọi là actor. Phương pháp actor–critic cập nhật $\theta$ theo hệ số lập từ critic, và cập nhật $w$ để $\hat v$ xấp xỉ $v_\pi$."
  - "Trên chuỗi, giả định critic $\hat v=(1{,}4;\,1)$, học từ ít lượt qua $s_B$: đúng ở $s_A$, thấp hơn $v_\pi(s_B)=2$ một đơn vị."
- **Dựng dần:** (0) dòng mở, định nghĩa; (1) dòng giả định, hình.
- **1 phút:** Critic là hàm giá trị học được, có thể sai; ở đây critic đánh giá $s_B$ là $1$ thay cho $2$.
- **Mới:** critic và actor (định nghĩa); critic sai giả định.
- **Nguồn số:** $v_\pi=(1{,}4;\,2)$ từ `1-10`; $\hat v=(1{,}4;\,1)$ là giả định, lý do nêu trên trang (#19, TB29).
- **Hình:** sửa `chuoi-critic-sai.svg`: dưới ô $s_A$ ghi "$\hat v=1{,}4=v_\pi$" (xanh), dưới ô $s_B$ ghi "$\hat v=1$ (cam, nét đứt) $<v_\pi=2$ (xanh)" (#18: cả hai trạng thái); các cung giữ nhãn hành động và phần thưởng. Nửa phải.
- **Ghi chú nguồn:** Định nghĩa 10.7 và đoạn sau; đoạn trước Định nghĩa 10.7 (critic $(1{,}4;\,1)$); Ví dụ 10.7, "Dữ kiện".
- **Diễn giả:** $s_B$ chỉ được thăm ở một nửa số lượt, nên critic học từ ít dữ liệu dễ sai ở đó. Phép bootstrap phân biệt critic với đường cơ sở của mạch 2: $\hat v$ đánh giá cả trạng thái thứ hai của bước chuyển. Khi $Z_{t+1}=1$, mục tiêu chỉ còn $R_{t+1}$. Actor–critic còn gọi là A2C (ghi chú).
- **Phút:** 1,5.

#### `L10-3-06` · Với critic sai, ước lượng một bước bị chệch, ước lượng cả lượt có phương sai lớn (mã mới, tách từ `3-01` cũ; #18, #19)

- **Câu:** 2 (mạch 3). **Nhãn:** hộp ý chính.
- **Mặt trang:**
  - "Nhắc lại: critic $\hat v=(1{,}4;\,1)$, giá trị đúng $v_\pi=(1{,}4;\,2)$, $p_B=\tfrac23$, $\gamma=0{,}9$." (Đ1)
  - "Cần ước lượng $A_\pi(s_A,1)=0{,}4$ từ một lượt bắt đầu bằng hành động 1 ở $s_A$."

    | Lượt | Xác suất | $R_1$, $R_2$ | Một bước: $\delta_0=R_1+\gamma\hat v(s_B)-\hat v(s_A)$ | Cả lượt: $G_0-\hat v(s_A)$, $G_0=R_1+\gamma R_2$ |
    |---|---|---|---|---|
    | (i) $s_A\xrightarrow1s_B\xrightarrow1$ | $p_B=\tfrac23$ | $0$, $3$ | $0+0{,}9\cdot1-1{,}4=-0{,}5$ | $0+0{,}9\cdot3-1{,}4=1{,}3$ |
    | (ii) $s_A\xrightarrow1s_B\xrightarrow2$ | $1-p_B=\tfrac13$ | $0$, $0$ | như (i), $-0{,}5$ | $0-1{,}4=-1{,}4$ |
    | kỳ vọng | | | $-0{,}5$ | $\tfrac23\cdot1{,}3-\tfrac13\cdot1{,}4=0{,}4$ |
    | độ chệch (so với $0{,}4$) | | | $-0{,}5-0{,}4=-0{,}9$ | $0$ |
    | phương sai | | | $0$ | $\tfrac23\cdot1{,}3^2+\tfrac13\cdot1{,}4^2-0{,}4^2=1{,}62$ |
  - Hộp: "Ước lượng một bước chệch $-0{,}9=\gamma\bigl(\hat v(s_B)-v_\pi(s_B)\bigr)$ và sai dấu. Ước lượng cả lượt không chệch nhưng hai lượt cách nhau $2{,}7$."
  - "Lưu ý: độ chệch là kỳ vọng của ước lượng trừ đại lượng cần ước lượng, $0{,}4$. Nó không phải sai số của một lượt." (Đ4)
- **Dựng dần:** (0) nhắc lại, dòng mục tiêu, bảng đến cột $R$; (1) cột một bước và ba hàng cuối của cột đó; (2) cột cả lượt và ba hàng cuối; (3) hộp, lưu ý. Hàng (ii) cột một bước ghi "như (i)" (Đ10).
- **1 phút:** Critic đánh giá thấp $s_B$ làm ước lượng một bước luôn bằng $-0{,}5$, sai dấu; dùng cả lượt thì đúng kỳ vọng $0{,}4$ nhưng phương sai $1{,}62$.
- **Mới:** bảng hai ước lượng lợi thế (một đối tượng).
- **Nguồn số:** $A_\pi(s_A,1)=0{,}4$ từ `2-06`; $\hat v$ từ `3-01`; $p_B$ từ `1-09`; $v_\pi(s_B)=2$ từ `1-10`; phép tính trong ô.
- **Hình:** không (bảng). Có thể đặt `chuoi-critic-sai.svg` thu nhỏ ở góc trên phải nếu vừa.
- **Ghi chú nguồn:** đoạn mở §3; Ví dụ 10.8 (hai hàng "một bước", "hai bước"); Mệnh đề 10.8(b) cho độ chệch.
- **Diễn giả:** độ chệch đến từ $\hat v(s_B)$ trong mục tiêu một bước (Mệnh đề 10.8(b): $\gamma\sum_{s'}P(s'\mid s,a)e(s')-e(s)$ với $e=\hat v-v_\pi=(0;\,-1)$). Ước lượng cả lượt không dùng $\hat v(s_B)$ nên không chệch; $\hat v(s_A)$ đúng nên không có phần chệch ở $s_A$. Ghi chú dùng "khoảng cách hai lượt" $2{,}7$; phương sai $=\tfrac29\cdot2{,}7^2=1{,}62$.
- **Phút:** 2,5.

#### `L10-3-07` · Lợi thế $n$ bước (mã mới)

- **Câu:** 3 (mạch 3). **Nhãn:** "Định nghĩa.".
- **Mặt trang:**
  - "Giữa một bước và cả lượt: dùng $n$ phần thưởng quan sát được rồi thay phần còn lại bằng giá trị của critic."
  - "**Định nghĩa.** Với critic $\hat v$ cố định và $t<T$, lợi tức $n$ bước và lợi thế $n$ bước là" $$G_{t:t+n}=\sum_{k=0}^{n-1}\gamma^kR_{t+k+1}+\gamma^n\hat v(S_{t+n})\ \ (t+n<T),\qquad \widehat A^{(n)}_t=G_{t:t+n}-\hat v(S_t),$$ "với $G_{t:t+n}=G_t$ khi $t+n\ge T$."
  - "Trên lượt (i): $\widehat A^{(1)}_0=\delta_0=-0{,}5$; $\widehat A^{(2)}_0=G_0-\hat v(s_A)=1{,}3$; $\delta_1=3-\hat v(s_B)=2$ và $1{,}3=-0{,}5+0{,}9\cdot2=\delta_0+\gamma\delta_1$."
- **Dựng dần:** (0) dòng mở, định nghĩa; (1) dòng số.
- **1 phút:** Lợi thế $n$ bước nối hai đầu của trang trước; trên chuỗi, $n=1$ là ước lượng một bước, $n=2$ là ước lượng cả lượt, và nó bằng tổng các sai số TD.
- **Mới:** lợi thế $n$ bước.
- **Nguồn số:** $\delta_0$, $1{,}3$ từ `3-06`; $\delta_1=R_2+0-\hat v(s_B)$ (mặt nạ tắt ở bước cuối).
- **Hình:** không. **Ghi chú nguồn:** Định nghĩa 10.11; Bổ đề 10.12; Ví dụ 10.8, "Kiểm tra lại".
- **Diễn giả:** $n=1$ là mục tiêu TD(0), $n\ge T-t$ là lợi tức Monte Carlo. Đẳng thức $\widehat A^{(n)}_t=\sum_{k<n}\gamma^k\delta_{t+k}$ (Bổ đề 10.12) là tổng lồng nhau, đúng trên từng lượt khi critic cố định trong lượt; trang `3-08` dùng nó.
- **Phút:** 1.

#### `L10-3-02` · Ước lượng lợi thế tổng quát (giữ mã)

- **Câu:** 3. **Nhãn:** "Định nghĩa.", "Ý nghĩa:".
- **Mặt trang:**
  - "Trên lượt (i), trộn ước lượng một bước $-0{,}5$ và ước lượng cả lượt $1{,}3$ với trọng số $\tfrac12$, $\tfrac12$ cho $0{,}4$. Trên lượt (ii) cho $-0{,}95$." (Đ5: trực quan trên chuỗi trước định nghĩa)
  - "**Định nghĩa.** Với $\lambda\in[0,1)$, lợi tức λ là trung bình có trọng số $(1-\lambda)\lambda^{n-1}$ của các lợi tức $n$ bước. Ước lượng lợi thế tổng quát (generalized advantage estimation, GAE) là" $$G^\lambda_t=(1-\lambda)\sum_{n\ge1}\lambda^{n-1}G_{t:t+n},\qquad\widehat A_t=G^\lambda_t-\hat v(S_t),$$ "và $G^1_t=G_t$ khi $\lambda=1$."
  - "Ý nghĩa: $\lambda$ nhỏ dựa nhiều vào critic, $\lambda$ gần $1$ dựa nhiều vào phần thưởng quan sát được."
  - "Ở đây, trên lượt (i), $G_{0:1}=0+0{,}9\cdot\hat v(s_B)=0{,}9$ và $G_{0:n}=G_0=2{,}7$ với $n\ge2$; với $\lambda=0{,}5$: $G^{0{,}5}_0=0{,}5\cdot0{,}9+0{,}5\cdot2{,}7=1{,}8$, nên $\widehat A_0=1{,}8-1{,}4=0{,}4$."
- **Dựng dần:** (0) dòng trực quan; (1) định nghĩa; (2) ý nghĩa và hình; (3) dòng số ("Ở đây $G_{0:1}=0{,}9$, $G_{0:2}=G_0=2{,}7$", Đ6).
- **1 phút:** GAE là tổ hợp có trọng số của các lợi thế $n$ bước; $\lambda$ quyết định trọng số.
- **Mới:** GAE.
- **Nguồn số:** $G_{0:1}=0+0{,}9\cdot\hat v(s_B)=0{,}9$; $G_{0:n}=G_0=2{,}7$ với $n\ge2$; trọng số $1-\lambda=0{,}5$ cho $n=1$, phần còn lại $\lambda=0{,}5$ dồn vào $G_0$.
- **Hình:** mới `gae-weights-trang.svg` (thay việc dùng lại `gae-weights.svg` của ghi chú, vẽ theo cùng tham số với ví dụ, $\lambda=0{,}5$, $\gamma=0{,}9$): trái, cột trọng số $(1-\lambda)\lambda^{n-1}$ của lợi tức $n$ bước, $0{,}5$; $0{,}25$; $0{,}125$; $0{,}0625$; …; phải, cột trọng số $(\gamma\lambda)^k$ của sai số TD, $1$; $0{,}45$; $0{,}2025$; $0{,}091$; …; dưới hình ghi "trên chuỗi, $T-t-1=1$: trọng số $0{,}5$ cho $G_{0:1}$, $0{,}5$ dồn vào $G_0$". Nhãn ≥ 20 px. Nửa phải.
- **Ghi chú nguồn:** Định nghĩa 10.13 và đoạn sau; hình trọng số.
- **Diễn giả:** trọng số cộng lại bằng $1$; với lượt kết thúc, phần trọng số $\lambda^{T-t-1}$ dồn vào lợi tức thật. Với $\lambda=0$ được $\delta_t$, với $\lambda=1$ được $G_t-\hat v(S_t)$.
- **Phút:** 1,5.

#### `L10-3-08` · Dạng tổng và công thức truy hồi của GAE (mã mới)

- **Câu:** 3. **Nhãn:** "Mệnh đề.", "Ý nghĩa:".
- **Mặt trang:**
  - "**Mệnh đề.** Giả thiết: critic cố định trong lượt, $\delta_k=0$ khi $k\ge T$, $\lambda\in[0,1]$. Kết luận:"
  - "(a) $\widehat A_t=\sum_{k=0}^{T-t-1}(\gamma\lambda)^k\,\delta_{t+k}$. (b) $\lambda=0$ cho $\widehat A_t=\delta_t$, $\lambda=1$ cho $\widehat A_t=G_t-\hat v(S_t)$." $$\text{(c)}\quad\widehat A_t=\delta_t+\gamma\lambda\,(1-Z_{t+1})\,\widehat A_{t+1},\qquad\widehat A_T=0.$$
  - "Ý nghĩa: mọi $\widehat A_t$ của một lượt tính được bằng một lượt quét lùi."
  - "Ở đây, trên lượt (i), $\delta_1=2$, $\delta_0=-0{,}5$, $\gamma\lambda=0{,}45$: $\widehat A_1=2$, $\widehat A_0=-0{,}5+0{,}45\cdot2=0{,}4$." (Đ6)
- **Dựng dần:** (0) mệnh đề; (1) ý nghĩa; (2) hình tính lùi (ba bước) và dòng số.
- **1 phút:** GAE là tổng các sai số TD với trọng số $(\gamma\lambda)^k$ và tính được bằng một lượt quét lùi.
- **Mới:** dạng tổng và truy hồi.
- **Nguồn số:** $\delta_0=-0{,}5$, $\delta_1=2$ từ `3-07`; kết quả $0{,}4$ trùng `3-02`.
- **Hình:** `gae-tinh-lui-buoc0.svg`, `-buoc1.svg`, `gae-tinh-lui.svg` (giữ). Dải dưới.
- **Ghi chú nguồn:** Mệnh đề 10.14; đoạn sau Mệnh đề 10.14. Chứng minh ở trang `3-11` (TB28 dạng trang riêng, §7).
- **Diễn giả:** mặt nạ $(1-Z_{t+1})$ không đổi kết quả trên lượt đầy đủ, nhưng cần trên đoạn thu có nhiều lượt; trên đoạn thu còn cờ cắt ngắn (Thuật toán 10.16, Bài tập 10.7).
- **Phút:** 1,5.

#### `L10-3-11` · Ý tưởng chứng minh: dạng tổng và công thức truy hồi của GAE (mã mới; TB28 dạng trang riêng, Đ8, Đ9)

- **Câu:** 3. **Nhãn:** "Ý tưởng chứng minh." (tiêu đề), "Câu hỏi:".
- **Mặt trang** (bốn bước của chứng minh Mệnh đề 10.14 trong ghi chú, Đ8):
  - "Bước 1 (thay lợi thế $n$ bước): $\widehat A_t=(1-\lambda)\sum_{n\ge1}\lambda^{n-1}\widehat A^{(n)}_t$, và mỗi $\widehat A^{(n)}_t=\sum_{k<n}\gamma^k\delta_{t+k}$ (tổng lồng nhau)."
  - "Bước 2 (đổi thứ tự lấy tổng): hệ số của $\gamma^k\delta_{t+k}$ là" $$(1-\lambda)\sum_{n>k}\lambda^{n-1}=\lambda^k .$$
  - "Bước 3 (hai đầu mút): $\lambda=0$ giữ số hạng $k=0$. $\lambda=1$ được xét riêng vì thừa số $1-\lambda$ bằng $0$."
  - "Bước 4 (truy hồi): tách số hạng $k=0$ của (a) được $\delta_t+\gamma\lambda\widehat A_{t+1}$. $\square$"
  - Hộp "Câu hỏi: vì sao Bước 1 cần critic cố định trong cả lượt?" → mảnh sau: "Để $\hat v(S_{t+1})$ trong $\delta_t$ và trong $\delta_{t+1}$ là cùng một số, nên triệt tiêu trong tổng lồng nhau." (Đ9)
- **Dựng dần:** từng bước một mảnh; câu hỏi; lời giải.
- **1 phút:** GAE là tổ hợp của các lợi thế $n$ bước, mỗi lợi thế là tổng lồng nhau của sai số TD; đổi thứ tự tổng cho trọng số $(\gamma\lambda)^k$.
- **Mới:** không. **Nguồn số:** không.
- **Hình:** không. **Ghi chú nguồn:** Mệnh đề 10.14, chứng minh Bước 1–4; Bổ đề 10.12.
- **Diễn giả:** Bổ đề 10.12 (lợi thế $n$ bước bằng tổng sai số TD) là đồng nhất thức trên từng lượt, kiểm ở `3-07`. Nếu $\hat v$ đổi giữa hai bước, tổng sai lệch khỏi $\widehat A^{(n)}_t$ bằng $\gamma$ nhân hiệu hai giá trị (ghi chú).
- **Phút:** 2.

#### `L10-3-05` · Tham số $\lambda$ cân bằng độ chệch và phương sai (giữ mã)

- **Câu:** 4 (mạch 3). **Nhãn:** hộp.
- **Mặt trang:**
  - "$\widehat A_0=\delta_0+0{,}9\lambda\,\delta_1$ trên hai lượt, critic $(1{,}4;\,1)$, mục tiêu $A_\pi(s_A,1)=0{,}4$:"

    | | $\lambda=0$ | $\lambda=0{,}5$ | $\lambda=1$ |
    |---|---|---|---|
    | (i), $\tfrac23$: $\delta_1=3-1=2$ | $-0{,}5$ | $-0{,}5+0{,}45\cdot2=0{,}4$ | $-0{,}5+0{,}9\cdot2=1{,}3$ |
    | (ii), $\tfrac13$: $\delta_1=0-1=-1$ | $-0{,}5$ | $-0{,}5-0{,}45=-0{,}95$ | $-0{,}5-0{,}9=-1{,}4$ |
    | kỳ vọng $-0{,}5+0{,}9\lambda$ | $-0{,}5$ | $-0{,}05$ | $0{,}4$ |
    | độ chệch $-0{,}9(1-\lambda)$ | $-0{,}9$ | $-0{,}45$ | $0$ |
    | phương sai $\tfrac29(2{,}7\lambda)^2=1{,}62\lambda^2$ | $0$ | $0{,}405$ | $1{,}62$ |
  - Hộp: "$\lambda$ tăng thì độ chệch giảm và phương sai tăng."
- **Dựng dần:** (0) dòng mở, hai hàng lượt; (1) hàng kỳ vọng; (2) độ chệch, phương sai; (3) hộp.
- **1 phút:** Với critic sai, chọn $\lambda$ là chọn giữa độ chệch và phương sai.
- **Mới:** bảng theo $\lambda$ (một đối tượng; cùng khuôn `3-06`).
- **Nguồn số:** $\delta_0$, $\delta_1$ từ `3-06`, `3-07`; kỳ vọng $\tfrac23(-0{,}5+1{,}8\lambda)+\tfrac13(-0{,}5-0{,}9\lambda)=-0{,}5+0{,}9\lambda$; phương sai $\tfrac23\cdot\tfrac13\cdot(2{,}7\lambda)^2$ vì hai giá trị cách nhau $2{,}7\lambda$.
- **Hình:** không.
- **Ghi chú nguồn:** Ví dụ 10.8 (bảng, "Diễn giải"); Ví dụ 10.9.
- **Diễn giả:** với $\lambda=0{,}5$, lượt (i) cho đúng $0{,}4$ chỉ do trùng hợp; hàng kỳ vọng $-0{,}05$ mới là kết quả. Chỉ ở $s_A$ hành động 1 mới có độ chệch; hành động 2 kết thúc ngay nên $\widehat A_0=-0{,}4$ với mọi $\lambda$.
- **Phút:** 2.

#### `L10-3-09` · GAE không làm chệch gradient khi $\lambda=1$ hoặc critic đúng (mã mới; TB28)

- **Câu:** 4. **Nhãn:** "Mệnh đề.", "Lưu ý:".
- **Mặt trang:**
  - "**Mệnh đề.** Giả thiết: giả thiết chung. Thêm: critic cố định, bị chặn; GAE tính trên lượt đầy đủ. Kết luận: nếu $\lambda=1$, hoặc $\hat v=v_\pi$ và $\lambda$ tùy ý, thì" $$\mathbb E\Bigl[\sum_t\gamma^t\,\widehat A_t\,\psi_t\Bigr]=\nabla_\theta J(\theta).$$
  - "Trên chuỗi, tọa độ $\theta_A$ của kỳ vọng là $-0{,}025+0{,}225\lambda$: $-0{,}025$; $0{,}0875$; $0{,}2$ với $\lambda=0$; $0{,}5$; $1$."
  - "Lưu ý: mệnh đề nói về gradient, không về lợi thế. Với $\lambda=1$, tại $s_B$, kỳ vọng của $\widehat A_1$ vẫn chệch $+1$."
- **Dựng dần:** (0) mệnh đề; (1) dòng số; (2) lưu ý.
- **1 phút:** Với critic sai, chỉ $\lambda=1$ cho ước lượng gradient không chệch; $\lambda<1$ đổi độ chệch lấy phương sai.
- **Mới:** điều kiện không chệch của GAE.
- **Nguồn số:** $\tfrac12\cdot(-0{,}5+0{,}9\lambda)\cdot0{,}5+\tfrac12\cdot(-0{,}4)\cdot(-0{,}5)=-0{,}025+0{,}225\lambda$ (dòng số viết đủ công thức này ở mảnh (1)); kỳ vọng $-0{,}5+0{,}9\lambda$ từ `3-05`; $\widehat A_0=-0{,}4$ khi chọn hành động 2 vì lượt kết thúc ngay; $\mathbb E[\widehat A_1\mid s_B,\cdot]=(2;\,-1)$ so với $A_\pi(s_B,\cdot)=(1;\,-2)$.
- **Hình:** không.
- **Ghi chú nguồn:** Mệnh đề 10.15; Ví dụ 10.9; đoạn "Trong thực hành" sau Ví dụ 10.9. Chứng minh ở `3-12`.
- **Diễn giả:** Schulman và cộng sự (2016) gọi tính chất này là γ-just. Tại $s_B$, độ chệch $+1$ giống nhau cho hai hành động nên bị khử khi nhân hàm điểm (kỳ vọng $0$).
- **Phút:** 1.

#### `L10-3-12` · Ý tưởng chứng minh: GAE và gradient (mã mới; TB28 dạng trang riêng, Đ8, Đ9)

- **Câu:** 4. **Nhãn:** "Ý tưởng chứng minh." (tiêu đề), "Câu hỏi:".
- **Mặt trang** (năm bước của chứng minh Mệnh đề 10.15 trong ghi chú, Đ8):
  - "Bước 1 (trường hợp $\lambda=1$): $\widehat A_t=G_t-\hat v(S_t)$, và $\hat v$ là một đường cơ sở. Áp dụng mệnh đề đường cơ sở."
  - "Bước 2 (trường hợp $\hat v=v_\pi$, tách theo $k$): $\widehat A_t=\sum_k(\gamma\lambda)^k\delta_{t+k}$; xét từng $\mathbb E[\delta_{t+k}\psi_t]$."
  - "Bước 3 (các số hạng $k\ge1$ bằng $0$): $\psi_t$ là hàm của $H_{t+k}$, nên" $$\mathbb E[\delta_{t+k}\psi_t]=\mathbb E\bigl[\psi_t\,\mathbb E[A_\pi(S_{t+k},A_{t+k})\mid H_{t+k}]\bigr]=0 .$$
  - "Bước 4 (số hạng $k=0$): $\mathbb E[\delta_t\psi_t]=\mathbb E[A_\pi(S_t,A_t)\psi_t]$. Bước 5 (cộng theo $t$): gradient dạng lợi thế. $\square$"
  - Hộp "Câu hỏi: ở Bước 3, critic đúng được dùng ở đâu?" → mảnh sau: "Ở kỳ vọng có điều kiện của $\delta_{t+k}$: chỉ khi $\hat v=v_\pi$ nó bằng $A_\pi(S_{t+k},A_{t+k})$. Với critic sai, còn một số hạng chệch không bị khử." (Đ9)
- **Dựng dần:** từng bước một mảnh; câu hỏi; lời giải.
- **1 phút:** Với $\lambda=1$, GAE là lợi tức trừ một đường cơ sở; với critic đúng, mọi sai số TD sau bước $t$ nhân hàm điểm có kỳ vọng $0$.
- **Mới:** không. **Nguồn số:** không.
- **Hình:** không. **Ghi chú nguồn:** Mệnh đề 10.15, chứng minh Bước 1–5; Mệnh đề 10.8(a); Mệnh đề 10.5(a).
- **Diễn giả:** đẳng thức cuối của Bước 3 dùng $\sum_a\pi(a\mid s)A_\pi(s,a)=0$ (`2-06`). Lượt bị cắt ngắn giữa chừng làm mất Bước 1, vì $\widehat A_t$ khi đó bootstrap từ $\hat v$ (ghi chú: cắt ở $s_B$ cho $-0{,}025$ thay cho $0{,}2$).
- **Phút:** 2.

#### `L10-3-13` · Critic hồi quy về lợi tức λ (mã mới; góp ý tác giả #2, #3; TB24, TB27)

- **Nhãn:** "Định nghĩa."; hộp ví dụ.
- **Mặt trang:** bài toán (critic cần xấp xỉ $v_\pi$ chưa biết; dữ liệu của lượt cho mục tiêu thay thế); định nghĩa $V^{\mathrm{targ}}_t=\widehat A_t+\hat v(S_t,w_{\mathrm{old}})$, bằng $G^\lambda_t$ vì $\widehat A_t=G^\lambda_t-\hat v(S_t,w_{\mathrm{old}})$; bảng hai dòng $\lambda=0$ (mục tiêu TD, Bài 05), $\lambda=1$ ($G_t$, lợi tức Monte Carlo); một bước hạ gradient của $\tfrac12\sum_t(V^{\mathrm{targ}}_t-\hat v(S_t,w))^2$ với mục tiêu cố định: $w\leftarrow w+\alpha_w\sum_t(V^{\mathrm{targ}}_t-\hat v(S_t,w))\nabla_w\hat v(S_t,w)$; dạng bảng $w_{S_t}\leftarrow w_{S_t}+\alpha_w(V^{\mathrm{targ}}_t-w_{S_t})$; hộp: lượt (i), $\lambda=0{,}5$, critic $(1{,}4;\,1)$, $V^{\mathrm{targ}}_0=1{,}8=G^{0{,}5}_0$, $V^{\mathrm{targ}}_1=3=G_1$.
- **Dựng dần:** (0) bài toán; (1) định nghĩa; (2) bảng $\lambda$; (3) cập nhật; (4) hộp.
- **1 phút:** Mục tiêu của critic là lợi tức λ, nên critic dùng cùng $\lambda$ với actor.
- **Nguồn số:** $\widehat A_0=0{,}4$, $\widehat A_1=2$ (`3-02`, `3-08`); điều phối viên đã kiểm.
- **Ghi chú nguồn:** §2.3 (Thuật toán 10.6 và đoạn "Trong thực hành"); §3.3 (thuật toán actor–critic với GAE, bước 4); bảng ký hiệu ($V^{\mathrm{targ}}_t$). **Diễn giả:** vì sao mục tiêu là $\widehat A_t+\hat v$; câu "critic cân bằng độ chệch và phương sai bằng cùng $\lambda$" (chuyển xuống để vừa khung). **Phút:** 1,5.

#### `L10-3-04` · Câu hỏi nhanh: một vòng cập nhật với GAE (giữ mã, nội dung mới; TB22; ví dụ tay trước thuật toán)

- **Câu:** 4. **Nhãn:** "Câu hỏi:", "Lời giải:".
- **Mặt trang:**
  - "Lượt (i), $\lambda=0{,}5$: $\widehat A_0=0{,}4$ tại $(s_A,1)$, $\widehat A_1=2$ tại $(s_B,1)$. Actor cập nhật theo gradient dạng lợi thế, thay $A_\pi$ bằng $\widehat A_t$, với $\alpha_\theta=1$:" $$\theta\leftarrow\theta+\alpha_\theta\sum_t\gamma^t\,\widehat A_t\,\psi_t .$$
  - "Câu hỏi: từ $\theta=(0;\,\log2)$, tham số và chính sách mới bằng bao nhiêu?"
  - "Lời giải:" ba dòng mang tên mục tiêu con của `3-10` (Đ12):
    - "**Ước lượng lợi thế:** $\widehat A_1=\delta_1=2$, $\widehat A_0=-0{,}5+0{,}45\cdot2=0{,}4$."
    - "**Cập nhật actor:** $\theta_A=0+1\cdot0{,}4\cdot0{,}5=0{,}2$, $p_A=\sigma(0{,}2)=0{,}550$; $\theta_B=\log2+0{,}9\cdot2\cdot\tfrac13=\log2+0{,}6$, $p_B=\sigma(1{,}293)=0{,}785$."
    - "**Cập nhật critic** ($\alpha_w=0{,}5$, mục tiêu $\widehat A_t+\hat v(S_t)$): $w_A=1{,}4+0{,}5(1{,}8-1{,}4)=1{,}6$, $w_B=1+0{,}5(3-1)=2$."
- **Dựng dần:** (0) dữ kiện, câu hỏi; (1) lời giải.
- **1 phút:** Một vòng với GAE tăng cả $p_A$ lẫn $p_B$; với $\lambda=0$, cùng lượt sẽ giảm $p_A$ (ghi chú Ví dụ 10.7).
- **Mới:** quy tắc cập nhật actor với $\widehat A_t$.
- **Nguồn số:** $\widehat A_0$, $\widehat A_1$ từ `3-08`; $\psi_A(1)=0{,}5$, $\psi_B(1)=\tfrac13$ từ `1-11`; $\gamma^1=0{,}9$; $\sigma(0{,}2)=0{,}5498$, $\sigma(1{,}2931)=0{,}7847$; critic từ `3-01`.
- **Hình:** không. **Ghi chú nguồn:** Ví dụ 10.7 (cùng lượt, $\lambda=0$); đề xuất N9.
- **Diễn giả:** "Gợi ý: tọa độ $\theta_A$ chỉ nhận bước $t=0$, tọa độ $\theta_B$ chỉ nhận bước $t=1$ với trọng số $\gamma$." Câu hỏi chỉ hỏi phần actor; dòng critic đọc cùng lời giải. Với $\lambda=0$ (Ví dụ 10.7), $\widehat A_0=-0{,}5$ và $p_A$ giảm xuống $0{,}438$. Năng lực kiểm tra: áp dụng quy tắc cập nhật trên một lượt (NT-RL-10).
- **Phút:** 2.

#### `L10-3-10` · Thuật toán actor–critic với GAE (mã mới; TB31, #26)

- **Câu:** 4–5 (mạch 3). **Nhãn:** "Thuật toán.", "Đầu vào:", "Đầu ra:".
- **Mặt trang:**
  - "Ước lượng gradient của REINFORCE có phương sai lớn. Actor–critic thay lợi tức bằng hệ số GAE lập từ critic."
  - "Đầu vào: chính sách $\pi_\theta$, critic $\hat v(s,w)$; $\gamma\in[0,1)$, $\lambda\in[0,1]$; bước học $\alpha_\theta$, $\alpha_w$. Đầu ra: $\theta$, $w$."
  - "Lặp với mỗi lượt:"
    1. "**Thu lượt:** một lượt $S_0,A_0,R_1,\dots,S_T$ bằng $\pi_\theta$; giữ $w_{\mathrm{old}}=w$."
    2. "**Ước lượng lợi thế:** $\delta_t$ với $\hat v(\cdot,w_{\mathrm{old}})$; $\widehat A_T=0$, tính lùi $\widehat A_t=\delta_t+\gamma\lambda(1-Z_{t+1})\widehat A_{t+1}$."
    3. "**Cập nhật actor:** $\theta\leftarrow\theta+\alpha_\theta\sum_t\gamma^t\widehat A_t\,\psi_\theta(S_t,A_t)$."
    4. "**Cập nhật critic:** $w\leftarrow w+\alpha_w\sum_t\bigl(\widehat A_t+\hat v(S_t,w_{\mathrm{old}})-\hat v(S_t,w)\bigr)\nabla_w\hat v(S_t,w)$." (Đ12; cùng tên ở `3-04` và sơ đồ neo)
  - "Dừng sau số lượt đã định."
  - Hộp: "Mỗi lượt chỉ cho một bước cập nhật, vì các ước lượng cần lượt của chính sách đang được cập nhật." (nối sang mạch 4)
- **Dựng dần:** không (danh sách đọc một lần; TB17 không áp vì ví dụ tay đã ở `3-04`).
- **1 phút:** Mỗi lượt: tính GAE lùi, một bước cho actor theo $\widehat A_t$, một bước cho critic về $\widehat A_t+\hat v_{\mathrm{old}}$.
- **Mới:** thuật toán (một đối tượng).
- **Nguồn số:** không số.
- **Hình:** không (≈ 8 dòng; trang riêng theo quy định giả mã).
- **Ghi chú nguồn:** Thuật toán 10.9 và 10.16, đoạn không đánh số sau Thuật toán 10.16 mô tả actor–critic với GAE (quyết định N7 của điều phối viên); Thuật toán 10.6.
- **Diễn giả:** $\lambda=0$ cho bản cập nhật theo lượt của actor–critic một bước (Thuật toán 10.9 cập nhật sau từng bước); $\lambda=1$ cho REINFORCE có đường cơ sở (Thuật toán 10.6). Hệ số đã dừng gradient: gradient của actor không đi vào $w$. Dữ liệu theo chính sách: mỗi lượt chỉ dùng một lần, giới hạn mà mạch 4 xử lý.
- **Phút:** 2.

---

### Mạch 4. Hàm thay thế và miền tin cậy (`id="mach-4"`, 29 trang sau khi tách `4-07` thành `4-07` và `4-32`, 37,5 phút; kế hoạch theo đề xuất trình bày TRPO của tác giả, 2026-11-21)

**Trạng thái.** Đã dựng trên deck (biên tập viên, 2026-11-21); chỗ lệch so với các mục dưới đây ở §10, mục "Ghi chú khi dựng mạch 4 (2026-11-21)". Bản trước đề xuất TRPO ở mục "Lịch sử: mạch 4 trước đề xuất TRPO (2026-11-21)" cuối tệp. Chữ trong ngoặc kép là chữ dự kiến lên trang (`no-ai-slop` chế độ Edit); người dựng được rút, không thêm ý. Số lấy từ ghi chú mới (`materials/lec-10/lecture-note.md` §4–§5, bản đang rà) và được tính lại trong `/tmp/claude-1000/-data-tqlong-lectures/678a7f48-9d80-46cf-a421-67398857f913/scratchpad/m4-plan/kiem.py`. Số hiệu khối theo `doi-so-ghi-chu-2026-11-21.md`.

**Căn cứ.** Đề xuất `de-xuat-trinh-bay-trpo-2026-11-21.md` (20 trang, năm cụm A–E, 14 hình); quyết định của tác giả: theo đề xuất, các trang ý tưởng chứng minh gom thành cụm "Cơ sở lý thuyết" ngay sau trang (15) "Vì sao giới hạn KL kiểm soát sai số" và trước cụm D; tinh chỉnh TB27 (hiện tượng → câu hỏi → trực giác → mô hình hóa → chứng minh → thuật toán) và TB31 (mọi đại lượng một bước thuật toán tính ra có công thức trong bước đó) của `NGUYEN-TAC-HOC-PHAN.md` §3a.F.

**Quyết định của điều phối viên (2026-11-21, sau kế hoạch).** Chấp nhận kế hoạch 28 trang và các chỗ lệch có lý do (§10). (1) Câu chuyện mạch 4 dưới đây được duyệt, đã thay mục mạch 4 của `cau-chuyen-deck-2026-11-21.md` (bản cũ ở mục lịch sử cuối tệp đó). (2) H13 `vong-trpo.svg` đặt ở `5-09`, vòng tìm kiếm lùi màu đỏ, đúng chỗ nêu chi phí của TRPO. (3) Năm bước của H1 không lên `p.strand-keys` (các mạch khác không có dòng này); chỉ giữ trong storyboard (cấu trúc cụm A–E). (4) `1-07` mục tiêu 3 giữ nguyên. (5) `6-13` giữ bốn hàng. (6) `lec-10-topic-25` giữ cho §4.3 mới; mã DPO lấy mã của Bài 13 khi dựng bài đó. (7) Đề xuất 9 không có trang riêng: câu hỏi nhanh `4-16` và hình luồng `4-27` đủ; lời giải `4-16` nêu rõ hai cột "đã hiệu chỉnh: phân phối hành động" và "chưa hiệu chỉnh: phân bố trạng thái". Thêm: `4-11` dùng "lấy mẫu quan trọng (importance sampling)" như Bài 06 và ghi chú; ghi chú diễn giả `4-08` có câu "gradient tự nhiên chọn hướng theo khoảng cách KL, không bảo đảm $J$ cao hơn trên mọi bài toán". Ghi chú đã chốt (văn xuôi 32 493 từ): §4.1 dòng 953, §4.2 dòng 1088, §4.3 "Sai số dự báo theo độ dài bước" dòng 1168, §4.4 dòng 1216, §4.5 dòng 1267, §4.6 dòng 1292, §5.1 dòng 1572, §5.2 dòng 1725; số khối và dòng nguồn của mạch 4 đã đối chiếu lại (§10).

**Câu chuyện mạch 4 (đã duyệt 2026-11-21; thay mục "Mạch 4" của `cau-chuyen-deck-2026-11-21.md` §2).**

1. Hiện tượng và câu hỏi: mỗi lượt của mạch trước chỉ cho một bước, và bước dài theo ước lượng của một lượt cũ làm $J$ giảm. Trên đoạn từ $\pi$ tới ứng viên $\tilde\pi=(0{,}9;\,0{,}5)$, $J(\pi_t)=1{,}4+0{,}095t-0{,}18t^2$: hướng này làm $J$ tăng lúc đầu, nhưng $J$ về $1{,}4$ tại $t=\tfrac{19}{36}$ và xuống $1{,}315$ tại $t=1$. Biết hướng làm $J$ tăng chưa cho biết đi bao xa. $\tilde\pi$ đổi cả hành động tại $s_B$ lẫn tần suất tới $s_B$ (trong $100$ lượt, từ $50$ lên $90$), và $J(\tilde\pi)$ chỉ biết sau khi chạy nó. Đánh giá chính sách mới từ lượt của $\pi$ thế nào, và tin được đến đâu?
2. Mô hình: mức thay đổi của $J$ là lợi thế của $\pi$ cộng theo tần suất gặp trạng thái dưới chính sách mới, $1\cdot0{,}32+0{,}81\cdot(-0{,}5)=-0{,}085$ (bổ đề chênh lệch hiệu năng). Hàm thay thế thay tần suất mới bằng tần suất cũ và hiệu chỉnh hành động bằng tỉ số chính sách, nên tính được từ lượt cũ.
3. Kết quả trên ví dụ: hàm thay thế dự báo $+0{,}095$ trong khi $J$ giảm $0{,}085$, toàn bộ sai số nằm ở $s_B$. Trên đoạn từ $\pi$ tới $\tilde\pi$, dự báo tăng như $0{,}095t$ còn sai số tăng như $0{,}18t^2$; hàm thay thế tiếp xúc $J$ tại $\pi$ nên là mô hình cục bộ.
4. Giới hạn thay đổi: cùng bước tham số đổi hành vi rất khác nhau ($\Delta p=0{,}2311$ so với $0{,}0042$), nên khoảng cách đo trên phân phối hành động bằng KL. Bài toán miền tin cậy tối đa hàm thay thế với KL trung bình $\le\kappa$; trên đoạn, $\kappa=0{,}01$ giữ $t\le0{,}515$, nơi $\Delta J>0$. KL nhỏ kéo theo TV nhỏ, phân bố chiếm dụng ít đổi và sai số nhỏ (cơ sở lý thuyết; với $\tilde\pi$ cận là $-4{,}18$, cận dương chỉ với bước rất ngắn).
5. Giải và thuật toán: bậc một cho hàm thay thế, bậc hai cho KL, miền tin cậy thành một elip của ma trận Fisher; bước tối ưu đi theo gradient tự nhiên $F^{-1}g=(8;\,30)$, dồn về $\theta_B$, và một bước TRPO đưa $J$ từ $1{,}4$ lên $1{,}807$. Điều còn thiếu: mỗi bộ đệm chỉ cho một bước, với gradient liên hợp và tìm kiếm lùi.

**Thứ tự (28 trang, năm cụm và cụm lý thuyết).**

| Cụm | Trang (theo thứ tự) | Trang đề xuất | Phút |
|---|---|---|---|
| — | `4-00` | — | 0,5 |
| A. Động cơ | `4-01` → `4-27` | 1, 2 → `4-01`; 3 → `4-27` | 3,5 |
| B. Hàm thay thế | `4-13` → `4-02` → `4-03` → `4-11` | 4, 5, 6 → `4-02` (cần `4-13` trước); 7 → `4-03`; 8 → `4-11` | 5,5 |
| C. Từ hàm thay thế đến miền tin cậy | `4-16` → `4-04` → `4-10` → `4-17` → `4-28` → `4-12` → `4-07` → `4-32` → `4-21` | 9, 10 → `4-16`; 11 → `4-04`, `4-10`, `4-17`; 12 → `4-28`; 13 → `4-12`; 14 → `4-07`; 15 → `4-21` | 11 |
| Cơ sở lý thuyết | `4-14` → `4-20` → `4-24` → `4-06` → `4-19` → `4-29` (thứ tự mắt xích của H10, sau cổng storyboard) | ý tưởng chứng minh bổ đề; Pinsker; TV và phân bố chiếm dụng; định lý, ý tưởng chứng minh và chứng minh hệ quả KL của `4-21`; ví dụ trên chuỗi; hệ quả đơn điệu | 8 |
| D. Giải bài toán TRPO | `4-22` → `4-30` → `4-08` | 16 → `4-22`; 17 → `4-30`; 18 → `4-08` | 4 |
| E. Từ lý thuyết đến thuật toán | `4-25` → `4-09` → `4-26` → `4-31` | 19 → `4-25`, `4-09`, `4-26` (sơ đồ H13 ở `5-09`, quyết định 2); 20 → `4-31` (phần "giải quyết gì"), `5-09` (phần "còn khó khăn gì") | 5 |
| **Tổng** | **29 trang** (`4-32` tách từ `4-07`, lượt sửa sau năm vai) | | **37,5** |

**Đối chiếu mã (cũ 27 trang → mới 28 trang).**

| Mã | Quyết định | Ghi chú |
|---|---|---|
| `4-00`, `4-13`, `4-11`, `4-14`, `4-19`, `4-20`, `4-26` | giữ | đổi chỗ (`4-14`, `4-19`, `4-20` vào cụm lý thuyết) hoặc chỉ sửa dòng nguồn, một dòng (`4-13` "Dạng khác:", `4-20` "Ý nghĩa:"), một cụm từ (`4-11`); `4-26` giữ nguyên chữ (vừa sửa theo góp ý #1) |
| `4-01`, `4-02`, `4-03`, `4-16`, `4-04`, `4-10`, `4-17`, `4-12`, `4-07`, `4-21`, `4-24`, `4-06`, `4-22`, `4-08`, `4-25`, `4-09` | sửa | `4-25`: dòng "Nhắc lại:" và đường tính của $\Delta\mathcal L$; `4-09`: bước 1 lưu cả phân phối cũ (sau cổng storyboard); các trang khác | nội dung theo đề xuất; `4-21` thành trang (15), `4-24` thành trang bổ đề dịch chuyển |
| `4-15` | bỏ (gộp vào `4-02`) | phép cộng theo bước thời gian đứng trước bổ đề (TB27); dòng bỏ "cùng $\mu_0$" chuyển sang `4-14` |
| `4-05` | bỏ (gộp vào `4-04`) | đoạn thẳng tính thẳng từ số của `4-16`; công thức tổng quát của sai số lên `4-16`; dạng $2{,}7\Delta p_A\Delta p_B$ xuống ghi chú diễn giả `4-04` |
| `4-23` | bỏ | khai triển $J$ ba dòng là phép kiểm, chuyển xuống ghi chú diễn giả `4-04` (TB4) |
| `4-18` | bỏ (gộp vào `4-06`) | đẳng thức sai số đã ở `4-16`, bổ đề dịch chuyển có trang riêng `4-24`, nên chứng minh định lý còn một dòng "Chứng minh." (TB28 dạng a); câu hỏi về $1/(1-\gamma)^2$ xuống ghi chú diễn giả `4-24` |
| `4-27` | thêm | luồng 100 lượt (đề xuất 3, H4) |
| `4-28` | thêm | sigmoid (đề xuất 12, H8) |
| `4-29` | thêm (tách từ `4-21`) | hệ quả cải thiện đơn điệu, khép cụm lý thuyết; bỏ ngoại lệ "hai khối có số hiệu" của `4-21` cũ (TB6) |
| `4-30` | thêm | tròn và elip (đề xuất 17, H11) |
| `4-31` | thêm | trạm dừng cuối mạch, ba trực giác (đề xuất 20, H14) |

**Mã trang trong mục "Diễn giả".** Mã như `4-16` trong các mục dưới đây chỉ để người dựng tra; ghi chú diễn giả trên deck gọi trang bằng nội dung ("bảng đóng góp từng trạng thái"), không ghi mã, không câu điều hướng (VP8; lượt sửa G3).

**Trạm dừng (TB5).** `4-16` (dự báo và thực tế), `4-17` (mô hình cục bộ), `4-07` (bài toán trung tâm của mạch, trang cần nhớ), `4-19` (cận trên chuỗi), `4-08` (cụm D: kết quả $\Delta^*$, ý nghĩa hai quyết định, điều còn thiếu; sau cổng storyboard), `4-31` (cuối mạch). **Câu hỏi nhanh (TB22).** `4-16` (vì sao tỉ số chính sách không biến hàm thay thế thành mức thay đổi thật, câu hỏi kiểm tra của đề xuất), `4-10` (bước $t=0{,}25$). Câu hỏi "10.000 bước" của đề xuất ở ghi chú diễn giả `4-01`; câu hỏi "vì sao TRPO ưu tiên $\theta_B$" ở ghi chú diễn giả `4-08`; câu hỏi "vì sao không giảm bước học" ở ghi chú diễn giả `4-28`. **Trang ý tưởng chứng minh.** Chỉ `4-14` (Đ8, Đ9), trong cụm lý thuyết; các kết quả khác dùng dòng "Chứng minh." một dòng (TB28 dạng a).

**Bảng số dùng chung của mạch** (kiểm trong `kiem.py`):

| Đại lượng | Giá trị | Trang đầu tiên có đường tính |
|---|---|---|
| $\pi$, $\tilde\pi$: $(p_A;\,p_B)$ | $(\tfrac12;\,\tfrac23)$, $(\sigma(\log9);\,\sigma(0))=(0{,}9;\,0{,}5)$ | `1-09`, `4-01` |
| $J(\pi)$, $J(\tilde\pi)$ | $1{,}4$; $2{,}7\cdot0{,}45+0{,}1=1{,}315$ | `1-10`, `4-01` |
| luồng 100 lượt, $\pi$ | tới $s_B$ $50$ ($33\tfrac13$ nhận $3$, $16\tfrac23$ nhận $0$, làm tròn $33$, $17$); $50$ nhận $1$ | `4-27` |
| luồng 100 lượt, $\tilde\pi$ | tới $s_B$ $90$ ($45$ nhận $3$, $45$ nhận $0$); $10$ nhận $1$ | `4-27` |
| $A_\pi(s,\tilde\pi)$ | $(0{,}32;\,-0{,}5)$ | `4-13` |
| $\eta_{\tilde\pi}$, $\eta_\pi$ | $(1;\,0{,}81)$, $(1;\,0{,}45)$ | `4-02`, `4-03` |
| $\Delta\mathcal L$, $\Delta J$, sai số với $\tilde\pi$ | $0{,}095$; $-0{,}085$; $-0{,}18$ | `4-16` |
| đoạn $\pi_t$ | $J(\pi_t)=1{,}4+0{,}095t-0{,}18t^2$: $1{,}4125$ ($t=0{,}25$), $1{,}4025$ ($t=0{,}5$), $1{,}4$ ($t=\tfrac{19}{36}$), $1{,}315$ ($t=1$) | `4-01` |
| dự báo trên đoạn | $\Delta\mathcal L=0{,}095t$, sai số $0{,}18t^2$; $t=0{,}25$: $0{,}02375$, $0{,}01125$; $t=0{,}5$: $0{,}0475$, $0{,}045$ | `4-04`, `4-10` |
| sigmoid | $\sigma(1)-\sigma(0)=0{,}2311$; $\sigma(6)-\sigma(5)=0{,}0042$; tỉ số $\approx55$ | `4-28` |
| $D_{\mathrm{TV}}$, $D_{\mathrm{KL}}(\pi\Vert\cdot)$ tại $s_A$ | $(0{,}6;\,0{,}4)$: $0{,}1$, $0{,}0204$; $(0{,}9;\,0{,}1)$: $0{,}4$, $\log\tfrac53=0{,}511$ | `4-12` |
| $\nu^\pi$; $D_{\mathrm{KL}}(s_B)$ với $\tilde\pi$; $\bar D_{\mathrm{KL}}(\tilde\pi)$ | $(0{,}1;\,0{,}045)$; $0{,}0566$; $0{,}0536$ | `4-07` |
| miền $\kappa=0{,}01$ trên đoạn | $t\le0{,}515$; tại biên $\Delta\mathcal L\approx0{,}049$, $\Delta J\approx0{,}0012$ | `4-07` |
| phạt dạng KL với $\tilde\pi$ | $\chi=0{,}5$, $90\sqrt{0{,}0536/2}\approx14{,}7$ | `4-21` |
| dịch chuyển với $\tilde\pi$ | $\lVert\nu^{\tilde\pi}-\nu^\pi\rVert_1=0{,}1\cdot\lvert0{,}81-0{,}45\rvert=0{,}036\le18\cdot0{,}0475=0{,}855$ (hiệu phân bố chiếm dụng; khác sai số $0{,}036$ của bước $\pi'$ trong ghi chú) | `4-24` |
| cận dạng TV | $0{,}095-90\cdot0{,}0475=-4{,}18$; bước chỉ đổi $p_B$ thêm $d$: $1{,}35d-24{,}3d^2>0$ khi $d<0{,}056$ | `4-06`, `4-19` |
| hàm chặn dưới | $\bar\chi=2$, $C=360$ | `4-29` |
| Fisher, gradient tự nhiên | $F=\operatorname{diag}(0{,}025;\,0{,}01)$; $F^{-1}g=(8;\,30)$; $g^\top F^{-1}g=10{,}6$; tỉ trọng $40\%/60\%$ và $21\%/79\%$ | `4-22`, `4-08` |
| một bước TRPO | $\Delta^*=(0{,}35;\,1{,}30)$, $p=(0{,}586;\,0{,}880)$, $\bar D_{\mathrm{KL}}=0{,}0085$, $J=1{,}807$ | `4-25` |

**Rủi ro số (TB15).** Trên chuỗi, bước theo $g$ co về cùng bán kính KL bậc hai cho $J\approx1{,}835$, lớn hơn $1{,}807$ của bước gradient tự nhiên (mức tăng bậc một $0{,}422$ so với $0{,}460$). Không trang nào được so $J$ của hai bước này hay viết rằng gradient tự nhiên cho $J$ lớn hơn; `4-30`, `4-08` chỉ nói về hướng và tỉ trọng.

#### `L10-4-00` · Hàm thay thế và miền tin cậy (trang tiêu đề mạch; điểm vào mạch 4)

- **Quyết định:** giữ (mặt trang và hình giữ; ghi chú diễn giả sửa đầu ra).
- **Mục đích:** mở mạch bằng khối "Cập nhật actor" tô tím trên sơ đồ neo.
- **Mặt trang:** "4."; `h2` "Hàm thay thế và miền tin cậy"; `p.strand-lead` "Chính sách mới được đánh giá từ dữ liệu của chính sách cũ với sai số nhỏ khi hai chính sách gần nhau." (23 âm tiết; giữ, chỉ dùng thuật ngữ đã có, Đ11).
- **Hình:** `so-do-neo-m4-vao.svg` (giữ). **Dựng dần:** không.
- **Diễn giả:** "Mạch 2 và 3 cho hệ số ít phương sai, nhưng mọi ước lượng cần lượt của chính sách đang cập nhật, nên mỗi lượt chỉ cho một bước nhỏ. Mạch này đánh giá chính sách mới bằng lượt của chính sách cũ, giới hạn khoảng cách giữa hai chính sách bằng KL, rồi tìm bước tốt nhất trong giới hạn đó. Đầu ra là bài toán miền tin cậy, cơ sở lý thuyết của nó và thuật toán TRPO."
- **Nguồn:** §4 (đoạn mở). **Nối vào:** `3-10` (mỗi lượt một bước). **Nối ra:** `4-01`.
- **Phút:** 0,5.

#### `L10-4-01` · Đánh giá chính sách mới trước khi chạy (sửa; cụm A; đề xuất 1 và 2; sửa sau cổng storyboard)

- **Quyết định:** sửa. Gộp đề xuất 1 ("biết hướng đi lên nhưng chưa biết đi bao xa") và đề xuất 2 vào trang bài toán. Sau cổng storyboard (mục nghiêm trọng 1): hiện tượng lấy từ chính đoạn thẳng $\pi\to\tilde\pi$ của Ví dụ 10.12, không từ `1-05`. Ở `1-05`, $\widehat g=(-0{,}5;\,0)$ ngược dấu gradient đúng, nên $J$ giảm vì sai hướng, không vì bước quá dài; trang chỉ nhắc `1-05` bằng câu "bước dài theo ước lượng của một lượt cũ làm $J$ giảm". Trên đoạn, độ dốc ban đầu $0{,}095>0$: hướng làm $J$ tăng, nhưng đi quá $t=\tfrac{19}{36}$ thì $J$ thấp hơn $1{,}4$. Trang ghi "hướng làm $J$ tăng", không ghi "gradient" ($\tilde\pi$ không nằm trên hướng gradient). Đường $\Delta\mathcal L$ chưa lên trang này; `4-04` thêm nó. Hình thanh `chuoi-ti-le-toi-sB*` và hình nhỏ `buoc-dai-mot-luot-nho.svg` không dùng.
- **Mục đích:** cho thấy hướng làm $J$ tăng chưa cho biết đi bao xa, và nêu bài toán của mạch: đánh giá chính sách mới từ lượt của chính sách cũ trước khi chạy nó.
- **Câu:** 1. **Nhãn:** "Nhắc lại:", "Câu hỏi:", hộp.
- **Mặt trang:**
  - "Mỗi lượt của mạch trước chỉ cho một bước. Nhắc lại: bước dài theo ước lượng của một lượt cũ làm $J$ giảm."
  - "Xét ứng viên $\tilde\theta=(\log9;\,0)$: $(\tilde p_A;\,\tilde p_B)=(\sigma(\log9);\,\sigma(0))=(0{,}9;\,0{,}5)$. Đoạn thẳng $\pi_t=(1-t)\pi+t\tilde\pi$, $t\in[0,1]$, có $p_A=\tfrac12+0{,}4t$, $p_B=\tfrac23-\tfrac t6$."
  - "Thế vào $J=2{,}7p_Ap_B+1-p_A$:" $$J(\pi_t)=1{,}4+0{,}095t-0{,}18t^2 .$$
  - Hộp: "Độ dốc tại $t=0$ là $0{,}095>0$, nên hướng tới $\tilde\pi$ làm $J$ tăng. $J$ lên $1{,}4125$ tại $t=0{,}25$, còn $1{,}4025$ tại $t=0{,}5$, về $1{,}4$ tại $t=\tfrac{19}{36}\approx0{,}53$ và xuống $1{,}315$ tại $t=1$. Biết hướng làm $J$ tăng chưa cho biết đi bao xa."
  - Hộp "Câu hỏi: từ các lượt đã thu bằng $\pi$, đánh giá một chính sách trên đoạn này trước khi chạy nó thế nào?"
- **Hình:** `ham-thay-the-tiep-xuc-chi-J.svg` (mới, §4.5): cùng khung và tỉ lệ với `ham-thay-the-tiep-xuc*.svg`, chỉ có đường $J$ xanh nét liền và năm điểm. Nửa phải.
- **Dựng dần:** (0) dòng nối và nhắc lại; (1) dòng ứng viên, đoạn thẳng, công thức $J(\pi_t)$, hình; (2) hộp số; (3) câu hỏi.
- **1 phút:** Đi từ $\pi$ về phía $\tilde\pi$, $J$ tăng lúc đầu rồi giảm dưới $1{,}4$; hướng đúng chưa đủ, phải biết đi bao xa, và điều đó chỉ thấy sau khi chạy chính sách mới.
- **Mới:** chính sách ứng viên $\tilde\pi$ và đoạn $\pi_t$ (hai đối tượng, TB24).
- **Nguồn số:** $\sigma(\log9)=\tfrac9{10}$, $\sigma(0)=\tfrac12$; $J(\pi_t)=2{,}7(\tfrac12+0{,}4t)(\tfrac23-\tfrac t6)+\tfrac12-0{,}4t$ (khai triển trong ghi chú diễn giả: $2{,}7(\tfrac13+0{,}18\overline3\,t-0{,}0\overline6\,t^2)=0{,}9+0{,}495t-0{,}18t^2$); bốn giá trị $J$ lấy từ Ví dụ 10.12, "Kiểm tra lại" ($1{,}4125$; $1{,}4025$; $1{,}315$) và "Diễn giải" ($t=\tfrac{19}{36}$); mỗi giá trị kiểm được bằng công thức trên trang.
- **Diễn giả:** đề xuất hỏi lớp: đã thu $10\,000$ bước tương tác, dùng bộ dữ liệu này thế nào để cập nhật đủ lớn mà không quá mạo hiểm; câu trả lời của mạch là đánh giá ứng viên bằng chính bộ dữ liệu đó. $\tilde\pi$ được chọn để sai số của phép đánh giá hiện rõ; nó không nằm trên hướng gradient ($p_B$ giảm). $J$ lớn nhất khoảng $1{,}4125$ quanh $t\approx0{,}26$. $\tilde\theta$ hữu hạn nên $\tilde\pi$ dương trên mọi hành động.
- **Nguồn:** §4 (đoạn mở, "Câu hỏi."); §4.1 (Ví dụ 10.11, giá trị thật); §4.3 (Ví dụ 10.12, "Đoạn thẳng", "Diễn giải", "Kiểm tra lại").
- **Nối vào:** `4-00`, `3-10` (mỗi lượt chỉ cho một bước). **Nối ra:** `4-27` (dữ liệu của chính sách mới khác dữ liệu cũ ở đâu).
- **Phút:** 2.

#### `L10-4-27` · Đổi chính sách cũng làm đổi dữ liệu (thêm; cụm A; đề xuất 3, H4)

- **Quyết định:** thêm. Đề xuất xếp mức "rất cao": phân biệt phân phối hành động và phân bố trạng thái bằng hình luồng trước mọi công thức. Thay hình thanh `chuoi-ti-le-toi-sB*` của `4-01` cũ.
- **Mục đích:** cho thấy chính sách mới đổi hai thứ khác loại: hành động tại một trạng thái và tần suất gặp trạng thái.
- **Câu:** 1. **Nhãn:** "Kiểm tra lại:" không dùng; hộp.
- **Mặt trang:**
  - "Chạy $100$ lượt với mỗi chính sách. Số lượt kỳ vọng trên mỗi nhánh là $100$ nhân xác suất của nhánh, ví dụ $100\cdot\tfrac12\cdot\tfrac23=33\tfrac13$."
  - Hình luồng (trái hoặc giữa, khoảng 60% bề rộng).
  - Hai dòng: "Phân phối hành động tại $s_B$: xác suất chọn hành động 1 giảm từ $\tfrac23$ xuống $\tfrac12$." / "Phân bố trạng thái: số lượt tới $s_B$ tăng từ $50$ lên $90$."
  - Hộp: "Trong học có giám sát, tập dữ liệu cố định. Trong học tăng cường, chính sách mới đổi cả phân bố của các trạng thái mà tác tử sẽ gặp."
- **Hình:** `luong-100-luot-buoc0.svg` (chỉ $\pi$), `luong-100-luot.svg` (thêm $\tilde\pi$); mô tả ở §4.5.
- **Dựng dần:** (0) dòng mở, luồng của $\pi$; (1) luồng của $\tilde\pi$; (2) hai dòng; (3) hộp.
- **1 phút:** Với $\tilde\pi$, $90$ lượt tới $s_B$ thay cho $50$, và tại $s_B$ chỉ một nửa chọn hành động 1, nên $45$ lượt nhận $0$.
- **Mới:** phân biệt phân phối hành động và phân bố trạng thái (một ý, TB26: "phân bố trạng thái", "phân phối hành động").
- **Nguồn số:** $100\cdot p_A$, $100\cdot p_Ap_B$, $100\cdot p_A(1-p_B)$, $100(1-p_A)$ với $p$ của `4-01`; làm tròn $33\tfrac13\to33$, $16\tfrac23\to17$ ghi trên hình.
- **Diễn giả:** kiểm $J$ từ hình: $J(\tilde\pi)=\tfrac1{100}(45\cdot0{,}9\cdot3+10\cdot1)=1{,}315$, $J(\pi)=\tfrac1{100}(33\tfrac13\cdot2{,}7+50)=1{,}4$, khớp bảng `4-01`. Lượt của $\pi$ chỉ cho $50$ lần ghé $s_B$ trên $100$ lượt, nên dữ liệu cũ đánh giá thấp vai trò của $s_B$ dưới $\tilde\pi$.
- **Nguồn:** §4.1 (Ví dụ 10.11, "Luồng 100 lượt", "Diễn giải", "Kiểm tra lại"; hai gạch đầu dòng sau ví dụ; câu về học có giám sát).
- **Nối vào:** `4-01`. **Nối ra:** `4-13` (đổi hành động tại một trạng thái thay đổi lợi tức bao nhiêu).
- **Phút:** 1,5.

#### `L10-4-13` · Lợi thế của $\pi'$ so với $\pi$ tại một trạng thái (giữ, sửa dòng "Dạng khác:"; cụm B)

- **Quyết định:** giữ mặt trang như deck hiện tại, trừ dòng "Dạng khác:" thêm $A_\pi(s,\pi)=0$ (sau cổng storyboard: `4-04` dùng đẳng thức này). Lý do giữ: $A_\pi(s,\pi')$ là đại lượng cần trước khi viết ba thành phần (đề xuất 4); nó đo riêng thay đổi thứ nhất của `4-27`.
- **Mục đích:** đo tác động của việc đổi hành động tại một trạng thái, với tần suất giữ nguyên.
- **Câu:** 2. **Nhãn:** "Nhắc lại:", "Ký hiệu:", "Câu hỏi:", "Định nghĩa.", "Dạng khác:".
- **Mặt trang:** như deck: nhắc lại $q_\pi(s_A,\cdot)=(1{,}8;\,1)$, $q_\pi(s_B,\cdot)=(3;\,0)$, $v_\pi=(1{,}4;\,2)$; ký hiệu $\pi'$ và $\tilde\pi$; câu hỏi một bước theo $\pi'$ rồi theo $\pi$; định nghĩa $A_\pi(s,\pi')=\sum_a\pi'(a\mid s)q_\pi(s,a)-v_\pi(s)$; "Dạng khác: $A_\pi(s,\pi')=\sum_a\pi'(a\mid s)A_\pi(s,a)$; với $\pi'=\pi$, $A_\pi(s,\pi)=0$."; hộp "$A_\pi(s_A,\tilde\pi)=0{,}9\cdot1{,}8+0{,}1\cdot1-1{,}4=0{,}32$; $A_\pi(s_B,\tilde\pi)=0{,}5\cdot3+0{,}5\cdot0-2=-0{,}5$."
- **Hình:** không. **Dựng dần:** (0) nhắc lại, ký hiệu, câu hỏi; (1) định nghĩa, dạng khác; (2) hộp số.
- **1 phút:** Đổi một bước sang $\tilde\pi$ có lợi tại $s_A$ ($+0{,}32$), có hại tại $s_B$ ($-0{,}5$).
- **Mới:** $A_\pi(s,\pi')$. **Nguồn số:** $q_\pi$, $v_\pi$ từ `1-10`, `1-11`, `2-06`; $\tilde p_s$ từ `4-01`; $A_\pi(s,\pi)=\sum_a\pi(a\mid s)A_\pi(s,a)=0$ (Mệnh đề 10.5(a), nhắc ở `2-06`).
- **Diễn giả:** như deck; thêm: "tại $s_B$, $\tilde\pi$ chọn hành động 1 ít hơn, như trên hình luồng, nên lợi thế âm".
- **Nguồn:** §4.1 (đoạn định nghĩa $A_\pi(s,\pi')$ sau Ví dụ 10.11 và hai gạch đầu dòng số); Hệ quả 10.20.
- **Nối vào:** `4-27`. **Nối ra:** `4-02` (cộng các lợi thế này theo tần suất gặp trạng thái).
- **Phút:** 1,5.

#### `L10-4-02` · Bổ đề chênh lệch hiệu năng (sửa; cụm B; đề xuất 4, 5, 6, H5)

- **Quyết định:** sửa, gộp `4-15`. Ba trang đề xuất 4 (ba thành phần), 5 (bổ đề), 6 (tô $\eta_{\pi'}$ chưa biết) thành một trang: trực quan trên chuỗi đứng trước bổ đề (TB27), hình ba thành phần gọi tên từng thừa số của công thức (TB12), mảnh cuối tô thừa số chưa biết. Ý tưởng chứng minh chuyển vào cụm lý thuyết (`4-14`). Bảng kiểm của `4-15` cũ thành dòng trực quan đầu trang.
- **Mục đích:** phát biểu mức thay đổi của $J$ theo ba thành phần và chỉ ra thành phần chưa biết.
- **Câu:** 2. **Nhãn:** "Bổ đề.", "Giả thiết:", "Ký hiệu:", "Kết luận:".
- **Mặt trang:**
  - "Trên chuỗi, cộng lợi thế của $\tilde\pi$ theo bước thời gian: bước $0$ ở $s_A$ có trọng số $1$, bước $1$ ở $s_B$ có trọng số $\gamma\tilde p_A=0{,}81$. Tổng $1\cdot0{,}32+0{,}81\cdot(-0{,}5)=-0{,}085$ đúng bằng $J(\tilde\pi)-J(\pi)$."
  - Khối: "**Bổ đề** (chênh lệch hiệu năng, performance difference lemma). Giả thiết: giả thiết chung cho $\pi$, $\pi'$ (cùng $P$, cùng $\mu_0$). Ký hiệu: số lần thăm có chiết khấu $\eta_{\pi'}(s)=\sum_{t\ge0}\gamma^t\Pr_{\pi'}(S_t=s,\,t<T)$. Kết luận:" $$J(\pi')-J(\pi)=\sum_s\eta_{\pi'}(s)\sum_a\pi'(a\mid s)\,A_\pi(s,a).$$
  - Hình ba thành phần dưới công thức, thẳng hàng với ba thừa số.
- **Hình:** `ba-thanh-phan-buoc0.svg` (ba khối xám), `ba-thanh-phan.svg` (khối $\eta_{\pi'}$ tím, nhãn "chưa biết khi chưa chạy $\pi'$"); mô tả ở §4.5.
- **Dựng dần:** (0) dòng trực quan; (1) khối bổ đề và hình `-buoc0`; (2) hình đủ (tô $\eta_{\pi'}$).
- **1 phút:** Mức thay đổi của $J$ là lợi thế của $\pi$ cộng theo tần suất mà chính sách mới gặp mỗi trạng thái; tần suất đó chưa biết khi chưa chạy chính sách mới.
- **Mới:** $\eta_{\pi'}$; bổ đề (hai đối tượng, TB24).
- **Nguồn số:** $0{,}32$, $-0{,}5$ từ `4-13`; $\gamma\tilde p_A=0{,}9\cdot0{,}9$; $J$ từ `4-01`. Dòng "Ở đây" (Đ6) nằm trong hình: $\eta_{\tilde\pi}=(1;\,0{,}81)$, $\tilde\pi(1\mid s)=(0{,}9;\,0{,}5)$, $A_\pi(s_A,\cdot)=(0{,}4;\,-0{,}4)$, $A_\pi(s_B,\cdot)=(1;\,-2)$.
- **Diễn giả:** $\eta$ không phải số lần thăm: lần thăm ở bước $t$ có trọng số $\gamma^t$. Ghi chú viết bổ đề theo phân bố chiếm dụng $\nu=(1-\gamma)\eta$ với thừa số $\tfrac1{1-\gamma}$. Lợi thế $A_\pi$ ước lượng được từ lượt cũ (mạch 2–3), $\pi'$ là của ứng viên; chỉ $\eta_{\pi'}$ cần lượt của chính sách mới, trong thiết lập không mô hình. Chứng minh ở cụm lý thuyết.
- **Nguồn:** §4.1 (đoạn cộng theo bước thời gian; Định nghĩa 10.18; Bổ đề 10.19 và đoạn sau, dạng $\eta$; đoạn cuối §4.1 về đại lượng chưa biết).
- **Nối vào:** `4-13`. **Nối ra:** `4-03` (thay thừa số chưa biết).
- **Phút:** 1,5.

#### `L10-4-03` · Hàm thay thế (sửa; cụm B; đề xuất 7)

- **Quyết định:** sửa. Thêm câu "thay đúng một đại lượng" và diễn giải của đề xuất; số $\eta_\pi$ chuyển lên đây (dòng "Ở đây", Đ6) để `4-16` dùng.
- **Mục đích:** định nghĩa hàm thay thế bằng cách thay đúng một thừa số của bổ đề.
- **Câu:** 2. **Nhãn:** "Định nghĩa.", "Ký hiệu:", "Ý nghĩa:".
- **Mặt trang:**
  - "Thay đúng một đại lượng: $\eta_{\pi'}$ bằng $\eta_\pi$. Phân phối hành động mới và lợi thế cũ giữ nguyên."
  - "**Định nghĩa.** Hàm thay thế (surrogate objective) của $\pi'$ quanh $\pi$ là" $$\mathcal L_\pi(\pi')=J(\pi)+\sum_s\eta_\pi(s)\,A_\pi(s,\pi').$$
  - "Ký hiệu: $\Delta J=J(\pi')-J(\pi)$, $\Delta\mathcal L=\mathcal L_\pi(\pi')-J(\pi)$."
  - Hộp: "Ý nghĩa: $\Delta\mathcal L$ là mức tăng của $J$ nếu tác tử vẫn gặp các trạng thái với tần suất như dưới $\pi$."
  - "Ở đây $\eta_\pi=(1;\,\gamma p_A)=(1;\,0{,}45)$."
- **Hình:** không (hình ba thành phần của `4-02` có thể hiện lại thu nhỏ với khối $\eta_\pi$ thay $\eta_{\pi'}$; không bắt buộc, người dựng chọn nếu trang còn chỗ). **Dựng dần:** (0) dòng thay; (1) định nghĩa, ký hiệu; (2) hộp, dòng "Ở đây".
- **1 phút:** Hàm thay thế là bổ đề với tần suất của chính sách cũ.
- **Mới:** hàm thay thế; $\Delta J$, $\Delta\mathcal L$.
- **Nguồn số:** $\gamma p_A=0{,}9\cdot0{,}5$.
- **Diễn giả:** như deck (dạng $\mathcal L_{\theta_{\mathrm{old}}}(\theta)$ của ghi chú); "tính được từ lượt của $\pi$" còn cần đổi kỳ vọng theo hành động của $\pi'$ sang hành động của $\pi$.
- **Nguồn:** §4.2 (đoạn mở, $\Delta\mathcal L$; Định nghĩa 10.21 dạng tổng; câu "Khi viết theo chính sách …").
- **Nối vào:** `4-02`. **Nối ra:** `4-11` (lượt cũ chỉ có hành động của $\pi$).
- **Phút:** 1,5.

#### `L10-4-11` · Tỉ số chính sách (giữ, sửa câu mở; cụm B; đề xuất 8)

- **Quyết định:** giữ bảng và định nghĩa; câu mở gọi tên phép lấy mẫu quan trọng (importance sampling) như Bài 06 (Định nghĩa 06.24) và ghi chú §4.2.
- **Mục đích:** tính $A_\pi(s,\pi')$ từ hành động của $\pi$.
- **Câu:** 2. **Nhãn:** "Định nghĩa.", "Dạng khác:".
- **Mặt trang:** câu mở "Lượt cũ chỉ chứa hành động do $\pi$ chọn, còn $A_\pi(s,\pi')$ lấy kỳ vọng theo $\pi'$. Phép lấy mẫu quan trọng (importance sampling) nhân lợi thế của mỗi hành động đã lấy mẫu với một tỉ số."; định nghĩa, dạng khác, bảng bốn hàng và dòng cộng như deck.
- **Hình:** không. **Dựng dần:** như deck.
- **1 phút:** Nhân lợi thế của mỗi hành động cũ với tỉ số xác suất mới trên cũ cho lại $A_\pi(s,\tilde\pi)$, không cần chạy $\tilde\pi$.
- **Mới:** tỉ số chính sách. **Nguồn số:** như deck; kết quả trùng `4-13`.
- **Diễn giả:** như deck; thêm mục tiêu mẫu trên bộ đệm $N$ mẫu, $\widehat{\mathcal L}(\theta)=\tfrac1N\sum_t\rho_t(\theta)\widehat A_t$, bằng một bội dương của $\Delta\mathcal L$ khi trạng thái lấy theo phân bố chiếm dụng chuẩn hóa; bộ đệm thực tế lấy trung bình đều (công thức này lên mặt trang ở `4-26` và `5-09`).
- **Nguồn:** §4.2 (đoạn lấy mẫu quan trọng; Định nghĩa 10.21, tỉ số; đoạn mục tiêu mẫu; kiểm sau Mệnh đề 10.22); Định nghĩa 06.24.
- **Nối vào:** `4-03`. **Nối ra:** `4-16` (tỉ số đã sửa hành động; dự báo có đúng không).
- **Phút:** 1.

#### `L10-4-16` · Hàm thay thế dự báo $J$ tăng $0{,}095$, còn $J$ giảm $0{,}085$ (sửa; cụm C; đề xuất 9, 10, H6; câu hỏi nhanh; trạm dừng)

- **Quyết định:** sửa. Bảng bảy cột thay bằng hình đóng góp từng trạng thái (H6), số và phép nhân ghi trên cột (TB10: hình và bảng nói cùng điều thì giữ một). Đẳng thức sai số chuyển lên đây từ `4-05` cũ (dạng tổng quát ngay sau ví dụ). Câu hỏi kiểm tra của đề xuất 9 thành câu hỏi nhanh (TB22); bảng "đã hiệu chỉnh / chưa hiệu chỉnh" của đề xuất 9 thành lời giải của câu hỏi, hai cột trên mặt trang (quyết định 7). Mật độ: đo ở 1600×900 khi dựng; nếu trang tràn, tách thành trang riêng "Tỉ số chính sách sửa phân phối hành động, không sửa phân bố trạng thái" (câu hỏi nhanh và bảng hai cột) ngay sau `4-11`, `4-16` giữ hình, đẳng thức và câu sai số (§7; +1 trang, +0,5 phút).
- **Mục đích:** cho thấy tỉ số chính sách không sửa được tần suất gặp trạng thái, và sai số nằm đúng ở đó.
- **Câu:** 3. **Nhãn:** "Câu hỏi:", "Lời giải:".
- **Mặt trang:**
  - Hộp "Câu hỏi: tỉ số chính sách đã hiệu chỉnh phân phối hành động. Vì sao $\Delta\mathcal L$ vẫn có thể khác $\Delta J$?"
  - Hình hai bảng cột (dự báo với $\eta_\pi$; thực tế với $\eta_{\tilde\pi}$).
  - "Trừ định nghĩa hàm thay thế khỏi bổ đề:" $$\Delta J-\Delta\mathcal L=\sum_s\bigl(\eta_{\pi'}(s)-\eta_\pi(s)\bigr)\,A_\pi(s,\pi').$$
  - Hộp "Lời giải:" gồm bảng hai cột rồi một câu (quyết định 7 của điều phối viên):

    | đã hiệu chỉnh | chưa hiệu chỉnh |
    |---|---|
    | phân phối hành động tại trạng thái đã gặp: tỉ số chính sách thay $\pi(a\mid s)$ bằng $\tilde\pi(a\mid s)$ | phân bố trạng thái: $\Delta\mathcal L$ vẫn dùng $\eta_\pi(s_B)=0{,}45$ thay cho $\eta_{\tilde\pi}(s_B)=0{,}81$ |

    "Với $\tilde\pi$, sai số $(0{,}81-0{,}45)\cdot(-0{,}5)=-0{,}18$ nằm ở $s_B$, nơi $\tilde\pi$ tới thường hơn và kém $\pi$."
- **Hình:** `dong-gop-tung-trang-thai-buoc0.svg` (chỉ bảng dự báo), `dong-gop-tung-trang-thai.svg` (thêm bảng thực tế và dấu ngoặc đỏ "$-0{,}18$ tại $s_B$"); mô tả ở §4.5. Nửa phải.
- **Dựng dần:** (0) câu hỏi, hình `-buoc0`; (1) hình đủ; (2) đẳng thức; (3) lời giải.
- **1 phút:** Dùng tần suất cũ, hàm thay thế dự báo tăng $0{,}095$; thực tế giảm $0{,}085$, vì $\tilde\pi$ tới $s_B$ thường hơn.
- **Mới:** đẳng thức sai số (một phép biến đổi).
- **Nguồn số:** $A_\pi(s,\tilde\pi)$ từ `4-13`; $\eta_\pi$ từ `4-03`; $\eta_{\tilde\pi}$ từ `4-02`; tích trên từng cột: $1\cdot0{,}32$, $0{,}45\cdot(-0{,}5)=-0{,}225$, $0{,}81\cdot(-0{,}5)=-0{,}405$.
- **Diễn giả:** đề xuất: "nếu sinh viên trả lời được câu này, họ đã hiểu phần cốt lõi dẫn tới TRPO và PPO". Thành phần thứ ba trên bộ đệm, lợi thế, được ước lượng bằng critic hoặc GAE.
- **Nguồn:** §4.2 (bảng ba thành phần; "Câu hỏi."); §4.3 (bảng đóng góp; đẳng thức sai số và đoạn sau).
- **Nối vào:** `4-11`. **Nối ra:** `4-04` (sai số phụ thuộc thế nào vào độ dài bước).
- **Phút:** 1,5.

#### `L10-4-04` · Hàm thay thế trên đoạn thẳng từ $\pi$ tới $\tilde\pi$ (sửa; cụm C; đề xuất 11, H7 phần đồ thị)

- **Quyết định:** sửa, gộp `4-05` và `4-23`. Sau cổng storyboard: đoạn $\pi_t$ và $J(\pi_t)$ đã lên `4-01`; trang này nhắc lại đoạn thẳng và chỉ thêm đường $\Delta\mathcal L$. Đường tính chỉ dùng số của `4-16`: $A_\pi(s,\cdot)$ tuyến tính theo phân phối hành động và $A_\pi(s,\pi)=0$ (`4-13`), nên $A_\pi(s,\pi_t)=t\,A_\pi(s,\tilde\pi)$. Cùng kết quả với Ví dụ 10.12. Vùng KL của H7 chưa lên trang này vì KL chưa định nghĩa (TB11); vùng đó ở `4-07`.
- **Mục đích:** cho thấy dự báo là phần bậc nhất của $\Delta J$, còn sai số là phần bậc hai theo độ dài bước.
- **Câu:** 3. **Nhãn:** "Nhắc lại:", hộp.
- **Mặt trang:**
  - "Nhắc lại: trên đoạn $\pi_t$, $\Delta J=J(\pi_t)-1{,}4=0{,}095t-0{,}18t^2$."
  - "$A_\pi(s,\cdot)$ tuyến tính theo phân phối hành động và $A_\pi(s,\pi)=0$, nên $A_\pi(s,\pi_t)=t\,A_\pi(s,\tilde\pi)=(0{,}32t;\,-0{,}5t)$."
  - "$\Delta\mathcal L=1\cdot0{,}32t+0{,}45\cdot(-0{,}5t)=0{,}095t$. Sai số $\Delta J-\Delta\mathcal L=-0{,}18t^2=\bigl(\eta_{\pi_t}(s_B)-\eta_\pi(s_B)\bigr)A_\pi(s_B,\pi_t)=0{,}36t\cdot(-0{,}5t)$, với $\eta_{\pi_t}(s_B)=\gamma p_A=0{,}45+0{,}36t$."
  - Hộp: "Hai đường tiếp xúc tại $t=0$ và tách nhau theo $t^2$. $\Delta J$ lớn nhất, $0{,}0125$, tại $t\approx0{,}26$, và bằng $0$ tại $t=\tfrac{19}{36}\approx0{,}53$."
- **Hình:** `ham-thay-the-tiep-xuc-chi-J.svg` (đường $\Delta J$ của `4-01`) → `ham-thay-the-tiep-xuc-buoc2.svg` (thêm đường $\Delta\mathcal L$) → `ham-thay-the-tiep-xuc.svg` (điểm $t=1$). `-buoc0`, `-buoc1` không dùng. Nửa phải.
- **Dựng dần:** (0) nhắc lại, hình đường $\Delta J$; (1) dòng $A_\pi(s,\pi_t)$, $\Delta\mathcal L$, hình thêm đường cam; (2) dòng sai số; (3) điểm $t=1$ và hộp.
- **1 phút:** Trên đoạn tới $\tilde\pi$, dự báo là tiếp tuyến của $\Delta J$; bước ngắn cho hai số gần nhau, $t=1$ cho hai số trái dấu.
- **Mới:** không (đoạn $\pi_t$ ở `4-01`; dùng $\Delta\mathcal L$ của `4-03`).
- **Nguồn số:** $J(\pi_t)$ từ `4-01`; $0{,}32$, $-0{,}5$, $0{,}45$ từ `4-16`; $0{,}9\cdot0{,}4t=0{,}36t$; đỉnh $t^*=0{,}095/0{,}36$, $\Delta J(t^*)=0{,}095^2/0{,}72$; nghiệm $0{,}095/0{,}18=\tfrac{19}{36}$.
- **Diễn giả:** cách của ghi chú: với mọi $\pi'$, $\Delta\mathcal L=0{,}8\Delta p_A+1{,}35\Delta p_B$ và $\Delta J$ thêm $2{,}7\Delta p_A\Delta p_B$, đúng phần bậc hai của khai triển $J=2{,}7p_Ap_B+1-p_A$ (nội dung của `4-05`, `4-23` cũ). Trên chuỗi, bước chỉ đổi $p_A$ hoặc chỉ đổi $p_B$ có sai số $0$.
- **Nguồn:** §4.3 (Ví dụ 10.12: "Hai mức thay đổi", "Đoạn thẳng", "Diễn giải").
- **Nối vào:** `4-16`. **Nối ra:** `4-10`.
- **Phút:** 1.

#### `L10-4-10` · Câu hỏi nhanh: độ dài bước trên đoạn thẳng (sửa; cụm C; đề xuất 11, bảng H7; TB22)

- **Quyết định:** sửa. Bảng độ dài bước của đề xuất thành đề của câu hỏi nhanh: hàng $t=0{,}5$ và $t=1$ cho sẵn; ở hàng $t=0{,}25$, ô $\Delta J=0{,}0125$ cho sẵn (đã có ở `4-01`), ô $\Delta\mathcal L$ và sai số để "?" (TB16: ô đang tính được đánh dấu).
- **Mục đích:** sinh viên tự tính một hàng và đọc ra quy luật bình phương của sai số.
- **Câu:** 3. **Nhãn:** "Câu hỏi:", "Lời giải:".
- **Mặt trang:**

  | $t$ | $(p_A;\,p_B)$ | $\Delta\mathcal L=0{,}095t$ | $\Delta J=0{,}095t-0{,}18t^2$ | sai số $0{,}18t^2$ |
  |---|---|---|---|---|
  | $0{,}25$ | $(0{,}6;\,0{,}625)$ | ? | $0{,}0125$ | ? |
  | $0{,}5$ | $(0{,}7;\,\tfrac7{12})$ | $0{,}0475$ | $0{,}0025$ | $0{,}045$ |
  | $1$ | $(0{,}9;\,0{,}5)$ | $0{,}095$ | $-0{,}085$ | $0{,}18$ |
  - "Câu hỏi: điền hàng $t=0{,}25$. Dự báo và thực tế có cùng dấu không? Sai số nhỏ hơn ở $t=1$ bao nhiêu lần?"
  - "Lời giải: $\Delta\mathcal L=0{,}02375$, sai số $0{,}18\cdot0{,}0625=0{,}01125$, và $0{,}02375-0{,}01125=0{,}0125=\Delta J>0$: cùng dấu. Sai số nhỏ hơn $16$ lần, bằng $(1/0{,}25)^2$."
- **Hình:** `ham-thay-the-tiep-xuc-cau-hoi.svg`, `ham-thay-the-tiep-xuc-loi-giai.svg` (sửa nhãn "$0{,}024$" thành "$0{,}02375$" cho khớp bảng). Nửa phải.
- **Dựng dần:** (0) bảng, câu hỏi, hình câu hỏi; (1) lời giải, hình lời giải.
- **1 phút:** Nhân đôi độ dài bước làm sai số tăng bốn lần; ở $t=0{,}25$ dự báo và thực tế cùng dấu.
- **Mới:** không. **Nguồn số:** hai công thức ở đầu cột (từ `4-04`); $(p_A;\,p_B)$ theo đoạn của `4-01`.
- **Diễn giả:** "Gợi ý: thế $t=0{,}25$ vào hai công thức ở đầu cột." Kiểm trực tiếp $J(0{,}6;\,0{,}625)=2{,}7\cdot0{,}375+0{,}4=1{,}4125$. Năng lực kiểm tra: đọc sai số bậc hai theo độ dài bước.
- **Nguồn:** §4.3 (Ví dụ 10.12, bảng theo độ dài bước, "Kiểm tra lại").
- **Nối vào:** `4-04`. **Nối ra:** `4-17` (vì sao dự báo đúng đến bậc một).
- **Phút:** 1,5.

#### `L10-4-17` · Hàm thay thế tiếp xúc $J$ tại chính sách cũ (sửa, đổi chỗ; cụm C; trạm dừng)

- **Quyết định:** sửa, chuyển ra sau câu hỏi nhanh (đề xuất §6 đặt kết quả tiếp xúc ở đầu phần "từ mô hình cục bộ đến thước đo hành vi"). Dòng số trên chuỗi đổi đường tính vì `4-05` bỏ; hộp "Ý nghĩa:" nêu kết luận của cụm và nhu cầu thước đo khoảng cách.
- **Mục đích:** phát biểu vì sao hàm thay thế chỉ là mô hình cục bộ và nêu nhu cầu giới hạn khoảng cách giữa hai chính sách.
- **Câu:** 3. **Nhãn:** "Mệnh đề.", "Chứng minh.", "Ý nghĩa:", "Lưu ý:".
- **Mặt trang:**
  - Khối mệnh đề và dòng "Chứng minh." như deck.
  - "Trên chuỗi: $\nabla\mathcal L=\bigl(\eta_\pi(s)\,p_s(1-p_s)\,(A_\pi(s,1)-A_\pi(s,2))\bigr)_s=(1\cdot\tfrac14\cdot0{,}8;\,0{,}45\cdot\tfrac29\cdot3)=(0{,}2;\,0{,}3)=\nabla J$."
  - Hộp: "Ý nghĩa: hàm thay thế là mô hình cục bộ của $J$. Nó khớp đến bậc một tại $\pi$, còn sai số tăng theo bình phương độ dài bước, nên chính sách mới phải ở gần chính sách cũ."
  - "Lưu ý: với lợi thế ước lượng, $\mathcal L_\pi(\pi)=J(\pi)$ có thể sai; critic $(1{,}4;\,1)$ và $\lambda=0$ cho $-0{,}45$ thay cho $0$." (Đ2; mảnh cuối; nếu tràn khung thì xuống ghi chú diễn giả và ghi ở §7.)
- **Hình:** không. **Dựng dần:** (0) mệnh đề; (1) chứng minh, dòng chuỗi; (2) hộp; (3) lưu ý.
- **1 phút:** Tại chính sách cũ, hàm thay thế và $J$ cùng giá trị, cùng gradient; xa ra, sai số tăng bậc hai.
- **Mới:** tính tiếp xúc.
- **Nguồn số:** $\eta_\pi$ từ `4-03`; $A_\pi(s,\cdot)$ từ `2-06`; $p_s(1-p_s)=\tfrac14,\tfrac29$ và $\nabla J=(0{,}2;\,0{,}3)$ từ `1-11`; đạo hàm $\partial_{\theta_s}\sum_a\pi_\theta(a\mid s)A_\pi(s,a)=p_s(1-p_s)(A_\pi(s,1)-A_\pi(s,2))$ (ghi trên trang); $-0{,}5$, $-0{,}4$ từ `3-06`.
- **Diễn giả:** như deck; thêm câu nối: muốn giữ chính sách mới gần chính sách cũ thì cần đo khoảng cách giữa hai chính sách.
- **Nguồn:** §4.2 (Mệnh đề 10.22, chứng minh Bước 1–2; kiểm và hai phản ví dụ sau mệnh đề); §4.3 (đoạn cuối).
- **Nối vào:** `4-10`. **Nối ra:** `4-28` (khoảng cách đo trên tham số hay trên hành vi).
- **Phút:** 1.

#### `L10-4-28` · Cùng một bước tham số, hai mức thay đổi hành vi (thêm; cụm C; đề xuất 12, H8)

- **Quyết định:** thêm. Đề xuất xếp mức "cao": giải thích không gian tham số khác không gian chính sách trước KL. Ví dụ 10.13 của ghi chú mới đặt trước định nghĩa KL và chỉ tính $\Delta p$.
- **Mục đích:** cho thấy chuẩn của bước tham số không đo được mức thay đổi hành vi.
- **Câu:** 4. **Nhãn:** hộp.
- **Mặt trang:**
  - "Thuật toán cập nhật $\theta$, nhưng điều cần giữ gần là phân phối hành động."
  - "Một trạng thái, hai hành động, $p=\sigma(\theta)$. Bước $\Delta\theta=1$ từ hai điểm:"

    | bước | $p=\sigma(\theta)$ | $p'=\sigma(\theta+1)$ | $\Delta p$ |
    |---|---|---|---|
    | $0\to1$ | $0{,}5$ | $1/(1+e^{-1})=0{,}7311$ | $0{,}2311$ |
    | $5\to6$ | $0{,}99331$ | $0{,}99753$ | $0{,}0042$ |
  - Hộp: "Cùng $\Delta\theta=1$, xác suất đổi ở $\theta=0$ gấp khoảng $55$ lần ở $\theta=5$. Ràng buộc trên $\lVert\theta-\theta_{\mathrm{old}}\rVert_2$ vì vậy không đo mức thay đổi hành vi."
- **Hình:** `sigmoid-hai-buoc-buoc0.svg` (đường cong và bước $0\to1$), `sigmoid-hai-buoc.svg` (thêm bước $5\to6$); mô tả ở §4.5. Nửa phải.
- **Dựng dần:** (0) dòng mở, dữ kiện, hàng $0\to1$, hình `-buoc0`; (1) hàng $5\to6$, hình đủ; (2) hộp.
- **1 phút:** Cùng một bước trên $\theta$ đổi xác suất $0{,}23$ ở chỗ dốc và chỉ $0{,}004$ ở chỗ bão hòa.
- **Mới:** không (dùng hàm logistic của `1-09`); ý "khoảng cách đo trên hành vi".
- **Nguồn số:** $\sigma(5)=1/1{,}006738$, $\sigma(6)=1/1{,}002479$ (ghi chú diễn giả, phép chia); $0{,}2311/0{,}0042\approx55$.
- **Diễn giả:** câu hỏi của đề xuất: "Tại sao không đơn giản giảm bước học?" Bước học nhỏ thu nhỏ $\lVert\Delta\theta\rVert$ như nhau ở mọi điểm và mọi hướng: ở $\theta=5$ bước đã gần như không đổi hành vi, ở $\theta=0$ cùng bước đổi nhiều. Trên chuỗi, độ dốc $p_s(1-p_s)$ là $\tfrac14$ và $\tfrac29$, gần nhau; khác biệt lớn đến từ tần suất gặp trạng thái (`4-22`).
- **Nguồn:** §4.4 (đoạn mở; Ví dụ 10.13).
- **Nối vào:** `4-17`. **Nối ra:** `4-12` (đo khoảng cách giữa hai phân phối hành động).
- **Phút:** 1,5.

#### `L10-4-12` · Khoảng cách giữa hai phân phối hành động (sửa; cụm C; đề xuất 13, H9)

- **Quyết định:** sửa. TV và KL định nghĩa cùng một khối như Định nghĩa 10.23 mới (TV cần cho trang (15) `4-21`, đứng trước cụm lý thuyết). Hình ba thanh Bernoulli tại $s_A$ thay dòng số dài; KL trung bình chuyển sang `4-07`; "Dạng khác: $-\log\rho$" xuống ghi chú diễn giả.
- **Mục đích:** định nghĩa hai khoảng cách giữa phân phối hành động và cho thấy KL tăng nhanh khi chính sách mới gần bỏ một hành động.
- **Câu:** 4. **Nhãn:** "Định nghĩa.", hộp.
- **Mặt trang:**
  - "Khác biệt giữa hai phân phối hành động đo được bằng lượng xác suất phải dời, hoặc bằng kỳ vọng của log-tỉ số hai xác suất." (Đ5)
  - "**Định nghĩa.** Với hai phân phối $q$, $q'$ trên tập hành động, khoảng cách biến phân toàn phần (total variation distance, TV) và phân kỳ Kullback–Leibler (Kullback–Leibler divergence, KL) là" $$D_{\mathrm{TV}}(q,q')=\tfrac12\sum_a\lvert q(a)-q'(a)\rvert,\qquad D_{\mathrm{KL}}(q\Vert q')=\sum_aq(a)\log\frac{q(a)}{q'(a)}.$$
  - "Tại $s_A$, so với $\pi$: $(0{,}6;\,0{,}4)$ cho $D_{\mathrm{KL}}=\tfrac12\log\tfrac{0{,}5}{0{,}6}+\tfrac12\log\tfrac{0{,}5}{0{,}4}=0{,}0204$; $\tilde\pi$ cho $D_{\mathrm{TV}}=\tfrac12(0{,}4+0{,}4)=0{,}4$, $D_{\mathrm{KL}}=\tfrac12\log\tfrac{0{,}5}{0{,}9}+\tfrac12\log\tfrac{0{,}5}{0{,}1}=\log\tfrac53\approx0{,}511$."
  - Hộp: "TV tăng $4$ lần thì KL tăng khoảng $25$ lần. Khi chính sách mới gần bỏ một hành động, KL tăng không giới hạn, còn $D_{\mathrm{TV}}\le1$."
- **Hình:** `kl-ba-bernoulli-buoc0.svg` (hàng $\pi$), `-buoc1.svg` (thêm $(0{,}6;\,0{,}4)$, nhãn $t=0{,}25$), `kl-ba-bernoulli.svg` (thêm $\tilde\pi$); cột phải mỗi hàng ghi "TV … · KL …"; mô tả ở §4.5. Nửa phải.
- **Dựng dần:** (0) dòng trực quan, định nghĩa, hình `-buoc0`; (1) hình `-buoc1`; (2) hình đủ, dòng số; (3) hộp.
- **1 phút:** TV đo xác suất phải dời, KL đo log-tỉ số; bước lớn tại $s_A$ làm KL tăng nhanh hơn TV nhiều.
- **Mới:** $D_{\mathrm{TV}}$, $D_{\mathrm{KL}}$ (hai đối tượng, TB24).
- **Nguồn số:** phân phối tại $s_A$ từ `4-01`, `4-10` ($t=0{,}25$); $D_{\mathrm{TV}}$ của $(0{,}6;\,0{,}4)$ bằng $\tfrac12(0{,}1+0{,}1)=0{,}1$ (ghi trên hình).
- **Diễn giả:** KL không đối xứng: $D_{\mathrm{KL}}(\tilde\pi\Vert\pi)=0{,}368\ne0{,}511$; bài dùng chiều cũ‖mới như TRPO. Dạng khác $D_{\mathrm{KL}}(\pi\Vert\pi')=\mathbb E_{a\sim\pi}[-\log\rho(s,a)]$ gắn KL với tỉ số chính sách. KL trơn theo $\theta$ khi $\pi_\theta>0$, còn $D_{\mathrm{TV}}$ chứa $\lvert\cdot\rvert$. Ở Ví dụ 10.13 (`4-28`): $0{,}1201$ và $0{,}00245$. Với hai hành động, $D_{\mathrm{TV}}=\lvert\Delta p\rvert$.
- **Nguồn:** §4.4 (Định nghĩa 10.23; đoạn sau; bảng KL ba phân phối Bernoulli và đoạn sau).
- **Nối vào:** `4-28`. **Nối ra:** `4-07` (đặt giới hạn KL vào bài toán).
- **Phút:** 1,5.

#### `L10-4-07` · Bài toán miền tin cậy (sửa; cụm C; đề xuất 14, H7 phần vùng KL; trạm dừng)

- **Quyết định:** sửa. Trang đứng trước mọi chứng minh (tinh chỉnh TB27): bài toán là đầu ra của trực giác ở `4-16`–`4-12`, không còn suy ra từ hệ quả chặn cải thiện. Thêm KL trung bình và $\nu^\pi$ (từ `4-12`, `4-24` cũ). Sau cổng storyboard: hàm mục tiêu viết dạng tỉ số như Định nghĩa 10.24; thêm câu về dấu và độ lớn của dự báo tại biên; khối $0{,}145$ của $\nu^\pi$ ở ghi chú diễn giả; ba phần tử mới là ngoại lệ ở §7. Đề xuất gọi đây là trang sinh viên cần nhớ.
- **Mục đích:** phát biểu bài toán trung tâm của mạch và giải nó trên đoạn thẳng.
- **Câu:** 4. **Nhãn:** "Ký hiệu:", "Định nghĩa.", "Ý nghĩa:".
- **Mặt trang:**
  - "Ký hiệu: phân bố chiếm dụng $\nu^\pi(s)=(1-\gamma)\eta_\pi(s)$, trên chuỗi $\nu^\pi=(0{,}1;\,0{,}045)$. KL trung bình $\bar D_{\mathrm{KL}}(\pi\Vert\pi')=\sum_s\nu^\pi(s)\,D_{\mathrm{KL}}(\pi(\cdot\mid s)\Vert\pi'(\cdot\mid s))$ là kỳ vọng theo $\nu^\pi$, không phải trung bình trên mẫu." (Đ4)
  - "**Định nghĩa.** Với bán kính $\kappa>0$, bài toán miền tin cậy (trust region problem) là" $$\max_\theta\ \mathbb E_{S\sim\nu^\pi,\,A\sim\pi(\cdot\mid S)}\bigl[\rho_\theta(S,A)\,A_\pi(S,A)\bigr]\quad\text{với ràng buộc}\quad\bar D_{\mathrm{KL}}(\pi\Vert\pi_\theta)\le\kappa,$$ "với $\rho_\theta(s,a)=\pi_\theta(a\mid s)/\pi(a\mid s)$."
  - Hộp: "Ý nghĩa: hàm mục tiêu bằng $(1-\gamma)\Delta\mathcal L$, nên chọn hành vi có dự báo tốt nhất; ràng buộc giữ chính sách mới gần chính sách đã sinh dữ liệu."
  - "Với $\tilde\pi$: $D_{\mathrm{KL}}(s_B)=\tfrac23\log\tfrac43+\tfrac13\log\tfrac23=0{,}0566$, $\bar D_{\mathrm{KL}}=0{,}1\cdot0{,}511+0{,}045\cdot0{,}0566=0{,}0536>\kappa=0{,}01$."
  - "Giải số $\bar D_{\mathrm{KL}}(\pi_t)=0{,}01$ trên đoạn: $t=0{,}515$. Tại biên, $\Delta\mathcal L\approx0{,}049$ và $\Delta J\approx0{,}0012$: cùng dấu dương, nhưng dự báo lớn hơn thực tế khoảng $40$ lần."
- **Hình:** giữ `ham-thay-the-mien-tin-cay-buoc0.svg`, `ham-thay-the-mien-tin-cay.svg` (sửa nhãn "$0{,}054$" thành "$0{,}0536$" cho khớp mặt trang). Nửa phải.
- **Dựng dần:** (0) ký hiệu; (1) định nghĩa, hộp ý nghĩa; (2) dòng $\tilde\pi$; (3) dòng giải số, hình `-buoc0`; (4) hình đủ.
- **1 phút:** TRPO tối đa dự báo trong vùng KL trung bình nhỏ; trên chuỗi vùng đó dừng ở $t=0{,}515$, trước chỗ $\Delta J$ đổi dấu, và tại biên dự báo vẫn lớn hơn thực tế nhiều.
- **Mới:** $\nu^\pi$, $\bar D_{\mathrm{KL}}$, bài toán miền tin cậy (ba phần tử, vượt TB11; ngoại lệ §7).
- **Nguồn số:** $\eta_\pi$ từ `4-03`, $1-\gamma=0{,}1$; $\rho$ từ `4-11`; $0{,}511$ từ `4-12`; $\Delta\mathcal L$, $\Delta J$ tại $t=0{,}515$ theo công thức `4-04`; $0{,}049/0{,}0012\approx41$; nghiệm số $t=0{,}515$ (ghi chú diễn giả: $D_{\mathrm{KL}}(s_A)=0{,}093$, $D_{\mathrm{KL}}(s_B)=0{,}0155$, $0{,}1\cdot0{,}093+0{,}045\cdot0{,}0155=0{,}0100$; $t=0{,}25$ cho $0{,}0022$, $t=0{,}5$ cho $0{,}0094$).
- **Diễn giả:** tổng của $\nu^\pi$ trên chuỗi là $0{,}145\le1$, vì lượt kết thúc. Theo dạng tỉ số của Định nghĩa 10.21, hàm mục tiêu là $(1-\gamma)(\mathcal L-J)$; dạng (14) của Schulman và cộng sự (2015) bỏ thừa số $1/(1-\gamma)$ và thay $A$ bằng $Q$, có cùng nghiệm. Định nghĩa 10.24 giả thiết $\pi_{\mathrm{old}}>0$ nên dạng tỉ số luôn dùng được. $\kappa$ là siêu tham số. Mép miền gần điểm $\Delta J=0$ ($t=0{,}528$) do cách chọn $\kappa$. Bài toán không tự bảo đảm $J$ tăng.
- **Nguồn:** §4.4 (đoạn KL trung bình trên chuỗi); §4.5 (Định nghĩa 10.24 và đoạn sau, ví dụ $\kappa=0{,}01$).
- **Nối vào:** `4-12`. **Nối ra:** `4-21` (vì sao giới hạn KL kiểm soát sai số).
- **Phút:** 1,5.

#### `L10-4-32` · Ví dụ: miền tin cậy $\kappa=0{,}01$ loại $\tilde\pi$ (thêm, tách từ `4-07`; cụm C; quyết định của điều phối viên sau lượt sửa C)

- **Quyết định:** thêm. `4-07` chứa cả định nghĩa, ý nghĩa và ví dụ số thì chạm chân trang (698 px, `footer_check.py`); điều phối viên quyết tách, nội dung giữ nguyên. `4-07` giữ dòng mở, "Ký hiệu:" ($\nu^\pi$, tổng $0{,}145$; $\bar D_{\mathrm{KL}}$ là tổng có trọng số), "Định nghĩa." và hộp "Ý nghĩa:" ($(1-\gamma)\Delta\mathcal L$; ràng buộc giữ chính sách mới gần chính sách cũ).
- **Mục đích:** giải bài toán miền tin cậy trên đoạn thẳng: $\tilde\pi$ nằm ngoài miền, biên ở $t=0{,}515$.
- **Mặt trang:** "Nhắc lại: $\nu^\pi=(0{,}1;\,0{,}045)$; với $\tilde\pi$, $D_{\mathrm{KL}}(s_A)=0{,}511$."; "Với $\tilde\pi$ và $\kappa=0{,}01$: $D_{\mathrm{KL}}(s_B)=\tfrac23\log\tfrac43+\tfrac13\log\tfrac23=0{,}0566$, nên $\bar D_{\mathrm{KL}}(\tilde\pi)=0{,}1\cdot0{,}511+0{,}045\cdot0{,}0566=0{,}0536\gt\kappa$."; hộp "Nghiệm của $\bar D_{\mathrm{KL}}(\pi_t)=0{,}01$ là $t=0{,}515$. Tại đó $\Delta\mathcal L\approx0{,}049\approx41\,\Delta J$."
- **Hình:** `ham-thay-the-mien-tin-cay-buoc0.svg` (mảnh 1), `ham-thay-the-mien-tin-cay.svg` (mảnh 2), 440 px, nửa phải. **Dựng dần:** (0) nhắc lại, dòng $\tilde\pi$; (1) hình `-buoc0`, hộp nghiệm; (2) hình đủ.
- **1 phút:** Với $\kappa=0{,}01$, $\tilde\pi$ có KL trung bình $0{,}0536$ nên bị loại; miền dừng ở $t=0{,}515$, nơi dự báo vẫn lớn hơn thực tế khoảng $41$ lần.
- **Mới:** không. **Nguồn số:** như mục `4-07` cũ (§3 trên).
- **Diễn giả:** mép miền ($t=0{,}515$) trước điểm $\Delta J=0$ ($t=0{,}528$); KL trung bình nhỏ hơn KL từng trạng thái vì khối $0{,}145$; đường tính KL tại biên, $\Delta\mathcal L$, $\Delta J$.
- **Nguồn:** §4.4 (KL trung bình trên chuỗi); §4.5 (đoạn sau Định nghĩa 10.24, ví dụ $\kappa=0{,}01$).
- **Nối vào:** `4-07`. **Nối ra:** `4-21`.
- **Phút:** 0,75 (`4-07` còn 0,75).

#### `L10-4-21` · Giới hạn KL kiểm soát sai số qua ba mắt xích (sửa; cụm C; đề xuất 15, H10)

- **Quyết định:** sửa. Trang (15) của đề xuất mang hình chuỗi bốn khối và hệ quả chặn cải thiện theo KL (khối chính của `4-21` cũ). Hệ quả cải thiện đơn điệu tách sang `4-29` (bỏ ngoại lệ hai khối có số hiệu, TB6). Sau cổng storyboard: bỏ dòng "Chứng minh." trên trang này; chứng minh hệ quả đặt ở `4-06`, sau khi cả ba mắt xích đã có trang (`4-20`, `4-24`, `4-06`). Đây là lần đầu dùng "chặn cải thiện", nên tên tiếng Anh ở đây.
- **Mục đích:** nối giới hạn KL của bài toán với sai số của hàm thay thế bằng một cận.
- **Câu:** 4. **Nhãn:** "Hệ quả.", "Giả thiết:", "Ký hiệu:", "Kết luận:", "Ý nghĩa:".
- **Mặt trang:**
  - Hình chuỗi bốn khối (toàn bề rộng, thấp).
  - Khối: "**Hệ quả** (chặn cải thiện, policy improvement bound, theo KL trung bình). Giả thiết: giả thiết chung; $A_\pi$ và $\nu^\pi$ tính chính xác. Ký hiệu: $\chi_{\pi'}=\max_s\lvert A_\pi(s,\pi')\rvert$. Kết luận:" $$J(\pi')-J(\pi)\ \ge\ \Delta\mathcal L-\frac{2\gamma\,\chi_{\pi'}}{(1-\gamma)^2}\sqrt{\tfrac12\,\bar D_{\mathrm{KL}}}.$$
  - Hộp: "Ý nghĩa: với $\tilde\pi$, $\chi=0{,}5$ và phạt $\tfrac{2\cdot0{,}9\cdot0{,}5}{0{,}01}\sqrt{0{,}0536/2}\approx14{,}7>0{,}095$, nên cận không chứng nhận $J$ tăng. Cận chỉ chứng nhận khi $\Delta\mathcal L$ lớn hơn phạt."
- **Hình:** `chuoi-bon-mat-xich-buoc0.svg` … `chuoi-bon-mat-xich.svg` (bốn bản, mỗi mũi tên một mảnh; nhãn mắt xích 3 "định lý chặn cải thiện"); mô tả ở §4.5.
- **Dựng dần:** (0) khối 1; (1)–(3) từng mũi tên và khối tiếp; (4) hệ quả; (5) hộp.
- **1 phút:** KL nhỏ kéo theo TV nhỏ, phân bố chiếm dụng ít đổi và sai số nhỏ; với $\tilde\pi$ phạt $14{,}7$ lớn hơn nhiều mức tăng dự báo.
- **Mới:** $\chi_{\pi'}$; hệ quả (hai đối tượng).
- **Nguồn số:** $A_\pi(s,\tilde\pi)$ từ `4-13`; $\bar D_{\mathrm{KL}}=0{,}0536$ từ `4-07`; $\sqrt{0{,}0268}=0{,}164$; $90\cdot0{,}164=14{,}7$.
- **Diễn giả:** đọc chuỗi: bất đẳng thức Pinsker cho $D_{\mathrm{TV}}(s)\le\sqrt{D_{\mathrm{KL}}(s)/2}$; bổ đề dịch chuyển chặn $\lVert\nu^{\pi'}-\nu^\pi\rVert_1$; định lý chặn cải thiện chặn sai số $\lvert\Delta J-\Delta\mathcal L\rvert$ theo khoảng cách đó, qua đẳng thức sai số của bảng đóng góp từng trạng thái. Hệ quả đúng với cả hai chiều KL. TRPO thực hành ràng buộc KL trên mẫu và giải gần đúng, nên thỏa ràng buộc chưa đủ để $J$ tăng; cận có thể lỏng (với $\gamma=0{,}99$, $2\gamma/(1-\gamma)^2=19\,800$).
- **Nguồn:** §4.5 (đoạn ba mắt xích và cận); §4.6 (Hệ quả 10.28; đoạn sau hệ quả, số $14{,}7$).
- **Nối vào:** `4-07`. **Nối ra:** `4-14` (cụm lý thuyết: mắt xích dưới cùng của định lý là bổ đề chênh lệch hiệu năng).
- **Phút:** 1,5.

**Cụm "Cơ sở lý thuyết"** (`4-14` → `4-20` → `4-24` → `4-06` → `4-19` → `4-29`, 8 phút). Đặt sau `4-21`, trước cụm D (quyết định của tác giả). Sau cổng storyboard, thứ tự theo các mắt xích của H10: bổ đề chênh lệch hiệu năng (nền của đẳng thức sai số), Pinsker (mắt xích 1), bổ đề dịch chuyển (mắt xích 2), định lý chặn cải thiện (mắt xích 3) cùng chứng minh hệ quả KL của `4-21`, ví dụ trên chuỗi, hệ quả đơn điệu. Không có trang tiêu đề cụm (VP: không câu điều hướng); tên cụm chỉ ở storyboard.

#### `L10-4-14` · Ý tưởng chứng minh: bổ đề chênh lệch hiệu năng (giữ, chuyển vào cụm lý thuyết)

- **Quyết định:** giữ mặt trang; chuyển chỗ; thêm dòng bỏ giả thiết "cùng $\mu_0$" từ `4-15` cũ (Đ2) làm mảnh cuối.
- **Mục đích:** cho lộ trình năm bước của chứng minh bổ đề và vai trò của từng giả thiết.
- **Câu:** 4 (cơ sở lý thuyết). **Nhãn:** "Ý tưởng chứng minh." (tiêu đề), "Câu hỏi:", "Lời giải:".
- **Mặt trang:** năm bước như deck (Đ8); hộp câu hỏi và lời giải như deck (Đ9); mảnh cuối: "Bỏ cùng $\mu_0$: nếu $\tilde\pi$ xuất phát từ $s_B$ còn $\pi$ từ $s_A$, vế trái là $0{,}5\cdot3-1{,}4=0{,}1$, vế phải là $A_\pi(s_B,\tilde\pi)=-0{,}5$."
- **Hình:** không. **Dựng dần:** từng bước; câu hỏi; lời giải; dòng bỏ giả thiết.
- **1 phút:** Lợi thế của $\pi$ cộng dọc lượt của $\pi'$ là tổng lồng nhau, còn lại đúng hiệu $J$; Bước 4 cần cùng $\mu_0$.
- **Mới:** không. **Nguồn số:** $A_\pi(s_B,\tilde\pi)$ từ `4-13`; $v_{\tilde\pi}(s_B)=\tilde p_B\cdot3$.
- **Diễn giả:** như deck: Bước 2 dùng cùng $P$ và tính Markov; Bước 4 dùng cùng $\mu_0$, phần thưởng bị chặn và $\gamma<1$. Ghi chú dùng phản ví dụ cùng dạng với $\pi'=(0{,}6;\,0{,}8)$ ($1$ so với $0{,}4$); số với $\tilde\pi$ là đề xuất NT3 (§10). Ngoại lệ mật độ: §7.
- **Nguồn:** §4.1 (Bổ đề 10.19, chứng minh Bước 1–5; đoạn "Hai giả thiết có vai trò riêng").
- **Nối vào:** `4-21`. **Nối ra:** `4-20`.
- **Phút:** 1,5.

#### `L10-4-20` · Bất đẳng thức Pinsker (giữ, sửa dòng "Ý nghĩa:"; cụm lý thuyết; mắt xích 1)

- **Quyết định:** giữ khối mệnh đề và dòng "Chứng minh."; dòng "Ý nghĩa:" tính $D_{\mathrm{TV}}(s_B)=\tfrac16$ ngay trên trang (sau cổng storyboard, vì `4-20` nay đứng trước `4-24`); dòng nguồn đổi số (Mệnh đề 10.25(b)).
- **Mục đích:** cho mắt xích thứ nhất: KL nhỏ thì TV nhỏ.
- **Câu:** 4 (cơ sở lý thuyết). **Nhãn:** "Mệnh đề.", "Giả thiết:", "Kết luận:", "Chứng minh.", "Ý nghĩa:".
- **Mặt trang:** khối mệnh đề và "Chứng minh." như deck; "Ý nghĩa: KL nhỏ kéo theo TV nhỏ. Với $\tilde\pi$, tại $s_A$: $0{,}4\le\sqrt{0{,}511/2}=0{,}505$; tại $s_B$: $D_{\mathrm{TV}}=\tfrac12\bigl(\lvert0{,}5-\tfrac23\rvert+\lvert0{,}5-\tfrac13\rvert\bigr)=\tfrac16\approx0{,}167\le\sqrt{0{,}0566/2}=0{,}168$."
- **Hình:** không. **Dựng dần:** như deck.
- **1 phút:** Khoảng cách TV bị chặn bởi căn của nửa KL; trên chuỗi bất đẳng thức gần chặt tại $s_B$.
- **Mới:** bất đẳng thức Pinsker. **Nguồn số:** $D_{\mathrm{TV}}(s_A)$, $D_{\mathrm{KL}}(s_A)$ từ `4-12`; $D_{\mathrm{KL}}(s_B)$ từ `4-07`; $D_{\mathrm{TV}}(s_B)$ trên trang.
- **Diễn giả:** như deck; thêm: chứng minh hệ quả theo KL trung bình (`4-06`) dùng bất đẳng thức này tại từng trạng thái.
- **Nguồn:** §4.6 (Mệnh đề 10.25(b), chứng minh Bước 3; đoạn sau).
- **Nối vào:** `4-14`. **Nối ra:** `4-24` (mắt xích 2).
- **Phút:** 1.

#### `L10-4-24` · Bổ đề dịch chuyển phân bố chiếm dụng (sửa; cụm lý thuyết; mục "TV và phân bố chiếm dụng" của đề xuất; mắt xích 2)

- **Quyết định:** sửa. Giữ mã vì trang cũ "Biến phân toàn phần và phân bố chiếm dụng" chuyển thành trang của mắt xích "TV nhỏ thì phân bố chiếm dụng ít thay đổi"; định nghĩa TV đã lên `4-12`, $\nu^\pi$ lên `4-07`, $\chi$ lên `4-21`. Bổ đề 10.26 có khối riêng (TB28); trước đây chỉ nêu trong bước 5 của `4-18`. Sau cổng storyboard: vế trái viết $0{,}1\cdot\lvert0{,}81-0{,}45\rvert$ để thấy đây là hiệu phân bố chiếm dụng, không lẫn với sai số $0{,}036$ của bước $\pi'$ trong ghi chú.
- **Mục đích:** phát biểu mắt xích thứ hai và kiểm trên chuỗi.
- **Câu:** 4 (cơ sở lý thuyết). **Nhãn:** "Bổ đề.", "Giả thiết:", "Kết luận:", "Chứng minh.".
- **Mặt trang:**
  - "Tại mọi trạng thái, nếu $\pi'$ chọn hành động gần như $\pi$ thì hai chính sách gặp các trạng thái với tần suất gần nhau. Khác biệt nhỏ ở mỗi bước tích lũy dọc lượt." (Đ5)
  - "**Bổ đề** (dịch chuyển phân bố chiếm dụng). Giả thiết: giả thiết chung. Kết luận, với $D_{\mathrm{TV}}(s)=D_{\mathrm{TV}}(\pi'(\cdot\mid s),\pi(\cdot\mid s))$:" $$\sum_s\bigl\lvert\nu^{\pi'}(s)-\nu^\pi(s)\bigr\rvert\ \le\ \frac{2\gamma}{1-\gamma}\,\mathbb E_{S\sim\nu^\pi}\bigl[D_{\mathrm{TV}}(S)\bigr].$$
  - "Chứng minh. Hiệu hai phân bố bằng $\gamma$ nhân khác biệt một bước của hai ma trận chuyển, lan qua các bước sau với tổng trọng số không quá $\tfrac1{1-\gamma}$; khác biệt một bước không quá $2\,\mathbb E_{\nu^\pi}[D_{\mathrm{TV}}]$."
  - "Ở đây, với $\tilde\pi$: $\mathbb E_{\nu^\pi}[D_{\mathrm{TV}}]=0{,}1\cdot0{,}4+0{,}045\cdot\tfrac16=0{,}0475$. Chỉ $s_B$ đổi tần suất: vế trái $=(1-\gamma)\lvert\eta_{\tilde\pi}(s_B)-\eta_\pi(s_B)\rvert=0{,}1\cdot\lvert0{,}81-0{,}45\rvert=0{,}036$, vế phải $=18\cdot0{,}0475=0{,}855$."
- **Hình:** không. **Dựng dần:** (0) trực quan; (1) bổ đề; (2) chứng minh; (3) dòng số.
- **1 phút:** Khoảng cách giữa hai phân bố chiếm dụng không vượt $\tfrac{2\gamma}{1-\gamma}$ lần TV kỳ vọng; trên chuỗi cận đúng nhưng lỏng.
- **Mới:** bổ đề dịch chuyển.
- **Nguồn số:** $D_{\mathrm{TV}}=(0{,}4;\,\tfrac16)$ từ `4-12`, `4-20`; $\nu^\pi$ từ `4-07`; $\eta$ từ `4-02`, `4-03`; $2\gamma/(1-\gamma)=18$.
- **Diễn giả:** câu hỏi của `4-18` cũ: vì sao định lý có $1/(1-\gamma)^2$. Một thừa số $\tfrac1{1-\gamma}$ ở bổ đề này (khác biệt tích lũy qua các bước sau), một thừa số khi đổi $\nu$ về $\eta$ trong định lý. Chứng minh trong ghi chú dùng dạng ma trận $(I-\gamma P_\pi)^{-1}$; sự kết thúc chỉ làm các tổng nhỏ đi. Ghi chú kiểm bổ đề với $\pi'=(0{,}6;\,0{,}8)$ ($0{,}009$ so với $0{,}288$); số với $\tilde\pi$ là đề xuất NT3 (§10).
- **Nguồn:** §4.6 (Bổ đề 10.26, chứng minh Bước 1–6; đoạn trực quan trước bổ đề; đoạn sau chứng minh).
- **Nối vào:** `4-20`. **Nối ra:** `4-06` (mắt xích 3).
- **Phút:** 1,5.

#### `L10-4-06` · Định lý chặn cải thiện (sửa, gộp `4-18`; cụm lý thuyết; mục "định lý chặn cải thiện và ý tưởng chứng minh"; mắt xích 3)

- **Quyết định:** sửa. Chứng minh rút thành một dòng gọi tên Bước 1–5 của ghi chú, vì đẳng thức sai số (`4-16`) và bổ đề dịch chuyển (`4-24`) đã có trang (TB28 dạng a); `4-18` bỏ. Giả thiết theo Định lý 10.27 mới (không còn điều kiện hỗ trợ). Sau cổng storyboard: "Ý nghĩa:" dùng biểu thức của ghi chú $\tfrac{2\gamma\chi}{(1-\gamma)^2}=90$; dòng chứng minh Hệ quả 10.28 (của `4-21`) đặt ở mảnh cuối trang này.
- **Mục đích:** phát biểu cận dạng TV và khép chứng minh của cận dạng KL ở `4-21`.
- **Câu:** 4 (cơ sở lý thuyết). **Nhãn:** "Định lý.", "Giả thiết:", "Kết luận:", "Chứng minh.", "Ý nghĩa:".
- **Mặt trang:**
  - "**Định lý** (chặn cải thiện). Giả thiết: giả thiết chung; $A_\pi$ và $\nu^\pi$ tính chính xác. Kết luận:" $$J(\pi')-J(\pi)\ \ge\ \Delta\mathcal L-\frac{2\gamma\,\chi_{\pi'}}{(1-\gamma)^2}\,\mathbb E_{S\sim\nu^\pi}\bigl[D_{\mathrm{TV}}(S)\bigr].$$
  - "Chứng minh. Bước 1–3: bổ đề chênh lệch hiệu năng và hàm thay thế cho $\Delta J-\Delta\mathcal L=\sum_s(\eta_{\pi'}-\eta_\pi)(s)A_\pi(s,\pi')$. Bước 4: bất đẳng thức Hölder chặn tổng này dưới bởi $-\chi_{\pi'}\sum_s\lvert\eta_{\pi'}(s)-\eta_\pi(s)\rvert$. Bước 5: bổ đề dịch chuyển, với $\eta=\nu/(1-\gamma)$."
  - "Ý nghĩa: phạt tỉ lệ với TV kỳ vọng theo phân bố của chính sách cũ. Với $\tilde\pi$, $\chi=0{,}5$ và $\tfrac{2\gamma\chi}{(1-\gamma)^2}=\tfrac{2\cdot0{,}9\cdot0{,}5}{0{,}01}=90$."
  - "**Chứng minh** (hệ quả chặn cải thiện theo KL trung bình). Bất đẳng thức Pinsker tại từng trạng thái, rồi bất đẳng thức Jensen cho hàm lõm $\sqrt{\cdot}$ với $\sum_s\nu^\pi(s)\le1$, cho $\mathbb E_{\nu^\pi}[D_{\mathrm{TV}}]\le\sqrt{\tfrac12\bar D_{\mathrm{KL}}}$; thế vào định lý."
- **Hình:** không. **Dựng dần:** (0) định lý; (1) chứng minh; (2) ý nghĩa; (3) chứng minh hệ quả.
- **1 phút:** Mức tăng thật không nhỏ hơn dự báo trừ một phạt tỉ lệ với TV kỳ vọng giữa hai chính sách; Pinsker và Jensen đổi phạt đó sang KL trung bình.
- **Mới:** định lý.
- **Nguồn số:** $\chi$ từ `4-21`; $2\cdot0{,}9\cdot0{,}5/0{,}01$.
- **Diễn giả:** cận vẫn đúng khi thay $\chi_{\pi'}$ bằng $\max_{s,a}\lvert A_\pi(s,a)\rvert$. Định lý không cần điều kiện hỗ trợ vì Bước 3 dùng dạng tổng của hàm thay thế. Bỏ "$\gamma<1$" thì thừa số vô hạn; bỏ "đại lượng chính xác" thì cận không còn chứng nhận cải thiện. Nhận xét 10.29: cận dạng TV lớn nhất của Schulman và cộng sự (2015), lỏng hơn trên chuỗi. Dòng chứng minh hệ quả là Bước 1–3 của chứng minh Hệ quả 10.28.
- **Nguồn:** §4.6 (Định lý 10.27, chứng minh Bước 1–5; đoạn sau định lý; Hệ quả 10.28, chứng minh Bước 1–3; Nhận xét 10.29).
- **Nối vào:** `4-24`. **Nối ra:** `4-19`.
- **Phút:** 1.

#### `L10-4-19` · Ví dụ: chặn cải thiện trên chuỗi (giữ; cụm lý thuyết; mục "ví dụ trên chuỗi")

- **Quyết định:** giữ bảng; sửa dòng "Nhắc lại:" theo trang mới của các đại lượng ($\nu^\pi$ ở `4-07`, $D_{\mathrm{TV}}$ ở `4-12`, `4-20`, $\chi$ ở `4-21`) và dòng nguồn. Trang mang thông điệp "cận có ích" của TB15 (cận dương với bước ngắn) và "cận lỏng" (bước tới $\tilde\pi$).
- **Mục đích:** cho hai số của cận trên chuỗi: đúng nhưng lỏng với $\tilde\pi$, dương với bước rất ngắn.
- **Câu:** 4 (cơ sở lý thuyết). **Nhãn:** "Nhắc lại:", hộp.
- **Mặt trang:** như deck; giữ phép tính đủ $0{,}1\cdot0{,}4+0{,}045\cdot\tfrac16=0{,}0475$ trong ô (TB29: phép tính ở `4-24` cách hai trang).
- **Hình:** không. **Dựng dần:** như deck.
- **1 phút:** Với $\tilde\pi$ cận là $-4{,}18$, đúng nhưng xa $-0{,}085$; cận chỉ dương khi bước chỉ đổi $p_B$ dưới $0{,}056$.
- **Mới:** không. **Nguồn số:** như deck.
- **Diễn giả:** như deck; Ví dụ 10.14 còn tính bước $\pi'=(0{,}6;\,0{,}8)$: phạt $1{,}152>0{,}26$.
- **Nguồn:** §4.6 (Ví dụ 10.14: bước dài $\tilde\pi$, bước nhỏ chỉ đổi $s_B$, "Diễn giải", "Kiểm tra lại").
- **Nối vào:** `4-06`. **Nối ra:** `4-29`.
- **Phút:** 1,5.

#### `L10-4-29` · Cải thiện đơn điệu qua hàm chặn dưới (thêm, tách từ `4-21`; cụm lý thuyết; mục "hệ quả đơn điệu")

- **Quyết định:** thêm. Hệ quả 10.30 có trang riêng thay vì đứng chung `4-21` (TB6). Trang khép cụm lý thuyết và nối về bài toán `4-07`: phạt với hằng của lý thuyết cho bước gần như bằng $0$, nên TRPO dùng ràng buộc.
- **Mục đích:** cho biết khi nào cận bảo đảm $J$ không giảm, và vì sao TRPO không dùng trực tiếp cách đó.
- **Câu:** 4 (cơ sở lý thuyết). **Nhãn:** "Hệ quả.", "Giả thiết:", "Kết luận:", "Chứng minh.", hộp.
- **Mặt trang:**
  - "**Hệ quả** (cải thiện đơn điệu). Giả thiết: như định lý chặn cải thiện cho mỗi cặp $(\pi_k,\pi)$, với $A_{\pi_k}$, $\nu^{\pi_k}$ chính xác. Đặt $C_k=\tfrac{2\gamma\bar\chi_k}{(1-\gamma)^2}$, $\bar\chi_k=\max_{s,a}\lvert A_{\pi_k}(s,a)\rvert$ và" $$\mathcal M_k(\pi)=\mathcal L_{\pi_k}(\pi)-C_k\,\mathbb E_{S\sim\nu^{\pi_k}}\bigl[D_{\mathrm{TV}}(S)\bigr].$$ "Kết luận: nếu $\mathcal M_k(\pi_{k+1})\ge\mathcal M_k(\pi_k)$ thì $J(\pi_{k+1})\ge J(\pi_k)$."
  - "Chứng minh. $J(\pi_{k+1})\ge\mathcal M_k(\pi_{k+1})\ge\mathcal M_k(\pi_k)=J(\pi_k)$, theo định lý, giả thiết, rồi $\mathcal L_{\pi_k}(\pi_k)=J(\pi_k)$ và $D_{\mathrm{TV}}=0$."
  - "Trên chuỗi, $\bar\chi=2$ nên $C=\tfrac{2\cdot0{,}9\cdot2}{0{,}01}=360$: mọi bước khác $\pi_k$ làm $\mathcal M_k$ giảm, nên phép cực đại hóa đứng yên tại $\pi_k$."
  - Hộp: "TRPO thay phạt bằng ràng buộc $\bar D_{\mathrm{KL}}\le\kappa$ của bài toán miền tin cậy. Bước được phép dài hơn, đổi lại $J$ có thể giảm."
- **Hình:** không. **Dựng dần:** (0) hệ quả; (1) chứng minh; (2) dòng chuỗi; (3) hộp.
- **1 phút:** Cực đại một hàm nằm dưới $J$ và chạm $J$ tại chính sách hiện tại thì $J$ không giảm, nhưng với hằng của lý thuyết bước gần như bằng $0$.
- **Mới:** hàm chặn dưới $\mathcal M_k$.
- **Nguồn số:** $\bar\chi=\max\lvert A_\pi(s,a)\rvert=\lvert-2\rvert$ từ `2-06`.
- **Diễn giả:** Schulman và cộng sự (2015) gọi đây là thuật toán cực đại hóa qua hàm chặn dưới (minorize–maximize). Trên chuỗi, $\mathcal M_k(\pi')-\mathcal M_k(\pi_k)\le\sum_s\nu(s)D_{\mathrm{TV}}(s)c_s$ với $c_s=8-360$ và $30-360$. Hệ quả 10.31: với đại lượng và nghiệm chính xác, bước miền tin cậy có $J(\pi_{k+1})-J(\pi_k)\ge-\sqrt{2\kappa}\,\gamma\chi_{\pi_{k+1}}/(1-\gamma)^2$; mức giảm tối đa nhỏ khi $\kappa$ nhỏ, không phải bảo đảm cải thiện. Hệ quả không áp dụng khi lợi thế, phân bố chiếm dụng hay nghiệm chỉ có gần đúng.
- **Nguồn:** §4.6 (Hệ quả 10.30, chứng minh Bước 1–3; đoạn MM; đoạn số trên chuỗi; đoạn "Để cho phép bước lớn"; Hệ quả 10.31 và đoạn sau).
- **Nối vào:** `4-19`. **Nối ra:** `4-22` (giải bài toán của `4-07` khi $d$ lớn).
- **Phút:** 1,5.

#### `L10-4-22` · Xấp xỉ bậc một của hàm thay thế và bậc hai của KL (sửa; cụm D; đề xuất 16)

- **Quyết định:** sửa. Câu mở nêu bài toán của cụm D bằng câu của ghi chú ("bài toán tối ưu phi tuyến có ràng buộc"); hai xấp xỉ đặt cạnh nhau như bảng của đề xuất §8.1; dòng nối về ví dụ sigmoid (`4-28`) ở ghi chú diễn giả, với đúng số của ghi chú.
- **Mục đích:** biến bài toán miền tin cậy thành bài toán với mục tiêu tuyến tính và ràng buộc bậc hai.
- **Câu:** 5. **Nhãn:** "Mệnh đề.", "Chứng minh.".
- **Mặt trang:**
  - "Bài toán miền tin cậy là một bài toán tối ưu phi tuyến có ràng buộc trên $\theta$, và $\theta$ có thể có hàng triệu tọa độ. Gần $\theta$: $\mathcal L_\pi(\pi_{\theta+\Delta})-J(\theta)\approx g^\top\Delta$ với $g=\nabla J$ theo mệnh đề tiếp xúc, còn KL trung bình bằng $0$ và có gradient $0$, nên cần bậc hai."
  - Khối mệnh đề như deck (giả thiết chung; $\pi_\theta$ khả vi liên tục hai lần; $\nu^\pi$ cố định; ma trận thông tin Fisher $F$; kết luận $\bar D_{\mathrm{KL}}(\theta+\Delta)=\tfrac12\Delta^\top F\Delta+o(\lVert\Delta\rVert^2)$) và dòng "Chứng minh." như deck.
  - "Ở đây $F=\operatorname{diag}(\nu^\pi(s)\,p_s(1-p_s))=\operatorname{diag}(0{,}1\cdot\tfrac14;\,0{,}045\cdot\tfrac29)=\operatorname{diag}(0{,}025;\,0{,}01)$."
- **Hình:** không. **Dựng dần:** (0) dòng mở; (1) mệnh đề; (2) chứng minh; (3) dòng số.
- **1 phút:** Gần chính sách cũ, dự báo là tuyến tính theo bước, KL trung bình là dạng toàn phương với ma trận Fisher.
- **Mới:** ma trận Fisher; xấp xỉ bậc hai.
- **Nguồn số:** $\nu^\pi$ từ `4-07`; $p_s(1-p_s)$ từ `1-11`; $\mathbb E[\psi^2]=p(1-p)^2+(1-p)p^2=p(1-p)$ (ghi chú diễn giả).
- **Diễn giả:** với sigmoid của trang "cùng một bước tham số", $F=p(1-p)$ bằng $0{,}25$ tại $\theta=0$ và $0{,}00665$ tại $\theta=5$; xấp xỉ bậc hai $\tfrac12p(1-p)\cdot1^2$ là $0{,}125$ và $0{,}00332$, cùng bậc độ lớn với KL thật $0{,}1201$ và $0{,}00245$; lệch $0{,}0049$ và $0{,}00087$ (số của ghi chú §5.1). Hai chiều KL có cùng xấp xỉ bậc hai. $F$ nửa xác định dương, có thể suy biến (Ví dụ 10.15).
- **Nguồn:** §4.6 (câu cuối: "bài toán tối ưu phi tuyến có ràng buộc trên $\theta$"); §5 (đoạn mở); §5.1 (đoạn mở; Định nghĩa 10.32; Mệnh đề 10.33, chứng minh Bước 2–3; đoạn sau mệnh đề với Ví dụ 10.13; đoạn chuỗi $F=\operatorname{diag}(0{,}025;\,0{,}01)$).
- **Nối vào:** `4-29`. **Nối ra:** `4-30` (bài toán xấp xỉ nhìn bằng hình).
- **Phút:** 1,5.

#### `L10-4-30` · Miền tin cậy bậc hai là một elip (thêm; cụm D; đề xuất 17, H11)

- **Quyết định:** thêm. Đề xuất xếp mức "cao": dẫn gradient tự nhiên từ hình học trước Cauchy–Schwarz (TB27: trực quan trước kết quả). Hình dựng trên số của chuỗi (TB25), không dùng hình tổng quát của đề xuất.
- **Mục đích:** cho thấy bằng hình vì sao bước tốt nhất trong miền KL lệch khỏi hướng $g$.
- **Câu:** 5. **Nhãn:** "Trực quan.".
- **Mặt trang:**
  - "Bài toán xấp xỉ:" $$\max_\Delta\ g^\top\Delta\quad\text{với ràng buộc}\quad\tfrac12\Delta^\top F\Delta\le\kappa .$$
  - Hình hai bảng (tròn và elip).
  - "**Trực quan.** Đường đồng mức của $g^\top\Delta$ là các đường thẳng vuông góc với $g$. Trong hình tròn, điểm tốt nhất nằm theo hướng $g$. Elip hẹp theo $\theta_A$ ($F_A=0{,}025$), rộng theo $\theta_B$ ($F_B=0{,}01$), nên điểm tốt nhất nghiêng về $\theta_B$."
  - Hộp: "Bán trục theo $\theta_B$ dài gấp $\sqrt{0{,}025/0{,}01}\approx1{,}58$ lần bán trục theo $\theta_A$."
- **Hình:** `tron-va-elip-buoc0.svg` (hình tròn, $g$), `tron-va-elip-buoc1.svg` (thêm elip với $g$ nét đứt xám), `tron-va-elip.svg` (thêm hướng tốt nhất trong elip, tím); dựng từ `elip-gradient-tu-nhien.svg`; mô tả ở §4.5. Toàn bề rộng hoặc khoảng 60%.
- **Dựng dần:** (0) bài toán, hình `-buoc0`; (1) hình `-buoc1`; (2) hình đủ, trực quan; (3) hộp.
- **1 phút:** Với ràng buộc Euclid bước đi theo $g$; với ràng buộc KL bước nghiêng về hướng mà KL ít nhạy.
- **Mới:** không (hình học của bài toán xấp xỉ).
- **Nguồn số:** $F$ từ `4-22`; $g$ từ `4-17`; bán trục $\sqrt{2\kappa/F_s}$.
- **Diễn giả:** "Tại sao không chỉ đi theo $g$?" Vì đo bước bằng chuẩn Euclid là đo trên tham số, điều `4-28` đã cho thấy không phản ánh hành vi. Không so $J$ giữa bước theo $g$ và bước theo hướng tối ưu trong elip (rủi ro số ở đầu mạch).
- **Nguồn:** §5.1 (đoạn "Một cách trực quan" về tròn và elip; đoạn sau Mệnh đề 10.34 về chuẩn Euclid và $\lVert\cdot\rVert_F$).
- **Nối vào:** `4-22`. **Nối ra:** `4-08`.
- **Phút:** 1.

#### `L10-4-08` · Gradient tự nhiên dồn bước cập nhật về $\theta_B$ (sửa; cụm D; đề xuất 18, H12; trạm dừng)

- **Quyết định:** sửa. Hình elip chuyển sang `4-30`; trang này mang hình tỉ trọng hai thành phần (H12) và dòng "hai quyết định" của đề xuất (hướng và độ dài). Sau cổng storyboard: trang là trạm dừng của cụm D (TB5): kết quả là công thức $\Delta^*$, ý nghĩa là hai quyết định, điều còn thiếu ở hộp cuối.
- **Mục đích:** phát biểu nghiệm của bài toán xấp xỉ, tách nó thành hướng và độ dài, và nêu điều còn thiếu để thành thuật toán.
- **Câu:** 5. **Nhãn:** "Mệnh đề.", "Chứng minh.", "Ý nghĩa:", hộp.
- **Mặt trang:**
  - Khối mệnh đề (bước gradient tự nhiên) và dòng "Chứng minh." như deck.
  - "Ý nghĩa: bước tối ưu gồm hai quyết định. Hướng $F^{-1}g$, gọi là gradient tự nhiên (natural gradient); độ dài $\sqrt{2\kappa/(g^\top F^{-1}g)}$, đưa bước tới biên elip."
  - "Ở đây $F^{-1}g=(0{,}2/0{,}025;\,0{,}3/0{,}01)=(8;\,30)$."
  - Hộp: "Với $d$ lớn, lập và nghịch đảo $F$ quá tốn. Thuật toán phải giải $Fx=g$ gần đúng chỉ bằng tích $Fv$, rồi kiểm lại bước trên dữ liệu vì xấp xỉ bậc hai có sai số."
- **Hình:** `ti-trong-hai-thanh-phan.svg` (H12); mô tả ở §4.5. Nửa phải.
- **Dựng dần:** (0) mệnh đề, chứng minh; (1) ý nghĩa; (2) dòng số, hình; (3) hộp.
- **1 phút:** Bước tối ưu đi theo $F^{-1}g$; trên chuỗi phần của $\theta_B$ tăng từ $60\%$ lên $79\%$; còn thiếu cách giải $Fx=g$ khi $d$ lớn.
- **Mới:** gradient tự nhiên.
- **Nguồn số:** $g$ từ `4-17`; $F$ từ `4-22`; tỉ trọng $\tfrac{0{,}3}{0{,}5}=60\%$, $\tfrac{30}{38}\approx79\%$ (ghi trên hình).
- **Diễn giả:** câu hỏi của đề xuất: "Vì sao TRPO ưu tiên đổi $\theta_B$?" KL ít nhạy theo $\theta_B$: $F_B=0{,}01<F_A=0{,}025$ chủ yếu vì $s_B$ ít được thăm ($\nu^\pi(s_B)=0{,}045$ so với $0{,}1$). Tỉ trọng so các thành phần của hướng, không phải độ dài bước. Nhân $g$ với một hằng dương không đổi $\Delta^*$. $F$ suy biến: giả nghịch đảo (Mệnh đề 10.34(b), Nhận xét 10.35). Câu bắt buộc (quyết định của điều phối viên): "Gradient tự nhiên chọn hướng theo khoảng cách KL, không bảo đảm $J$ cao hơn trên mọi bài toán." Không so $J$ của bước này với bước theo $g$. Lập $F\in\mathbb R^{d\times d}$ cần $O(d^2)$ bộ nhớ, nghịch đảo cần $O(d^3)$ phép tính.
- **Nguồn:** §5.1 (Mệnh đề 10.34(a), chứng minh Bước 1–3; hai quyết định; đoạn chuỗi: $F^{-1}g$, tỉ trọng; đoạn "Gradient tự nhiên dồn bước về $\theta_B$"); §5.2 (đoạn mở: $O(d^2)$, $O(d^3)$, tích $v\mapsto Fv$).
- **Nối vào:** `4-30`. **Nối ra:** `4-25`.
- **Phút:** 1,5.

#### `L10-4-25` · Ví dụ: một bước TRPO trên chuỗi (sửa: khôi phục đường tính của $\Delta\mathcal L$; cụm E)

- **Quyết định:** sửa hai dòng, giữ phần còn lại của mặt trang (ví dụ tay của `4-09`, `4-26`, Đ12). Sau cổng storyboard (mục nghiêm trọng 2): `4-05` cũ đã bỏ, nên hệ số $0{,}8$, $1{,}35$ của dòng $\Delta\mathcal L$ hiện tại không còn đường tính trên deck; dòng đầu thay bằng "Nhắc lại:" và dòng $\Delta\mathcal L$ viết đủ thừa số. Dòng nguồn ghi cả §5.1 và §5.2.
- **Mục đích:** tính tay một bước với cùng tên nhóm bước của thuật toán.
- **Câu:** 5. **Nhãn:** "Nhắc lại:", hộp; tên nhóm bước in đậm trùng `4-09`, `4-26`.
- **Mặt trang:**
  - "Nhắc lại: $A_\pi(s_A,\pi')=0{,}8\,\Delta p_A$, $A_\pi(s_B,\pi')=3\,\Delta p_B$, $\eta_\pi=(1;\,0{,}45)$." (thay dòng "Ví dụ dùng $g=\nabla\mathcal L$ và $F$ tính chính xác theo $\nu^\pi$.", câu này xuống ghi chú diễn giả)
  - **Tính hướng**, **Chọn độ dài bước**, dòng chính sách mới: như deck ($F^{-1}g=(8;\,30)$, $10{,}6$; $\Delta_0=0{,}04344\cdot(8;\,30)=(0{,}3475;\,1{,}3031)$; $p=(0{,}5860;\,0{,}8804)$).
  - "KL trung bình tính trực tiếp là $0{,}1\cdot0{,}0150+0{,}045\cdot0{,}156=0{,}0085\le\kappa$. Với $\Delta p=(0{,}0860;\,0{,}2137)$: $\Delta\mathcal L=1\cdot0{,}8\cdot0{,}0860+0{,}45\cdot3\cdot0{,}2137=0{,}357>0$. Bước $\Delta_0$ thỏa ràng buộc KL và làm hàm thay thế tăng, nên giữ nguyên."
  - Hộp như deck: "$J=2{,}7p_Ap_B+1-p_A=2{,}7\cdot0{,}5860\cdot0{,}8804+0{,}4140=1{,}807$, tăng từ $1{,}4$."
- **Hình:** không. **Dựng dần:** như deck; dòng "Nhắc lại:" ở mảnh (0).
- **1 phút:** Hướng $(8;\,30)$, bước tới biên miền, KL trung bình thật $0{,}0085\le\kappa$, $J$ tăng từ $1{,}4$ lên $1{,}807$.
- **Mới:** không (áp dụng).
- **Nguồn số:** $A_\pi(s_A,\pi')=0{,}4p'_A-0{,}4(1-p'_A)=0{,}8\Delta p_A$ và $A_\pi(s_B,\pi')=p'_B-2(1-p'_B)=3\Delta p_B$ từ $A_\pi(s,\cdot)$ của `2-06` (phép tính trong ghi chú diễn giả); $\eta_\pi$ từ `4-03`; $\Delta p=(0{,}5860-0{,}5;\,0{,}8804-\tfrac23)$; $D_{\mathrm{KL}}$ theo định nghĩa ở `4-12`.
- **Diễn giả:** như deck; thêm dòng đầu cũ "Ví dụ dùng $g=\nabla\mathcal L$ và $F$ tính chính xác theo $\nu^\pi$" và phép tính hai lợi thế của dòng "Nhắc lại:". Các số nhiều chữ số của trang ($0{,}04344$, $(0{,}3475;\,1{,}3031)$, $0{,}0150$, $0{,}156$, $0{,}357$) không có trong ghi chú; ghi chú chỉ có $\Delta^*\approx(0{,}35;\,1{,}30)$, $p\approx(0{,}586;\,0{,}880)$, KL $\approx0{,}0085$, $J\approx1{,}807$: đề xuất NT3 ở §10.
- **Nguồn:** §5.1 (đoạn chuỗi: $F^{-1}g$, $10{,}6$, hệ số $0{,}0434$, $\Delta^*\approx(0{,}35;\,1{,}30)$, $J\approx1{,}807$); §5.2 (Thuật toán 10.37, bước 5–6); §4.3 (Ví dụ 10.12, "Hai mức thay đổi với mọi chính sách mới").
- **Nối vào:** `4-08`. **Nối ra:** `4-09`.
- **Phút:** 1,5.

#### `L10-4-09` · Thuật toán TRPO (1) (sửa một cụm từ ở bước 1)

- **Quyết định:** giữ chữ và ghi chú diễn giả (vừa sửa theo góp ý #1 của tác giả; TB31), trừ bước 1: "lưu $\log\pi_{\mathrm{old}}(A_t\mid S_t)$" thành "lưu $\log\pi_{\mathrm{old}}(A_t\mid S_t)$ và phân phối $\pi_{\mathrm{old}}(\cdot\mid S_t)$", khớp Thuật toán 10.37 bước 1 và khối **Thu lượt** của H13 (sau cổng storyboard). Số khối trong dòng nguồn không đổi (Thuật toán 10.37, 10.16).
- **Mục đích:** câu bài toán, đầu vào, đầu ra, bước 1–2 (thu lượt; $\delta_t$, $\widehat A_t$, $V^{\mathrm{targ}}_t$ có công thức).
- **Câu:** 5.
- **Diễn giả:** thêm một câu: KL ở bước 3 cần cả phân phối cũ tại mỗi trạng thái, không chỉ log-xác suất của hành động đã chọn.
- **Nguồn:** §5.2 (Thuật toán 10.37, bước 1–2; đoạn "Trong thực hành" sau thuật toán); §3.3 (Thuật toán 10.16).
- **Nối vào:** `4-25`. **Nối ra:** `4-26`.
- **Phút:** 1,5.

#### `L10-4-26` · Thuật toán TRPO (2) (giữ nguyên)

- **Quyết định:** giữ nguyên (góp ý #1). Bước 3 ($\rho_t$, $\widehat{\mathcal L}$, $\widehat D$, $g$, gradient liên hợp), "Lưu ý:" về $g^\gamma$, bước 4 (tìm kiếm lùi đủ điều kiện), bước 5 (mất mát của critic).
- **Mục đích:** các bước tính hướng, chọn độ dài và cập nhật critic.
- **Nguồn:** §5.2 (Thuật toán 10.36, 10.37; Nhận xét 10.38).
- **Nối vào:** `4-09`. **Nối ra:** `4-31`.
- **Phút:** 1.

#### `L10-4-31` · TRPO dự báo cục bộ, giới hạn thay đổi và đi theo hình học KL (thêm; cụm E; đề xuất 20, H14; trạm dừng cuối mạch)

- **Quyết định:** thêm, gộp với `5-09`. Đề xuất 20 có hai phần: "TRPO giải quyết gì" lên trang này (ba trực giác của đề xuất §11, H14); "còn khó khăn gì" là việc của `5-09` (TB27: mạch sau mở bằng điều mạch trước còn thiếu), nên trang này chỉ giữ một câu điều còn thiếu (TB5) và `5-09` bỏ câu liệt kê chi phí trùng (mục "Ảnh hưởng ngoài mạch 4").
- **Mục đích:** gom ba ý mang về của mạch và nêu điều còn thiếu.
- **Câu:** 5. **Nhãn:** hộp.
- **Mặt trang:**
  - Hình ba bảng, mỗi bảng một chú thích:
    - "Hàm thay thế: dự báo $J$ của chính sách mới từ lượt cũ, đúng đến bậc một."
    - "Miền tin cậy: chỉ tối ưu trong vùng $\bar D_{\mathrm{KL}}\le\kappa$, nơi dự báo còn đáng tin."
    - "Gradient tự nhiên: hướng tốt nhất theo hình học KL cục bộ."
  - "Trên chuỗi, một bước TRPO đưa $J$ từ $1{,}4$ lên $1{,}807$, với KL trung bình $0{,}0085\le\kappa$."
  - Hộp: "Mỗi bộ đệm chỉ cho một bước cập nhật, sau một lượt gradient liên hợp và một lượt tìm kiếm lùi."
- **Hình:** `ba-truc-giac.svg` (H14); mô tả ở §4.5. Chú thích là chữ HTML dưới mỗi bảng hoặc chữ trong SVG, không cả hai (TB10).
- **Dựng dần:** (0) hình và ba chú thích; (1) dòng chuỗi; (2) hộp.
- **1 phút:** TRPO dựng một mô hình dự báo từ dữ liệu cũ, giới hạn vùng mà mô hình còn đáng tin, và tìm bước tốt nhất trong vùng đó.
- **Mới:** không.
- **Nguồn số:** $1{,}807$, $0{,}0085$ từ `4-25`.
- **Diễn giả:** thông điệp xuyên suốt của đề xuất: TRPO không chỉ là gradient chính sách với bước nhỏ; nó dựng mô hình dự báo hiệu năng từ dữ liệu hiện có, giới hạn miền mà mô hình còn tương đối đáng tin, rồi tìm bước tốt nhất trong miền đó. So với định lý, TRPO thực hành thay năm điểm (Nhận xét 10.38), nên không bảo đảm $J$ tăng.
- **Nguồn:** §5.2 (đoạn kết "TRPO chọn từ một bộ đệm …"; Nhận xét 10.38).
- **Nối vào:** `4-26`. **Nối ra:** `5-00`, `5-09` (dùng lại một bộ đệm cho nhiều bước).
- **Phút:** 1.

**Ảnh hưởng ngoài mạch 4** (người dựng làm cùng lượt; mỗi chỗ ghi ở §10 khi làm):

| Chỗ | Việc |
|---|---|
| mạch 1, `1-08`, `so-do-neo-m1.svg` | không đổi: tên mạch 4, thẻ "mạch 4, 5" ở khối cập nhật, ghi chú diễn giả vẫn đúng |
| mạch 1, `1-06`, `1-05` | không đổi; `4-01` chỉ nhắc `1-05` bằng câu "bước dài theo ước lượng của một lượt cũ làm $J$ giảm" (ở `1-05`, $\widehat g$ ngược dấu gradient đúng), không dùng hình nhỏ của `1-06` |
| mạch 1, `1-07` (mục tiêu 3) | giữ nguyên (quyết định 4) |
| mạch 5, `5-09` | bỏ câu liệt kê chi phí TRPO ở đầu trang (đã là câu điều còn thiếu của `4-31`); câu mở mới "Cần dùng lại một bộ đệm $\mathcal D$ cho nhiều bước cập nhật, mỗi bước chỉ cần gradient bậc một của một hàm mục tiêu."; thêm hình `vong-trpo.svg` (H13), vòng tìm kiếm lùi màu đỏ (quyết định 2). Chi tiết ở mục `5-09` của §3 mạch 5 |
| mạch 5, `5-02`, `5-03` | dòng nguồn: Ví dụ 10.17 → 10.18; Ví dụ 10.18 → 10.19 |
| mạch 5, `5-00` | ghi chú diễn giả "Mạch trước cho TRPO …" giữ |
| mạch 6, `6-18` | ghi chú diễn giả: Định lý 10.26 → 10.27, Hệ quả 10.27 → 10.28; mặt trang giữ |
| mạch 6, `6-13` | giữ bốn hàng (quyết định 5); hàng "Chặn cải thiện" vẫn đúng ("như bổ đề"; Định lý 10.27 không cần điều kiện hỗ trợ) |
| mạch 6, `6-12`, `6-14` | không đổi |
| mạch 6, `6-15` | không đổi (câu 2 khớp `4-16`) |
| dòng nguồn mạch 4 | theo `doi-so-ghi-chu-2026-11-21.md`: mọi "§4.3" cũ (TV, KL) → §4.4; "§4.4" cũ (chặn cải thiện) → §4.6; "§4.5" cũ → §4.5 (bài toán) hoặc §4.6 (hệ quả); Mệnh đề 10.24 → 10.25, Bổ đề 10.25 → 10.26, Định lý 10.26 → 10.27, Hệ quả 10.27 → 10.28, Nhận xét 10.28 → 10.29, Hệ quả 10.29 → 10.30, Định nghĩa 10.30 → 10.24; Ví dụ 10.11 phần đoạn thẳng → Ví dụ 10.12; Ví dụ 10.12 cũ → 10.14. Dòng nguồn từng trang ở mục trên đã theo số mới |
| `outline.md` | bảng "Sáu mạch": mạch 4 28 trang, 37,5 phút, đầu ra thêm "luồng 100 lượt, bài toán miền tin cậy trước cơ sở lý thuyết, hình học elip"; tổng 87 trang. "Chuỗi định nghĩa → kết quả → phương pháp": thứ tự mới (bổ đề → hàm thay thế, tỉ số → sai số và đoạn thẳng → KL → miền tin cậy (Định nghĩa 10.24) → chặn cải thiện (Bổ đề 10.26, Định lý 10.27, Hệ quả 10.28, Mệnh đề 10.25) → Fisher, gradient tự nhiên → TRPO), số mới. "Phân loại chủ đề": tên mục `lec-10-topic-10` … `-14` theo §4.1–§4.6 mới; thêm `lec-10-topic-25` (§4.3 Sai số dự báo theo độ dài bước, cốt lõi; quyết định 6); biên tập viên sửa dòng 124 của `outline.md` (câu "Mã `lec-10-topic-25` … `-30` (DPO) chuyển sang Bài 13": mã `lec-10-topic-25` nay thuộc §4.3 Bài 10, các mục DPO lấy mã của Bài 13 khi dựng bài đó) và dòng 148 (phần lịch sử, dòng "Số hiệu (Q3, Q4)" ghi `lec-10-topic-25` … `-30` cho DPO: thêm chú thích mã đã dùng lại); `lec-10-topic-12` (§4.4) có thể đổi nhóm "cầu nối" → "cốt lõi" vì KL nay là thước đo trung tâm. "Quyết định ký hiệu": $\nu^\pi$ dùng từ `4-07` (bài toán miền tin cậy), không chỉ ở định lý; thêm $\pi_t$ (đoạn thẳng). Bảng thuật ngữ: "lấy mẫu quan trọng (importance sampling)", "bổ đề dịch chuyển phân bố chiếm dụng", "cực đại hóa qua hàm chặn dưới (minorize–maximize)" nếu chưa có |
| `exercises.md` | bảng `Mạch | Mở phần | Bài tập`: không đổi (mạch 4 vẫn mở tại `#/4/1`, trang `4-00` giữ mã) |

---

### Mạch 5. Tối ưu chính sách gần kề (PPO) (`id="mach-5"`, 14 trang, 17 phút + 3,5 bài tập)

Thứ tự: `5-00` → `5-09` → `5-10` → `5-01` → `5-02` → `5-11` → `5-03` → `5-05` → `5-06` → `5-07` → `5-14` → `5-08` → `5-12` → `5-13`. `5-07`/`5-14` là thuật toán PPO-Clip tách hai trang (góp ý tác giả #1). Mã bỏ: `5-04` (đồ thị $s_B$ với bộ đệm ba mẫu khác; #26: một bộ dữ liệu cho cả mạch). Mã mới: `5-09` … `5-13` (bài tập tổng hợp, Bài tập 10.23, chuyển từ `7-03`, `7-04` cũ). Ví dụ tay của PPO-Clip là `5-10`, `5-01`, `5-05`, đứng trước thuật toán `5-07` và mang cùng tên nhóm bước (Đ12). `5-10` và `5-01` là chuỗi dựng dần cùng bố cục (bảng bộ đệm thêm cột), tính một trang theo TB17. Một bộ đệm cho cả mạch; bài tập tổng hợp dùng lợi thế đúng, lý do nêu trên trang đề. Không dùng "Adam" trên mặt trang; không nhãn "Còn thiếu:".

Bộ đệm chung (kiểm trong `kiem_so.py`): hai lượt $s_A\xrightarrow1s_B\xrightarrow2$ ($G_0=0$, $G_1=0$) và $s_A\xrightarrow2$ ($G_0=1$); critic $\hat v=(1{,}4;\,1)$; $\lambda=1$; ba mẫu $(s_A,1)$, $(s_A,2)$, $(s_B,2)$ với $\widehat A=-1{,}4$; $-0{,}4$; $-1$ (lợi thế đúng $0{,}4$; $-0{,}4$; $-2$); $\rho_{s_A}(1)=2p_A$, $\rho_{s_A}(2)=2(1-p_A)$, $\rho_{s_B}(2)=3(1-p_B)$.

#### `L10-5-00` · Tối ưu chính sách gần kề (PPO) (trang tiêu đề mạch; điểm vào mạch 5; giữ mã; #6)

- **Mặt trang:** "5."; `h2` "Tối ưu chính sách gần kề (PPO)"; `p.strand-lead` "PPO cắt tỉ số chính sách để dùng lại một bộ đệm nhiều lần bằng gradient bậc một."
- **Hình:** `so-do-neo-m5-vao.svg`.
- **Diễn giả:** "Mạch trước cho TRPO: tối đa hàm thay thế trong miền KL, mỗi bộ đệm một bước, với ma trận Fisher, gradient liên hợp và tìm kiếm lùi. Mạch này giữ ý 'hàm thay thế chỉ đáng tin gần chính sách cũ' nhưng đưa giới hạn vào chính hàm mục tiêu. Đầu ra là PPO-Clip và so sánh với TRPO." **Phút:** 0,5.

#### `L10-5-09` · Mỗi bộ đệm của TRPO chỉ cho một bước cập nhật (mã mới; #26)

- **Câu:** 1 (mạch 5). **Nhãn:** "Câu hỏi:".
- **Mặt trang:**
  - Theo đề xuất TRPO (quyết định 2 của điều phối viên, 2026-11-21; đã dựng, xem §10 "Ghi chú khi dựng mạch 4"): câu "Mỗi vòng TRPO cần tích Fisher–vector, gradient liên hợp và tìm kiếm lùi, rồi bỏ bộ đệm sau một bước." bỏ khỏi mặt trang (trùng hộp điều còn thiếu của `4-31`); thay bằng hình `vong-trpo.svg` (H13, §4.5) nửa trái, vòng tìm kiếm lùi đỏ là chỗ nêu chi phí. Ghi chú diễn giả đọc hình: mỗi vòng cần khoảng mười tích $Fv$, một lượt tìm kiếm lùi, rồi bỏ bộ đệm.
  - "Cần dùng lại một bộ đệm $\mathcal D$ cho nhiều bước cập nhật, mỗi bước chỉ cần gradient bậc một của một hàm mục tiêu."
  - "Ứng viên trực tiếp là hàm thay thế mẫu, trung bình trên bộ đệm:" $$\mathcal L^{\mathrm{CPI}}(\theta)=\frac1{|\mathcal D|}\sum_{t\in\mathcal D}\rho_t(\theta)\,\widehat A_t,\qquad\rho_t(\theta)=\frac{\pi_\theta(A_t\mid S_t)}{\pi_{\mathrm{old}}(A_t\mid S_t)}.$$
  - "Câu hỏi: tối đa $\mathcal L^{\mathrm{CPI}}$ không ràng buộc trên một bộ đệm nhỏ thì chính sách đi tới đâu?"
- **Dựng dần:** (0) hình H13 và dòng bài toán; (1) công thức; (2) câu hỏi.
- **1 phút:** Muốn dùng lại bộ đệm với gradient thường thì phải tối đa một hàm mục tiêu tính trên bộ đệm; hàm thay thế mẫu là ứng viên đầu tiên.
- **Mới:** hàm thay thế mẫu $\mathcal L^{\mathrm{CPI}}$.
- **Nguồn số:** không.
- **Hình:** `vong-trpo.svg` (H13, mới; quyết định 2), khoảng 40% bề rộng.
- **Ghi chú nguồn:** đoạn mở §6; Định nghĩa 10.39 ($\mathcal L^{\mathrm{CPI}}$); đoạn "Trong thực hành" sau Mệnh đề 10.22.
- **Diễn giả:** $\mathcal L^{\mathrm{CPI}}$ là hàm thay thế của mạch 4 với kỳ vọng thay bằng trung bình trên bộ đệm và lợi thế thay bằng GAE, bỏ hằng $J(\theta_{\mathrm{old}})$; CPI là "lặp chính sách bảo thủ" (Kakade và Langford, 2002). Trung bình đều không có trọng số $\gamma^t$.
- **Phút:** 1,5.

#### `L10-5-10` · Bộ đệm hai lượt và lợi thế ước lượng (mã mới; #26; đầu chuỗi dựng dần với `5-01`)

- **Câu:** 2 (mạch 5). **Nhãn:** hộp.
- **Mặt trang:**
  - "Nhắc lại: critic $\hat v=(1{,}4;\,1)$ (mạch 3); GAE với $\lambda=1$ cho $\widehat A_t=G_t-\hat v(S_t)$; $\pi_{\mathrm{old}}=(\tfrac12;\,\tfrac23)$." (Đ1)
  - "**Thu lượt:** bộ đệm gồm hai lượt $s_A\xrightarrow1s_B\xrightarrow2$ và $s_A\xrightarrow2$, xác suất $2\cdot\tfrac16\cdot\tfrac12=\tfrac16$. **Ước lượng lợi thế:**" (Đ12)

    | Mẫu | $G_t$ | $\widehat A_t=G_t-\hat v(S_t)$ | $A_\pi$ đúng |
    |---|---|---|---|
    | $(s_A,1)$ | $0+0{,}9\cdot0=0$ | $0-1{,}4=$ **$-1{,}4$** (đỏ) | $+0{,}4$ |
    | $(s_A,2)$ | $1$ | $1-1{,}4=-0{,}4$ | $-0{,}4$ |
    | $(s_B,2)$ | $0$ | $0-1=-1$ | $-2$ |
  - Hộp: "Lợi thế ước lượng của hành động 1 ở $s_A$ sai dấu: lượt chọn nó gặp phần thưởng $0$ ở $s_B$."
- **Dựng dần:** (0) dòng bộ đệm, hình; (1) bảng; (2) hộp.
- **1 phút:** Bộ đệm nhỏ cho lợi thế ước lượng sai dấu ở hành động tốt, dù ước lượng với $\lambda=1$ không chệch.
- **Mới:** bộ đệm (một đối tượng, nguồn gốc nêu trên trang, TB25).
- **Nguồn số:** xác suất loại lượt $\tfrac16$, $\tfrac12$ từ `1-10` (hai thứ tự); critic từ `3-01`; GAE với $\lambda=1$ từ `3-08`(b); $A_\pi$ từ `2-06`.
- **Hình:** giữ `chuoi-bo-dem-hai-luot.svg` (lượt 1 nét liền, lượt 2 nét đứt, nhãn "thưởng 0", "thưởng 1"). Nửa trái nhỏ.
- **Ghi chú nguồn:** §6.1, đoạn "Hàm thay thế cũng chỉ đáng tin khi lợi thế được ước lượng tốt".
- **Diễn giả:** với $\lambda=1$, ước lượng tại $s_A$ không chệch vì $\hat v(s_A)=v_\pi(s_A)$; trên một bộ đệm nhỏ nó vẫn sai dấu ở một mẫu (phương sai, mạch 3).
- **Phút:** 1,5.

#### `L10-5-01` · Hàm thay thế mẫu tuyến tính theo tỉ số nên cực đại nằm ở biên (giữ mã; #26; tiêu đề theo E3)

- **Câu:** 2. **Nhãn:** hộp.
- **Mặt trang:**
  - Bảng của `5-10` thêm hai cột:

    | Mẫu | $\widehat A_t$ | $\rho_t$ theo $(p_A;\,p_B)$ mới | $\rho_t\widehat A_t$ |
    |---|---|---|---|
    | $(s_A,1)$ | $-1{,}4$ | $p_A/\tfrac12=2p_A$ | $-2{,}8p_A$ |
    | $(s_A,2)$ | $-0{,}4$ | $(1-p_A)/\tfrac12=2-2p_A$ | $-0{,}8+0{,}8p_A$ |
    | $(s_B,2)$ | $-1$ | $(1-p_B)/\tfrac13=3-3p_B$ | $-3+3p_B$ |
  - $$\mathcal L^{\mathrm{CPI}}=\tfrac13\bigl(-2{,}8p_A-0{,}8+0{,}8p_A-3+3p_B\bigr)=\tfrac13\bigl(-3{,}8-2p_A+3p_B\bigr).$$
  - Hộp: "$\mathcal L^{\mathrm{CPI}}$ tăng khi $p_A$ giảm và $p_B$ tăng, nên cực đại ở giới hạn $(p_A;\,p_B)=(0;\,1)$, tức $\theta_A\to-\infty$, $\theta_B\to+\infty$. Tại đó $J=2{,}7\cdot0\cdot1+1-0=1$: giảm $0{,}4$."
- **Dựng dần:** (0) cột $\rho_t$; (1) cột $\rho_t\widehat A_t$, công thức; (2) hộp.
- **1 phút:** Hàm thay thế mẫu tuyến tính theo tỉ số, nên không có gì giữ chính sách gần chính sách cũ; với lợi thế sai dấu, chính sách đi tới biên và $J$ giảm $0{,}4$.
- **Mới:** không (tính trên bộ đệm).
- **Nguồn số:** $\widehat A_t$ từ `5-10`; $\pi_{\mathrm{old}}=(\tfrac12;\,\tfrac23)$ từ `1-09`; $J$ theo `1-10`.
- **Hình:** không.
- **Ghi chú nguồn:** §6.1, cùng đoạn (dạng theo từng trạng thái; deck dùng trung bình trên ba mẫu, cùng nghiệm vì tham số tách theo trạng thái).
- **Diễn giả:** tại nghiệm, ba tỉ số là $0$; $2$; $0$, xa $1$, đúng vùng mà mạch 4 cho thấy hàm thay thế sai nhiều. Giới hạn $(0;\,1)$ không đạt được với $\theta$ hữu hạn; ghi rõ là giới hạn (TB25). Giảm $0{,}4$ trùng mức giảm của bước dài ở mạch 1.
- **Phút:** 2.

#### `L10-5-02` · Mục tiêu PPO-Clip (giữ mã; #26)

- **Câu:** 3 (mạch 5). **Nhãn:** "Định nghĩa.".
- **Mặt trang:**
  - "Hàm thay thế chỉ đáng tin khi chính sách mới gần chính sách cũ, tức khi mọi $\rho_t$ gần $1$. Mục tiêu cắt bỏ phần tăng của mục tiêu khi $\rho_t$ ra ngoài $[1-\epsilon,1+\epsilon]$ theo hướng có lợi, và giữ phần giảm theo hướng bất lợi."
  - "**Định nghĩa.** Với bán kính cắt $\epsilon\in(0,1)$ và $\operatorname{clip}(x,l,u)=\min(\max(x,l),u)$, mục tiêu PPO-Clip là" $$\mathcal L^{\mathrm{CLIP}}(\theta)=\frac1{|\mathcal D|}\sum_{t\in\mathcal D}\min\Bigl(\rho_t(\theta)\widehat A_t,\ \operatorname{clip}(\rho_t(\theta),1-\epsilon,1+\epsilon)\,\widehat A_t\Bigr).$$
- **Dựng dần:** (0) lý do; (1) định nghĩa; (2) hình `-buoc0`; (3) hình đủ.
- **1 phút:** Mỗi mẫu đóng góp giá trị nhỏ hơn giữa bản không cắt và bản đã cắt tỉ số.
- **Mới:** mục tiêu cắt.
- **Nguồn số:** không.
- **Hình:** giữ `ppo-cat-hai-dau-buoc0.svg`, `ppo-cat-hai-dau.svg` (hai khung theo $\rho$, $\widehat A>0$ và $\widehat A<0$, $\epsilon=0{,}2$, đoạn phẳng tô sọc). Kiểm nhãn: không có "đoán", "đi quá xa"; nhãn vùng sọc "gradient bằng $0$". Nửa dưới hoặc nửa phải.
- **Ghi chú nguồn:** đoạn trước Ví dụ 10.17; Định nghĩa 10.39; hình `ppo-clipping-signs.svg` của ghi chú (không dùng).
- **Diễn giả:** trực giác đến từ mạch 4 (tiếp xúc tại chính sách cũ, sai số tăng theo bình phương bước). Phép $\min$ làm mục tiêu cắt không vượt mục tiêu không cắt và trùng nó gần $\theta_{\mathrm{old}}$ (Mệnh đề 10.41, ghi chú).
- **Phút:** 1,5.

#### `L10-5-11` · Mục tiêu cắt theo dấu của lợi thế (mã mới; TB28)

- **Câu:** 3. **Nhãn:** "Mệnh đề.", "Chứng minh.".
- **Mặt trang:**
  - "**Mệnh đề.** Với $\epsilon\in(0,1)$, số hạng của mẫu $t$ là:"

    | | Số hạng | Gradient bằng $0$ khi |
    |---|---|---|
    | $\widehat A_t>0$ | $\widehat A_t\,\min(\rho_t,\,1+\epsilon)$ | $\rho_t>1+\epsilon$ |
    | $\widehat A_t<0$ | $\widehat A_t\,\max(\rho_t,\,1-\epsilon)$ | $\rho_t<1-\epsilon$ |
  - "Ngoài hai tập đó, gradient là $\widehat A_t\,\rho_t\,\psi_t$."
  - "Chứng minh. Nhân với $\widehat A_t>0$ giữ thứ tự và nhân với $\widehat A_t<0$ đảo thứ tự, nên phép $\min$ của định nghĩa thành $\min(\rho_t,1+\epsilon)$ hoặc $\max(\rho_t,1-\epsilon)$."
- **Dựng dần:** (0) mệnh đề và bảng; (1) dòng gradient; (2) chứng minh.
- **1 phút:** Mẫu có lợi thế dương ngừng đóng góp khi tỉ số vượt $1+\epsilon$, mẫu có lợi thế âm ngừng khi tỉ số dưới $1-\epsilon$; phía bất lợi không bị cắt.
- **Mới:** dạng theo dấu.
- **Nguồn số:** không.
- **Hình:** không.
- **Ghi chú nguồn:** Mệnh đề 10.40 (dòng "Chứng minh." gộp Bước 1 và Bước 2 của ghi chú); đoạn đọc bằng lời sau mệnh đề.
- **Diễn giả:** nhầm lẫn thường gặp: mọi mẫu ngoài khoảng cắt có gradient $0$; chỉ đúng khi tỉ số ra ngoài theo hướng có lợi. Tại $\rho_t=1\pm\epsilon$, vi phân tự động trả về gradient của một nhánh.
- **Phút:** 1.

#### `L10-5-03` · Câu hỏi nhanh: mẫu lợi thế âm với $\rho=1{,}3$ (giữ mã, số theo bộ đệm chung; TB22)

- **Câu:** 3. **Nhãn:** "Câu hỏi:", "Lời giải:".
- **Mặt trang:**
  - "Mẫu $(s_B,2)$ của bộ đệm: $\widehat A=-1$. Giả định sau vài bước trên các mẫu khác, $p_B$ đã giảm, $\rho=3(1-p_B)=1{,}3$, tức $p_B=1-\tfrac{1{,}3}3\approx0{,}57$. Giá trị $1{,}3$ được chọn ở phía bất lợi, ngoài khoảng cắt."
  - "Câu hỏi: với $\epsilon=0{,}2$, số hạng của mẫu có bị cắt không, và gradient làm $p_B$ thay đổi theo chiều nào?"
  - "Lời giải: $\min(-1\cdot1{,}3;\ -1\cdot1{,}2)=-1{,}3$, nhánh không cắt. Theo mệnh đề, $\widehat A<0$ chỉ có gradient $0$ khi $\rho<0{,}8$. Gradient khác $0$ làm $\rho$ giảm, tức làm $p_B$ tăng trở lại."
- **Dựng dần:** (0) dữ kiện, câu hỏi, hình câu hỏi; (1) lời giải, hình lời giải.
- **1 phút:** Khi tỉ số đi theo hướng bất lợi, mục tiêu cắt vẫn phạt đủ và gradient đưa chính sách về phía chính sách cũ.
- **Mới:** không.
- **Nguồn số:** $\widehat A=-1$ từ `5-10`; $\rho_{s_B}(2)=3(1-p_B)$ từ `5-01`; $1-1{,}3/3=0{,}5667$.
- **Hình:** sửa `ppo-cat-hai-dau-cau-hoi.svg`, `ppo-cat-hai-dau-loi-giai.svg`: khung $\widehat A<0$ với $\widehat A=-1$ (đoạn phẳng ở $-0{,}8$, đường dốc $-\rho$); điểm "?" đỏ tại $\rho=1{,}3$; bản lời giải: điểm nằm trên đường dốc, nhãn "$-1{,}3$", mũi tên về phía $\rho$ nhỏ.
- **Ghi chú nguồn:** Ví dụ 10.18 (mẫu $(-2;\,1{,}3)$ cùng cơ chế).
- **Diễn giả:** "Gợi ý: xác định dấu của $\widehat A$ rồi dùng dòng tương ứng của bảng." Năng lực kiểm tra: phân biệt phía có lợi và phía bất lợi của phép cắt.
- **Phút:** 2.

#### `L10-5-05` · Với phép cắt, $J$ chỉ giảm $0{,}008$ (giữ mã; #26)

- **Hiện hành (E1, E3):** dòng mở định nghĩa *vòng trong* tại chỗ ("*Vòng trong* gồm nhiều bước gradient tăng $\mathcal L^{\mathrm{CLIP}}$ trên cùng bộ đệm, lợi thế giữ cố định."); câu "mỗi số hạng là $\widehat A_t\max(\rho_t,0{,}8)$" xuống ghi chú diễn giả; bảng ba cột (Trạng thái, phần của $3\mathcal L^{\mathrm{CLIP}}$, vòng trong dừng tại); đoạn "Dưới $p_A=0{,}4$ …", phép tính $J=1{,}392$ và câu "Trên bộ đệm này, vòng trong dừng khi $\lvert\rho_t-1\rvert=\epsilon$ ở cả ba mẫu, $\rho=(0{,}8;\,1{,}2;\,0{,}8)$."; hộp "Phép cắt không sửa lợi thế ước lượng sai." cạnh hình. Mục cũ dưới đây giữ để đối chiếu.

- **Câu:** 4 (mạch 5). **Nhãn:** hộp.
- **Mặt trang:**
  - "**Cập nhật actor** (tối đa $\mathcal L^{\mathrm{CLIP}}$ trên cùng bộ đệm, $\epsilon=0{,}2$): cả ba $\widehat A_t<0$, nên mỗi số hạng là $\widehat A_t\max(\rho_t,\,0{,}8)$:" (Đ12)

    | Trạng thái | Phần của $3\,\mathcal L^{\mathrm{CLIP}}$ | Tăng khi | Dừng ở |
    |---|---|---|---|
    | $s_A$ | $-1{,}4\max(2p_A;\,0{,}8)-0{,}4\max(2-2p_A;\,0{,}8)$ | $p_A$ giảm từ $0{,}5$ | $p_A=0{,}4$, nơi $2p_A=0{,}8$ |
    | $s_B$ | $-\max(3-3p_B;\,0{,}8)$ | $p_B$ tăng từ $\tfrac23$ | $p_B=\tfrac{11}{15}\approx0{,}733$, nơi $3-3p_B=0{,}8$ |
  - "Dưới $p_A=0{,}4$, mẫu $(s_A,1)$ nằm trên đoạn phẳng. Mẫu $(s_A,2)$ có $\rho=2-2p_A>1{,}2$ ở phía bất lợi, không bị cắt, nên phần của $s_A$ là $-1{,}92+0{,}8p_A$, giảm khi $p_A$ giảm."
  - Hộp: "Vòng trong dừng ở $(0{,}4;\,\tfrac{11}{15})$: $J=2{,}7\cdot0{,}4\cdot\tfrac{11}{15}+0{,}6=1{,}392$, giảm $0{,}008$, thay cho $0{,}4$ khi không cắt."
  - "Trên chuỗi, mỗi trạng thái có tham số riêng, nên vòng trong dừng đúng ở đầu đoạn phẳng. Khi tham số dùng chung giữa các trạng thái, tỉ số có thể vượt khoảng cắt (trang sau)." (Đ2)
- **Dựng dần:** (0) dòng mở, hàng $s_A$ và panel trái của hình; (1) dòng "dưới $p_A=0{,}4$"; (2) hàng $s_B$ và panel phải; (3) hộp; (4) dòng phạm vi của chuỗi.
- **1 phút:** Phép cắt không sửa lợi thế sai, nhưng giới hạn mỗi vòng đi bao xa: $J$ chỉ giảm $0{,}008$.
- **Mới:** không (tính trên bộ đệm).
- **Nguồn số:** $\rho_t$, $\widehat A_t$ từ `5-01`; dạng theo dấu từ `5-11`; trên $[0{,}4;\,0{,}6]$ phần $s_A$ là $-0{,}8-2p_A$ ($-1{,}8$ tại $0{,}5$, $-1{,}6$ tại $0{,}4$); dưới $0{,}4$: $-1{,}4\cdot0{,}8-0{,}4(2-2p_A)=-1{,}92+0{,}8p_A$ ($-1{,}68$ tại $0{,}3$); $1-0{,}8/3=\tfrac{11}{15}$; $J=0{,}792+0{,}6$.
- **Hình:** mới `ppo-bo-dem-hai-luot.svg` (+ `-buoc0` chỉ panel trái): hai panel. Trái, trục $p_A\in[0;\,0{,}7]$: đường cam nét đứt "không cắt" $-0{,}8-2p_A$ (tức phần $s_A$ của $3\mathcal L^{\mathrm{CPI}}$), đường xanh nét liền "có cắt" gấp khúc ($-1{,}92+0{,}8p_A$ dưới $0{,}4$, $-0{,}8-2p_A$ trên $[0{,}4;\,0{,}6]$, $-2{,}8p_A-0{,}32$ trên $0{,}6$), cực đại tại $p_A=0{,}4$, chấm tím "$p_A=0{,}4$", mũi tên từ $p_A=0{,}5$ "chính sách cũ". Phải, trục $p_B\in[\tfrac23;\,1]$: đường cam nét đứt $-3+3p_B$, đường xanh $-\max(3-3p_B;\,0{,}8)$, đoạn phẳng từ $\tfrac{11}{15}$ tô sọc "gradient bằng $0$". Dải dưới bảng.
- **Ghi chú nguồn:** §6.1, đoạn "Trở lại bộ đệm hai lượt ở đầu mục"; đề xuất N9 nếu thiếu.
- **Diễn giả:** "dừng ở" là đầu đoạn phẳng, nơi gradient bằng $0$; deck không giả định bộ tối ưu nào. Phép cắt chỉ giới hạn bước của vòng này; vòng sau thu dữ liệu mới.
- **Phút:** 2.

#### `L10-5-06` · Giới hạn của phép cắt (giữ mã; #26)

- **Câu:** 4. **Nhãn:** "Nhận xét.".
- **Mặt trang:**
  - "**Nhận xét.** Trên đoạn phẳng, gradient bằng $0$: mục tiêu cắt không tạo gradient đưa tham số trở lại, và cũng không tạo gradient đẩy tiếp. Với bộ đệm chung, $p_A=0{,}4$:"

    | $p_B$ | Phần của $s_B$ | $D_{\mathrm{KL}}(s_B)$, chiều cũ‖mới | $J(0{,}4;\,p_B)$ |
    |---|---|---|---|
    | $\tfrac{11}{15}\approx0{,}733$ | $-0{,}8$ | $0{,}011$ | $1{,}392$ |
    | $0{,}85$ | $-0{,}8$ | $0{,}104$ | $1{,}518$ |
    | $0{,}95$ | $-0{,}8$ | $0{,}396$ | $1{,}626$ |
  - "1. Phép cắt không chặn KL: nếu các bước trên mẫu khác hoặc quán tính của bộ tối ưu đẩy $p_B$ vào đoạn phẳng, KL tăng mà mục tiêu không đổi."
  - "2. Phép cắt dừng cả bước làm $J$ tăng: $\partial J/\partial p_B=2{,}7p_A=1{,}08>0$."
- **Dựng dần:** (0) nhận xét và bảng; (1) ý 1; (2) ý 2.
- **1 phút:** Mục tiêu cắt phẳng nên không giữ được khoảng cách, và cũng dừng một bước tốt.
- **Mới:** không.
- **Nguồn số:** phần của $s_B$ từ `5-05`; $D_{\mathrm{KL}}(s_B)=\tfrac23\log\frac{2/3}{p_B}+\tfrac13\log\frac{1/3}{1-p_B}$ (công thức `4-12`); $J=1{,}08p_B+0{,}6$.
- **Hình:** không.
- **Ghi chú nguồn:** Nhận xét 10.42; đề xuất N9 (bảng KL trên bộ đệm chung).
- **Diễn giả:** các cài đặt PPO đo KL ước lượng trên bộ đệm (approxKL) và có thể dừng sớm khi vượt ngưỡng (Định nghĩa 10.47, Mệnh đề 10.48). Engstrom và cộng sự (2020): tỉ số vượt khoảng cắt trong thực hành. Trong thực hành tham số dùng chung giữa các trạng thái, nên một bước trên mẫu này đổi tỉ số của mẫu khác.
- **Phút:** 1,5.

#### `L10-5-07` · Thuật toán PPO-Clip (giữ mã; TB31, #26)

- **Câu:** 5 (mạch 5). **Nhãn:** "Thuật toán.", "Đầu vào:", "Đầu ra:".
- **Mặt trang:**
  - "PPO-Clip dùng lại mỗi bộ đệm cho nhiều bước gradient, với mục tiêu cắt thay ràng buộc KL."
  - "Đầu vào: $\pi_\theta$, critic $\hat v_w$; $\gamma$, $\lambda$, $\epsilon$; số lần qua bộ đệm $K$, cỡ lô nhỏ $M$, bước học. Đầu ra: $\theta$, $w$."
  - "Mỗi vòng lặp:"
    1. "**Thu lượt:** một bộ đệm $\mathcal D$ bằng $\pi_{\mathrm{old}}=\pi_\theta$; lưu $\log\pi_{\mathrm{old}}(A_t\mid S_t)$ và $\hat v_{\mathrm{old}}(S_t)$."
    2. "**Ước lượng lợi thế:** $\widehat A_t$ bằng GAE và mục tiêu của critic $\widehat A_t+\hat v_{\mathrm{old}}(S_t)$; giữ cố định trong cả vòng."
    3. "Lặp $K$ lần: xáo $\mathcal D$, chia lô nhỏ cỡ $M$; với mỗi lô, tính lại $\rho_t(\theta)$, rồi **Cập nhật actor:** một bước gradient tăng $\mathcal L^{\mathrm{CLIP}}$; **Cập nhật critic:** một bước gradient giảm $(\hat v(S_t,w)-\widehat A_t-\hat v_{\mathrm{old}}(S_t))^2$."
    4. "**Dừng sớm** (tùy chọn): bỏ các lần còn lại khi KL ước lượng trên bộ đệm vượt ngưỡng." (Đ12)
- **Dựng dần:** không.
- **1 phút:** Một bộ đệm, GAE một lần, rồi $K$ lần qua bộ đệm với mục tiêu cắt; chỉ cần gradient bậc một.
- **Mới:** thuật toán.
- **Nguồn số:** không (ví dụ tay: `5-10` thu lượt và ước lượng lợi thế, `5-05` cập nhật actor; cùng tên nhóm).
- **Hình:** không. Sơ đồ khung `so-do-neo-m5-ra*.svg` bỏ.
- **Ghi chú nguồn:** Thuật toán 10.49 (bản rút gọn: bỏ chuẩn hóa lợi thế, entropy và hệ số $c_1$, $c_2$ của Định nghĩa 10.46, ghi ở diễn giả); bảng "giữ cố định / tính lại" sau thuật toán.
- **Diễn giả:** cài đặt thường gộp hai bước của mục 3 thành một hàm mất mát tổng $-\mathcal L^{\mathrm{CLIP}}+c_1L^V-c_2\mathcal H$ và dùng bộ tối ưu Adam (Bài 08); thêm chuẩn hóa lợi thế trên lô. Từ lô thứ hai, dữ liệu đã khác chính sách; $\rho_t$ hiệu chỉnh phân phối hành động, phân bố trạng thái vẫn của $\pi_{\mathrm{old}}$. Chi phí: $K\lceil|\mathcal D|/M\rceil$ bước gradient mỗi bộ đệm.
- **Phút:** 2.

#### `L10-5-08` · So sánh TRPO và PPO (giữ mã; bỏ dòng dẫn sang DPO)

- **Câu:** 5. **Nhãn:** không.
- **Mặt trang:**

  | | TRPO | PPO-Clip |
  |---|---|---|
  | Quy tắc cập nhật | bước gradient tự nhiên (gradient liên hợp, tích Fisher–vector), tìm kiếm lùi | gradient bậc một của $\mathcal L^{\mathrm{CLIP}}$ trên lô nhỏ |
  | Dữ liệu dùng | một bộ đệm, một bước | một bộ đệm, $K$ lần |
  | Cách giữ bước gần | $\bar D_{\mathrm{KL}}\le\kappa$ | cắt tỉ số chính sách |
  | Bảo đảm | trên bộ đệm: KL mẫu $\le\kappa$, hàm thay thế mẫu tăng. $J$ tăng: không bảo đảm | không chặn KL; gradient $0$ khi tỉ số ra ngoài theo hướng có lợi. $J$ tăng: không bảo đảm |
- **1 phút:** Hai thuật toán cùng ý giữ bước gần, khác cách giữ và chi phí. Hai phương pháp đã trình bày riêng (`4-09`, `5-07`); bảng dùng cùng tiêu chí ở hàng cho cả hai (Đ3), và cùng tên cột với bảng phương pháp `6-14`.
- **Mới:** không. **Nguồn số:** không.
- **Hình:** không.
- **Ghi chú nguồn:** Nhận xét 10.38, Nhận xét 10.42; §7.2 của ghi chú (so sánh phương pháp).
- **Diễn giả:** cả hai dựa vào tính tiếp xúc của hàm thay thế và chặn cải thiện của mạch 4, nhưng các đại lượng đều là ước lượng, nên bảo đảm của định lý không chuyển sang thuật toán.
- **Phút:** 1.

#### `L10-5-12` · Bài tập: một vòng PPO-Clip trên chuỗi hai trạng thái (mã mới; thay `7-03`; #28, quyết định 3a; Bài tập 10.23)

- **Câu:** 5. **Nhãn:** "Câu hỏi:".
- **Mặt trang:**
  - "Để tách cơ chế cắt khỏi sai số ước lượng, bài dùng lợi thế đúng thay cho bộ đệm của mạch: $A_\pi(s_A,\cdot)=(0{,}4;\,-0{,}4)$, $A_\pi(s_B,\cdot)=(1;\,-2)$, giữ cố định. Tại mỗi trạng thái, mẫu có đúng tần suất hành động của $\pi=(\tfrac12;\,\tfrac23)$; $\eta_\pi=(1;\,0{,}45)$, $\epsilon=0{,}2$."
  - "Phần của mục tiêu cắt tại $s$: $\ell_s=\sum_a\pi(a\mid s)\min\bigl(\rho_s(a)A_\pi(s,a),\ \operatorname{clip}(\rho_s(a),0{,}8,1{,}2)A_\pi(s,a)\bigr)$."
  - "Câu hỏi: (a) Viết $\ell_{s_A}$ theo $p_A$, $\ell_{s_B}$ theo $p_B$, và tìm chính sách $\pi'$ nơi vòng trong dừng (đầu đoạn phẳng). (b) Tính $\Delta\mathcal L$ và $\Delta J$ của $\pi'$. (c) Tính $\sum_s\eta_\pi(s)\ell_s(\pi')$ và xếp ba số theo thứ tự tăng. (d) Giải thích vì sao $\Delta\mathcal L<\Delta J$."
- **1 phút:** Một vòng PPO-Clip với lợi thế đúng; bốn câu nối mục tiêu cắt, hàm thay thế và $J$ thật.
- **Mới:** không. **Nguồn số:** $A_\pi$ từ `2-06`; $\eta_\pi$ từ `4-16`.
- **Hình:** không.
- **Ghi chú nguồn:** Bài tập 10.23 (viết theo $\eta$, ghi chú viết theo $\nu^{\mathrm{old}}$ với $\tfrac1{1-\gamma}$).
- **Diễn giả:** lý do đổi dữ liệu (TB29): bài tập kiểm cơ chế cắt khi lợi thế đúng, tách khỏi sai số ước lượng của bộ đệm. Năng lực: dùng dạng theo dấu, hàm thay thế và công thức sai số trên một bài toán. "Gợi ý: tham số hai trạng thái tách nhau; tìm lúc từng nhóm mẫu chạm biên."
- **Phút:** 1,5.

#### `L10-5-13` · Bài tập: một vòng PPO-Clip trên chuỗi hai trạng thái, lời giải (mã mới; thay `7-04`)

- **Câu:** 5. **Nhãn:** "Lời giải:".
- **Mặt trang:** "Lời giải:"

  | | $s_A$ ($p_A\ge\tfrac12$) | $s_B$ ($p_B\ge\tfrac23$) |
  |---|---|---|
  | $\ell_s$ | $0{,}2\min(2p_A;\,1{,}2)-0{,}2\max(2-2p_A;\,0{,}8)$ | $\tfrac23\min(1{,}5p_B;\,1{,}2)-\tfrac23\max(3-3p_B;\,0{,}8)$ |
  | chạm biên | cả hai mẫu tại $p_A=0{,}6$ | hành động 2 tại $0{,}7\overline3$; hành động 1 tại $0{,}8$ |
  | dừng ở | $p'_A=0{,}6$ | $p'_B=0{,}8$ |
  | $A_\pi(s,\pi')$ | $0{,}6\cdot0{,}4-0{,}4\cdot0{,}4=0{,}08$ | $0{,}8\cdot1-0{,}2\cdot2=0{,}4$ |
  | $\ell_s(\pi')$ | $0{,}24-0{,}16=0{,}08$ | $0{,}8-0{,}5\overline3=0{,}2\overline6$ |

  - "(b) $\Delta\mathcal L=0{,}08+0{,}45\cdot0{,}4=0{,}26$; $\Delta J=2{,}7\cdot0{,}6\cdot0{,}8+0{,}4-1{,}4=0{,}296$. (c) $0{,}08+0{,}45\cdot0{,}2\overline6=0{,}2$; thứ tự $0{,}2<0{,}26<0{,}296$."
  - "(d) Sai số $2{,}7\,\Delta p_A\Delta p_B=2{,}7\cdot0{,}1\cdot\tfrac2{15}=0{,}036>0$: $\pi'$ thăm $s_B$ nhiều hơn và tại $s_B$ tốt hơn $\pi$."
- **Dựng dần:** (0) hàng $\ell_s$; (1) hai hàng chạm biên, dừng ở; (2) hai hàng cuối; (3) (b), (c); (4) (d).
- **1 phút:** Vòng trong dừng ở $(0{,}6;\,0{,}8)$; mục tiêu cắt $<$ hàm thay thế $<$ mức tăng thật.
- **Mới:** không.
- **Nguồn số:** tỉ số $\rho_{s_A}=(2p_A;\,2-2p_A)$, $\rho_{s_B}=(1{,}5p_B;\,3-3p_B)$; công thức sai số từ `4-05`; mọi ô có phép tính.
- **Hình:** không.
- **Ghi chú nguồn:** Bài tập 10.23, lời giải (a)–(d).
- **Diễn giả:** hai lỗi thường gặp: dừng ở $p_B=0{,}7\overline3$ khi chỉ mẫu hành động 2 chạm biên; bỏ phép cắt thì $\ell_{s_B}=3p_B-2$ tăng mãi. Ở đây hàm thay thế dự báo thấp hơn mức tăng thật vì sai số dương; ở `4-16` nó dự báo sai dấu vì sai số âm và lớn. Cùng một công thức sai số giải thích cả hai.
- **Phút:** 2.

---

### Mạch 6. Tổng kết (`id="mach-6"`, 10 trang, 11 phút)

Thứ tự: `6-00` → `6-10` → `6-11` → `6-18` → `6-12` → `6-13` → `6-14` → `6-15` → `6-16` → `6-17`. Mã mới `6-18` (E1: câu trả lời câu 2 tách khỏi `6-11` để vừa khung). Mã cũ `7-00` … `7-07` bỏ (đổi tiền tố); `7-03`, `7-04` chuyển thành `5-12`, `5-13`. Không có số của ví dụ trên mặt trang (#28, TB32); không khái niệm mới.

#### `L10-6-00` · Tổng kết (trang tiêu đề mạch; điểm vào mạch 6)

- **Mặt trang:** "6."; `h2` "Tổng kết"; `p.strand-lead` "Mỗi phương pháp của bài giảm phương sai hoặc giới hạn bước cập nhật dưới những giả thiết riêng."
- **Hình:** `so-do-neo-tong-ket-vao.svg`.
- **Diễn giả:** "Năm mạch trước sửa hai khối của vòng cập nhật: hệ số của mỗi bước và bước cập nhật. Mạch này gom các kết luận, mỗi kết luận kèm giả thiết quyết định, và so bốn phương pháp." **Phút:** 0,5.

#### `L10-6-10` · Vòng cập nhật chính sách sau năm mạch (thay `7-01`; #28)

- **Mặt trang:** sơ đồ neo cuối, tên khối trùng tên nhóm bước của ba trang thuật toán (Đ12), dựng dần ba bước: (0) "**Thu lượt** bằng chính sách cũ" và khối liền "**Cập nhật critic**: $\hat v$" (thay khối nét đứt); (1) "**Ước lượng lợi thế** (hệ số của mỗi bước): $G_t\ \to\ G_t-v_\pi(S_t)\ \to\ \delta_t\ \to\ \widehat A_t$ (GAE)", nhãn "mạch 2, 3"; (2) "**Cập nhật actor**: một bước gradient → tối đa hàm thay thế trong miền tin cậy (TRPO) → tối đa mục tiêu cắt, $K$ lần qua bộ đệm (PPO)", nhãn "mạch 4, 5", mũi tên "dùng lại lượt vừa thu". Dòng chú thích dưới hình: "Ví dụ chung: chuỗi hai trạng thái." Không số, không khối phần thưởng (Đ13).
- **1 phút:** Khối hệ số và khối cập nhật đã được thay; mỗi công cụ có tên trên sơ đồ.
- **Hình:** `so-do-neo-tong-ket-buoc0.svg`, `-buoc1.svg`, `so-do-neo-tong-ket.svg` (sửa từ `so-do-neo-m7*.svg`: bỏ khối "Phần thưởng", bỏ mọi dòng số "$0{,}69\to0{,}20\to0$", "$+0{,}175$, $-0{,}05$", "dừng ở $p=0{,}8$", bỏ dòng $\pi^*$ và mũi tên DPO, đổi tên tệp).
- **Diễn giả:** đọc vòng lần cuối; mỗi mũi tên "→" là một mạch. **Phút:** 1,5.

#### `L10-6-11` · Vấn đề trung tâm (thay `7-02`; #28, TB32; dựng lại theo E1, G2)

- **Nhãn:** "Câu hỏi:" (khung, danh sách đánh số hai câu như `1-06`); dòng "Trả lời câu 1:" (chữ thường, không phải nhãn NT19); câu trả lời dùng `<ul>` để số không trùng số câu hỏi (G2).
- **Mặt trang:** khung "Câu hỏi:"; "Trả lời câu 1:":
  - "Trừ một đường cơ sở chỉ phụ thuộc trạng thái giữ nguyên kỳ vọng của ước lượng gradient, và trên ví dụ chung phương sai giảm."
  - "Khi $\hat v\ne v_\pi$, sai số TD là ước lượng chệch của lợi thế. GAE cân bằng độ chệch và phương sai bằng $\lambda$, cho ước lượng gradient không chệch khi $\lambda=1$ trên lượt đầy đủ hoặc $\hat v=v_\pi$."
- **1 phút:** Câu 1 có hai câu trả lời (đường cơ sở, GAE), mỗi câu trả lời kèm điều kiện.
- **Ngoại lệ:** câu "Với $b=v_\pi$, hệ số có kỳ vọng có điều kiện bằng lợi thế." ở ghi chú diễn giả (vừa khung); dòng ví dụ chung ở `6-18`; mật độ > 80 âm tiết, mục 7.
- **Ghi chú nguồn:** §7.3. **Diễn giả:** điều kiện của từng câu trả lời; Mệnh đề 10.2, 10.5; 10.8, 10.14, 10.15. **Phút:** 1.

#### `L10-6-18` · Vấn đề trung tâm: trả lời câu 2 (mã mới; E1, tách từ `6-11`; G2)

- **Nhãn:** "Nhắc lại:" (câu 2); dòng "Trả lời câu 2:"; `<ul>`.
- **Mặt trang:** nhắc câu 2; hai mục:
  - "Hàm thay thế tính được từ lượt của chính sách cũ và tiếp xúc $J$ tại chính sách cũ. Khi lợi thế và số lần thăm tính chính xác, $J$ không giảm nếu mức tăng của hàm thay thế vượt phạt tỉ lệ với kỳ vọng khoảng cách TV, hoặc với căn của KL trung bình. Thừa số của phạt là $2\gamma\chi_{\pi'}/(1-\gamma)^2$."
  - "TRPO giữ KL trung bình mẫu trên bộ đệm không vượt $\kappa$. PPO dùng lại bộ đệm $K$ lần, cắt tỉ số chính sách và không chặn KL. Với lợi thế ước lượng, cả hai đều có thể làm $J$ giảm."
  Dòng cuối "Ví dụ chung của bài là chuỗi hai trạng thái." (Đ13).
- **1 phút:** Câu 2 có hai câu trả lời (hàm thay thế và cận; TRPO và PPO), mỗi câu kèm điều kiện.
- **Ghi chú nguồn:** §7.3. **Diễn giả:** Mệnh đề 10.22, Định lý 10.26, Hệ quả 10.27; Thuật toán 10.37, 10.49, Nhận xét 10.38, 10.42. **Phút:** 1.

#### `L10-6-12` · Kết quả và giả thiết (1) (thay một phần `7-02`; CLAUDE.md "Conclusion strand", P4)

- **Mặt trang:** bảng `Kết quả | Giả thiết không được bỏ | Công thức hoặc thuật toán`, phần giảm phương sai:

  | Kết quả | Giả thiết không được bỏ | Công thức hoặc thuật toán |
  |---|---|---|
  | Đường cơ sở không làm chệch | $b$ không phụ thuộc hành động đã chọn; lượt sinh bởi $\pi_\theta$ | $\mathbb E\bigl[\sum_t\gamma^t(G_t-b(S_t))\psi_t\bigr]=\nabla J$ |
  | Gradient dạng lợi thế | lợi thế của chính $\pi_\theta$; tính Markov | $\nabla J=\mathbb E\bigl[\sum_t\gamma^tA_\pi(S_t,A_t)\psi_t\bigr]$ |
  | Sai số TD và lợi thế | giá trị đúng $v_\pi$; điều kiện theo $(S_t,A_t)$ | $\mathbb E[\delta_t\mid S_t,A_t]=A_\pi(S_t,A_t)$ |
  | GAE và gradient | $\lambda=1$ trên lượt đầy đủ, hoặc $\hat v=v_\pi$ | $\widehat A_t=\sum_k(\gamma\lambda)^k\delta_{t+k}$; $\mathbb E[\sum_t\gamma^t\widehat A_t\psi_t]=\nabla J$ |
- **Ghi chú nguồn:** §7.1. **Diễn giả:** mỗi giả thiết bỏ đi đều có phản ví dụ trên chuỗi (trừ $q_\pi$ cho kỳ vọng $0$; critic sai với $\lambda=0$ cho tọa độ âm). **Phút:** 1.

#### `L10-6-13` · Kết quả và giả thiết (2)

- **Mặt trang:** cùng bảng, phần giới hạn bước:

  | Kết quả | Giả thiết không được bỏ | Công thức hoặc thuật toán |
  |---|---|---|
  | Bổ đề chênh lệch hiệu năng | cùng $P$, cùng $\mu_0$; $\gamma<1$ | $J(\pi')-J(\pi)=\sum_s\eta_{\pi'}(s)A_\pi(s,\pi')$ |
  | Hàm thay thế tiếp xúc $J$ | $\eta_\pi$, $A_\pi$ chính xác; $\pi>0$ | $\mathcal L_\pi(\pi)=J(\pi)$, $\nabla\mathcal L=\nabla J$ tại $\pi$ |
  | Chặn cải thiện | như bổ đề; điều kiện hỗ trợ | $\Delta J\ge\Delta\mathcal L-\frac{2\gamma\chi}{(1-\gamma)^2}\mathbb E_{\nu^\pi}[D_{\mathrm{TV}}]$, hoặc $\sqrt{\tfrac12\bar D_{\mathrm{KL}}}$ thay $\mathbb E_{\nu^\pi}[D_{\mathrm{TV}}]$ |
  | Mục tiêu cắt | lợi thế cố định trong vòng | gradient $0$ khi $\widehat A>0,\rho>1+\epsilon$ hoặc $\widehat A<0,\rho<1-\epsilon$ |
- **Ghi chú nguồn:** §7.1. **Diễn giả:** "chính xác" là điều kiện áp dụng; mọi thuật toán thay nó bằng ước lượng. **Phút:** 1.

#### `L10-6-14` · So sánh các phương pháp (TB32; #28)

- **Mặt trang:**

  | Phương pháp | Quy tắc cập nhật | Dữ liệu dùng | Cách giữ bước gần | Bảo đảm |
  |---|---|---|---|---|
  | REINFORCE | $\theta\leftarrow\theta+\alpha\sum_t\gamma^tG_t\psi_t$ | một lượt, một lần | bước học nhỏ | ước lượng gradient không chệch |
  | Actor–critic với GAE | $\theta\leftarrow\theta+\alpha_\theta\sum_t\gamma^t\widehat A_t\psi_t$; critic về $\widehat A_t+\hat v_{\mathrm{old}}$ | một lượt, một lần | bước học nhỏ | không chệch khi $\lambda=1$ hoặc critic đúng |
  | TRPO | bước gradient tự nhiên (gradient liên hợp, tích Fisher–vector), tìm kiếm lùi | một bộ đệm, một bước | $\bar D_{\mathrm{KL}}\le\kappa$ | trên bộ đệm: KL mẫu $\le\kappa$, hàm thay thế mẫu tăng. $J$ tăng: không bảo đảm |
  | PPO-Clip | gradient bậc một của $\mathcal L^{\mathrm{CLIP}}$ trên lô nhỏ | một bộ đệm, $K$ lần | cắt tỉ số chính sách | không chặn KL; gradient $0$ khi tỉ số ra ngoài theo hướng có lợi. $J$ tăng: không bảo đảm |
- **1 phút:** Bốn phương pháp khác nhau ở dữ liệu dùng và cách giữ bước gần; không phương pháp nào trong thực hành bảo đảm $J$ tăng.
- **Ghi chú nguồn:** §7.2 (bảng phương pháp và bảng bảo đảm). **Diễn giả:** điều kiện dừng của cả bốn là ngân sách (số lượt, số vòng). **Phút:** 1,5.

#### `L10-6-15` · Câu hỏi tự kiểm tra (thay `7-05`; #28, NT-RL-9)

- **Mặt trang:** "Câu hỏi: trả lời và nêu kết quả đã dùng." Ba câu khái niệm, một câu vận dụng sang tình huống mới (Đ13): 1. "Vì sao đường cơ sở không được phụ thuộc hành động đã chọn?" 2. "Vì sao hàm thay thế sai khi chính sách mới thăm các trạng thái với tần suất khác chính sách cũ?" 3. "Phép cắt tỉ số có chặn KL giữa chính sách mới và chính sách cũ không?" 4. "Một môi trường có giới hạn thời gian, nên nhiều lượt bị cắt ngắn ở biên đoạn thu. Với critic sai, GAE với $\lambda=1$ còn cho ước lượng gradient không chệch không?"
- **Ghi chú nguồn:** §7.4 (bản định tính). **Diễn giả (lời giải ngắn):** (1) mệnh đề đường cơ sở cần $\mathbb E[b\psi_t\mid H_t]=0$; trừ $q_\pi(S_t,A_t)$ làm kỳ vọng thành $0$. (2) bổ đề chênh lệch hiệu năng cần số lần thăm của chính sách mới; sai số là $\sum_s(\eta_{\pi'}-\eta_\pi)A_\pi(s,\pi')$. (3) không (nhận xét về phép cắt); đoạn phẳng có gradient $0$, không lực kéo về. (4) không: mệnh đề GAE và gradient cần lượt đầy đủ; lượt bị cắt bootstrap từ $\hat v$ sai ở biên, nên ước lượng chệch kể cả khi $\lambda=1$ (ghi chú, đoạn sau Mệnh đề 10.15: cắt ở $s_B$ cho $-0{,}025$ thay cho $0{,}2$; Nhận xét 10.17). **Phút:** 1,5.

#### `L10-6-16` · Bài tập về nhà (thay `7-06`)

- **Mặt trang:** bảng `Mạch | Bài tập`:

  | Mạch | Bài tập |
  |---|---|
  | 1. Giới hạn của REINFORCE | 10.22 |
  | 2. Đường cơ sở và hàm lợi thế | ghi chú: 10.1, 10.4, 10.10 |
  | 3. Ước lượng lợi thế: độ chệch và phương sai | 10.13, 10.15; ghi chú: 10.5, 10.6, 10.7 |
  | 4. Hàm thay thế và miền tin cậy | 10.16, 10.17; ghi chú: 10.8, 10.9, 10.11 |
  | 5. Tối ưu chính sách gần kề (PPO) | 10.14; ghi chú: 10.2, 10.3, 10.12, 10.23 |
  "Ghi chú bài giảng · Bài tập" (liên kết trình xem `material-viewer.html?doc=materials/lec-10/lecture-note.md&deck=lecture-10-trpo-va-ppo.html` và `...exercises.md...`).
- **Ghi chú nguồn:** §7.5; bảng mở đầu `exercises.md`. **Diễn giả:** mỗi bài đặt ở mạch cung cấp kiến thức cuối cùng nó cần: 10.22 (softmax hai hành động là hàm logistic) dùng tham số hóa của mạch 1; 10.5 (độ chệch của sai số TD khi critic sai) cần critic của mạch 3; 10.23 là bài tổng hợp đã giải trên trang `5-12`, `5-13`. Số 10.18–10.21 bỏ trống (BT4). Bảng mở đầu `exercises.md` hiện đặt 10.5 ở mạch 2; cần sửa theo bảng này. **Phút:** 1.

#### `L10-6-17` · Tài liệu tham khảo (thay `7-07`)

- **Mặt trang:** Sutton, R. S., Barto, A. G. *Reinforcement Learning: An Introduction*, ấn bản 2, 2018, §7.1, §12.1–12.3, §13.4–13.5. Kakade, S., Langford, J. Approximately Optimal Approximate Reinforcement Learning, 2002. Schulman và cộng sự. Trust Region Policy Optimization, 2015; High-Dimensional Continuous Control Using Generalized Advantage Estimation, 2016; Proximal Policy Optimization Algorithms, 2017. Achiam và cộng sự. Constrained Policy Optimization, 2017. Engstrom và cộng sự. Implementation Matters in Deep Policy Gradients, 2020. Tạ Việt Cường. Bài giảng 10, học phần AIT3007, 2025–2026. "Bài tiếp theo: [Bài 11, Lập kế hoạch dựa trên mô hình](lecture-11-lap-ke-hoach-dua-tren-mo-hinh.html)." Bỏ Christiano, Ouyang, Rafailov (DPO, #27).
- **Phút:** 0,5.

---

## 4. Danh sách hình (`2627-1/img/lec-10/`)

Nhãn ≥ 20 px trên ảnh 1600×900; màu theo quy ước đầu tệp, luôn kèm nét hoặc nhãn; `role="img"` và `alt` mô tả đủ số trên hình; không nhãn "đoán/thật", "đi quá xa", "nơi chính sách tới".

### 4.1 Giữ nguyên

| Tệp | Trang |
|---|---|
| `gae-tinh-lui-buoc0.svg`, `gae-tinh-lui-buoc1.svg`, `gae-tinh-lui.svg` | `3-08` |
| `elip-gradient-tu-nhien-buoc1.svg`, `elip-gradient-tu-nhien.svg` | `4-08` |
| `ppo-cat-hai-dau-buoc0.svg`, `ppo-cat-hai-dau.svg` | `5-02` (kiểm nhãn vùng sọc "gradient bằng $0$") |
| `chuoi-bo-dem-hai-luot.svg` | `5-10` |

### 4.2 Sửa

| Tệp | Trang | Sửa gì |
|---|---|---|
| `so-do-neo-m1.svg` | `1-08` | bỏ khối "Phần thưởng" và thẻ "mạch 6"; bỏ cột mạch 6, 7; cột phải ghi mạch 2–6 đúng tên mục 1; "? dao động" → "? phương sai lớn"; thẻ "mạch 2" ở khối hệ số, "mạch 3" ở khối nét đứt và khối hệ số, "mạch 4, 5" ở khối cập nhật |
| `so-do-neo-m2-vao.svg` | `2-00` | bỏ khối "Phần thưởng"; giữ "Hệ số: $G_t$ ?" tô tím |
| `so-do-neo-m3-vao.svg` | `3-00` | bỏ "Phần thưởng"; khối hệ số ghi "$G_t-v_\pi(S_t)$, $\delta_t$ với $v_\pi$"; khối nét đứt tô tím "$v_\pi$ chưa biết ?" (không chữ "critic" trước mạch 3) |
| `so-do-neo-m4-vao.svg` | `4-00` | bỏ "Phần thưởng"; khối liền "Cập nhật critic: $\hat v$"; "Ước lượng lợi thế: $\widehat A_t$ (GAE)"; khối cập nhật tô tím "?" (tên khối theo Đ12) |
| `so-do-neo-m5-vao.svg` | `5-00` | bỏ "Phần thưởng"; tên khối như `m4-vao`; khối cập nhật "Cập nhật actor: tối đa hàm thay thế trong miền tin cậy (TRPO) ?" tô tím; giữ mũi tên mờ "Thu lượt" → "Cập nhật actor", nhãn "dùng lại lượt vừa thu" (như mục 2) |
| `so-do-neo-m7-vao.svg` → đổi tên `so-do-neo-tong-ket-vao.svg` | `6-00` | bỏ "Phần thưởng", bỏ mũi tên DPO, bỏ mọi số |
| `so-do-neo-m7-buoc0.svg`, `-buoc1.svg`, `so-do-neo-m7.svg` → `so-do-neo-tong-ket-buoc0.svg`, `-buoc1.svg`, `so-do-neo-tong-ket.svg` | `6-10` | bỏ khối "Phần thưởng", dòng $\pi^*$, mũi tên DPO; bỏ ba dòng số ("phương sai 0,69 → 0,20 → 0", "hàm thay thế đoán +0,175, thật −0,05", "dừng ở p = 0,8"); tên khối **Thu lượt**, **Cập nhật critic**, **Ước lượng lợi thế**, **Cập nhật actor** (Đ12); nội dung khối như `6-10`; chú thích "Ví dụ chung: chuỗi hai trạng thái"; ba bước dựng dần theo `6-10` |
| `chuoi-loi-the.svg` | `2-06` | thêm "$v_\pi=1{,}4$", "$v_\pi=2$" dưới hai ô; nhãn cung "$q_\pi=\dots$, $A_\pi=\dots$" (#13) |
| `chuoi-critic-sai.svg` | `3-01` | ghi $\hat v$ và $v_\pi$ ở cả hai trạng thái (#18) |
| `chuoi-ti-le-toi-sB-buoc0.svg`, `chuoi-ti-le-toi-sB.svg` | `4-01` | thanh chính sách mới thành "$\tilde\pi$: $0{,}9$" (thay $1$); nhãn "tại $s_B$: $\tilde p_B=0{,}5<\tfrac23$" |
| `ham-thay-the-tiep-xuc-buoc0.svg`, `-buoc1.svg`, `ham-thay-the-tiep-xuc.svg` | `4-04` | $\Delta\mathcal L=0{,}095t$, $\Delta J=0{,}095t-0{,}18t^2$; điểm $t=1$: $+0{,}095$, $-0{,}085$; nhãn dưới trục "$\pi$", "$\tilde\pi=(0{,}9;\,0{,}5)$"; nhãn đường "hàm thay thế", "giá trị thật"; bỏ điểm $t=0{,}4$ |
| `ham-thay-the-mien-tin-cay-buoc0.svg`, `ham-thay-the-mien-tin-cay.svg` | `4-07` | hai đường mới như `4-04`; dải $t\le0{,}515$ "miền tin cậy, $\kappa=0{,}01$"; nhãn tại $t=1$ "$\tilde\pi$: $\bar D_{\mathrm{KL}}=0{,}054$" (bỏ "KL ở $s_A$ vô hạn") |
| `ppo-cat-hai-dau-cau-hoi.svg`, `ppo-cat-hai-dau-loi-giai.svg` | `5-03` | $\widehat A=-1$ (thay $-2$): đoạn phẳng ở $-0{,}8$, điểm $\rho=1{,}3$ giá trị $-1{,}3$ |
| `img/lec-10/central-problem.svg` (hình của ghi chú) | ghi chú §1.1 | bỏ hàng thứ ba (DPO, phần thưởng từ so sánh ưu tiên); giữ hai hàng (giảm phương sai; giới hạn bước cập nhật) gặp nhau ở PPO; sửa `alt` và đoạn đọc hình của ghi chú theo (người sửa ghi chú làm hoặc điều phối viên giao) |

### 4.3 Mới

| Tệp | Trang | Mô tả |
|---|---|---|
| `chuoi-hai-trang-thai-buoc0.svg`, `chuoi-hai-trang-thai.svg` | `1-09`, `1-10` (thu nhỏ) | mô tả ở `1-09`; không giá trị, không chữ đỏ |
| `reinforce-truc-so-buoc0.svg` … `-buoc3.svg`, `reinforce-truc-so.svg` | `1-04` | **trục đứng** bên phải bảng (đổi ở cổng storyboard); chấm $1{,}35$, $0$, $-0{,}5$ hiện cùng hàng bảng; vạch ngang kỳ vọng $0{,}2$; vùng dưới $0$ "ngược dấu gradient" |
| `reinforce-truc-so-nho.svg` | `1-06` | bản thu nhỏ (trục đứng), chú thích "phương sai lớn" |
| `buoc-dai-mot-luot.svg` | `1-05` | $J=1+0{,}8\,\sigma(-0{,}5\alpha)$ theo $\alpha\in[0,8]$; điểm $\alpha=1,2$; tiệm cận $1$ |
| `buoc-dai-mot-luot-nho.svg` | `1-06` | bản thu nhỏ, chú thích "bước dài làm $J$ giảm" |
| `truc-so-loi-tuc-buoc0.svg`, `truc-so-loi-tuc.svg` | `2-01` | lợi tức $0$, $1$, $2{,}7$ với xác suất; vạch $v_\pi(s_A)=1{,}4$; mũi tên $G_0-1{,}4$; hai vùng "kém hơn / tốt hơn mức kỳ vọng" |
| `sai-so-td-mot-buoc.svg` | `2-07` | hai cung từ $s_A$ với $\delta_0=\pm0{,}4=A_\pi(s_A,\cdot)$; không actor, critic |
| `ham-thay-the-tiep-xuc-cau-hoi.svg`, `ham-thay-the-tiep-xuc-loi-giai.svg` | `4-10` | từ `ham-thay-the-tiep-xuc.svg`: "?" tại $t=0{,}25$; lời giải hai điểm $0{,}024$, $0{,}0125$ |
| `ppo-bo-dem-hai-luot-buoc0.svg`, `ppo-bo-dem-hai-luot.svg` | `5-05` | hai panel $s_A$, $s_B$: mục tiêu không cắt và có cắt trên bộ đệm chung; cực đại $p_A=0{,}4$; đoạn phẳng $p_B\ge\tfrac{11}{15}$ |
| `gae-weights-trang.svg` | `3-02` | trọng số GAE với $\lambda=0{,}5$, $\gamma=0{,}9$ (mô tả ở `3-02`); thay việc dùng lại `gae-weights.svg` |

### 4.4 Bỏ khỏi deck

`hanh-lang-*.svg` (11 tệp); `chuoi-gia-tri.svg` (in sẵn kết luận, #7); `critic-mot-buoc.svg` (actor/critic ở mạch 2, #15); `so-do-neo-m2-ra.svg`, `so-do-neo-m3-ra.svg`, `so-do-neo-m4-ra*.svg` (5 tệp), `so-do-neo-m5-ra*.svg` (2 tệp) (trạm dừng không đặt sơ đồ cạnh bảng tính, #16; thuật toán thành danh sách, TB31); `so-do-neo-m6-*.svg` (5 tệp, DPO); `so-do-neo-m7*.svg` (đổi tên, mục 4.2); `ppo-sB-do-thi*.svg` (4 tệp) và `ppo-sB-do-thi-kl*.svg` (2 tệp) (bộ đệm khác, #26); `bradley-terry-sigmoid*.svg` (3), `dpo-cac-buoc*.svg` (2), `loi-nhac-hai-cau-tra-loi*.svg` (2), `nghiem-phat-kl-cot*.svg` (3), `phat-kl-duong-J1*.svg` (3), `rlhf-dpo-hai-con-duong.svg` (DPO). Hình của ghi chú (`two-state-chain.svg`, `actor-critic-advantage.svg`, `policy-update-feedback.svg`, `ppo-clipping-signs.svg`, `ppo-one-step-plateau.svg`, các tệp `gae-*` khác) không lên deck nhưng ghi chú còn dùng, không xóa.

### 4.5 Mạch 4 theo đề xuất TRPO (2026-11-21, kế hoạch; thay các dòng mạch 4 của 4.1–4.4)

Phong cách theo các SVG hiện có trong `img/lec-10/`: `viewBox` cố định, `role="img"`, `aria-labelledby="t d"` với `<title>` và `<desc>` đủ số, phông `'Source Sans 3','Source Sans Pro','Noto Sans',Arial,sans-serif`, chữ `#1d2433`, mũi tên bằng `<marker>`; màu theo quy ước đầu tệp (đỏ: ngược dấu, sai chiều; cam nét đứt: hàm thay thế, dự báo; xanh nét liền: $J$ thật; tím: đại lượng mới của trang), mỗi màu kèm nét hoặc nhãn (NT25). Ký hiệu trong SVG viết bằng ký tự Unicode như các tệp hiện có (π̃, η, Δ, κ). Không chữ tiếng Anh trần (đề xuất có "Occupancy", "Surrogate", "Trust region", "Natural gradient", "PDL": đều thay bằng thuật ngữ Việt). Cỡ chữ: trang 1280 px chụp ở 1600 px nhân $1{,}25$, nên chữ chính $\ge20$ px trên ảnh cần cỡ chữ SVG $\ge16\cdot W/w$ với $W$ là bề rộng `viewBox`, $w$ là bề rộng đặt trên trang; cột "cỡ chữ tối thiểu" dưới đây là số đó, làm tròn lên.

**Mới.**

| Tệp | Trang | Nội dung và số | Dựng dần | `viewBox` · bề rộng đặt · cỡ chữ tối thiểu |
|---|---|---|---|---|
| `ham-thay-the-tiep-xuc-chi-J.svg` (H7, bản chỉ có đường $J$; sau cổng storyboard) | `4-01`, mảnh đầu của `4-04` | Cùng `viewBox`, khung, trục $t\in[0;\,1]$ và tỉ lệ trục tung với `ham-thay-the-tiep-xuc*.svg`, để `4-04` chỉ thêm đường cam. Trục tung ghi "$J(\pi_t)-1{,}4$" (vạch $-0{,}1$; $0$; $0{,}1$). Chỉ đường xanh nét liền $0{,}095t-0{,}18t^2$, nhãn "$J(\pi_t)$"; năm điểm xanh: $t=0$, $0{,}25$, $0{,}5$, $\tfrac{19}{36}$, $1$, nhãn giá trị $J$: "$1{,}4$", "$1{,}4125$", "$1{,}4025$", "$1{,}4$", "$1{,}315$"; mũi tên ngắn tại $t=0$ ghi "độ dốc $0{,}095$". Không đường cam, không nhãn "hàm thay thế" | không | 840×475 · 560 · 24 (như bản gốc) |
| `luong-100-luot-buoc0.svg`, `luong-100-luot.svg` (H4) | `4-27` | Hai luồng chồng nhau, nhãn trái "chính sách cũ $\pi=(0{,}5;\,\tfrac23)$" và "ứng viên $\tilde\pi=(0{,}9;\,0{,}5)$". Mỗi luồng: khối "100 lượt" → khối "tới $s_B$" ($50$; $90$) và khối "nhận $1$ tại $s_A$" ($50$; $10$); từ "tới $s_B$" → "nhận $3$" ($33$; $45$) và "nhận $0$" ($17$; $45$). Bề dày dải tỉ lệ số lượt. Dải tới $s_B$ của $\tilde\pi$ tím (đại lượng mới: tần suất tới $s_B$); dải khác xám, khối "nhận 3" viền xanh, "nhận 0" viền xám. Chú thích nhỏ dưới: "số lượt kỳ vọng; $33\tfrac13$, $16\tfrac23$ làm tròn". Không màu đỏ | `-buoc0` chỉ luồng $\pi$; bản đủ thêm luồng $\tilde\pi$ | 960×440 · 620 · 25 (chữ chính 26) |
| `ba-thanh-phan-buoc0.svg`, `ba-thanh-phan.svg` (H5) | `4-02` | Ba khối ngang, thẳng hàng với ba thừa số của công thức bổ đề: "$\eta_{\pi'}(s)$: tần suất gặp $s$ dưới $\pi'$" với dòng số "$\tilde\pi$: $(1;\,0{,}81)$"; "$\pi'(a\mid s)$: phân phối hành động mới" với "$\tilde\pi(1\mid s)=(0{,}9;\,0{,}5)$"; "$A_\pi(s,a)$: lợi thế của $\pi$" với "$s_A$: $(0{,}4;\,-0{,}4)$, $s_B$: $(1;\,-2)$". Không có chú thích "thay bằng η cũ", "hiệu chỉnh bằng tỉ số", "ước lượng bằng critic" của đề xuất (thuật ngữ chưa dạy ở `4-02`, TB11; ý này ở lời giải `4-16` và ghi chú diễn giả) | `-buoc0` ba khối viền xám; bản đủ: khối $\eta_{\pi'}$ nền tím nhạt, viền tím đậm, nhãn dưới "chưa biết khi chưa chạy $\pi'$" | 1200×200 · 900 · 22 (chữ chính 24) |
| `dong-gop-tung-trang-thai-buoc0.svg`, `dong-gop-tung-trang-thai.svg` (H6) | `4-16` | Hai bảng cột cùng trục tung $[-0{,}45;\,0{,}4]$. Trái "dự báo: tần suất của $\pi$": cột $s_A$ $1\cdot0{,}32=+0{,}32$, cột $s_B$ $0{,}45\cdot(-0{,}5)=-0{,}225$; tổng "$\Delta\mathcal L=+0{,}095$" màu cam, khung nét đứt. Phải "thực tế: tần suất của $\tilde\pi$": $s_A$ $+0{,}32$, $s_B$ $0{,}81\cdot(-0{,}5)=-0{,}405$; tổng "$\Delta J=-0{,}085$" màu xanh, khung liền. Cột dương xanh lục nhạt, cột âm xám đậm (không dùng đỏ cho cột âm); ngoặc đỏ ở $s_B$ bảng phải nối hai mức $-0{,}225$ và $-0{,}405$, nhãn "$-0{,}18$" | `-buoc0` chỉ bảng trái; bản đủ thêm bảng phải và ngoặc đỏ | 900×440 · 560 · 26 |
| `sigmoid-hai-buoc-buoc0.svg`, `sigmoid-hai-buoc.svg` (H8) | `4-28` | Đường $p=\sigma(\theta)$, $\theta\in[-6;\,6]$, trục tung $[0;\,1]$. Bước $0\to1$: đoạn ngang, đoạn đứng tím nét đứt, nhãn "$\Delta\theta=1$, $\Delta p=0{,}2311$". Bước $5\to6$: hai chấm tím sát nhau trên đoạn bão hòa, nhãn "$\Delta\theta=1$, $\Delta p=0{,}0042$" | `-buoc0` đường và bước $0\to1$; bản đủ thêm bước $5\to6$ | 720×440 · 520 · 23 (chữ chính 24) |
| `kl-ba-bernoulli-buoc0.svg`, `-buoc1.svg`, `kl-ba-bernoulli.svg` (H9) | `4-12` | Tiêu đề "phân phối hành động tại $s_A$". Ba thanh xếp chồng 100%: "$\pi$" $50\%\,/\,50\%$; "$t=0{,}25$" $60\%\,/\,40\%$; "$\tilde\pi$" $90\%\,/\,10\%$ (hành động 1 xanh dương, hành động 2 xám, nhãn trong thanh). Cột phải mỗi hàng: "TV $0$ · KL $0$"; "TV $0{,}1$ · KL $0{,}0204$"; "TV $0{,}4$ · KL $0{,}511$" | mỗi bản thêm một hàng | 760×330 · 560 · 22 (chữ chính 24) |
| `chuoi-bon-mat-xich-buoc0.svg`, `-buoc1.svg`, `-buoc2.svg`, `chuoi-bon-mat-xich.svg` (H10) | `4-21` | Bốn khối ngang: "KL trung bình $\le\kappa$" (tím) → "TV nhỏ tại mỗi trạng thái" → "phân bố chiếm dụng ít thay đổi" → "sai số $\lvert\Delta J-\Delta\mathcal L\rvert$ nhỏ". Nhãn dưới ba mũi tên: "bất đẳng thức Pinsker", "bổ đề dịch chuyển", "định lý chặn cải thiện" (sau cổng storyboard). Không chữ tiếng Anh | mỗi bản thêm một mũi tên và khối kế | 1500×240 · 1100 · 22 (chữ chính 24) |
| `tron-va-elip-buoc0.svg`, `-buoc1.svg`, `tron-va-elip.svg` (H11) | `4-30` | Hai bảng cùng hệ trục $(\Delta_A,\Delta_B)$, cùng ba đường đồng mức xám nét đứt vuông góc với $g=(0{,}2;\,0{,}3)$. Trái "ràng buộc Euclid: $\lVert\Delta\rVert\le r$": hình tròn, mũi tên xám đậm $g$ tới biên. Phải "ràng buộc KL bậc hai: $\tfrac12\Delta^\top F\Delta\le\kappa$": elip có bán trục theo $\Delta_B$ dài gấp $1{,}58$ lần theo $\Delta_A$ (như `elip-gradient-tu-nhien.svg`), mũi tên $g$ nét đứt xám, mũi tên tím theo hướng $F^{-1}g\propto(8;\,30)$ tới điểm biên chạm đường đồng mức cao nhất, nhãn "$F^{-1}g$". Không số trên trục | `-buoc0` bảng trái; `-buoc1` thêm elip và $g$; bản đủ thêm mũi tên tím | 1100×520 · 760 · 24 |
| `ti-trong-hai-thanh-phan.svg` (H12) | `4-08` | Hai thanh xếp chồng 100%: "$g=(0{,}2;\,0{,}3)$": $\theta_A$ $40\%$ (xám), $\theta_B$ $60\%$ (tím); "$F^{-1}g=(8;\,30)$": $21\%$, $79\%$. Chú thích dưới: "tỉ trọng theo tổng giá trị tuyệt đối, không phải độ dài bước" | không | 760×260 · 520 · 24 |
| `ba-truc-giac.svg` (H14) | `4-31` | Ba bảng nhỏ có tiêu đề "hàm thay thế", "miền tin cậy", "gradient tự nhiên": (1) đường cong xanh và tiếp tuyến cam nét đứt chạm tại một điểm (như `ham-thay-the-tiep-xuc.svg`); (2) vòng tròn tím nét đứt, một chấm xanh bên trong, một chấm đỏ bên ngoài có nhãn "ngoài miền", mũi tên từ tâm; (3) elip tím với mũi tên tím và mũi tên xám nét đứt (như bảng phải của H11). Chú thích một dòng mỗi bảng là chữ HTML trên trang, không lặp trong SVG | không | 1200×360 · 1000 · 20 (tiêu đề bảng 24) |
| `vong-trpo.svg` (H13; quyết định 2 của điều phối viên) | `5-09` | Sơ đồ đứng năm khối theo tên nhóm bước của `4-09`, `4-26` (Đ12): **Thu lượt** (bộ đệm, lưu phân phối cũ) → **Ước lượng lợi thế** ($\delta_t$, GAE) → **Tính hướng** (giải $Fx=g$ bằng gradient liên hợp) → **Chọn độ dài bước** (kiểm hàm thay thế mẫu và KL mẫu) → **Cập nhật critic**; mũi tên cuối "bỏ bộ đệm, thu lượt mới". Vòng tìm kiếm lùi màu đỏ, nét liền, nhãn "không đạt: thu nhỏ bước" (chỗ nêu chi phí của TRPO; đỏ ở đây theo quyết định của điều phối viên, kèm nhãn theo NT25). Khối "Tính hướng" viền tím, nhãn "khoảng mười tích $Fv$" | không | 700×620 · 420 · 27 (chữ chính 28) |

**Không vẽ.** H1 (năm bước của đề xuất): sơ đồ neo của bài là vòng bốn khối (TB2), và các nhãn của H1 ("PDL", "Surrogate + IS", "KL / Trust region", "Fisher") là thuật ngữ chưa dạy ở điểm vào mạch (TB11, Đ11). Năm bước chỉ nằm trong cấu trúc cụm A–E của storyboard; không lên `p.strand-keys` của `4-00`, vì các mạch khác không có dòng này (quyết định 3). H2 (gradient đúng, bước dài làm giảm hiệu năng): trái số của chuỗi (bước theo gradient đúng không làm $J$ giảm), thay bằng `buoc-dai-mot-luot-nho.svg`. H3 (chuỗi hai trạng thái): đã ở `1-09`, `1-10`; `4-27` không lặp.

**Dùng lại, giữ nguyên.** `so-do-neo-m4-vao.svg` (`4-00`); `ham-thay-the-tiep-xuc-buoc2.svg`, `ham-thay-the-tiep-xuc.svg` (`4-04`, sau bản chỉ có đường $J$). Không dùng nữa trên mạch 4: `ham-thay-the-tiep-xuc-buoc0.svg`, `-buoc1.svg`; `buoc-dai-mot-luot-nho.svg` chỉ còn ở `1-06`.

**Sửa.** `ham-thay-the-tiep-xuc-loi-giai.svg` (`4-10`): nhãn điểm cam "$0{,}024$" thành "$0{,}02375$" (khớp bảng của trang), sửa `<desc>` và `alt`. `ham-thay-the-mien-tin-cay.svg` (`4-07`): nhãn tại $t=1$ "$\bar D_{\mathrm{KL}}=0{,}054$" thành "$0{,}0536$" (khớp mặt trang), sửa `<desc>` và `alt`.

**Bỏ khỏi deck (giữ tệp).** `chuoi-ti-le-toi-sB-buoc0.svg`, `chuoi-ti-le-toi-sB.svg` (thay bằng H4); `elip-gradient-tu-nhien-buoc0.svg`, `-buoc1.svg`, `elip-gradient-tu-nhien.svg` (thành nguồn hình học của H11; `4-08` dùng H12).

---

## 5. Thời lượng (P6: 120 phút)

| Mạch | Phút từng trang | Tổng |
|---|---|---|
| 1 | 1-01 0,5 · 1-02 2 · 1-09 2 · 1-10 1,5 · 1-11 2 · 1-04 3 · 1-12 1 · 1-05 2,5 · 1-06 1 · 1-07 0,5 · 1-08 1 | 17 |
| 2 | 2-00 0,5 · 2-01 2,5 · 2-04 1,5 · 2-02 2 · 2-03 2 · 2-06 1,5 · 2-09 1,5 · 2-10 2 · 2-07 1,5 · 2-08 1,5 · 2-11 1,5 | 18 |
| 3 | 3-00 0,5 · 3-01 1,5 · 3-06 2,5 · 3-07 1,5 · 3-02 1,5 · 3-08 1,5 · 3-11 2 · 3-05 2 · 3-09 1 · 3-12 2 · 3-13 1,5 · 3-04 2 · 3-10 2 | 21,5 |
| 4 | 4-00 0,5 · 4-01 2 · 4-27 1,5 · 4-13 1,5 · 4-02 1,5 · 4-03 1,5 · 4-11 1 · 4-16 1,5 · 4-04 1 · 4-10 1,5 · 4-17 1 · 4-28 1,5 · 4-12 1,5 · 4-07 0,75 · 4-32 0,75 · 4-21 1,5 · 4-14 1,5 · 4-20 1 · 4-24 1,5 · 4-06 1 · 4-19 1,5 · 4-29 1,5 · 4-22 1,5 · 4-30 1 · 4-08 1,5 · 4-25 1,5 · 4-09 1,5 · 4-26 1 · 4-31 1 (29 trang sau khi tách `4-07`, `4-32`) | 37,5 |
| 5 | 5-00 0,5 · 5-09 1,5 · 5-10 1,5 · 5-01 2 · 5-02 1,5 · 5-11 1 · 5-03 2 · 5-05 2 · 5-06 1,5 · 5-07 1 · 5-14 1,5 · 5-08 1 · (5-12 1,5 · 5-13 2: tính vào 30 phút bài tập) | 17 |
| 6 | 6-00 0,5 · 6-10 1,5 · 6-11 1 · 6-18 1 · 6-12 1 · 6-13 1 · 6-14 1,5 · 6-15 1,5 · 6-16 1 · 6-17 0,5 | 11 |
| **Tổng** | 88 trang thật; 87 trang đếm (TB17: `5-10`–`5-01`; sau khi tách `4-07`, `4-32`) | **122** trình chiếu + 3,5 bài tập 10.23 (ước lượng của biên tập viên) |

**Cập nhật theo đề xuất trình bày TRPO (2026-11-21, kế hoạch mạch 4).** Hàng mạch 4 trước kế hoạch: 27 trang, 37,5 phút (4-00 0,5 · 4-01 1,5 · 4-13 1,5 · 4-02 1,5 · 4-14 2 · 4-15 1 · 4-03 1,5 · 4-11 1 · 4-16 1,5 · 4-05 1,5 · 4-23 1,5 · 4-17 1,5 · 4-04 1,5 · 4-10 2 · 4-24 1 · 4-06 1 · 4-18 2 · 4-19 1,5 · 4-12 1,5 · 4-20 1 · 4-21 1,5 · 4-07 1,5 · 4-22 1 · 4-08 1,5 · 4-25 1,5 · 4-09 1,5 · 4-26 1); tổng 86 trang thật, 85 trang đếm. Sau kế hoạch: 28 trang, 37,5 phút; tổng 87 trang thật, 86 trang đếm, 122 phút. Phút không tăng: năm trang mới (`4-27` 1,5, `4-28` 1,5, `4-29` 1,5, `4-30` 1, `4-31` 1; cộng 6,5) bù bằng bốn trang bỏ (`4-05`, `4-15`, `4-18`, `4-23`; cộng 6) và rút `4-10` (2 → 1,5), `4-17` (1,5 → 1), `4-14` (2 → 1,5); `4-22` tăng 0,5 (dòng mở bài toán của cụm D), `4-24` tăng 0,5 (khối bổ đề thay hai định nghĩa).

**Hai ước lượng thời lượng mạch 4 (sau cổng storyboard, 2026-11-21; chờ tác giả quyết; hiện dựng đủ 28 trang).** (a) Cộng theo trang: 37,5 phút (hàng trên; sau cổng `4-01` 1,5 → 2 vì thêm đoạn thẳng và đường $J$, `4-04` 1,5 → 1 vì đoạn thẳng đã ở `4-01`). (b) Ước lượng của cổng storyboard: khoảng 47,5 phút, cao hơn khoảng 10 phút; vai mạch truyện trước đó ước khoảng 50 phút cho mạch 4 cũ. Nếu tác giả chọn (b) và giữ tổng 122 phút, các trang có thể rút, theo thứ tự đề xuất (phút theo cách đếm (a), cộng $10{,}5$, khoảng $13$ phút theo (b)):

| # | Rút | Cách | Phút (a) | Mất gì |
|---|---|---|---|---|
| 1 | `4-29` | xuống ghi chú diễn giả `4-19`; hộp "TRPO thay phạt bằng ràng buộc" lên `4-19` | −1,5 | Hệ quả 10.30 không còn khối trên trang (TB28) |
| 2 | `4-19` | gộp vào `4-06` thành hai dòng số | −1,5 | bảng hai cột của cận trên chuỗi |
| 3 | `4-14` | thành dòng "Chứng minh." của `4-02`; dòng bỏ "cùng $\mu_0$" xuống ghi chú diễn giả | −1,5 | trang ý tưởng chứng minh duy nhất của mạch (Đ8, Đ9) |
| 4 | `4-13` | gộp vào `4-02`: $A_\pi(s,\pi')$ thành dòng "Ký hiệu:" có số | −1,5 | câu hỏi mở khái niệm (TB27) |
| 5 | `4-10` | câu hỏi nhanh xuống ghi chú diễn giả `4-04`; mạch còn câu hỏi nhanh `4-16` (TB22) | −1,5 | phép thử quy luật bình phương |
| 6 | `4-30` | gộp vào `4-08`, H11 thay H12 | −1 | trang trực quan hình học (đề xuất 17, mức "cao") |
| 7 | `4-22` | gộp vào `4-30`: mệnh đề KL bậc hai thành dòng "Nhắc lại:" của bài toán xấp xỉ | −1 | khối Mệnh đề 10.33 |
| 8 | `4-31` | hộp điều còn thiếu chuyển lên `5-09`, H14 xuống ghi chú diễn giả `4-26`; `4-08` còn là trạm dừng | −1 | trạm dừng cuối mạch (TB5) |

*Lịch sử (bản trước hai lượt sửa theo năm vai; số trang và phút đã thay bằng đoạn "Cập nhật sau lượt sửa thứ hai" dưới đây).* **Ngoại lệ số trang (điều phối viên chấp nhận 2026-11-21; chờ tác giả xác nhận khi duyệt deck).** 81 trang thật, 79 trang đếm (TB17: `4-15`–`4-16`, `5-10`–`5-01`), 120 phút; vượt trần 60 của P6 (`NGUYEN-TAC-HOC-PHAN.md` §3, "Số trang ở đợt sửa"). Lý do: TB24 (ba trang dựng ví dụ), TB28 (mỗi kết quả một khối có nhãn; năm trang ý tưởng chứng minh riêng `2-10`, `3-11`, `3-12`, `4-14`, `4-18`), TB29 (bảng tính đủ cột; `4-05`/`4-23` tách vì đưa khai triển lên mặt trang), TB12/TB24 (`4-24` tách định nghĩa khỏi định lý), TB31 và Đ12 (ba trang thuật toán, ví dụ tay TRPO riêng `4-25`), cùng góp ý #14, #21–#26 của tác giả. Bản trước cổng storyboard: 76 trang thật, 74 trang đếm; cổng thêm năm trang (`3-11`, `3-12`, `4-23`, `4-24`, `4-25`). Thời lượng giữ 120 phút bằng cách rút phút ở các trang kết quả có chứng minh một dòng và ở câu hỏi nhanh (mục trên). Rủi ro: mạch 4 dài 36,5 phút (26 trang), có ba trạm dừng `4-16`, `4-19`, `4-09`.

*Lịch sử (lượt sửa thứ nhất).* **Cập nhật sau năm vai rà (2026-11-21, B8).** Thêm trang `1-12` (câu hỏi nhanh của mạch 1, B5; không vừa `1-05` và `1-04`, nên tách trang, trái khuyến nghị "không tách thêm trang" của B7) và đổi thứ tự mạch 4 (B5), nên `4-15` và `4-16` không còn liền nhau: chúng không còn là một chuỗi dựng dần, tính hai trang. `3-07` (+0,5, bổ đề) và `4-21` (+0,5, hệ quả cải thiện đơn điệu) thêm phút. Bài tập 10.23 (`5-12`, `5-13`, 3,5 phút) tính vào 30 phút bài tập trên lớp. Tổng: 82 trang thật, 81 trang đếm, 118,5 phút trình chiếu.

**Cập nhật sau lượt sửa thứ hai (2026-11-21, E1, E3).** `6-11` tách thành `6-11` và `6-18` (+1 phút); `1-12` chuyển lên giữa `1-04` và `1-05`. Tổng theo biên tập viên: 83 trang thật, 82 trang đếm, 119,5 phút trình chiếu, Bài tập 10.23 tính 3,5 phút. Ước lượng của vai mạch truyện (mục D của `ra-soat-nam-vai-2026-11-21.md`): khoảng 145–155 phút, riêng mạch 4 khoảng 50 phút; Bài tập 10.23 khoảng 10–12 phút. Hai ước lượng chênh nhau khoảng 30 phút; ước lượng của vai mạch truyện vượt 120 phút của P6. Lượt sửa thứ ba (G1–G3) không thêm, không bớt trang; số phút giữ nguyên. Sau góp ý tác giả #1–#3 (2026-11-21): thêm `3-13` (+1,5 phút), tách thuật toán TRPO (`4-09`, `4-26`) và PPO-Clip (`5-07`, `5-14`) để mọi đại lượng có công thức tại bước tính nó (+0,5 phút mỗi thuật toán); tổng 86 trang thật, 85 trang đếm, 122 phút trình chiếu theo ước lượng của biên tập viên, vượt 120 phút của P6: ngoại lệ chờ tác giả. Đây là đoạn hiện hành của mục này. **Ngoại lệ chờ tác giả:** chọn ước lượng thời lượng và quyết định có rút trang hay không.

**Phương án rút gọn: không áp dụng** (quyết định của điều phối viên, 2026-11-21). Danh sách giữ lại để đối chiếu nếu lượt rà sau cần:

1. `4-22` gộp vào `4-08`: xấp xỉ bậc hai của KL thành giả thiết của mệnh đề bước gradient tự nhiên (−1 phút).
2. `3-07` gộp vào `3-02`: lợi thế $n$ bước thành dòng "Ký hiệu:" của định nghĩa GAE (−1).
3. `2-11` gộp vào `2-08`: hai hàng kỳ vọng, phương sai dưới bảng ba hệ số, ô ghi kết quả và nhắc nguồn `1-04`, `2-02` (−1,5).
4. `4-15` gộp vào `4-16` (bỏ bước dựng dần đầu) (−1).
5. `6-12` và `6-13` thành một trang 8 hàng (vượt ≤ 6 hàng của TB21) (−0,5).
6. `5-09` gộp vào `5-10`: câu bài toán thành dòng đầu của trang bộ đệm (−1).
7. `1-11` gộp vào `1-10`: gradient dưới bảng $J$, hàm điểm chuyển sang dòng đầu `1-04` (−1).
8. `2-03` (câu hỏi nhanh trừ $q_\pi$) chuyển sang ghi chú diễn giả của `2-04`; mạch 2 khi đó không có câu hỏi nhanh (trái TB22) (−2,5).

---

## 6. Đối chiếu mã trang

| Mã cũ (2026-11-20) | Mã mới | Ghi chú |
|---|---|---|
| `1-01`, `1-02`, `1-06`, `1-07`, `1-08` | giữ | sửa nội dung |
| `1-03` | bỏ | hành lang |
| `1-04`, `1-05` | giữ | chức năng "vấn đề 1", "vấn đề 2", nay trên chuỗi |
| — | `1-09`, `1-10`, `1-11` | dựng ví dụ chung |
| `2-00`–`2-04`, `2-06`–`2-08` | giữ | `2-01` từ ví dụ REINFORCE thành bài toán và trực quan; bảng REINFORCE chuyển sang `1-04` |
| `2-05` | bỏ | gộp vào dòng "Chứng minh." của `2-04` |
| — | `2-09`, `2-10`, `2-11` | hệ quả, ý tưởng chứng minh, trạm dừng |
| `3-00`, `3-01`, `3-02`, `3-04`, `3-05` | giữ | `3-04` đổi câu hỏi nhanh ($\lambda=0{,}8$ → một vòng với GAE) |
| — | `3-06` … `3-10`; `3-11`, `3-12` (cổng storyboard) | |
| `4-00` … `4-12` | giữ | thứ tự mới ở mục 3 |
| — | `4-13` … `4-22`; `4-23`, `4-24`, `4-25` (cổng storyboard) | |
| `5-00`–`5-03`, `5-05`–`5-08` | giữ | |
| `5-04` | bỏ | bộ đệm khác |
| `7-03`, `7-04` | `5-12`, `5-13` | bài tập tổng hợp về cuối mạch 5 |
| — | `5-09`, `5-10`, `5-11` | |
| `6-00` … `6-09` (DPO) | bỏ; `6-00` dùng lại cho trang tiêu đề tổng kết | |
| `7-00`, `7-01`, `7-02`, `7-05`, `7-06`, `7-07` | `6-00`, `6-10`, `6-11`, `6-15`, `6-16`, `6-17` | đổi tiền tố |
| — | `6-12`, `6-13`, `6-14` | bảng kết quả, bảng phương pháp |

**Đề xuất TRPO (2026-11-21, kế hoạch).** Mạch 4: bỏ `4-05` (gộp vào `4-04`), `4-15` (gộp vào `4-02`), `4-18` (gộp vào `4-06`), `4-23` (xuống ghi chú diễn giả `4-04`); thêm `4-27` (luồng 100 lượt), `4-28` (sigmoid), `4-29` (cải thiện đơn điệu, tách từ `4-21`), `4-30` (tròn và elip), `4-31` (trạm dừng cuối mạch); không dùng lại mã đã bỏ. Chi tiết ở §3 mạch 4.

**Liên kết sâu cần sửa (giao cho người khác):** bảng mở đầu `exercises.md` (`#/1/1` … `#/6/1`, tên mạch theo mục 1, bài tập theo `6-16`); dòng "Trùng trang chiếu" của Bài tập 10.23 trong ghi chú (nếu có) trỏ tới `5-12`, `5-13`; thẻ Bài 10 trong `index.html` ("TRPO và PPO").

---

## 7. Ngoại lệ mật độ và quy tắc (ghi trước, người dựng đo lại)

**Dạng chứng minh trên trang (TB28, quyết định ở cổng storyboard).** Chỉ hai dạng: (a) đúng một dòng "Chứng minh." nêu bước then chốt trên trang kết quả; (b) trang riêng "Ý tưởng chứng minh: …" có bước mang tên của ghi chú (Đ8) và một hộp "Câu hỏi:" tự giải thích (Đ9).

| Kết quả | Dạng | Trang |
|---|---|---|
| Đường cơ sở (Mệnh đề 10.2) | (a), Bước 2 của ghi chú | `2-04` |
| Sai số TD và lợi thế (Mệnh đề 10.8(a)) | (a), Bước 1 | `2-07` |
| Gradient dạng lợi thế (Mệnh đề 10.5(b)) | (b) | `2-10` |
| Dạng tổng, truy hồi của GAE (Mệnh đề 10.14) | (b) | `3-11` |
| GAE và gradient (Mệnh đề 10.15) | (b) | `3-12` |
| Bổ đề chênh lệch hiệu năng (Bổ đề 10.19) | (b) | `4-14` |
| Hàm thay thế tiếp xúc (Mệnh đề 10.22) | (a), gộp Bước 1–2 | `4-17` |
| Pinsker (Mệnh đề 10.25(b)) | (a), Bước 3 (ý tưởng, như ghi chú) | `4-20` |
| Dịch chuyển phân bố chiếm dụng (Bổ đề 10.26) | (a), Bước 1, 3, 5 bằng lời | `4-24` |
| Chặn cải thiện (Định lý 10.27) | (a), Bước 1–5 gọi tên | `4-06` |
| Chặn theo KL (Hệ quả 10.28) | (a), Bước 1–3; dòng đặt ở mảnh cuối `4-06`, `4-21` chỉ phát biểu | `4-06` |
| Cải thiện đơn điệu (Hệ quả 10.30) | (a), Bước 1–3 | `4-29` |
| KL bậc hai (Mệnh đề 10.33) | (a), Bước 2–3 | `4-22` |
| Bước gradient tự nhiên (Mệnh đề 10.34(a)) | (a), Bước 2–3 | `4-08` |
| Mục tiêu cắt theo dấu (Mệnh đề 10.40) | (a), Bước 1–2 | `5-11` |

Dòng "Chứng minh." một dòng tính là một phần của khối kết quả khi đếm khối có nhãn (TB13).

| Trang | Lý do |
|---|---|
| `1-02` | hai công thức hiển thị và sáu dòng có nhãn (hai "Nhắc lại:", "Ý nghĩa:", "Ký hiệu:", "Lưu ý:", "Giả thiết chung:"), vượt TB13 (≤ 2 khối có nhãn); giữ vì #1 (định nghĩa, ý nghĩa của $\psi$), Đ4 (dòng phân biệt kỳ vọng, không chệch, phương sai, chuyển từ `1-04`) và Đ7 (giả thiết chung một lần trên trang có tên); dựng dần bốn mảnh |
| `2-07` | ba khối có nhãn ("Nhắc lại:", "Mệnh đề." kèm "Chứng minh.", "Lưu ý:"), vượt TB13; "Lưu ý:" là trường hợp khác cấu trúc của Đ2 cho mệnh đề này |
| `2-10`, `3-11`, `3-12`, `4-14`, `4-18` | trang ý tưởng chứng minh 4–5 bước kèm hộp câu hỏi (Đ8, Đ9); mỗi bước một dòng |
| `2-09`, `4-15`, `4-17` | thêm dòng "Ở đây" (Đ6) hoặc dòng trường hợp khác cấu trúc (Đ2); vượt 6 dòng thì dòng thêm hiện ở mảnh cuối |
| `1-04`, `2-02`, `2-08`, `3-06`, `3-05`, `4-16`, `4-19` | bảng tính đủ cột (#3, #16, #19, #25, TB29); cột 6–7 vượt "≤ 5–6 cột" của TB16 ở `1-04`, `2-08`, `4-16` |
| `4-23` | ba dòng khai triển trong một công thức hiển thị (TB12 tính một công thức nhiều dòng; dựng dần từng dòng) |
| `4-25` | năm dòng tính, giữ trên một trang vì là ví dụ tay của `4-09` (Đ12) |
| `3-10`, `4-09`, `5-07` | trang thuật toán ≈ 8–9 dòng (TB31; giả mã trên 8 dòng có trang riêng) |
| `6-11` | khoảng 105 âm tiết (trần 80): bốn câu trả lời có điều kiện và dòng mở gọi tên ví dụ chung (Đ13) |
| `6-12`, `6-13`, `6-14` | bảng tổng kết (trần 80) |
| `3-06` | tiêu đề 17 âm tiết (TB6: ≤ 16), giữ đúng câu tác giả đề xuất (#18) |
| `4-22` | "Đặt $F$" nằm trong giả thiết của mệnh đề để trang chỉ có một khối có số hiệu (TB6); $D_{\mathrm{TV}}$, $\nu^\pi$ đã tách sang `4-24` (TB12, TB24) |
| cả deck: lớp `dense` trên `div.reveal` | KaTeX 1,1em (tức .88em, vẫn lớn hơn chữ thân bài .8em) thay 1,21em mặc định; khoảng cách giữa đoạn, công thức hiển thị và hộp nhỏ hơn trên trang `compact`. Lý do: với 1,21em, phần lớn trang theo storyboard tràn khung 720 px. Giữ theo B7 của `ra-soat-nam-vai-2026-11-21.md`; chờ tác giả duyệt (đề xuất C2) |
| mọi bảng tính: `table.calc` | ô không xuống dòng, công thức trong ô cùng cỡ chữ bảng (.752em ≥ .75em của NT-RL-7), lề ô .3em. Lý do: bảng đủ cột (TB29) vừa bề rộng 1280. Giữ theo B7; chờ tác giả duyệt |
| `4-21` | hai khối có số hiệu (Hệ quả 10.27 và Hệ quả 10.29), trái TB6 "trang có từ hai khối có số hiệu trở lên thì tách"; B5 chọn đặt Hệ quả 10.29 ở `4-21` hoặc `4-07`, `4-07` không còn chỗ, và B7 không cho thêm trang |
| `6-11`, `6-18` | E1 yêu cầu khung "Câu hỏi:" là danh sách hai câu và hai nhóm trả lời dưới khung; một trang cao 1031 px, nên tách: `6-11` (khung, "Trả lời câu 1:", mục 1–2), `6-18` (nhắc câu 2, "Trả lời câu 2:", mục 3–4, dòng "Ví dụ chung của hai câu: chuỗi hai trạng thái."). "Trả lời câu 1:", "Trả lời câu 2:" để chữ thường, không in đậm, vì không thuộc danh sách nhãn NT19 |
| `5-05` | câu "mỗi số hạng là $\widehat A_t\max(\rho_t,0{,}8)$" xuống ghi chú diễn giả; câu dừng của E1 đứng trong đoạn văn, hộp cạnh hình chỉ giữ "Phép cắt không sửa lợi thế ước lượng sai." (hộp hai câu trong cột hẹp cao sáu dòng, trang 768 px) |
| `4-21` | câu "Với $\tilde\pi$, phạt $\approx14{,}7$ … phạt dạng TV $\approx4{,}3$" xuống ghi chú diễn giả để thêm dòng "Chứng minh." của Hệ quả 10.29 (E2) |
| `5-07` | mục 3 tách hai dòng con (E4), `deck_lint` LINES6 (8 dòng) |
| tên tiếng Anh | "số lần thăm có chiết khấu" (`4-02`), "điều kiện hỗ trợ" (`4-11`), "bổ đề dịch chuyển" (`4-18`) không kèm tên tiếng Anh: ghi chú không có tên tiếng Anh cho ba thuật ngữ này (E3, E4) |
| `1-08` | liên kết `#/1` của mục 1 trong `<ol>` dẫn tới bìa (mạch 1 không có trang tiêu đề mạch); chấp nhận (mục D, G3) |
| `4-09` | câu mở (actor–critic một bước nhỏ; TRPO tối đa hàm thay thế với KL trung bình $\le\kappa$) xuống ghi chú diễn giả để "Lưu ý:" của G1 đứng trên mặt trang; tên tiếng Anh của TRPO đặt ở dòng nhãn "Thuật toán", "bộ đệm (buffer)" ở bước 1; `deck_lint` LINES6 (7 dòng) |
| `4-13` | dòng "Ký hiệu:" riêng (G3), `deck_lint` LINES6 (7 dòng) |
| `2-09`, `2-02`, `5-02`, `3-08` | rút chữ để vừa khung sau G3: `2-09` bỏ tên trong ngoặc của "Hệ quả" (trùng tiêu đề), gọn câu chính sách đều; `2-02` câu cuối "…, còn $b\ne v_\pi$ có thể tăng phương sai."; `5-02` "$\rho_t\approx1$", "(làm tích tăng)"; `3-08` "$\hat v$ cố định trong lượt" |
| `1-06` | "Câu hỏi:" có danh sách hai câu (B1); `deck_lint` báo STRUCT "Vấn đề trung tâm mở đầu có danh sách (chỉ một hộp)": vẫn một hộp, danh sách nằm trong hộp |

**Mạch 4 theo đề xuất TRPO (2026-11-21, kế hoạch; người dựng đo lại).** Các hàng mạch 4 của bảng dạng chứng minh trên đã theo số và mã mới (sau cổng storyboard); `4-18` bỏ, chứng minh Hệ quả 10.28 ở mảnh cuối `4-06`.

| Trang | Lý do |
|---|---|
| `4-02` | dòng trực quan, khối bổ đề có công thức ba thừa số và hình ba thành phần trên một trang (gộp đề xuất 4, 5, 6); dòng "Ở đây" (Đ6) nằm trong hình. Nếu cao quá 720 px: dòng trực quan rút còn phép cộng, hình thu thấp |
| `4-01` | dòng nối, dòng ứng viên và đoạn thẳng, một công thức, hộp số hai câu, hộp câu hỏi và hình nửa phải (gộp đề xuất 1, 2; sau cổng storyboard); hai phần tử mới ($\tilde\pi$, $\pi_t$). Nếu tràn: hộp câu hỏi đi cùng mảnh với hộp số, câu "Mỗi lượt của mạch trước chỉ cho một bước" xuống ghi chú diễn giả |
| `4-08` | trạm dừng của cụm D: khối mệnh đề, "Ý nghĩa:", dòng số, hình H12 và hộp điều còn thiếu |
| `4-07` | ba phần tử mới ($\nu^\pi$, $\bar D_{\mathrm{KL}}$, bài toán miền tin cậy), vượt TB11 (một) và TB24 (hai): $\nu^\pi$ và KL trung bình là đối tượng của chính định nghĩa, tách ra một trang thì trang đó không có câu hỏi riêng (sau cổng storyboard). Khoảng 7 dòng ("Ký hiệu:" hai dòng, định nghĩa dạng tỉ số, "Ý nghĩa:", hai dòng số) và hình: trang trung tâm của mạch (đề xuất 14), $\nu^\pi$ và KL trung bình phải đứng trước bài toán. Nếu tràn: dòng $\tilde\pi$ rút còn "$\bar D_{\mathrm{KL}}(\tilde\pi)=0{,}1\cdot0{,}511+0{,}045\cdot0{,}0566=0{,}0536$", công thức $D_{\mathrm{KL}}(s_B)$ xuống ghi chú diễn giả |
| `4-12` | hai công thức định nghĩa trên một dòng hiển thị; dòng số tính hai KL; hai đối tượng mới (TB24 cho phép hai) |
| `4-14` | sáu dòng của trang ý tưởng chứng minh cộng dòng bỏ "cùng $\mu_0$" (Đ2), LINES6 |
| `4-17` | ba khối có nhãn ("Mệnh đề." kèm "Chứng minh.", "Ý nghĩa:", "Lưu ý:"), vượt TB13; "Lưu ý:" là trường hợp khác cấu trúc của Đ2, xuống ghi chú diễn giả nếu tràn |
| `4-21` | hình bốn khối, hệ quả, dòng chứng minh và hộp số trên một trang (đề xuất 15) |
| `4-16` | câu hỏi, hình hai bảng cột, đẳng thức sai số và hộp "Lời giải:" có bảng hai cột "đã hiệu chỉnh / chưa hiệu chỉnh" (quyết định 7 của điều phối viên). Nếu tràn: hình đặt cạnh bảng hai cột, đẳng thức hiện cùng mảnh với hình; nếu vẫn tràn, tách trang câu hỏi nhanh và bảng hai cột ngay sau `4-11` (mục `4-16`) |
| `4-06` | dòng "Chứng minh." dài hai dòng (gộp `4-18`) |
| `4-24`, `4-29` | khối kết quả có công thức hiển thị cộng dòng số trên chuỗi (Đ6) |

---

## 8. Đối chiếu góp ý #1–#28

| # | Xử lý ở |
|---|---|
| 1 | `1-02` (định nghĩa, ý nghĩa của $\psi$); `1-11` (dạng trên chuỗi, độ lớn $1-p_s$, $p_s$) |
| 2 | `1-09`, `1-10`, `1-11` (dựng ví dụ trước khi tính, TB24) |
| 3 | `1-04` (cột kết quả, hiện cùng chấm trên trục số; mọi ô viết đủ) |
| 4 | `1-10` ($J$ dẫn từ ba loại lượt; hành lang và $J(p)$ ở ghi chú) |
| 5 | `1-09` (một tham số hóa, quy ước $\theta\to(p_A;\,p_B)$); mọi bảng cập nhật có $\theta$ và $p$ (`1-05`, `3-04`, `4-01`) |
| 6 | mục 1 (năm dòng dẫn mới), `2-00`, `3-00`, `4-00`, `5-00`, `6-00` |
| 7 | `1-09`–`1-11`, `1-04` (môi trường bằng lời, tham số, $J$, gradient, ý chính trên mặt trang), `2-01` (câu hỏi so với mức nào); hình sạch `chuoi-hai-trang-thai*.svg` |
| 8, 9 | một ví dụ chung cho cả deck; bỏ hành lang (`1-03`); vấn đề 2 bằng bước dài theo ước lượng một lượt (`1-05`) |
| 10 | `2-01` (bài toán, trực quan trục số, cách tính $1{,}4$, tên đường cơ sở sau trực quan), `2-04` (vì sao kỳ vọng giữ), `2-02` (phương sai có phép tính) |
| 11 | mọi tiêu đề và dòng dẫn (mục 3; TB26) |
| 12 | "kỳ vọng" trên mọi trang; "trung bình trên bộ đệm" ở `5-09`, `5-01` |
| 13 | `2-06` (tiêu đề "Hàm lợi thế", định nghĩa theo Định nghĩa 10.4, "Ý nghĩa:", hình ghi $q_\pi$, $v_\pi$) |
| 14 | `2-09` (hệ quả), `2-10` (ý tưởng chứng minh 3 bước, kiểm $0{,}2$) |
| 15 | mạch 2 không có critic, actor; `2-07` (câu hỏi dẫn, mệnh đề $\delta_t$ có chứng minh), `2-11` (điều còn thiếu), `3-01` (critic, actor đúng nơi cần) |
| 16 | `2-08` (đủ cột đầu vào, $\delta_0$ có phép tính, nhắc $v_\pi$), `2-11` (kỳ vọng, phương sai có phép tính); không sơ đồ neo cạnh bảng |
| 17 | `3-00` (tên mạch, dòng dẫn); "chệch", "phương sai" toàn deck |
| 18 | `3-01` (critic sai có lý do, hình hai trạng thái), `3-06` (tiêu đề học thuật) |
| 19 | `3-06` (mục tiêu $0{,}4$, xác suất $p_B$, $1-p_B$, công thức đầu cột, kỳ vọng, độ chệch, phương sai có phép tính) |
| 20 | `4-01` (bài toán ở câu đầu, nguồn và tham số của $\tilde\pi$, bảng hai chính sách với $J$) |
| 21 | `4-13` ($A_\pi(s,\pi')$ từ câu hỏi), `4-02` (bổ đề đủ giả thiết, $\eta$, ý nghĩa), `4-14` (ý tưởng chứng minh), `4-15` (bảng kiểm) |
| 22 | `4-03` (định nghĩa $\Delta J$, $\Delta\mathcal L$), `4-05` (sai số dạng tổng quát, trên chuỗi, $\Delta\mathcal L$ có phép tính), `4-23` (khai triển $J$ ba dòng trên mặt trang), `4-17` (mệnh đề tiếp xúc, chứng minh), `4-04` (đoạn thẳng có phép thế, sau dạng tổng quát) |
| 23 | `4-24` ($D_{\mathrm{TV}}$, $\nu^\pi$ định nghĩa trước định lý), `4-06` (định lý bằng công thức, giả thiết của ghi chú, hằng $2\gamma\chi/(1-\gamma)^2$), `4-18`, `4-19` (số trên chuỗi) |
| 24 | `4-12` (định nghĩa KL, dạng tỉ số), `4-20` (Pinsker), `4-21` (hệ quả KL, chứng minh), `4-07` (lý do chọn KL phân biệt với TV) |
| 25 | `4-03` (định nghĩa đầy đủ, lý do trước), `4-16` (bảng đủ cột, tên cột đúng đại lượng), `4-11` (tỉ số); ký hiệu $\eta$ thống nhất với ghi chú (N5) |
| 26 | mạch 5 dựng lại (`5-09` bài toán … `5-08`); một bộ đệm cho cả mạch; trang "Thuật toán." `3-10`, `4-09`, `5-07`; không "Adam", không "Còn thiếu:" trên mặt trang |
| 27 | bỏ mạch DPO; bìa, mục tiêu, nội dung, sơ đồ neo, tổng kết, bài tập về nhà, tài liệu không còn DPO |
| 28 | mạch 6 định tính (`6-10` không số, `6-11` câu trả lời có điều kiện, `6-14` bảng phương pháp, `6-15` câu hỏi khái niệm); bài tập tổng hợp ở `5-12`, `5-13` |

Không có mục nào chưa xử lý. Hai điểm thực hiện một phần: #5 (bảng cập nhật có đủ cột $\theta$, $p$, $J$) chỉ ở các trang có bước cập nhật; #16 (tách trang khi chật) được làm bằng `2-11`. Sau tinh chỉnh Đ1–Đ13, các mục #10, #13, #14, #21–#24 được bổ sung: dòng phân biệt thuật ngữ (`1-02`, `1-04`, `2-06`, `3-06`, `4-12`), bước chứng minh trùng ghi chú (`2-04`, `2-07`, `2-10`, `3-08`, `3-09`, `4-14`, `4-17`, `4-18`, `4-20`, `4-21`, `4-22`, `4-08`, `5-11`), giả thiết chung một lần ở `1-02`.

### 8a. Đối chiếu tinh chỉnh Đ1–Đ13 (`NGUYEN-TAC-HOC-PHAN.md` §3a.F)

| Đ | Nội dung | Xử lý ở |
|---|---|---|
| 1 | "Nhắc lại:" ở trang tính đầu sau trang dựng | `1-04` ($\theta$, $p$, $J$, gradient, $\psi_A$); `3-06` (critic, $v_\pi$, $p_B$); `4-13` ($q_\pi$, $v_\pi$, $\tilde\pi$); `5-10` (critic, GAE $\lambda=1$, $\pi_{\mathrm{old}}$) |
| 2 | trường hợp khác cấu trúc cho mỗi kết quả chính; tính chất chỉ đúng trên chuỗi | đường cơ sở: `2-03` (trừ $q_\pi$), `2-02` (phương sai chỉ giảm trên ví dụ); gradient dạng lợi thế: `2-09` (phản ví dụ của ghi chú: lợi thế của chính sách đều cho $0{,}5\ne0$); chệch của $\delta$: `2-07` (điều kiện theo riêng $S_t$), ví dụ critic sai `3-06`; bổ đề chênh lệch hiệu năng: `4-15` (khác $\mu_0$, số của ghi chú: $1$ so với $0{,}4$); tiếp xúc: `4-17` (lợi thế ước lượng, $-0{,}45\ne0$), `4-23` (dạng tích chỉ trên chuỗi); chặn cải thiện: `4-19` (bước chỉ đổi $p_B$); mục tiêu cắt: `5-03` (phía bất lợi), `5-05` (tham số tách theo trạng thái), `5-06`; chỉ đúng trên chuỗi: `1-05` (gradient đúng không làm $J$ giảm) |
| 3 | phương pháp trình bày riêng trước; so sánh cùng bảng, cùng tên cột | REINFORCE `1-04`, đường cơ sở `2-02`, $\delta$ `2-07` → so sánh `2-08`, `2-11`; TRPO `4-09`, PPO `5-07` → `5-08`; bốn phương pháp → `6-14` |
| 4 | dòng phân biệt khi dùng lần đầu | kỳ vọng, không chệch, phương sai `1-02`; lợi thế `2-06` (trong "Ý nghĩa:"); độ chệch như đại lượng `3-06`; KL trung bình `4-12` (trong định nghĩa, "tổng có trọng số $\nu^\pi$") |
| 5 | khái niệm mở bằng trực quan trên chuỗi | đường cơ sở `2-01`; lợi thế `2-06` (dòng lý do); critic `3-01`; lợi thế $n$ bước `3-07`; GAE `3-02`; $A_\pi(s,\pi')$ `4-13` (câu hỏi); hàm thay thế `4-03`; $D_{\mathrm{TV}}$ `4-06`; KL `4-12`; Fisher `4-22`; mục tiêu cắt `5-02` |
| 6 | dòng tương ứng ký hiệu ↔ số sau kết quả | `2-02`, `2-09`, `3-02`, `3-08`, `4-15`, `4-19`, `4-22`, `4-24`, `4-13` ("Với $\pi'=\tilde\pi$") |
| 7 | giả thiết chung một lần, mỗi kết quả ghi giả thiết riêng | `1-02` ("Giả thiết chung:"); `2-04`, `2-07`, `2-09`, `3-09`, `4-02`, `4-06`, `4-17`, `4-22` ghi "giả thiết chung; thêm …"; `4-21` "như định lý" |
| 8 | bước chứng minh trùng ghi chú | trang ý tưởng chứng minh: 10.5 → `2-10` (tên Bước 2–4, không số vì số nhảy); 10.14 → `3-11` (Bước 1–4); 10.15 → `3-12` (Bước 1–5); Bổ đề 10.19 → `4-14` (Bước 1–5); Định lý 10.26 → `4-18` (Bước 1–5). Dòng "Chứng minh." một dòng nêu bước then chốt (§7): `2-04`, `2-07`, `4-17`, `4-20`, `4-21`, `4-22`, `4-08`, `5-11` |
| 9 | câu hỏi tự giải thích trên trang ý tưởng chứng minh; kết quả viết bằng công thức và dòng có nhãn | `2-10` (vì sao cần Markov dừng), `3-11` (vì sao critic cố định), `3-12` (critic đúng dùng ở đâu), `4-14` (vì sao kỳ vọng dưới $\pi'$ bằng $q_\pi$), `4-18` (vì sao $1/(1-\gamma)^2$); mọi khối kết quả có "Giả thiết:"/"Kết luận:" và công thức |
| 10 | phép tính cùng khuôn rút gọn từ hàng thứ hai | `1-04`, `2-02` (hàng đầu đủ), `2-08` ("như hàng trên"), `3-06` ("như (i)") |
| 11 | dòng dẫn chỉ dùng thuật ngữ đã có | mục 1, đoạn sau bảng mạch |
| 12 | thuật toán nhóm bước theo mục tiêu con; ví dụ tay đứng trước, cùng tên; sơ đồ khung cùng tên | `3-04` → `3-10`; `4-25` → `4-09`; `5-10`, `5-05` → `5-07`; sơ đồ neo `m4-vao`, `m5-vao`, `tong-ket` |
| 13 | câu hỏi tự kiểm tra có câu vận dụng; tổng kết gọi tên ví dụ chung, không số | `6-15` (câu 4: lượt bị cắt ngắn); `6-10` (chú thích), `6-11` (dòng mở) |

## 9. Quyết định của điều phối viên (2026-11-21) và câu hỏi còn mở

Đã chốt: (1) chấp nhận số trang vượt P6 như ngoại lệ (bản hiện hành sau năm vai rà: 82 trang thật, 81 trang đếm, 118,5 phút trình chiếu, mục 5), không áp phương án rút gọn; (2) N7: ghi chú thêm đoạn không đánh số sau Thuật toán 10.16 mô tả actor–critic với GAE, `3-10` dẫn Thuật toán 10.9 và 10.16; N8: không thêm khối định nghĩa, ghi chú thêm câu vào đoạn mở §4.1, trang `4-13` giữ nhãn "Định nghĩa."; N9: các số được thêm vào ghi chú; (3) giữ luận điểm bìa của `1-01`; (4) số bài tập theo BT4: Bài tập 10.22 (mạch 1), Bài tập 10.23 (cuối mạch 5), 10.18–10.21 bỏ trống; (5) giữ "KL trung bình", `4-12` có dòng phân biệt.

Còn mở: bảng mở đầu `exercises.md` đặt 10.5 ở mạch 2, còn `6-16` đặt ở mạch 3 (critic dạy ở mạch 3); dòng "Mức độ" của Bài tập 10.22 trong `exercises.md` còn ghi "mục tiêu học tập 8; mạch 7".


## 10. Ghi chú khi dựng (2026-11-21)

Biên tập viên dựng deck theo các mục 1–9. Chỗ lệch dưới đây đều là rút chữ, đổi chỗ trên trang hoặc chuyển một câu phụ xuống ghi chú diễn giả để trang vừa khung 1280×720 với chữ thân bài .8em (NT-RL-7); không thêm ý, không đổi số. Mọi số trên mặt trang khớp `kiem_so.py`.

**Khung kỹ thuật và CSS** (`lecture-course.css`, bốn nhóm quy tắc mới, chỉ deck 10 dùng; đã `grep` các deck khác: không deck nào có các lớp này, nên không đổi hiển thị của chúng).

- `div.reveal` mang lớp `dense`: công thức KaTeX ở 1,1 lần cỡ chữ quanh nó (thay 1,21), khoảng cách giữa đoạn, công thức hiển thị và hộp nhỏ hơn trên trang `compact`; ảnh có thuộc tính `width` không bị `max-width: 95%` của Reveal thu nhỏ. Lý do: với 1,21 lần, phần lớn trang của storyboard tràn khung 100–300 px.
- `table.calc`: ô không xuống dòng, lề ô `.3em`, công thức trong ô cùng cỡ chữ bảng (.752em, trên mức .75em). Dùng cho mọi bảng tính tay.
- `.grid2.fig-right`, `.grid2.fig-left`: cột hình rộng đúng bằng hình. Hình đặt bằng thuộc tính `width` theo độ rộng tối thiểu trong `hinh/kiem-tra.json` (nhãn ≥ 20 px trên ảnh 1600×900); `gae-weights-trang.svg` đặt 430 (tối thiểu 427, đề xuất 540) vì chiều cao trang `3-02`.
- Mọi trang nội dung có lớp `compact`.

**Lệch so với mặt trang của storyboard.**

| Trang | Lệch | Lý do |
|---|---|---|
| `1-02` | Hai "Nhắc lại:" gộp một đoạn, $\widehat g$ và $\psi_\theta$ viết nội dòng; "Giả thiết chung:" viết thành nhãn "Giả thiết:" kèm *giả thiết chung* in nghiêng | chiều cao; chỉ dùng nhãn được phép |
| `1-09` | $p_s=\sigma(\theta_s)$ nội dòng; câu "Ta cập nhật $\theta$ …" thành "Chính sách và $J$ được đọc qua $(p_A;\,p_B)$." | chiều cao; mặt trang không dùng "ta" |
| `1-10` | hình thu nhỏ đặt dưới bảng, cạnh công thức $J$ | bảng cần cả bề rộng |
| `1-04` | dòng "Tọa độ $\theta_A$ của $\widehat g$ chỉ có số hạng $t=0$" chuyển ghi chú diễn giả (đầu cột ghi $\widehat g_A=G_0\psi_A$); "Nhắc lại:" bỏ $\theta$, $J$ (trang không dùng) | chiều cao |
| `1-05` | tiêu đề "… làm $J$ giảm" thay "… làm hàm mục tiêu giảm"; dòng gradient đúng bỏ công thức $J$ lặp lại, $p$ của $\alpha=2$ và câu cuối (hộp đã nói), $p$ đưa vào ghi chú diễn giả | tiêu đề một dòng; chiều cao |
| `1-06` | hai câu hỏi trong một đoạn của hộp "Câu hỏi:", không danh sách | `deck_lint` STRUCT: "Vấn đề trung tâm" mở đầu chỉ một hộp |
| `1-08` | (hết hiệu lực sau năm vai rà, B6) danh sách mạch nay là `<ol>` có liên kết `#/k`; cột danh sách đã bỏ khỏi `so-do-neo-m1.svg` | NT11 |
| `2-01` | $\widehat g_b$ nội dòng trong định nghĩa | chiều cao |
| `2-02` | hộp bỏ câu thứ ba ($s_A\xrightarrow1s_B\xrightarrow2$ bị phạt) → ghi chú diễn giả; dòng phạm vi rút còn "Mệnh đề chỉ bảo đảm kỳ vọng: …" | hộp ≤ 2 câu; chiều cao |
| `2-07` | tiêu đề "Sai số TD với $v_\pi$ ước lượng không chệch lợi thế"; dòng số trên chuỗi bỏ vì hình `sai-so-td-mot-buoc.svg` ghi đúng hai phép tính đó (TB10); $\delta_t$ nội dòng | tiêu đề một dòng; chiều cao |
| `2-08` | bỏ cột "Xác suất"; hàng hai cột $\delta_0$ ghi "như hàng trên" | bề rộng; trang không tính kỳ vọng (`2-11` ghi xác suất) |
| `2-09` | dòng giả thiết bị vi phạm gộp một câu: "lợi thế $A$ của chính sách đều cho $\sum_a\pi_\theta(a\mid s)A(s,a)=0{,}5\ne0$" | chiều cao |
| `3-06` | bỏ cột $R_1,R_2$ (phần thưởng có trong phép tính hai cột sau); công thức $\delta_0$ và đại lượng cần ước lượng ở dòng "Nhắc lại:"; hàng "độ chệch: kỳ vọng $-\,0{,}4$" thay khối "Lưu ý:"; câu "không phải sai số của một lượt" → ghi chú diễn giả | bề rộng, chiều cao; Đ4 còn trên mặt trang ở dạng công thức của hàng — cần người rà xác nhận |
| `3-02` | thêm "(λ-return)"; $\widehat A_t$ nội dòng, công thức hiển thị chỉ còn $G^\lambda_t$ (`\textstyle`) | tràn công thức ở 390 px; chiều cao |
| `3-11`, `3-04` | công thức của Bước 2, của quy tắc cập nhật viết nội dòng | chiều cao |
| `3-10` | "Dừng sau số lượt đã định" gộp vào dòng "Lặp với mỗi lượt" | chiều cao |
| `4-01` | câu nối "Mỗi lượt của mạch trước chỉ cho một bước nhỏ" → ghi chú diễn giả, "Bước dài cần đánh giá …" vào hộp "Câu hỏi:"; bỏ hàng "xác suất tới $s_B$, bằng $p_A$" (hai thanh của hình cho đúng số này, TB10) → ghi chú diễn giả; hộp rút | chiều cao |
| `4-14` | Bước 2 viết $\mathbb E_{\pi'}[\delta_t]$, "$\delta_t$ là sai số TD với $v_\pi$"; hộp câu hỏi và lời giải đặt cạnh nhau; câu "Chính sách chỉ quyết định $A_t$" → ghi chú diễn giả | chiều cao |
| `4-12` | quy ước $D_{\mathrm{KL}}=+\infty$ khi $\pi'(a\mid s)=0$ → ghi chú diễn giả | nhánh suy biến (TB7); chiều cao |
| `4-07` | bài toán miền tin cậy viết bằng câu có công thức nội dòng | tránh `\text{}` tiếng Việt (NT26) |
| `4-02`, `4-06`, `4-08`, `4-09`, `4-22`, `4-24`, `5-02`, `5-07` | thêm tên tiếng Anh ở lần đầu: performance difference lemma, policy improvement bound, natural gradient, trust region policy optimization, conjugate gradient, backtracking line search, Fisher information matrix, occupancy distribution, clipped objective, proximal policy optimization, mini-batch, early stopping | VP2, NT21 |
| `4-17`, `4-20`, `4-22`, `4-10` | rút vài chữ ("Lợi thế ước lượng làm giá trị không khớp"; nhãn "Mệnh đề." vì tiêu đề đã nêu tên Pinsker) | mật độ, dấu chấm lẻ dòng |
| `5-05` | bỏ cột "Tăng khi" và dòng "Dưới $p_A=0{,}4$ …" → ghi chú diễn giả (khung trái của hình cho thấy cực đại tại $0{,}4$); dòng phạm vi bỏ "(trang sau)" | chiều cao, bề rộng; VP20 |
| `5-12`, `5-13` | tiêu đề "Bài tập: một vòng PPO-Clip trên chuỗi"; "Lời giải:" ở ô đầu bảng; $\ell_s$ viết gọn bằng ngoặc vuông; hàng chạm biên ghi "$0{,}7\overline3$ (hành động 2), $0{,}8$ (hành động 1)" | tiêu đề một dòng; bề rộng |
| `6-11` | hộp nhắc hai câu hỏi viết dạng cụm danh từ ngắn | chiều cao |
| `6-14` | ô "Bảo đảm" của PPO-Clip bỏ "gradient $0$ khi tỉ số ra ngoài theo hướng có lợi" (đã ở `6-13`) → ghi chú diễn giả; xuống dòng thủ công trong ô | chiều cao |
| `6-16` | "10.23 (trên lớp)" | NT15 |

Ghi chú diễn giả theo ý của storyboard, bỏ mọi mã trang, mã Đk/TBk/Nk, câu "Mạch này"; "trang `2-11`" và các chỗ tương tự viết bằng lời. Dòng nguồn dẫn mục của ghi chú theo số mục hiện hành (Ví dụ 10.6, 10.7, Định nghĩa 10.7, Mệnh đề 10.8 ở §2.4; Ví dụ 10.11 ở §4.1; Ví dụ 10.12 ở §4.4).

**Kiểm máy (2026-11-21, máy chủ tĩnh tạm cổng 8841).** `deck_lint.py --course rl-plan`: 33 phát hiện, gồm SYLL60 ở 28 trang, LINES6 ở `2-10`, `3-12`, `3-10`, `4-09`, `5-12` (trang ý tưởng chứng minh, thuật toán, đề bài tập: mục 7), STRUCT "Nội dung có 0 mục" (`1-08`, xem bảng trên). `footer_check.py`: 0 trang. `formula_overflow.py`: 0. Playwright 81 trang × 1600×900 và 390×844, fragment hiện hết: 0 lỗi console, 0 lỗi trang, 0 request lỗi, 0 `.katex-error`, không trang nào cao quá 720 px, không tràn ngang khung 1280; bàn phím (→, ↓, Space, Esc) và liên kết `#/2/1` … `#/6/1` mở đúng trang tiêu đề mạch.

**Mật độ đo thực tế** (`âm tiết/dòng/chiều cao px` theo cách đếm của `deck_lint.py`; chiều cao là chiều cao nội dung trong khung 720). Trần 60 âm tiết (80 cho mục tiêu, nội dung, bảng tổng kết) bị vượt ở các trang có số đậm dưới đây; theo §3a.E bước 7, đây là danh sách để vai người thầy xem lại, không phải tiêu chí đạt.

- `1-01` 41/3/398 · **`1-02` 127/5/652** · **`1-09` 74/5/668** · `1-10` 21/4/679
- `1-11` 39/6/610 · `1-04` 35/3/658 · `1-05` 35/4/656 · `1-06` 37/1/587
- **`1-07` 88/5/459** · `1-08` 0/0/487 · `2-00` 22/1/654 · **`2-01` 71/4/657**
- `2-04` 42/4/531 · `2-02` 60/4/672 · `2-03` 39/4/587 · **`2-06` 80/5/674**
- **`2-09` 73/5/640** · `2-10` 59/7/579 · **`2-07` 70/5/631** · `2-08` 38/3/503
- `2-11` 38/3/612 · `3-00` 19/1/713 · **`3-01` 78/3/596** · `3-06` 47/3/661
- `3-07` 43/5/537 · **`3-02` 74/5/676** · `3-08` 34/5/663 · **`3-11` 77/6/635**
- `3-05` 23/3/512 · `3-09` 56/4/585 · **`3-12` 82/7/621** · `3-04` 41/6/586
- **`3-10` 77/8/629** · `4-00` 23/1/640 · **`4-01` 72/4/661** · `4-13` 40/6/583
- `4-02` 58/5/562 · **`4-14` 86/6/644** · `4-03` 42/5/408 · `4-15` 28/5/646
- `4-16` 23/3/521 · `4-11` 26/6/672 · `4-05` 29/6/547 · `4-23` 44/4/566
- `4-17` 60/5/545 · `4-04` 25/3/601 · `4-10` 36/3/555 · `4-24` 47/5/632
- `4-06` 29/3/413 · **`4-18` 92/6/576** · `4-19` 34/3/553 · **`4-12` 77/6/657**
- `4-20` 57/5/552 · `4-21` 46/5/474 · **`4-07` 74/4/639** · **`4-22` 63/5/647**
- `4-08` 39/4/614 · `4-25` 26/5/504 · **`4-09` 121/7/701** · `5-00` 22/1/640
- **`5-09` 75/5/530** · `5-10` 40/4/567 · `5-01` 18/3/518 · `5-02` 46/3/643
- `5-11` 39/4/433 · **`5-03` 67/3/571** · `5-05` 43/4/640 · **`5-06` 69/4/534**
- **`5-07` 124/6/673** · **`5-08` 79/1/544** · **`5-12` 67/7/644** · `5-13` 28/3/633
- `6-00` 19/1/640 · `6-10` 0/0/517 · **`6-11` 156/6/687** · `6-12` 58/1/498
- `6-13` 51/1/561 · **`6-14` 102/1/610** · **`6-15` 91/5/449** · `6-16` 53/2/470
- **`6-17` 90/7/601**

### Lượt sửa theo năm vai (2026-11-21)

Biên tập viên sửa theo mục B của `ra-soat-nam-vai-2026-11-21.md` (B1–B8) và C5. Không thêm số nào ngoài ghi chú và các số mục B đã kiểm.

**Thứ tự mới.** Mạch 1: `1-01` → `1-02` → `1-09` → `1-10` → `1-11` → `1-04` → `1-05` → `1-12` → `1-06` → `1-07` → `1-08`. Mạch 4: `4-00` → `4-01` → `4-13` → `4-02` → `4-14` → `4-15` → `4-03` → `4-11` → `4-16` → `4-05` → `4-23` → `4-17` → `4-04` → `4-10` → `4-24` → `4-06` → `4-18` → `4-19` → `4-12` → `4-20` → `4-21` → `4-07` → `4-22` → `4-08` → `4-25` → `4-09`.

| Mục | Trang | Đã sửa |
|---|---|---|
| B1 | `1-05`, `1-06`, `6-11` | `1-05`: câu "REINFORCE dùng mỗi lượt cho đúng một bước, vì sau bước đó lượt đã thuộc chính sách cũ." lên hộp; dòng gradient đúng, kèm $p$ của $\alpha=1$ và $\alpha=2$, xuống ghi chú diễn giả. `1-06`: câu hỏi 2 mới, hai câu thành danh sách trong hộp. `6-11`: chép hai câu hỏi dưới nhãn "Câu hỏi:" |
| B2 | `5-00`, `5-01`, `5-02`, `5-03`, `5-05`, `5-06`, `5-07`, `5-08`, `5-11`, `5-12`, `5-13`, `6-14` | dòng dẫn `5-00` dùng "cắt"; `5-01` nêu tuyến tính theo tỉ số và lợi thế sai dấu, mức giảm $0{,}4$ như mạch 1; `5-02` tiêu đề "Mục tiêu cắt", câu nối $\rho_t$ gần 1 → $D_{\mathrm{TV}}$ nhỏ, hình trước định nghĩa, một tên "mục tiêu cắt (clipped surrogate objective)", định nghĩa *đoạn phẳng*; `5-03` "Giả sử $p_B\approx0{,}57$" và lý do không xảy ra trên bộ đệm; `5-05` định nghĩa *vòng trong*, cột "Vòng trong dừng tại" (cực đại $p_A=0{,}4$; đầu đoạn phẳng $p_B=11/15$), lý do dưới $0{,}4$, hộp "Phép cắt không sửa lợi thế ước lượng sai; nó giới hạn mỗi vòng ở $\lvert\rho_t-1\rvert\le\epsilon$", ghi chú diễn giả sửa; `5-06` viết lại theo B2, bỏ "quán tính của bộ tối ưu", ghi chú diễn giả về Engstrom theo Nhận xét 10.42(2), 10.50; `5-07` "(epoch)", câu mở về TRPO, ghi chú diễn giả PPO-Penalty và (9) của PPO 2017; `5-11` "Giả thiết:/Kết luận:", hàng $\widehat A_t=0$, dòng số; `5-12` câu vòng trong và $\pi'$; `5-13`(d) theo $\eta$ và $A_\pi(s_B,\pi')$; `5-08`, `6-14` "Không bảo đảm $J$ tăng" |
| B3 | `2-09`, `2-04` | phản ví dụ chính sách đều trên chuỗi ($\bar A(s_A,\cdot)=(0{,}175;-0{,}175)$, tọa độ $0{,}0875\ne0{,}2$) trên mặt trang; $v(s_B)$, $q(s_A,1)$, $v(s_A)$ ở ghi chú diễn giả; ghi chú diễn giả `2-04` nói phản ví dụ thuộc bài toán một bước |
| B4 | `2-08`, `2-11`, `3-06`, `3-05`, `2-02`, `4-01`, `4-16`, `5-13`, `3-02`, `1-04`, `4-02`, `4-03`, `4-11`, `4-17`, `4-22`, `4-08`, `6-11` và các mục nhẹ | "ước lượng" thay "hệ số" (`2-08` tiêu đề "Ba ước lượng gradient trên chuỗi hai trạng thái", `2-11` cột "Ước lượng (tọa độ $\theta_A$)", hộp mới); `3-06` điều kiện lượt bắt đầu bằng hành động 1, hàng "độ chệch $=$ kỳ vọng $-\,0{,}4$", "Lưu ý:", câu kết về phương sai, tiêu đề rút thành "Hai ước lượng lợi thế khi critic sai" (để vừa khung); `3-05` "xác suất khi $A_0=1$", hộp; `2-02` dòng ô $-0{,}7$, tiêu đề "Trên chuỗi, $b=v_\pi$ giữ kỳ vọng và giảm phương sai"; "xác suất thăm" ở `4-01`, hai SVG `chuoi-ti-le-toi-sB*`, `alt`; `4-16`, `5-13` theo $\eta$, $A_\pi$; `3-02` bỏ "trộn", hai phép tính sau định nghĩa, quy ước $\lambda=1$ câu riêng; cột "chiều đổi của $p_A$" (`1-04`, `2-02`); `4-02`, `4-03`, `4-11` (điều kiện hỗ trợ chuyển về đây), `4-17` ("Lưu ý:", điều kiện áp dụng trong kết luận), `4-22` (câu mở, $F$ chéo, $F_B<F_A$), `4-08` (Giả thiết/Kết luận, $g=\nabla\mathcal L$, định nghĩa gradient tự nhiên), `6-11` (mục 2, mục 4, "Ví dụ chung: chuỗi hai trạng thái."). Nhẹ: `1-02` $\gamma^t$; `1-09`; `1-07` mục tiêu 2, 4; câu hỏi `2-01`, `5-09`; CPI tên đầy đủ (`5-09`); `2-07` tiêu đề "Sai số TD với giá trị đúng và hàm lợi thế", tên đầy đủ TD; "làm chệch ước lượng gradient" (`3-09`, `6-11`, `6-12`); "trang trước" và "=" thay "là" (`4-04`, `4-10`, `4-19`, `4-23`, `4-24`); "tính trực tiếp" thay "thật" (`4-19`, `4-25`); dấu hai chấm lật bài (`5-08`, `5-10`, `6-14`); tên tiếng Anh (tính chất tháp, lợi tức $n$ bước, bán kính cắt, bộ đệm); câu quy trình trong ghi chú diễn giả (`1-07`, `1-09`, `2-01`, `2-11`, `3-10`, `4-04`, `4-16`, `4-25`, `5-08`, `6-10`); `6-10` tiêu đề "Vòng cập nhật chính sách của bài"; ghi chú diễn giả `6-12`, `6-15` bỏ số; $0{,}0536$ (`4-12`, `4-21`, `4-07`); `4-25` làm tròn bốn chữ số; `4-12` $p'_A\to1$; `4-24` "Ký hiệu:" thêm $\sum_s\nu^\pi\le1$ và $\mathbb E_{\nu^\pi}$; `3-09` phép tính độ chệch $+1$; `3-11` kết quả $\lambda=1$; ngắt dòng `4-20`, `5-12` (công thức hiển thị); `4-07` công thức $\bar D_{\mathrm{KL}}(t)$; `2-04` $H_t$ và bước $\sum_a\pi\nabla\log\pi=\nabla\sum_a\pi$; `4-06`, `6-13` bỏ điều kiện hỗ trợ khỏi giả thiết. Không làm: chú thích "cạnh chấm" của `reinforce-truc-so.svg` (tệp hình không thuộc phạm vi được sửa) |
| B5 | mạch 4, `4-15`, `4-01`, `4-24`, `4-12`, `4-07`, `4-21`, `4-25`, `4-09`, `5-07`, `3-01`, `3-04`, `3-07`, `2-00`, `1-12`, `4-04`, `4-19` | thứ tự mạch 4 như trên; `4-15` phản ví dụ $\mu_0$ dùng $\tilde\pi$ ($0{,}1$ và $-0{,}5$); `4-01` câu mở, "Giả sử một bước dài cho …", ghi chú diễn giả; `4-24` câu đầu; `4-12` lý do chọn KL lên đầu, `4-07` chỉ giữ câu nối, ghi chú diễn giả về ràng buộc, $D^{\max}$ và Achiam; `4-21` thêm Hệ quả 10.29 (cải thiện đơn điệu); `4-25` bỏ tên tìm kiếm lùi, thêm dòng "ví dụ dùng $g$, $F$ chính xác"; `4-09` câu mở, "Lưu ý:" về $g^\gamma$, ghi chú diễn giả, tiêu đề "Tối ưu chính sách miền tin cậy (TRPO)" (để thuật ngữ có tên đầy đủ và trang vừa khung); `5-07` câu mở; `3-01` mở bằng bài toán và critic sai; `3-04` critic dạng bảng, hỏi cả critic; `3-07` "Bổ đề." và "Chứng minh."; `2-00` dòng dẫn mới; câu hỏi nhanh mạch 1 ở trang mới `1-12` (không vừa `1-05`, `1-04`); `4-04` "$t\in[0,1]$ là tham số của đoạn thẳng"; `4-19` $\Delta$ vô hướng thành $d$ |
| B6 | `1-08`, `so-do-neo-m1.svg` | bỏ cột danh sách mạch khỏi SVG (viewBox 1620×790, XML hợp lệ); hình 760 px bên trái, `<ol>` sáu mục có `<a href="#/k">` bên phải; `alt` sửa |
| B7 | CSS | giữ `dense`, `table.calc`; ghi ngoại lệ ở mục 7. Thêm một quy tắc: dưới `dense`, cột hình của `.grid2.fig-right`, `.fig-left` lấy `min-content` (ảnh có `width` không còn bị thu theo phần trăm), để chữ đặt dưới hình trong cùng cột xuống dòng theo bề rộng hình |
| B8 | mục 5, mục 9 | thời lượng tính lại; 82 trang thật, 81 trang đếm, 118,5 phút trình chiếu, Bài tập 10.23 tính vào 30 phút bài tập |
| C5 | `6-17` | tài liệu thêm nơi công bố, phụ đề Engstrom, Kakade (2002, NPG), Cover và Thomas (2006), Nota và Thomas (2020), Sutton và Barto §13.3; ghi chú diễn giả đối chiếu ký hiệu ($\eta(\pi)$, $\rho_\pi$, $\delta$, $r_t(\theta)$, $T$, $r_t$) theo bảng ký hiệu của ghi chú |

**Kiểm máy sau lượt sửa** (cổng 8843): `deck_lint.py --course rl-plan` 42 phát hiện (SYLL60 ở 36 trang, LINES6 ở `2-10`, `3-12`, `3-10`, `4-09`, `5-12`, STRUCT danh sách trong hộp ở `1-06`; hết STRUCT "Nội dung có 0 mục"); `footer_check.py` 0 trang; `formula_overflow.py` 0; Playwright 82 trang × 1600×900 và 390×844: 0 lỗi console, 0 lỗi trang, 0 request lỗi, 0 `.katex-error`, không trang nào cao quá 720 px.

---

### Lượt sửa thứ hai (2026-11-21)

Biên tập viên sửa theo mục E của `ra-soat-nam-vai-2026-11-21.md` (E1–E4), `no-ai-slop` chế độ Edit. Số mới chỉ có $\Delta_0=(0{,}3475;\,1{,}3031)$, $D_{\mathrm{KL}}(s_B)\approx0{,}0566$ (điều phối viên đã kiểm) và $g^\gamma=(0{,}2;\,0{,}333)$ của E2; mọi số khác lấy từ ghi chú hoặc trang trước, tính lại trong `kiem_so.py` và một lần chạy riêng ($\sqrt{0{,}02/10{,}6}=0{,}043437$, $\sigma(0{,}3475)=0{,}58601$, $\sigma(\log2+1{,}3031)=0{,}88040$, $\sqrt{0{,}0566/2}=0{,}1682$, $0{,}1\cdot0{,}511+0{,}045\cdot0{,}0566=0{,}0536$, $\rho=(0{,}8;\,1{,}2;\,0{,}8)$ tại $(0{,}4;\,\tfrac{11}{15})$).

**Thứ tự mới.** Mạch 1: `1-01` → `1-02` → `1-09` → `1-10` → `1-11` → `1-04` → `1-12` → `1-05` → `1-06` → `1-07` → `1-08`. Mạch 6: `6-00` → `6-10` → `6-11` → `6-18` → `6-12` → … → `6-17`. Deck 83 trang.

| Mục | Trang | Thay đổi |
|---|---|---|
| E1 | `5-05` | hộp "Phép cắt không sửa lợi thế ước lượng sai."; câu dừng "Trên bộ đệm này, vòng trong dừng khi $\lvert\rho_t-1\rvert=\epsilon$ ở cả ba mẫu, $\rho=(0{,}8;\,1{,}2;\,0{,}8)$." đứng cuối đoạn văn trên hình (hộp hai câu không vừa cột hẹp); bỏ câu "giới hạn mỗi vòng ở $\lvert\rho_t-1\rvert\le\epsilon$" |
| E1 | `1-12` | chuyển lên giữa `1-04` và `1-05`; tiêu đề "Câu hỏi nhanh: bước dài theo lượt $s_A\xrightarrow1s_B\xrightarrow1$"; câu hỏi "$J$ tăng hay giảm?"; lời giải trong hộp (mảnh 1) kèm số $\sigma$; Nhắc lại tách hai câu; ghi chú diễn giả không còn câu quy trình |
| E1 | `1-05` | hộp: cùng $\alpha$, chiều đổi của $J$ phụ thuộc lượt đã thu; với $s_A\xrightarrow2$ ở giới hạn $J$ giảm $0{,}4$; $\widehat g$ không chệch chỉ khi lượt sinh bởi chính sách đang cập nhật, nên REINFORCE dùng mỗi lượt cho một bước. Câu "ở giới hạn $J$ giảm $0{,}4$" bỏ khỏi đoạn trên bảng (trùng hộp) |
| E1 | `1-06` | ghi chú diễn giả: câu 1 từ bảng ba ước lượng, câu 2 từ hai bước dài (`1-12`, `1-05`) thay "hai trang vừa xem"; `alt` hình nhỏ |
| E1 | `1-02` | "*Hệ số* của bước $t$ là số nhân với $\gamma^t\psi_t$, ở REINFORCE là $G_t$."; dòng Giả thiết bỏ hai dấu hai chấm liền nhau |
| E1 | cả deck, "hệ số" | nghĩa khác đổi tên: `3-11` "trọng số của $\gamma^k\delta_{t+k}$", `4-19` bỏ chữ "hệ số" ở hàng $\tfrac{2\gamma\chi}{(1-\gamma)^2}$; ghi chú diễn giả `4-07`, `4-19`, `4-21` "thừa số", `4-17` "hai số", `4-09` "tỉ lệ co", `5-07` "trọng số phạt"; `3-10` "lợi thế GAE $\widehat A_t$" |
| E1 | `6-11`, `6-18` (mới) | khung "Câu hỏi:" là `<ol>` hai câu; "Trả lời câu 1:" mục 1–2 ở `6-11`; `6-18` nhắc câu 2, "Trả lời câu 2:" mục 3–4, dòng "Ví dụ chung của hai câu: chuỗi hai trạng thái."; mục 2 "trên lượt đầy đủ", "$\hat v=v_\pi$"; mục 3 "tính được từ lượt của chính sách cũ", "tiếp xúc $J$"; mục 4 "PPO dùng lại bộ đệm $K$ lần", "không bảo đảm $J$ không giảm"; ghi chú diễn giả chia hai trang |
| E2 | `4-19` | ghi chú diễn giả "$\Delta p_A=0$", tách câu, "vì cận phải đúng cho mọi MDP" |
| E2 | `4-25` | dòng đầu "Ví dụ dùng $g=\nabla\mathcal L$ và $F$ theo $\nu^\pi$. Trung bình trên bộ đệm ước lượng $g^\gamma$, trên chuỗi là $(0{,}2;\,0{,}333)$."; $\Delta_0=0{,}04344\cdot(8;30)=(0{,}3475;\,1{,}3031)$, $p=(\sigma(0{,}3475);\,\sigma(\log2+1{,}3031))=(0{,}5860;\,0{,}8804)$; "thỏa ràng buộc KL và làm hàm thay thế tăng, nên tìm kiếm lùi giữ $\Delta_0$ ($j=0$)"; giữ $0{,}0085$, $0{,}357$, $1{,}807$; ghi chú diễn giả "tính trực tiếp" |
| E2 | `4-12`, `4-20` | $D_{\mathrm{KL}}(s_B)\approx0{,}0566$; `4-12` mở bằng câu bài toán (khoảng cách khả vi theo $\theta$), bỏ câu lặp về trung bình trên bộ đệm; `4-20` ghi chú diễn giả $p'_A\to1$ |
| E2 | `4-09` | "Lưu ý:" $g$ không có $\gamma^t$, nên ước lượng vectơ tỉ lệ với $g^\gamma=\mathbb E[\sum_tA_\pi(S_t,A_t)\psi_t]\ne\nabla J$ |
| E2 | `4-21` | thêm dòng "Chứng minh." của hệ quả cải thiện đơn điệu; Giả thiết "như định lý chặn cải thiện"; dòng Pinsker rút; câu $14{,}7$/$4{,}3$ xuống ghi chú diễn giả |
| E2 | `4-15` | hàng tổng "$J(\tilde\pi)-J(\pi)=-0{,}085$"; hộp "Giá trị tính trực tiếp … trùng tổng của bảng" |
| E2 | `3-07` | quy ước $\delta_k=0$ khi $k\ge T$; dòng chứng minh: $\gamma^{k+1}\hat v(S_{t+k+1})$ của $\gamma^k\delta_{t+k}$ triệt tiêu với $-\gamma^{k+1}\hat v(S_{t+k+1})$ của $\gamma^{k+1}\delta_{t+k+1}$; câu mở và định nghĩa rút để vừa khung |
| E2 | `4-22` | "không có nghiệm dạng đóng"; "$F_B<F_A$ chủ yếu vì $\nu^\pi(s_B)=0{,}045<0{,}1$"; bỏ dấu hai chấm lật bài; Giả thiết bỏ "thêm:" |
| E2 | `4-14` | Bước 1 thêm $r(s,a)=\mathbb E[R_{t+1}\mid S_t=s,A_t=a]$ |
| E2 | ghi chú diễn giả | `2-02` tên cột "chiều đổi của $p_A$"; `6-17` "$h$" là ký hiệu của ghi chú bài giảng |
| E3 | `5-01` | tiêu đề "Hàm thay thế mẫu tuyến tính theo tỉ số nên cực đại nằm ở biên"; hộp không lặp tiêu đề |
| E3 | `5-05`, `5-07` | dòng mở `5-05` định nghĩa *vòng trong* tại chỗ, bỏ "bước 3 của thuật toán, $K$"; `5-07` mục 3 mở bằng "*Vòng trong*, lặp $K$ lần" |
| E3 | `5-11` | dòng số: mẫu $(s_A,1)$ với $\rho=1$ cho $-1{,}4\max(1;\,0{,}8)=-1{,}4$ |
| E3 | `5-03` | "Trên bộ đệm này $p_B$ không giảm, vì mỗi trạng thái có tham số riêng và mẫu duy nhất tại $s_B$ có $\widehat A<0$, chỉ đẩy $p_B$ tăng."; ghi chú diễn giả bỏ câu quy trình |
| E3 | `5-06` | "Trên bộ đệm hai lượt, với $p_A=0{,}4$:"; mục 1 "Phép cắt chỉ đặt gradient của số hạng bằng $0$ khi tỉ số ra ngoài khoảng theo hướng làm số hạng tăng."; mục 2 bỏ dấu hai chấm lật bài; ghi chú diễn giả "động lượng (momentum) của Adam" |
| E3 | `5-02` | định nghĩa một lần "*hướng có lợi*, hướng làm $\rho_t\widehat A_t$ tăng"; vế "$D_{\mathrm{TV}}$ nhỏ" xuống ghi chú diễn giả (vừa khung) |
| E3 | `2-09` | $\bar\pi=(\tfrac12;\,\tfrac12)$ và $\bar A=A_{\bar\pi}$ trên mặt trang |
| E3 | `2-02` | dòng ô $-0{,}7$: $G_0=0<v_\pi(s_A)=1{,}4$ do phần thưởng $0$ ở $s_B$, nên ước lượng giảm $p_A$ dù $q_\pi(s_A,1)=1{,}8>1{,}4$; "Mệnh đề đường cơ sở chỉ bảo đảm kỳ vọng. Đường cơ sở khác có thể tăng phương sai."; câu "Lượt chọn hành động 2 nay giảm xác suất của nó." xuống ghi chú diễn giả (vừa khung) |
| E3 | `4-02` | Ý nghĩa "$J(\pi')-J(\pi)$ là tổng của lợi thế $A_\pi(s,\pi')$ theo trọng số $\eta_{\pi'}(s)$"; Ký hiệu "*số lần thăm có chiết khấu*" (ghi chú không có tên tiếng Anh); dòng số từ `4-15` |
| E3 | `4-16` | tiêu đề "Hàm thay thế dự báo $J$ tăng $0{,}095$ khi $J$ giảm $0{,}085$"; dòng cuối "Điều còn thiếu là sai số $\Delta J-\Delta\mathcal L$ phụ thuộc thế nào vào khoảng cách giữa $\pi'$ và $\pi$."; hộp bỏ câu lặp tiêu đề và dấu hai chấm lật bài; dòng đầu bỏ dấu chấm phẩy |
| E3 | `4-17` | "Ý nghĩa:" dòng riêng; "Lưu ý:" gọi $-0{,}45$ là ước lượng của $A_\pi(s_A,\pi)$, khác giá trị đúng $0$ |
| E3 | `4-13` | Nhắc lại "$\pi'$ là chính sách mới bất kỳ, $\tilde\pi=(0{,}9;\,0{,}5)$ là một trường hợp" |
| E3 | `4-24` | dòng "Trực quan." trước định nghĩa TV (câu chuyển từ ghi chú diễn giả) |
| E3 | `4-19`, `4-07` | `4-19` hộp "Cận đúng nhưng không chặt. Cận chỉ chứng nhận …"; `4-07` câu mở bỏ dấu hai chấm lật bài |
| E3 | `6-15` | câu 2 "số lần thăm có chiết khấu $\eta_{\pi'}$ khác $\eta_\pi$"; câu 4 "Một môi trường dừng mỗi lượt sau $H$ bước, nên nhiều lượt dừng trước khi tới trạng thái kết thúc."; ghi chú diễn giả bỏ "lực kéo về" |
| E3 | hình | `ham-thay-the-tiep-xuc*.svg` (6 tệp) "tính trực tiếp: $\Delta J=\dots$"; `ham-thay-the-mien-tin-cay*.svg` (2 tệp) nhãn "$\Delta J$ tính trực tiếp"; `buoc-dai-mot-luot-nho.svg` "bước dài theo một lượt làm $J$ giảm"; `reinforce-truc-so*.svg` (5 tệp) "số cạnh chấm: xác suất của lượt"; `<title>`, `<desc>`, `alt` (`1-04`, `1-06`, `4-04`, `4-07`, `4-10`) theo chữ mới; XML hợp lệ, chữ nằm trong `viewBox` (đo `getBBox`) |
| E3 | `1-08`, `5-00` | `alt` của `1-08` ghi tên các mạch; mục 5 của `<ol>` "Tối ưu chính sách gần kề (Proximal Policy Optimization, PPO)"; `5-00` dòng dẫn "PPO (Proximal Policy Optimization) cắt tỉ số chính sách …" (`h2` kèm tên đầy đủ làm trang cao 787 px) |
| E3 | mục 1, 3, 5 | đồng bộ số trang, phút, thứ tự; hai ước lượng thời lượng ghi ở mục 5, ngoại lệ chờ tác giả |
| E4 | nhẹ | `1-07` "mức độ"; `2-07` "(temporal-difference error, sai số TD, Bài 05)"; `3-01` "giả sử"; `3-02` định nghĩa lợi tức λ kèm công thức, câu GAE riêng; `3-05` tách dấu chấm phẩy; `3-06` cột "Lượt, xác suất khi $A_0=1$" (gộp hai cột để vừa bề rộng), "có kỳ vọng sai dấu"; `3-10` "Ước lượng REINFORCE có phương sai lớn"; `4-01` ghi chú diễn giả bỏ "nó"; `4-04` câu mở tách hai câu; `5-07` mục 3 hai dòng con; `5-09` "phương pháp lặp chính sách bảo thủ (conservative policy iteration, CPI)", "tích $Fv$ của ma trận Fisher với một vectơ"; `5-12` "tại đó", "Bộ đệm chứa các cặp $(s,a)$ với tần suất hành động bằng $\pi(a\mid s)$"; "tính trực tiếp" thay "thật" ở ghi chú diễn giả `4-06`, `4-08`, `4-09`, `4-25`, `5-13`; câu quy trình bỏ ở ghi chú diễn giả `1-12`, `2-03`, `3-04`, `4-10`, `5-03`, `4-23`, `2-08`, `4-05`, `4-08` |
| E4 | không làm | tên tiếng Anh "điều kiện hỗ trợ" (`4-11`), "bổ đề dịch chuyển" (`4-18`): ghi chú không có |

**Kiểm máy sau lượt sửa thứ hai** (cổng 8843): `deck_lint.py --course rl-plan` 44 phát hiện (SYLL60 ở 37 trang, LINES6 ở `2-10`, `3-12`, `3-10`, `4-09`, `5-07`, `5-12`, STRUCT danh sách trong hộp ở trang "Vấn đề trung tâm"); `footer_check.py` 0 trang; `formula_overflow.py` 0; Playwright 83 trang × 1600×900 và 390×844, chuyển trang tắt, fragment hiện hết: 0 lỗi console, 0 lỗi trang, 0 request lỗi, 0 `.katex-error`, không trang nào cao quá 720 px, không tràn ngang; liên kết mạch và phím điều hướng đúng.

### Lượt sửa thứ ba (2026-11-21)

Biên tập viên sửa theo mục G của `ra-soat-nam-vai-2026-11-21.md` (G1–G3), `no-ai-slop` chế độ Edit. Số mới chỉ lấy từ G (điều phối viên đã kiểm): $\widehat g=(2{,}7\cdot0{,}5;\,0{,}9\cdot3\cdot\tfrac13)=(1{,}35;\,0{,}9)$, $\partial J/\partial p_A=2{,}7p_B-1>0$ khi $p_B\ge\tfrac23$; $\bar v=(1{,}175;\,1{,}5)$; $\eta_{\tilde\pi}=(1;\,0{,}81)$; $g^\gamma=(0{,}2;\,0{,}333)$, $\nabla J=(0{,}2;\,0{,}3)$. Không đổi thứ tự, không thêm trang (83 trang).

| Mục | Trang | Thay đổi |
|---|---|---|
| G1 | `1-05`, `1-06` | tiêu đề "Bước dài theo lượt $s_A\xrightarrow2$ làm $J$ giảm"; hộp theo G1 ("$J$ giảm $0{,}4$ khi $\alpha\to\infty$"; "Sau một bước, lượt đã thu là lượt của chính sách cũ và $\widehat g$ tính từ nó mất tính không chệch, nên …"; "mất tính không chệch" thay "không còn không chệch" để tránh phủ định kép); hình nhỏ `buoc-dai-mot-luot-nho.svg` "bước dài theo lượt $s_A\to2$ làm $J$ giảm", `<title>`, `<desc>`, `alt` |
| G1 | `4-25`, `4-09` | `4-25` dòng đầu "… $F$ tính chính xác theo $\nu^\pi$.", câu cuối "…, nên giữ nguyên."; bỏ tìm kiếm lùi, $j$, $g^\gamma$. `4-09` "Lưu ý:" thêm "Trung bình trên bộ đệm tỉ lệ với $g^\gamma=\dots$. Trên chuỗi $g^\gamma=(0{,}2;\,0{,}333)$, khác $\nabla J=(0{,}2;\,0{,}3)$."; câu mở xuống ghi chú diễn giả, tên tiếng Anh TRPO ở dòng nhãn "Thuật toán" (vừa khung); ghi chú diễn giả rút dưới 150 âm tiết |
| G2 | `1-12` | câu hỏi có đường tính $\widehat g$; lời giải nêu lý do của dấu rồi kiểm bằng số; ghi chú diễn giả "cùng $\alpha=1$", bỏ câu điều hướng, gợi ý xét dấu |
| G2 | `6-11`, `6-18` | câu trả lời dùng `<ul>`; mục 1 "và trên ví dụ chung phương sai giảm" (câu "Với $b=v_\pi$ …" xuống ghi chú diễn giả để vừa khung); mục 3 theo G2 với thừa số $2\gamma\chi_{\pi'}/(1-\gamma)^2$; mục 4 "Với lợi thế ước lượng, cả hai đều có thể làm $J$ giảm."; dòng cuối "Ví dụ chung của bài là chuỗi hai trạng thái."; ghi chú diễn giả `6-11` nêu điều kiện từng câu |
| G2 | `6-15` | khung chỉ "Câu hỏi:"; câu 4 "Một môi trường có giới hạn thời gian cắt ngắn nhiều lượt. Điểm cắt không phải trạng thái kết thúc của MDP, nên GAE bootstrap từ $\hat v$ ở bước cắt. …" |
| G2 | `5-03` | thứ tự: mẫu → $p_B$ không giảm trên bộ đệm này → tham số dùng chung → giả sử $\rho=1{,}3$ |
| G2 | `4-02` | dòng số "$\eta_{\tilde\pi}=(1;\,\gamma\tilde p_A)=(1;\,0{,}81)$ và $1\cdot0{,}32+0{,}81\cdot(-0{,}5)=-0{,}085=J(\tilde\pi)-J(\pi)$" |
| G2 | `4-12` | đoạn mở gọi đủ tên "Phân kỳ Kullback–Leibler (Kullback–Leibler divergence, KL)"; "KL tăng không giới hạn khi chính sách mới gần bỏ một hành động, còn $D_{\mathrm{TV}}\le1$."; tỉ số $0{,}2$ xuống ghi chú diễn giả (số $p'_A=0{,}99$ đã ở đó); định nghĩa "Phân kỳ KL tại $s$ …"; công thức kết thúc bằng dấu chấm |
| G3 | `5-05` | câu dừng "Tại điểm dừng, cả ba tỉ số nằm ở biên khoảng cắt với $\epsilon=0{,}2$, $\rho=(0{,}8;\,1{,}2;\,0{,}8)$."; hộp "…, nên $J$ vẫn giảm." |
| G3 | `5-06`, `5-01`, `5-02` | `5-06` mục 1 "Mục tiêu cắt không chặn KL. …" và "theo hướng có lợi"; `5-01` hộp "$\mathcal L^{\mathrm{CPI}}$ giảm theo $p_A$, tăng theo $p_B$, nên tăng mãi khi $(p_A;\,p_B)\to(0;\,1)$, biên của miền xác suất.", dòng $J$ "theo lượt $s_A\xrightarrow2$"; `5-02` "phần tăng của $\rho_t\widehat A_t$" |
| G3 | `4-24`, `4-13`, `4-16`, `4-17`, `4-04` | `4-24` "Trực quan." không dùng "TV" trước định nghĩa; `4-13` dòng "Ký hiệu:" riêng; `4-16` tiêu đề "…, còn $J$ giảm $0{,}085$"; `4-17` điều kiện "$\eta_\pi$ và $A_\pi$ tính chính xác" vào Giả thiết; `4-04` tách dấu chấm phẩy trong hộp |
| G3 | `2-02`, `2-09` | `2-02` "… chỉ bảo đảm kỳ vọng, còn $b\ne v_\pi$ có thể tăng phương sai." (dạng "Với đường cơ sở khác $v_\pi$, …" làm trang tràn), ghi chú diễn giả "hành động 2"; `2-09` đường tính $\bar v=(\tfrac12(0{,}9\cdot1{,}5+1);\,\tfrac12\cdot3)=(1{,}175;\,1{,}5)$ và $\bar A$ tại $s_A$ |
| G3 | `3-07`, `3-08` | "$\delta_j=0$ khi $j\ge T$, $\hat v(S_T)=0$" |
| G3 | ghi chú diễn giả | `4-21` "$2\cdot0{,}5\cdot\tfrac{0{,}9}{0{,}01}=2\cdot0{,}5\cdot90$"; bỏ câu điều hướng ở `1-10`, `2-01`, `3-07`, `3-08`, `4-06`, `1-12`; `1-06` "Câu trả lời theo mạch:"; `3-10` câu dừng gradient viết lại ("$\widehat A_t$ là hằng số theo $\theta$") |
| G3 | hình | `reinforce-truc-so*.svg` (5 tệp) chú thích hai dòng "số ghi cạnh mỗi chấm là / xác suất của lượt", `alt` của `1-04`; `gae-tinh-lui*.svg` (3 tệp) `<title>` "Tính lùi lợi thế GAE trên lượt (i)"; XML hợp lệ, chữ nằm trong `viewBox` |
| G3 | `5-00`, `5-07` | không lặp tên tiếng Anh của PPO (đã có ở mục 5 của `1-08`): dòng dẫn "PPO cắt tỉ số chính sách …", `5-07` "PPO-Clip, dạng cắt của PPO, …" |
| G3 | storyboard | §3 câu 2 của `1-06` theo deck, mục `1-05`, `1-12`, `4-25`, `4-09`, `6-11`, `6-18`; §5 đánh dấu hai đoạn cũ là lịch sử; §7 thêm hàng `1-08` (`#/1` dẫn tới bìa) và các ngoại lệ mới |

**Kiểm máy sau lượt sửa thứ ba** (cổng 8843): `deck_lint.py --course rl-plan` 45 phát hiện (SYLL60 ở 37 trang; LINES6 ở `2-10`, `3-12`, `3-10`, `4-13`, `4-09`, `5-07`, `5-12`; STRUCT danh sách trong hộp ở trang "Vấn đề trung tâm"); `footer_check.py` 0 trang; `formula_overflow.py` 0; Playwright 83 trang × 1600×900 và 390×844, chuyển trang tắt, fragment hiện hết: 0 lỗi console, 0 lỗi trang, 0 request lỗi, 0 `.katex-error`, không trang nào cao quá 720 px, không tràn ngang; liên kết mạch và phím điều hướng đúng; `git diff --check` sạch.

**Lượt sửa thứ tư (2026-11-21, sau vòng kiểm hẹp).** `6-11` mục 1 "…giữ nguyên kỳ vọng của ước lượng gradient, và trên ví dụ chung, $b=v_\pi$ làm phương sai giảm." (không còn đọc như mọi đường cơ sở đều giảm phương sai); `6-15` danh sách bốn câu hỏi đưa vào khung `div.check` "Câu hỏi:" như `6-11`; ghi chú diễn giả `4-06` "Định lý dùng lợi thế và phân bố chính xác; với đại lượng ước lượng, cận không áp dụng." thay câu "điều kiện áp dụng, không phải giả thiết" (khớp Giả thiết của `4-17`, `4-21`); ghi chú diễn giả `1-10` bỏ con trỏ "được dùng lại ở mạch 2". Kiểm: `deck_lint` 45 phát hiện (không đổi), `footer_check` 0, `formula_overflow` 0, Playwright `6-11`, `6-15`, `4-06`, `1-10` ở hai cỡ: 0 lỗi, không tràn; `git diff --check` sạch.

### Góp ý tác giả #1 (2026-11-21)

Góp ý "cần có công thức của \delta_t" ở `3-10` (`gop-y-tac-gia-deck-2026-11-21.md` #1); quy tắc: mọi đại lượng một bước thuật toán tính ra có công thức trong bước đó (tinh chỉnh TB31). Chỉ dùng công thức của ghi chú (Thuật toán 10.16, 10.37, 10.49, Định nghĩa 10.47) hoặc trang trước.

| Trang | Thay đổi |
|---|---|
| `3-10` | bước 2: $\delta_t=R_{t+1}+\gamma(1-Z_{t+1})\,\hat v(S_{t+1},w_{\mathrm{old}})-\hat v(S_t,w_{\mathrm{old}})$ với $Z_{t+1}=1$ khi $S_{t+1}$ kết thúc, $\widehat A_T=0$, công thức tính lùi. Để vừa khung: câu mở rút một dòng ("phương sai lớn" xuống ghi chú diễn giả), hộp rút một dòng, dòng "Lặp với mỗi lượt…" nhập vào dòng Đầu vào/Đầu ra |
| `4-09`, `4-26` (mới) | tách hai trang "Thuật toán TRPO (1)", "(2)"; tên đầy đủ "tối ưu chính sách miền tin cậy (trust region policy optimization, TRPO)" ở dòng nhãn "Thuật toán". (1): bước 1 giữ $\hat v_{\mathrm{old}}$; bước 2 công thức $\delta_t$, $\widehat A_t$, $V^{\mathrm{targ}}_t$; bước 3 $\rho_t(\theta)$, $\widehat{\mathcal L}(\theta)=\frac1{|\mathcal D|}\sum_t\rho_t(\theta)\widehat A_t$, $\widehat D(\theta)=\frac1{|\mathcal D|}\sum_tD_{\mathrm{KL}}(\pi_{\mathrm{old}}(\cdot\mid S_t)\Vert\pi_\theta(\cdot\mid S_t))$, $g=\nabla\widehat{\mathcal L}(\theta_{\mathrm{old}})=\frac1{|\mathcal D|}\sum_t\widehat A_t\psi_t$, $F$ là Hessian của $\widehat D$. (2): bước 4 tìm kiếm lùi viết đủ điều kiện nhận $j$ và trường hợp không có $j$; bước 5 mất mát của critic theo $V^{\mathrm{targ}}_t$; "Lưu ý:" về $g^\gamma$ giữ nguyên. Ghi chú diễn giả chia hai trang |
| `5-07`, `5-14` (mới) | tách hai trang "Thuật toán PPO-Clip (1)", "(2)". (1): câu mở, Đầu vào/Đầu ra, bước 1, bước 2 với $\delta_t$, $\widehat A_t$, $V^{\mathrm{targ}}_t$. (2): bước 3 với $\rho_t(\theta)$, mục tiêu cắt trên lô $\frac1M\sum_{t\in\mathcal B}\min(\rho_t\widehat A_t,\operatorname{clip}(\rho_t,1-\epsilon,1+\epsilon)\widehat A_t)$, mất mát của critic; bước 4 KL ước lượng (approxKL) $\frac1M\sum_{t\in\mathcal B}[(\rho_t-1)-\log\rho_t]$ |

### Góp ý tác giả #2, #3 (2026-11-21)

Góp ý "công thức cập nhật w cũng chưa nói ở các slide trước" và "tại sao dùng A_t+v làm target". Thêm `3-13` "Critic hồi quy về lợi tức λ" sau `3-12`, trước `3-04` (mục §3). Sửa kèm: `3-04` đề dùng "Nhắc lại:" quy tắc của actor và critic (dạng bảng, $V^{\mathrm{targ}}_t$), dòng dữ kiện rút một dòng, lời giải ghi $V^{\mathrm{targ}}=(1{,}8;\,3)$; `3-10` bước 4 theo $V^{\mathrm{targ}}_t=\widehat A_t+\hat v(S_t,w_{\mathrm{old}})$; `4-09` bước 2 và `5-07` bước 2 gọi "mục tiêu của critic $V^{\mathrm{targ}}_t$", `4-26` bước 5 và `5-14` bước 3 viết mất mát theo $V^{\mathrm{targ}}_t$.

**Kiểm máy** (cổng 8843): `deck_lint.py --course rl-plan` 44 phát hiện trên 86 trang (LINES6 ở `2-10`, `3-12`, `3-04`, `3-10`, `4-13`, `5-12`; STRUCT trang "Vấn đề trung tâm"; còn lại SYLL60); `footer_check.py` 0 trang; `formula_overflow.py` 0; Playwright `3-04`, `3-10`, `3-12`, `3-13`, `4-09`, `4-26`, `5-07`, `5-14` ở 1600×900 và 390×844: 0 lỗi console, 0 request lỗi, không trang nào cao quá 720 px; `git diff --check` sạch.

### Sau kiểm lại góp ý #1–#3 (2026-11-21)

| Trang | Thay đổi |
|---|---|
| `3-13` | thứ tự theo TB27, TB28: bài toán ("Critic xấp xỉ $v_\pi$ chưa biết. Lượt đã thu cho một ước lượng của $v_\pi(S_t)$ để hồi quy.", bỏ chữ "mục tiêu thay thế" trùng với surrogate) → lý do ($G^\lambda_t$ là trung bình có trọng số của các lợi tức $n$ bước, mỗi lợi tức ước lượng $v_\pi(S_t)$; $\lambda$ cân bằng độ chệch và phương sai như ở $\widehat A_t$) → "Định nghĩa. Mục tiêu của critic là $V^{\mathrm{targ}}_t=G^\lambda_t$, tính được là $\widehat A_t+\hat v(S_t,w_{\mathrm{old}})$." → bảng hai hàng → bước hạ gradient → ví dụ. Dạng bảng $w_s\leftarrow w_s+\alpha_w\sum_{t:S_t=s}(V^{\mathrm{targ}}_t-w_s)$; "lợi tức $\lambda$" trong `$…$`; hộp ví dụ gọn một dòng (giá trị critic $1{,}4$, $1$ hiện trong phép cộng) |
| `3-04` | "Nhắc lại:" dạng bảng có $\sum_{t:S_t=s}$ và hàm điểm $\psi(s,1)=(1-p_s)e_s$, $\psi_A(1)=0{,}5$, $\psi_B(1)=\tfrac13$; dòng cập nhật critic trong lời giải viết gọn $w=(1{,}4+0{,}5\cdot0{,}4;\,1+0{,}5\cdot2)=(1{,}6;\,2)$ để vừa khung |
| `3-10` | câu bài toán trở lại mặt trang: "REINFORCE có phương sai lớn. Actor–critic thay lợi tức bằng lợi thế GAE $\widehat A_t$ lập từ critic." (hai câu, không dùng dấu chấm phẩy, TB13) |
| `4-09`, `4-26` | `4-09`: câu bài toán, Đầu vào/Đầu ra (chính sách $\pi_\theta$, critic $\hat v(s,w)$, bán kính $\kappa$, hệ số co $\zeta\in(0,1)$, số lần co tối đa $j_{\max}$), bước 1–2. `4-26`: bước 3, "Lưu ý:" ngay sau bước 3 ("$g$ ở bước 3 không có $\gamma^t$. Với lợi thế đúng, kỳ vọng của $g$ tỉ lệ với $g^\gamma=\dots$. Trên chuỗi …"), bước 4–5; "vài bước hạ gradient". Ghi chú diễn giả chia lại |
| `5-07`, `5-14` | Đầu vào thêm "ngưỡng approxKL (tùy chọn)" (ghi chú, Thuật toán 10.49, không đặt ký hiệu cho ngưỡng nên deck cũng không dùng $d_{\mathrm{targ}}$); critic $\hat v(s,w)$, $\hat v_{\mathrm{old}}(S_t)=\hat v(S_t,w)$; "giữ cố định trong cả $K$ lần qua bộ đệm (bước 3)". Dừng sớm thành ý thứ ba của bước 3: tính approxKL, vượt ngưỡng thì bỏ các lần qua bộ đệm còn lại; "một bước hạ gradient" cho critic; ghi chú diễn giả "bước 3" |

`3-04` thêm sau vòng kiểm: dòng "Lời giải:" nhập vào dòng "Ước lượng lợi thế", cập nhật actor viết theo vectơ $\theta=(0+0{,}4\cdot0{,}5;\,\log2+0{,}9\cdot2\cdot\tfrac13)$, critic $w=(1{,}4+0{,}5(1{,}8-1{,}4);\,1+0{,}5(3-1))=(1{,}6;\,2)$, để trang không chạm chân trang.

**Kiểm** (cổng 8843): `deck_lint.py --course rl-plan` 46 phát hiện trên 86 trang (LINES6 ở `2-10`, `3-12`, `3-13`, `3-10`, `4-13`, `5-12`; STRUCT trang "Vấn đề trung tâm"; còn lại SYLL60); `footer_check.py` 0; `formula_overflow.py` 0; Playwright `3-12`, `3-13`, `3-04`, `3-10`, `4-09`, `4-26`, `5-07`, `5-14` ở hai cỡ: 0 lỗi, không trang nào cao quá 720 px.

### Đổi thuật ngữ "bổ đề chênh lệch hiệu năng" (2026-11-21, góp ý tác giả #4, VP-RL-10)

Tên cũ của bổ đề (ghi ở góp ý #4) đổi thành "bổ đề chênh lệch hiệu năng" (performance difference lemma), giữ viết hoa đúng vị trí: deck 11 chỗ (`1-02` ghi chú diễn giả, `4-02` tiêu đề và khối bổ đề, `4-14`, `4-15` tiêu đề, `4-03`, `4-16`, `4-05` và các ghi chú diễn giả, `6-12` bảng, `6-15` ghi chú diễn giả); `materials/lec-10/lecture-note.md` 7 chỗ trên 6 dòng (mục tiêu 4 "Chênh lệch hiệu năng và hàm thay thế", tiêu đề §4.1, Bổ đề 10.19, bảng tổng kết, hai dòng §7); `outline.md` cả tệp; phần hiện hành của storyboard này (phần lịch sử giữ nguyên). Không có chỗ nào trong SVG `img/lec-10`. Trình xem ghi chú: 0 `.katex-error`, 0 lỗi console, 0 request lỗi, không còn dấu `:::` chưa nhận; tiêu đề trang deck đã đổi (`4-02`, `4-14`, `4-15`) vừa khung.


### Đề xuất TRPO (#5): kế hoạch mạch 4 (2026-11-21)

Người lập kế hoạch deck viết lại §3 mạch 4, thêm §4.5, sửa dòng mạch 4 ở §1, §5, thêm ngoại lệ ở §7 và dòng đối chiếu mã ở §6, theo đề xuất trình bày TRPO của tác giả (`de-xuat-trinh-bay-trpo-2026-11-21.md`; góp ý #5 của `gop-y-tac-gia-deck-2026-11-21.md`) và ghi chú §4–§5 mới. Chưa sửa deck, ghi chú, hình. Bản cũ của §3 mạch 4 chép nguyên ở mục cuối tệp "Lịch sử: mạch 4 trước đề xuất TRPO (2026-11-21)". Số tính lại trong `/tmp/claude-1000/-data-tqlong-lectures/678a7f48-9d80-46cf-a421-67398857f913/scratchpad/m4-plan/kiem.py`.

**Kết quả.** 28 trang (cũ 27), 37,5 phút (không đổi); toàn deck 87 trang thật, 86 trang đếm, 122 phút. Thứ tự: A (`4-01`, `4-27`) → B (`4-13`, `4-02`, `4-03`, `4-11`) → C (`4-16`, `4-04`, `4-10`, `4-17`, `4-28`, `4-12`, `4-07`, `4-21`) → cơ sở lý thuyết (`4-14`, `4-24`, `4-06`, `4-19`, `4-20`, `4-29`; sau cổng storyboard: `4-14`, `4-20`, `4-24`, `4-06`, `4-19`, `4-29`) → D (`4-22`, `4-30`, `4-08`) → E (`4-25`, `4-09`, `4-26`, `4-31`). Bỏ `4-05`, `4-15`, `4-18`, `4-23`; thêm `4-27` … `4-31`; `4-09`, `4-26` giữ nguyên.

**Chỗ lệch so với đề xuất và lý do.**

1. Trang 1 và 2 gộp thành `4-01`. Trên chuỗi, bước theo gradient đúng không làm $J$ giảm, nên hình 2 của đề xuất trái số của ví dụ chung (TB15, TB25); hiện tượng bước dài làm $J$ giảm lấy lại từ `1-05` (bước theo một lượt, $1{,}4\to1{,}22$).
2. Trang 4, 5, 6 gộp thành `4-02`: phép cộng theo bước thời gian trên chuỗi đứng trước bổ đề, hình ba thành phần gọi tên ba thừa số của công thức, thừa số chưa biết tô ở mảnh cuối. Cần thêm `4-13` ($A_\pi(s,\pi')$) đứng trước, vì ba thành phần dùng nó. Tiết kiệm hai trang so với đề xuất.
3. Trang 9 ("đã sửa gì, chưa sửa gì") không thành trang riêng: câu hỏi kiểm tra của đề xuất thành câu hỏi nhanh mở `4-16`, bảng ba thành phần thành lời giải và ghi chú diễn giả. Mục tiêu mẫu $\widehat{\mathcal L}$ để ở ghi chú diễn giả `4-11`, lên mặt trang ở `4-26` và `5-09`.
4. Hình 7 tách đôi: đường dự báo và thực tế ở `4-04`, `4-10`; vùng KL $\le0{,}01$ ở `4-07`, vì KL chưa định nghĩa khi đồ thị độ dài bước xuất hiện (TB11). Đường tính của đoạn thẳng đổi: $A_\pi(s,\pi_t)=t\,A_\pi(s,\tilde\pi)$ cho ba dòng từ số của `4-16`, thay hai trang khai triển `4-05`, `4-23` (cùng số với Ví dụ 10.12; cách của ghi chú ở ghi chú diễn giả).
5. Hình 9 thay nhãn "thay đổi nhỏ/lớn" bằng $t=0{,}25$ và $\tilde\pi$, hai chính sách đã có trên đoạn thẳng (TB25). TV và KL định nghĩa cùng trang (như Định nghĩa 10.23), vì trang (15) cần TV.
6. Trang 15 (`4-21`) mang hệ quả chặn cải thiện theo KL có nhãn và giả thiết (TB28), không chỉ công thức "dạng" như đề xuất; mắt xích được nêu tên ở đây, phát biểu và chứng minh ở cụm lý thuyết ngay sau.
7. Cụm lý thuyết: "định lý chặn cải thiện và ý tưởng chứng minh" là một trang (`4-06`) với dòng "Chứng minh." vì đẳng thức sai số và bổ đề dịch chuyển đã có trang; `4-18` bỏ. "Hệ quả KL" đứng ở `4-21` trước cụm, không lặp trong cụm. "Hệ quả đơn điệu" có trang riêng `4-29` (tách khỏi `4-21` cũ, bỏ ngoại lệ TB6).
8. Hình 11 dựng trên số của chuỗi ($F=\operatorname{diag}(0{,}025;\,0{,}01)$, $g=(0{,}2;\,0{,}3)$), không dùng hình tổng quát (TB25).
9. Trang 19 ("một vòng lặp TRPO") là `4-25`, `4-09`, `4-26` hiện có; sơ đồ H13 không lên mạch 4, đặt ở `5-09` (quyết định 2).
10. Trang 20 tách: "giải quyết gì" thành trạm dừng `4-31` (H14), "còn khó khăn gì" ở `5-09`; `5-09` bỏ câu liệt kê chi phí trùng.
11. Hình 1 (năm bước) không vẽ (TB2, TB11) và không lên `p.strand-keys` (quyết định 3).
12. Ba câu hỏi cho lớp của đề xuất: "10.000 bước" → ghi chú diễn giả `4-01`; "vì sao tỉ số không biến hàm thay thế thành hiệu năng thực" → câu hỏi nhanh `4-16`; "vì sao TRPO ưu tiên $\theta_B$" → ghi chú diễn giả `4-08`. Thêm câu "vì sao không giảm bước học" (bảng câu hỏi của đề xuất §1) → ghi chú diễn giả `4-28`.

**Rủi ro.** (a) Trên chuỗi, bước theo $g$ co về cùng bán kính KL bậc hai cho $J\approx1{,}835>1{,}807$; mọi trang, hình và ghi chú diễn giả chỉ nói về hướng và tỉ trọng, không so $J$ của hai bước. (b) Mật độ `4-02`, `4-07`, `4-12`, `4-21`, `4-29` sát trần (§7); người dựng đo ở 1600×900 trước khi rút. (c) Ghi chú đang được rà song song: số khối theo `doi-so-ghi-chu-2026-11-21.md`, cần đối chiếu lại khi ghi chú chốt. (d) `lec-10-topic-25` của ghi chú mới trùng mã DPO đã ghi "chuyển sang Bài 13" trong `outline.md`.

**Việc tiếp.** Điều phối viên duyệt câu chuyện mạch 4 mới và các câu hỏi ở dưới; vẽ chín hình mới (§4.5) và sửa hai hình; dựng 28 trang; sửa ngoài mạch 4 theo bảng "Ảnh hưởng ngoài mạch 4" (§3 cuối mạch 4); cập nhật `outline.md`; vai người thầy và năm vai rà.

**Câu hỏi cho điều phối viên** (đã trả lời, xem mục sau).

1. Duyệt câu chuyện mạch 4 mới (đầu §3 mạch 4) thay mục mạch 4 của `cau-chuyen-deck-2026-11-21.md`?
2. H13 (`vong-trpo.svg`) đặt ở `5-09` hay bỏ?
3. Năm bước của H1 làm `p.strand-keys` của `4-00` (mạch khác không có) hay để trong storyboard?
4. `1-07` mục tiêu 3 sửa theo câu đề xuất ở bảng ảnh hưởng hay giữ?
5. `6-13` thêm hàng "Bài toán miền tin cậy" (mức giảm tối đa, Hệ quả 10.31) hay giữ bốn hàng?
6. Mã `lec-10-topic-25`: giữ cho §4.3 mới của Bài 10 và đổi câu trong `outline.md` về DPO, hay đề nghị người sửa ghi chú dùng mã chưa dùng?
7. Lời giải câu hỏi nhanh `4-16` thay cho trang riêng của đề xuất 9: tác giả xếp ý này mức "rất cao"; nếu cần trang riêng thì mạch tăng một trang và 1 phút.

### Đề xuất TRPO (#5): quyết định của điều phối viên và đối chiếu ghi chú đã chốt (2026-11-21)

Điều phối viên chấp nhận kế hoạch mạch 4 (28 trang) và các chỗ lệch có lý do ở mục trên; bảy câu hỏi được trả lời như sau (đã ghi vào đầu §3 mạch 4, bảng "Ảnh hưởng ngoài mạch 4", §4.5 và mục `5-09`).

| # | Quyết định | Sửa trong storyboard |
|---|---|---|
| 1 | câu chuyện mạch 4 mới được duyệt | thay mục "Mạch 4" của `cau-chuyen-deck-2026-11-21.md`; bản cũ ở mục "Lịch sử: câu chuyện mạch 4 trước đề xuất TRPO (2026-11-21)" cuối tệp đó |
| 2 | H13 `vong-trpo.svg` đặt ở `5-09`, vòng tìm kiếm lùi màu đỏ | §4.5 (hàng H13), mục `5-09` (hình, dựng dần, câu chi phí bỏ khỏi mặt trang), bảng ảnh hưởng |
| 3 | năm bước H1 không lên `p.strand-keys` | §4.5 "Không vẽ"; chỗ lệch 11 |
| 4 | `1-07` mục tiêu 3 giữ nguyên | bảng ảnh hưởng |
| 5 | `6-13` giữ bốn hàng | bảng ảnh hưởng |
| 6 | `lec-10-topic-25` giữ cho §4.3; mã DPO lấy mã của Bài 13 | bảng ảnh hưởng: biên tập viên sửa dòng 124 và dòng 148 của `outline.md` |
| 7 | đề xuất 9 không có trang riêng; lời giải `4-16` nêu hai cột "đã hiệu chỉnh: phân phối hành động", "chưa hiệu chỉnh: phân bố trạng thái" | mục `4-16` (bảng hai cột trong hộp "Lời giải:"); §7 thêm `4-16` |

Hai việc thêm. (a) `4-11`: "lấy mẫu quan trọng (importance sampling)" thay "lấy mẫu theo trọng số", như Định nghĩa 06.24 và ghi chú §4.2 dòng 1094. (b) Ghi chú diễn giả `4-08` có câu "Gradient tự nhiên chọn hướng theo khoảng cách KL, không bảo đảm $J$ cao hơn trên mọi bài toán."; quy định không so $J$ của hai hướng giữ nguyên.

**Đối chiếu với ghi chú đã chốt** (văn xuôi 32 493 từ; `grep` tiêu đề và khối trên `materials/lec-10/lecture-note.md`). Mục: §4.1 dòng 953, §4.2 dòng 1088, §4.3 "Sai số dự báo theo độ dài bước" dòng 1168, §4.4 dòng 1216, §4.5 dòng 1267, §4.6 dòng 1292, §5.1 dòng 1572, §5.2 dòng 1725, khớp danh sách của điều phối viên. Khối: Ví dụ 10.11 (957), Định nghĩa 10.18 (995), Bổ đề 10.19 (1007), Hệ quả 10.20 (1066), Định nghĩa 10.21 (1098), Mệnh đề 10.22 (1127), Ví dụ 10.12 (1182), Ví dụ 10.13 (1220), Định nghĩa 10.23 (1234), Định nghĩa 10.24 (1271), Mệnh đề 10.25 (1294), Bổ đề 10.26 (1329), Định lý 10.27 (1388), Ví dụ 10.14 (1437), Hệ quả 10.28 (1459), Nhận xét 10.29 (1492), Hệ quả 10.30 (1500), Hệ quả 10.31 (1538), Định nghĩa 10.32 (1580), Mệnh đề 10.33 (1588), Ví dụ 10.15 (1638), Mệnh đề 10.34 (1651), Ví dụ 10.16 (1697), Nhận xét 10.35 (1718), Ví dụ 10.17 (1733), Thuật toán 10.36 (1756), Thuật toán 10.37 (1785), Nhận xét 10.38 (1816): mọi số khối trong dòng nguồn của §3 mạch 4 khớp. Đoạn được dẫn có trong ghi chú: luồng 100 lượt và "Kiểm tra lại" (Ví dụ 10.11), câu học có giám sát (dòng 981), lấy mẫu quan trọng (1094), bảng đóng góp và đẳng thức sai số (§4.3), bảng KL ba phân phối Bernoulli và KL trung bình trên chuỗi (§4.4), ví dụ $\kappa=0{,}01$ và ba mắt xích (§4.5, dòng 1279–1290), đoạn tròn và elip (1576), hai quyết định (1688), tỉ trọng (1712), "Gradient tự nhiên dồn bước về $\theta_B$" (1716), đoạn kết §5.2 (1828). Sửa theo bản chốt: bảng ảnh hưởng ghi tên §4.3 mới. (Đính chính sau cổng storyboard: câu "dạng (14) của Schulman và cộng sự (2015) … có cùng nghiệm" vẫn có trong ghi chú, §4.5 dòng 1277; lượt này đã bỏ nhầm nó khỏi ghi chú diễn giả `4-07`, lượt sau cổng đưa lại.) Ví dụ 10.13 của bản chốt chỉ kiểm $\sigma(1)$ và tỉ số $55$; hai phép chia $\sigma(5)$, $\sigma(6)$ ở `4-28` để trong ghi chú diễn giả, không lên mặt trang.

### Đề xuất TRPO (#5): sửa sau cổng storyboard mạch 4 (2026-11-21)

Cổng storyboard mạch 4: qua có điều kiện. Người lập kế hoạch sửa §3 mạch 4, §4.5, §5, §7 và câu chuyện mạch 4 (`cau-chuyen-deck-2026-11-21.md`) theo các mục của cổng. Không thêm, không bớt trang: vẫn 28 trang; phút cộng theo trang vẫn 37,5.

| Mức | Mục của cổng | Sửa |
|---|---|---|
| nghiêm trọng | `4-01` nhắc `1-05` sai lý do ($\widehat g$ ở `1-05` ngược dấu gradient đúng, $J$ giảm vì sai hướng) | `4-01` dựng lại: câu nối điều còn thiếu của `3-10`; câu nhắc "bước dài theo ước lượng của một lượt cũ làm $J$ giảm"; đoạn $\pi_t$ và $J(\pi_t)=1{,}4+0{,}095t-0{,}18t^2$ trên mặt trang; hộp "hướng làm $J$ tăng" với $1{,}4125$, $1{,}4025$, $1{,}4$ ($t=\tfrac{19}{36}$), $1{,}315$ (Ví dụ 10.12, "Kiểm tra lại", "Diễn giải"); hình mới `ham-thay-the-tiep-xuc-chi-J.svg` (§4.5). `4-04` nhắc đoạn thẳng, chỉ thêm đường $\Delta\mathcal L$. `4-10`: ô $\Delta J$ của hàng $t=0{,}25$ cho sẵn. Câu chuyện câu 1 viết lại |
| nghiêm trọng | `4-25` mất đường tính của $\Delta\mathcal L$ | dòng "Nhắc lại: $A_\pi(s_A,\pi')=0{,}8\Delta p_A$, $A_\pi(s_B,\pi')=3\Delta p_B$, $\eta_\pi=(1;\,0{,}45)$"; $\Delta\mathcal L=1\cdot0{,}8\cdot0{,}0860+0{,}45\cdot3\cdot0{,}2137=0{,}357$ |
| nghiêm trọng | thời lượng | §5: hai ước lượng (37,5 phút cộng theo trang; khoảng 47,5 phút theo cổng) và bảng tám trang có thể rút (−10,5 phút theo cách đếm trang); chờ tác giả, dựng đủ 28 trang |
| trung bình | thứ tự cụm lý thuyết | `4-14` → `4-20` → `4-24` → `4-06` → `4-19` → `4-29`; `4-20` tính $D_{\mathrm{TV}}(s_B)=\tfrac16$; `4-21` bỏ dòng "Chứng minh.", chứng minh Hệ quả 10.28 ở mảnh cuối `4-06` |
| trung bình | `4-09` bước 1 | "lưu $\log\pi_{\mathrm{old}}(A_t\mid S_t)$ và phân phối $\pi_{\mathrm{old}}(\cdot\mid S_t)$" |
| trung bình | `4-07` | 1 phút "trước chỗ $\Delta J$ đổi dấu"; câu dấu và độ lớn tại biên ($0{,}049$ so với $0{,}0012$, khoảng $40$ lần); hàm mục tiêu dạng tỉ số như Định nghĩa 10.24; ngoại lệ ba phần tử mới ở §7; khối $0{,}145$ ở ghi chú diễn giả |
| trung bình | trạm dừng | `4-08` là trạm dừng của cụm D (hộp điều còn thiếu: giải $Fx=g$ chỉ bằng tích $Fv$, kiểm lại bước) |
| trung bình | `4-13`, `4-04` | `4-13` "Dạng khác:" thêm $A_\pi(s,\pi)=0$; `4-04` "$A_\pi(s,\cdot)$ tuyến tính theo phân phối hành động" |
| trung bình | thuật ngữ | "lấy mẫu quan trọng" ở bảng ảnh hưởng (`outline.md`) và `doi-so-ghi-chu-2026-11-21.md` §1; câu chuyện §1 câu 4 và bảng kết quả lên trang: "chênh lệch hiệu năng" |
| trung bình | số không có trong ghi chú | giữ trên deck; đề xuất NT3 dưới đây. `4-24`: kiểm lại $0{,}036$ (dưới đây). `4-06`: "Ý nghĩa:" dùng $\tfrac{2\gamma\chi}{(1-\gamma)^2}=90$. `4-22`: số sigmoid theo ghi chú ($0{,}00665$, $0{,}00332$, $0{,}1201$, $0{,}00245$, lệch $0{,}0049$, $0{,}00087$) |
| nhẹ | `4-28`, `4-22`, `4-21`, H10, H14, `4-16`, sổ sách | `4-28` bỏ $\varepsilon$; `4-22` câu "bài toán tối ưu phi tuyến có ràng buộc"; `4-21` "(chặn cải thiện, policy improvement bound, theo KL trung bình)" (lần đầu dùng thuật ngữ; `4-06` không lặp tên tiếng Anh); H10 mắt xích 3 "định lý chặn cải thiện"; H14 chấm đỏ "ngoài miền"; `4-16` đo mật độ, tràn thì tách trang câu hỏi nhanh ngay sau `4-11`; câu "dạng (14)" của §10 đính chính và đưa lại vào ghi chú diễn giả `4-07`; bảng dạng chứng minh §7 theo số và mã mới; dòng nguồn `4-25` ghi §5.1 và §5.2; trường "Câu" cho sáu trang lý thuyết (câu 4); câu chuyện câu 4 "nơi $\Delta J>0$" |

**Kiểm lại $0{,}036$ ở `4-24`.** Không nhầm. Vế trái của bổ đề là $\lVert\nu^{\tilde\pi}-\nu^\pi\rVert_1=\lvert0{,}1\cdot0{,}81-0{,}1\cdot0{,}45\rvert=0{,}036$ (chỉ $s_B$ đổi; $\nu^{\tilde\pi}(s_A)=\nu^\pi(s_A)=0{,}1$). Sai số $0{,}036$ trong ghi chú là $\Delta J-\Delta\mathcal L$ của bước $\pi'=(0{,}6;\,0{,}8)$: $(0{,}54-0{,}45)\cdot0{,}4$. Hai đại lượng khác nhau trùng số. Trang viết vế trái thành $(1-\gamma)\lvert\eta_{\tilde\pi}(s_B)-\eta_\pi(s_B)\rvert=0{,}1\cdot\lvert0{,}81-0{,}45\rvert$, và ghi chú diễn giả `4-16` không còn nhắc sai số của $\pi'$, nên deck không đặt hai số này cạnh nhau.

**Đề xuất NT3 cho tác giả (số trên deck không có trong ghi chú; ghi chú ở trần số từ nên chưa thêm).** Mọi số dưới đây tính từ ví dụ chung, đường tính có trên trang.

1. `4-14`, dòng bỏ "cùng $\mu_0$" với $\tilde\pi$: vế trái $0{,}5\cdot3-1{,}4=0{,}1$, vế phải $A_\pi(s_B,\tilde\pi)=-0{,}5$ (ghi chú §4.1 dùng $\pi'$: $1$ và $0{,}4$).
2. `4-24`, kiểm bổ đề dịch chuyển với $\tilde\pi$: vế trái $0{,}036$, vế phải $18\cdot0{,}0475=0{,}855$ (ghi chú §4.6 dùng $\pi'$: $0{,}009$ và $0{,}288$; $0{,}0475$ có ở Ví dụ 10.14).
3. `4-30`, tỉ số bán trục $\sqrt{0{,}025/0{,}01}\approx1{,}58$ của elip trên chuỗi.
4. `4-25`, các số nhiều chữ số: hệ số $0{,}04344$, $\Delta_0=(0{,}3475;\,1{,}3031)$, $p=(0{,}5860;\,0{,}8804)$, $\Delta p=(0{,}0860;\,0{,}2137)$, $D_{\mathrm{KL}}=(0{,}0150;\,0{,}156)$, $\Delta\mathcal L=0{,}357$ (ghi chú §5.1 có $0{,}0434$, $(0{,}35;\,1{,}30)$, $(0{,}586;\,0{,}880)$, KL $\approx0{,}0085$, $J\approx1{,}807$).
5. `4-07`, tỉ số $0{,}049/0{,}0012\approx40$ (hai số có trong ghi chú §4.5, tỉ số thì không).

Phương án nếu tác giả không duyệt: (1), (2) đổi sang số của $\pi'$, khi đó $\pi'$ phải lên deck như một chính sách thứ hai (trái quyết định đã chốt ở câu chuyện của bài); (3) bỏ hộp của `4-30`; (4) làm tròn về số của ghi chú, khi đó $0{,}357$ tính lại với $\Delta p=(0{,}086;\,0{,}213)$.

### Ghi chú khi dựng mạch 4 (2026-11-21)

Biên tập viên dựng 28 trang của §3 mạch 4 đúng thứ tự: `4-00`, `4-01`, `4-27`, `4-13`, `4-02`, `4-03`, `4-11`, `4-16`, `4-04`, `4-10`, `4-17`, `4-28`, `4-12`, `4-07`, `4-21`, `4-14`, `4-20`, `4-24`, `4-06`, `4-19`, `4-29`, `4-22`, `4-30`, `4-08`, `4-25`, `4-09`, `4-26`, `4-31`. Bỏ `4-05`, `4-15`, `4-18`, `4-23`. `4-16` không phải tách: sau khi rút câu cuối của lời giải, trang cao 673 px. Toàn deck 87 trang thật, 86 trang đếm; phút giữ như §5 (mạch 4 37,5; tổng 122). Không thu nhỏ chữ: chỗ lệch dưới đây đều là rút câu phụ xuống ghi chú diễn giả hoặc đổi bố cục, vì ở cỡ chữ .8em và KaTeX 1,1em nhiều trang của §3 cao 750–930 px, trong khi `footer_check.py` đòi đáy nội dung dưới khoảng 700 px (đỉnh chân trang). Mọi số trên mặt trang khớp §3 và ghi chú.

**Hình và CSS.**

- Mọi hình đặt bằng thuộc tính `width` không dưới mức tối thiểu của `m4-hinh/kiem-tra.json`: `luong-100-luot*` 620, `ba-thanh-phan*` 900, `dong-gop-tung-trang-thai*` 560, `sigmoid-hai-buoc*` 520, `kl-ba-bernoulli*` 510 (tối thiểu 507; đặt hẹp hơn 560 của §4.5 để cột chữ `4-12` rộng hơn), `chuoi-bon-mat-xich*` 1100, `tron-va-elip*` 740 (tối thiểu 733; §4.5 ghi 760), `ti-trong-hai-thanh-phan` 520, `vong-trpo` 420, `ham-thay-the-tiep-xuc-chi-J` 560, `ham-thay-the-mien-tin-cay*` 440. `ba-truc-giac.svg` dùng lớp `figure short-l` (cao 310, rộng 1033 ≥ 800) để hình căn giữa, ba bảng gần thẳng hàng với ba chú thích chữ HTML (lưới ba cột, TB10: chú thích chỉ ở HTML).
- `lecture-course.css`: quy tắc `.reveal.lecture-deck.dense img[width]` thêm `max-height: none`. Lý do: `max-height: 95%` của theme Reveal làm mọi hình trong `r-stack` hiện bằng 95% kích thước đặt (ví dụ 560 px thành 532 px hiệu dụng, dưới mức tối thiểu), ở cả mạch 1–3, 5. Lớp `dense` chỉ có ở deck 10 (đã `grep`), nên các deck khác không đổi. Sau sửa, đo lại toàn deck: không trang nào cao quá 720 px.
- `tron-va-elip-buoc0.svg`, `-buoc1.svg`, `tron-va-elip.svg`: nhãn "ràng buộc Euclid: ‖Δ‖ ≤ r" thành "ràng buộc Euclid: ‖Δ‖ ≤ hằng số" (ghi chú đã bỏ ký hiệu $r$ vì trùng phần thưởng); `<desc>` sửa tương ứng; ba tệp qua kiểm XML.
- `ham-thay-the-tiep-xuc-chi-J.svg` vẽ trục tung là $J$ (vạch $1{,}3$; $1{,}4$; $1{,}5$), không phải "$J(\pi_t)-1{,}4$" như §4.5, nên không chồng được lên `-buoc2.svg` (nhãn trục khác nhau). Ở `4-04`, bản chỉ có đường $J$ mang `fragment fade-out` và `-buoc2.svg` hiện cùng mảnh 1; ghi chú diễn giả nói trục tung đổi từ $J$ sang $\Delta J=J-1{,}4$. Đề xuất cho lượt sửa hình: vẽ lại theo §4.5 để chỉ thêm đường cam.
- `4-10`: hình câu hỏi mang `fragment fade-out` ở mảnh lời giải, vì hai SVG nền trong suốt chồng nhau làm dấu "?" đỏ còn lộ cạnh điểm $0{,}02375$.
- Alt: theo `m4-hinh/_hinh_m4.json`; bản dựng dần ghi "Thêm …" như các mạch khác. Alt `ham-thay-the-tiep-xuc-loi-giai.svg` ghi $0{,}02375$, alt `ham-thay-the-mien-tin-cay.svg` ghi $0{,}0536$; alt `tron-va-elip*` không dùng $r$.

**Lệch so với mặt trang của §3.**

| Trang | Lệch | Lý do |
|---|---|---|
| `4-00` | ghi chú diễn giả viết "Mạch 4 đánh giá …" thay "Mạch này …" | quy ước ghi chú diễn giả ở đầu §10 |
| `4-01` | câu "Mỗi lượt của mạch trước chỉ cho một bước." xuống ghi chú diễn giả (dự phòng của §7); hộp số giữ độ dốc $0{,}095$, "tăng lúc đầu", $1{,}315$ tại $t=1$ và câu kết; $1{,}4125$, $1{,}4025$, $1{,}4$ tại $t=\tfrac{19}{36}$ là nhãn của hình đặt cạnh hộp (TB10), ghi chú diễn giả đọc lại ba số; hộp ở cột trái cạnh hình, hộp câu hỏi toàn bề rộng, viết gọn "đánh giá $\pi_t$ từ lượt của $\pi$, trước khi chạy $\pi_t$, thế nào?" | chiều cao 803 → 669 px; chân trang |
| `4-27` | "phân phối hành động", "phân bố trạng thái" in nghiêng ở lần đầu | thuật ngữ mới (TB26) |
| `4-03` | không đặt hình ba thành phần thu nhỏ | §3 để tùy người dựng |
| `4-16` | câu cuối của lời giải bỏ "Với $\tilde\pi$," | chiều cao; chân trang |
| `4-04` | dòng $A_\pi(s,\pi_t)$ và dòng $\Delta\mathcal L$ gộp một đoạn; dòng sai số viết $\eta_{\pi_t}(s_B)$ trước rồi đẳng thức tới $-0{,}18t^2$; hộp cạnh hình | chiều cao 754 → 655 px |
| `4-10` | lời giải viết "hiệu $0{,}0125=\Delta J\gt0$: cùng dấu. Sai số nhỏ hơn $(1/0{,}25)^2=16$ lần." | chân trang |
| `4-17` | "Lưu ý:" theo chữ §3 ("cho $-0{,}45$ thay cho $0$"), dấu hai chấm thay dấu chấm phẩy; ghi chú diễn giả nói $-0{,}45$ là ước lượng của $A_\pi(s_A,\pi)$; hộp "phải gần" thay "phải ở gần" | TB13; chân trang |
| `4-12` | dòng số chỉ giữ phép tính của $\tilde\pi$; phép tính $D_{\mathrm{KL}}=0{,}0204$ của $(0{,}6;\,0{,}4)$ xuống ghi chú diễn giả (số có trên hình, TB10); hộp "TV tăng $4$ lần, KL tăng khoảng $25$ lần. KL không bị chặn khi một xác suất mới tiến về $0$.", "$D_{\mathrm{TV}}\le1$" xuống ghi chú diễn giả | chiều cao 815 → 680 px |
| `4-07` | "Ký hiệu:" viết $\nu^\pi=(1-\gamma)\eta_\pi=(0{,}1;\,0{,}045)$ và $\bar D_{\mathrm{KL}}(\pi\Vert\pi')=\mathbb E_{S\sim\nu^\pi}[\dots]$ thay dạng tổng; định nghĩa: "… là" + $\max_\theta\mathbb E[\rho_\theta A_\pi]$ hiển thị + "với ràng buộc …, trong đó $\rho_\theta=\pi_\theta/\pi$" (không `\text{}` tiếng Việt, NT26); "Ý nghĩa:" còn "hàm mục tiêu bằng $(1-\gamma)\Delta\mathcal L$. Ràng buộc giữ chính sách mới gần chính sách cũ.", ý "chọn hành vi có dự báo tốt nhất" xuống ghi chú diễn giả; dòng $\tilde\pi$ bỏ công thức $D_{\mathrm{KL}}(s_B)$ (dự phòng của §7) và "$=0{,}01$" sau $\kappa$ (có trên hình); dòng giải số rút còn "Tại biên $t=0{,}515$, $\Delta\mathcal L\approx0{,}049$ và $\Delta J\approx0{,}0012$ cùng dương, dự báo lớn hơn khoảng $40$ lần.", "giải số $\bar D_{\mathrm{KL}}(\pi_t)=0{,}01$" xuống ghi chú diễn giả; hai dòng cuối là một đoạn hai mảnh | chiều cao 928 → 667 px; câu về dấu và độ lớn tại biên (cổng) giữ trên mặt trang |
| `4-14` | Bước 2 viết "$\delta_t$ theo $v_\pi$", định nghĩa $\delta_t$ xuống ghi chú diễn giả; câu hỏi bỏ "dù lượt chạy theo $\pi'$"; lời giải bỏ chữ "động lực"; dòng bỏ cùng $\mu_0$ viết "vế trái $0{,}1$, vế phải $-0{,}5$", phép tính $0{,}5\cdot3-1{,}4$ và $A_\pi(s_B,\tilde\pi)$ xuống ghi chú diễn giả | chiều cao 750 → 658 px |
| `4-24` | dòng "Chứng minh." tách hai câu (TB13); dòng số viết "vế trái $0{,}1\cdot\lvert0{,}81-0{,}45\rvert=0{,}036$" (giữ dạng hiệu phân bố của cổng), dạng $(1-\gamma)\lvert\eta_{\tilde\pi}(s_B)-\eta_\pi(s_B)\rvert$ xuống ghi chú diễn giả | TB13; chân trang |
| `4-06` | dòng chứng minh hệ quả: "… $\le\sqrt{\tfrac12\bar D_{\mathrm{KL}}}$. Thế vào định lý." thành hai câu | TB13 |
| `4-29` | dòng chuỗi tách hai câu ("… $=360$. Với hằng này, …") | TB13 |
| `4-22` | câu "$F_B\lt F_A$ chủ yếu vì …" của bản cũ không giữ ở đây (đã ở ghi chú diễn giả `4-08`) | §3 không ghi câu này cho `4-22` |
| `4-30` | bài toán xấp xỉ viết bằng câu có công thức nội dòng, thêm $g=(0{,}2;\,0{,}3)$ (hình không ghi số); "Trực quan." bỏ "là các đường thẳng" và hai giá trị $F_A=0{,}025$, $F_B=0{,}01$ (ở `4-22` ngay trước và trong hộp $\sqrt{0{,}025/0{,}01}$), hai giá trị lên ghi chú diễn giả | NT26; chiều cao 765 → 663 px |
| `4-08` | $\Delta^*$ viết nội dòng trong "Kết luận:", "bài toán xấp xỉ" thay chép lại bài toán của `4-30`; "Ý nghĩa:" tách câu thay dấu chấm phẩy; hộp mở bằng "Với $\theta\in\mathbb R^d$ và $d$ lớn" ($d$ chưa có trên deck); hộp cạnh hình | chiều cao 803 → 660 px; TB13, TB11 |
| `4-31` | tiêu đề "TRPO tối ưu dự báo cục bộ theo hình học KL" thay "TRPO dự báo cục bộ, giới hạn thay đổi và đi theo hình học KL"; hộp "Mỗi bộ đệm chỉ cho một bước cập nhật, sau gradient liên hợp và tìm kiếm lùi." | tiêu đề §3 xuống hai dòng ở 1600×900 (TB6); chân trang |
| `5-09` | hình `vong-trpo.svg` nửa trái theo §3 mạch 5; công thức $\rho_t(\theta)$ tách khỏi dòng hiển thị thành dòng "với $\rho_t(\theta)=\dots$"; dòng nguồn thêm §5.2 (Thuật toán 10.37; đoạn kết) | công thức tràn ngang cột phải (1307 px) |

**Ngoài mạch 4.** `5-02` dòng nguồn: "đoạn trước Ví dụ 10.17" thành "đoạn trước Ví dụ 10.18"; `5-03` ghi chú diễn giả và dòng nguồn: Ví dụ 10.18 thành Ví dụ 10.19; `6-18` ghi chú diễn giả: Định lý 10.26, Hệ quả 10.27 thành Định lý 10.27, Hệ quả 10.28. `grep` toàn deck không còn Mệnh đề 10.24, Bổ đề 10.25, Định lý 10.26, Hệ quả 10.27, Nhận xét 10.28, Hệ quả 10.29, Định nghĩa 10.30 theo số cũ; "Ví dụ 10.11" còn ở `4-01`, `4-27`, `4-13` (giá trị thật, luồng 100 lượt, $A_\pi(s,\pi')$: đúng Ví dụ 10.11 mới), chỗ dẫn đoạn thẳng và khai triển đổi thành Ví dụ 10.12. `outline.md`: câu mở, chuỗi định nghĩa → kết quả → phương pháp, hàng mạch 4 (28 trang), tổng 87 trang, bảng thuật ngữ (đoạn thẳng, phân phối hành động, phân bố trạng thái, lấy mẫu quan trọng, bổ đề dịch chuyển phân bố chiếm dụng, cực đại hóa qua hàm chặn dưới; trang lần đầu của TV, phân bố chiếm dụng, chặn cải thiện, cải thiện đơn điệu), quyết định ký hiệu ($\nu^\pi$ từ `4-07`, $\pi_t$), phân loại chủ đề (§4.1–§4.6 mới, `lec-10-topic-25` cho §4.3, `lec-10-topic-12` đổi sang cốt lõi), dòng tổng và dòng 148 phần lịch sử.

**Kiểm máy (2026-11-21, máy chủ tĩnh cổng 8844).** `deck_lint.py --course rl-plan`: 51 phát hiện, ở mạch 4 gồm SYLL60 tại `4-27`, `4-16`, `4-17`, `4-12`, `4-07`, `4-14`, `4-24`, `4-06`, `4-29`, `4-22`, `4-08`, `4-09`, `4-26`, `4-31`, `5-09` và LINES6 tại `4-13`, `4-14` (ngoại lệ §7); không NOTES150. `footer_check.py`: 0 trang. `formula_overflow.py`: 0. Playwright 87 trang ở 1600×900 và 390×844, `transition: none`, hiện hết mảnh: 0 lỗi console, 0 lỗi trang, 0 request lỗi, 0 `.katex-error`, trang cao nhất 713 px (mạch 4: 686 px, `4-06`), không tràn ngang khung 1280. `#/1` … `#/6`, `#/4/1` (trang `4-00`), `#/4/28` (trang `4-31`) đúng; phím Space đi hết 28 trang mạch 4 theo thứ tự rồi sang `5-00`; ↓, →, ←, Esc hoạt động.

**Chiều cao (px, khung 720) sau khi dựng.** `4-00` 640 · `4-01` 669 · `4-27` 567 · `4-13` 636 · `4-02` 651 · `4-03` 548 · `4-11` 663 · `4-16` 673 · `4-04` 655 · `4-10` 644 · `4-17` 662 · `4-28` 634 · `4-12` 680 · `4-07` 667 · `4-21` 618 · `4-14` 658 · `4-20` 552 · `4-24` 665 · `4-06` 686 · `4-19` 646 · `4-29` 666 · `4-22` 669 · `4-30` 663 · `4-08` 660 · `4-25` 555 · `4-09` 539 · `4-26` 674 · `4-31` 663 · `5-09` 619.

### Lượt sửa mạch 4 theo năm vai rà (B2, 2026-11-21)

Biên tập viên sửa mạch 4 và `5-09` theo mục B2 của `ra-soat-mach4-2026-11-21.md`, sau khi ghi chú được sửa theo B1 (gradient lệch $(-0{,}025;\,0{,}3)$ ở §4.2; $(F^{-1}g)_s=\Delta A_s/(1-\gamma)$ và bước theo $g$ cho $J\approx1{,}835$, KL thật $0{,}0093$ ở §5.1; mắt xích "TV kỳ vọng theo $\nu^\pi$" ở §4.5). Số trang và thứ tự không đổi (28 trang). Không thu nhỏ chữ.

**Chữ SVG (chỉ sửa chuỗi, kiểm XML, `<desc>` và `alt` theo).** `chuoi-bon-mat-xich-buoc1/-buoc2/.svg`: khối 2 "TV kỳ vọng theo $\nu^\pi$ nhỏ", mũi tên "Pinsker và Jensen" (bản `-buoc0` chỉ có khối 1, không đổi). `dong-gop-tung-trang-thai(-buoc0).svg`: tiêu đề hai bảng "$\Delta\mathcal L$: số lần thăm $\eta_\pi$", "$\Delta J$: số lần thăm $\eta_{\tilde\pi}$". `ba-thanh-phan(-buoc0).svg`: "số lần thăm có chiết khấu", nhãn dưới "chưa có lượt của $\pi'$". `ba-truc-giac.svg`: thêm nhãn xanh "bước nhận" cạnh chấm xanh. Chữ mới nằm trong khung (xem ảnh 1600×900).

**Lệch hoặc rút khi sửa** (để vừa khung và để `footer_check.py` không báo; câu mức nghiêm trọng và trung bình của B2 đều trên mặt trang, trừ chỗ ghi rõ dưới đây):

| Trang | Việc | Ghi chú |
|---|---|---|
| `4-01` | tiêu đề "Hướng làm $J$ tăng chưa cho biết độ dài bước"; dòng mở rút thành "Mỗi lượt chỉ cho một bước. Bước dài hơn trên lượt đã thu đòi hỏi biết đi bao xa." (câu "Mạch 2–3 cho hướng ít phương sai" xuống ghi chú diễn giả); lý do "công thức cần mô hình của môi trường" đặt ở câu "Thế vào $J=\dots$"; hộp số còn một câu (thông điệp ở tiêu đề) | chiều cao |
| `4-27` | dòng mở "Dữ liệu của $\tilde\pi$ khác dữ liệu của $\pi$ ở hai chỗ."; câu học có giám sát rút, chuyển "Dữ liệu của $\pi$ đánh giá thấp vai trò của $s_B$" lên hộp; tên tiếng Anh action distribution, state distribution | |
| `4-02` | "Ý nghĩa:" một dòng "trong ba thừa số, chỉ $\eta_{\pi'}$ cần lượt của $\pi'$"; dòng trực quan gộp thành một câu; tên tiếng Anh discounted visitation frequency | chiều cao |
| `4-11` | câu nối "trùng hai lợi thế" (nhẹ) để ở ghi chú diễn giả | dòng cuối xuống hai dòng |
| `4-16` | "Lời giải:" đặt ở ô đầu bảng; câu sai số "… nằm ở $s_B$: $\eta$ tăng, $A_\pi(s_B,\tilde\pi)\lt0$"; điều còn thiếu "Sai số này còn phụ thuộc độ dài bước." ở cột trái; đẳng thức sai số cùng mảnh với lời giải | chiều cao |
| `4-04` | dòng sai số viết "$\eta_{\pi_t}(s_B)-\eta_\pi(s_B)=\gamma\Delta p_A=0{,}36t$, sai số là $0{,}36t\cdot(-0{,}5t)$"; dạng đầy đủ của đẳng thức sai số xuống ghi chú diễn giả | chiều cao |
| `4-28` | tiêu đề "Cùng $\Delta\theta$, hai mức thay đổi phân phối hành động" (bản "… mức thay đổi phân phối hành động" đầy đủ xuống hai dòng); câu hỏi dẫn của văn học thuật không thêm, dòng mở hiện có giữ | TB6 |
| `4-12` | dòng số đưa lên trên lưới; hộp "Từ $t=0{,}25$ tới $\tilde\pi$, TV tăng $4$ lần, KL tăng khoảng $25$ lần. KL trơn theo $\theta$, TV không khả vi tại $\pi'=\pi$, nên TRPO ràng buộc KL, còn Pinsker giữ cận theo TV."; dòng trực quan rút | chiều cao |
| `4-07` | dòng mở "Cần chọn chính sách có $\Delta\mathcal L$ lớn nhất mà vẫn gần $\pi$."; $\kappa=0{,}01$ ở định nghĩa; $D_{\mathrm{KL}}(s_B)$ có đường tính; "Nghiệm của $\bar D_{\mathrm{KL}}(\pi_t)=0{,}01$ là $t=0{,}515$, nơi $\Delta\mathcal L\approx0{,}049\approx41\,\Delta J$"; tổng $0{,}145\le1$ và "tổng có trọng số" trong dòng Ký hiệu. Rút: "Ý nghĩa: hàm mục tiêu bằng $(1-\gamma)\Delta\mathcal L$" (không thuộc B2) và giá trị $\Delta J\approx0{,}0012$ xuống ghi chú diễn giả; tên tiếng Anh occupancy distribution bỏ (ghi chú không có) | trang chật nhất của mạch; nếu tác giả muốn giữ cả "Ý nghĩa:" trên mặt trang thì phải tách trang |
| `4-21` | dòng mở "Câu hỏi:"; nhãn hệ quả "(chặn cải thiện theo KL trung bình, policy improvement bound; từ định lý chặn cải thiện và Pinsker)"; "Ý nghĩa: số hạng phạt tỉ lệ với $\sqrt{\bar D_{\mathrm{KL}}}$, về $0$ khi $\kappa\to0$. Với $\tilde\pi$, nó là $14{,}7\gt0{,}095$."; phép tính $90\sqrt{0{,}0536/2}$ và nguồn Achiam (2017, Hệ quả 1, 3) ở ghi chú diễn giả; hình đặt 1000 px (tối thiểu) | chiều cao |
| `4-14` | dòng "Nhắc lại:" phát biểu bổ đề; Bước 2 có $\delta_t=R_{t+1}+\gamma v_\pi(S_{t+1})-v_\pi(S_t)$; Bước 3 viết $\sum_{t<K}\gamma^t\delta_t=\dots$; "Lưu ý: bổ đề cần cùng $\mu_0$ …" có đường tính $0{,}5\cdot3-1{,}4=0{,}1\ne-0{,}5$. Rút: $r(s,a)$, "không chứa $\pi'$", quy ước $v_\pi(S_T)=0$ xuống ghi chú diễn giả | chiều cao |
| `4-20` | "Ý tưởng chứng minh." thay "Chứng minh."; ghi chú diễn giả thêm phản ví dụ $\pi=(1-\varepsilon;\,\varepsilon)$, $\pi'=(1;\,0)$ | |
| `4-24` | trực quan theo TV kỳ vọng, một câu; vế trái $(1-\gamma)\lvert\eta_{\tilde\pi}(s_B)-\eta_\pi(s_B)\rvert$ | |
| `4-19` | $\Delta p_B$ thay $d$; tiêu đề "Cơ sở lý thuyết: chặn cải thiện đúng nhưng lỏng" | |
| `4-29` | $\pi'$ thay $\pi$; $\bar\chi_k\ge\chi_{\pi'}$ trong giả thiết; $\bar\chi=\lvert A_\pi(s_B,2)\rvert=2$; hộp "Schulman và cộng sự (2015) chứng minh cận với KL lớn nhất theo trạng thái, còn KL trung bình là xấp xỉ kinh nghiệm."; "(minorize–maximize, MM)" ở ghi chú diễn giả; câu "bước dài hơn, $J$ có thể giảm" xuống ghi chú diễn giả | chiều cao |
| `4-22` | dòng "Nhắc lại:" bài toán miền tin cậy và $\nabla\mathcal L=\nabla J$; dòng mở tách câu | |
| `4-30` | $\Delta\theta_A$, $\Delta\theta_B$; câu hỏi ở ghi chú diễn giả trả lời bằng tính bất biến | |
| `4-08` | "Ký hiệu:" gradient tự nhiên đứng trước mệnh đề, cùng đoạn; dòng "Ở đây" theo $(F^{-1}g)_s=\Delta A_s/(1-\gamma)$ và thừa số $\nu^\pi(s_B)$; hộp "Khi số tham số $d$ lớn, giải $Fx=g$ gần đúng chỉ bằng tích $Fv$, rồi kiểm lại bước." (câu "lập và nghịch đảo $F$ quá tốn" xuống ghi chú diễn giả); hình 507 px (tối thiểu) | chiều cao |
| `4-25` | "Lưu ý:" bước theo $g$ ($J\approx1{,}835$, KL thật $0{,}0093$) và câu của B1.3; $\theta_{\mathrm{old}}$ trong "Nhắc lại:"; KL theo trạng thái $(0{,}0150;\,0{,}156)$; hệ số $0{,}043437$ | |
| `4-09` | "cực đại hóa"; bước 1 có động từ "thu"; "$\widehat A=0$ sau cuối bộ đệm"; tham số $k_{\max}$ | |
| `4-26` | "xấp xỉ tỉ lệ" | |
| `4-31` | tiêu đề "Hàm thay thế, miền tin cậy và gradient tự nhiên"; câu thông điệp rút gọn trên mặt trang "TRPO dự báo $J$ từ lượt cũ, giới hạn bước trong miền KL và tìm bước tốt nhất ở đó." (câu đầy đủ ở ghi chú diễn giả); chú thích "nơi sai số của dự báo bị chặn theo KL", "hướng tốt nhất của bài toán xấp xỉ bậc một–bậc hai"; hình lớp `figure short` (rộng 867 ≥ 800) | chiều cao |
| `5-09` | bỏ "ứng viên": "Hàm thay thế mẫu $\widehat{\mathcal L}$ ở bước 3 của TRPO, viết theo tên phương pháp lặp chính sách bảo thủ (…, CPI), là" | |

Mục nhẹ chưa làm: `4-06` chứng minh tách dòng có nhãn (trang cao 686 px, không còn chỗ); `4-17` đường tính $\nabla J$ và $\psi(s,2)$ (không thuộc B2); ghi chú diễn giả 4-00, 4-13, 4-27, 4-28 chỉ sửa chỗ khẩu ngữ đã nêu.

**Đề xuất NT3 bổ sung (số trên deck không có trong ghi chú).** (6) `4-26`: $g^\gamma=(0{,}2;\,0{,}333)$ trên chuỗi. (7) `4-04`: $\eta_{\pi_t}(s_B)=0{,}45+0{,}36t$, hiệu $\gamma\Delta p_A=0{,}36t$ (ghi chú có $(0{,}32t;\,-0{,}5t)$ qua $0{,}8\cdot0{,}4t$, $1{,}35\cdot\tfrac t6$). (8) `4-07`: tỉ số $0{,}049/0{,}0012\approx41$; tại $t=0{,}515$, $D_{\mathrm{KL}}(s_A)=0{,}093$, $D_{\mathrm{KL}}(s_B)=0{,}0155$ (ghi chú diễn giả); thang $\kappa=0{,}01$ so với kỳ vọng chuẩn hóa $\approx0{,}07$ (ghi chú diễn giả). (9) `4-17`: kỳ vọng của lợi thế ước lượng tại $s_B$, $(2;\,-1)$, đã có trong ghi chú sau B1; không còn đề xuất. (10) `4-21`: $\sqrt{0{,}0268}\approx0{,}164$ (ghi chú có $14{,}7$). (11) `4-25`: hệ số $0{,}043437$ và KL theo trạng thái $(0{,}0150;\,0{,}156)$ (đã ở đề xuất 4). Bước theo $g$ ($J\approx1{,}835$, KL $0{,}0093$, $\Delta\approx(0{,}649;\,0{,}973)$) nay có trong ghi chú §5.1, không còn là đề xuất.

**Lệch thứ tự Taylor trước hình học.** Đề xuất của tác giả (trang 16–17) và đoạn trực quan của ghi chú §5.1 đặt hình tròn/elip trước Định nghĩa 10.32; deck đặt `4-22` (xấp xỉ bậc một, KL bậc hai, ma trận Fisher) trước `4-30` (elip). Lý do: elip của `4-30` vẽ theo $F=\operatorname{diag}(0{,}025;\,0{,}01)$ và tỉ số bán trục $\sqrt{F_A/F_B}$, nên cần $F$ và dạng $\tfrac12\Delta^\top F\Delta$ trước (TB24, TB29). Giữ thứ tự của storyboard §3.

**Kiểm máy (2026-11-21, máy chủ tĩnh cổng 8844, đã tắt).** `deck_lint.py --course rl-plan`: 55 phát hiện, mạch 4 chỉ SYLL60 và LINES6 (`4-13`, `4-14` 8 dòng, `4-25`), không NOTES150. `footer_check.py`: 0. `formula_overflow.py`: 0. Playwright 87 trang ở 1600×900 và 390×844, tắt chuyển trang, hiện hết mảnh: 0 lỗi console, 0 lỗi trang, 0 request lỗi, 0 `.katex-error`, cao nhất 713 px (`3-00`), mạch 4 cao nhất 694 px (`4-29`), không tràn ngang khung 1280. Liên kết `#/1`…`#/6`, `#/4/1`, `#/4/28` và phím điều hướng đúng. `git diff --check` sạch.

### Lượt sửa C (2026-11-21)

Biên tập viên làm tám mục ở mục C của `ra-soat-mach4-2026-11-21.md`, sau khi ghi chú §5.1 (dòng ~1714) được sửa.

1. `4-08`: dòng "Ở đây" viết $(F^{-1}g)_s=\bigl(A_\pi(s,1)-A_\pi(s,2)\bigr)/(1-\gamma)$, tức $0{,}8/0{,}1=8$ và $3/0{,}1=30$, rồi câu "Vì $g_s=F_{ss}(F^{-1}g)_s$ với $(F_{AA};\,F_{BB})=(0{,}025;\,0{,}01)$, thành phần $s_B$ của $g$ có thừa số nhỏ hơn, chủ yếu do $\nu^\pi(s_B)=0{,}045\lt0{,}1$. Gradient tự nhiên chia cho $F_{ss}$." Ghi chú diễn giả theo. Để vừa khung: hình H12 đặt cạnh "Chứng minh." và "Ý nghĩa:"; nhãn mệnh đề còn "Mệnh đề." (tên "bước gradient tự nhiên" bỏ vì dòng "Ký hiệu:" ngay trước đã gọi tên); giả thiết viết $g\ne0$; dòng chứng minh bỏ vế giữa $\langle F^{-1}g,\Delta\rangle_F$ (xuống ghi chú diễn giả); "Ý nghĩa:" rút thành "hai quyết định, hướng $F^{-1}g$ và độ dài tới biên elip" (công thức độ dài đã ở kết luận, nhắc ở ghi chú diễn giả).
2. `4-07`: "Ý nghĩa: hàm mục tiêu bằng $(1-\gamma)\Delta\mathcal L$" lên lại mặt trang (cuối dòng ràng buộc); bỏ ", không phải trung bình mẫu" (xuống ghi chú diễn giả). Trang cao 698 px trong khung 720; `footer_check.py` báo trang chạm đúng mép trên chân trang (863/863 px ở 1600×900), không tràn khung. Dòng $\tilde\pi$ ba dòng vì "$\gt\kappa$" xuống dòng riêng. Chưa tách trang (theo chỉ đạo); chờ điều phối viên quyết.
3. `4-17`: "Lưu ý:" viết "Với critic $(1{,}4;\,1)$ và $\lambda=0$, gradient thành $(\dots)=(-0{,}025;\,0{,}3)\ne\nabla J$", không dùng $\widehat{\mathcal L}$.
4. `4-12`: hộp viết "…, nên TRPO ràng buộc KL, và KL nhỏ kéo theo TV nhỏ (bất đẳng thức Pinsker)."
5. `4-01`: "Muốn dùng lại lượt đã thu cho một bước dài hơn thì phải biết đi bao xa."; "Theo mô hình của môi trường, $J=2{,}7p_Ap_B+1-p_A$, nên".
6. `5-09`: "Hàm thay thế mẫu $\widehat{\mathcal L}$ ở bước 3 của TRPO được ký hiệu là $\mathcal L^{\mathrm{CPI}}$, theo tên phương pháp lặp chính sách bảo thủ (…):".
7. `4-25`: "Lưu ý:" còn hai câu đầu.
8. Khẩu ngữ: ghi chú diễn giả `4-01` (câu hỏi "bước cập nhật dài mà $J$ không giảm", lời giải "trước khi thu lượt của nó"), `4-11` ("không cần lượt của $\tilde\pi$"), `4-24` (TV kỳ vọng theo $\nu^\pi$; "trạng thái kết thúc"), `4-27` ("Trong $100$ lượt của $\pi$, chỉ $50$ lượt tới $s_B$"), `4-28` ("nơi hàm sigmoid dốc nhất", "gần bão hòa", "phân phối hành động"), `4-08`; mặt trang `4-07` "Cần tìm chính sách có $\Delta\mathcal L$ lớn nhất trong một vùng quanh $\pi$". `<title>` của `dong-gop-tung-trang-thai(-buoc0).svg` đổi "mức thay đổi thực tế" thành "mức thay đổi tính trực tiếp" (kiểm XML).

Ghi chú diễn giả rút để dưới 150 âm tiết: `4-01` (câu "$\tilde\theta$ hữu hạn"), `4-07` (câu mở và "$\kappa$ là siêu tham số"), `4-08` (câu "tối ưu bài toán xấp xỉ", đã ở `4-25`).

**Kiểm (máy chủ cổng 8844, đã tắt).** `deck_lint.py --course rl-plan`: 54 phát hiện, không NOTES150. `footer_check.py`: 1 trang chạm mép (`4-07`, xem mục 2). `formula_overflow.py`: 0. Playwright 87 trang ở 1600×900 và 390×844, tắt chuyển trang: 0 lỗi console, 0 lỗi trang, 0 request lỗi, 0 `.katex-error`, cao nhất 713 px (`3-00`), mạch 4 cao nhất 698 px (`4-07`), không tràn ngang. `git diff --check` sạch.

### Tách `4-07` thành `4-07` và `4-32` (2026-11-21, quyết định của điều phối viên)

Sau lượt sửa C, `4-07` chạm mép trên chân trang. Điều phối viên quyết tách, nội dung giữ nguyên. `4-07` "Bài toán miền tin cậy" còn dòng mở, "Ký hiệu:" (đưa lại cụm "không phải trung bình mẫu"), "Định nghĩa." (bỏ "(ở đây $\kappa=0{,}01$)", số này sang `4-32`) và hộp "Ý nghĩa:" với $(1-\gamma)\Delta\mathcal L$ và câu ràng buộc giữ chính sách mới gần chính sách cũ. `4-32` "Ví dụ: miền tin cậy $\kappa=0{,}01$ loại $\tilde\pi$" mới: "Nhắc lại:" $\nu^\pi$ và $D_{\mathrm{KL}}(s_A)=0{,}511$ (TB24, Đ1), đường tính $D_{\mathrm{KL}}(s_B)$ và $\bar D_{\mathrm{KL}}(\tilde\pi)=0{,}0536\gt\kappa$, hộp nghiệm $t=0{,}515$ với $\Delta\mathcal L\approx0{,}049\approx41\,\Delta J$, hình `ham-thay-the-mien-tin-cay*`. Ghi chú diễn giả chia đôi (91 và 53 âm tiết theo cách đếm bỏ công thức). Phút: `4-07` 0,75, `4-32` 0,75; mạch 4 29 trang, 37,5 phút; toàn deck 88 trang thật, 87 trang đếm, 122 phút. Ngoại lệ mật độ: `4-07` SYLL60 79 (dòng Ký hiệu hai đối tượng và hộp ý nghĩa hai câu; trang trung tâm của mạch).

**Kiểm (máy chủ cổng 8844, đã tắt).** `footer_check.py`: 0. `formula_overflow.py`: 0. `deck_lint.py --course rl-plan`: 55 phát hiện trên 88 trang, mới chỉ có SYLL60 ở `4-07`. Playwright `4-12`, `4-07`, `4-32`, `4-21` ở 1600×900 và 390×844: 0 lỗi, chiều cao 650, 564, 456, 678 px, không tràn ngang. `#/4/1` mở `4-00`, `#/4/29` mở `4-31`; phím Space đi hết 29 trang mạch 4 rồi sang `5-00`. `git diff --check` sạch.

# Lịch sử (bản 2026-11-20)

Phần dưới là storyboard bản 2026-11-20 (bảy mạch, có hành lang và DPO), giữ nguyên chữ, mọi tiêu đề hạ một bậc. Không còn hiệu lực; chỉ để đối chiếu nhật ký rà.

## Storyboard Bài 10: TRPO, PPO và DPO (dựng lại theo TB1–TB23)

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

### 1. Câu chuyện của bài (đã duyệt, chép nguyên)

1. Trên hành lang ngắn, ba lượt REINFORCE cho ba hướng cập nhật khác nhau (tọa độ thứ nhất $-5{,}5$; $-1$; $1$, trong khi gradient đúng là $2$), và một bước theo đúng gradient nhưng quá dài kéo $J$ từ $-12$ xuống khoảng $-21$.
2. So lợi tức với giá trị của trạng thái thì hướng trung bình giữ nguyên mà dao động giảm; nếu một hàm giá trị (critic) đánh giá đúng, mỗi bước cho ngay hệ số đúng: trên chuỗi hai trạng thái, cả ba loại lượt cùng cho $0{,}2$.
3. Critic học dở thì đánh giá một bước bị lệch, còn lợi tức cả lượt không lệch nhưng dao động; GAE trộn hai cách bằng một tham số $\lambda$.
4. Muốn đi bước lớn bằng dữ liệu cũ, ta đoán $J$ của chính sách mới bằng hàm thay thế; trên chuỗi, hàm thay thế báo tăng $0{,}175$ trong khi $J$ thật giảm $0{,}05$, nên chỉ được tin nó khi chính sách mới ở gần chính sách cũ: đó là miền tin cậy, mà TRPO giải bằng gradient tự nhiên.
5. PPO giữ chính sách mới ở gần bằng cách cắt tỉ số xác suất, nên chỉ cần Adam: trên $s_B$, mục tiêu cắt nằm ngang từ $p=0{,}8$.

   *Sửa theo cổng (2026-11-20, lệch so với câu chuyện đã duyệt):* câu 5 thành "Lợi thế ước lượng từ ít lượt có thể sai dấu, và tối đa hàm thay thế mẫu thì đi tới tận biên: trên chuỗi, một bộ đệm hai lượt đẩy $p_A$ về $0$ và $J$ giảm $0{,}4$. PPO cắt tỉ số xác suất nên chỉ cần Adam: với cùng bộ đệm, vòng dừng ở $(0{,}4;\,0{,}73)$ và $J$ chỉ giảm $0{,}008$; trên $s_B$, mục tiêu cắt nằm ngang từ $p=0{,}8$."
6. Khi chỉ có người so sánh hai câu trả lời, ta khớp phần thưởng từ các so sánh và phạt việc rời mô hình ban đầu; RLHF (dùng PPO) và DPO (một hàm mất mát phân loại) cùng đi tới một chính sách, trên ví dụ là $(\tfrac45;\tfrac15)$.

Trong các mục trang dưới đây, "Câu k" chỉ câu thứ k ở trên; "Câu M" chỉ phần mở đầu của câu chuyện (câu hỏi trung tâm, mục tiêu, nội dung), "Câu T" chỉ phần tổng kết.

---

### 2. Bảng mạch

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

### 3. Sơ đồ neo (TB2) và trạng thái ở từng mạch

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

### 4. Ví dụ chạy và thông điệp (TB14–TB16)

| Mạch | Ví dụ | Thông điệp (một câu) | Số trên trang | Bẫy cần tránh (từ câu chuyện, mục 4.1) |
|---|---|---|---|---|
| 1 | hành lang, ba lượt, hai bước | Một lượt cho một hướng ngẫu nhiên; bước đúng hướng mà dài vẫn làm $J$ giảm. | $-1$; $1$; $-5{,}5$ quanh $2$; $-12\to-11{,}7$; $-12\to-21{,}3$ | không dùng hành lang cho đường cơ sở (trên hành lang, trừ $v_\pi$ làm lượt (b) đổi chiều) |
| 2 | chuỗi, ba loại lượt | So với giá trị của trạng thái, hệ số ít dao động mà trung bình giữ nguyên; critic đúng cho hệ số đúng ngay. | cột $1{,}35;0;-0{,}5$ → $0{,}65;-0{,}7;0{,}2$ → $0{,}2;0{,}2;0{,}2$; trung bình $0{,}2$; phương sai $0{,}69$; $0{,}20$; $0$; xác suất sai dấu $\tfrac12$; $\tfrac16$; $0$ | ghi phương sai cả cột và xác suất sai dấu, vì lượt thứ hai xấu đi ($0\to-0{,}7$); chỉ tọa độ $\theta_A$ |
| 3 | chuỗi, critic $(1{,}4;1)$, hai lượt | Một bước: đều nhưng lệch; cả lượt: không lệch nhưng dao động; $\lambda$ ở giữa. | $-0{,}5;-0{,}5$; $1{,}3;-1{,}4$; $0{,}4;-0{,}95$; trung bình $-0{,}5$; $-0{,}05$; $0{,}4$ | hàng "trung bình" bắt buộc, vì lượt (i) với $\lambda=0{,}5$ cho đúng $0{,}4$ do trùng hợp |
| 4 | chuỗi, bước $(1;0{,}5)$, $(0{,}7;0{,}6)$ | Hàm thay thế đoán đúng khi bước ngắn, có thể sai chiều khi bước dài đổi nơi chính sách tới. | $+0{,}175$ so với $-0{,}05$; $+0{,}07$ so với $+0{,}034$; $(8;30)$ | ghi "tại $p'_A=1$, KL ở $s_A$ vô hạn" ở ghi chú diễn giả của `L10-4-07` |
| 5 | chuỗi, bộ đệm hai lượt; $s_B$ với bộ đệm $1,1,2$ | Lợi thế ước lượng từ ít lượt sai dấu đẩy chính sách đi xa; cắt giới hạn mỗi vòng đi bao xa, nhưng không chặn KL. | $-1{,}4$ so với $+0{,}4$; không cắt $J$ giảm $0{,}4$, có cắt giảm $0{,}008$; $3p-2$; mốc $0{,}73$, $0{,}8$; mức phẳng $0{,}27$; KL $0{,}049\to0{,}10$ | trên $s_B$ đứng riêng, hàm thay thế bằng đúng $J-J_{\mathrm{old}}$, nên ví dụ $s_B$ chỉ dùng để xem cơ chế, không làm hiện tượng (cổng 2026-11-20) |
| 6 | lời nhắc, sáu so sánh | Hai con đường khác nhau tới cùng một chính sách. | $\tfrac46\to\hat r=(\log2;0)\to(\tfrac45;\tfrac15)$; phần thưởng đã trừ KL $0{,}51$ ở cả hai câu; DPO $0{,}67\to0{,}74\to0{,}77\to0{,}78\to0{,}79\to0{,}8$ | không đưa hai vòng PPO của Ví dụ 10.27 lên trang (vòng 1 dừng ở $0{,}8$ do trùng hợp $\tfrac23\cdot1{,}2$) |

---

### 5. Các trang

#### Mạch 1. Mở đầu (`id="mach-1"`, 8 trang, 12 phút)

Không có trang tiêu đề mạch (NT10, mạch mở đầu). Thứ tự theo TB19, TB20: bìa, một trang chữ (tiên quyết), ví dụ, hiện tượng thứ hai, câu hỏi trung tâm, mục tiêu, nội dung cùng sơ đồ neo. Hai trang chữ trước ví dụ đầu tiên.

##### `L10-1-01` · Bìa

- **Câu:** M. **Biết thêm:** tên bài và việc bài làm, bằng một dòng.
- **1 phút:** Bài này sửa hai điểm yếu của REINFORCE, rồi học chính sách cả khi phần thưởng chỉ đến từ so sánh của người.
- **Mới:** không. **Ý chính:** luận điểm một dòng (NT11, NT-RL-8).
- **Mặt trang:** "Học tăng cường" · "Bài 10" · "TRPO, PPO và DPO" · luận điểm "Sửa hai điểm yếu của REINFORCE, rồi học được cả khi chỉ có so sánh của người." (17 âm tiết; điều phối viên chốt 2026-11-20) · "Trường Đại học Công nghệ, Đại học Quốc gia Hà Nội" · "Năm học 2026–2027, học kỳ 1". Không tên giảng viên.
- **Hình:** không (bìa).
- **Ghi chú diễn giả:** "Bài trước dừng ở REINFORCE: mỗi lượt cho một mẫu không chệch của gradient. Hôm nay ta xem hai điểm yếu của nó trên một ví dụ nhỏ, sửa từng điểm, rồi áp cùng công cụ cho bài toán mà phần thưởng chỉ biết qua so sánh của người, như khi tinh chỉnh mô hình ngôn ngữ."
- **Nguồn:** ghi chú, đoạn mở §1.1.

##### `L10-1-02` · Tiên quyết và quy ước

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

##### `L10-1-03` · Ví dụ: hành lang ngắn (1)

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

##### `L10-1-04` · Ba lượt cho ba hướng cập nhật khác nhau

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

##### `L10-1-05` · Bước đúng hướng mà dài làm $J$ giảm

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

##### `L10-1-06` · Vấn đề trung tâm

- **Câu:** M (trạm dừng của mạch 1). **Biết thêm:** hai câu hỏi của cả bài, mỗi câu gắn với một hình vừa xem.
- **1 phút:** Từ hai hình, bài đặt hai câu hỏi: làm sao để hướng ít dao động, và làm sao đi bước lớn mà $J$ không giảm.
- **Mới:** không. **Ý chính:** hộp "Câu hỏi:".
- **Mặt trang** (≈ 22 âm tiết): hai hình thu nhỏ đặt ngang (trục số của `L10-1-04`, đồ thị của `L10-1-05`), dưới mỗi hình một nhãn "dao động", "bước dài". Hộp "Câu hỏi: 1. Làm sao ước lượng gradient ít dao động hơn? 2. Làm sao đi bước lớn mà $J$ không giảm?"
- **Hình:** hai bản thu nhỏ, mỗi bản khoảng 40% chiều ngang; không hình mới.
- **Dựng dần:** không.
- **Ghi chú diễn giả:** "Câu trả lời theo mạch, chỉ ở lời giảng: mạch 2 và 3 trả lời câu 1 bằng đường cơ sở, critic và GAE; mạch 4 và 5 trả lời câu 2 bằng hàm thay thế, miền tin cậy, TRPO và PPO. Mạch 6 dùng các công cụ đó khi phần thưởng chỉ biết qua so sánh của người, một câu hỏi mà ví dụ hành lang chưa đặt ra."
- **Nguồn:** ghi chú §1.1, đoạn "bài toán trung tâm của chương" (hai phần đầu; phần thứ ba mở mạch 6, quyết định 8).

##### `L10-1-07` · Mục tiêu học tập

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

##### `L10-1-08` · Nội dung

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

#### Mạch 2. So lợi tức với giá trị của trạng thái (`id="mach-2"`, 9 trang thật, 7 trang đếm, 19 phút)

Ví dụ chạy: chuỗi hai trạng thái, chính sách cũ $p_A=\tfrac12$, $p_B=\tfrac23$, $\gamma=0{,}9$. Một khuôn bảng cho cả mạch (NT-RL-5, TB16): hàng là ba loại lượt, cột theo thứ tự tính, cột kết quả thêm dần. `L10-2-01` → `L10-2-03` là chuỗi trang liên tiếp cùng bố cục (tính một trang).

##### `L10-2-00` · Trang tiêu đề mạch 2 (điểm vào mạch 2)

- **Câu:** 2. **Biết thêm:** việc của mạch, bằng một hiện tượng.
- **1 phút:** Mạch này sửa khối hệ số và thêm khối thứ ba trên vòng cập nhật, vì một nửa số lượt đẩy chính sách sai hướng.
- **Mới:** không. **Ý chính:** dòng dẫn.
- **Mặt trang:** `span.strand-number` "2." · `h2` "So lợi tức với giá trị của trạng thái" · `p.strand-lead` "Một nửa số lượt trên chuỗi hai trạng thái đẩy chính sách sai hướng." (15 âm tiết). Không `p.strand-keys` (các thuật ngữ của mạch chưa được dạy, TB11).
- **Hình:** sơ đồ neo thu nhỏ `so-do-neo-m2-vao.svg`: ③ và ④ tô tím, ④ còn nhãn "$G_t$" kèm "?"; khối khác mờ (TB2, NT12 sửa theo TB).
- **Ghi chú diễn giả:** "Mạch trước cho thấy một lượt REINFORCE là một mẫu ồn của gradient. Mạch này giữ nguyên trung bình mà giảm độ ồn: so lợi tức với mức thường có ở trạng thái, rồi để một hàm giá trị đánh giá hành động ngay sau một bước. Kết quả chuyển sang mạch sau là hệ số $\delta_t$ và câu hỏi khi hàm giá trị học dở."
- **Nguồn:** ghi chú §2, đoạn mở.

##### `L10-2-01` · Ví dụ: chuỗi hai trạng thái (1)

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

##### `L10-2-02` · Trừ giá trị của trạng thái: trung bình giữ, dao động giảm

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

##### `L10-2-03` · Câu hỏi nhanh: trừ mức của hành động

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

##### `L10-2-04` · Trừ một mức của trạng thái không đổi trung bình

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

##### `L10-2-05` · Ý tưởng chứng minh: đường cơ sở

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

##### `L10-2-06` · Hệ số trung bình là lợi thế

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

##### `L10-2-07` · Critic đánh giá hành động ngay sau một bước

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

##### `L10-2-08` · Với critic đúng, mọi lượt cho cùng tọa độ $0{,}2$

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

#### Mạch 3. Trộn đánh giá một bước và cả lượt (`id="mach-3"`, 6 trang, 12 phút)

Ví dụ chạy: cùng chuỗi, critic cố định $\hat v=(1{,}4;\,1)$ (đúng ở $s_A$, đánh giá thấp $s_B$; giá trị thật $(1{,}4;\,2)$), hai lượt cùng bắt đầu bằng hành động 1 ở $s_A$. Khuôn bảng: hàng là hai lượt, cột là cách ước lượng.

##### `L10-3-00` · Trang tiêu đề mạch 3 (điểm vào mạch 3)

- **Câu:** 3. **Biết thêm:** việc của mạch: critic học dở làm đánh giá một bước lệch.
- **1 phút:** Mạch này sửa lại khối hệ số, vì critic học dở thì cách đánh giá một bước bị lệch.
- **Mới:** không. **Ý chính:** dòng dẫn.
- **Mặt trang:** "3." · "Trộn đánh giá một bước và cả lượt" · `p.strand-lead` "Critic học dở thì đánh giá một bước bị lệch, còn lợi tức cả lượt thì dao động." (17 âm tiết).
- **Hình:** sơ đồ neo thu nhỏ `so-do-neo-m3-vao.svg`: ④ tô tím, nhãn "$\delta_t$ ?".
- **Ghi chú diễn giả:** "Mạch trước có hai cách lập hệ số: lợi tức cả lượt trừ giá trị, không lệch nhưng ồn; và $\delta_t$ một bước, ít ồn và đúng khi critic đúng. Critic thật luôn sai một chút. Mạch này đặt hai cách cạnh nhau trên cùng một critic sai, rồi trộn chúng bằng một tham số. Đầu ra là $\widehat A_t$ và công thức tính lùi mà PPO dùng."
- **Nguồn:** ghi chú §2.4 đoạn cuối, §3 đoạn mở.

##### `L10-3-01` · Một bước thì lệch, cả lượt thì dao động

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

##### `L10-3-02` · Ước lượng lợi thế tổng quát

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

##### `L10-3-03` · Tính lùi từ cuối lượt

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

##### `L10-3-04` · Câu hỏi nhanh: lượt bị cắt vì hết giờ

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

##### `L10-3-05` · $\lambda$ đổi độ lệch lấy dao động

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

#### Mạch 4. Đánh giá chính sách mới bằng dữ liệu cũ (`id="mach-4"`, 10 trang thật, 9 trang đếm, 22 phút)

Ví dụ chạy: chuỗi, chính sách cũ $\pi=(\tfrac12;\tfrac23)$ với $J=1{,}4$, lợi thế cũ $A_\pi(s_A,\cdot)=(0{,}4;-0{,}4)$, $A_\pi(s_B,\cdot)=(1;-2)$; chính sách mới dọc đường thẳng tới $(1;\,0{,}5)$. `L10-4-02` và `L10-4-03` là chuỗi trang cùng bố cục (tính một trang). Khuôn bảng: hàng là trạng thái, cột theo thứ tự tính.

##### `L10-4-00` · Trang tiêu đề mạch 4 (điểm vào mạch 4)

- **Câu:** 4. **Biết thêm:** việc của mạch: đánh giá một chính sách trước khi chạy nó.
- **1 phút:** Mạch này sửa khối cập nhật: muốn đi bước lớn thì phải đoán được chính sách mới tốt hay xấu từ lượt cũ.
- **Mới:** không. **Ý chính:** dòng dẫn.
- **Mặt trang:** "4." · "Đánh giá chính sách mới bằng dữ liệu cũ" · `p.strand-lead` "Muốn đi bước lớn, phải đánh giá chính sách mới trước khi chạy nó." (14 âm tiết).
- **Hình:** `so-do-neo-m4-vao.svg`: ⑤ tô tím, nhãn "một bước gradient ?".
- **Ghi chú diễn giả:** "Hai mạch trước cho một hệ số ít ồn, nhưng mỗi lô dữ liệu vẫn chỉ cho một bước nhỏ, vì hành lang đã cho thấy bước dài có thể làm $J$ giảm. Mạch này tìm một công thức đoán $J$ của chính sách mới từ dữ liệu cũ, xem nó sai khi nào, và dẫn tới miền tin cậy cùng TRPO."
- **Nguồn:** ghi chú §3.3 đoạn cuối, §4 đoạn mở.

##### `L10-4-01` · Bước lớn đổi cả nơi chính sách tới

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

##### `L10-4-02` · Hiệu $J$ bằng lợi thế cũ cộng theo nơi chính sách mới tới

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

##### `L10-4-03` · Hàm thay thế dùng nơi chính sách cũ tới

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

##### `L10-4-04` · Hàm thay thế tiếp xúc $J$ tại chính sách cũ

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

##### `L10-4-05` · Bước gần thì hàm thay thế sai ít

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

##### `L10-4-06` · Sai số của hàm thay thế bị chặn theo khoảng cách hai chính sách

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

##### `L10-4-07` · Miền tin cậy: tối đa hàm thay thế trong vùng KL nhỏ

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

##### `L10-4-08` · Gradient tự nhiên dồn bước về $\theta_B$

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

##### `L10-4-09` · TRPO: một bước gần đúng, kiểm lại trên dữ liệu

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

#### Mạch 5. Giữ chính sách mới gần chính sách cũ (`id="mach-5"`, 9 trang thật, 8 trang đếm, 16 phút)

Ví dụ chạy (sửa theo cổng 2026-11-20): chuỗi hai trạng thái với critic $(1{,}4;1)$ của mạch 3, $\lambda=1$, và một bộ đệm nhỏ có hai lượt, $s_A\xrightarrow1s_B\xrightarrow2$ và $s_A\xrightarrow2$ (`L10-5-01`, `L10-5-05`); $\epsilon=0{,}2$. Để thấy cơ chế cắt, `L10-5-04` và `L10-5-06` xét riêng trạng thái $s_B$ của cùng chuỗi với bộ đệm ba mẫu đúng tần suất (ghi chú gọi là "bài toán một bước": chính sách cũ $(\tfrac23;\tfrac13)$, hành động $1,1,2$, lợi thế $1,1,-2$). Một đồ thị theo $p$ dùng cho `L10-5-04`, `L10-5-06`. `L10-5-02` và `L10-5-03` là chuỗi trang cùng bố cục (tính một trang).

##### `L10-5-00` · Trang tiêu đề mạch 5 (điểm vào mạch 5)

- **Câu:** 5. **Biết thêm:** việc của mạch: giữ bước gần mà không cần bộ máy bậc hai.
- **1 phút:** Mạch này thay cách TRPO giữ chính sách mới ở gần bằng một cách chỉ cần Adam.
- **Mới:** không. **Ý chính:** dòng dẫn.
- **Mặt trang:** "5." · "Giữ chính sách mới gần chính sách cũ" · `p.strand-lead` "Giữ chính sách mới ở gần chính sách cũ mà chỉ dùng Adam." (13 âm tiết).
- **Hình:** `so-do-neo-m5-vao.svg`: ⑤ tô tím, nhãn "miền tin cậy (TRPO) ?".
- **Ghi chú diễn giả:** "TRPO cho một bước lớn nhưng tốn: gradient liên hợp, tìm kiếm lùi, và không hợp với mạng dùng chung tham số giữa chính sách và critic. Hàm thay thế chỉ đáng tin gần chính sách cũ vì hai lý do: nơi chính sách tới đổi (mạch 4), và lợi thế chỉ là ước lượng từ ít lượt (trang sau). Mạch này đưa giới hạn khoảng cách vào chính hàm mục tiêu, để vài lượt Adam trên dữ liệu tự dừng. Đầu ra là vòng PPO, dùng lại ở mạch sau."
- **Nguồn:** đoạn cuối §5.2; đoạn mở §6.

##### `L10-5-01` · Bộ đệm hai lượt đẩy chính sách đi xa và sai hướng

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

##### `L10-5-02` · Mục tiêu cắt bỏ phần thưởng của việc đi quá xa

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

##### `L10-5-03` · Câu hỏi nhanh: mẫu lợi thế âm với $\rho=1{,}3$

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

##### `L10-5-04` · Trên $s_B$, mục tiêu cắt nằm ngang từ $p=0{,}8$

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

##### `L10-5-05` · Trên bộ đệm hai lượt, phép cắt giữ $J$ gần như không đổi

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

##### `L10-5-06` · Phép cắt không chặn KL

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

##### `L10-5-07` · Một vòng PPO dùng mỗi lô dữ liệu nhiều lần

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

##### `L10-5-08` · TRPO và PPO cùng giữ bước gần, khác cách giữ

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

#### Mạch 6. Học từ so sánh của người (`id="mach-6"`, 10 trang, 22 phút)

Ví dụ chạy: một lời nhắc, hai câu trả lời $y_1$, $y_2$; mô hình hiện tại (chính sách tham chiếu) $\pi_{\mathrm{ref}}=(\tfrac23;\tfrac13)$, cùng xác suất với $s_B$ ở mạch 5 (quyết định 9); sáu so sánh, bốn lần chọn $y_1$; $\beta=1$. Hai con đường (RLHF với PPO, DPO) tới cùng $\pi^*=(\tfrac45;\tfrac15)$.

##### `L10-6-00` · Trang tiêu đề mạch 6 (điểm vào mạch 6)

- **Câu:** 6. **Biết thêm:** việc của mạch: học khi không có hàm phần thưởng.
- **1 phút:** Mạch này thay khối phần thưởng, vì nhiều bài toán không có phần thưởng, chỉ có người chọn câu trả lời tốt hơn.
- **Mới:** không. **Ý chính:** dòng dẫn.
- **Mặt trang:** "6." · "Học từ so sánh của người" · `p.strand-lead` "Không có phần thưởng, chỉ có người chọn câu trả lời tốt hơn." (13 âm tiết).
- **Hình:** `so-do-neo-m6-vao.svg`: ① tô tím, nhãn "phần thưởng ?".
- **Ghi chú diễn giả:** "PPO cần một hàm phần thưởng. Khi tinh chỉnh một mô hình ngôn ngữ, ta chỉ có người đọc hai câu trả lời và chọn câu tốt hơn. Mạch này học một phần thưởng từ các lần chọn, thêm phạt rời mô hình ban đầu, rồi so hai cách tìm chính sách tốt nhất: chạy PPO, hoặc học thẳng bằng một hàm mất mát phân loại."
- **Nguồn:** đoạn cuối §1.1 (phần thứ ba của bài toán trung tâm); §7 đoạn mở.

##### `L10-6-01` · Một lời nhắc, hai câu trả lời, sáu lần chọn

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

##### `L10-6-02` · Khớp phần thưởng để xác suất chọn bằng tỉ lệ $\tfrac46$

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

##### `L10-6-03` · Phạt KL chọn một điểm giữa tham lam và mô hình ban đầu

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

##### `L10-6-04` · Nghiệm có phạt KL: $\pi^*\propto\pi_{\mathrm{ref}}\,e^{\hat r/\beta}$

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

##### `L10-6-05` · RLHF tìm $\pi^*$ bằng PPO trên phần thưởng đã trừ KL

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

##### `L10-6-06` · Đổi biến: phần thưởng viết theo chính sách

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

##### `L10-6-07` · DPO học thẳng chính sách bằng hồi quy logistic

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

##### `L10-6-08` · Hai con đường tới cùng chính sách $(\tfrac45;\,\tfrac15)$

- **Câu:** 6 (trạm dừng cuối của phần chính). **Biết thêm:** RLHF và DPO là hai cách đi tới cùng nghiệm, khác nhau ở số mô hình và dữ liệu; điều kiện quyết định.
- **1 phút:** Từ cùng sáu lần chọn, đường trên đi qua mô hình phần thưởng và PPO, đường dưới đi thẳng bằng DPO; cả hai gặp nhau ở $(\tfrac45;\,\tfrac15)$.
- **Mới:** không (gom ý). **Ý chính:** tiêu đề; câu "Điều kiện quyết định: mỗi cặp câu được chọn theo cả hai chiều ít nhất một lần."
- **Mặt trang** (≈ 25 âm tiết ngoài hình): câu điều kiện quyết định.
- **Hình:** sơ đồ neo `so-do-neo-m6-ra.svg`: từ khung "so sánh của người", đường liền đi qua ① (mô hình phần thưởng, trừ phạt KL) → ② → ③ (critic) → ④ → ⑤ (PPO), ghi "bốn mô hình, sinh câu trong lúc học"; đường nét đứt "DPO" đi thẳng tới ⑤, ghi "hai mô hình, dữ liệu cố định"; hai đường gặp ở khung đậm "$\pi^*=(\tfrac45;\,\tfrac15)$". Khoảng 60%.
- **Dựng dần:** (0) đường trên; (1) đường dưới; (2) khung gặp nhau và câu điều kiện.
- **Ghi chú diễn giả:** "Định lý 10.65 của ghi chú ghép các điều kiện: tập câu trả lời hữu hạn, mô hình tham chiếu dương, chính sách chọn tự do, và mất mát Bradley–Terry có đúng một lớp cực tiểu. Trên ví dụ, điều kiện cuối là có ít nhất một lần chọn mỗi phía. Bảng so sánh đầy đủ hai con đường ở §7.5."
- **Nguồn:** Định lý 10.65 (câu lời thường, câu chuyện mục 5); hình `rlhf-dpo-hai-con-duong.svg` và bảng §7.5 của ghi chú.

##### `L10-6-09` · Câu hỏi nhanh: người luôn chọn một phía

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

#### Mạch 7. Tổng kết (`id="mach-7"`, 8 trang, 9 phút)

Theo TB21: sơ đồ neo lần cuối; trả lời câu hỏi trung tâm bằng ba câu khẳng định; câu hỏi tự kiểm tra về hành vi trên ví dụ; một bài tổng hợp có lời giải và trang bài tập về nhà; tài liệu tham khảo. Không bảng giả thiết (ở §8.1 của ghi chú). Bảng thẳng hàng các quy tắc cập nhật nằm ngay trên khối ④ và ⑤ của sơ đồ neo cuối (TB21 cho bài nhiều thuật toán cùng khung), không thành trang riêng.

##### `L10-7-00` · Trang tiêu đề mạch 7 (điểm vào mạch 7)

- **Câu:** T. **Biết thêm:** mạch gom ý, không ý mới.
- **1 phút:** Mạch cuối đặt lại năm khối của vòng cập nhật, mỗi khối với một công thức và một con số.
- **Mới:** không. **Ý chính:** dòng dẫn.
- **Mặt trang:** "7." · "Tổng kết" · `p.strand-lead` "Mỗi khối của vòng cập nhật nhận một công thức và một con số." (14 âm tiết).
- **Hình:** `so-do-neo-m7-vao.svg`: cả năm khối tô tím nhạt.
- **Ghi chú diễn giả:** "Năm mạch nội dung đổi lần lượt khối hệ số, khối cập nhật và khối phần thưởng của cùng một vòng. Mạch này gom các thay đổi đó, trả lời hai câu hỏi đầu bài và câu hỏi về so sánh, rồi giao bài tổng hợp trên chuỗi hai trạng thái."
- **Nguồn:** §8 của ghi chú.

##### `L10-7-01` · Vòng cập nhật chính sách sau năm mạch

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

##### `L10-7-02` · Vấn đề trung tâm

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

##### `L10-7-03` · Bài tập: một vòng PPO-Clip trên chuỗi hai trạng thái

- **Câu:** T (bài tổng hợp nối mạch 2, 4, 5; quyết định 6). **Biết thêm:** đề bài tổng hợp.
- **1 phút:** Chạy một vòng PPO-Clip trên chính chuỗi của bài: tìm chính sách nơi vòng dừng, rồi so mức tăng mà hàm thay thế đoán với mức tăng thật.
- **Mới:** không. **Ý chính:** hộp "Câu hỏi:".
- **Mặt trang** (≈ 70 âm tiết, trang đề):
  - Hộp "Câu hỏi: Chuỗi hai trạng thái, chính sách cũ $(\tfrac12;\,\tfrac23)$, lợi thế đúng $(0{,}4;\,-0{,}4)$ ở $s_A$ và $(1;\,-2)$ ở $s_B$. Một vòng PPO-Clip với $\epsilon=0{,}2$ tăng mục tiêu cắt tới đầu đoạn phẳng, các mẫu có đúng tần suất của chính sách cũ. (a) Vòng dừng ở chính sách nào? (b) Hàm thay thế đoán $J$ tăng bao nhiêu? $J$ thật tăng bao nhiêu?"
- **Hình:** chuỗi thu nhỏ `chuoi-loi-the.svg` (khoảng 30%), để có lợi thế trên các cung.
- **Dựng dần:** không.
- **Ghi chú diễn giả:** "Bài kiểm ba năng lực: tìm mốc cắt theo dấu lợi thế, tính hàm thay thế bằng bảng của mạch 4, và tính $J$ thật. Gợi ý: tham số của hai trạng thái tách nhau, nên xét từng trạng thái; khi $p$ tăng, tìm lúc từng nhóm mẫu chạm biên. Câu (c), (d) của bài đầy đủ ở Bài tập 10.23 trong ghi chú."
- **Nguồn:** Bài tập 10.23 (câu (a), (b); gợi ý).

##### `L10-7-04` · Bài tập: một vòng PPO-Clip trên chuỗi hai trạng thái, lời giải

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

##### `L10-7-05` · Câu hỏi tự kiểm tra

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

##### `L10-7-06` · Bài tập về nhà

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

##### `L10-7-07` · Tài liệu tham khảo

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

### 6. Danh sách hình mới cho người vẽ

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

### 7. Đối chiếu mã trang cũ → mới

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

#### Liên kết sâu cần sửa (không thuộc phạm vi tệp này; ghi để điều phối viên giao)

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

### 8. Chỗ lệch so với câu chuyện đã duyệt và lý do

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

### 9. Kiểm theo quy tắc trên storyboard (tự kiểm của người viết, chưa thay vai duyệt)

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


### 10. Câu hỏi cho điều phối viên (sau cổng)

Câu hỏi 1–3 của bản trước đã được trả lời (tên mạch lời thường, mạch 5 đổi tên; câu bìa; năm mục tiêu và ba dòng ở `L10-6-06` được chấp nhận). Còn lại:

1. **Sửa `exercises.md`** (bảng bảy mạch ở mục 7, tên mạch 5 mới): giao cho ai, trong commit nào?
2. **Bộ sơ đồ neo 14 trạng thái:** script sinh SVG trong `tools/courses/rl-plan/` hay vẽ tay?
3. **Đề xuất sửa ghi chú G1–G4 (mục 11)** phải xong, rà toán và commit trước khi viết HTML (quyết định 6 của tác giả: ghi chú sửa trước, cùng số với deck).
4. **Tệp quy tắc:** câu "lưu ý cho người dựng" trong TB15 của `quy-tac-trinh-bay.md` vẫn sai (câu chuyện mục 4.1).

---

### 11. Đề xuất sửa ghi chú (để điều phối viên giao trước khi viết deck)

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

### 12. Phác bố cục bổ sung (cổng: các trang có hình, bảng tính hay dựng dần còn thiếu phác)

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

### 13. Sửa theo cổng (2026-11-20)

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

### 14. Sửa theo năm vai rà (2026-11-20, biên tập viên)

Căn cứ: năm báo cáo rà trên bản đóng băng (sinh viên, chuyên gia, toán, sư phạm, mạch truyện) và chín quyết định của điều phối viên. Nhật ký đầy đủ (mỗi phát hiện, quyết định, lý do, trang đổi) ở thư mục rà của phiên. Ghi chú bài giảng và bài tập không đổi.

#### 14.1 Mã trang hiện hành (62 trang, 7 mạch)

| Mạch | Mã trang theo thứ tự trình chiếu | Số trang |
|---|---|---|
| 1 | `L10-1-01` … `L10-1-08` | 8 |
| 2 | `L10-2-00` … `L10-2-08` | 9 |
| 3 | `L10-3-00`, `3-01`, `3-02`, `3-05`, `3-04` | 5 |
| 4 | `L10-4-00`, `4-01`, `4-02`, `4-03`, **`4-11`**, `4-04`, `4-05`, `4-10`, `4-06`, **`4-12`**, `4-07`, `4-08`, `4-09` | 13 |
| 5 | `L10-5-00` … `L10-5-08` | 9 |
| 6 | `L10-6-00` … `L10-6-09` | 10 |
| 7 | `L10-7-00` … `L10-7-07` | 8 |

#### 14.2 Mã bỏ, thêm, đổi chỗ (cộng dồn từ sau cổng storyboard)

| Mã | Thay đổi | Đợt | Lý do |
|---|---|---|---|
| `L10-3-03` | bỏ | sửa theo người thầy | gộp vào `3-02` (dựng dần tính lùi) |
| `L10-4-10` | thêm sau `4-05` | sửa theo người thầy | tách câu hỏi nhanh bước gần khỏi trạm dừng `4-05` |
| `L10-4-11` | thêm sau `4-03` | năm vai rà | dạy tỉ số chính sách $\rho$ và $\pi_{\mathrm{old}}$ trước khi mạch 5 dùng (quyết định 6; SV, SP, MT) |
| `L10-4-12` | thêm sau `4-06` | năm vai rà | định nghĩa KL bằng công thức và lý do KL vô hạn trước miền tin cậy (quyết định 5) |
| `L10-3-05` ↔ `L10-3-04` | đổi chỗ | năm vai rà | câu hỏi nhanh kiểm lại trạm dừng trên $\lambda$ mới; "Còn thiếu" sang `3-04`; `3-05` thêm sơ đồ neo `m3-ra` (MT) |

Không dùng lại mã đã bỏ. Mạch 4 dài 13 trang: trạm dừng `4-05` (trang 6 của mạch) và `4-09` (cuối mạch).

#### 14.3 Trang đổi nội dung mặt trang

`1-01` (luận đề một ý, 20 âm tiết), `1-03`, `1-04`, `1-07`, `2-01`, `2-02`, `2-07`, `3-01`, `3-02`, `3-04`, `3-05`, `4-01`, `4-02`, `4-03`, `4-04`, `4-05`, `4-06`, `4-07`, `4-08`, `4-09`, `4-10`, `5-00`, `5-01`, `5-02`, `5-03`, `5-04`, `5-05`, `5-06`, `5-07`, `5-08`, `6-01`, `6-03`, `6-04`, `6-05`, `6-06`, `6-07`, `6-08`, `6-09`, `7-00`, `7-01` (hình, alt), `7-02`, `7-05`, `7-07`; trang mới `4-11`, `4-12`. Hình đổi (không đổi mã trang): `1-08` (`m1`), `5-00`, `6-00`, `7-00` (thu nhỏ), `6-05` (`m6-rlhf`). Chỉ đổi ghi chú diễn giả: `1-02`, `1-08`, `2-00`, `2-03`, `2-04`, `3-00`, `4-00`.

#### 14.4 Mạch 4 sau sửa (câu "sau trang này sinh viên biết thêm")

- `4-11`: hàm thay thế tính được từ hành động của chính sách cũ nhờ tỉ số $\rho=\pi'/\pi_{\mathrm{old}}$ (bảng $s_B$ cho lại $-0{,}5$).
- `4-06`: cận cải thiện bằng lời; khoảng cách biến phân viết ra; thừa số $1/(1-\gamma)^2=100$ làm phạt vượt mức đoán trừ khi bước rất ngắn.
- `4-12`: KL bằng công thức, tính được từ lượt cũ, chặn khoảng cách của định lý; bước $(1;0{,}5)$ có KL vô hạn tại $s_A$ vì bỏ hẳn hành động 2.
- `4-07`: miền tin cậy là bài toán $\max\mathcal L$ với $\overline D_{\mathrm{KL}}\le\kappa$.
- `4-08`: $F_s$ = tần suất tới × $p(1-p)$ có số trên mặt trang; gradient tự nhiên $(8;30)$ dồn về $\theta_B$.
- `4-09`: TRPO ghép ba thứ trên; khung "tính gần đúng gradient tự nhiên", "thu ngắn bước tới khi KL ≤ κ và hàm thay thế tăng" thay "tích $Fv$", "tìm kiếm lùi"; "Còn thiếu" nói chi phí, dẫn vào `5-01` ("Bỏ ràng buộc KL, chỉ chạy Adam").

#### 14.5 Ngoại lệ mật độ (âm tiết theo `deck_lint`, sau sửa)

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

#### 14.6 Đề xuất sửa ghi chú (NT3, chưa làm)

1. §8.4 câu 3 dùng $\beta=2$, đọc thẳng được từ hình nghiệm có phạt KL; deck hỏi $\beta=4$ (đáp số $(0{,}70;\,0{,}30)$). Đề xuất đổi câu §8.4 theo, hoặc tác giả chọn giữ $\beta=2$ và deck quay lại.
2. Ví dụ 10.23 (tùy chọn): tỉ lệ người chọn $\tfrac46$ trùng xác suất $\tfrac23$ của mô hình; deck bỏ câu phủ định, giữ số. Nếu muốn tránh trùng hẳn, đổi số lần chọn trong ghi chú trước (SP).
3. Bảng thuật ngữ `outline.md`: thêm "lô nhỏ (mini-batch)", "lần qua bộ đệm (epoch)", "chính sách tham chiếu" cho $\pi_{\mathrm{ref}}$ theo cách deck dùng (CG).

#### 14.7 Vòng sửa chân trang (2026-11-20)

`footer_check` về 0 bằng bố cục: `1-03`, `2-01`, `3-01` (ảnh 345 px, nhãn hình lớn hơn), `3-05` (bảng gọn một hàng), `4-10` ("Còn thiếu" xuống ghi chú diễn giả), `5-01` (bảng thêm cột $\rho\widehat A$, dòng hàm thay thế mẫu còn một dòng; âm tiết dưới trần), `5-02`, `6-07`. Không đổi số, ý hay mã trang; vẫn 62 trang.

#### 14.8 Lượt sửa cuối sau rà lại (2026-11-20)

- `L10-7-02`: bốn câu trả lời: đường cơ sở (giữ $0{,}69\to0{,}20$ và "mức khác có thể làm nó tăng"), critic một bước và GAE trộn bằng $\lambda$ (lệch khi critic sai và $\lambda<1$), hàm thay thế và TRPO/PPO, RLHF ≡ DPO với Bradley–Terry, $\pi_{\mathrm{ref}}$ cố định, dương trên mọi câu, chính sách chọn tự do.
- Nhẹ: `4-11` thêm "(probability ratio)"; `4-06`, `5-04`, `2-01` công thức nội dòng không ngắt; `4-08` viết $1-\gamma=0{,}1$ trên mặt trang, trục elip $\Delta\theta_A$, $\Delta\theta_B$; `4-10` "Còn thiếu" trở lại mặt trang (cột trái); `5-03` "$p_B$"; nhãn "dùng lại / lượt / vừa thu" ba dòng, không đè đường nối (m4-ra, m5-ra, m5/m6/m7-vao, m6-rlhf, m6-ra).
- `exercises.md`: bảng "Mạch | Mở phần | Bài tập" theo 7 mạch, liên kết `#/1/1` … `#/7/1`, bài tập khớp `L10-7-06`.

#### 14.9 Thời lượng (62 trang, 120 phút)

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


# Lịch sử: mạch 4 trước đề xuất TRPO (2026-11-21)

Phần dưới là §3 mạch 4 của storyboard trước kế hoạch theo đề xuất trình bày TRPO (27 trang, 37,5 phút, khớp deck bản sau góp ý #1–#4; trang `4-26` không có mục riêng ở bản này), giữ nguyên chữ, mọi tiêu đề hạ một bậc. Hết hiệu lực khi deck dựng theo §3 mạch 4 mới; chỉ để đối chiếu nhật ký rà.

#### Mạch 4. Hàm thay thế và miền tin cậy (`id="mach-4"`, 27 trang, 37,5 phút)

Thứ tự hiện hành (B5): `4-00` → `4-01` → `4-13` → `4-02` → `4-14` → `4-15` → `4-03` → `4-11` → `4-16` → `4-05` → `4-23` → `4-17` → `4-04` → `4-10` → `4-24` → `4-06` → `4-18` → `4-19` → `4-12` → `4-20` → `4-21` → `4-07` → `4-22` → `4-08` → `4-25` → `4-09` → `4-26`; `4-09`/`4-26` là thuật toán TRPO tách hai trang (góp ý tác giả #1); `4-15` và `4-16` không còn liền nhau, tính hai trang. Thứ tự sau cổng storyboard (cũ): `4-00` → `4-01` → `4-13` → `4-02` → `4-14` → `4-03` → `4-15` → `4-16` → `4-11` → `4-05` → `4-23` → `4-17` → `4-04` → `4-10` → `4-24` → `4-06` → `4-18` → `4-19` → `4-12` → `4-20` → `4-21` → `4-07` → `4-22` → `4-08` → `4-25` → `4-09`. Mã mới thêm ở cổng: `4-23` (sai số (2)), `4-24` ($D_{\mathrm{TV}}$, $\nu^\pi$), `4-25` (ví dụ một bước TRPO). `4-03` đặt trước `4-15` để chuỗi dựng dần `4-15`–`4-16` liền nhau. Không bỏ mã nào; mã mới `4-13` … `4-22`. Thứ tự theo #20–#25: bài toán → $A_\pi(s,\pi')$ → bổ đề → ý tưởng chứng minh → bảng kiểm → hàm thay thế → bảng đủ cột → tỉ số → sai số → tiếp xúc → đoạn thẳng → câu hỏi nhanh → định lý TV → ý tưởng → số → KL → Pinsker → hệ quả KL → miền tin cậy → Fisher → gradient tự nhiên → TRPO. `4-15` và `4-16` là một chuỗi dựng dần cùng bố cục (bảng thêm cột), tính một trang theo TB17. Trạm dừng: `4-16` (trang 7), `4-19` (trang 15), `4-09` (cuối).

Bảng số dùng chung của mạch (kiểm trong `kiem_so.py`):

| Đại lượng | $s_A$ | $s_B$ | Nguồn |
|---|---|---|---|
| $\pi$: $p_s$ | $\tfrac12$ | $\tfrac23$ | `1-09` |
| $\tilde\pi$: $\tilde p_s=\sigma(\tilde\theta_s)$ | $\sigma(\log9)=0{,}9$ | $\sigma(0)=0{,}5$ | `4-01` |
| $A_\pi(s,\tilde\pi)$ | $0{,}9\cdot1{,}8+0{,}1\cdot1-1{,}4=0{,}32$ | $0{,}5\cdot3+0{,}5\cdot0-2=-0{,}5$ | `4-13` |
| $\eta_{\tilde\pi}(s)$ | $1$ | $\gamma\tilde p_A=0{,}81$ | `4-15` |
| $\eta_\pi(s)$ | $1$ | $\gamma p_A=0{,}45$ | `4-16` |
| $D_{\mathrm{TV}}(s)$ | $0{,}4$ | $\tfrac16$ | `4-24` |
| $D_{\mathrm{KL}}(s)$, chiều $\pi\Vert\tilde\pi$ | $\tfrac12\log\tfrac{0{,}5}{0{,}9}+\tfrac12\log\tfrac{0{,}5}{0{,}1}=\log\tfrac53=0{,}511$ | $\tfrac23\log\tfrac43+\tfrac13\log\tfrac23=0{,}0566$ | `4-12` |
| $\nu^\pi(s)=(1-\gamma)\eta_\pi(s)$ | $0{,}1$ | $0{,}045$ | `4-24` |

$J(\tilde\pi)=2{,}7\cdot0{,}45+0{,}1=1{,}315$; $\Delta J=-0{,}085$; $\Delta\mathcal L=0{,}095$; sai số $-0{,}18$.

##### `L10-4-00` · Hàm thay thế và miền tin cậy (trang tiêu đề mạch; điểm vào mạch 4; giữ mã)

- **Mặt trang:** "4."; `h2` "Hàm thay thế và miền tin cậy"; `p.strand-lead` "Chính sách mới được đánh giá từ dữ liệu của chính sách cũ với sai số nhỏ khi hai chính sách gần nhau."
- **Hình:** `so-do-neo-m4-vao.svg`.
- **Diễn giả:** "Mạch 2–3 cho hệ số ít phương sai, nhưng mọi ước lượng cần lượt của chính sách đang cập nhật, nên mỗi lượt chỉ cho một bước nhỏ. Mạch này đánh giá một chính sách mới bằng lượt của chính sách cũ, chặn sai số của phép đánh giá theo khoảng cách giữa hai chính sách, và dẫn tới TRPO. Đầu ra là bài toán miền tin cậy và chi phí bậc hai của TRPO." **Phút:** 0,5.

##### `L10-4-01` · Đánh giá chính sách mới từ lượt của chính sách cũ (giữ mã; #20)

- **Câu:** 1 (mạch 4). **Nhãn:** "Câu hỏi:" (hộp đầu); hộp kết luận.
- **Mặt trang:**
  - "Mỗi lượt của mạch trước chỉ cho một bước nhỏ. Bước dài cần đánh giá chính sách mới trước khi chạy nó." (nửa câu nối từ `3-10`)
  - Hộp: "Câu hỏi: cho các lượt sinh bởi $\pi$, ước lượng $J$ của một chính sách mới trước khi chạy nó thế nào?" (bài toán của mạch, TB30)
  - "Xét chính sách ứng viên (giả định) $\tilde\theta=(\log9;\,0)$, như do một bước cập nhật dài đề xuất. Nó tăng $p_A$ và giảm $p_B$, và đủ xa $\pi$ để sai số của phép đánh giá hiện rõ."

    | | $\pi$ | $\tilde\pi$ |
    |---|---|---|
    | $\theta$ | $(0;\,\log2)$ | $(\log9;\,0)$ |
    | $p_A=\sigma(\theta_A)$ | $0{,}5$ | $0{,}9$ |
    | $p_B=\sigma(\theta_B)$ | $\tfrac23$ | $0{,}5$ |
    | xác suất tới $s_B$, bằng $p_A$ | $0{,}5$ | $0{,}9$ |
    | $J=2{,}7p_Ap_B+1-p_A$ | $1{,}4$ | $2{,}7\cdot0{,}45+0{,}1=1{,}315$ |
  - Hộp: "$\tilde\pi$ tới $s_B$ với xác suất lớn hơn và tại $s_B$ chọn hành động 1 với xác suất nhỏ hơn. Lượt của $\pi$ phân bố theo $\pi$: chỉ một nửa số lượt tới $s_B$."
- **Dựng dần:** (0) câu hỏi, dòng ứng viên, ba hàng đầu; (1) hàng xác suất tới $s_B$ và hình; (2) hàng $J$; (3) hộp.
- **1 phút:** Chính sách mới thăm $s_B$ với xác suất $0{,}9$ thay cho $0{,}5$; dữ liệu cũ không cho thấy điều đó, và $J$ thật giảm từ $1{,}4$ xuống $1{,}315$.
- **Mới:** chính sách ứng viên $\tilde\pi$ (một đối tượng, có nguồn gốc và tham số, #20, TB25).
- **Nguồn số:** $\sigma(\log9)=9/10$, $\sigma(0)=\tfrac12$; $J$ theo công thức của `1-10`.
- **Hình:** sửa `chuoi-ti-le-toi-sB-buoc0.svg`, `chuoi-ti-le-toi-sB.svg`: thanh "chính sách cũ $\pi$: $0{,}5$" (xám, dài một nửa) và "chính sách ứng viên $\tilde\pi$: $0{,}9$" (tím, dài $0{,}9$) dưới tiêu đề "xác suất tới $s_B$"; nhãn dưới thanh tím "tại $s_B$: $\tilde p_B=0{,}5<\tfrac23$" (thay "ở $s_B$ chọn kém hơn"). Nửa phải.
- **Ghi chú nguồn:** đoạn mở §4; Ví dụ 10.11, đoạn "Hai bước trên một đường thẳng" ($\tilde\pi$); hình `policy-update-feedback.svg` của ghi chú (không dùng trên trang).
- **Diễn giả:** ứng viên này đến từ một bước dài, như bước theo ước lượng một lượt ở mạch 1; ở đây không quan trọng nó đến từ ước lượng nào, chỉ cần đánh giá nó trước khi chạy. $\tilde\theta$ hữu hạn nên $\tilde\pi$ dương trên mọi hành động. Ghi chú dùng thêm một bước ngắn $\pi'=(0{,}6;\,0{,}8)$ với $\Delta J=0{,}296$.
- **Phút:** 1,5.

##### `L10-4-13` · Lợi thế của $\pi'$ so với $\pi$ tại một trạng thái (mã mới; #21)

- **Câu:** 2 (mạch 4). **Nhãn:** "Câu hỏi:", "Định nghĩa.", "Dạng khác:".
- **Mặt trang:**
  - "Nhắc lại: $q_\pi(s_A,\cdot)=(1{,}8;\,1)$, $q_\pi(s_B,\cdot)=(3;\,0)$, $v_\pi=(1{,}4;\,2)$; $\tilde\pi=(0{,}9;\,0{,}5)$." (Đ1)
  - "Câu hỏi: tại $s$, chọn một hành động theo $\pi'$ rồi từ bước sau theo $\pi$. So với theo $\pi$ ngay từ $s$, lợi tức kỳ vọng thay đổi bao nhiêu?"
  - "**Định nghĩa.** Lợi thế của $\pi'$ so với $\pi$ tại $s$ là" $$A_\pi(s,\pi')=\sum_a\pi'(a\mid s)\,q_\pi(s,a)-v_\pi(s).$$
  - "Dạng khác: $A_\pi(s,\pi')=\sum_a\pi'(a\mid s)\,A_\pi(s,a)$."
  - "Với $\pi'=\tilde\pi$: $A_\pi(s_A,\tilde\pi)=0{,}9\cdot1{,}8+0{,}1\cdot1-1{,}4=0{,}32$; $A_\pi(s_B,\tilde\pi)=0{,}5\cdot3+0{,}5\cdot0-2=-0{,}5$."
- **Dựng dần:** (0) câu hỏi; (1) định nghĩa, dạng khác; (2) dòng số.
- **1 phút:** Đổi một bước sang $\tilde\pi$ có lợi tại $s_A$ ($+0{,}32$) và có hại tại $s_B$ ($-0{,}5$).
- **Mới:** $A_\pi(s,\pi')$.
- **Nguồn số:** $q_\pi$, $v_\pi$ từ `1-10`, `1-11`, `2-06`; $\tilde p_s$ từ `4-01`.
- **Hình:** không (hoặc `chuoi-loi-the.svg` thu nhỏ, đã có $q_\pi$, $v_\pi$).
- **Ghi chú nguồn:** đoạn mở §4.1 (câu dạng $\sum_a\pi'(a\mid s)q_\pi(s,a)-v_\pi(s)$ được thêm theo quyết định N8; ghi chú không có khối định nghĩa riêng, trang chiếu vẫn ghi nhãn "Định nghĩa."); Ví dụ 10.11, đoạn "Hai bước trên một đường thẳng".
- **Diễn giả:** $A_\pi(s,\pi)=0$ với mọi $s$ (kỳ vọng của lợi thế theo chính sách của nó). Nếu $A_\pi(s,\pi')\ge0$ với mọi $s$ thì $\pi'$ không kém $\pi$ ở mọi trạng thái (Hệ quả 10.20), dạng ngẫu nhiên của định lý cải thiện chính sách (Bài 04).
- **Phút:** 1,5.

##### `L10-4-02` · Bổ đề chênh lệch hiệu năng (giữ mã; #21, TB28)

- **Câu:** 2. **Nhãn:** "Bổ đề.", "Giả thiết:", "Ký hiệu:", "Kết luận:", "Ý nghĩa:".
- **Mặt trang:**
  - "**Bổ đề** (chênh lệch hiệu năng). Giả thiết: giả thiết chung cho hai chính sách $\pi$, $\pi'$ (cùng $P$, cùng $\mu_0$)."
  - "Ký hiệu: số lần thăm kỳ vọng có chiết khấu của $s$ dưới $\pi'$ là $\eta_{\pi'}(s)=\sum_{t\ge0}\gamma^t\Pr_{\pi'}(S_t=s,\,t<T)$."
  - "Kết luận:" $$J(\pi')-J(\pi)=\sum_s\eta_{\pi'}(s)\,A_\pi(s,\pi').$$
  - "Ý nghĩa: mức thay đổi của $J$ là lợi thế một bước của $\pi'$ tại mỗi trạng thái, cộng theo số lần $\pi'$ thăm trạng thái đó."
- **Dựng dần:** (0) giả thiết, ký hiệu; (1) kết luận; (2) ý nghĩa.
- **1 phút:** Hiệu $J$ là tổng của lợi thế một bước, trọng số là số lần thăm của chính sách mới.
- **Mới:** $\eta_{\pi'}$; bổ đề (hai đối tượng).
- **Nguồn số:** không.
- **Hình:** không.
- **Ghi chú nguồn:** Bổ đề 10.19 (dạng $\eta$, theo câu nối $\eta=\nu/(1-\gamma)$ của ghi chú, N5); Định nghĩa 10.18.
- **Diễn giả:** $\eta$ không phải số lần thăm: mỗi lần thăm ở bước $t$ có trọng số $\gamma^t$. Vế phải cần quỹ đạo của $\pi'$, nên chưa tính được từ lượt của $\pi$. Bỏ "cùng $\mu_0$" hay "cùng $P$" thì bổ đề sai (ghi chú, hai phản ví dụ).
- **Phút:** 1,5.

##### `L10-4-14` · Ý tưởng chứng minh: bổ đề chênh lệch hiệu năng (mã mới; #21)

- **Câu:** 2. **Nhãn:** "Ý tưởng chứng minh." (tiêu đề).
- **Mặt trang** (năm bước của chứng minh Bổ đề 10.19, Đ8):
  - "Bước 1 (một bước): $A_\pi(s,a)=r(s,a)+\gamma\sum_{s'}P(s'\mid s,a)v_\pi(s')-v_\pi(s)$, không chứa $\pi'$."
  - "Bước 2 (tính chất tháp trên quỹ đạo của $\pi'$):" $$\mathbb E_{\pi'}\bigl[A_\pi(S_t,A_t)\bigr]=\mathbb E_{\pi'}\bigl[R_{t+1}+\gamma v_\pi(S_{t+1})-v_\pi(S_t)\bigr].$$
  - "Bước 3 (tổng lồng nhau tới $K$): cộng theo $t<K$ với trọng số $\gamma^t$, các số hạng $v_\pi$ triệt tiêu, còn $\sum_{t<K}\gamma^tR_{t+1}+\gamma^Kv_\pi(S_K)-v_\pi(S_0)$."
  - "Bước 4 (qua giới hạn): $K\to\infty$, cùng $\mu_0$ cho $J(\pi')-J(\pi)$. Bước 5 (dạng chiếm dụng): gom theo trạng thái được $\sum_s\eta_{\pi'}(s)A_\pi(s,\pi')$. $\square$"
  - Hộp "Câu hỏi: vì sao ở Bước 2 kỳ vọng dưới $\pi'$ của $R_{t+1}+\gamma v_\pi(S_{t+1})$ bằng $q_\pi(S_t,A_t)$, dù lượt chạy theo $\pi'$?" → mảnh sau: "Khi biết $(S_t,A_t)$, bước chuyển chỉ phụ thuộc động lực $P$, chung cho hai chính sách. Chính sách chỉ quyết định $A_t$." (Đ9)
- **Dựng dần:** từng bước một mảnh; câu hỏi; lời giải câu hỏi.
- **1 phút:** Lợi thế của $\pi$ cộng dọc lượt của $\pi'$ là tổng lồng nhau, còn lại đúng hiệu $J$.
- **Mới:** không. **Nguồn số:** không.
- **Hình:** không. **Ghi chú nguồn:** Bổ đề 10.19, chứng minh Bước 1–5.
- **Diễn giả:** Bước 2 dùng cùng động lực và tính Markov; Bước 4 dùng cùng $\mu_0$, phần thưởng bị chặn và $\gamma<1$ (hội tụ trội); Bước 5 dùng định nghĩa của $\eta_{\pi'}$.
- **Phút:** 2.

##### `L10-4-03` · Hàm thay thế (giữ mã; #25)

- **Câu:** 3 (mạch 4). **Nhãn:** "Định nghĩa.", "Ý nghĩa:".
- **Mặt trang:**
  - "Vế phải của bổ đề chênh lệch hiệu năng cần $\eta_{\pi'}$, tức cần chạy $\pi'$. Thay $\eta_{\pi'}$ bằng $\eta_\pi$."
  - "**Định nghĩa.** Hàm thay thế (surrogate objective) của $\pi'$ quanh $\pi$ là" $$\mathcal L_\pi(\pi')=J(\pi)+\sum_s\eta_\pi(s)\,A_\pi(s,\pi').$$
  - "Ký hiệu: $\Delta J=J(\pi')-J(\pi)$, $\Delta\mathcal L=\mathcal L_\pi(\pi')-J(\pi)$."
  - "Ý nghĩa: mọi đại lượng ở vế phải là của $\pi$, nên $\mathcal L_\pi(\pi')$ tính được từ lượt của $\pi$."
- **Dựng dần:** (0) lý do; (1) định nghĩa, ký hiệu; (2) ý nghĩa.
- **1 phút:** Hàm thay thế là bổ đề chênh lệch hiệu năng với số lần thăm của chính sách cũ.
- **Mới:** hàm thay thế; ký hiệu $\Delta J$, $\Delta\mathcal L$ (#22).
- **Nguồn số:** không.
- **Hình:** không.
- **Ghi chú nguồn:** đoạn mở §4.2; Định nghĩa 10.21 (dạng thứ hai, viết theo $\eta$); câu "khi viết theo chính sách, ta cũng ký hiệu $\mathcal L_\pi(\pi')$".
- **Diễn giả:** ghi chú viết $\mathcal L_{\theta_{\mathrm{old}}}(\theta)$ khi tham số hóa và $\mathcal L_\pi(\pi')$ khi viết theo chính sách; deck chỉ dùng dạng sau. "Tính được từ lượt của $\pi$" cần một bước nữa: $A_\pi(s,\pi')$ là kỳ vọng theo hành động của $\pi'$, đổi sang hành động của $\pi$ bằng tỉ số (trang `4-11`).
- **Phút:** 1,5.

##### `L10-4-15` · Ví dụ: bổ đề chênh lệch hiệu năng trên chuỗi (mã mới; #21; đầu chuỗi dựng dần với `4-16`)

- **Câu:** 2. **Nhãn:** hộp.
- **Mặt trang:**
  - "Với $\tilde\pi$: $\eta_{\tilde\pi}(s_A)=1$ (chỉ thăm ở $t=0$); $\eta_{\tilde\pi}(s_B)=\gamma\cdot\Pr_{\tilde\pi}(\text{tới }s_B)=\gamma\tilde p_A=0{,}9\cdot0{,}9=0{,}81$."

    | $s$ | $A_\pi(s,\tilde\pi)$ | $\eta_{\tilde\pi}(s)$ | $\eta_{\tilde\pi}A_\pi$ |
    |---|---|---|---|
    | $s_A$ | $0{,}32$ | $1$ | $0{,}32$ |
    | $s_B$ | $-0{,}5$ | $0{,}81$ | $-0{,}405$ |
    | tổng | | | $\Delta J=-0{,}085$ |
  - Hộp: "Tổng của bảng trùng $J(\tilde\pi)-J(\pi)=1{,}315-1{,}4=-0{,}085$."
  - "Ở đây $\pi'=\tilde\pi$, $\eta_{\pi'}=(1;\,0{,}81)$, $A_\pi(\cdot,\pi')=(0{,}32;\,-0{,}5)$." (Đ6)
  - "Bỏ giả thiết cùng $\mu_0$: với $\pi'=(0{,}6;\,0{,}8)$ xuất phát từ $s_B$ và $\pi$ từ $s_A$, vế trái là $v_{\pi'}(s_B)-v_\pi(s_A)=0{,}8\cdot3-1{,}4=1$, còn vế phải là $A_\pi(s_B,\pi')=0{,}8\cdot1+0{,}2\cdot(-2)=0{,}4$." (Đ2; số của ghi chú)
- **Dựng dần:** (0) dòng $\eta$; (1) bảng; (2) hộp, dòng tương ứng; (3) dòng bỏ giả thiết.
- **1 phút:** Bổ đề cho đúng $-0{,}085$: lợi ích tại $s_A$ nhỏ hơn thiệt hại tại $s_B$, nhân với $0{,}81$ lần thăm.
- **Mới:** không (áp dụng). **Nguồn số:** $A$ từ `4-13`; $\tilde p_A$ từ `4-01`; $J$ từ `4-01`; dòng bỏ giả thiết dùng phản ví dụ của ghi chú (đoạn sau Bổ đề 10.19, "Bỏ cùng $\mu_0$"), với $v_{\pi'}(s_B)$ và $A_\pi(s_B,\pi')$ tính trên trang.
- **Hình:** không. **Ghi chú nguồn:** Ví dụ 10.11 ($\tilde\pi$); Bổ đề 10.19.
- **Diễn giả:** đây là bảng của trang sau, mới có ba cột đầu. Chính sách $(0{,}6;\,0{,}8)$ ở dòng cuối là bước ngắn của ghi chú, chỉ dùng cho phản ví dụ này.
- **Phút:** 1.

##### `L10-4-16` · Hàm thay thế dự báo $J$ tăng $0{,}095$ khi $J$ giảm $0{,}085$ (mã mới; #25; trạm dừng; dòng cuối nêu điều còn thiếu, E3)

- **Câu:** 3. **Nhãn:** hộp.
- **Mặt trang:**
  - "$\eta_\pi(s_A)=1$; $\eta_\pi(s_B)=\gamma p_A=0{,}9\cdot0{,}5=0{,}45$."

    | $s$ | $A_\pi(s,\tilde\pi)$ | $\eta_{\tilde\pi}(s)$ | $\eta_\pi(s)$ | $\eta_{\tilde\pi}A_\pi$ | $\eta_\pi A_\pi$ | $(\eta_{\tilde\pi}-\eta_\pi)A_\pi$ |
    |---|---|---|---|---|---|---|
    | $s_A$ | $0{,}32$ | $1$ | $1$ | $0{,}32$ | $0{,}32$ | $0$ |
    | $s_B$ | $-0{,}5$ | $\gamma\tilde p_A=0{,}81$ | $\gamma p_A=0{,}45$ | $-0{,}405$ | $-0{,}225$ | $-0{,}18$ |
    | tổng | | | | $\Delta J=-0{,}085$ | $\Delta\mathcal L=+0{,}095$ | $-0{,}18$ |
  - Hộp: "Hàm thay thế dự báo $J$ tăng $0{,}095$, trong khi $J$ giảm $0{,}085$. Toàn bộ sai số nằm ở $s_B$, nơi $\tilde\pi$ thăm nhiều hơn và kém hơn $\pi$."
- **Dựng dần:** (0) bảng của `4-15` (ba cột đầu và cột $\eta_{\tilde\pi}A_\pi$ giữ nguyên vị trí); (1) cột $\eta_\pi$ và $\eta_\pi A_\pi$; (2) cột cuối; (3) hộp.
- **1 phút:** Dùng số lần thăm cũ, hàm thay thế cho sai dấu: dự báo tăng, thực tế giảm.
- **Mới:** cột $\eta_\pi$ (một đối tượng).
- **Nguồn số:** cột trái từ `4-15`; $p_A$ từ `1-09`; phép tính trong ô (tên cột đúng đại lượng, #25).
- **Hình:** không (bảng).
- **Ghi chú nguồn:** Ví dụ 10.11 ($\tilde\pi$); Định nghĩa 10.21; Bổ đề 10.19.
- **Diễn giả:** đây là kết quả chính của nửa đầu mạch: hàm thay thế tính được từ dữ liệu cũ, nhưng với bước dài nó có thể sai cả dấu. Hỏi lớp: muốn tin hàm thay thế thì cần điều kiện gì giữa hai chính sách.
- **Phút:** 1,5.

##### `L10-4-11` · Tỉ số chính sách (giữ mã; #25)

- **Câu:** 3. **Nhãn:** "Định nghĩa.", "Dạng khác:".
- **Mặt trang:**
  - "Lượt cũ chỉ chứa hành động do $\pi$ chọn."
  - "**Định nghĩa.** Với $\pi(a\mid s)>0$, tỉ số chính sách (probability ratio) là $\rho(s,a)=\pi'(a\mid s)/\pi(a\mid s)$."
  - "Dạng khác:" $$A_\pi(s,\pi')=\sum_a\pi(a\mid s)\,\rho(s,a)\,A_\pi(s,a)=\mathbb E_{a\sim\pi(\cdot\mid s)}\bigl[\rho(s,a)A_\pi(s,a)\bigr].$$

    | $(s,a)$ | $\pi(a\mid s)$ | $\tilde\pi(a\mid s)$ | $\rho$ | $A_\pi(s,a)$ | $\pi\,\rho\,A_\pi$ |
    |---|---|---|---|---|---|
    | $(s_A,1)$ | $0{,}5$ | $0{,}9$ | $0{,}9/0{,}5=1{,}8$ | $0{,}4$ | $0{,}5\cdot1{,}8\cdot0{,}4=0{,}36$ |
    | $(s_A,2)$ | $0{,}5$ | $0{,}1$ | $0{,}2$ | $-0{,}4$ | $-0{,}04$ |
    | $(s_B,1)$ | $\tfrac23$ | $0{,}5$ | $0{,}75$ | $1$ | $0{,}5$ |
    | $(s_B,2)$ | $\tfrac13$ | $0{,}5$ | $1{,}5$ | $-2$ | $-1$ |
  - "Cộng theo hành động: $0{,}36-0{,}04=0{,}32$ tại $s_A$, $0{,}5-1=-0{,}5$ tại $s_B$."
- **Dựng dần:** (0) định nghĩa, dạng khác; (1) bảng; (2) dòng cộng.
- **1 phút:** Nhân lợi thế của mỗi hành động cũ với tỉ số xác suất mới trên cũ cho lại lợi thế của chính sách mới, không cần chạy nó.
- **Mới:** tỉ số chính sách.
- **Nguồn số:** $\pi$, $\tilde\pi$ từ `4-01`; $A_\pi(s,a)$ từ `2-06`; kết quả trùng `4-13`.
- **Hình:** không.
- **Ghi chú nguồn:** Định nghĩa 10.21 (tỉ số chính sách, dạng thứ nhất); kiểm sau Mệnh đề 10.22; Định nghĩa 06.24.
- **Diễn giả:** điều kiện hỗ trợ: $\pi'(a\mid s)>0\Rightarrow\pi(a\mid s)>0$, đúng với chính sách softmax. Trên bộ đệm, kỳ vọng thay bằng trung bình trên mẫu, đúng đại lượng mạch 5 tối đa.
- **Phút:** 1.

##### `L10-4-05` · Sai số của hàm thay thế (1) (giữ mã; #22)

- **Câu:** 3. **Nhãn:** hộp.
- **Mặt trang:**
  - "Trừ định nghĩa hàm thay thế khỏi bổ đề chênh lệch hiệu năng:" $$\Delta J-\Delta\mathcal L=\sum_s\bigl(\eta_{\pi'}(s)-\eta_\pi(s)\bigr)\,A_\pi(s,\pi').$$
  - "Trên chuỗi, với $\Delta p_A=p'_A-\tfrac12$, $\Delta p_B=p'_B-\tfrac23$: $A_\pi(s_A,\pi')=0{,}4p'_A-0{,}4(1-p'_A)=0{,}8\,\Delta p_A$ và $A_\pi(s_B,\pi')=p'_B-2(1-p'_B)=3\,\Delta p_B$."
  - "Với $\eta_\pi=(1;\,0{,}45)$:" $$\Delta\mathcal L=1\cdot0{,}8\,\Delta p_A+0{,}45\cdot3\,\Delta p_B=0{,}8\,\Delta p_A+1{,}35\,\Delta p_B .$$
  - "Chỉ $s_B$ đổi số lần thăm, $\eta_{\pi'}(s_B)-\eta_\pi(s_B)=\gamma\,\Delta p_A$, nên sai số bằng $\gamma\,\Delta p_A\cdot3\,\Delta p_B=2{,}7\,\Delta p_A\,\Delta p_B$."
  - Hộp: "Với $\tilde\pi$: $\Delta p_A=0{,}4$, $\Delta p_B=-\tfrac16$, sai số $2{,}7\cdot0{,}4\cdot(-\tfrac16)=-0{,}18$."
- **Dựng dần:** (0) công thức sai số; (1) hai lợi thế; (2) $\Delta\mathcal L$; (3) sai số trên chuỗi; (4) hộp.
- **1 phút:** Sai số của hàm thay thế là số lần thăm tăng thêm nhân lợi thế tại trạng thái đó; trên chuỗi nó bằng tích hai mức đổi xác suất.
- **Mới:** công thức sai số.
- **Nguồn số:** $\gamma=0{,}9$; $A_\pi(s,\cdot)$ từ `2-06`; $\eta_\pi$ từ `4-16`; mọi phép tính trên trang (TB9, TB29).
- **Hình:** không.
- **Ghi chú nguồn:** đoạn mở §4.4; Ví dụ 10.11, "Mọi chính sách mới trên chuỗi".
- **Diễn giả:** dạng tổng quát trước, chuỗi sau (#22). Hai thừa số $\gamma\Delta p_A$ và $3\Delta p_B$ cùng bằng $0$ khi $\pi'=\pi$; trang `4-17` dùng điều này.
- **Phút:** 1,5.

##### `L10-4-23` · Sai số của hàm thay thế (2) (mã mới; #22, tách từ `4-05`)

- **Câu:** 3. **Nhãn:** hộp.
- **Mặt trang:**
  - "Khai triển $J=2{,}7p_Ap_B+1-p_A$ tại $p_A=\tfrac12+\Delta p_A$, $p_B=\tfrac23+\Delta p_B$ cho cùng kết quả:" $$\begin{aligned}J&=2{,}7\bigl(\tfrac13+\tfrac23\Delta p_A+\tfrac12\Delta p_B+\Delta p_A\Delta p_B\bigr)+\tfrac12-\Delta p_A\\&=0{,}9+1{,}8\,\Delta p_A+1{,}35\,\Delta p_B+2{,}7\,\Delta p_A\Delta p_B+0{,}5-\Delta p_A\\&=1{,}4+\underbrace{0{,}8\,\Delta p_A+1{,}35\,\Delta p_B}_{\Delta\mathcal L}+2{,}7\,\Delta p_A\,\Delta p_B .\end{aligned}$$
  - Hộp: "Phần bậc nhất của $\Delta J$ là $\Delta\mathcal L$. Phần bậc hai là sai số của trang trước."
  - "Dạng tích chỉ đúng trên chuỗi, nơi chỉ $s_B$ đổi số lần thăm. Trên chuỗi, bước chỉ đổi $p_A$ hoặc chỉ đổi $p_B$ có sai số $0$." (Đ2)
- **Dựng dần:** (0) dòng mở; (1)–(3) ba dòng khai triển; (4) hộp; (5) dòng phạm vi.
- **1 phút:** Khai triển $J$ trực tiếp xác nhận: hàm thay thế là phần bậc nhất, sai số là tích $2{,}7\Delta p_A\Delta p_B$.
- **Mới:** không (kiểm bằng khai triển).
- **Nguồn số:** $(\tfrac12+\Delta p_A)(\tfrac23+\Delta p_B)=\tfrac13+\tfrac23\Delta p_A+\tfrac12\Delta p_B+\Delta p_A\Delta p_B$; $2{,}7\cdot\tfrac13=0{,}9$, $2{,}7\cdot\tfrac23=1{,}8$, $2{,}7\cdot\tfrac12=1{,}35$; $1{,}8-1=0{,}8$.
- **Hình:** không. **Ghi chú nguồn:** Ví dụ 10.11, "Mọi chính sách mới trên chuỗi".
- **Diễn giả:** trang này là phép kiểm, không phải dạng tổng quát; với MDP khác, sai số không có dạng tích nhưng vẫn là $\sum_s(\eta_{\pi'}-\eta_\pi)A_\pi(s,\pi')$.
- **Phút:** 1,5.

##### `L10-4-17` · Hàm thay thế tiếp xúc $J$ tại chính sách cũ (mã mới; #22, TB28)

- **Câu:** 3. **Nhãn:** "Mệnh đề.", "Chứng minh.", "Ý nghĩa:".
- **Mặt trang:**
  - "**Mệnh đề.** Giả thiết: giả thiết chung. Thêm: $\eta_\pi$, $A_\pi$ chính xác. Kết luận: với $\pi=\pi_\theta$," $$\mathcal L_\pi(\pi_\theta)=J(\theta),\qquad\nabla_{\theta'}\mathcal L_\pi(\pi_{\theta'})\big|_{\theta'=\theta}=\nabla_\theta J(\theta).$$
  - "Chứng minh. $A_\pi(s,\pi)=0$ cho giá trị. Với gradient, $\eta_\pi$, $A_\pi$ không phụ thuộc $\theta'$ và $\nabla\pi_{\theta'}=\pi_{\theta'}\psi_{\theta'}$. Gom theo trạng thái được gradient dạng lợi thế."
  - "Trên chuỗi: $\nabla\mathcal L=(0{,}8\cdot\tfrac14;\,1{,}35\cdot\tfrac29)=(0{,}2;\,0{,}3)=\nabla J$. Ý nghĩa: một bước đủ ngắn theo hướng tăng của $\mathcal L$ làm $J$ tăng."
  - "Với lợi thế ước lượng, giá trị không còn khớp: critic $(1{,}4;\,1)$ và $\lambda=0$ cho tại $s_A$ $\tfrac12(-0{,}5)+\tfrac12(-0{,}4)=-0{,}45\ne0$." (Đ2)
- **Dựng dần:** (0) mệnh đề; (1) chứng minh; (2) dòng số, ý nghĩa; (3) dòng lợi thế ước lượng.
- **1 phút:** Tại chính sách cũ, hàm thay thế và $J$ có cùng giá trị và cùng gradient.
- **Mới:** tính tiếp xúc.
- **Nguồn số:** hệ số $0{,}8$, $1{,}35$ từ `4-05`; $p_s(1-p_s)=\tfrac14$, $\tfrac29$ từ `1-11`; $(0{,}2;\,0{,}3)$ từ `1-11`; $(-0{,}5;\,-0{,}4)$ là kỳ vọng của $\delta_0$ với critic sai (`3-06`, `2-07`).
- **Hình:** không.
- **Ghi chú nguồn:** Mệnh đề 10.22 (dòng "Chứng minh." gộp Bước 1, giá trị, và Bước 2, gradient); kiểm và phản ví dụ sau Mệnh đề 10.22.
- **Diễn giả:** cách nhìn khác qua công thức sai số của `4-05`: sai số là tổng các tích của hai thừa số cùng bằng $0$ tại $\pi$, nên gradient của nó bằng $0$.
- **Phút:** 1,5.

##### `L10-4-04` · Hàm thay thế trên đoạn thẳng từ $\pi$ tới $\tilde\pi$ (giữ mã; #22)

- **Câu:** 4 (mạch 4). **Nhãn:** hộp.
- **Mặt trang:**
  - "Đoạn thẳng $p_A=\tfrac12+0{,}4t$, $p_B=\tfrac23-\tfrac t6$, $t\in[0,1]$: $t=0$ là $\pi$, $t=1$ là $\tilde\pi$. Thế $\Delta p_A=0{,}4t$, $\Delta p_B=-\tfrac t6$ vào trang trước:"
  - "$\Delta\mathcal L=0{,}8\cdot0{,}4t-1{,}35\cdot\tfrac t6=0{,}095t$. Sai số $=2{,}7\cdot0{,}4t\cdot(-\tfrac t6)=-0{,}18t^2$; $\Delta J=0{,}095t-0{,}18t^2$."
  - Hộp: "Hai đường tiếp xúc tại $t=0$ và tách nhau theo $t^2$; $\Delta J$ lớn nhất, $0{,}0125$, tại $t\approx0{,}26$ và bằng $0$ tại $t=\tfrac{19}{36}\approx0{,}53$."
- **Dựng dần:** (0) hai dòng chữ, khung đồ thị trống; (1) đường $\Delta\mathcal L$; (2) đường $\Delta J$; (3) điểm $t=1$ và hộp.
- **1 phút:** Trên đoạn từ chính sách cũ tới $\tilde\pi$, hàm thay thế là tiếp tuyến của $J$; ở bước ngắn hai đường gần nhau, ở $t=1$ chúng trái dấu.
- **Mới:** tham số đoạn thẳng $t$.
- **Nguồn số:** công thức sai số và hệ số từ `4-05`; $t^*=0{,}095/0{,}36=0{,}264$, $\Delta J(t^*)=0{,}095^2/0{,}72=0{,}0125$; $t_0=0{,}095/0{,}18=19/36$; tại $t=1$: $0{,}095$; $-0{,}085$ từ `4-16`.
- **Hình:** sửa `ham-thay-the-tiep-xuc-buoc0.svg`, `-buoc1.svg`, `ham-thay-the-tiep-xuc.svg`: trục $t\in[0,1]$, trục tung khoảng $[-0{,}1;\,0{,}1]$; đường cam nét đứt "hàm thay thế: $\Delta\mathcal L=0{,}095t$"; parabol xanh nét liền "giá trị thật: $\Delta J=0{,}095t-0{,}18t^2$"; điểm tại $t=1$ ghi "$+0{,}095$" (cam) và "$-0{,}085$" (xanh); dưới trục nhãn "$\pi$" tại $t=0$ và "$\tilde\pi=(0{,}9;\,0{,}5)$" tại $t=1$; không đánh dấu $t=0{,}25$ (dành cho câu hỏi nhanh). Bỏ nhãn "đoán/thật" (#23, TB26). Nửa phải, khoảng 50%.
- **Ghi chú nguồn:** Ví dụ 10.11, "Hai bước trên một đường thẳng".
- **Diễn giả:** đây là trường hợp riêng của công thức sai số, đặt sau dạng tổng quát (#22). Tiếp xúc tại $t=0$ là mệnh đề của trang trước nhìn trên một đường.
- **Phút:** 1,5.

##### `L10-4-10` · Câu hỏi nhanh: bước ngắn trên đoạn thẳng (giữ mã, số mới; TB22)

- **Câu:** 4. **Nhãn:** "Câu hỏi:", "Lời giải:".
- **Mặt trang:**
  - "Bước ngắn $t=0{,}25$: chính sách $(0{,}6;\,0{,}625)$."
  - "Câu hỏi: hàm thay thế dự báo $\Delta J$ bao nhiêu, sai số bao nhiêu, và $J$ có tăng không?"
  - "Lời giải: $\Delta\mathcal L=0{,}095\cdot0{,}25\approx0{,}024$. Sai số $-0{,}18\cdot0{,}25^2\approx-0{,}011$; $\Delta J=0{,}0125>0$, cùng dấu với $\Delta\mathcal L$. Sai số nhỏ hơn ở $\tilde\pi$ $16$ lần, bằng $(1/0{,}25)^2$."
- **Dựng dần:** (0) dữ kiện, câu hỏi, đồ thị của `4-04` với dấu "?" tại $t=0{,}25$; (1) lời giải.
- **1 phút:** Bước ngắn bốn lần cho sai số nhỏ mười sáu lần; hàm thay thế và $J$ cùng dấu.
- **Mới:** không. **Nguồn số:** công thức từ `4-04`; $J(0{,}6;\,0{,}625)=2{,}7\cdot0{,}375+0{,}4=1{,}4125$, $\Delta J=0{,}0125$ (ghi chú diễn giả).
- **Hình:** bản `ham-thay-the-tiep-xuc-cau-hoi.svg` (mới, từ `ham-thay-the-tiep-xuc.svg`): thêm đường đứng mảnh tại $t=0{,}25$, dấu "?" đỏ; bản `-loi-giai` thay "?" bằng hai điểm "$0{,}024$" (cam), "$0{,}0125$" (xanh).
- **Ghi chú nguồn:** Ví dụ 10.11, điểm $t=0{,}25$.
- **Diễn giả:** "Gợi ý: thế $t=0{,}25$ vào hai công thức của trang trước." Năng lực kiểm tra: đọc sai số bậc hai theo độ dài bước. Câu này dẫn sang câu hỏi "bước phải ngắn đến mức nào", trả lời ở định lý sau.
- **Phút:** 2.

##### `L10-4-24` · Biến phân toàn phần và phân bố chiếm dụng (mã mới; tách từ `4-06`; TB12, TB13, TB24)

- **Câu:** 3–4 (mạch 4). **Nhãn:** "Định nghĩa.", "Ký hiệu:".
- **Mặt trang:**
  - "Sai số $-0{,}18$ đến từ khác biệt giữa hai phân phối hành động: tại $s_A$, $\tilde\pi$ chuyển $0{,}4$ xác suất sang hành động 1." (Đ5)
  - "**Định nghĩa.** Khoảng cách biến phân toàn phần (total variation distance, TV) giữa $\pi'$ và $\pi$ tại $s$ là" $$D_{\mathrm{TV}}(s)=\tfrac12\sum_a\bigl|\pi'(a\mid s)-\pi(a\mid s)\bigr| .$$
  - "Ký hiệu: phân bố chiếm dụng $\nu^\pi(s)=(1-\gamma)\,\eta_\pi(s)$; $\chi_{\pi'}=\max_s|A_\pi(s,\pi')|$."
  - "Ở đây, với $\tilde\pi$: $D_{\mathrm{TV}}(s_A)=\tfrac12(0{,}4+0{,}4)=0{,}4$, $D_{\mathrm{TV}}(s_B)=\tfrac12(\tfrac16+\tfrac16)=\tfrac16$; $\nu^\pi=0{,}1\cdot(1;\,0{,}45)=(0{,}1;\,0{,}045)$, $\mathbb E_{\nu^\pi}[D_{\mathrm{TV}}]=0{,}1\cdot0{,}4+0{,}045\cdot\tfrac16=0{,}0475$; $\chi_{\tilde\pi}=\max(0{,}32;\,0{,}5)=0{,}5$." (Đ6)
- **Dựng dần:** (0) dòng trực quan; (1) định nghĩa; (2) ký hiệu; (3) dòng số.
- **1 phút:** TV đo lượng xác suất phải dời để biến phân phối hành động này thành phân phối kia; trên chuỗi nó bằng $0{,}4$ tại $s_A$ và $\tfrac16$ tại $s_B$.
- **Mới:** $D_{\mathrm{TV}}$; $\nu^\pi$ (hai đối tượng, TB24).
- **Nguồn số:** $\pi$, $\tilde\pi$ từ `4-01`; $\eta_\pi$ từ `4-16`; $A_\pi(s,\tilde\pi)$ từ `4-13`.
- **Hình:** không.
- **Ghi chú nguồn:** Định nghĩa 10.23 (biến phân toàn phần), Định nghĩa 10.18; Ví dụ 10.12.
- **Diễn giả:** $D_{\mathrm{TV}}$ đối xứng, nằm trong $[0,1]$, bằng hiệu lớn nhất giữa xác suất hai phân phối gán cho cùng một tập hành động. $\nu^\pi$ là phân bố chiếm dụng chuẩn hóa của ghi chú; tổng của nó trên chuỗi là $0{,}145\le1$.
- **Phút:** 1.

##### `L10-4-06` · Định lý chặn cải thiện (giữ mã; #23, TB28)

- **Câu:** 3–4 (mạch 4). **Nhãn:** "Định lý.", "Giả thiết:", "Kết luận:", "Ý nghĩa:".
- **Mặt trang:**
  - "**Định lý** (chặn cải thiện). Giả thiết: giả thiết chung. Thêm: $\pi'(a\mid s)>0\Rightarrow\pi(a\mid s)>0$. Kết luận:" $$J(\pi')-J(\pi)\ \ge\ \Delta\mathcal L-\frac{2\gamma\,\chi_{\pi'}}{(1-\gamma)^2}\,\mathbb E_{S\sim\nu^\pi}\bigl[D_{\mathrm{TV}}(S)\bigr].$$
  - "Ý nghĩa: nếu số hạng phạt nhỏ hơn $\Delta\mathcal L$ thì $J$ tăng. Với $\gamma=0{,}9$, thừa số $\gamma/(1-\gamma)^2$ bằng $90$."
- **Dựng dần:** (0) định lý; (1) ý nghĩa.
- **1 phút:** Mức tăng thật không nhỏ hơn mức dự báo trừ một phạt tỉ lệ với kỳ vọng của khoảng cách giữa hai chính sách theo phân bố trạng thái của chính sách cũ.
- **Mới:** định lý.
- **Nguồn số:** $0{,}9/0{,}01=90$.
- **Hình:** không.
- **Ghi chú nguồn:** Định lý 10.26.
- **Diễn giả:** mọi đại lượng của kết luận đã định nghĩa ở `4-24` (TB28). "Lợi thế và phân bố chính xác" là điều kiện áp dụng, không phải giả thiết (#23). Cận vẫn đúng khi thay $\chi_{\pi'}$ bằng $\max_{s,a}|A_\pi(s,a)|$. Nhận xét 10.28: cận dạng lớn nhất của Schulman và cộng sự (2015).
- **Phút:** 1.

##### `L10-4-18` · Ý tưởng chứng minh: định lý chặn cải thiện (mã mới; #23)

- **Câu:** 3–4. **Nhãn:** "Ý tưởng chứng minh." (tiêu đề), "Bổ đề" nêu tên trong bước 2.
- **Mặt trang** (năm bước của chứng minh Định lý 10.26, Đ8):
  - "Bước 1 (đẳng thức chính xác): bổ đề chênh lệch hiệu năng, $\Delta J=\sum_s\eta_{\pi'}(s)A_\pi(s,\pi')$."
  - "Bước 2 (tách): $\eta_{\pi'}=\eta_\pi+(\eta_{\pi'}-\eta_\pi)$. Bước 3 (hàm thay thế): phần với $\eta_\pi$ là $\Delta\mathcal L$."
  - "Bước 4 (bất đẳng thức Hölder): $\sum_s(\eta_{\pi'}-\eta_\pi)(s)A_\pi(s,\pi')\ge-\chi_{\pi'}\sum_s|\eta_{\pi'}(s)-\eta_\pi(s)|$."
  - "Bước 5 (bổ đề dịch chuyển phân bố chiếm dụng): khác biệt ở mỗi bước tích lũy dọc lượt," $$\sum_s|\eta_{\pi'}(s)-\eta_\pi(s)|\ \le\ \frac{2\gamma}{(1-\gamma)^2}\,\mathbb E_{S\sim\nu^\pi}\bigl[D_{\mathrm{TV}}(S)\bigr].\ \square$$
  - Hộp "Câu hỏi: ở Bước 5, vì sao xuất hiện thừa số $1/(1-\gamma)^2$ chứ không phải $1/(1-\gamma)$?" → mảnh sau: "Một thừa số $1/(1-\gamma)$ đổi $\nu$ thành $\eta$ (độ dài hiệu dụng của lượt). Thừa số thứ hai đến từ việc khác biệt ở mỗi bước tích lũy qua các bước sau." (Đ9)
- **Dựng dần:** từng bước một mảnh; câu hỏi; lời giải câu hỏi.
- **1 phút:** Sai số là số lần thăm thay đổi nhân lợi thế; lợi thế bị chặn bởi $\chi$, số lần thăm thay đổi bị chặn theo khoảng cách TV.
- **Mới:** bổ đề dịch chuyển (nêu trong bước).
- **Nguồn số:** không.
- **Hình:** không.
- **Ghi chú nguồn:** Định lý 10.26, chứng minh Bước 1–5; Bổ đề 10.25 (dạng $\nu$: $\lVert\nu'-\nu\rVert_1\le\frac{2\gamma}{1-\gamma}\mathbb E_\nu[D_{\mathrm{TV}}]$, chia cho $1-\gamma$ được dạng $\eta$ trên trang).
- **Diễn giả:** Bước 5 là nơi xuất hiện thừa số $1/(1-\gamma)^2$: một $1/(1-\gamma)$ từ độ dài lượt hiệu dụng, một từ việc khác biệt tích lũy. Chứng minh Bổ đề 10.25 dùng dạng ma trận $(I-\gamma P_\pi)^{-1}$ (ghi chú).
- **Phút:** 2.

##### `L10-4-19` · Ví dụ: chặn cải thiện trên chuỗi (mã mới; #23; trạm dừng)

- **Câu:** 4. **Nhãn:** hộp.
- **Mặt trang:**
  - "Ở đây $\nu^\pi=(0{,}1;\,0{,}045)$. $D_{\mathrm{TV}}$ và $\chi_{\pi'}$ tính theo định nghĩa ở trang trước định lý." (Đ6)

    | | Bước tới $\tilde\pi$ | Bước chỉ đổi $p_B$ thêm $\Delta>0$ |
    |---|---|---|
    | $\Delta\mathcal L$ | $0{,}095$ | $0{,}45\cdot3\Delta=1{,}35\Delta$ |
    | $D_{\mathrm{TV}}(s_A)$; $D_{\mathrm{TV}}(s_B)$ | $0{,}4$; $\tfrac16$ | $0$; $\Delta$ |
    | $\mathbb E_{\nu^\pi}[D_{\mathrm{TV}}]$ | $0{,}1\cdot0{,}4+0{,}045\cdot\tfrac16=0{,}0475$ | $0{,}045\Delta$ |
    | $\chi$; hệ số $\tfrac{2\gamma\chi}{(1-\gamma)^2}$ | $0{,}5$; $90$ | $3\Delta$; $540\Delta$ |
    | cận dưới của $\Delta J$ | $0{,}095-90\cdot0{,}0475=-4{,}18$ | $1{,}35\Delta-24{,}3\Delta^2$ |
    | $\Delta J$ thật | $-0{,}085$ | $1{,}35\Delta$ |
  - Hộp: "Cận đúng nhưng lỏng: nó chỉ chứng nhận $J$ tăng khi $\Delta<1{,}35/24{,}3\approx0{,}056$."
- **Dựng dần:** (0) dòng $\nu^\pi$, cột "bước tới $\tilde\pi$"; (1) cột thứ hai; (2) hộp.
- **1 phút:** Với bước tới $\tilde\pi$, cận là $-4{,}18$, đúng nhưng xa $-0{,}085$; cận chỉ dương với bước rất ngắn.
- **Mới:** không (áp dụng).
- **Nguồn số:** $\eta_\pi$ từ `4-16`; $A_\pi(s,\tilde\pi)$ từ `4-13`; $D_{\mathrm{TV}}(s_A)=\tfrac12(0{,}4+0{,}4)$, $D_{\mathrm{TV}}(s_B)=\tfrac12(\tfrac16+\tfrac16)$; $C=2\cdot0{,}9\cdot0{,}5/0{,}01=90$; cột hai: $A_\pi(s_A,\pi')=0$, $A_\pi(s_B,\pi')=3\Delta$, $2\cdot0{,}9\cdot3\Delta/0{,}01=540\Delta$, $540\Delta\cdot0{,}045\Delta=24{,}3\Delta^2$; $\Delta J=1{,}35\Delta$ vì $\Delta p_A=0$ (sai số $0$, `4-05`).
- **Hình:** không.
- **Ghi chú nguồn:** Ví dụ 10.12 (bước $\tilde\pi$ và "Bước nhỏ chỉ đổi $s_B$").
- **Diễn giả:** ở cột hai hàm thay thế chính xác, nhưng cận vẫn phạt, vì nó phải đúng cho mọi MDP. Với $\Delta=0{,}05$ cho $0{,}0068>0$, $\Delta=0{,}06$ cho $-0{,}0065<0$. Hệ quả 10.29: tối đa cận dưới cho cải thiện đơn điệu, nhưng bước quá nhỏ.
- **Phút:** 1,5.

##### `L10-4-12` · Phân kỳ Kullback–Leibler (giữ mã; #24)

- **Câu:** 5 (mạch 4). **Nhãn:** "Định nghĩa.", "Dạng khác:".
- **Mặt trang:**
  - "Tại $s_A$, tỉ số của hành động 2 là $0{,}1/0{,}5=0{,}2$: chính sách mới gần bỏ hành động 2. Một độ đo dựa trên log-tỉ số phạt nặng trường hợp này." (Đ5)
  - "**Định nghĩa.** Phân kỳ Kullback–Leibler (Kullback–Leibler divergence, KL) tại $s$, từ $\pi$ tới $\pi'$, và KL trung bình, tổng có trọng số $\nu^\pi$, là" $$D_{\mathrm{KL}}(s)=\sum_a\pi(a\mid s)\log\frac{\pi(a\mid s)}{\pi'(a\mid s)},\qquad\bar D_{\mathrm{KL}}=\sum_s\nu^\pi(s)\,D_{\mathrm{KL}}(s),$$ "với $D_{\mathrm{KL}}(s)=+\infty$ khi $\pi'(a\mid s)=0<\pi(a\mid s)$. $\bar D_{\mathrm{KL}}$ là kỳ vọng theo $\nu^\pi$, không phải trung bình trên các mẫu của một bộ đệm." (Đ4)
  - "Dạng khác: $D_{\mathrm{KL}}(s)=\mathbb E_{a\sim\pi(\cdot\mid s)}[-\log\rho(s,a)]$, tính được từ hành động của lượt cũ."
  - "Với $\tilde\pi$: $D_{\mathrm{KL}}(s_A)=\tfrac12\log\tfrac{0{,}5}{0{,}9}+\tfrac12\log\tfrac{0{,}5}{0{,}1}=\log\tfrac53\approx0{,}511$, $D_{\mathrm{KL}}(s_B)=\tfrac23\log\tfrac43+\tfrac13\log\tfrac23\approx0{,}057$, nên $\bar D_{\mathrm{KL}}=0{,}1\cdot0{,}511+0{,}045\cdot0{,}057\approx0{,}054$. Khi $\tilde p_A\to1$, $D_{\mathrm{KL}}(s_A)\to\infty$ còn $D_{\mathrm{TV}}(s_A)\to0{,}5$."
- **Dựng dần:** (0) dòng trực quan; (1) định nghĩa; (2) dạng khác; (3) dòng số.
- **1 phút:** KL đo khác biệt giữa hai phân phối hành động qua log-tỉ số, và tăng không giới hạn khi chính sách mới gần bỏ hẳn một hành động.
- **Mới:** KL; KL trung bình.
- **Nguồn số:** $\pi$, $\tilde\pi$ từ `4-01`; $\nu^\pi$ từ `4-24`; $\rho$ từ `4-11`.
- **Hình:** không.
- **Ghi chú nguồn:** Định nghĩa 10.23 (KL) và đoạn sau; số $D_{\mathrm{KL}}(s_B)$, $\bar D_{\mathrm{KL}}$ thêm vào ghi chú (N9).
- **Diễn giả:** KL không đối xứng và không là khoảng cách; deck dùng chiều cũ‖mới như TRPO. $\log\tfrac53=\tfrac12\log\tfrac{25}9$. Giới hạn: $\tilde p_A=0{,}99$ cho $1{,}61$, $0{,}999$ cho $2{,}76$.
- **Phút:** 1,5.

##### `L10-4-20` · Bất đẳng thức Pinsker (mã mới; #24, TB28)

- **Câu:** 5. **Nhãn:** "Mệnh đề.", "Giả thiết:", "Kết luận:", "Chứng minh.", "Ý nghĩa:".
- **Mặt trang:**
  - "**Mệnh đề** (bất đẳng thức Pinsker). Giả thiết: $q$, $q'$ là hai phân phối trên tập hữu hạn, logarit tự nhiên. Kết luận:" $$D_{\mathrm{TV}}(q,q')\le\sqrt{\tfrac12D_{\mathrm{KL}}(q\Vert q')},$$ "và cũng đúng với $D_{\mathrm{KL}}(q'\Vert q)$."
  - "Chứng minh. Gộp các phần tử thành hai nhóm $\{q>q'\}$ và phần bù, giữ nguyên $D_{\mathrm{TV}}$ và không làm $D_{\mathrm{KL}}$ tăng, rồi chứng minh trên hai điểm."
  - "Ý nghĩa: KL nhỏ kéo theo khoảng cách TV nhỏ. Với $\tilde\pi$: $0{,}4\le\sqrt{0{,}511/2}=0{,}505$ tại $s_A$, $0{,}167\le\sqrt{0{,}057/2}=0{,}168$ tại $s_B$."
- **Dựng dần:** (0) mệnh đề; (1) chứng minh; (2) ý nghĩa.
- **1 phút:** Khoảng cách TV bị chặn bởi căn của nửa KL; trên chuỗi bất đẳng thức gần chặt tại $s_B$.
- **Mới:** bất đẳng thức Pinsker.
- **Nguồn số:** $D_{\mathrm{TV}}$ từ `4-24`; $D_{\mathrm{KL}}$ từ `4-12`; $\sqrt{0{,}0283}=0{,}168$.
- **Hình:** không.
- **Ghi chú nguồn:** Mệnh đề 10.24(b); dòng "Chứng minh." là Bước 3 (ý tưởng chứng minh) của ghi chú (Cover và Thomas, 2006, Bổ đề 11.6.1).
- **Diễn giả:** phép gộp dùng bất đẳng thức xử lý dữ liệu cho KL; trên hai điểm, khảo sát hiệu hai vế như hàm một biến. Chứng minh đầy đủ nằm ngoài phạm vi học phần. Không có cận ngược: TV nhỏ không kéo theo KL nhỏ (`4-12`).
- **Phút:** 1.

##### `L10-4-21` · Chặn cải thiện theo KL trung bình (mã mới; #24, TB28)

- **Câu:** 5. **Nhãn:** "Hệ quả.", "Chứng minh.", "Ý nghĩa:".
- **Mặt trang:**
  - "**Hệ quả.** Giả thiết: như định lý chặn cải thiện. Kết luận:" $$J(\pi')-J(\pi)\ \ge\ \Delta\mathcal L-\frac{2\gamma\,\chi_{\pi'}}{(1-\gamma)^2}\sqrt{\tfrac12\,\bar D_{\mathrm{KL}}}.$$
  - "Chứng minh. Bất đẳng thức Pinsker tại từng trạng thái, rồi bất đẳng thức Jensen cho hàm lõm $\sqrt{\cdot}$ với khối $\sum_s\nu^\pi(s)\le1$."
  - "Với $\tilde\pi$: phạt $90\sqrt{0{,}054/2}\approx14{,}7$, lớn hơn phạt dạng TV $90\cdot0{,}0475\approx4{,}3$."
  - "Ý nghĩa: giữ $\bar D_{\mathrm{KL}}\le\kappa$ thì phạt không vượt $\frac{2\gamma\chi_{\pi'}}{(1-\gamma)^2}\sqrt{\kappa/2}$."
- **Dựng dần:** (0) hệ quả; (1) chứng minh; (2) dòng số, ý nghĩa.
- **1 phút:** Phạt của định lý viết lại theo KL trung bình; chặn KL trung bình là chặn phạt.
- **Mới:** chặn theo KL.
- **Nguồn số:** $C=90$ từ `4-19`; $\bar D_{\mathrm{KL}}=0{,}0536$ từ `4-12`; $90\cdot\sqrt{0{,}0268}=14{,}74$; $\mathbb E_{\nu^\pi}[D_{\mathrm{TV}}]=0{,}0475$ từ `4-24`.
- **Hình:** không.
- **Ghi chú nguồn:** Hệ quả 10.27; dòng "Chứng minh." gộp Bước 1 (Pinsker theo trạng thái) và Bước 2 (Jensen với khối không quá $1$); số $14{,}7$ thêm vào ghi chú (N9).
- **Diễn giả:** cận yếu hơn định lý vì có thêm hai bất đẳng thức; đổi lại phạt viết theo KL, đại lượng mà miền tin cậy ràng buộc. Hệ quả đúng với cả hai chiều KL.
- **Phút:** 1.

##### `L10-4-07` · Bài toán miền tin cậy (giữ mã; #24)

- **Câu:** 5. **Nhãn:** "Định nghĩa.", "Ý nghĩa:".
- **Mặt trang:**
  - "KL được chọn thay cho TV vì hai lý do. KL trơn theo $\theta$ khi $\pi_\theta>0$, còn $D_{\mathrm{TV}}$ chứa $|\cdot|$ nên không khả vi tại $\pi'=\pi$. Hệ quả trước chặn phạt bằng KL trung bình."
  - "**Định nghĩa.** Với bán kính $\kappa>0$, bài toán miền tin cậy (trust region problem) là" $$\max_\theta\ \mathcal L_{\pi}(\pi_\theta)\quad\text{với ràng buộc}\quad\bar D_{\mathrm{KL}}(\pi\Vert\pi_\theta)\le\kappa .$$
  - "Trên đoạn thẳng từ $\pi$ tới $\tilde\pi$, nghiệm số của $\bar D_{\mathrm{KL}}(t)=0{,}01$ là $t\approx0{,}515$. Tại đó $(p_A;\,p_B)=(0{,}706;\,0{,}581)$ và $\bar D_{\mathrm{KL}}=0{,}1\cdot0{,}093+0{,}045\cdot0{,}0155=0{,}0100$."
  - "Ý nghĩa: trên chuỗi, với $\kappa=0{,}01$, ràng buộc giữ $t\le0{,}515$, nơi $\Delta J\ge0$, và loại $\tilde\pi$, có $\bar D_{\mathrm{KL}}=0{,}054>\kappa$."
- **Dựng dần:** (0) lý do; (1) định nghĩa; (2) hình `-buoc0`, dòng nghiệm số; (3) hình đủ, ý nghĩa.
- **1 phút:** TRPO tối đa hàm thay thế trong một vùng KL trung bình nhỏ; trên chuỗi vùng đó loại phần đoạn thẳng mà $J$ giảm.
- **Mới:** bài toán miền tin cậy.
- **Nguồn số:** $t_\kappa$ giải số $\bar D_{\mathrm{KL}}(t)=0{,}01$ với $p_A=\tfrac12+0{,}4t$, $p_B=\tfrac23-\tfrac t6$ (`kiem_so.py`); $D_{\mathrm{KL}}(s_A)=0{,}093$, $D_{\mathrm{KL}}(s_B)=0{,}0155$ tại $t_\kappa$ theo công thức `4-12`; $\Delta J(0{,}515)=0{,}095\cdot0{,}515-0{,}18\cdot0{,}515^2=0{,}0012$ (công thức `4-04`); $t_0=19/36=0{,}528$ từ `4-04`; $\bar D_{\mathrm{KL}}(\tilde\pi)$ từ `4-12`.
- **Hình:** sửa `ham-thay-the-mien-tin-cay-buoc0.svg`, `ham-thay-the-mien-tin-cay.svg`: cùng hai đường của `4-04` ($0{,}095t$ cam nét đứt, $0{,}095t-0{,}18t^2$ xanh); dải tím nhạt $t\in[0;\,0{,}515]$, nhãn "miền tin cậy, $\kappa=0{,}01$"; phần còn lại phủ mờ, nhãn "ngoài miền"; tại $t=1$ nhãn "$\tilde\pi$: $\bar D_{\mathrm{KL}}=0{,}054$". Nửa phải.
- **Ghi chú nguồn:** Định nghĩa 10.30 và đoạn sau; Hệ quả 10.31; số $t_\kappa$ thêm vào ghi chú (N9).
- **Diễn giả:** hàm mục tiêu của ghi chú là $(1-\gamma)(\mathcal L-J)$, cùng nghiệm. Bài toán không bảo đảm $J$ tăng; Hệ quả 10.31 chặn mức giảm tối đa theo $\sqrt{2\kappa}$. $\kappa$ là siêu tham số. Mép miền ($t=0{,}515$) gần điểm $\Delta J=0$ ($t=0{,}528$) do chọn $\kappa$; với $\kappa$ khác thì khác.
- **Phút:** 1,5.

##### `L10-4-22` · Xấp xỉ bậc hai của KL trung bình (mã mới; TB28)

- **Câu:** 5. **Nhãn:** "Mệnh đề.", "Chứng minh.".
- **Mặt trang:**
  - "Trên chuỗi, $s_B$ chỉ được thăm ở một nửa số lượt, nên đổi $\theta_B$ ít làm đổi KL trung bình hơn đổi $\theta_A$." (Đ5)
  - "**Mệnh đề.** Giả thiết: giả thiết chung. Thêm: $\pi_\theta$ khả vi liên tục hai lần, $\nu^\pi$ giữ cố định. Đặt ma trận thông tin Fisher $F=\sum_s\nu^\pi(s)\,\mathbb E_{a\sim\pi}\bigl[\psi(s,a)\psi(s,a)^\top\bigr]$. Kết luận:" $$\bar D_{\mathrm{KL}}(\theta+\Delta)=\tfrac12\Delta^\top F\Delta+o(\lVert\Delta\rVert^2).$$
  - "Chứng minh. $\bar D_{\mathrm{KL}}$ có cực tiểu $0$ tại $\theta$ nên gradient bằng $0$, và Hessian của $-\mathbb E_{a\sim\pi}\log\pi_\theta(a\mid s)$ tại $\theta$ là $\mathbb E[\psi\psi^\top]$."
  - "Ở đây $F_s=\nu^\pi(s)\,p_s(1-p_s)$: $F=\operatorname{diag}(0{,}1\cdot\tfrac14;\,0{,}045\cdot\tfrac29)=\operatorname{diag}(0{,}025;\,0{,}01)$." (Đ6)
- **Dựng dần:** (0) dòng trực quan, mệnh đề; (1) chứng minh; (2) dòng số.
- **1 phút:** Gần chính sách cũ, KL trung bình là một dạng toàn phương theo bước tham số, với ma trận Fisher.
- **Mới:** ma trận Fisher; xấp xỉ bậc hai.
- **Nguồn số:** $\nu^\pi$ từ `4-24`; $p_s(1-p_s)$ từ `1-11`; $\mathbb E[\psi^2]=p(1-p)^2+(1-p)p^2=p(1-p)$.
- **Hình:** không.
- **Ghi chú nguồn:** Định nghĩa 10.32, Mệnh đề 10.33 (dòng "Chứng minh." gộp Bước 2, gradient, và Bước 3, Hessian); đoạn cuối §5.2.
- **Diễn giả:** Ví dụ 10.13: cùng bước $+1$ trên logit cho KL $0{,}12$ tại $p=0{,}5$ nhưng $0{,}0037$ tại $p=0{,}99$; khoảng cách Euclid trên tham số không đo được mức đổi của chính sách.
- **Phút:** 1.

##### `L10-4-08` · Gradient tự nhiên tập trung bước cập nhật vào $\theta_B$ (giữ mã; sửa văn, giữ nội dung)

- **Câu:** 5. **Nhãn:** "Mệnh đề.", "Chứng minh.".
- **Mặt trang:**
  - "**Mệnh đề** (bước gradient tự nhiên). Với $g\ne0$ và $F$ xác định dương, bài toán $\max_\Delta g^\top\Delta$ với $\tfrac12\Delta^\top F\Delta\le\kappa$ có nghiệm" $$\Delta^*=\sqrt{\frac{2\kappa}{g^\top F^{-1}g}}\;F^{-1}g .$$
  - "Chứng minh. Với tích trong $\langle x,y\rangle_F=x^\top Fy$, bất đẳng thức Cauchy–Schwarz cho $g^\top\Delta=\langle F^{-1}g,\Delta\rangle_F\le\sqrt{g^\top F^{-1}g}\,\sqrt{2\kappa}$, dấu bằng khi $\Delta$ cùng hướng $F^{-1}g$."
  - "Trên chuỗi, $g=\nabla\mathcal L=(0{,}2;\,0{,}3)$ cho gradient tự nhiên $F^{-1}g=(0{,}2/0{,}025;\,0{,}3/0{,}01)=(8;\,30)$."
- **Dựng dần:** (0) mệnh đề, chứng minh, hình `-buoc1` (elip và $g$); (1) dòng $F^{-1}g$, hình đủ.
- **1 phút:** Trong miền KL, bước tốt nhất đi theo $F^{-1}g$; vì $s_B$ ít được thăm, KL ít nhạy với $\theta_B$, nên bước dồn về $\theta_B$.
- **Mới:** gradient tự nhiên.
- **Nguồn số:** $g$ từ `4-17`; $F$ từ `4-22`.
- **Hình:** giữ `elip-gradient-tu-nhien-buoc1.svg`, `elip-gradient-tu-nhien.svg`. Nửa phải.
- **Ghi chú nguồn:** Mệnh đề 10.34(a) (dòng "Chứng minh." gộp Bước 1–3); đoạn cuối §5.2.
- **Diễn giả:** $\Delta^*$ là nghiệm của bài toán xấp xỉ, có thể vi phạm ràng buộc thật; trang sau kiểm trên chuỗi. $F$ suy biến: giả nghịch đảo (Mệnh đề 10.34(b)).
- **Phút:** 1,5.

##### `L10-4-25` · Ví dụ: một bước TRPO trên chuỗi (mã mới; tách từ `4-08`; Đ12, TB29)

- **Hiện hành (G1):** dòng đầu "Ví dụ dùng $g=\nabla\mathcal L$ và $F$ tính chính xác theo $\nu^\pi$."; câu cuối "Bước $\Delta_0$ thỏa ràng buộc KL và làm hàm thay thế tăng, nên giữ nguyên."; không nhắc tìm kiếm lùi, $j$, $g^\gamma$ (đứng trước `4-09`).

- **Câu:** 5. **Nhãn:** không ("Ví dụ:" ở tiêu đề); tên nhóm bước in đậm trùng `4-09` (Đ12).
- **Mặt trang:**
  - "**Tính hướng:** $g=(0{,}2;\,0{,}3)$, $F^{-1}g=(8;\,30)$, $g^\top F^{-1}g=0{,}2\cdot8+0{,}3\cdot30=10{,}6$."
  - "**Chọn độ dài bước** ($\kappa=0{,}01$): $\Delta_0=\sqrt{0{,}02/10{,}6}\cdot(8;\,30)=0{,}0434\cdot(8;\,30)=(0{,}35;\,1{,}30)$."
  - "Chính sách mới: $p_A=\sigma(0{,}35)=0{,}586$, $p_B=\sigma(\log2+1{,}30)=0{,}880$."
  - "KL trung bình thật bằng $0{,}1\,D_{\mathrm{KL}}(s_A)+0{,}045\,D_{\mathrm{KL}}(s_B)=0{,}1\cdot0{,}0150+0{,}045\cdot0{,}156=0{,}0085\le\kappa$. Hàm thay thế tăng: $\Delta\mathcal L=0{,}8\cdot0{,}086+1{,}35\cdot0{,}214=0{,}357>0$. Tìm kiếm lùi nhận bước đầu, $j=0$."
  - Hộp: "$J=2{,}7p_Ap_B+1-p_A=2{,}7\cdot0{,}586\cdot0{,}880+0{,}414=1{,}807$: tăng từ $1{,}4$."
- **Dựng dần:** (0) tính hướng; (1) chọn độ dài bước, chính sách mới; (2) kiểm ràng buộc; (3) hộp.
- **1 phút:** Một bước TRPO trên chuỗi: hướng $(8;\,30)$, bước tới biên miền, KL thật dưới $\kappa$, $J$ tăng lên $1{,}807$.
- **Mới:** không (áp dụng).
- **Nguồn số:** $g$, $F^{-1}g$ từ `4-08`; $D_{\mathrm{KL}}$ theo công thức `4-12` với $p=(0{,}586;\,0{,}880)$; $\Delta p=(0{,}086;\,0{,}214)$; $\Delta\mathcal L$ theo `4-05`; $J$ theo `1-10`.
- **Hình:** không (hoặc `elip-gradient-tu-nhien.svg` thu nhỏ ở góc, không bắt buộc).
- **Ghi chú nguồn:** Thuật toán 10.37, bước 5–6; số được thêm vào ghi chú (N9).
- **Diễn giả:** ví dụ tay của trang thuật toán kế tiếp (Đ12). Xấp xỉ bậc hai cho $\tfrac12\Delta_0^\top F\Delta_0=0{,}01$, KL thật $0{,}0085$: trên chuỗi, xấp xỉ hơi lớn hơn giá trị thật.
- **Phút:** 1,5.

##### `L10-4-09` · Thuật toán TRPO (giữ mã; TB31, #26)

- **Hiện hành (G1):** `h2` "Tối ưu chính sách miền tin cậy (TRPO)"; dòng nhãn "**Thuật toán** (trust region policy optimization, TRPO). Đầu vào: … Đầu ra: …"; câu mở về actor–critic và mục tiêu của TRPO xuống ghi chú diễn giả (vừa khung); "bộ đệm (buffer)" ở bước 1; "Lưu ý:" "$g$ không có $\gamma^t$. Trung bình trên bộ đệm tỉ lệ với $g^\gamma=\mathbb E[\sum_tA_\pi(S_t,A_t)\psi_t]$. Trên chuỗi $g^\gamma=(0{,}2;\,0{,}333)$, khác $\nabla J=(0{,}2;\,0{,}3)$."

- **Câu:** 5. **Nhãn:** "Thuật toán.", "Đầu vào:", "Đầu ra:".
- **Mặt trang:**
  - "TRPO tối đa hàm thay thế ước lượng từ dữ liệu cũ, với KL trung bình không vượt $\kappa$."
  - "Đầu vào: $\pi_\theta$, critic $\hat v_w$; $\gamma$, $\lambda$; bán kính $\kappa$; hệ số co $\zeta\in(0,1)$; số lần co tối đa $j_{\max}$. Đầu ra: $\theta$, $w$."
  - "Mỗi vòng lặp:"
    1. "**Thu lượt:** một bộ đệm bằng $\pi_{\mathrm{old}}=\pi_\theta$, lưu $\log\pi_{\mathrm{old}}(A_t\mid S_t)$."
    2. "**Ước lượng lợi thế:** $\widehat A_t$ bằng GAE."
    3. "**Tính hướng:** $g=$ trung bình trên bộ đệm của $\widehat A_t\psi_t$; giải gần đúng $Fx=g$ bằng gradient liên hợp, chỉ dùng tích $Fv$."
    4. "**Chọn độ dài bước:** $\Delta_0=\sqrt{2\kappa/(x^\top Fx)}\,x$; thử $\theta_{\mathrm{old}}+\zeta^j\Delta_0$, $j=0,1,\dots,j_{\max}$, nhận bước đầu tiên có hàm thay thế mẫu tăng và KL trung bình mẫu $\le\kappa$. Không có $j$ nào đạt thì giữ $\theta=\theta_{\mathrm{old}}$."
    5. "**Cập nhật critic:** hồi quy $\hat v$ về $\widehat A_t+\hat v_{\mathrm{old}}(S_t)$." (Đ12)
- **Dựng dần:** không.
- **1 phút:** TRPO: GAE, gradient, gradient tự nhiên gần đúng, bước tới biên miền, kiểm lại trên dữ liệu.
- **Mới:** thuật toán.
- **Nguồn số:** không (ví dụ tay ở `4-25`, cùng tên nhóm "Tính hướng", "Chọn độ dài bước").
- **Hình:** không (danh sách ≈ 9 dòng, trang riêng). Sơ đồ khung `so-do-neo-m4-ra*.svg` bỏ (TB31: sơ đồ chỉ bổ sung; không còn chỗ).
- **Ghi chú nguồn:** Thuật toán 10.37; Thuật toán 10.36; Nhận xét 10.38.
- **Diễn giả:** trên chuỗi, bước của `4-25` có KL thật $0{,}0085\le0{,}01$ và hàm thay thế tăng ($\Delta\mathcal L=0{,}357$), nên tìm kiếm lùi nhận $j=0$; $J$ tăng từ $1{,}4$ lên $1{,}807$. So với định lý, TRPO thay năm điểm: trung bình trên bộ đệm thay kỳ vọng có chiết khấu, lợi thế GAE thay lợi thế đúng, hàm thay thế bậc một và KL bậc hai, gradient liên hợp dừng sớm, ràng buộc KL thay phạt TV; nên TRPO trong thực hành không bảo đảm $J$ tăng. Chi phí: khoảng mười tích Fisher–vector mỗi vòng, một bộ máy bậc hai riêng.
- **Phút:** 2.
