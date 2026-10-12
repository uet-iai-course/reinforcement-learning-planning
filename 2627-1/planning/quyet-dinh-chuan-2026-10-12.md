# Quyết định chung cho đợt sửa Bài 01–07 theo chuẩn 2026-10-12

Điều phối viên (phiên Claude Code chính) chốt các quyết định dưới đây sau khi đọc bảy báo cáo kiểm toán `planning/lec-NN/revision-plan-2026-10-12.md`. Yêu cầu hiện hành của người dùng là áp dụng chuẩn 2026-10-12 trong `AGENTS.md` cho mọi deck, ghi chú bài giảng và bài tập của Bài 01–07; chuẩn này thay các chỉ dẫn trang lẻ trước đó khi hai bên mâu thuẫn. Mọi tác tử soạn và rà soát của đợt này đọc tệp này trước khi làm việc. Quyết định riêng của từng bài nằm ở mục cuối.

## 1. Thuật ngữ thống nhất toàn học phần

| Khái niệm | Dùng | Không dùng |
|---|---|---|
| return | lợi tức (return) ở lần đầu, sau đó "lợi tức" | tổng thưởng, phần thưởng tích lũy, điểm thưởng tích lũy |
| reward | phần thưởng (reward); "thưởng" trong cụm "thưởng kỳ vọng", "thưởng một bước" | điểm thưởng |
| Markov decision process | quá trình quyết định Markov (Markov decision process, MDP) | quy trình quyết định Markov |
| episode | lượt (episode) | tập, hồi |
| trajectory | quỹ đạo (trajectory) | — |
| tie-breaking | quy tắc phá hòa (tie-breaking) | quy tắc giữ hòa |
| sweep | lượt quét (sweep) | — |
| bootstrap target | mục tiêu bootstrap (bootstrap target) | — |
| semi-gradient | bán gradient (semi-gradient); Monte Carlo với xấp xỉ hàm là "Monte Carlo gradient", không phải bán gradient | bán gradient MC |
| on-policy, off-policy | theo chính sách (on-policy), khác chính sách (off-policy) | — |
| agent | tác tử (agent) | tác nhân |
| almost surely | hầu chắc chắn (almost surely) | gần chắc chắn |
| Bellman operator | $T_\pi$, $T_*$ (chỉ số dưới, theo Bài 04–05) | $T^\pi$ |
| first-visit, every-visit | lần ghé đầu tiên (first-visit), mọi lần ghé (every-visit); theo Định nghĩa 05.6 | lần ghé đầu |

Thuật ngữ tiếng Anh đặt trong ngoặc ở lần xuất hiện đầu của mỗi tài liệu. "Lời giải", không "Đáp án". Thuật ngữ mới của bài ghi vào bảng Việt–Anh trong `outline.md`.

## 2. Ký hiệu thống nhất

- Giá trị thật: $v_\pi$, $q_\pi$, $v_*$, $q_*$ (chữ thường, theo Sutton và Barto); bảng hoặc bộ xấp xỉ đang học: $V$, $Q$, $\hat v(s,\mathbf w)$. Bài 01 đổi $V^\pi$ thành $v_\pi$.
- Mô hình: $p(s',r\mid s,a)$ chữ thường; $p(s'\mid s,a)$ và $r(s,a)$ suy ra. Hệ số chiết khấu $\gamma$ đứng ngoài bộ $(\mathcal S,\mathcal A,p)$ theo Sutton và Barto; bảng ký hiệu nêu tương ứng với $\langle S,A,T,R,\gamma\rangle$ của giáo trình *Học máy thống kê* một lần.
- Tên trạng thái, nút, ô viết chữ đứng: $\mathrm H,\mathrm L,\mathrm S,\mathrm X,\mathrm G$; hành động có tên viết chữ đứng $\mathrm{tim},\mathrm{cho},\mathrm{sac}$. Chữ nghiêng dành cho biến. Sửa SVG tương ứng khi nhãn trùng ký hiệu biến ($G_t$, $H_t$).
- Chi phí mỗi bước trong ví dụ thiết kế phần thưởng: $c$ (không dùng $\alpha$, dành cho bước học). Ngưỡng dừng của các phép lặp: $\theta$ (Sutton và Barto); $\varepsilon$ dành cho chính sách $\varepsilon$-tham lam.
- Phản ví dụ hàm lợi ích trong Bài 02 dùng $W$ thay $V$.
- Dấu thập phân: dấu phẩy trong deck và ghi chú, viết `0{,}5` trong KaTeX và "0,5" trong chữ; các số trong notebook (mã và kết quả in ra) giữ dấu chấm, ô Markdown của notebook không sửa trong đợt này trừ tham chiếu mục.
- Lịch sử $H_t$: Bài 01 định nghĩa trên quan sát, $H_t=(O_0,A_0,R_1,\dots,O_t)$ (bài chưa giả thiết quan sát đầy đủ, theo Sutton và Barto §17.3); từ Bài 02 trở đi, trong khung quan sát đầy đủ, $H_t=(S_0,A_0,R_1,\dots,S_t)$ và ghi chú Bài 02 nêu một câu rằng đây là trường hợp $O_t=S_t$ của định nghĩa ở Bài 01.
- Chỉ số thời gian: $R_{t+1}$ là phần thưởng của chuyển từ $t$ sang $t+1$; $G_T=0$; giá trị trạng thái kết thúc bằng $0$.

## 3. Nguồn và trích dẫn

- Bỏ mọi liên kết tới `../RL-hk2-2025-2026/*.pdf` (tệp không được theo dõi) trong deck và ghi chú; thay bằng trích dẫn văn bản: "Bài giảng gốc (2025–2026), trang N" và "Bài tập tuần N (2025–2026), bài k". Các đề bài tập tuần là nguồn hợp lệ cho `exercises.md`.
- Giáo trình: dẫn tác giả, năm, chương và mục. Số trang chỉ ghi khi xác minh được trên bản sách; Sutton và Barto (2018) có bản PDF tại `/data/tqlong/qa/sources/sutton-barto-rl2020` (trang in bằng trang PDF trừ 22). Puterman, Bertsekas, Szepesvári: dẫn mục, không ghi trang.
- Nguồn Russell và Norvig, *AIMA*, §17.1 cho định lý ưu tiên dừng (Bài 02) chỉ dẫn nếu tác tử soạn xác minh được nội dung.
- Mọi bộ số tự xây dựng ghi "số liệu sư phạm tự xây dựng".

## 4. Số hiệu và tham chiếu chéo giữa các bài

- Mỗi ghi chú đánh số theo `AGENTS.md` §"Môi trường và đánh số": một bộ đếm chung `NN.k` cho Định nghĩa, Định lý, Mệnh đề, Bổ đề, Hệ quả, Nhận xét, Thuật toán; bộ đếm riêng cho Ví dụ và Bài tập; Tình huống `NN.1`, `NN.2`.
- Bảy ghi chú được viết lại song song, nên trong đợt này kết quả của bài khác được dẫn bằng "ghi chú Bài 0N, Mục k" kèm phát biểu lại trong một câu đủ để dùng ngay. Một đợt đồng bộ sau sẽ thay bằng số hiệu `0N.k`; mỗi ghi chú ghi giới hạn này một lần trong `review-log.md`.
- Mục "Tóm tắt chương" liệt kê đủ số hiệu của bài; đợt đồng bộ dùng danh sách này.
- `note-topic-id` cũ (`lec-NN-part-0k`, `lec-NN-topic-NN`) được giữ cho các chủ đề còn tồn tại; chủ đề mới nhận mã tiếp theo. Không đổi `id` trang đã được học liệu liên kết.

## 5. Deck

- Trang bìa: tên học phần, "Bài NN", tên bài, câu luận đề một dòng, "Trường Đại học Công nghệ, Đại học Quốc gia Hà Nội", "Năm học 2026–2027, học kỳ 1". Không ghi tên giảng viên.
- Mạch mở đầu và mạch kết luận theo `AGENTS.md` §"Mẫu RevealJS bắt buộc"; trang "Nội dung" được phép 7 dòng khi bài có 7 mạch (ghi ngoại lệ trong storyboard).
- Mã trang tiêu đề mạch: `<tiền tố>00` nếu chưa dùng, nếu đã dùng thì `<tiền tố>T` (Bài 01, Bài 05 mạch tách); với mã dạng `L07-NN` dùng `L07-M<k>T` theo đề xuất của kế hoạch Bài 07. `id="mach-N"`.
- Số trang tăng lên 60–70 là chấp nhận được khi storyboard phân bổ đủ 120 phút; nếu vượt, chuyển chi tiết (dạng ma trận, chi phí, biến thể) sang ghi chú bài giảng, không thu nhỏ chữ.
- Bỏ mọi khối `<style>` hoặc lớp cục bộ thu nhỏ chữ (`font-size` dưới 1em trên trang, `.dense`, `.92em`); dùng lớp chung của `lecture-slide.css`. Không sửa `lecture-slide.css`; nếu thật sự cần, dừng và báo điều phối viên.
- Trang "Câu hỏi kiểm tra" cuối mạch đổi thành "Bài tập: <chủ đề>" có "Câu hỏi:" và "Lời giải:" trên mặt trang; câu còn lại gom về "Câu hỏi tự kiểm tra" của mạch kết luận.
- Các tệp planning cũ ngoài ba tệp chuẩn (`analysis.md`, `note-for-author.md`, `concept-flow-audit.md`, `detailed-slide-plan.md`, `storyboard-mdp-replanned.md`) được giữ và thêm một dòng đầu tệp: "Hồ sơ lịch sử trước đợt sửa 2026-10-12; không còn phản ánh deck hiện tại." Không xóa.

## 6. Ghi chú bài giảng

- Viết lại theo `AGENTS.md` §"Tiêu chuẩn giáo trình cho ghi chú bài giảng" và mẫu `materials/_templates/lecture-note.md`, giữ nội dung đúng của bản cũ, bổ sung theo mục B của kế hoạch từng bài. Ghi chú dùng cùng bộ số với deck (ví dụ xuyên suốt chung); Bài 04 bỏ bộ số riêng của ghi chú cũ.
- Đoạn "Trong thực hành" dùng số liệu của notebook chỉ khi notebook đã nhúng kết quả; ghi "một lần chạy đã nhúng trong notebook".
- Tác tử soạn ghi vào `review-log.md` giáo trình và mục đã tham khảo cho từng mục; không dịch hay chép.

## 7. Bài tập và notebook

- `exercises.md` theo mẫu `materials/_templates/exercises.md` và kế hoạch mục C của từng bài; viết sau khi deck đã commit (giai đoạn III).
- Notebook: trong giai đoạn III được sửa ô Markdown để cập nhật tham chiếu mục và tên gọi; không chạy lại, giữ nguyên output, chạy `nbformat.validate`. Không sửa mã.
- `index.html` do điều phối viên sửa: nhóm "Bài tập" hiển thị `Chưa có` cho tới khi `exercises.md` của bài qua kiểm định.

## 8. Quyết định riêng từng bài

- **Bài 01:** gộp mạch E và F thành mạch 5 (7 mạch). Bỏ phụ lục H00–H03 (thông tin tổ chức chưa xác minh), ghi lý do trong review-log. H06–H07 về trí tuệ nhân tạo tổng quát chuyển thành Bài tập 01.16 [Tìm hiểu], không giữ trang. Ví dụ xuyên suốt "robot dọn dãy bốn ô" với số liệu sư phạm. Kiểm thế cờ gốc (PPTX tr. 28–30): nếu nguồn có 2 X và 3 O thì nêu O đi trước; nếu không, sửa ba SVG và thêm nhánh $a=6$. Sửa lỗi giá trị sau nước thắng (bằng 0, thưởng $+1$).
- **Bài 02:** theo mục "Quyết định của điều phối viên" trong `planning/lec-02/revision-plan-2026-10-12.md`.
- **Bài 03:** gộp mạch Markov với mạch mô hình MDP (7 mạch). Không làm bài thực hành riêng; dẫn sang notebook CartPole của Bài 04.
- **Bài 04:** ghi chú dùng bộ số của deck và nguồn; thay các SVG của ghi chú bằng `dp04-*.svg`, vẽ lại `convergence.svg` theo $30\cdot0{,}9^k$. Bài 3–9 của hw3 và Bài 10 của hw04 là nguồn hợp lệ cho `exercises.md`.
- **Bài 05:** 6 mạch (tách mạch D thành hai); mã trang tiêu đề mạch tách dùng `L05-DT` và `L05-ET` theo kế hoạch. Dãy bốn ô được đặt tên "tàu đổ bộ thu nhỏ" nhưng giữ nguyên số liệu; ô tự chuyển của Lunar Lander ở C06b được phép. Giữ $\Delta_k$ nhưng gọi tên khi xuất hiện; ngưỡng dừng dùng $\theta$. SVG chưa dùng (`design-grid.svg`, `mc-td-timeline.svg`): dùng nếu có chỗ, nếu không thì xóa và ghi review-log. Deck writer đồng bộ outline, storyboard, review-log với commit `bc95338`.
- **Bài 06:** 7 mạch. Nội dung đã có ở Bài 03–05 ($q_\pi$, cải thiện tham lam, lần ghé, trung bình gia tăng, Robbins–Monro theo trạng thái) chuyển thành "Nhắc lại:" kèm phát biểu lại; đóng góp mới của bài là ước lượng theo cặp, cải thiện trong lớp $\varepsilon$-mềm, Robbins–Monro theo cặp và GLIE.
- **Bài 07:** 7 mạch (tách mạch kết luận khỏi Q-learning). Ví dụ dự đoán (L07-06, L07-14, L07-19) chỉ đổi tên thành "trạng thái hai đặc trưng", không tính lại. Các phần bổ sung ngoài nguồn (thuật toán Q-learning, ví dụ hai trạng thái Bellman chiếu, ví dụ phân kỳ $w\to2w$, ví dụ hai mục tiêu trên mẫu thứ hai, số liệu notebook ở L07-04) được duyệt, ghi sai khác trong storyboard và review-log. Tên trạng thái chuỗi đổi sang chữ đứng; giữ ký hiệu $u(a)$ (không đổi sang $\sigma$).
