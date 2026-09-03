# Nhật ký rà soát Bài 12

## Trạng thái bản nháp

- Nguồn đã kiểm kê: 54/54 trang chiếu, 76/76 media, 0 trang ẩn, 53 notes rỗng, không code demo; bản trích nguồn có 585 dòng theo `wc -l`.
- Bản hiện tại có 47 trang chính, gồm `L12-07B`, `L12-22B`, và ba bài tập `X01`–`X03` sau kết luận.
- Tài sản đích: 11 SVG; không có tham chiếu ảnh raster và không có ngoại lệ raster.
- Thời lượng thiết kế: 42 trang cốt lõi trong 110 phút; 5 trang linh hoạt không trùng lặp trong 10 phút; 30 phút chữa ba bài tập sau kết luận.
- Bốn báo cáo của vòng nháp trước được lưu dưới đây. Vòng bàn giao phải có đủ năm vai độc lập; kết quả vòng hiện tại được bổ sung sau khi các reviewer hoàn tất.

## Phân tích nguồn và quyết định ban đầu

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa và quyết định |
|---|---|---|---|---|
| chặn bàn giao | nguồn 4–6 → `L12-04`–`L12-07` | Nguồn trộn góc nhìn tác tử chung, MDP không dừng và policy tất định/ngẫu nhiên; thiếu quan sát/lịch sử. | $P$ nền có thể dừng; MDP cảm sinh đổi theo $\pi_{-i}$; $\pi:S\to A$ mâu thuẫn với $\pi(a\mid s)$. | Dùng $G=(\mathcal N,\mathcal S,\{\mathcal O_i\},\{\mathcal A_i\},P,\Omega,\{r_i\},\gamma)$; chuẩn hóa $P$, thêm kernel quan sát $\Omega$; actor dùng $\tau_i$. Đã áp dụng. |
| chặn bàn giao | nguồn 12 → `L12-13`–`L12-17` | Baseline COMA thiếu trọng số policy và actor domain không rõ. | Baseline phản thực phải lấy kỳ vọng dưới $\pi_i$ khi giữ $\mathbf a_{-i}$ cố định. | Viết đủ $b_i$, $A_i^{\mathrm{COMA}}$ và gradient theo $\tau_i$; thêm ví dụ số. Đã áp dụng. |
| chặn bàn giao | nguồn 13 → `L12-23` | Công thức gắn nhãn MADDPG nhưng dùng stochastic score gradient; target thiếu target actors và mask. | MADDPG dùng deterministic policy gradient qua centralized critic. | Thay bằng $D_{\theta_i}\mu_i^\top\nabla_{a_i}Q_i$ và target đủ mọi actor, $m$. Đã áp dụng. |
| chặn bàn giao | nguồn 14 → `L12-18`–`L12-22` | Nguồn gọi phép cộng là QMIX và viết argmax lỗi. | Phép cộng là VDN; QMIX dùng mixer đơn điệu, state-conditioned. | Tách VDN/QMIX, nêu IGM và giới hạn không biểu diễn mọi joint $Q$. Đã áp dụng. |
| chặn bàn giao | nguồn 17–18 → `L12-27`–`L12-28` | Nguồn nói tái ước lượng advantage sau mỗi agent, bỏ bước thì thành MAPPO và permutation “unbiased”. | HAPPO thực hành dùng một joint GAE và sequential multiplier; sequential update vẫn khác MAPPO. | Viết pipeline và tích tỷ số; thu hẹp mệnh đề về contour/order. Đã áp dụng. |
| chặn bàn giao | nguồn 47–51 → `L12-38`–`L12-41` | Nguồn đồng nhất CTDE với full communication; trộn topology và chu kỳ $T$. | CTDE là tổ chức thông tin training/execution; full là complete sender–receiver graph. | Tách CTDE, topology và communication policy. Đã áp dụng. |
| nghiêm trọng | nguồn 7 → `L12-08` | Nash viết sai lệch đơn phương; tối ưu chung bị trộn với cân bằng. | Điều kiện phải cố định $\pi_{-i}^*$ và phân phối đầu; quan hệ tối ưu chung → Nash cần common payoff. | Viết đúng bất đẳng thức, giới hạn quan hệ một chiều cho trò chơi hợp tác hoàn toàn. Đã áp dụng. |
| nghiêm trọng | nguồn 9 → `L12-09` | Zero-sum và general-sum reward viết sai kiểu. | Zero-sum là $\sum_i r_i=0$; mixed/general-sum là vector. | Sửa ba reward regimes; thêm constant-sum. Đã áp dụng. |
| nghiêm trọng | nguồn 15–16 → `L12-24`–`L12-26` | Ratio thiếu chỉ số agent; claim IPPO kém và MAPPO SOTA quá rộng. | Actor dùng local history; benchmark paper không tạo thứ hạng chung. | Viết ratio từng agent, centralized value; bỏ ranking/SOTA. Đã áp dụng. |
| nghiêm trọng | nguồn 34 → ghi chú `L12-33` | AutoGen bị xếp như MARL environment và “self-train LLM”. | AutoGen là framework agent conversation, không mặc nhiên cập nhật policy/LLM bằng RL. | Bỏ khỏi mặt trang, ghi ranh giới trong note. Đã áp dụng. |
| nghiêm trọng | nguồn 36–38 → ghi chú `L12-33` | OpenAI Five action gọi là continuous; win rate thiếu mẫu. | Action được factorize/rời rạc hóa; Arena 2019 có $7215/7257=99{,}421\%$. | Thu hẹp thành ca lịch sử trong notes; không dùng để xếp hạng. Đã áp dụng. |
| nghiêm trọng | nguồn 53–54 → `L12-43`–`L12-44` | Không nói message availability; privacy bị diễn đạt ngược. | Actor phụ thuộc message thì message phải có khi execution; privacy hạn chế suy diễn. | Hiện đường actor/critic và yêu cầu threat model. Đã áp dụng. |
| trung bình | nguồn 20–33 → `L12-30`–`L12-34` | Một số nhãn environment/reward và số tác tử bị trình bày như thuộc tính cố định. | LBF/RWARE có reward mode; số MAgent/Pogema là cấu hình nguồn. | Gắn scope theo cấu hình; bỏ SOTA và đường cong. Đã áp dụng. |
| trung bình | nguồn 35 → `L12-33` | “Cuộc thi 2023 đang bắt đầu” đã lỗi thời. | NeurIPS 2023 đã kết thúc. | Dùng mô tả lịch sử, không giữ trạng thái hiện tại. Đã áp dụng. |
| trung bình | nguồn 40–46 → `L12-35`–`L12-37` | Support matrix của framework thay đổi theo thời gian. | Repo/package có thể đổi sau paper. | Trình bày vai trò lịch sử; yêu cầu pin version/commit khi tái lập. Đã áp dụng. |

## Kiểm số và công thức

| mục | kết quả |
|---|---|
| joint action `L12-06` | $2\times3\times4=24$; $5^{10}=9.765.625$. |
| COMA `L12-15` | $0{,}25\times2+0{,}75\times6=5$; advantage action phải là $6-5=1$. |
| QMIX ví dụ `L12-20` | $2\times3+5+0{,}1\times3\times5=12{,}5$; đạo hàm dương trên miền ví dụ. |
| QMIX `L12-22B` | Utility online chọn từng $a_{t+1,i}^*$; target mixer/utility đánh giá; $m_t=1-d_t$ với $d_t$ chỉ terminal thật; gradient chỉ qua mạng online. |
| HAPPO `L12-28`, `X02` | Với $M_2=2{,}2$, $r_2=1{,}3$, $\epsilon=0{,}2$: hạng clipped $=2{,}64$; $r_2^{\mathrm{new}}=0{,}9$ cho $M_3=1{,}98$. |
| OpenAI Five lịch sử | $7215/7257=99{,}421\%$; chỉ dùng trong ghi chú có mốc sự kiện. |
| Công thức nguồn dưới dạng ảnh | Đã dựng lại bằng KaTeX; không giữ công thức raster. |

## Kiểm định storyboard và quyết định chỉnh sửa

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa và quyết định |
|---|---|---|---|---|
| nghiêm trọng | `L12-08` | Mệnh đề “tối ưu toàn cục suy ra Nash” thiếu giả thiết common payoff. | $J_i$ khác nhau trong general-sum nên “tối ưu chung” chưa có nghĩa nếu chưa nêu tiêu chuẩn xã hội. | Giới hạn mệnh đề cho trò chơi hợp tác hoàn toàn; ghi ranh giới general-sum trong notes. Đã sửa. |
| nghiêm trọng | outline, storyboard, `note-for-author.md` | 110 phút cốt lõi và 10 phút linh hoạt cùng trỏ vào một số trang, nên tổng thời lượng bị đếm chồng. | Bảng cũ ghi toàn bộ 45 trang trong tuyến cốt lõi nhưng lại gọi năm trang là linh hoạt. | Tách tuyến hiện tại thành 42 trang cốt lõi và 5 trang linh hoạt không giao nhau; ghi hai nhánh cắt `L12-34` → `L12-38` và `L12-42` → `L12-45`. Đã sửa. |
| nghiêm trọng | `L12-27`–`L12-28` | Thủ tục HAPPO xuất hiện trước khi nêu vấn đề mà cập nhật tuần tự giải quyết. | Chu trình học tập yêu cầu vấn đề và trực giác trước thuật toán/hình thức. | `L12-27` nay nêu joint policy lệch khỏi policy tạo rollout và trực giác hoán vị; `L12-28` mới đưa thủ tục, tích tỷ số và giới hạn contour. Đã sửa. |
| trung bình | `L12-17`, `L12-22` | Hai cụm COMA và QMIX chưa có kiểm tra ngay sau giới hạn. | Storyboard gán bước kiểm tra chủ yếu cho `X02`, cách phần khái niệm. | Thêm hộp **Câu hỏi:** về chi phí tổng baseline COMA và điều kiện đơn điệu QMIX; đáp án ở notes. Đã sửa. |
| trung bình | `L12-38`–`L12-41` | Phần giao tiếp còn trừu tượng và taxonomy trộn topology với policy gửi. | Hàng policy cũ chứa cả “cấu trúc kết nối”, trong khi `L12-40` dành riêng cho topology. | Mở bằng ví dụ robot kho; topology chỉ định cạnh hợp lệ, policy/gate quyết định có gửi và khi nào trên topology đó. Đã sửa. |
| trung bình | các bảng, nhất là `L12-35`, `L12-39` | Cỡ chữ bảng thực tế thấp hơn $0{,}75\,\mathrm{em}$ do nhân $0{,}86\times0{,}76$ hoặc $0{,}82$. | CSS cục bộ đặt toàn deck $0{,}86\,\mathrm{em}$ rồi giảm bảng thêm lần nữa. | Đặt bảng ở $0{,}88\,\mathrm{em}$, tương đương $0{,}7568\,\mathrm{em}$ theo cỡ gốc; rút nội dung bảng framework và giảm nhịp dòng. Đã sửa. |
| trung bình | `L12-37` | Tiêu đề phần framework nhưng không có câu kiểm tra framework cụ thể. | `X03` cũ chỉ hỏi benchmark và giao tiếp. | Thêm câu hỏi so hai kho cùng ghi QMIX nhưng khác wrapper/action mask; đáp án yêu cầu pin phiên bản/commit. Đã sửa. |
| nhẹ | `L12-13`–`L12-16`, `X02` | Cụm COMA mở bằng $Q=8$ nhưng ví dụ tính dùng action thực $Q=6$. | Hai con số không sai riêng lẻ nhưng làm người học tưởng là hai ví dụ. | Thống nhất action thực $Q=6$, baseline $5$, advantage $1$ xuyên suốt. Đã sửa. |

Sau vòng storyboard đầu, đã rà các vùng ảnh hưởng và hai trang lân cận mỗi phía: `L12-06`–`L12-10`, `L12-11`–`L12-24`, `L12-25`–`X02`, `L12-33`–`L12-44`, `X03` và `L12-45`. Vòng phản biện tiếp theo bổ sung `L12-07B`, `L12-22B` và tái cấu trúc các stack; phạm vi rà lại cuối được ghi trong mục “Quyết định hợp nhất sau bốn báo cáo”.

### Tái kiểm định storyboard

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa và quyết định |
|---|---|---|---|---|
| trung bình | `L12-27`–`L12-28`, `X02` | Trực giác tuần tự chuyển thẳng sang công thức mà chưa có phép thế số. | `X02` có các tỷ số $1{,}1$ và $0{,}9$ nhưng dữ kiện này chưa được chuẩn bị trước công thức. | Thêm tại `L12-27`: ratio actor đầu $1{,}1$ làm surrogate actor kế thành $1{,}1\widehat A$; giữ `X02` làm bài tổng hợp $1{,}1\times0{,}9\times2=1{,}98$. Đã sửa và rà `L12-25`–`X02`. |
| trung bình | `L12-38`–`L12-40` | Storyboard chưa ghi đúng vai trò sư phạm đã có trên mặt trang. | `L12-38` đã gồm vấn đề, ví dụ và trực giác; `L12-39` là taxonomy/hình thức; `L12-40` giải thích cơ chế topology và áp nó vào đường gửi–nhận. | Sửa trường `bước` tương ứng, không đổi nội dung hoặc thứ tự trang; rà `L12-36`–`L12-42`. Đã sửa. |

## Bốn báo cáo độc lập của vòng nháp trước

### Góc nhìn sinh viên

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa và quyết định |
|---|---|---|---|---|
| nghiêm trọng | toàn bộ điều hướng, `X01`–`X03` | Bài tập nằm giữa các cụm nội dung và kết luận, nên phím Phải/Xuống không tạo tuyến 110/120 phút rõ. | `X01`, `X02`, `X03` từng nằm trong ba stack kiến thức; `L12-42` còn nối tới bài tập trước kết luận. | Vòng trước chuyển bài tập ra sau kết luận; vòng hiện tại giữ thứ tự đó nhưng gộp vào mạch ngoài thứ 7 để toàn bài có 7 mạch. |
| nghiêm trọng | 11 SVG | Chữ từ `17px` đến `24px` không đọc được sau khi hình co theo chiều cao. | Kiểm kê `font-size` cho thấy mọi SVG trừ một nhãn đều dưới ngưỡng nguồn `28px`. | Vẽ lại cả 11 SVG với chữ có nghĩa từ `30px`, rút nhãn và nới chiều cao cục bộ ở ba hình cao. Đã sửa. |
| trung bình | `L12-07` | Tuple, kernel và lịch sử cùng nằm trên một trang nhưng miền của các ánh xạ chưa rõ. | Người học gặp $\Delta$, $\tau_i$ và kernel trước khi biết kiểu. | Giữ tuple ở `L12-07`, thêm `L12-07B` cho lịch sử và công thức cảm sinh; notes nêu tổng/tích phân. Đã sửa. |
| trung bình | `L12-26`, `L12-28` | Kiểm tra actor/critic và ratio chỉ xuất hiện ở bài tập cuối. | Khoảng cách giữa công thức và lần truy hồi đầu tiên làm tăng tải nhớ. | Thêm câu hỏi ngay tại hai trang, giữ `X02` làm tổng hợp. Đã sửa. |

### Chuyên gia Học tăng cường

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa và quyết định |
|---|---|---|---|---|
| chặn bàn giao | `L12-18`–`L12-22` | QMIX dừng ở kiến trúc, chưa thành thuật toán có replay, target, mask và loss. | Không có tuple chuyển tiếp, next-action selection, TD target hoặc đường backprop. | Thêm `L12-22B`: utility online chọn local greedy actions theo IGM, target mixer/utility đánh giá, $m_t=1-d_t$ với $d_t$ chỉ terminal thật, MSE cập nhật mạng online. Đã sửa. |
| nghiêm trọng | `L12-13`, `L12-18`, `L12-23`–`L12-24` | Phạm vi game của các họ thuật toán chưa hiện rõ. | COMA/VDN/QMIX dùng common return; MADDPG paper còn có mixed tasks; PPO/HAPPO trong bài đang dùng cooperative setting. | Ghi phạm vi trên mặt trang và notes; không suy rộng common-return objective sang general-sum. Đã sửa. |
| nghiêm trọng | `L12-12`, `L12-24`, `L12-35` | Parameter sharing chưa nối với agent ID và tác tử dị thể. | Chia sẻ tham số có thể ép vai trò khác nhau dùng cùng mapping nếu input không mang ID/role. | Sửa trục “đồng nhất”, nêu ID/role, tham số/đầu ra riêng và nối HAPPO/HARL. Đã sửa. |
| trung bình | `L12-23`–`L12-25` | $x$, mask, target parameters và chỉ số policy PPO chưa được định nghĩa đủ. | Công thức dùng $x$, $m$, $\bar\theta$, $\bar\phi$ và $\pi_\theta$ trước khi khóa nghĩa. | Định nghĩa $x$, $m=1-d$, dấu gạch target và $\pi_{\theta_i}$. Đã sửa. |

### Độ chính xác toán học và thuật toán

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa và quyết định |
|---|---|---|---|---|
| chặn bàn giao | `L12-28` | HAPPO chỉ có tích ratio cũ, thiếu objective clipped của tác tử hiện tại và recurrence sau cập nhật. | Không thể suy ra biến nào cố định trong current-agent optimization hoặc cách tạo multiplier kế. | Viết $L_m^{\mathrm{clip}}$ với $M_m$ cố định và $M_{m+1}=r_m^{\mathrm{new}}M_m$; cập nhật `X02`. Đã sửa. |
| nghiêm trọng | `L12-07` | Hợp đồng Markov thiếu miền/kiểu; phép tổng ngầm giả định rời rạc. | $P$, $\Omega$, $r_i$, $\pi_i$ và $\tau_i$ chưa có domain/codomain. | Thêm $\Delta(\cdot)$, miền ánh xạ, chuỗi lịch sử; công thức cảm sinh chỉ dưới quan sát đầy đủ/policy Markov, notes thay tổng bằng tích phân khi liên tục. Đã sửa. |
| nghiêm trọng | `L12-21` | Đẳng thức argmax sai kiểu khi có nhiều cực đại. | Mỗi argmax là một tập, không phải một thành phần vector duy nhất. | Dùng $\prod_i\arg\max Q_i\subseteq\arg\max Q_{\mathrm{tot}}$ và giải thích tie. Đã sửa. |
| nghiêm trọng | `L12-23`, `L12-25` | MADDPG và PPO còn ký hiệu mơ hồ. | Critic MADDPG riêng theo $i$ nhưng tiêu đề gọi “critic chung”; ratio dùng $\pi_\theta(A_{t,i})$ thiếu chỉ số tham số và trộn action với advantage. | Đổi thành critic tập trung riêng, dùng $Q_{i,\phi_i}$, $\pi_{\theta_i}(a_{t,i}\mid\tau_{t,i})$ và định nghĩa target. Đã sửa. |
| trung bình | `X01`, `X02` | Chưa kiểm trực tiếp lệch đơn phương Nash và clipped objective HAPPO. | Bài tập chỉ hỏi định nghĩa reward và tích ratio. | Thêm ca $5\to5{,}4$ để bác bỏ Nash; thêm phép tính $2{,}64$ và recurrence $1{,}98$. Đã sửa. |

### Phản biện học thuật và giảng dạy Học tăng cường–lập kế hoạch

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa và quyết định |
|---|---|---|---|---|
| nghiêm trọng | `L12-21`–`L12-23` | Trình tự đi từ điều kiện QMIX sang MADDPG mà không cho người học thấy một bước học QMIX. | Công thức IGM đúng riêng lẻ nhưng thiếu cầu nối từ cấu trúc hàm tới TD update. | Chèn `L12-22B` sau giới hạn biểu diễn, rồi mới chuyển sang actor–critic. Đã sửa. |
| nghiêm trọng | `L12-27`–`L12-28` | Ví dụ ratio chưa dẫn tới objective của tác tử hiện tại. | $1{,}1\widehat A$ chỉ giải thích multiplier, không giải thích clipping. | Giữ ví dụ ở `L12-27`, viết objective và recurrence tại `L12-28`, dùng `X02` để nối hai phép tính. Đã sửa. |
| nghiêm trọng | `L12-34`–`L12-45`, `X01`–`X03` | Trình tự trang không thực hiện đúng nhánh cắt đã mô tả trong planning. | Các trang linh hoạt và bài tập từng cùng nằm trong stack chính, nên không thể đi Phải để bỏ qua đúng chỗ. | Vòng trước dùng 10 stack; vòng hiện tại giữ hai nhánh cắt nhưng hợp nhất thành 7 mạch ngoài theo quy ước kho. |
| trung bình | `L12-05`, `L12-12` | “Dừng hơn” và “đồng nhất” quá tắt, dễ tạo trực giác sai. | Cụm từ không nêu tác nhân gây không dừng hoặc điều kiện chia sẻ tham số. | Viết lại siêu tác tử theo một bộ chọn joint action; tách compatibility, ID/role và dị thể. Đã sửa. |

## Quyết định hợp nhất vòng nháp trước

- Đã xử lý toàn bộ lỗi chặn bàn giao và nghiêm trọng; các lỗi trung bình liên quan trực tiếp tới công thức, tải nhận thức, kiểm tra tại chỗ, điều hướng và khả năng đọc cũng đã xử lý.
- Hai trang bổ sung giữ nguyên tổng 110 phút cốt lõi bằng cách phân bổ lại thời gian trong cụm hợp đồng Markov 25 phút và VDN/QMIX 15 phút; không lấy thời gian từ bài tập.
- Rà lại sau thay đổi số lượng/thứ tự bao phủ `L12-04`–`L12-10`, `L12-18`–`L12-28`, `L12-29`–`L12-45` và toàn bộ `X01`–`X03`, gồm ít nhất hai trang lân cận mỗi phía khi tồn tại.

### Kiểm tra của tác tử chỉnh sửa

- KaTeX strict sau hậu kiểm: 147 biểu thức hợp lệ, `throwOnError: true`, `strict: "error"`.
- Cấu trúc sau chỉnh sửa hiện tại: 50 mã trang duy nhất, 50 khối ghi chú, 7 mạch ngoài, độ sâu `<section>` tối đa bằng 2; thứ tự khớp bảng hash trong storyboard.
- SVG: 11/11 tệp là XML hợp lệ và có `role="img"`, `title`, `desc`; cỡ chữ nguồn nhỏ nhất bằng `30px`.
- Sửa hậu kiểm trực quan cục bộ: nới khối MARL cuối trong `path-to-marl.svg` để hai dòng tên thuật toán không vượt biên; tách nội dung khối kết hợp trong `message-integration.svg` thành ba dòng và dịch biểu diễn $h_i$ để không chồng chữ hoặc mũi tên.
- Tài sản: 21 tham chiếu cục bộ hợp lệ; không có ảnh raster hoặc phụ thuộc mạng.
- Cỡ chữ bảng hiệu dụng: $0{,}86\times0{,}88=0{,}7568\,\mathrm{em}$; bảng framework đã rút nội dung và dùng nhịp dòng $1{,}12$ để giảm nguy cơ tràn.
- Markdown chỉ dùng `$...$` và `$$...$$`; kiểm tra khoảng trắng bằng `git diff --no-index --check` sạch.
- Tự kiểm theo `no-ai-slop/eval.md`: không thêm kết quả thực nghiệm; các mệnh đề bổ sung đều là điều kiện, ví dụ tính hoặc ví dụ sư phạm có ghi nguồn/phạm vi; không có từ cấm và lời dẫn rỗng trong phần đã sửa.
- Không thể khởi động máy chủ bằng `python3 -m reloadserver 8765` trong môi trường tác tử chỉnh sửa vì Python báo thiếu mô-đun `reloadserver`.
- Môi trường tác tử chỉnh sửa không có Chromium, Chrome hoặc Firefox, nên kết luận về không tràn cần được xác nhận trong kiểm định trực quan cuối bằng Codex Slides hoặc trình duyệt của điều phối viên. Theo kích thước viewBox và `max-height`, cỡ chữ SVG nhỏ nhất sau scale ước tính không dưới khoảng `26px`, tương ứng hơn `0.75em` của thân bài.

## Sai khác so với nguồn

1. Dời CTDE lên trước thuật toán để khóa thông tin training/execution.
2. Tách VDN khỏi QMIX; nguồn đã gộp sai hai cấu trúc.
3. Thêm `L12-07B` để nêu miền/kiểu, chuỗi lịch sử và công thức cảm sinh có đủ giả thiết; thêm `L12-22B` để hoàn tất bước huấn luyện QMIX.
4. Thu gọn MADDPG vì Bài 11 đã dạy DPG/DDPG, nhưng giữ đủ actor gradient, target actors và terminal mask.
5. Thay 19 trang benchmark bằng taxonomy, ca đại diện và giới hạn bằng chứng; không dựng lại screenshot hoặc đường cong thiếu dữ liệu gốc.
6. Gộp PyMARL, EPyMARL, MARLlib và HARL thành ma trận theo tài liệu nguồn; không tuyên bố support hiện tại.
7. Bỏ AutoGen khỏi nội dung hiển thị vì nó không mặc nhiên là MARL.
8. Sửa phần communication để tách CTDE, topology, tần suất, nội dung, integration và constraints.
9. Chuyển ba bài tập ra sau kết luận, gộp COMA với VDN/QMIX, gộp hai cụm giao tiếp và đặt kết luận–bài tập trong cùng mạch cuối để đạt 7 mạch ngoài; hai phần linh hoạt vẫn là đuôi dọc cho tuyến 110/120 phút.

## Tài sản và ngoại lệ

- 76/76 media đã được ánh xạ trong `outline.md`.
- Logo, UI, screenshot và plot raster bị bỏ khi không mang quan hệ kỹ thuật cần thiết hoặc thiếu dữ liệu để tái tạo.
- Sơ đồ kỹ thuật được vẽ lại thành 11 SVG; công thức và bảng dùng KaTeX/HTML. Mọi nhãn SVG có nghĩa dùng cỡ nguồn từ `30px`, không còn nhãn `17px`–`24px` của bản nháp.
- Không có ngoại lệ raster cần người dùng duyệt.

## Nguồn sơ cấp dùng để sửa hoặc kiểm chứng

- Littman (1994), Markov games.
- Foerster et al. (2018), COMA.
- Lowe et al. (2017), MADDPG và MPE.
- Sunehag et al. (2018), VDN; Rashid et al. (2020), QMIX.
- de Witt et al. (2020), IPPO; Yu et al. (2022), MAPPO.
- Kuba et al. (2021/2022), HATRPO/HAPPO.
- Samvelyan et al. (2019), SMAC; Kurach et al. (2020), Google Research Football.
- Papoudakis et al. (2020), EPyMARL; Hu et al. (2023), MARLlib; Zhong et al. (2023), HARL.
- Zhu, Dastani & Wang (2022/2024), communication survey; Singh et al. (2018); Agarwal et al. (2019); Kim et al. (2020).

## Năm báo cáo độc lập của vòng hiện tại

Cả năm báo cáo hợp lệ có `requested_model=z-ai/glm-5.3-flash`, `observed_model=z-ai/glm-5.3-flash`, `provider=OpenRouter`. Lượt sư phạm đầu tiên bị treo phản hồi ở vòng 7 và bị hủy; lượt chạy lại riêng hoàn tất, nên chỉ lượt chạy lại được tính.

### Góc nhìn sinh viên

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa |
|---|---|---|---|---|
| trung bình | `L12-11` | VDN bị gộp với QMIX và mixer. | Hàng cũ ghi “VDN/QMIX — target và mixer”. | Tách hai hàng, ghi đây là bản đồ tới trước. Đã sửa. |
| trung bình | `L12-28` | $r_m^{\mathrm{new}}$ chưa có định nghĩa trên mặt trang. | Recurrence dùng ký hiệu mới chỉ được giải thích trong notes. | Định nghĩa $r_m^{\mathrm{new}}=r_m(\theta_m^*)$. Đã sửa. |
| trung bình | `L12-33` | Phạm vi MAgent ghi “hình nguồn” mơ hồ. | Không xác định hình nào hoặc ý nghĩa con số. | Ghi rõ slide nguồn chỉ minh họa cấu hình 22–1000. Đã sửa. |
| nhẹ | `L12-05`, `L12-45` | “Động lực nền” mơ hồ; chỉ dẫn bài tập không nêu phím Xuống. | Một cụm dễ hiểu thành motivation; bài tập ở cùng stack dọc. | Dùng kernel chuyển tiếp nền $P$ và ghi “Bấm Xuống”. Đã sửa. |

### Chuyên gia Học tăng cường

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa |
|---|---|---|---|---|
| trung bình | `L12-30` | LBF bị mô tả như mặc định mixed. | Bản cũ ghi “mặc định có yếu tố hợp tác–cạnh tranh”. | Ghi mặc định hợp tác; biến thể phụ thuộc cấu hình. Đã sửa. |
| trung bình | `L12-23` | MADDPG thiếu hành vi khám phá khi thu dữ liệu. | Actor tất định không tự tạo exploration. | Thêm policy khám phá/nhiễu trong notes, tách khỏi target actor. Đã sửa. |
| trung bình | `L12-25`, `L12-28` | Chưa nói advantage được tính và giữ cố định thế nào. | Công thức chỉ có ratio và multiplier. | Ghi advantage/GAE tính dưới policy cũ, giữ cố định; chuẩn hóa batch là lựa chọn triển khai. Đã sửa. |
| trung bình | `L12-33` | Mốc Arena thiếu mẫu trên mặt trang. | Mẫu 7.215/7.257 chỉ ở notes. | Đưa mốc 18–21/4/2019 và mẫu vào bảng. Đã sửa. |

### Độ chính xác toán học và thuật toán

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa |
|---|---|---|---|---|
| trung bình | `L12-18`–`L12-22B` | Chữ ký $Q_{\mathrm{tot}}$ và đường gradient chưa nhất quán. | `L12-18` thiếu $s$; câu backprop có thể bị hiểu là đi qua argmax. | Thêm $s$; ghi argmax/target dừng gradient và loss chỉ backprop qua dự đoán online. Đã sửa. |
| trung bình | `L12-05` | Ghi chú về một bộ học và tính không dừng tự mâu thuẫn. | Cấu trúc câu cũ làm sai quan hệ nguyên nhân. | Viết lại theo kernel nền và nhiều bộ học độc lập. Đã sửa. |
| nhẹ | `L12-08`, `L12-16`, `L12-20`, `X02` | Thiếu $\Omega$ trong kỳ vọng, thiếu tổng theo $t$, trộn vector/vô hướng, và đáp án QMIX thiếu utility target. | Các ký hiệu không khớp phần định nghĩa hoặc bước target. | Sửa bốn vị trí theo hợp đồng đã khóa. Đã sửa. |

### Phản biện học thuật và giảng dạy

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa |
|---|---|---|---|---|
| trung bình | `L12-29`–`L12-34` | Tuyến 110 phút không có kiểm tra benchmark tại chỗ. | `L12-37` thuộc nhánh linh hoạt, `X03` ở sau kết luận. | Thêm câu kiểm tra tại `L12-34`. Đã sửa. |
| trung bình | `L12-38`–`L12-42` | Tuyến cốt lõi giao tiếp không có kiểm tra tại chỗ. | Không có `.check` trước điểm cắt `L12-42`. | Thêm câu phân biệt topology và policy gửi tại `L12-42`. Đã sửa. |
| trung bình | `L12-11` | Bảng thuật toán xuất hiện trước trực giác từng họ. | Các công thức bắt đầu từ `L12-13`. | Đổi tiêu đề thành bản đồ và báo rõ ký hiệu sẽ học sau. Đã sửa. |

### Kết nối và mạch viết

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa |
|---|---|---|---|---|
| nghiêm trọng | `L12-34` → `L12-38` | Vai trò trong mạch: trang chốt bằng chứng không có kết nối ra; trang mở giao tiếp không có kết nối vào. | Cầu nối cũ chỉ nằm ở `L12-37`, bị tuyến 110 phút cắt bỏ. | Đặt cầu nối ở notes của cả `L12-34` và `L12-38`; kết nối ra sang taxonomy `L12-39`. Đã sửa. |
| trung bình | `L12-42` → `L12-45` | Vai trò trong mạch: điểm cắt giao tiếp→kết luận thiếu kết nối vào–ra. | Cầu nối cũ chỉ có trong nhánh linh hoạt `L12-43`–`L12-44`. | Thêm câu tổng hợp ở `L12-42` và thu hồi mạch giao tiếp tại `L12-45`. Đã sửa. |
| trung bình | `L12-03`→`L12-04`, `L12-12`→`L12-13`, `L12-17`→`L12-18`, `L12-22B`→`L12-23`, `L12-28`→`L12-29` | Vai trò trong mạch đúng trong storyboard nhưng tín hiệu chuyển chưa nằm ở trang biên. | Người học chỉ thấy bước nhảy mục tiêu→hợp đồng hoặc công thức→họ thuật toán kế. | Thêm câu nối vào notes/mặt trang tại đúng ranh giới; giữ nguyên thứ tự nguồn. Đã sửa. |

## Quyết định của pha chỉnh sửa hiện tại

- Đã xử lý lỗi `nghiêm trọng` và mọi mục `trung bình` liên quan đến tính đúng, chu trình học tập, điểm cắt tuyến cốt lõi và phạm vi bằng chứng.
- Không chuyển đáp án của sáu câu kiểm tra tại chỗ thành fragment. Đây là bộ trang chiếu giảng dạy; đáp án trong notes giữ mặt trang gọn, còn `X01`–`X03` đã có fragment để chữa bài. Quyết định không ảnh hưởng tính đúng hoặc khả năng trình chiếu.
- Không thêm trang tài liệu tham khảo riêng và không đổi các `max-height` cục bộ trước khi render. Nguồn đã truy nguyên trong notes; chiều cao từng hình phải được quyết định bằng kiểm định hiển thị, không bằng đồng nhất số CSS cơ học.
- Biên tập theo `no-ai-slop`: cắt lời dẫn rỗng, sửa cụm mơ hồ “động lực nền”, giữ câu ngắn và không thêm kết quả thực nghiệm. Rà theo Quill: giữ tuyến hợp đồng → thuật toán → bằng chứng → giao tiếp → checklist; không tạo `quill.json`.

## Kiểm định cuối của điều phối viên

1. Đủ năm báo cáo độc lập hiện tại; mọi lỗi `chặn bàn giao` và `nghiêm trọng` đã được xử lý. Tái kiểm toán toán học và mạch viết sau sửa đều có `requested_model=observed_model=z-ai/glm-5.3-flash`, `provider=OpenRouter`, kết luận `PASS` và không còn lỗi bắt buộc.
2. Kiểm định tĩnh đạt: 50 mã trang duy nhất, 50 ghi chú, 7 `<section>` ngoài, độ sâu tối đa 2, 21 tham chiếu cục bộ hợp lệ, 11 SVG XML hợp lệ, không có raster hoặc phụ thuộc mạng cốt lõi. `index.html` liên kết đúng tới bài và không liên kết tệp planning.
3. `python3 -m reloadserver 8765` thất bại vì môi trường không có mô-đun `reloadserver`. Máy chủ dự phòng `python3 -m http.server --bind 127.0.0.1 8765` đã phục vụ bản này trong các lượt kiểm định đầu; HTML, CSS, JavaScript, font KaTeX và 11 SVG đều trả `200`. Sau đó cổng 8765 bị một kho khác chiếm, nên lượt tái kiểm cuối dùng cổng tạm 8766 mà không đổi nội dung.
4. Chromium headless đã duyệt đủ 50 trang ở 1280×720 và 800×600, tạo 100 ảnh kiểm tra; không có lỗi console, lỗi request hoặc tràn sau khi bộ dò bỏ nhiễu `scrollWidth` nội bộ của KaTeX. Điều phối viên đã xem contact sheet toàn bài và các trang dày `L12-11`, `L12-16`, `L12-22B`, `L12-28`, `L12-33`, `L12-34`, `L12-42`, `L12-45`.
5. KaTeX render 150 biểu thức, 0 lỗi. Sáu trạng thái fragment của `X01`–`X03` ở hai viewport đều hiển thị đủ, không bị cắt. Bảy phép thử điều hướng đạt: hai nhánh cắt `L12-34`, `L12-42`, kết luận → `X01`, và chuyển `X01` → `X02` → `X03` sau khi mở fragment đáp án.
6. Dự án Codex Slides `20260825012827-b-i-12-nh-p-m-n-h-c-t-ng-c-ng-a-t-c-t-fht2` truy cập được. Năm Design Files (HTML, outline, storyboard, review-log, note-for-author) khớp chính xác từng ký tự với bản trong kho. Dự án vẫn là draft với 0 slide native; môi trường không có Browser nhúng để rà trực quan trong giao diện Codex Slides, nên không tuyên bố đã rà hình bằng Browser. Kiểm định hình ảnh được thực hiện bằng RevealJS/Chromium cục bộ như mục 4.

### Bằng chứng runtime của vòng hiện tại

- Lượt lập kế hoạch, phân tích nguồn và tái kiểm định storyboard hợp lệ đều có `requested_model=z-ai/glm-5.3-flash`, `observed_model=z-ai/glm-5.3-flash`, `provider=OpenRouter`. Lượt storyboard hợp lệ dùng `reasoning_effort=low`; hai lượt trước bị cắt do vượt ngân sách đầu ra nên không được dùng làm bằng chứng.
- Hai lượt writer không hoàn tất: lượt đầu không tạo thay đổi; lượt sau chỉ sửa một phần ranh giới `<section>` rồi chạm giới hạn tool call. Điều phối viên đã kiểm tra byte, sửa lại cấu trúc và hoàn tất các thay đổi bằng `apply_patch`; không coi hai lượt này là bằng chứng bàn giao.
- Năm reviewer độc lập và hai lượt tái kiểm hợp lệ đều dùng `requested_model=observed_model=z-ai/glm-5.3-flash`, `provider=OpenRouter`. Lượt reviewer sư phạm đầu tiên bị treo phản hồi và bị hủy; lượt chạy lại riêng hoàn tất mới được tính.
- Không thêm trang tài liệu tham khảo riêng. Ghi chú diễn giả đã giữ truy nguyên nguồn; thêm một trang mới sẽ đổi 50 mã trang và lấy thời gian khỏi tuyến 120 phút mà không tăng nội dung khái niệm.

## Đối chiếu mã trang của bản nháp

Trang chính theo thứ tự: `L12-01`–`L12-07`, `L12-07B`, `L12-08`–`L12-22`, `L12-22B`, `L12-23`–`L12-45`. Cụm cuối: `X01`, `X02`, `X03`. Tổng 50 mã; bảng route/hash nằm trong storyboard.

Danh mục 50 mã trang: `L12-01`, `L12-02`, `L12-03`, `L12-04`, `L12-05`, `L12-06`, `L12-07`, `L12-07B`, `L12-08`, `L12-09`, `L12-10`, `L12-11`, `L12-12`, `L12-13`, `L12-14`, `L12-15`, `L12-16`, `L12-17`, `L12-18`, `L12-19`, `L12-20`, `L12-21`, `L12-22`, `L12-22B`, `L12-23`, `L12-24`, `L12-25`, `L12-26`, `L12-27`, `L12-28`, `L12-29`, `L12-30`, `L12-31`, `L12-32`, `L12-33`, `L12-34`, `L12-35`, `L12-36`, `L12-37`, `L12-38`, `L12-39`, `L12-40`, `L12-41`, `L12-42`, `L12-43`, `L12-44`, `L12-45`, `X01`, `X02`, `X03`.

## Nhật ký Giai đoạn I — lecture note Bài 12

- Nguồn và plan: `RL-hk2-2025-2026/Lecture12-MARL.pptx` (54 trang, bản trích 585 dòng); plan reader và source reader đều `requested_model=observed_model=deepseek/deepseek-v4-flash-0731`, provider `OpenRouter`, reasoning `none`. Topic-map reviewer cùng model, profile `review`.
- Metadata runtime: draft writer và ba patch writer dùng `requested_model=observed_model=z-ai/glm-5.3-flash`, provider `OpenRouter`, profiles `write`/`patch`, reasoning `minimal`. Năm reviewer độc lập: student/flow `z-ai/glm-5.3-flash`, expert/math/pedagogy `deepseek/deepseek-v4-flash-0731`; recheck student/flow `z-ai/glm-5.3-flash`, recheck math `deepseek/deepseek-v4-flash-0731`; provider `OpenRouter`, profile `recheck`.
- Bảng năm báo cáo độc lập (mức độ, vị trí, vấn đề, bằng chứng, đề xuất sửa):
  - Sinh viên: 3 chặn bàn giao + 3 nghiêm trọng về "hỏng mã hóa" tại topic-11, 05, 06, 08, 10, 02; 2 trung bình (thuật ngữ "gán công", tỷ lệ OpenAI Five); 2 nhẹ. Kết luận KHÔNG PASS.
  - Chuyên gia RL: PASS; 2 phát hiện mức thấp — chiều sâu HATRPO mỏng (dòng 301) và thiếu bảng phân bổ thời lượng theo nhóm chủ đề.
  - Toán học: PASS; tính lại toàn bộ ví dụ số (COMA b=5/A=1, QMIX 12,5, HAPPO 2,64/1,98, OpenAI Five 99,421%), miền/kiểu, chỉ số, kích thước tensor — không lỗi.
  - Sư phạm: KHÔNG PASS; 1 nghiêm trọng — cầu nối PPO (topic-12) đặt sau MAPPO/HAPPO mà nó là tiên quyết; 2 trung bình — "Nối ra" của cầu nối PG/AC nói "COMA ở topic kế" sai vị trí và bỏ MADDPG.
  - Mạch viết: PASS; 1 trung bình — cầu nối PPO đứt kết nối vào khi đặt sau topic-10; 3 nhẹ về kết nối vào/ra và thu hồi nhánh bổ sung.

### Trường phát hiện chuẩn hóa của năm báo cáo note

| vai rà soát | mức độ | vị trí | vấn đề | bằng chứng | đề xuất sửa và quyết định |
|---|---|---|---|---|---|
| Góc nhìn sinh viên | chặn bàn giao | topic-11, 05, 06 | Reviewer báo công thức và văn bản bị hỏng mã hóa. | Điều phối viên đọc trực tiếp đúng các khối; `file` xác nhận UTF-8 và `iconv` không báo lỗi. Recheck sinh viên đọc được toàn bộ công thức. | Từ chối như false positive; không sửa công thức đúng. |
| Góc nhìn sinh viên | nghiêm trọng | topic-08, 10, 02 | Reviewer báo các đoạn HAPPO, giao tiếp và câu nối không đọc được. | Các đoạn nguyên vẹn trong tệp; recheck trích đúng HAPPO và topology/policy gửi. | Từ chối như false positive; recheck PASS. |
| Góc nhìn sinh viên | trung bình | topic-14; X02 | Mẫu của tỷ lệ OpenAI Five chưa rõ; X02 chưa yêu cầu tính target QMIX. | Bản nháp chỉ nêu 7.215/7.257 và hỏi đường chọn/đánh giá. | Ghi rõ tỷ lệ thắng thuộc sự kiện; thêm phép tính $y$, loss và ca terminal vào topic-05/X02. |
| Góc nhìn sinh viên | trung bình | toàn note | Reviewer nghi “gán công” là lỗi từ. | Thuật ngữ dùng nhất quán cho credit assignment và đúng ngữ cảnh COMA. | Không áp dụng; giữ “gán công (credit assignment)”. |
| Chuyên gia Học tăng cường | nhẹ | topic-08 | HATRPO mỏng hơn HAPPO. | Bản nháp chỉ nói cùng ý tưởng tuần tự. | Thêm giới hạn: HATRPO thay clip bằng trust region/KL; không triển khai ngoài nguồn. |
| Chuyên gia Học tăng cường | nhẹ | bản đồ chủ đề | Chưa có ngân sách thời gian theo cụm. | Chỉ X01–X03 có thời lượng. | Thêm 110 phút tuyến chính + 10 phút linh hoạt; bài tập 30 phút. |
| Độ chính xác toán học–thuật toán | nhẹ | toàn note | Không có lỗi bắt buộc; cần xác nhận lại các phép tính và hợp đồng gradient. | Reviewer tính lại COMA $b=5$, QMIX $12{,}5$, MAPPO $2{,}4$, HAPPO $2{,}64/1{,}98$, Jacobian MADDPG và các mask; tất cả khớp. | Giữ công thức; recheck riêng target QMIX sau bổ sung. |
| Phản biện học thuật–giảng dạy | nghiêm trọng | topic-12 so với topic-07/08 | Cầu nối PPO đặt sau MAPPO/HAPPO. | Câu “đọc lại topic 07 và 08” cho thấy tiên quyết xuất hiện sau nội dung phụ thuộc. | Di chuyển topic-12 lên sau MADDPG và trước MAPPO; recheck flow PASS. |
| Phản biện học thuật–giảng dạy | trung bình | topic-11 | Câu “COMA ở topic kế” sai vị trí và không nối MADDPG. | Ba topic hợp đồng nằm giữa cầu nối và COMA; topic-map ghi C1 phục vụ T4 và T6. | Đặt topic-11 sau CTDE; dẫn rõ tới COMA topic-04 và MADDPG topic-06. |
| Kết nối và mạch viết | trung bình | topic-12 | Vai trò trong mạch là tiên quyết on-policy nhưng kết nối vào–ra bị đảo. | Topic-12 nằm sau topic-10 trong bản nháp, trái vị trí “trước T7” của topic-map. | Di chuyển trước topic-07/08; đổi “đọc lại” thành “đọc”. |
| Kết nối và mạch viết | nhẹ | topic-09, 13, 10; phần kết | Nhánh framework thiếu kết nối vào–ra và kết bài thu hồi chưa rõ. | Topic-09 nối thẳng tới giao tiếp trong khi topic-13 nằm sau topic-10. | Đặt topic-13 sau benchmark, thêm đường quay lại topic-10 và giữ phép kiểm phiên bản ở kết bài. |
- Quyết định áp dụng/từ chối:
  - Áp dụng: di chuyển `lec-12-topic-11` xuống sau topic-03; di chuyển `lec-12-topic-12` lên sau topic-06 trước topic-07; đặt lại nhánh framework sau benchmark rồi quay về giao tiếp; thêm ví dụ tính tay target QMIX và câu target trong X02; nêu HATRPO dùng trust region/KL; làm rõ tỷ lệ OpenAI Five 7.215/7.257 trận của sự kiện; giữ tổng 110 + 10 phút.
  - Từ chối (false positive mã hóa): các phát hiện "hỏng văn bản/mã hóa" của reviewer sinh viên bị bác bỏ — điều phối viên kiểm bằng `file`, `iconv` và đọc trực tiếp; tệp UTF-8 hợp lệ, các khối công thức PG, QMIX, MADDPG, HAPPO và giao tiếp nguyên vẹn. Giữ thuật ngữ "gán công (credit assignment)"; không mở rộng claim/nguồn ngoài packet.
- Ba recheck PASS: recheck student PASS (3 ghi chú minor không chặn); recheck math PASS (tự tính lại $y=5{,}1$, loss $0{,}25$, terminal $y=1{,}5$); recheck flow PASS (thứ tự topic khớp 100%, ngân sách 120 phút đạt, 3 ghi chú nhẹ N1–N3).
- Kiểm no-ai-slop/Quill: tự kiểm theo `no-ai-slop/eval.md` — không từ cấm/pattern rỗng, không thêm claim ngoài nguồn, câu ngắn; không tạo `quill.json`, công thức chỉ dùng `$`/`$$`.
- Cổng tĩnh: 15 `note-topic-id` duy nhất, đủ bốn nhóm topic, ba exercise có hint/solution, không raster, không phụ thuộc mạng cốt lõi.
- Ngân sách: 110 phút tuyến chính + 10 phút linh hoạt; X01–X03 30 phút ngoài phần trình chiếu.
- Ngoại lệ index: theo goal hiện hành, thẻ index có hai nhóm Bài giảng/Ghi chú bài giảng thay cho quy tắc một liên kết duy nhất cũ trong `AGENTS.md`; không liên kết tệp planning.
- Viewer/index sau khi công bố note: `python3 -m reloadserver 8765` không chạy vì thiếu mô-đun `reloadserver`. Máy chủ dự phòng chỉ phục vụ webroot tạm đã loại `.env`; Chromium tải viewer ở 1280×720 và 800×600 với 20 mục lục, 270 node KaTeX, 9 khối chỉ dẫn và 6 `details`, không lỗi console/request và không tràn ngang. Phím Tab vào skip-link; Enter trên `summary` đóng/mở được. Hai truy vấn `../.env` và lệch số bài đều bị chặn, ẩn layout và báo lỗi. Index có 12 thẻ; Bài 12 có đúng hai liên kết deck/note, không lỗi tài nguyên ở cả hai viewport.
- Codex Slides chưa được dùng ở Giai đoạn I; kiểm định deck thuộc Giai đoạn II.
