# Sửa trang mục tiêu học tập, mạch 1, Bài 11 (2026-11-23)

Biên tập viên duy nhất của mạch 1.

**Căn cứ.** Quyết định của tác giả ngày 2026-11-23: "ở mạch 1, phần mục tiêu học tập cần có tính định tính thành các năng lực sau khi học bài, không cụ thể, định lượng". Quyết định này thay quyết định 2026-11-22 "viết mục tiêu thành câu hỏi hoặc sản phẩm tự kiểm được".

**Phạm vi.**
- Chỉ sửa L11-1-03 và L11-1-04: mặt trang và ghi chú diễn giả.
- Không sửa: các trang khác của mạch 1, mạch 2–6, phần đầu tệp.
- Không thêm lớp CSS. Không commit.
- Bản sao trước lượt: `deck-truoc-v9.html` trong scratchpad.

## 1. Văn bản mới (nguyên văn mặt trang)

**L11-1-03, "Mục tiêu học tập"**

Sau bài này, sinh viên có thể:

1. Phân biệt mô hình phân phối với mô hình mẫu, lập kế hoạch nền với lập kế hoạch tại thời điểm quyết định.
2. Ước lượng mô hình, tách độ ngẫu nhiên của môi trường khỏi sai số ước lượng.
3. Thực hiện Dyna-Q, nêu điều kiện Q-planning hội tụ, giải thích vì sao mô hình sai cần thưởng thăm dò.
4. So sánh cập nhật kỳ vọng với cập nhật mẫu khi ít phép tính.

**L11-1-04, "Mục tiêu học tập"** (danh sách đánh số tiếp từ 5)

5. Giải thích vì sao rollout cải thiện chính sách, chọn số mô phỏng, thực hiện tìm kiếm theo cây Monte Carlo.
6. Tối ưu kế hoạch bằng đạo hàm qua mô hình khả vi, giải thích vai trò của điều khiển dự báo theo chân trời lùi.
7. Xây dựng mô hình của tùy chọn và lập kế hoạch với tùy chọn.
8. Chọn cách dùng mô hình cho một bài toán và kiểm giả thiết mà cách đó cần.

**Ghi chú diễn giả.** Đã bỏ mọi số và phép tính kiểm.
- Trang đầu: bốn năng lực thuộc mạch 2. Hai năng lực đầu đặt nền cho cả bài, năng lực thứ ba là nội dung chính của mạch, năng lực thứ tư khép mạch. Nguồn: ghi chú bài giảng Bài 11, Mục tiêu học tập 1–3.
- Trang sau: rollout và tìm kiếm theo cây thuộc mạch 3, tối ưu kế hoạch bằng đạo hàm thuộc mạch 4, tùy chọn thuộc mạch 5. Năng lực cuối là việc của mạch tổng kết. Nguồn: ghi chú bài giảng Bài 11, Mục tiêu học tập 4–7.

## 2. Đối chiếu với bảy mục tiêu của ghi chú

| Mục tiêu ghi chú | Dòng trên trang | Phần giữ ở mức năng lực |
|---|---|---|
| 1. Mô hình và tính bất định | 1, 2 | phân biệt hai dạng mô hình và hai cách lập kế hoạch; ước lượng mô hình; tách bất định ngẫu nhiên (độ ngẫu nhiên của môi trường) khỏi bất định nhận thức (sai số ước lượng). Bỏ "tính độ lệch chuẩn" vì là phép tính cụ thể. |
| 2. Dyna | 3 | thực hiện Dyna-Q; điều kiện hội tụ của Q-planning; thưởng thăm dò khi mô hình sai |
| 3. Cập nhật kỳ vọng và cập nhật mẫu | 4 | so sánh khi ngân sách tính toán nhỏ ("khi ít phép tính") |
| 4. Rollout và tìm kiếm theo cây | 5 | tính chất cải thiện của rollout; chọn số mô phỏng; thực hiện MCTS. Chỉ số cận tin cậy trên là một phần của MCTS, không tách dòng. |
| 5. Tối ưu kế hoạch bằng đạo hàm | 6 | tối ưu qua mô hình khả vi; vai trò của điều khiển dự báo theo chân trời lùi. Không tách dòng riêng cho phương pháp entropy chéo vì không đủ âm tiết; xem mục 4. |
| 6. Tùy chọn | 7 | mô hình của tùy chọn; lập kế hoạch với tùy chọn. Phương trình bán-MDP, lặp giá trị và Q-learning với tùy chọn nằm trong "lập kế hoạch với tùy chọn". |
| 7. Chọn cách dùng mô hình | 8 | chọn cách dùng và kiểm giả thiết |

**Đối chiếu NT9.**
- Không có ký hiệu, con số, phép tính, câu hỏi hay fragment.
- Chỉ dùng tên phương pháp như ghi chú: Dyna-Q, Q-planning, rollout, tìm kiếm theo cây Monte Carlo, điều khiển dự báo theo chân trời lùi.
- Không có chữ viết tắt mới: bỏ RMSE, MCTS.

## 3. Hai trang hay một trang

- Bảy năng lực cùng dòng mở cần khoảng 100 âm tiết ở mức đủ nghĩa, vượt trần 80, nên giữ hai trang. Mã L11-1-04 vẫn dùng.
- Trang sau không lặp dòng "Sau bài này, sinh viên có thể:".
  - Danh sách đánh số tiếp từ 5 dưới cùng tiêu đề, đọc như phần tiếp của câu mở.
  - Thêm dòng mở thì trang sau lên 83 âm tiết, vượt trần.
- Vị trí giữ nguyên: hai trang mục tiêu vẫn ở cuối mạch 1, theo thứ tự 1-01, 1-06, 1-09, 1-07, 1-02, 1-05, 1-03, 1-04.
- Không trang nào khác nhắc tới trang mục tiêu hay "Mục tiêu k" trong ghi chú diễn giả. Không có liên kết `#/…` tới hai trang này.

## 4. Kiểm tra

- **`no-ai-slop` chế độ Edit** trên tám dòng:
  - Không có từ cấm, câu đệm, đối lập giả, câu kết kiểu châm ngôn.
  - Các dòng song song, mở bằng động từ, mỗi dòng một nhóm năng lực.
  - Không sửa thêm vì mọi thay đổi đều làm dài câu, vượt trần.
- **`deck_lint`:** L11-1-03 80 âm tiết, L11-1-04 77 âm tiết, cả hai ≤ 80. Không có cờ nào ở hai trang này, kể cả NOTES150. Toàn bài: 50 dòng, không có BANNED.
- **Các kiểm khác:**
  - `footer_check`: 0 trang chạm chân trang.
  - `formula_overflow`: `[]`.
  - Playwright 1600×900 và 390×844 trên hai trang: không có lỗi, không quá đáy hay mép phải. Đã xem ảnh rộng hai trang và ảnh hẹp của 1-03.
- **Phạm vi:**
  - Phần đầu tệp, các trang mạch 1 đứng trước 1-03 và mạch 2–6 trùng từng byte với `deck-truoc-v9.html`.
  - `git diff --check` sạch.

## 5. Âm tiết

| Trang | Trước | Sau | Trần |
|---|---|---|---|
| L11-1-03 | 108 | 80 | 80 |
| L11-1-04 | 88 | 77 | 80 |

## 6. Chỗ vướng

- Dòng 4 viết "khi ít phép tính" thay "khi ngân sách tính toán nhỏ" vì 1-03 đã đúng trần 80.
- Phương pháp entropy chéo của mục tiêu 5 không có dòng riêng; năng lực "tối ưu kế hoạch" bao cả hai cách tối ưu. Nếu tác giả muốn nêu tên, phải bỏ bớt chữ khác trên 1-04 (hiện 77).

## 7. Chỉnh nghĩa sau xét của điều phối viên (2026-11-23)

Căn cứ:
- NT11: khi phải chọn, giữ "đúng nghĩa" thắng trần âm tiết.
- NT17: trang mục tiêu được ngoại lệ đến 1,5 lần trần nếu ghi lý do.

Mức điều phối viên đặt cho lượt này: mỗi trang khoảng 90 âm tiết.

Bản sao trước lượt: `deck-truoc-v10.html`.

**Văn bản mới (nguyên văn):**
- 1-03, dòng 4: "So sánh cập nhật kỳ vọng với cập nhật mẫu khi ngân sách tính toán nhỏ." Đây là điều kiện của mục tiêu 3 trong ghi chú; thay "khi ít phép tính".
- 1-04: dòng 6 cũ tách thành hai dòng, để giữ đủ ba ý của mục tiêu 5:
  - 6. "Tối ưu kế hoạch qua mô hình khả vi bằng đạo hàm và phương pháp entropy chéo (cross-entropy method)."
  - 7. "Giải thích sai số dự báo tích lũy và vai trò của điều khiển dự báo theo chân trời lùi."
- "Entropy chéo" xuất hiện lần đầu trong deck ở trang này (trang mạch 4 đứng sau), nên kèm tên tiếng Anh trong ngoặc (VP2). Không thêm chữ viết tắt.
- Hai dòng cũ 7 và 8 thành 8 và 9. Dòng 9 bỏ "một": "Chọn cách dùng mô hình cho bài toán và kiểm giả thiết mà cách đó cần."
- Ghi chú diễn giả 1-04: "tối ưu kế hoạch và điều khiển dự báo theo chân trời lùi ứng với mạch 4".

**Âm tiết (deck_lint):**

| Trang | Trước lượt | Sau lượt | Trần | 1,5 lần trần |
|---|---|---|---|---|
| L11-1-03 | 80 | 82 | 80 | 120 |
| L11-1-04 | 77 | 90 | 80 | 120 |

**Ngoại lệ NT17 và lý do.** Cả hai trang vượt trần 80, vẫn dưới 1,5 lần trần. Lý do là giữ nghĩa NT11:
- 1-03 cần đúng điều kiện "ngân sách tính toán nhỏ" của ghi chú.
- 1-04 cần đủ ba ý của mục tiêu 5: tối ưu bằng đạo hàm, phương pháp entropy chéo, sai số dự báo tích lũy cùng điều khiển dự báo theo chân trời lùi.
- Ghi ngoại lệ này vào storyboard là việc của điều phối viên. Vai biên tập không ghi storyboard.

**Kiểm tra:**
- `deck_lint` chỉ còn cờ SYLL60 ở hai trang, đúng ngoại lệ nêu trên. Không có BANNED.
- `footer_check`: 0 trang chạm chân trang.
- `formula_overflow`: `[]`.
- Playwright 1600×900 và 390×844 trên hai trang: không có lỗi, không quá đáy hay mép phải. Đã xem ảnh rộng của 1-03 và 1-04, ảnh hẹp của 1-04.
- Mạch 2–6 và các trang đứng trước 1-03 trùng từng byte với `deck-truoc-v10.html`.
- `git diff --check` sạch.

Mục 6 cũ ("khi ít phép tính" và việc thiếu entropy chéo) đã được giải quyết bằng lượt này.

## 8. Chỉnh thứ tự từ ở 1-04 dòng 6 (2026-11-23)

Câu cũ đọc như cả hai cách tối ưu đều đi "qua mô hình khả vi", trong khi phương pháp entropy chéo không cần đạo hàm.

- Câu mới (nguyên văn): "Tối ưu kế hoạch bằng đạo hàm qua mô hình khả vi và bằng phương pháp entropy chéo (cross-entropy method)."
- `deck_lint`: L11-1-04 có 91 âm tiết, đúng giới hạn ≤ 91 điều phối viên đặt; vẫn là ngoại lệ NT17 ở mục 7.
- `footer_check`: 0 trang chạm chân trang. Không có BANNED.
- Playwright 1600×900 và 390×844 trên 1-04: không có lỗi hay tràn. Đã xem ảnh rộng.
- `git diff --check` sạch.

## 9. Sửa theo rà độ chính xác (2026-11-23)

**Nguồn.** `ra-soat-chinh-xac-muc-tieu-2026-11-23.md`: 1 phát hiện trung bình và 6 nhẹ, điều phối viên chấp nhận cả bảy.

**Quy tắc.** Vẫn theo NT-RL-13: viết định tính, thành năng lực, không số, không ký hiệu.

**Bản sao trước lượt.** `deck-truoc-v11.html`. Ba trang được sinh bằng script `obj.py` trong scratchpad.

### 9.1 Văn bản mới (nguyên văn)

**L11-1-03, "Mục tiêu học tập"**

Sau bài này, sinh viên có thể:

1. Phân biệt mô hình phân phối với mô hình mẫu, lập kế hoạch nền với lập kế hoạch tại thời điểm quyết định.
2. Ước lượng mô hình bằng tần suất từ dữ liệu.
3. Tách bất định ngẫu nhiên (aleatoric uncertainty) của môi trường khỏi bất định nhận thức (epistemic uncertainty) do thiếu dữ liệu.
4. Thực hiện Dyna-Q, nêu điều kiện Q-planning hội tụ, giải thích vì sao mô hình sai cần thưởng thăm dò.

**L11-1-04, "Mục tiêu học tập"**

5. So sánh cập nhật kỳ vọng với cập nhật mẫu theo số phép tính và sai số khi ngân sách tính toán nhỏ.
6. Phát biểu tính chất cải thiện của rollout cùng giả thiết của nó; chọn số mô phỏng theo xác suất chọn sai cho phép.
7. Giải thích quy tắc cận tin cậy trên và thực hiện tìm kiếm theo cây Monte Carlo.
8. Tối ưu kế hoạch bằng đạo hàm qua mô hình khả vi và bằng phương pháp entropy chéo (cross-entropy method).

**L11-1-10 (mã mới), "Mục tiêu học tập"**

9. Giải thích sai số dự báo tích lũy và vai trò của điều khiển dự báo theo chân trời lùi.
10. Định nghĩa tùy chọn và chính sách phân cấp; tính mô hình của tùy chọn; viết phương trình Bellman cho tùy chọn.
11. Lập kế hoạch và học giá trị với tùy chọn.
12. Chọn cách dùng mô hình cho bài toán và kiểm các giả thiết mà bảo đảm của cách đó cần.

### 9.2 Đối chiếu phát hiện

| Phát hiện | Sửa |
|---|---|
| trung bình, dòng rollout | "Phát biểu tính chất cải thiện của rollout cùng giả thiết của nó" (dòng 6). Ghi chú diễn giả nêu giả thiết là giá trị chính xác của chính sách cơ sở. |
| nhẹ, ước lượng mô hình và hai loại bất định | Dòng 2 dùng "bằng tần suất từ dữ liệu". Dòng 3 dùng đúng thuật ngữ của Định nghĩa 11.6, có tiếng Anh như ghi chú (VP2; lần đầu trong deck vì 2-04 đứng sau). |
| nhẹ, so sánh hai cách cập nhật | Dòng 5 thêm tiêu chí "theo số phép tính và sai số". Giữ "khi ngân sách tính toán nhỏ" theo chỉ thị điều phối viên; mốc "nhỏ hơn số trạng thái kế" ở ghi chú diễn giả 1-04, vì "hệ số phân nhánh" là thuật ngữ chưa giới thiệu (NT9). |
| nhẹ, "chọn số mô phỏng" và cận tin cậy trên | Dòng 6 thêm "theo xác suất chọn sai cho phép". Dòng 7 thêm "Giải thích quy tắc cận tin cậy trên". |
| nhẹ, tùy chọn | Dòng 10–11 thay "Xây dựng mô hình". Dòng 10: định nghĩa tùy chọn và chính sách phân cấp; tính mô hình của tùy chọn; viết phương trình Bellman cho tùy chọn. Dòng 11: lập kế hoạch và học giá trị với tùy chọn. Ghi chú diễn giả phân biệt lặp giá trị (lập kế hoạch) với Q-learning (học từ kinh nghiệm thật). |
| nhẹ, chữ "bảo đảm" | Dòng 12: "kiểm các giả thiết mà bảo đảm của cách đó cần". |
| nhẹ, ghi chú 1-03 "thuộc mạch 2" | Ghi chú mới: năng lực đầu dựng ở mạch 2 (hai dạng mô hình, lập kế hoạch nền) và mạch 3 (lập kế hoạch tại thời điểm quyết định); ba năng lực còn lại thuộc mạch 2. |

### 9.3 Ba trang và mã mới

- Mười hai dòng cần khoảng 237 âm tiết. Chia hai trang thì mỗi trang khoảng 118, vượt 100, nên chia ba trang.
- Mã mới L11-1-10 chưa từng dùng: đã kiểm `planning/lec-11/`, deck hiện tại và bản trước vòng 1; L11-1-08 đã dùng trước nên không gán lại.
- Thứ tự cuối mạch 1: 1-01, 1-06, 1-09, 1-07, 1-02, 1-05, 1-03, 1-04, 1-10. Deck có 66 trang (thêm một).
- Dòng mở chỉ ở trang đầu; hai trang sau đánh số tiếp (5–8, 9–12) dưới cùng tiêu đề.
- Liên kết: trang Nội dung dẫn bằng `#/N` theo chỉ số ngang của mạch, nên không đổi khi thêm trang dọc trong mạch 1. Không có liên kết `#/1/k` nào. Không ghi chú diễn giả nào của trang khác nhắc tới trang mục tiêu.
- Nguồn ghi chú diễn giả: 1-03 "Mục tiêu học tập 1–2"; 1-04 "Mục tiêu học tập 3–5"; 1-10 "Mục tiêu học tập 5–7".
- Việc phải ghi ở storyboard và outline (vai biên tập không ghi): mã L11-1-10 mới, cùng ngoại lệ âm tiết dưới đây.

### 9.4 Âm tiết (deck_lint) và ngoại lệ NT17

| Trang | Trước lượt | Sau lượt | Trần | Mức tối đa điều phối viên đặt |
|---|---|---|---|---|
| L11-1-03 | 82 | 81 | 80 | 100 |
| L11-1-04 | 91 | 84 | 80 | 100 |
| L11-1-10 | (mới) | 72 | 80 | 100 |

1-03 và 1-04 vượt trần 80 nhưng dưới 100 và dưới 1,5 lần trần. Lý do vẫn là giữ nghĩa NT11: phương pháp, tiêu chí và giả thiết mà bản rà yêu cầu giữ.

### 9.5 Kiểm tra

- `deck_lint`: chỉ còn cờ SYLL60 ở 1-03 (81) và 1-04 (84), đúng ngoại lệ nêu trên. 1-10 không có cờ. Không có BANNED.
- `footer_check`: 0 trang chạm chân trang.
- `formula_overflow`: `[]`.
- Playwright 1600×900 và 390×844 trên 1-03, 1-04, 1-10: không có lỗi, không quá đáy hay mép phải. Đã xem ảnh rộng của cả ba trang và ảnh hẹp của 1-04.
- Phần đầu tệp, các trang mạch 1 đứng trước 1-03 và mạch 2–6 trùng từng byte với `deck-truoc-v11.html`.
- `git diff --check` sạch.
