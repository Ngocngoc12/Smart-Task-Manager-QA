# 📋 Kịch bản Kiểm thử Thủ công (Manual Test Cases)
*Dự án: Hệ thống Quản lý Công việc (Task Manager)*

| Mã TC | Chức năng | Mô tả Test Case | Các bước thực hiện | Kết quả mong đợi | Trạng thái |
|---|---|---|---|---|---|
| TC_01 | API GET | Lấy danh sách Task | 1. Gửi request GET đến `/todos` | Trả về Status 200, danh sách không rỗng. | ✅ PASS |
| TC_02 | API POST | Tạo Task mới hợp lệ | 1. Gửi POST đến `/todos` kèm JSON data (title, userId) | Trả về Status 201 (Created), data khớp. | ✅ PASS |
| TC_03 | API POST | Tạo Task thiếu Title | 1. Gửi POST đến `/todos` thiếu field `title` | Trả về Status 400 (Bad Request). | ❌ FAIL |
| TC_04 | Mobile UI | Test hiển thị Responsive | 1. Mở web trên độ phân giải iPhone 12 Pro (Width: 390px) | Giao diện không bị tràn, chữ đọc rõ. | ✅ PASS |