# Bài NN — Tên bài

Tối đa một đoạn ngắn, hoặc bỏ hẳn. Bài toán trung tâm được nêu ở đầu mục nội dung thứ nhất.

## Mục tiêu học tập

- Mục tiêu quan sát hoặc đánh giá được: tính, thực hiện một bước, phân biệt, giải thích điều kiện áp dụng.

## Kiến thức tiên quyết

Số hiệu `03.k` chỉ ghi chú Bài 03.

- **Tên nhóm kiến thức** (Định lý 03.2, Hệ quả 03.5). Phát biểu lại kết quả trong một đến hai câu đủ để dùng ngay.

## Bảng ký hiệu

| Ký hiệu | Ý nghĩa | Miền hoặc kiểu |
|---|---|---|
| $\mathcal S$ | tập trạng thái | hữu hạn |
| $\mathcal A$ | tập hành động | hữu hạn |
| $\pi(a\mid s)$ | chính sách | phân phối trên $\mathcal A$ với mỗi $s$ |
| $\gamma$ | hệ số chiết khấu | $[0,1)$ |
| $G_t$ | lợi tức từ thời điểm $t$ | biến ngẫu nhiên thực |
| $v_\pi(s)$ | giá trị trạng thái thật | $\mathbb R$ |
| $V(s)$ | bảng ước lượng của $v_\pi(s)$ | $\mathbb R$ |

Khoảng 20 dòng; chỉ ký hiệu dùng xuyên suốt chương, mỗi chữ giữ một nghĩa trong cả chương. Ký hiệu chỉ dùng trong một ví dụ hay chứng minh được giới thiệu tại chỗ. Sau bảng, một đoạn nêu quy ước đọc: chỉ số thời gian của phần thưởng ($R_{t+1}$ là phần thưởng của chuyển từ $t$ sang $t+1$), kỳ vọng lấy theo chính sách và động lực môi trường, số liệu sư phạm tự xây dựng. Khi ký hiệu khác giáo trình *Học máy thống kê* ($v_\pi$ so với $V^\pi$), nêu tương ứng một lần.

## Bản đồ chủ đề

### Tên chủ đề

- Nhóm: `cốt lõi` | `cầu nối` | `bổ sung` | `đọc thêm`.
- Vai trò trong mạch: bước tiến của chủ đề đối với bài toán trung tâm.
- Kết nối vào: kiến thức đầu vào.
- Kết nối ra: sản phẩm học tập dùng cho phần sau.
- Mục: `## 1.` (mạch tương ứng của bộ trang chiếu).
- Nguồn: trang hoặc trang chiếu nguồn.

## 1. Tên mục (một mạch của bộ trang chiếu)

Mở mục bằng bài toán cụ thể, có dữ kiện và số liệu khi được, mà công cụ hiện có chưa giải được, viết như câu hỏi mà người đọc cùng tác giả đặt ra ("Để trả lời câu hỏi này, chúng ta cần…"). Không mở mục bằng định nghĩa, công thức hay danh sách.

<!-- note-topic-id: lec-NN-topic-01 -->
### 1.1 Nhu cầu và trực giác

Nêu quyết định, giới hạn hoặc bài toán chưa giải được bằng công cụ trước, rồi mô tả bằng quan hệ trạng thái, hành động, phần thưởng, quỹ đạo hoặc giá trị điều khái niệm sắp định nghĩa nắm bắt. Mở bằng "Một cách trực quan" hoặc "Về mặt ý tưởng" và nói rõ đây chưa phải định nghĩa.

![Mô tả đủ nội dung toán học của hình.](img/lec-NN/ten-hinh.svg)

Đoạn đọc hình: cần nhìn điều gì trên hình và điều đó ứng với công thức hay kết quả nào.

::: example Ví dụ NN.1 (Ví dụ dẫn nhập tính bằng tay)
Dữ kiện đầy đủ ngay trong khối: môi trường, chính sách, giá trị khởi tạo, tham số. Tính từng bước, ghi kết quả trung gian, kết quả số và một dòng kiểm tra lại.
:::

### 1.2 Định nghĩa

::: definition Định nghĩa NN.1 (Tên khái niệm)
Ghi đủ miền, kiểu và chiều của mọi đối tượng, chỉ số thời gian, quy ước kỳ vọng, giả thiết và ký hiệu đưa vào.
:::

Diễn giải từng thành phần của định nghĩa bằng lời. Chỉ ra chỗ định nghĩa tổng quát bao hàm ví dụ dẫn nhập. Một phản ví dụ hoặc trường hợp giới hạn.

Móc nối khái niệm: khái niệm vừa định nghĩa là trường hợp đặc biệt, tổng quát hóa hay bổ sung của khái niệm nào đã có (dẫn số hiệu), và khác khái niệm dễ nhầm ở điểm nào (trạng thái với quan sát, $v$ với $q$, dự đoán với điều khiển, theo chính sách với khác chính sách).

### 1.3 Kết quả và chứng minh

Câu dẫn vào định lý: kết quả này cần định nghĩa và kết quả nào trước đó, và trả lời câu hỏi nào của mục.

::: theorem Định lý NN.2 (Tên gọi quen thuộc)
**Giả thiết.** …

**Kết luận.** …

**Điều kiện áp dụng.** …

**Phạm vi.** …
:::

::: proof Chứng minh Định lý NN.2
**Bước 1 (tên bước).** Câu đầu nêu điều bước này thiết lập; các câu sau là lập luận; câu cuối nêu căn cứ.

**Bước 2 (tên bước).** Chuỗi biến đổi nhiều hơn hai dấu đặt trong `aligned`, mỗi dấu một dòng, căn cứ ở cột phải. Kết thúc bằng $\square$.
:::

Diễn giải định lý: ý nghĩa, vai trò từng giả thiết, điều gì xảy ra khi bỏ một giả thiết.

Móc nối định lý: mạnh hơn, yếu hơn hay mở rộng kết quả nào đã có; đổi giả thiết nào và trả giá bằng gì.

**Trong thực hành.** Đối tượng của định lý ứng với gì khi cài đặt (bảng giá trị, bộ xấp xỉ, bộ nhớ phát lại, chính sách hành vi); giả thiết được bảo đảm hay vi phạm ra sao trong môi trường thật hoặc với xấp xỉ hàm; kết luận cho phép làm gì hoặc giải thích hiện tượng gì. Dẫn tới Tình huống NN.k ở cuối chương, bài thực hành hoặc bài khác của học phần.

### 1.4 Thuật toán

::: algorithm Thuật toán NN.3 (Tên thuật toán)
**Đầu vào.** … **Đầu ra.** … **Giả thiết.** … **Khởi tạo.** … **Tham số.** …

1. Bước đánh số; phân biệt đại lượng cũ, mới và được giữ cố định.
2. …

**Điều kiện dừng.** … **Chi phí mỗi bước.** …
:::

::: example Ví dụ NN.2 (Một lượt lặp tính bằng tay)
Giá trị khởi tạo, mẫu chuyển, mục tiêu cập nhật, sai lệch, giá trị mới. Kết quả phải trùng với ví dụ dẫn nhập và với giả mã.
:::

::: remark Nhận xét NN.4
Giới hạn áp dụng, nhầm lẫn thường gặp, điều kiện hội tụ và giả thiết quyết định; bảo đảm lý thuyết khác tiêu chuẩn dừng thực hành.
:::

::: exercise Bài tập NN.1
Một yêu cầu đo đúng mục tiêu của tiểu mục: thực hiện bước tiếp theo, tìm lỗi trong cập nhật, phân biệt hai khái niệm. Dữ kiện nêu lại đầy đủ trong khối.
:::

::: hint
Bước khởi đầu, không thay toàn bộ lời giải.
:::

::: solution
Lời giải đầy đủ, từng bước có căn cứ, và dòng kiểm tra lại.
:::

Kết mục bằng văn xuôi: đã thu được kết quả gì (dẫn số hiệu), còn thiếu gì hoặc giả thiết nào còn hạn chế, mục kế tiếp giải quyết thiếu hụt đó như thế nào. Không dùng nhãn "Kết mục" hay danh sách.

## 2. Tên mục tiếp theo

Nhắc lại thiếu hụt của mục trước bằng một câu, rồi nêu bài toán cụ thể của mục này.

…

## Tình huống áp dụng và ứng dụng

::: application Tình huống NN.1 (Tên bài toán Học tăng cường)
Bài toán và môi trường → mô hình hóa thành đối tượng của chương → xác minh giả thiết → áp dụng kết quả → diễn giải → giới hạn. Dẫn ngược số hiệu các định nghĩa, định lý và thuật toán được dùng; nêu bước nào ứng với giả thiết nào.
:::

::: application Tình huống NN.2 (Trường hợp giả thiết không thỏa)
Nêu giả thiết bị vi phạm (quan sát không Markov, chính sách thay đổi, xấp xỉ hàm, dữ liệu khác chính sách) và hậu quả quan sát được.
:::

Ứng dụng: mỗi mục một hoặc hai câu nêu khái niệm nào của chương được dùng ở đâu (bài thực hành, bài sau của học phần, thuật toán Học tăng cường sâu), dẫn tới bài hoặc nguồn tương ứng.

## Tóm tắt chương

Một đoạn văn 5–8 câu kể lại câu chuyện của chương, dẫn số hiệu ngay trong câu: câu hỏi xuất phát, các bước đã đi, kết quả đích, giới hạn còn lại và bài nào xử lý tiếp.

**Định nghĩa và kết quả theo mục.**

- Mục 1: … (Định nghĩa NN.1); … (Định lý NN.2).
- Mục 2: …

**Công thức cần nhớ.**

$$
V(S_t)\leftarrow V(S_t)+\alpha\big[R_{t+1}+\gamma V(S_{t+1})-V(S_t)\big].
$$

**Giả thiết hay bị bỏ quên.** …

## Bài tập củng cố

Ít nhất một bài cho mỗi mục tiêu học tập. Không lặp đề bài của `exercises.md`.

### Mức nhận biết

::: exercise Bài tập NN.k
…
:::

::: hint
…
:::

::: solution
…
:::

### Mức tính toán hoặc chứng minh

### Mức vận dụng

::: exercise Bài tập NN.k
…
:::

::: hint
…
:::

::: solution
…
:::

## Hướng dẫn đọc thêm và tài liệu tham khảo

- Tác giả, năm, tên tài liệu, chương hoặc mục, trang; nêu mục nào của chương dựa trên nguồn nào. Ghi trang hoặc trang chiếu của bản nguồn.
