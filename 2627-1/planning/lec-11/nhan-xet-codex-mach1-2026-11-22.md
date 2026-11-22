# Nhận xét của Codex: mạch 1 "Học tăng cường · Bài 11", Bài 11 (2026-11-22)

- Nguồn: `codex exec` (gói ChatGPT), model mặc định của cấu hình Codex, mức suy luận high; chạy bằng `tools/deck/codex_review.py`.
- Bản được nhận xét: `2627-1/lecture-11-lap-ke-hoach-dua-tren-mo-hinh.html` tại `9096f20` cộng thay đổi chưa commit; 7 trang (L11-1-01, L11-1-02, L11-1-03, L11-1-04, L11-1-05, L11-1-06, L11-1-07).
- Điểm: Mạch dẫn dắt 7,0; Trực quan hóa 6,5; Liên kết ví dụ–toán 7,0; Cân bằng trực giác–chứng minh 7,5; Từ lý thuyết đến thuật toán 6,5. Chưa đạt điều kiện dừng (mọi tiêu chí ≥ 9).
- Prompt:

```text
Xem phần "Học tăng cường · Bài 11" (mạch 1) của bài giảng https://courses.iaidev.com/reinforcement-learning-planning/2627-1/lecture-11-lap-ke-hoach-dua-tren-mo-hinh.html#/1

Hãy phân tích dưới góc nhìn của sinh viên để gợi ý cách trình bày tốt hơn, trực quan hơn.

---
Ảnh đính kèm là 7 trang của phần này, đúng thứ tự trình chiếu (L11-1-01, L11-1-02, L11-1-03, L11-1-04, L11-1-05, L11-1-06, L11-1-07), chụp từ bản hiện tại, có thể mới hơn trang web. Tệp `mach.md` trong thư mục làm việc chứa văn bản, công thức (TeX) và ghi chú giảng viên của từng trang. Đọc theo ảnh; dùng `mach.md` để đọc chính xác công thức.
Khi nêu vấn đề hoặc đề xuất, ghi mã trang (ví dụ L11-1-03). Viết báo cáo bằng tiếng Việt, định dạng Markdown; hình đề xuất thì mô tả bằng lời (thành phần, số liệu, chú thích).
Cuối báo cáo, chấm điểm phần này trên thang 10 theo năm tiêu chí, ghi đúng một bảng Markdown hai cột `Tiêu chí | Điểm`, mỗi tiêu chí một dòng, điểm là một số (ví dụ 8,5): Mạch dẫn dắt; Trực quan hóa; Liên kết ví dụ–toán; Cân bằng trực giác–chứng minh; Từ lý thuyết đến thuật toán.
```

---
# Góp ý mạch 1 · Học tăng cường, Bài 11

**Đề xuất chính: đưa mê cung hai phòng lên ngay sau trang mở đầu.** Từ góc nhìn sinh viên, câu hỏi dễ bám nhất là “Tại sao đã đi qua F mà sau khi nhận thưởng, tác tử vẫn chưa cập nhật được hành động đi từ F sang K?”. Bản hiện tại đưa câu hỏi này đến sau phần tiên quyết, hai trang mục tiêu và mục lục. Có thể trình chiếu theo thứ tự **L11-1-01 → L11-1-06 → L11-1-07 → L11-1-02 → L11-1-05**, rồi giới thiệu các mục tiêu ở **L11-1-03–04** khi đến nội dung tương ứng.

Báo cáo dựa trên bảy ảnh đính kèm theo thứ tự trình chiếu và đối chiếu công thức với ghi chú giảng viên. Trang web không tải được trong phiên này. [mach.md](/tmp/claude-1000/-data-tqlong-lectures/fd411c55-a86c-4518-a9f0-a6d4fde11419/scratchpad/lec11/codex-m1-v1/mach.md)

## Góp ý theo trang

### L11-1-01 · Mở đầu bằng một dự đoán

Câu in đậm nêu đúng lợi ích của mô hình, nhưng sinh viên chưa có ví dụ để hình dung “nhiều cập nhật” diễn ra thế nào. Có thể hiện một dải ba ô **F → K → Z**, đặt nhãn **+1 khi vào Z**, rồi hỏi “Sau khi đến Z lần đầu, giá trị của hành động đi sang phải từ F đã tăng chưa?”. Giữ câu trả lời đến L11-1-06 để sinh viên có lý do theo dõi từng bước cập nhật.

### L11-1-02 · Minh họa hai loại mô hình bằng cùng một đầu vào

Hai ký hiệu đang đứng cạnh nhau, nên sinh viên dễ đọc qua mà chưa thấy chúng cho phép làm gì. Đề xuất đặt ô **Đầu vào \((\mathrm K,\rightarrow)\)** bên trái, nối sang hai khung. Khung **Mô hình phân phối** liệt kê hai kết quả và xác suất, chẳng hạn \((\mathrm Z,+1)\) với \(0{,}8\) và \((\mathrm K,0)\) với \(0{,}2\) nếu mô hình khớp luật mê cung. Khung **Mô hình mẫu** hiện một kết quả của một lần gọi, chẳng hạn \((\mathrm K,0)\). Cạnh ô Z, ghi “Kết thúc, giá trị tiếp nối bằng 0” để chuẩn bị cho phép tính ở L11-1-06. Giữ giả thiết nền trên trang và nhắc lại điều kiện Robbins–Monro theo từng cặp khi phát biểu kết quả hội tụ.

### L11-1-03 · Biến mục tiêu thành bài kiểm tra ngắn

Mục tiêu đầu gộp nhiều phân biệt và phép tính trong một câu. Có thể chuyển ba nhóm mục tiêu thành ba câu sinh viên sẽ tự trả lời trong phần lập kế hoạch nền.

- Cùng giả sử xác suất đi đúng là \(0{,}8\), vì sao độ lệch chuẩn của xác suất ước lượng giảm từ \(0{,}1789\) xuống \(0{,}0566\) khi số quan sát tăng từ \(5\) lên \(50\), trong khi xác suất trượt của môi trường vẫn là \(0{,}2\)?
- Sau một bước thật của Dyna-Q, bảng \(Q\) và mô hình được cập nhật ở đâu? Thưởng thăm dò giúp kiểm tra lại cặp trạng thái–hành động nào?
- Nếu có \(100\) kết quả kế tiếp và ngân sách chỉ đủ xét \(10\) kết quả, cập nhật kỳ vọng đầy đủ cần bao nhiêu phép tính và cập nhật mẫu có sai số gì?

### L11-1-04 · Cho mỗi phương pháp một sản phẩm nhìn thấy được

Các mục tiêu 4–7 dồn nhiều thuật ngữ vào cùng một trang. Có thể giữ trên trang một việc cụ thể cho mỗi phương pháp: **đi hết một vòng tìm kiếm theo cây**, **tính một bước hạ gradient và kiểm tra chi phí giảm từ \(8\) xuống \(2{,}88\)**, **tính giá trị của một tùy chọn đi từ A đến F**. Đưa các yêu cầu chi tiết như tính UCT, chạy một vòng entropy chéo và viết phương trình Bellman phân cấp về đầu mục tương ứng. Giữ mục tiêu 7 làm câu hỏi tổng kết để sinh viên tập chọn phương pháp và kiểm tra giả thiết.

### L11-1-05 · Dùng mục lục để chỉ ra mô hình được gọi khi nào

Mục lục hiện giúp tra tên phần. Có thể thêm một sơ đồ bốn nhánh xuất phát từ ô **Mô hình học được**. Nhánh **Dyna** ghi “giữa các bước thật, cập nhật bảng \(Q\)”. Nhánh **Tìm kiếm cây** ghi “trước khi chọn, thử các nhánh từ trạng thái hiện tại”. Nhánh **Tối ưu kế hoạch** ghi “trước khi chọn, tối ưu một chuỗi hành động liên tục”. Nhánh **Tùy chọn** ghi “lập kế hoạch với hành động kéo dài nhiều bước”. Cho hai nhánh giữa cùng một nhãn **Tại thời điểm quyết định** để sinh viên thấy điểm chung trước khi gặp hai thuật toán khác nhau.

### L11-1-06 · Cho sinh viên thấy phần thưởng lan qua bảng \(Q\) thế nào

Mê cung là hình trực quan nhất của mạch. Các số \(v_*(s)\) trong ô xuất hiện cùng lúc với các giá trị \(Q(s,a)\) đang học, nên sinh viên có thể nhầm \(0{,}9756\) trong ô K với giá trị mới \(Q(\mathrm K,\rightarrow)=0{,}5\). Đề xuất hiện hình theo hai lượt bấm.

1. **Lượt đi thật.** Giữ tường B–C, cửa F–K và đích Z. Vẽ một vòng nhỏ tại A có nhãn “trượt, ở yên”, rồi tô đường A → B → F → K → Z. Dưới lưới, đặt năm mục tiêu cập nhật theo thứ tự \(0,0,0,0,1\). Khi tác tử vào Z, hiện phép tính \(Q(\mathrm K,\rightarrow)\gets 0+0{,}5[1+0{,}9\cdot0-0]=0{,}5\).
2. **Một cập nhật lập kế hoạch.** Vẽ nét đứt từ F sang K và chú thích “mô hình sinh lại chuyển tiếp F → K, thưởng 0”. Nếu cập nhật này được chọn ngay sau khi \(Q(\mathrm K,\rightarrow)\) lên \(0{,}5\) và \(Q(\mathrm F,\rightarrow)\) còn bằng 0, giá trị mới tại F là \(0{,}5(0+0{,}9\cdot0{,}5)=0{,}225\). Cả hai trường hợp đều đã dùng đúng năm bước thật. Có thể hiện các số \(v_*(s)\) sau đó dưới nhãn **Giá trị tối ưu của môi trường** khi cần dùng lại mê cung.

### L11-1-07 · Tách câu hỏi về hiệu quả và câu hỏi về độ đúng

Khung văn bản hiện chứa hai câu hỏi lớn. Đề xuất đặt chúng thành hai dòng, mỗi dòng gắn với một chi tiết của mê cung.

- **Cùng năm bước thật, mô hình giúp cập nhật được gì?** Đặt \(Q(\mathrm F,\rightarrow)=0\) của Q-learning cạnh \(0{,}225\) của cập nhật lập kế hoạch vừa minh họa. Chú thích rằng đây là chênh lệch ở một mục của bảng \(Q\). Câu hỏi tiếp theo là tác tử chọn hành động nào tại F và thu được bao nhiêu phần thưởng khi chạy trong mê cung thật.
- **Kết quả đúng trên mô hình áp dụng được đến đâu?** Sau lượt đầu, mô hình đếm chỉ thấy một lần đi phải từ F và đã đến K, nên ước lượng xác suất đến K là \(1\). Mê cung thật cho xác suất \(0{,}8\). Đặt hai số cạnh nhau, rồi hỏi Q-planning đang tiến đến \(q_*\) của môi trường hay \(\hat q_*\) của mô hình. Ví dụ này tạo lý do để sinh viên đọc kỹ phạm vi của từng bảo đảm khi gặp định lý.

## Chấm điểm bản hiện tại

| Tiêu chí | Điểm |
|---|---:|
| Mạch dẫn dắt | 7 |
| Trực quan hóa | 6,5 |
| Liên kết ví dụ–toán | 7 |
| Cân bằng trực giác–chứng minh | 7,5 |
| Từ lý thuyết đến thuật toán | 6,5 |
