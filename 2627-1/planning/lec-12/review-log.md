# Nhật ký rà soát Bài 12

## Trạng thái bản nháp

- Nguồn đã kiểm kê: 54/54 trang chiếu, 76/76 media, 0 trang ẩn, 53 notes rỗng, không code demo.
- Bản sau bốn phản biện và chỉnh sửa: 47 trang chính, gồm `L12-07B`, `L12-22B`, và ba bài tập `X01`–`X03` trong cụm riêng sau kết luận.
- Tài sản đích: 11 SVG; không có tham chiếu ảnh raster và không có ngoại lệ raster.
- Thời lượng thiết kế: 42 trang cốt lõi trong 110 phút; 5 trang linh hoạt không trùng lặp trong 10 phút; 30 phút chữa ba bài tập sau kết luận.
- Bốn báo cáo độc lập đã được hợp nhất dưới đây; mọi lỗi `chặn bàn giao` và `nghiêm trọng` đã được xử lý trong bản hiện tại.

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

## Bốn báo cáo độc lập sau bản nháp

### Góc nhìn sinh viên

| mức độ | trang chiếu | vấn đề | bằng chứng | đề xuất sửa và quyết định |
|---|---|---|---|---|
| nghiêm trọng | toàn bộ điều hướng, `X01`–`X03` | Bài tập nằm giữa các cụm nội dung và kết luận, nên phím Phải/Xuống không tạo tuyến 110/120 phút rõ. | `X01`, `X02`, `X03` từng nằm trong ba stack kiến thức; `L12-42` còn nối tới bài tập trước kết luận. | Chuyển ba bài sang stack ngang 10 sau `L12-45`; dùng đuôi dọc cho hai phần linh hoạt và ghi hash một-gốc. Đã sửa. |
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
| nghiêm trọng | `L12-34`–`L12-45`, `X01`–`X03` | Trình tự trang không thực hiện đúng nhánh cắt đã mô tả trong planning. | Các trang linh hoạt và bài tập cùng nằm trong stack chính, nên không thể đi Phải để bỏ qua đúng chỗ. | Tái cấu trúc thành 10 stack ngang; đuôi framework và threat model dùng Xuống, kết luận thành stack 9, bài tập thành stack 10. Đã sửa. |
| trung bình | `L12-05`, `L12-12` | “Dừng hơn” và “đồng nhất” quá tắt, dễ tạo trực giác sai. | Cụm từ không nêu tác nhân gây không dừng hoặc điều kiện chia sẻ tham số. | Viết lại siêu tác tử theo một bộ chọn joint action; tách compatibility, ID/role và dị thể. Đã sửa. |

## Quyết định hợp nhất sau bốn báo cáo

- Đã xử lý toàn bộ lỗi chặn bàn giao và nghiêm trọng; các lỗi trung bình liên quan trực tiếp tới công thức, tải nhận thức, kiểm tra tại chỗ, điều hướng và khả năng đọc cũng đã xử lý.
- Hai trang bổ sung giữ nguyên tổng 110 phút cốt lõi bằng cách phân bổ lại thời gian trong cụm hợp đồng Markov 25 phút và VDN/QMIX 15 phút; không lấy thời gian từ bài tập.
- Rà lại sau thay đổi số lượng/thứ tự bao phủ `L12-04`–`L12-10`, `L12-18`–`L12-28`, `L12-29`–`L12-45` và toàn bộ `X01`–`X03`, gồm ít nhất hai trang lân cận mỗi phía khi tồn tại.

### Kiểm tra của tác tử chỉnh sửa

- KaTeX strict sau hậu kiểm: 147 biểu thức hợp lệ, `throwOnError: true`, `strict: "error"`.
- Cấu trúc: 50 mã trang duy nhất, 50 khối ghi chú, 10 stack ngang, độ sâu `<section>` tối đa bằng 2; thứ tự stack khớp bảng hash trong storyboard.
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
9. Chuyển ba bài tập ra sau kết luận và tổ chức hai phần linh hoạt thành đuôi dọc để phím Phải/Xuống thực hiện đúng tuyến 110/120 phút.

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

## Kiểm định cuối của điều phối viên

1. Bốn rà soát độc lập và pha chỉnh sửa riêng đã hoàn tất; mọi lỗi chặn và nghiêm trọng đã được xử lý.
2. Tái kiểm toán toán học đã đạt đối với `L12-07B`, `L12-21`–`L12-22B`, `L12-23`, `L12-25` và `L12-28`; không phát sinh lỗi chặn hoặc nghiêm trọng.
3. Kiểm định tĩnh cuối đạt: 50 mã trang duy nhất, 50 ghi chú, 50 mục nguồn, 10 stack ngang, 147 biểu thức KaTeX strict, 11 SVG hợp lệ và không có raster hoặc phụ thuộc mạng.
4. Tiến trình `python3 -m reloadserver 8765` đang phục vụ kho; tệp HTML và 21 tài nguyên cục bộ được kiểm tra qua HTTP, tất cả trả mã `200`.
5. Nguồn PowerPoint đã được nạp vào dự án Codex Slides bền vững. HTML, outline, storyboard, nhật ký và `note-for-author.md` đã được tải lên dưới dạng Design Files; năm tệp trong dự án khớp byte-for-byte với bản trong kho tại thời điểm xác minh.
6. Codex Slides khả dụng qua API dự án nhưng môi trường không cung cấp trình duyệt nhúng, Chromium, Chrome hoặc Firefox. Vì vậy không thể duyệt toàn bộ RevealJS ở khung 16:9 và màn hình hẹp trong trình duyệt, cũng không tuyên bố đã rà trực quan bằng Codex Slides. Hai SVG từng tràn nhãn đã được raster hóa riêng và phản biện học thuật xác nhận không còn chồng lấn.

## Đối chiếu mã trang của bản nháp

Trang chính theo thứ tự: `L12-01`–`L12-07`, `L12-07B`, `L12-08`–`L12-22`, `L12-22B`, `L12-23`–`L12-45`. Cụm cuối: `X01`, `X02`, `X03`. Tổng 50 mã; bảng route/hash nằm trong storyboard.
