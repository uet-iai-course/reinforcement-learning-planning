# Storyboard Bài 03

## Hành trình khái niệm

| Cụm | Vấn đề | Trực giác | Ví dụ | Hình thức | Ứng dụng | Kiểm tra | Đầu vào → sản phẩm | Phút |
|---|---|---|---|---|---|---|---|---:|
| Định hướng | không áp dụng: đặt phạm vi | P02 | không áp dụng | P02 | P02 | P01 | Bài 02 → ba lớp mô hình | 6 |
| Chuỗi Markov | A02 | A02–A03 | A02–A04 | A00–A01,A04 | A03–A04 | A05 | tính Markov → $P$, $\mu_{t+1}$ | 18 |
| MRP và phần thưởng tích lũy | B01 | B01–B02 | B01,B03 | B00,B02,B04 | B03–B04 | B04 | $P$ → $r,\gamma,G_t,v$ | 22 |
| Bellman MRP | C00 | C00–C01 | C00 | C01–C04 | C05 | C03,C06 | sao lưu số → Bellman → điều kiện giải | 30 |
| MDP và chính sách | D01 | D01–D03 | D01,D03,D06 | D00,D02,D04–D05,D07–D08 | D06–D08 | D08 | hành động + $\pi$ → $P^\pi,r^\pi,v_\pi,q_\pi$ | 28 |
| Racing Car | D09 | D09 | D09–D10 | D10 | D10 | D10 | sáu kết quả → hệ Bellman và điều kiện hữu hạn | 10 |
| Tổng hợp | D11 | D11,D13 | không áp dụng: tổng hợp | D11 | D13 | D12 | biết mô hình → quy hoạch động → phi mô hình | 6 |
| Bài tập | X03,X04,X07,X08 | gộp trong đề | gộp trong đề | X03,X04,X07,X08 | X03,X04,X07,X08 | X03,X04,X07,X08 | khái niệm → lời giải | ngoài tuyến |

Tổng tuyến chính: $6+18+22+30+28+10+6=120$ phút.

Phân bổ phần bài tập 30 phút: X03 12 phút, X04 10 phút, X08 8 phút; X07 tự luyện.

## Ánh xạ lecture note ↔ deck

Ánh xạ nhiều–nhiều giữa topic trong `materials/lec-03/lecture-note.md` và `data-slide-id` trong deck:

| Topic lecture note | Slide deck |
|---|---|
| `lec-03-topic-01` Chuỗi Markov | A02, A00, A01, A03, A04, A05, X03 |
| `lec-03-topic-02` MRP | B01, B00 |
| `lec-03-topic-03` $G_t$ sang kỳ vọng | B02, B03 |
| `lec-03-topic-04` Giá trị trạng thái | B04 |
| `lec-03-topic-05` Bellman MRP | C00, C01, C02 |
| `lec-03-topic-06` Dạng ma trận/giải hệ/$\gamma=1$ | C03, C04, C05, C06, X03 |
| `lec-03-topic-07` MDP và hạt nhân chung | D01, D00, D09, D10 |
| `lec-03-topic-08` Chính sách | D02 |
| `lec-03-topic-09` MRP cảm sinh | D03, D04, X04 |
| `lec-03-topic-10` $v_\pi$ | D05 |
| `lec-03-topic-11` $q_\pi$ | D05, D06, X07 |
| `lec-03-topic-12` Bellman kỳ vọng | D07, D08, X08 |
| `lec-03-topic-13` Tổng kết | D11, D12, D13 |

Ghi chú: bảng ánh xạ trực tiếp 36/39 `data-slide-id`. P00, P01 tạo khung phạm vi và mục tiêu cho cả 13 topic; P02 nối `lec-03-topic-01`, `lec-03-topic-02`, `lec-03-topic-07`, `lec-03-topic-13`. Ba trang P00–P02 được ánh xạ ở mức khung toàn bài; deck gồm 35 trang chính và 4 trang dọc.

## Cấu trúc section ngoài

HTML dùng đúng 7 `<section>` ngoài, khớp 7 mạch của bảng hành trình khái niệm:

1. Định hướng: P00–P02.
2. Chuỗi Markov: A02, A00, A01, A03, A04, A05.
3. MRP và phần thưởng tích lũy: B01, B00, B02, B03, B04.
4. Bellman MRP: C00–C06.
5. MDP và chính sách: D01, D00, D02–D08.
6. Racing Car: D09, D10.
7. Tổng hợp: D11, D12, D13; nhánh bài tập X03, X04, X07, X08 nằm trong section cuối.

## Truyền dữ kiện và câu nối

- A02 cho ví dụ đồ thị trước; A00–A01 mới hình thức hóa chuỗi Markov, phát biểu tính Markov và điều kiện của $P$. A02 chỉ nói đồ thị và ma trận dùng cùng thứ tự; thưởng và giá trị chưa xuất hiện. A02–A05 giữ thứ tự Student MRP là C1, C2, C3, Pass, Pub, Facebook, Sleep.
- B01 cho véc-tơ thưởng trước; B00 mới đóng gói thành MRP. B00–B04 dùng cùng quy ước $R_{t+1}=r(S_t)$. B02 nêu ý chiết khấu ưu tiên thưởng sớm và điều kiện hữu hạn khi $\gamma<1$ dưới thưởng bị chặn; hình minh họa suy giảm mũ ở trang 37 nguồn được bỏ vì công thức và ba trường hợp gamma đã phủ đủ nội dung.
- C00 dùng các giá trị tiếp tục tạm thời để tạo một phép nhìn trước một bước Student, chưa dùng nghiệm. C01 phân rã $G_t$; C02 mới định nghĩa Bellman; C05 mới đưa hai nghiệm. Mặt trang làm tròn cả hai véc-tơ đến ba chữ số thập phân; notes giữ số đầy đủ và nghiệm phân số chính xác.
- C03 nối phương trình theo trạng thái với $v=r+\gamma Pv$. C04 tách $\gamma<1$ khỏi $\gamma=1$; C06 kiểm lại điều kiện trước khi giải.
- D01 nêu vấn đề: MRP đánh giá động lực cố định nhưng không biểu diễn lựa chọn hành động; hình Student MDP cho trực giác trước D00. D03 tạo một hàng $P^\pi$ và $r^\pi$ trước công thức D04.
- D04 nối trở lại MRP bằng $v_\pi=r^\pi+\gamma P^\pi v_\pi$. D05 nêu quan hệ $v_\pi=\sum_a\pi q_\pi$; D06 kiểm bằng số trước Bellman $q_\pi$ ở D08. D06 dùng dữ kiện nguồn trang 54: chính sách đều trên các hành động khả dụng tại mỗi trạng thái, $\gamma=1$; bước giải hệ đầy đủ được lược để tập trung quan hệ $v_\pi$–$q_\pi$, nhưng dữ kiện truy nguyên và kiểm được bằng phương trình Bellman tại C1 trong notes.
- D09 mở mạch ứng dụng mới với quy ước nhìn thấy được: vào Overheated nhận $-10$, không cộng thêm $+2$. D10 yêu cầu người học tự lập hệ trước khi hiện nghiệm và đối chiếu điều kiện $\gamma=1$; notes D10 nhắc lại quy ước thưởng, giải thích $1{,}5=0{,}5\times1+0{,}5\times2$, $-4{,}5=0{,}5\times1+0{,}5\times(-10)$ và nêu phản ví dụ chính sách chọn Slow ở cả Cool và Warm nhận $+1$ mãi mãi nên phân kỳ khi $\gamma=1$.
- X07 và X08 là yêu cầu sinh viên tự suy diễn trước khi đối chiếu D05 hoặc D07; không thêm nhãn phân tuyến lên mặt slide hoặc notes.
- D11–D13 nối rõ: bài này biết mô hình, Bài 04 dùng quy hoạch động, các bài sau học phi mô hình.

## Bản đồ 35 trang tuyến chính

| Mã | Luận điểm trung tâm | Câu nối sang trang sau |
|---|---|---|
| P00 | Phạm vi là đánh giá mô hình Markov. | “Đầu ra cần đạt được đo bằng ví dụ.” |
| P01 | Năm mục tiêu có thể kiểm tra. | “Đặt chúng trên ba lớp mô hình.” |
| P02 | Mỗi lớp giữ cấu phần trước rồi bổ sung phần thưởng hoặc hành động. | “Bắt đầu từ động lực không có thưởng.” |
| A02 | Đồ thị Student tạo trực giác về trạng thái và xác suất chuyển. | “Đóng gói đồ thị thành một mô hình.” |
| A00 | Chuỗi Markov hữu hạn được xác định bởi $\mathcal S,P$; tính Markov tóm tắt quá khứ bằng trạng thái hiện tại. | “Ma trận phải là các phân phối.” |
| A01 | Mỗi hàng hợp lệ; Sleep là trạng thái hấp thụ. | “Một lần chạy chỉ cho một quỹ đạo.” |
| A03 | Quỹ đạo mẫu không phải động lực. | “Đóng gói toàn bộ động lực vào ma trận.” |
| A04 | Đồ thị và ma trận dùng cùng thứ tự. | “Dùng ma trận để đẩy phân phối.” |
| A05 | Quy ước véc-tơ cột cho phân phối. | “Thêm phần thưởng vào động lực.” |
| B01 | Véc-tơ thưởng Student tạo ví dụ trước định nghĩa. | “Đóng gói động lực và thưởng thành MRP.” |
| B00 | MRP thêm thưởng và chiết khấu, không có hành động. | “Tổng các thưởng dọc theo quỹ đạo.” |
| B02 | $G_t$ là tổng chiết khấu và cần điều kiện hữu hạn. | “Tính hai quỹ đạo cụ thể.” |
| B03 | Hai quỹ đạo có hai phần thưởng tích lũy. | “Giá trị phải lấy trung bình trên các quỹ đạo.” |
| B04 | Giá trị là kỳ vọng của $G_t$. | “Ước lượng một bước cần thưởng và giá trị tiếp tục.” |
| C00 | Nhìn trước một bước Student tạo mẫu tính một bước. | “Mẫu này đến từ phân rã của $G_t$.” |
| C01 | Phân rã một bước chuẩn bị Bellman. | “Lấy kỳ vọng có điều kiện.” |
| C02 | Bellman MRP là thưởng cộng giá trị tiếp tục trung bình. | “Viết đồng thời cho mọi trạng thái.” |
| C03 | Dạng véc-tơ tạo hệ tuyến tính. | “Khả năng giải phụ thuộc $\gamma$ và trạng thái kết thúc.” |
| C04 | Hai chế độ giải có điều kiện khác nhau. | “Áp điều kiện đúng cho Student.” |
| C05 | Hai nghiệm Student xuất hiện sau phương trình. | “Giải trực tiếp không mở rộng tốt.” |
| C06 | Giới hạn tính toán và kiểm tra $\gamma=1$. | “Thêm hành động vào mô hình.” |
| D01 | Student MDP tạo trực giác về hành động và phản hồi; MRP không biểu diễn lựa chọn. | “Đóng gói các nhánh thành hạt nhân chung.” |
| D00 | Hạt nhân chung biểu diễn chuyển và thưởng theo hành động. | “Cần quy tắc chọn hành động.” |
| D02 | Chính sách Markov dừng là phân phối theo trạng thái. | “Cố định chính sách tại một trạng thái.” |
| D03 | Một hàng MRP cảm sinh được tính bằng lấy trung bình hành động. | “Khái quát cho mọi trạng thái.” |
| D04 | $P^\pi,r^\pi$ đưa MDP về Bellman MRP. | “Có hai cách điều kiện hóa giá trị.” |
| D05 | $v_\pi$ là trung bình $q_\pi$ theo chính sách. | “Kiểm quan hệ bằng số Student.” |
| D06 | Dữ kiện nguồn trang 54 cho phép tính $q_\pi$ và khôi phục $v_\pi(\text{C1})$. | “Viết Bellman cho giá trị trạng thái.” |
| D07 | Bellman $v_\pi$ lấy trung bình theo chính sách rồi môi trường. | “Cố định hành động đầu để viết $q_\pi$.” |
| D08 | Bellman $q_\pi$ giữ cố định $(s,a)$ ở vế trái. | “Áp dụng trên MDP có rủi ro kết thúc.” |
| D09 | Racing Car có đúng sáu kết quả chuyển tiếp; quy ước thưởng vào Overheated được nêu rõ. | “Từ sáu kết quả, lập hai phương trình.” |
| D10 | Người học áp dụng Bellman và kiểm tính hữu hạn. | “Khái quát lại ba lớp.” |
| D11 | Ba lớp trả lời ba câu hỏi khác nhau. | “Tự kiểm các cầu nối quan trọng.” |
| D12 | Tự kiểm phủ $v_\pi$, $q_\pi$, Bellman kỳ vọng, kiểm ma trận và MRP cảm sinh. | “Nối đánh giá với điều khiển.” |
| D13 | Bài 04 dùng quy hoạch động; các bài sau học phi mô hình. | “Nhấn xuống để chữa bài.” |

## Nhánh bài tập

| Mã | Sản phẩm học tập |
|---|---|
| X03 | Kiểm tra ma trận, trạng thái hấp thụ và lập hệ Bellman. |
| X04 | Chứng minh MDP cảm sinh MRP dưới chính sách cố định. |
| X07 | Suy ra $v_\pi(s)=\sum_a\pi(a\mid s)q_\pi(s,a)$; tự luyện. |
| X08 | Viết và giải thích Bellman kỳ vọng cho $v_\pi$. |

## Rà lại sau đổi thứ tự

- Đã rà P02–A03 sau khi chuyển A02 trước A00–A01: câu nối đi từ ba lớp → đồ thị → định nghĩa → điều kiện → quỹ đạo; không dùng ký hiệu chưa được giải thích trong phép tính.
- Đã rà A04–B03 sau khi chuyển B01 trước B00: thứ tự trạng thái đã được cố định ở A04; véc-tơ thưởng là ví dụ trực quan rồi mới định nghĩa MRP và $r(s)$.
- Đã rà C05–D03 sau khi chuyển D01 trước D00: C06 kết thúc MRP; D01 giới thiệu hành động bằng hình; D00 mới định nghĩa hạt nhân; D02 mới định nghĩa chính sách.
- Đã rà C00–C05 và hai trang lân cận B03–B04, C06–D00: không còn nghiệm hoặc Bellman trước định nghĩa giá trị và ví dụ nhìn trước một bước.
- Đã rà D01–D08 cùng C05–D00 và D09–D10: mỗi công thức có tiên quyết, ví dụ hoặc cầu nối MRP cảm sinh.
- Đã rà D08–D13: Racing Car không lặp kết luận; D10 là câu hỏi áp dụng; tự kiểm cuối phủ đủ ba đại lượng trọng tâm.
