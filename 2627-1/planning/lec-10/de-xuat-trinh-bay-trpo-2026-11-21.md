# Đề xuất trình bày mạch TRPO của tác giả (2026-11-21)

Văn bản trích từ tệp `De_xuat_trinh_bay_TRPO.docx` tác giả gửi ngày 2026-11-21 (yêu cầu: "hãy tham khảo đề xuất trình bày mạch về TRPO này và chỉnh sửa"). Công thức trích từ OMML nên mất định dạng; ⟦…⟧ đánh dấu một công thức, [IMG rIdNN] đánh dấu một hình. Mười bốn hình gốc lưu ngoài repo; nội dung hình mô tả trong `gop-y-tac-gia-deck-2026-11-21.md`, mục #5.

Quyết định của tác giả (2026-11-21): sửa cả ghi chú §4 theo đề xuất; các trang ý tưởng chứng minh gom thành cụm "Cơ sở lý thuyết" ngay sau trang "Vì sao giới hạn KL kiểm soát sai số".

```text
Đề xuất đổi mới cách trình bày TRPO
Phần 4 · Hàm thay thế và miền tin cậy | Bài 10: TRPO và PPO
1. Đánh giá từ góc nhìn sinh viên
Bản ghi chú này đề xuất tổ chức lại phần 4 của bài giảng Reinforcement Learning & Planning. Mục đích là giúp sinh viên lần đầu học TRPO tự hình thành nhu cầu đối với từng công cụ toán học, đồng thời giữ được chiều sâu của bài giảng hiện tại.
Nhận xét chính. Nội dung hiện tại khá chặt chẽ về toán học, đặc biệt là ví dụ MDP hai trạng thái xuyên suốt. Tuy nhiên, trình tự từ bổ đề chênh lệch hiệu năng đến hàm thay thế, TV, KL, Pinsker, Fisher và thuật toán thuận lợi hơn cho người đã hiểu TRPO muốn kiểm tra cơ sở lý thuyết. Sinh viên lần đầu học phải theo dõi quá nhiều khái niệm trước khi nhìn thấy bài toán cần giải.
Nội dung
Câu hỏi sinh viên dễ mắc phải
Động cơ
Vì sao Policy Gradient chưa đủ, kể cả khi gradient chính xác?
Performance Difference Lemma (PDL)
Tại sao cần phân bố chiếm dụng trạng thái?
Hàm thay thế
Thay thế đại lượng nào, vì sao phải thay thế?
Tỉ số chính sách
Đã hiệu chỉnh mẫu bằng tỉ số, tại sao vẫn dự báo sai?
TV, KL, Pinsker
Vì sao tối ưu phần thưởng lại cần khoảng cách phân phối?
Fisher, gradient tự nhiên
Tại sao không đơn giản giảm learning rate?
Tách hai vấn đề: ước lượng gradient tốt (baseline, critic, GAE) và sử dụng gradient tốt (hướng và độ dài bước cập nhật). TRPO giải quyết chủ yếu vấn đề thứ hai.
 [IMG rId20]
Hình 1. Mạch tư duy đề xuất: mỗi câu hỏi dẫn đến một công cụ toán học.
Trình tự nên là: quan sát hiện tượng → đặt câu hỏi → hình thành trực giác → mô hình hóa → chứng minh → xây dựng thuật toán. Không giảm đáng kể lượng toán học, mà thay đổi thứ tự hình thành nhận thức.
2. Khởi đầu bằng thất bại của Policy Gradient
Thông điệp mở đầu: Biết hướng đi lên không có nghĩa là biết nên đi bao xa.
Policy Gradient cập nhật tham số theo quy tắc:
 ⟦θnew=θold+α∇θJθold.⟧
Ngay cả với gradient chính xác, tại điểm có gradient khác 0, ta chỉ biết rằng bước đủ nhỏ theo hướng gradient sẽ cải thiện mục tiêu. Bước quá nhỏ làm học chậm; bước quá lớn có thể phá hỏng chính sách đang hoạt động tốt.
 [IMG rId24]
Hình 2. Minh họa gradient chính xác nhưng bước cập nhật quá dài có thể làm giảm hiệu năng.
Câu hỏi cho lớp: Nếu đã thu thập 10.000 bước tương tác với môi trường, làm thế nào tận dụng bộ dữ liệu này để cập nhật đủ lớn nhưng không quá mạo hiểm?
Giữ nguyên ví dụ MDP hai trạng thái
 [IMG rId27]
Hình 3. MDP hai trạng thái, hệ số chiết khấu γ = 0,9; hành động a₁ tại sA dẫn đến sB.
Xác định chính sách bởi hai xác suất  ⟦pA,pB⟧  chọn hành động  ⟦a1⟧  ở mỗi trạng thái. Khi đó  ⟦JpA,pB=1−pA+2,7pApB⟧ .
Chính sách cũ  ⟦0,5;2/3⟧  cho  ⟦J=1,400⟧ ; ứng viên  ⟦0,9;0,5⟧  cho  ⟦J=1,315⟧ . Lưu ý ứng viên này minh họa sai số hàm thay thế, không phải bước theo gradient chính xác tại chính sách cũ.
3. Đổi chính sách cũng làm đổi dữ liệu
Trước khi đưa vào số lần thăm có chiết khấu, yêu cầu sinh viên tưởng tượng chạy 100 episode với mỗi chính sách. Hình dưới minh họa số episode kỳ vọng, làm tròn tới số nguyên.
 [IMG rId32]
Hình 4. Chính sách mới thay đổi cả xác suất chọn hành động và tần suất đến trạng thái sB; độ rộng đường thể hiện lượng episode tương đối.
Hai thay đổi cần phân biệt:
Action distribution: tại cùng trạng thái  ⟦sB⟧ , xác suất chọn  ⟦a1⟧  giảm từ  ⟦2/3⟧  xuống  ⟦1/2⟧ .
State distribution: chính sách mới đến  ⟦sB⟧  thường xuyên hơn, từ 50% lên 90% số episode.
Trong supervised learning, cập nhật tham số không làm đổi tập dữ liệu đã cho. Trong RL, chính sách mới còn làm đổi phân phối dữ liệu mà agent sẽ gặp trong tương lai.
Performance Difference Lemma
Gọi  ⟦ηπs=t≥0​γtPrπst=s⟧  là số lần thăm có chiết khấu (chưa chuẩn hóa). Mức cải thiện thực sự có thể viết chính xác:
 ⟦Jπ′−Jπ=s​ηπ′sa​π′a∣sAπs,a.⟧
 [IMG rId35]
Hình 5. Ba thành phần của chênh lệch hiệu năng: tần suất gặp trạng thái, quyết định mới và lợi thế theo chính sách cũ.
Điểm quan trọng: có thể đánh giá hành vi mới từ lợi thế của chính sách cũ, nhưng chưa biết phân bố  ⟦ηπ′⟧  khi chưa chạy chính sách mới (trong thiết lập model-free). Đây chính là động cơ của hàm thay thế.
4. Hàm thay thế: một phép xấp xỉ có chủ đích
4.1. Thay đúng một đại lượng
Mức cải thiện thực sự:
 ⟦ΔJ=s​ηπ′s⏟phân bố mớia​π′a∣sAπs,a.⟧
Mức cải thiện dự báo khi giữ nguyên tần suất trạng thái cũ:
 ⟦ΔL=s​ηπs⏟phân bố cũa​π′a∣sAπs,a.⟧
Chỉ thay  ⟦ηπ′→ηπ⟧ . Không thay lợi thế và cũng không giữ nguyên phân phối hành động. Định nghĩa hàm thay thế có hằng số gốc là  ⟦Lππ′=Jπ+ΔL⟧ .
Diễn giải cho sinh viên: Giả sử sau khi đổi chính sách, agent vẫn gặp các trạng thái với tần suất như trước. Trong những trạng thái quen thuộc ấy, hành vi mới có tốt hơn không?
4.2. Dùng lại các hành động đã lấy mẫu
Dữ liệu cũ chứa hành động từ  ⟦π⟧ , trong khi công thức cần hành động từ  ⟦π′⟧ . Với điều kiện hỗ trợ thích hợp, dùng importance sampling tại từng trạng thái:
 ⟦a​π′a∣sAπs,a=a​πa∣sπ′a∣sπa∣s⏟ρs,aAπs,a.⟧
Trong triển khai, ước lượng lợi thế bằng critic/GAE và tính mục tiêu trung bình thực nghiệm trên bộ đệm cố định  ⟦D⟧ :
 ⟦Lθ=1Nt=1Nπθat∣stπoldat∣stAt.⟧
Đây là dạng mục tiêu mẫu thường dùng; nếu lấy mẫu đúng phân bố chiếm dụng chuẩn hóa, nó tương ứng với  ⟦ΔL⟧  đến một hệ số dương. Cần phân biệt trọng số chiết khấu lý thuyết và trung bình mẫu trong thực hành.
Đã hiệu chỉnh
Chưa hiệu chỉnh
Phân phối hành động tại trạng thái đã gặp. Tỉ số xác suất cho phép tái sử dụng hành động cũ để tính kỳ vọng mới.
Phân phối trạng thái. Agent có thể đến trạng thái khác hoặc gặp trạng thái cũ với tần suất khác; tỉ số của một hành động không sửa được điều này.
Câu hỏi kiểm tra: Vì sao importance sampling theo từng hành động không biến hàm thay thế thành hiệu năng thực? Nếu sinh viên trả lời được, họ đã hiểu phần cốt lõi dẫn đến TRPO và PPO.
5. Sai số dự báo và nhu cầu về miền tin cậy
5.1. Khi dự báo cải thiện nhưng thực tế suy giảm
 [IMG rId43]
Hình 6. Đóng góp của từng trạng thái: tần suất đến sB tăng làm phần bất lợi lớn hơn dự báo.
Hàm thay thế dự báo tăng  ⟦0,095⟧  nhưng hiệu năng thực giảm  ⟦0,085⟧ , dù lợi thế được tính chính xác. Nguyên nhân là chính sách mới tăng tần suất đi đến nơi mà hành vi mới kém hơn. Đặt  ⟦Aπs,π′=a​π′a∣sAπs,a⟧ , ta có:
 ⟦ΔJ−ΔL=s​ηπ′s−ηπsAπs,π′.⟧
5.2. Thí nghiệm độ dài bước
Xét  ⟦pAt=0,5+0,4t⟧ ,  ⟦pBt=2/3−t/6⟧ , với  ⟦0≤t≤1⟧ . Khi đó  ⟦ΔL=0,095t⟧ , còn  ⟦ΔJ=0,095t−0,18t2⟧ .
 [IMG rId47]
Hình 7. Hàm thay thế tiếp xúc với hiệu năng thực tại t = 0; khi đi xa, sai số tăng. Vùng tím minh họa KL ≤ 0,01 theo quy ước trọng số của ví dụ.
Độ dài bước  ⟦t⟧
Dự báo  ⟦ΔL⟧
Thực tế  ⟦ΔJ⟧
Sai số tuyệt đối
0,00
0,00000
0,00000
0,00000
0,25
0,02375
0,01250
0,01125
0,50
0,04750
0,00250
0,04500
1,00
0,09500
−0,08500
0,18000
6. Từ mô hình cục bộ đến thước đo hành vi
Hàm thay thế có cùng giá trị và cùng gradient với hiệu năng thực tại chính sách cũ:
 ⟦Lπθπθ=Jθ,  ∇θ′Lπθπθ′θ′=θ=∇θJθ.⟧
Trong ví dụ, tín hiệu dự báo tăng bậc nhất còn sai số tăng bậc hai. Vì vậy, hãy giới thiệu miền tin cậy ở thời điểm này, trước các chứng minh TV và Pinsker: hàm thay thế là mô hình cục bộ, cần kiểm soát khoảng cách giữa chính sách cũ và mới.
6.1. Thay đổi tham số khác thay đổi hành vi
Xét  ⟦p=σθ⟧ : cùng một bước  ⟦Δθ=1⟧  có thể gây thay đổi xác suất rất khác nhau.
 [IMG rId52]
Hình 8. Hàm sigmoid: bước 0 → 1 làm p tăng 0,231; bước 5 → 6 chỉ làm p tăng khoảng 0,0042.
Do đó, ràng buộc Euclid  ⟦∥θnew−θold∥2≤ϵ⟧  không trực tiếp đo mức thay đổi hành vi. TRPO đo trong không gian phân phối hành động của chính sách.
6.2. KL divergence
 ⟦DKLπold⋅∣s‖πnew⋅∣s.⟧
 [IMG rId56]
Hình 9. So sánh KL của ba chính sách Bernoulli, lấy chính sách cũ p = 0,5 làm tham chiếu.
KL không phải khoảng cách đối xứng, nhưng rất hữu ích để đo sự thay đổi phân phối cục bộ.
7. Bài toán tối ưu trung tâm của TRPO
Sau khi sinh viên đã nhận ra lý do của hàm thay thế và thước đo thay đổi chính sách, đặt hai thành phần cạnh nhau:
 ⟦maxθ Es,a∼Dπθa∣sπolda∣sAs,a⟧
với ràng buộc
 ⟦Es∼DDKLπold⋅∣s‖πθ⋅∣s≤κ.⟧
Mục tiêu: tìm hành vi mới được dự báo có hiệu năng tốt nhất. Ràng buộc: không cho chính sách mới đi quá xa chính sách sinh ra dữ liệu. Đây là slide cần được sinh viên ghi nhớ ngay cả khi quên các chứng minh bên dưới.
Cơ sở lý thuyết: giới hạn KL có ích như thế nào?
 [IMG rId61]
Hình 10. Chuỗi lập luận: KL nhỏ → TV nhỏ → dịch chuyển phân bố chiếm dụng nhỏ → kiểm soát sai số.
Sử dụng Pinsker,  ⟦DTVp,q≤DKLp‖q/2⟧ , kết hợp chặn thay đổi phân bố trạng thái và chặn hiệu năng. Theo quy ước KL trung bình chuẩn hóa  ⟦DKL=Es∼dπDKLπ‖π′⟧ , với  ⟦dπ=1−γηπ⟧  và  ⟦χπ′=maxsAπs,π′⟧ , ta có một chặn dạng:
 ⟦ΔJ≥ΔL−2γχπ′1−γ2DKL2.⟧
Điều này diễn giải vì sao kiểm soát KL giúp kiểm soát sai số. Chỉ có đảm bảo cải thiện từ chặn nếu mức tăng dự báo lớn hơn số hạng sai số. TRPO thực nghiệm không tự động bảo đảm tăng đơn điệu chỉ vì thỏa ràng buộc KL trung bình mẫu. Cận lý thuyết có thể lỏng; thuật toán thực tế phải dùng các xấp xỉ, ước lượng và line search.
Gợi ý trình bày: đưa các chứng minh chi tiết của PDL, TV, dịch chuyển occupancy, Pinsker và bound vào cụm slide lý thuyết hoặc slide dọc trong Reveal.js; không để chúng cắt đứt mạch trực giác chính.
8. Gradient tự nhiên: giải thích bằng hình học
TRPO ưu tiên hướng tăng hàm mục tiêu mạnh nhưng ít làm thay đổi chính sách. Hãy so sánh hai miền ràng buộc của cùng mục tiêu tuyến tính  ⟦g⊤Δθ⟧ .
 [IMG rId66]
Hình 11. Miền Euclid là hình tròn; miền KL cục bộ là ellipse. Các đường đứt là đường đồng mức của mục tiêu tuyến tính.
Một số hướng tham số rất nhạy đối với KL, trong khi hướng khác ít nhạy. Hình ellipse mô tả đúng sự khác biệt ấy. Hướng gradient thường là hướng tối ưu trong hình tròn; gradient tự nhiên là hướng tối ưu theo hình học KL cục bộ.
8.1. Khai triển Taylor sau khi đã có trực giác
Đại lượng
Xấp xỉ cục bộ
Mức tăng hàm thay thế
 ⟦g⊤Δθ⟧  (bậc nhất)
KL divergence
 ⟦12Δθ⊤FΔθ⟧  (bậc hai)
Tại chính sách cũ, KL bằng 0 và gradient KL bằng 0. Hessian của KL tại điểm này là ma trận Fisher (theo phân bố trạng thái được dùng). Bài toán xấp xỉ:
 ⟦maxΔθ g⊤Δθ s.t. 12Δθ⊤FΔθ≤κ.⟧
Với  ⟦F⟧  xác định dương và  ⟦g≠0⟧ , dùng nhân tử Lagrange thu được:
 ⟦Δθ*=2κg⊤F−1g F−1g.⟧
Tách thành hai quyết định: đi hướng nào ( ⟦F−1g⟧ , gradient tự nhiên) và đi bao xa (hệ số căn bậc hai, đưa bước đến biên miền tin cậy xấp xỉ). Trong thực tế Fisher có thể suy biến nên thường dùng damping và phương pháp giải hệ gần đúng.
9. Ví dụ số và quy trình TRPO
9.1. Ý nghĩa của ma trận Fisher
Sử dụng dữ liệu ví dụ của bài giảng:
 ⟦g=0,20,3,  F=0,025000,01,  F−1g=830.⟧
 [IMG rId71]
Hình 12. So sánh thành phần hướng cập nhật, chuẩn hóa theo tổng độ lớn tuyệt đối (không phải độ dài bước thực tế).
Hỏi sinh viên: Tại sao TRPO ưu tiên thay đổi  ⟦θB⟧  nhiều hơn? Vì KL ít nhạy theo hướng đó (một phần do trạng thái  ⟦sB⟧  ít được thăm). Trong ví dụ, một bước cập nhật cho  ⟦J⟧  tăng từ 1,400 lên khoảng 1,807, tức khoảng 29%.
9.2. Một vòng lặp TRPO
 [IMG rId75]
Hình 13. Quy trình TRPO từ thu thập dữ liệu đến cập nhật actor; vòng lặp đỏ là backtracking line search.
Line search kiểm tra  ⟦Lθnew>Lθold⟧  và KL thực nghiệm không vượt  ⟦κ⟧  (có thể kèm tiêu chí tỷ lệ cải thiện). Nó không đo trực tiếp  ⟦J⟧  vì chưa chạy chính sách mới. Nếu mọi bước thử đều không đạt, giữ nguyên actor. Fisher-vector product và conjugate gradient giúp tránh tạo ma trận Fisher đầy đủ; cần giữ phân phối cũ, không chỉ log-prob hành động đã lấy mẫu, để tính KL.
10. Đề xuất cấu trúc 20 slide chính
Tổ chức phần 4 của Bài 10 thành năm cụm. Mỗi slide có một câu hỏi hoặc thông điệp duy nhất; dùng animation để từng thành phần xuất hiện đúng lúc.
Slide
Tiêu đề đề xuất
Hình thức
A
Động cơ của TRPO

1
Biết hướng đi lên nhưng chưa biết đi bao xa
Đồ thị mục tiêu (H. 2)
2
Đánh giá chính sách trước khi thực thi
Bộ đệm và các ứng viên
3
Đổi chính sách cũng làm đổi dữ liệu
MDP và luồng (H. 3–4)
B
Xây dựng hàm thay thế

4
Hiệu năng thay đổi vì những yếu tố nào?
Ba thành phần (H. 5)
5
Performance Difference Lemma
Công thức và chứng minh ngắn
6
Đại lượng chúng ta chưa biết
Tô màu occupancy mới
7
Giữ nguyên phân bố trạng thái cũ
Xây dựng surrogate
8
Hiệu chỉnh phân phối hành động
Importance sampling
9
Hàm thay thế đã sửa gì, chưa sửa gì?
Bảng so sánh hai phân bố
C
Từ hàm thay thế đến miền tin cậy

10
Khi dự báo tốt nhưng thực tế xấu
Đóng góp từng trạng thái (H. 6)
11
Khi nào hàm thay thế đáng tin?
Đồ thị tương tác (H. 7)
12
Thay đổi tham số khác thay đổi hành vi
Sigmoid (H. 8)
13
Đo sự thay đổi chính sách bằng KL
Thanh xác suất (H. 9)
14
Bài toán tối ưu miền tin cậy
Mục tiêu và ràng buộc
15
Vì sao giới hạn KL kiểm soát sai số?
Chuỗi lập luận (H. 10)
D
Giải bài toán TRPO

16
Xấp xỉ mục tiêu và ràng buộc
Taylor bậc một và hai
17
Hình học của miền tin cậy
Tròn và ellipse (H. 11)
18
Hướng đi và độ dài bước tối ưu
Gradient tự nhiên (H. 12)
E
Từ lý thuyết đến thuật toán

19
Một vòng lặp TRPO
Sơ đồ thuật toán (H. 13)
20
TRPO giải quyết gì và còn khó khăn gì?
Tổng kết, chuyển sang PPO
11. Tổng kết và thứ tự ưu tiên chỉnh sửa
Ba ý sinh viên cần nhớ sau phần TRPO:
 [IMG rId81]
Hình 14. Ba trực giác cốt lõi: dự báo cục bộ, giới hạn thay đổi và hướng tối ưu theo hình học KL.
Surrogate
Trust region
Natural gradient
Dùng dữ liệu cũ để dự báo hiệu năng của chính sách mới.
Chỉ tối ưu trong phạm vi mà dự báo còn tương đối đáng tin.
Tìm bước cập nhật tốt nhất theo hình học của chính sách.
Thứ tự ưu tiên chỉnh sửa
Mức độ
Thay đổi đề xuất
Rất cao
Phân biệt rõ action distribution và state distribution bằng hình luồng.
Rất cao
Đưa trực giác surrogate và trust region lên trước các chứng minh dài.
Cao
Dùng biểu đồ đóng góp, đồ thị độ dài bước và các câu hỏi tương tác thay cho bảng số dày đặc.
Cao
Giải thích không gian tham số khác không gian chính sách trước KL.
Cao
Dẫn xuất gradient tự nhiên từ bài toán hình học, sau đó mới chứng minh bằng Taylor và Lagrange.
Thông điệp xuyên suốt: TRPO không đơn thuần là Policy Gradient với bước cập nhật nhỏ. TRPO xây dựng một mô hình dự báo hiệu năng từ dữ liệu hiện có, giới hạn miền mà mô hình còn tương đối đáng tin, rồi tìm bước cập nhật tốt nhất trong miền đó.
Đến đây sinh viên có thể tự thấy nhược điểm: phải giải hệ Fisher, conjugate gradient, kiểm tra KL và line search. PPO xuất hiện tự nhiên như một nỗ lực đơn giản hóa cơ chế cập nhật để sử dụng các phương pháp tối ưu bậc nhất hiệu quả hơn; không nên xem clipping của PPO là ràng buộc KL cứng.
Tài liệu đối chiếu
Bài 10: TRPO và PPO, Reinforcement Learning & Planning, phần 4 – Hàm thay thế và miền tin cậy. Bài giảng trực tuyến.
Schulman, J. và cộng sự (2015). Trust Region Policy Optimization. Proceedings of ICML, PMLR 37, 1889–1897. Bài báo.
Schulman, J. và cộng sự (2017). Proximal Policy Optimization Algorithms. arXiv:1707.06347.
Các hình trong tài liệu được dựng lại từ nội dung và ví dụ của phần phân tích; đồ thị minh họa được tạo riêng cho mục đích giảng dạy. Hình 7 sử dụng quy ước trọng số chiết khấu của ví dụ:  ⟦0,1DKL,A+0,045DKL,B⟧ ; không đồng nhất với trung bình chuẩn hóa lại trên hai trạng thái chưa kết thúc.```
