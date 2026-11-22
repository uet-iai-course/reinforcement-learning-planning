# Nhận xét phần PPO, Bài 10 (tác giả gửi 2026-11-22)

Văn bản trích từ `Nhan_xet_phan_PPO_bai_10.docx` (yêu cầu: "Tiếp tục với mạch PPO"). ⟦…⟧ là công thức, [IMG rIdNN] là hình: rId23 chuỗi TRPO → vấn đề (Fisher, gradient liên hợp, tìm kiếm lùi tốn kém) → PPO-Clip (tối ưu bậc một với hàm mục tiêu cắt) → giám sát (approxKL, tỉ lệ cắt); rId27 hai đồ thị đóng góp của một mẫu theo ρ khi A>0 và A<0, CPI nét đứt cam, PPO-Clip tím; rId33 cột J: chính sách cũ 1,400, CPI không ràng buộc 1,000, PPO-Clip 1,392; rId37 hai đồ thị theo p_B: mục tiêu cắt phẳng −0,8, KL tại s_B tăng; rId41 vòng PPO: thu bộ đệm → đóng băng tham chiếu (log π_old, Â, mục tiêu giá trị) → K epoch, mỗi epoch tính lại ρ_t(θ) và mất mát → theo dõi approxKL, tỉ lệ cắt, thu bộ đệm mới; rId45 bốn tỉ số 1,05; 1,18; 1,24; 0,70 với dải [0,8; 1,2], tỉ lệ cắt 50%; rId52 điểm đánh giá.

```text
ĐÁNH GIÁ VÀ ĐỀ XUẤT CHỈNH SỬA PHẦN PPO
Bài 10 – Trust Region Policy Optimization và Proximal Policy Optimization | Góc nhìn sư phạm dành cho sinh viên
Nguồn đánh giá: Phần Tối ưu chính sách gần kề (PPO) trong bài giảng trực tuyến:https://courses.iaidev.com/reinforcement-learning-planning/2627-1/lecture-10-trpo-va-ppo.html
Phạm vi: Tập trung vào mạch diễn giải sau phần TRPO, trực giác về clipping, ví dụ MDP hai trạng thái, các giới hạn của PPO-Clip và quy trình triển khai thuật toán.
1. Kết luận tổng quan
Đánh giá chung: khoảng 8/10 về chất lượng sư phạm. Nội dung toán học tốt, ví dụ tính toán được xây dựng cẩn thận. Tuy nhiên, mạch giải thích clipping vẫn có thể trực quan hơn và chưa cân đối bằng phần TRPO đã được chỉnh sửa.
Ba điểm cần ưu tiên:
Trực giác clipping: cần để sinh viên tự nhận thấy vì sao phải ngừng thưởng cho thay đổi quá mức và vì sao công thức sử dụng phép min.
Thứ tự ví dụ: bộ đệm nhỏ có lợi thế ước lượng sai dấu là phản ví dụ tốt nhưng quá phức tạp cho lần giới thiệu đầu tiên.
Liên hệ thực hành: cần một sơ đồ thống nhất về thu thập dữ liệu, giữ cố định các đại lượng, lặp nhiều epoch và giám sát bằng approxKL/clip fraction.
1.1. Những điểm đã làm tốt
Nội dung
Đánh giá
Chuyển tiếp TRPO → PPO
Có động cơ rõ: tránh chi phí Fisher, Conjugate Gradient và line search.
Ví dụ MDP hai trạng thái
Duy trì tính liên tục với TRPO, cho phép so sánh các hàm mục tiêu trên cùng môi trường.
Công thức PPO-Clip
Đầy đủ; có đồ thị cho lợi thế dương và lợi thế âm.
Dạng theo dấu lợi thế
Là phần toán học quan trọng, được trình bày đúng trọng tâm.
Ví dụ lợi thế sai dấu
Cho thấy clipping không sửa được sai số của ước lượng lợi thế.
Giới hạn clipping
Chỉ rõ không phải ràng buộc KL; không bảo đảm hiệu năng tăng.
Bài tập tổng hợp
Kết nối surrogate, clipped objective và hiệu năng thực.
Điểm đặc biệt đáng giữ: phản ví dụ mà  ⟦J⟧  giảm từ  ⟦1,4⟧  xuống  ⟦1,392⟧  mặc dù dùng clipping. Ví dụ này giúp tránh ngộ nhận rằng PPO luôn cải thiện đơn điệu.
2. Thiết kế lại cách dẫn dắt clipping
Mạch hiện tại đi khá nhanh từ giới hạn TRPO, bộ đệm hai lượt có lợi thế sai, tối ưu CPI cực đoan sang định nghĩa clipped objective rồi mới phân tích trường hợp  ⟦A>0⟧  và  ⟦A<0⟧ . Sinh viên có thể nhớ công thức mà chưa tự hiểu được cách xây dựng.
Mạch đề xuất: (i) rủi ro tối ưu CPI quá lâu; (ii) một mẫu có lợi thế dương; (iii) một mẫu có lợi thế âm; (iv) ghép hai đồ thị gấp khúc; (v) viết công thức min tổng quát; (vi) quay lại bộ đệm sai dấu để thử độ bền của phương pháp.
 [IMG rId23]
Từ TRPO đến PPO: động cơ chuyển từ ràng buộc KL sang hàm mục tiêu cắt.
2.1. Hành động tốt có nên được tăng xác suất mãi?
Cho một mẫu có lợi thế  ⟦At=+2⟧ , với  ⟦ϵ=0,2⟧  và tỉ số chính sách
 ⟦ρtθ=πθat∣stπoldat∣st.⟧
Đóng góp của mẫu vào mục tiêu CPI là  ⟦ℓtCPI=2ρt⟧ . Nếu tiếp tục tăng  ⟦ρt⟧ , CPI tiếp tục tăng, kể cả khi chính sách mới đã khác xa chính sách cũ. PPO-Clip ngừng thưởng thêm khi  ⟦ρt>1+ϵ=1,2⟧ :
 ⟦ℓtCLIP=2minρt,1,2.⟧
Thông điệp cần nói trước công thức: Có thể tăng xác suất của hành động được đánh giá là tốt, nhưng không nên tiếp tục thưởng cho việc tăng quá mạnh trên bộ dữ liệu cũ.
2.2. Hành động xấu có nên giảm xác suất về 0?
Với  ⟦At=−2⟧ , sinh viên sẽ thấy việc giảm xác suất hành động làm CPI bớt âm (tức tăng mục tiêu). Nhưng khi  ⟦ρt<1−ϵ=0,8⟧ , PPO không còn thưởng thêm cho việc giảm xác suất:
 ⟦ℓtCLIP=min−2ρt,−1,6.⟧
 [IMG rId27]
Hai đường PPO-Clip theo dấu của lợi thế: chỉ cắt phần cải thiện dự báo vượt ngưỡng, không cắt hướng làm kết quả kém đi.
Trường hợp
 ⟦ρ⟧
CPI
PPO-Clip
 ⟦A=+2⟧ , tăng xác suất quá nhiều
1,3
2,6
2,4
 ⟦A=+2⟧ , giảm xác suất
0,7
1,4
1,4
 ⟦A=−2⟧ , giảm xác suất quá nhiều
0,7
−1,4
−1,6
 ⟦A=−2⟧ , tăng xác suất
1,3
−2,6
−2,6
Quy tắc sinh viên cần tự rút ra: lợi thế dương thì ngừng thưởng khi  ⟦ρ>1+ϵ⟧ ; lợi thế âm thì ngừng thưởng khi  ⟦ρ<1−ϵ⟧ ; nếu thay đổi theo hướng bất lợi, vẫn giữ tín hiệu giảm mục tiêu.
2.3. Vì sao dùng min, không chỉ dùng clip?
Sau khi sinh viên có hai đường gấp khúc, mới giới thiệu:
 ⟦ℓtCLIPθ=min​ρtAt, clipρt,1−ϵ,1+ϵAt.⟧
Nếu chỉ dùng  ⟦clipρtAt⟧ , tín hiệu cải thiện có thể bị che ngay cả khi thay đổi chính sách đi theo hướng bất lợi. Lấy min chọn giá trị bảo thủ hơn so với CPI, chỉ loại bỏ phần thưởng dự báo của cập nhật quá mức theo hướng có lợi.
Câu hỏi gợi mở nên đặt ngay trên slide: “Tại sao phải lấy min chứ không trực tiếp tối ưu  ⟦clipρA⟧ ?” Đây là câu hỏi trung tâm của phần PPO-Clip.
3. Đổi vị trí ví dụ bộ đệm có lợi thế sai dấu
Ví dụ hai lượt hiện có sử dụng  ⟦AsA,1=−1,4⟧ , trong khi lợi thế chính xác lại là  ⟦AπsA,1=+0,4⟧ . Ví dụ này rất có giá trị nhưng buộc sinh viên xử lý đồng thời sai số ước lượng lợi thế, tối ưu CPI không ràng buộc và clipping.
Đề nghị: chuyển xuống ngay sau khi sinh viên đã hiểu công thức cắt, và sử dụng nó làm phản ví dụ với câu hỏi: PPO có thể ngăn cập nhật quá mức, nhưng có sửa được ước lượng lợi thế sai hay không?
 [IMG rId33]
So sánh hiệu năng của chính sách cũ, nghiệm CPI không ràng buộc và nghiệm tối ưu PPO-Clip trong ví dụ lý tưởng hóa.
Phương pháp
Chính sách ứng viên
 ⟦J⟧
So với chính sách cũ
Chính sách cũ
 ⟦pA,pB=0,5,2/3⟧
1,400
0
CPI không ràng buộc
 ⟦pA,pB→0,1⟧
1,000
−0,400
PPO-Clip
 ⟦pA,pB=0,4,11/15⟧
1,392
−0,008
Kết luận: clipping giảm mạnh mức suy giảm trong ví dụ này nhưng không tự sửa lợi thế sai dấu, cũng không bảo đảm  ⟦J⟧  tăng. Các số liệu trên mô tả nghiệm của bài toán tối ưu lý tưởng hóa trên bộ đệm nhỏ, không phải kết quả tất yếu của một số bước Adam hữu hạn.
Một lưu ý sư phạm: lợi thế ước lượng sai dấu không nhất thiết đến từ critic kém. Ngay với baseline chính xác, một rollout ngẫu nhiên vẫn có thể tạo ra ước lượng lợi thế có phương sai lớn.
4. Clipping không phải ràng buộc khoảng cách
Cần có một slide riêng với câu khẳng định:
“PPO không cắt chính sách mới; PPO cắt đóng góp của từng mẫu vào hàm mục tiêu.”
Điều kiện  ⟦clipρ,0,8,1,2⟧  trong biểu thức mục tiêu không suy ra ràng buộc  ⟦0,8≤ρ≤1,2⟧  đối với chính sách sau cập nhật. Tối ưu theo cùng tham số  ⟦θ⟧  trên nhiều mẫu, mini-batch và epoch vẫn có thể khiến một số tỷ số đi ra ngoài khoảng cắt.
Ví dụ tại trạng thái  ⟦sB⟧  rất đáng giữ:
 ⟦pB⟧  sau cập nhật
Mục tiêu cắt
KL tại  ⟦sB⟧
0,733
−0,8
0,011
0,850
−0,8
0,104
0,950
−0,8
0,396
 [IMG rId37]
Giá trị mục tiêu cắt giữ nguyên trên một đoạn, nhưng KL giữa chính sách cũ và mới vẫn có thể tăng.
Thông điệp: Hàm mục tiêu đã phẳng nhưng khoảng cách chính sách vẫn tăng. Vì vậy, theo dõi KL và có thể dừng sớm theo KL là biện pháp thực hành có ý nghĩa, nhưng không biến PPO-Clip thành TRPO.
Cũng nên sửa mọi diễn đạt dạng “một vài tỷ số  ⟦ρt⟧  gần 1 thì TV nhỏ” thành phát biểu chính xác hơn: sự gần nhau của phân phối chính sách cần được kiểm soát trên toàn bộ phân phối hành động thích hợp, không thể chỉ suy ra từ một vài tỷ số trên mẫu quan sát.
5. Thiếu một sơ đồ thống nhất về vòng huấn luyện PPO
Các slide thuật toán hiện liệt kê đủ ký hiệu  ⟦θ,w,ρ,A,Vtarg,K,M⟧  và các đại lượng giám sát. Tuy nhiên, nên có một sơ đồ giúp sinh viên phân biệt rõ thông tin giữ cố định với thông tin phải tính lại sau mỗi bước tối ưu.
 [IMG rId41]
Một vòng PPO: thu dữ liệu, đóng băng tham chiếu, nhiều epoch trên cùng bộ đệm, giám sát và thu bộ đệm mới.
Giữ cố định trong một vòng cập nhật: tập dữ liệu  ⟦D⟧ , log-probability  ⟦logπoldat|st⟧ , lợi thế ước lượng  ⟦At⟧  và value targets  ⟦Vttarg⟧ .
Tính lại trong quá trình cập nhật actor/critic:  ⟦logπθat|st⟧ , tỷ số  ⟦ρtθ⟧ , các thành phần loss hiện hành và gradient. Một số triển khai còn có thể ước lượng lại các chỉ số giám sát sau từng epoch.
Đây là điểm sinh viên dễ nhầm với off-policy learning tổng quát. PPO tái sử dụng dữ liệu chính sách vừa thu trong một số epoch hữu hạn, rồi thu bộ đệm mới; không đơn thuần giữ bộ đệm lịch sử vô hạn.
6. Bổ sung hai slide thực hành
6.1. Slide “Đọc các chỉ số khi huấn luyện PPO”
Chỉ số
Ý nghĩa
Tín hiệu cần chú ý
approxKL
Ước lượng mức thay đổi chính sách
Cao so với ngưỡng mục tiêu; có thể dừng sớm
clip fraction
Tỷ lệ mẫu có tỷ số nằm ngoài khoảng cắt
Lớn kéo dài: nhiều mẫu bị ảnh hưởng bởi clipping
entropy
Mức ngẫu nhiên trong chính sách
Giảm quá nhanh: nguy cơ khám phá bị thu hẹp
Cho bộ tỷ số  ⟦ρ=1,05;1,18;1,24;0,70⟧ , với  ⟦ϵ=0,2⟧ . Hai trong bốn mẫu nằm ngoài khoảng  ⟦0,8,1,2⟧ , do đó:
 ⟦clip fraction=24=50%.⟧
Dùng ước lượng KL tương ứng:
 ⟦DKL=1Nt​ρt−1−logρt≈0,0243.⟧
 [IMG rId45]
Minh họa một mini-batch với hai tỷ số ngoài khoảng cắt.
Lưu ý về độ chính xác: tính không chệch của một ước lượng KL cho chính sách mới cố định không thể mặc nhiên suy ra khi cùng các mẫu được dùng để tối ưu tham số rồi tiếp tục đo KL trên chính bộ dữ liệu huấn luyện đó.
6.2. Slide “Hàm mất mát tổng của PPO”
Đề nghị tách riêng công thức hiện đang nằm trong phần diễn giải thuật toán:
 ⟦Ltotal=−LCLIP+c1LV−c2H.⟧
Thành phần
Vai trò trong học
Actor loss  ⟦−LCLIP⟧
Cải thiện hiệu năng dự báo nhưng không thưởng cho cập nhật quá mức theo hướng có lợi.
Value loss  ⟦LV⟧
Huấn luyện critic dự đoán giá trị trạng thái / value target.
Entropy bonus  ⟦H⟧
Khuyến khích mức ngẫu nhiên nhất định trong hành động, hỗ trợ khám phá.
Có thể nhắc biến thể PPO-Penalty sử dụng số hạng phạt KL trong một slide mở rộng, nhưng không nên ngắt mạch PPO-Clip chính.
7. Đề xuất bố cục PPO mới: 13 slide chính
Slide
Tiêu đề
Minh họa / mục tiêu
1
TRPO hiệu quả nhưng đắt
So sánh một vòng TRPO và PPO
2
Nếu tối ưu CPI quá lâu, chuyện gì xảy ra?
CPI và chính sách cực đoan
3
Hành động tốt có nên tăng xác suất mãi?
Đồ thị  ⟦A>0⟧
4
Hành động xấu có nên giảm xác suất về 0?
Đồ thị  ⟦A<0⟧
5
Xây dựng clipped objective
Hai đường gấp khúc → công thức min
6
Clipping theo dấu lợi thế
Bảng bốn trường hợp
7
PPO bảo vệ được gì, không bảo vệ được gì?
Hai phản ví dụ: KL và lợi thế sai
8
Quay lại bộ đệm hai lượt
CPI so với PPO trên cùng dữ liệu
9
Sử dụng lại bộ đệm qua nhiều epoch
Sơ đồ vòng lặp PPO
10
Hàm mất mát tổng PPO
Actor, critic, entropy
11
Đọc chỉ số huấn luyện
approxKL, clip fraction, entropy
12
Thuật toán PPO-Clip
Pseudocode + vòng thu dữ liệu
13
TRPO so với PPO
Tổng kết, ưu điểm và giới hạn
Bài tập MDP hai trạng thái sử dụng lợi thế chính xác nên đặt cuối phần học để sinh viên phân biệt ba đại lượng:
 ⟦LCLIP=0,200,  ΔL=0,260,  ΔJ=0,296.⟧
Các chứng minh dài, dạng theo từng dấu lợi thế và các biến thể PPO có thể để ở slide dọc/phụ, giúp mạch chính không bị ngắt quãng.
8. Tổng kết ưu tiên chỉnh sửa
 [IMG rId52]
Điểm đánh giá chủ quan theo các tiêu chí sư phạm.
Ưu tiên 1 – Cao nhất: đưa hai trường hợp  ⟦A>0⟧  và  ⟦A<0⟧  lên trước định nghĩa hàm mục tiêu, để sinh viên tự xây dựng công thức min.
Ưu tiên 2: chuyển ví dụ bộ đệm có lợi thế ước lượng sai dấu thành phản ví dụ về giới hạn PPO, thay vì ví dụ nhập môn.
Ưu tiên 3: bổ sung sơ đồ đầy đủ một vòng PPO nhiều epoch, chỉ rõ các đại lượng giữ cố định và tính lại.
Ưu tiên 4: thêm slide về loss tổng và log huấn luyện: approxKL, clip fraction, entropy.
Thông điệp kết thúc nên giữ thống nhất: TRPO kiểm soát thay đổi chính sách bằng ràng buộc KL và bước tối ưu dựa trên hình học bậc hai xấp xỉ. PPO-Clip thay cơ chế này bằng một hàm mục tiêu bảo thủ hơn, có thể tối ưu bằng phương pháp bậc nhất trên nhiều mini-batch. Clipping không bảo đảm KL luôn nhỏ, không bảo đảm hiệu năng tăng; nó chủ yếu giảm động lực cập nhật quá mức theo hướng được đánh giá là có lợi.

Ghi chú biên tập: Tài liệu được biên soạn từ phần nhận xét sư phạm về các slide PPO của bài giảng; hình và sơ đồ được dựng lại để minh họa các đề xuất. Các điểm số đánh giá mang tính chuyên môn chủ quan, không phải kết quả khảo sát sinh viên.
```
