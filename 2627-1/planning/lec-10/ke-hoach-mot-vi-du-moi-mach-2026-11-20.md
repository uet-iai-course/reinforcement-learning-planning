# Kế hoạch rút gọn ví dụ của deck Bài 10: mỗi mạch một ví dụ (2026-11-20)

Căn cứ: tác giả 2026-11-20 ("Kiểm tra lại số lượng ví dụ, chỉ để lại các ví dụ cần thiết, bổ sung nội dung cho các ví dụ đó"; "Mỗi mạch chỉ cần 1 ví dụ"; "Là quy định chung"), NT23 sửa cùng ngày. Tác tử lập kế hoạch chỉ đọc (`general-purpose`, `opus`, `high`); điều phối viên tóm tắt. Rà trước đó: `ra-soat-vi-du-NT23-2026-11-20.md`.

## Ví dụ giữ lại (một mỗi mạch)

| Mạch | Ví dụ giữ | Ghi chú | Trang sau sửa | Câu hỏi của mạch nó phục vụ |
|---|---|---|---|---|
| 1 | Hành lang ngắn: một lượt REINFORCE, rồi một bước theo đúng gradient | Ví dụ 10.2 và đoạn sau | `L10-107`, `107b`, `107c`, `108` (mở rộng thành bảng $\alpha=0{,}1$; $0{,}5$) | hai giới hạn của REINFORCE |
| 2 | Chuỗi hai trạng thái: $v_\pi$, $q_\pi$, $A_\pi$, rồi hai bước actor–critic | Ví dụ 10.6 + 10.7 | `L10-214`…`214e` (bỏ mã `211`) | lợi thế; bước tính tay trước Thuật toán 10.9 |
| 3 | Kết thúc và cắt ngắn trong GAE | Ví dụ 10.10 | `L10-307`, `307b`, `307c` | trộn TD và Monte Carlo trên đoạn thu; trước Thuật toán 10.16 |
| 4 | Đổi chính sách $p'=(0{,}6;0{,}8)$ và chặn cải thiện của bước đó | Ví dụ 10.11 + 10.12 | `L10-410`…`410d` (bỏ `402`) | đánh giá chính sách mới bằng dữ liệu cũ, cận sai số |
| 5 | Hai vòng gradient liên hợp | Ví dụ 10.16 | `L10-505`, `505b`, `505c` | bước tính tay trước Thuật toán 10.36 |
| 6 | Một mini-batch PPO tính tay, kèm chẩn đoán trên đoạn phẳng | Ví dụ 10.20 + 10.21 | `L10-610`…`610e` (sau `611b`; bỏ `614`) | trước Thuật toán 10.49 |
| 7 | Một bước DPO tính tay, bảng năm bước | Ví dụ 10.28 | `L10-D14`, `D14b`, `D14c` | trước Thuật toán 10.67 |
| 8 | (không có ví dụ) | — | — | — |

## Ví dụ bỏ khỏi deck (nội dung còn trong ghi chú)

`L10-106`, `106b` (Ví dụ 10.1, một dòng kết quả lên `L10-201`); `202`, `206` (dòng kết quả lên `204`); `211` (chuyển vào E2); `301`, `305` (dòng lên `302`, `306`); `402` (vào E4); `501`, `504` (dòng lên `502`, `503`); `602`, `605` (hình chuyển sang `606`, `604`), `614` (vào E6), `617` (ghi chú diễn giả `617b`); `D02b`, `D06` (dòng lên `D02`, `D04`); `L10-D08` đổi thành trang "Hai mỏ neo" không có phép tính. Dòng "Ví dụ."/"Kiểm" trên các trang kết quả bỏ hoặc rút thành một dòng kết quả không chuỗi tính.

## Bài tập (không tính là ví dụ)

Giữ mỗi mạch một bài: 10.1 (`210`), 10.7 (`309` + `309b`), 10.11 (`413`/`414`), 10.8 (`509`/`510`), 10.12 (`619`/`620`, (d) ở `608`), 10.18 (`D18` + `D18b`), Tình huống 10.1–10.2 (`705`/`706` + `706b`). Bỏ `216` (Bài tập 10.5). Phương án A′: lời giải trên mặt trang, mở rộng theo NT23 (+4 trang); phương án B: lời giải của 10.11, 10.8, 10.12 xuống ghi chú diễn giả.

## Tổng

- A′: 137 trang; B: 130 trang (hiện 130). Thời lượng giảng khoảng 127–131 phút (đích 135).
- Không liên kết sâu nào gãy: mọi `#/N/1`, `#/N` trỏ trang tiêu đề mạch, giữ nguyên. Các tham chiếu chữ cần sửa: xem báo cáo của tác tử (danh sách theo trang, `L10-104` … `L10-709`).
- Thứ tự làm: mạch 1 → 2 (trước 4, vì E4 dùng $A_\pi$ của E2) → 3 → … → 8 → việc chung (storyboard, outline, review-log, NGUYEN-TAC-HOC-PHAN mục 6, PDF). Mỗi mạch: biên tập → kiểm toán và mạch ±2 trang → trình duyệt.

## Quyết định của tác giả (2026-11-20)

Điểm 1–2: chấp nhận ngoại lệ, cho mọi môn (NT23). Điểm 3: mạch 2 giữ chuỗi hai trạng thái; mạch 3 giữ Ví dụ 10.10. Điểm 4: phương án A′ (137 trang), mạch 2 giữ Bài tập 10.1, bỏ 10.5 khỏi deck.

## Điểm vướng đã hỏi tác giả

1. NT-RL-2/GC-RL-11: Thuật toán 10.6 (REINFORCE có đường cơ sở) và 10.61 (RLHF với PPO) mất bước tính tay, chỉ còn dòng kết quả có số.
2. Hành trình khái niệm: bước "ví dụ" của các chủ đề cốt lõi không sở hữu ví dụ của mạch (03, 05, 10, 11, 12, 15, 17, 18, 26, 27) chỉ còn dòng kết quả có số hoặc hình.
3. Chọn ví dụ mạch 2 (chuỗi hai trạng thái hay hành lang có đường cơ sở) và mạch 3 (Ví dụ 10.10 hay 10.8/10.9 trên chuỗi).
4. Bài tập: A′ hay B; mạch 2 giữ 10.1 hay 10.5.

Tác giả thêm (2026-11-20): "nếu cần bổ sung nội dung vào ví dụ được chọn" — khi một khái niệm hay thuật toán của mạch mất ví dụ riêng, người biên tập ưu tiên bổ sung một phần vào ví dụ được chọn của mạch (cùng đối tượng, thêm một bảng hoặc một trang tiếp nối) trước khi rút thành một dòng kết quả; vẫn chỉ một ví dụ mỗi mạch.
