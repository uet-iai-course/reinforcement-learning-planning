# Rà độ chính xác hai trang mục tiêu học tập viết lại, Bài 11 (2026-11-23)

- **Vai:** người rà độ chính xác (chỉ đọc), sub-agent `general-purpose`, Opus 5.5.
- **Đối tượng:** L11-1-03, L11-1-04 (mặt trang và ghi chú diễn giả) theo `sua-muc-tieu-2026-11-23.md`, bản sau mục 8 (câu 1-04 dòng 6 đã đảo thứ tự từ).
- **Quy tắc:** NT-RL-13. Mục tiêu viết định tính, thành năng lực, không số. Ngoài ra, mục tiêu không được mất phương pháp, điều kiện hay đối tượng, và không được rộng hơn ghi chú.
- **Nguồn:** `materials/lec-11/lecture-note.md`, mục "Mục tiêu học tập" (dòng 7–13). Đối chiếu thêm Định nghĩa 11.6 (dòng 306–311), Mệnh đề 11.23 (dòng 687–692), Mệnh đề 11.24 và Ví dụ 11.14, §5 (Định nghĩa 11.40–11.42, Định lý 11.44, Thuật toán 11.47, 11.48, §5.4), Câu hỏi tự kiểm tra 3 (§6.3).

## 1. Phát hiện

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa |
|---|---|---|---|---|
| trung bình | L11-1-04, dòng 5 ("Giải thích vì sao rollout cải thiện chính sách…") | Câu nêu việc rollout cải thiện chính sách như một điều luôn đúng. Ghi chú có hai giới hạn mà câu này bỏ. Thứ nhất, kết luận là "không làm giảm" ($v_{\pi_{\mathrm{ro}}}\ge v_{\pi_0}$); bất đẳng thức chỉ nghiêm ngặt khi $\max_aq_{\pi_0}(s,a)>v_{\pi_0}(s)$. Thứ hai, kết luận chỉ đúng khi $q_{\pi_0}$ chính xác. Với trung bình của hữu hạn mô phỏng thì không có bảo đảm này; bài nhấn điều đó ở Câu hỏi tự kiểm tra 3. Mục tiêu 4 của ghi chú viết "phát biểu tính chất cải thiện… **cùng giả thiết**". Học phần cấm khẳng định tính chất mà không nêu giả thiết quyết định. | Dòng 10: "Phát biểu tính chất cải thiện của thuật toán rollout cùng giả thiết". Mệnh đề 11.23 (dòng 688–692): giả thiết "giá trị chính xác $q_{\pi_0}$"; Điều kiện áp dụng: "không phải trung bình của một số hữu hạn mô phỏng". §6.3, câu 3. | "Phát biểu tính chất cải thiện của rollout cùng giả thiết của nó, …", hoặc "Giải thích khi nào rollout không làm kém chính sách cơ sở, …". |
| nhẹ | L11-1-03, dòng 2 ("Ước lượng mô hình, tách độ ngẫu nhiên của môi trường khỏi sai số ước lượng.") | Dòng này lệch ghi chú ở hai điểm. (a) "Ước lượng mô hình" bỏ mất phương pháp "bằng tần suất từ dữ liệu", tức mô hình đếm. (b) "Sai số ước lượng" hẹp hơn bất định nhận thức. Định nghĩa 11.6 đo bất định nhận thức bằng độ phân tán của ước lượng, $\operatorname{Var}\hat p$, chứ không bằng sai số của một ước lượng cụ thể. Bất định nhận thức còn gồm "toàn bộ sự không biết" ở cặp chưa thử, nơi chưa có ước lượng nào. Vế "độ ngẫu nhiên của môi trường" khớp bất định ngẫu nhiên. Dòng này cũng không dùng hai thuật ngữ mà 2-04 sẽ định nghĩa. | Dòng 7: "ước lượng mô hình bằng tần suất từ dữ liệu, tách bất định ngẫu nhiên khỏi bất định nhận thức". Định nghĩa 11.6 (dòng 309–310). | "Ước lượng mô hình bằng tần suất từ dữ liệu; tách bất định ngẫu nhiên (độ ngẫu nhiên của môi trường) khỏi bất định nhận thức (độ phân tán của ước lượng do thiếu dữ liệu)." |
| nhẹ | L11-1-03, dòng 4 ("So sánh cập nhật kỳ vọng với cập nhật mẫu khi ngân sách tính toán nhỏ.") | Dòng này mất hai thứ so với ghi chú. Thứ nhất là tiêu chí so sánh, "theo số phép tính và sai số". Thứ hai là mốc của điều kiện, "nhỏ hơn hệ số phân nhánh". "Nhỏ" không có mốc thì không kiểm được. Ưu thế của cập nhật mẫu chỉ có khi ngân sách dưới $b$ lần đánh giá (Nhận xét 11.16: với $b=2$, cập nhật kỳ vọng có lợi). Ghi chú diễn giả đã có mốc này ("nhỏ hơn số trạng thái kế"), mặt trang thì chưa. | Dòng 9: "So sánh hai loại cập nhật theo số phép tính và sai số khi ngân sách tính toán nhỏ hơn hệ số phân nhánh." Nhận xét 11.16. | "…theo số phép tính và sai số, khi ngân sách tính toán nhỏ hơn hệ số phân nhánh." |
| nhẹ | L11-1-04, dòng 5 (cụm "chọn số mô phỏng") | "Chọn số mô phỏng" không nêu tiêu chí. Ghi chú viết "tính số mô phỏng đủ cho một xác suất chọn sai cho trước". Dòng cũng bỏ đối tượng "chỉ số cận tin cậy trên", tức quy tắc UCB của bài toán chọn lặp lại một bước, có Định nghĩa 11.25 và Định lý 11.26 riêng. Lý do biên tập viên nêu ("là một phần của MCTS") chỉ đúng cho chính sách cây UCT. | Dòng 10: "tính số mô phỏng đủ cho một xác suất chọn sai cho trước; tính chỉ số cận tin cậy trên". Tóm tắt chương, Mục 3 (dòng 1640). | "…chọn số mô phỏng theo xác suất chọn sai cho phép, dùng quy tắc cận tin cậy trên, thực hiện tìm kiếm theo cây Monte Carlo." |
| nhẹ | L11-1-04, dòng 8 ("Xây dựng mô hình của tùy chọn và lập kế hoạch với tùy chọn.") | Dòng này lệch mục tiêu 6 ở ba điểm. (a) "Xây dựng" rộng hơn "tính": ghi chú chỉ yêu cầu tính mô hình của một tùy chọn cho trước. Học mô hình tùy chọn từ dữ liệu là phần đọc thêm §5.4. (b) Dòng mất "định nghĩa tùy chọn và chính sách phân cấp" và "phương trình Bellman bán-MDP". (c) "Lập kế hoạch với tùy chọn" bao được lặp giá trị với tùy chọn (Thuật toán 11.47), nhưng không bao Q-learning bán-MDP (Thuật toán 11.48). Q-learning bán-MDP học từ kinh nghiệm thật, không phải lập kế hoạch trên mô hình. | Dòng 12: "Định nghĩa tùy chọn và chính sách phân cấp; tính mô hình của một tùy chọn; viết phương trình Bellman bán-MDP; thực hiện lặp giá trị và một cập nhật Q-learning với tùy chọn." Thuật toán 11.48 và đoạn sau (dòng 1521, 1545); §5.4 (dòng 1550). | "Định nghĩa tùy chọn, tính mô hình của tùy chọn, dùng phương trình Bellman bán-MDP để lập kế hoạch và học với tùy chọn." |
| nhẹ | L11-1-04, dòng 9 ("…kiểm giả thiết mà cách đó cần.") | Câu bỏ chữ "bảo đảm". Một cách dùng mô hình vẫn chạy được khi giả thiết hỏng: Dyna-Q chạy trên mê cung có trượt, rollout chạy với trung bình mô phỏng. Thứ cần giả thiết là **bảo đảm** của cách đó, như các Mệnh đề 11.4, 11.23, 11.24 và Định lý 11.29. Câu hiện tại đổi nghĩa thành điều kiện để thuật toán chạy được. | Dòng 13: "kiểm các giả thiết mà bảo đảm của cách đó cần". | "…kiểm giả thiết mà bảo đảm của cách đó cần." |
| nhẹ | L11-1-03, ghi chú diễn giả ("Bốn năng lực trên thuộc mạch 2") | Năng lực 1 có vế "lập kế hoạch nền với lập kế hoạch tại thời điểm quyết định". Khái niệm lập kế hoạch tại thời điểm quyết định được định nghĩa ở mạch 3 (Định nghĩa 11.21, §3.1), nên không thuộc trọn mạch 2. Câu tiếp theo, "hai năng lực đầu đặt nền cho cả bài", cũng không khớp với "thuộc mạch 2". | Định nghĩa 11.21 (dòng 617); Tóm tắt chương, Mục 3 (dòng 1640). | "Năng lực 2–4 thuộc mạch 2; năng lực 1 dựng ở mạch 2 (hai dạng mô hình, lập kế hoạch nền) và mạch 3 (lập kế hoạch tại thời điểm quyết định)." |

Tổng: 0 chặn bàn giao, 0 nghiêm trọng, 1 trung bình, 6 nhẹ.

## 2. Các dòng đạt

- **L11-1-03, dòng 1:** đủ cả hai cặp phân biệt của mục tiêu 1 (Định nghĩa 11.2, 11.9, 11.13, 11.21).
- **L11-1-03, dòng 3** ("Thực hiện Dyna-Q, nêu điều kiện Q-planning hội tụ, giải thích vì sao mô hình sai cần thưởng thăm dò"): đủ ba ý của mục tiêu 2. "Thực hiện Dyna-Q" ở mức năng lực bao "một bước thật gồm cập nhật trực tiếp, cập nhật mô hình và các cập nhật lập kế hoạch".
- **L11-1-04, dòng 6** ("Tối ưu kế hoạch bằng đạo hàm qua mô hình khả vi và bằng phương pháp entropy chéo (cross-entropy method)"): đúng. Sau lượt chỉnh mục 8, "qua mô hình khả vi" chỉ gắn với cách dùng đạo hàm, khớp Thuật toán 11.34: entropy chéo chỉ cần gọi mô hình. Truy hồi ngược là cách tính gradient, nằm trong "bằng đạo hàm", nên mức năng lực chấp nhận được.
- **L11-1-04, dòng 7** ("Giải thích sai số dự báo tích lũy và vai trò của điều khiển dự báo theo chân trời lùi"): khớp vế cuối của mục tiêu 5 (Mệnh đề 11.36, Định nghĩa 11.37). "Giải thích" thay "chặn" là đúng với quy tắc định tính.
- **Ghi chú diễn giả L11-1-04:**
  - Rollout và tìm kiếm theo cây ứng với mạch 3; tối ưu kế hoạch và điều khiển dự báo ứng với mạch 4; tùy chọn ứng với mạch 5; năng lực cuối ứng với mạch tổng kết. Cả bốn đúng theo Tóm tắt chương, mục theo mục, và §6.1.
  - Nguồn ghi "Mục tiêu học tập 4–7" là đúng.
- **Không có số trên mặt trang.** Không có ký hiệu hay viết tắt mới. Thuật ngữ "phương pháp entropy chéo" có kèm tiếng Anh ở lần đầu.

## 3. Ghi nhận

- Ba đề xuất ở các dòng 2, 4 và 8 làm tăng âm tiết. Trang đã ở mức ngoại lệ NT17: 82 và 91 âm tiết, so với 1,5 lần trần là 120, nên còn chỗ.
- Nếu phải chọn, phát hiện trung bình ở dòng 5 (giả thiết của tính chất cải thiện) và dòng 9 (chữ "bảo đảm") là hai chỗ làm sai nghĩa. Các phát hiện còn lại là mất đối tượng hoặc điều kiện.

## 4. Kiểm lại sau lượt sửa (mục 9 của `sua-muc-tieu-2026-11-23.md`)

Đối tượng là ba trang L11-1-03, L11-1-04 và L11-1-10 (mới), cả mặt trang lẫn ghi chú diễn giả, bản hiện tại của deck. Mỗi dòng được đối chiếu với các dòng 7–13 của ghi chú bài giảng.

### 4.1 Bảy phát hiện

| phát hiện | trạng thái | bằng chứng |
|---|---|---|
| trung bình, rollout cải thiện như luôn đúng | đã sửa đúng | Dòng 6: "Phát biểu tính chất cải thiện của rollout cùng giả thiết của nó". Ghi chú diễn giả 1-04 nêu giả thiết là "giá trị chính xác của chính sách cơ sở", khớp Mệnh đề 11.23 (dòng 688–692). |
| nhẹ, ước lượng mô hình và hai loại bất định | đã sửa đúng | Dòng 2: "bằng tần suất từ dữ liệu". Dòng 3 dùng đúng thuật ngữ của Định nghĩa 11.6. Cụm "do thiếu dữ liệu" khớp đoạn sau định nghĩa (dòng 313: "phần do thiếu dữ liệu"). |
| nhẹ, tiêu chí và mốc của so sánh hai cách cập nhật | đã sửa đúng | Dòng 5 có tiêu chí "theo số phép tính và sai số". Mốc "nhỏ hơn số trạng thái kế" nằm ở ghi chú diễn giả. Hệ số phân nhánh là số trạng thái kế có xác suất dương (Định nghĩa 11.14), nên mốc này đúng. Mặt trang chỉ ghi "nhỏ" theo chỉ thị của điều phối viên (NT9). |
| nhẹ, tiêu chí số mô phỏng và quy tắc cận tin cậy trên | đã sửa đúng | Dòng 6: "chọn số mô phỏng theo xác suất chọn sai cho phép". Dòng 7: "Giải thích quy tắc cận tin cậy trên…". |
| nhẹ, tùy chọn | đã sửa đúng | Dòng 10 có định nghĩa tùy chọn và chính sách phân cấp, mô hình của tùy chọn, phương trình Bellman. Dòng 11, "Lập kế hoạch và học giá trị với tùy chọn", bao cả Thuật toán 11.47 lẫn 11.48. Ghi chú diễn giả 1-10 phân biệt đúng hai cách: lặp giá trị là lập kế hoạch trên mô hình, Q-learning là học từ kinh nghiệm thật. |
| nhẹ, chữ "bảo đảm" | đã sửa đúng | Dòng 12: "kiểm các giả thiết mà bảo đảm của cách đó cần", đúng nguyên văn mục tiêu 7. |
| nhẹ, ghi chú 1-03 "thuộc mạch 2" | đã sửa đúng | Năng lực 1 nay dựng ở mạch 2 và mạch 3, nhờ Định nghĩa 11.21. Ba năng lực còn lại thuộc mạch 2. |

### 4.2 Dòng mới và ghi chú diễn giả

- Không dòng nào sai hoặc rộng hơn ghi chú.
- Dòng 10 viết "phương trình Bellman cho tùy chọn". Ghi chú gọi là phương trình Bellman bán-MDP, hay phương trình cho chính sách phân cấp (Định lý 11.44, (5.2)). Đây vẫn là cùng một đối tượng, nên không tính là phát hiện.
- Ghi chú diễn giả gán đúng mạch:
  - 1-04: so sánh hai cách cập nhật khép mạch 2 (§2.6); rollout, quy tắc cận tin cậy trên và tìm kiếm theo cây thuộc mạch 3; tối ưu kế hoạch thuộc mạch 4.
  - 1-10: sai số tích lũy và điều khiển dự báo khép mạch 4 (§4.4–4.5); tùy chọn thuộc mạch 5; năng lực cuối thuộc mạch tổng kết.
- Dòng nguồn khớp phần tương ứng của ghi chú:
  - 1-03 ứng với mục tiêu 1–2.
  - 1-04 ứng với mục tiêu 3–5 (dòng 5 là mục tiêu 3, dòng 6–7 là mục tiêu 4, dòng 8 là mục tiêu 5).
  - 1-10 ứng với mục tiêu 5–7 (dòng 9 là vế cuối của mục tiêu 5).
- Mặt trang không có số hay ký hiệu.

Tổng phát hiện của lượt kiểm lại: 0 chặn bàn giao, 0 nghiêm trọng, 0 trung bình, 0 nhẹ.
