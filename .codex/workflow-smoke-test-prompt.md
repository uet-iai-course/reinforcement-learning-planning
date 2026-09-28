# Kiểm thử quy trình tác tử gốc của Codex

Kiểm thử điều phối theo `AGENTS.md`; không chuyển bài giảng hoặc sửa tệp
trong kho. Ghi nhận `git status --short` trước và sau để phân biệt thay đổi
đã có với thay đổi do kiểm thử.

## Trình tự

1. Đọc `AGENTS.md`. Mọi tác tử trong kiểm thử dùng
   `collaboration.spawn_agent` với `model: "gpt-6-astra"` và
   `fork_turns: "none"` hoặc số lượt phù hợp. Không dùng OpenRouter,
   script gọi mô hình qua API/CLI hoặc nạp `.env`, `.env.*` hay khóa API.
2. Giao một tác tử chỉ đọc `AGENTS.md`, tóm tắt trách nhiệm của điều phối
   viên và thứ tự các giai đoạn, kèm số dòng làm bằng chứng. Codex chính
   kiểm tra và chấp nhận kết quả trước bước tiếp theo.
3. Giao hai tác tử rà soát chỉ đọc độc lập; chạy song song trong giới hạn
   khả dụng. Tác tử thứ nhất đối chiếu độ chính xác của bản tóm tắt.
   Tác tử thứ hai kiểm tra ràng buộc về mô hình, quyền ghi, năm vai rà
   soát, văn phong học thuật và kiểm định cuối. Báo cáo gồm `mức độ`,
   `vị trí`, `vấn đề`, `bằng chứng`, `đề xuất sửa`.
4. Sau khi hai báo cáo hoàn tất, Codex chính tạo một thư mục tạm duy nhất
   bằng `mktemp -d /tmp/rl-plan-native-smoke.XXXXXX`. Giao một tác tử chỉ
   tạo `worker-check.txt` trong thư mục đó, ghi vai trò và kết quả nhiệm
   vụ; không yêu cầu tác tử tự chứng thực mô hình hoặc tuyến xác thực.
   Không cho phép sửa tệp trong kho hoặc chạy tác tử ghi khác đồng thời.
5. Codex chính đọc và kiểm tra tệp kết quả, chỉ xóa tệp và thư mục tạm
   vừa tạo, rồi đối chiếu trạng thái Git với bản đầu. Kiểm tra độc lập
   mọi đầu ra; không chấp nhận báo cáo hoàn thành nếu chưa có bằng chứng.
6. Báo cáo tên tác tử, vai trò, mô hình đã chỉ định từ lời gọi công cụ,
   trạng thái, bằng chứng hoàn thành và kết quả kiểm tra của Codex chính.
   Chỉ ghi mô hình thực chạy hoặc tuyến xác thực nếu công cụ cung cấp;
   nếu không, ghi rõ chưa có bằng chứng này.

## Tiêu chí đạt

- Tất cả tác tử được tạo qua cơ chế gốc với GPT-6-Astra được chỉ định.
- Hai báo cáo rà soát độc lập và được Codex chính kiểm tra.
- Chỉ một tác tử ghi tệp, trong thư mục tạm được giao.
- Kiểm thử không phát sinh thay đổi trong kho; tệp tạm được dọn sau kiểm tra.

Nếu không tạo được tác tử theo quy định, báo lỗi và giai đoạn bị chặn.
Tiếp tục kiểm tra độc lập đã được phép; không thay mô hình, dùng OpenRouter
hoặc script gọi mô hình để hoàn tất kiểm thử.
