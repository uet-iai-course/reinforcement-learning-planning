# Rà các trang có phép tính của deck Bài 10 theo NT23 (2026-11-20)

Căn cứ: yêu cầu của tác giả 2026-11-20 ("các ví dụ cần viết sao cho sinh viên có thể tự tính lại, theo các bước"), đoạn bổ sung của NT23 trong `NGUYEN-TAC-TRANG-CHIEU.md`. Tác tử rà chỉ đọc (`general-purpose`, `opus`, `high`); điều phối viên tóm tắt. Không gồm `L10-101`, `L10-106`, `L10-107` (đã sửa cùng ngày).

## Kết quả

- 57 trang có phép tính: 4 đạt (`L10-210`, `L10-413`, `L10-705`, `L10-D01`), 53 không đạt.
- Nghiêm trọng (15): `L10-202`, `206`, `211`, `402`, `410`, `414`, `504`, `505`, `510`, `602`, `610`, `620`, `D06`, `D08`, `D14`.
- Trung bình (24): `L10-108`, `208`, `213`, `214`, `216`, `301`, `303`, `305`, `307`, `309`, `403`, `406`, `407`, `412b`, `501`, `605`, `607`, `611`, `614`, `617`, `D03`, `D17`, `D18`, `706`.
- Nhẹ (14, sửa tại chỗ, không thêm trang): `L10-207`, `212`, `304`, `405`, `408`, `411`, `502`, `502b`, `509`, `608`, `619`, `D02b`, `D10`, `D11`.
- Số trang thêm: đề xuất đầy đủ khoảng +40 (127 → khoảng 167); chỉ nghiêm trọng và trung bình, gộp bảng vừa một trang: khoảng +30.

## Bốn kiểu lỗi lặp lại

1. Phép tính đặt cạnh hình (`grid2`): `L10-202`, `211`, `303`, `504`, `505`, `602`, `605`.
2. Ví dụ đứng trước công thức nó dùng (cần dòng "Công thức:" hoặc đổi thứ tự): `L10-505`/`506`, `602`/`603`, `607`/`608`, `214`/`215`; $F_s$ của Ví dụ 10.14 chưa được dẫn ra ở trang nào.
3. Bảng thiếu cột trung gian: $p_k$, $Fp_k$ (gradient liên hợp); $\operatorname{clip}(\rho)$, $\rho\widehat A$ (PPO); giá trị bootstrap, hệ số ngắt (GAE); $\psi_t$ (REINFORCE, actor–critic).
4. Số nền cho sẵn, không trang nào tính: $v_\pi$, $A_\pi$ (`L10-211`), $\nu^\pi$ (`L10-403`) của chuỗi hai trạng thái, dùng lại ở hơn mười trang. Đề xuất một trang "Dữ kiện chuỗi hai trạng thái" có phép tính đầy đủ.

## Lưu ý khi sửa

- Bảng 8–11 cột (`L10-505`, `510`, `610`, `620`, `D14`, `D18`) phải tách thành hai bảng theo thứ tự tính.
- Cách kiểm thứ hai, lỗi thường gặp, Nhận xét 10.58 (khỏi `L10-D08`) chuyển xuống ghi chú diễn giả; mặt trang giữ một đường tính.
- Mọi số tác tử kiểm đều khớp ghi chú; ghi chú bài giảng có đủ phép tính trung gian để dùng.
- Đề xuất bố cục chi tiết từng trang: báo cáo của tác tử rà (phiên 2026-11-20); điều phối viên chuyển cho người biên tập khi tác giả chọn phạm vi.

## Trạng thái

Chờ tác giả chọn phạm vi sửa (số trang thêm ảnh hưởng thời lượng P6).
