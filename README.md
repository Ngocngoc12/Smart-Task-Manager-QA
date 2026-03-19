# 📱 Smart Task Manager - QA Automation Project

![CI/CD Status](https://github.com/Ngocngoc12/Smart-Task-Manager-QA/actions/workflows/qa-tests.yml/badge.svg)

## 📌 Giới thiệu dự án
Dự án áp dụng quy trình kiểm thử toàn diện (Manual & Automation) cho nền tảng quản lý công việc (Task Manager), đáp ứng đầy đủ các yêu cầu kiểm thử trên nền tảng Web, Web Services (API) và Thiết bị di động (Mobile Responsive).

## 🛠️ Công nghệ sử dụng
* **Ngôn ngữ:** Python 3.11
* **Testing Framework:** Pytest
* **API Testing:** Thư viện `requests`
* **Mobile UI Automation:** Selenium WebDriver (Sử dụng tính năng Mobile Emulation mô phỏng iPhone X).
* **CI/CD:** GitHub Actions (Tự động hóa luồng chạy test).
* **Manual Testing:** Viết Test Case chuẩn format bằng file Markdown.

## 🎯 Chi tiết các phần kiểm thử
1. **Manual Testing:** Thiết kế file `MANUAL_TEST_CASES.md` cover các luồng nghiệp vụ cơ bản, bao gồm cả Happy Path và Unhappy Path.
2. **Web Services (API) Testing:** Tự động hóa kiểm tra các HTTP Status Code (200, 201, 400) và cấu trúc dữ liệu JSON trả về cho các method `GET` (Lấy danh sách) và `POST` (Tạo mới).
3. **Mobile UI Testing:** Ứng dụng kỹ thuật Custom Mobile Emulation trong Selenium để ép trình duyệt hiển thị chính xác theo độ phân giải của thiết bị di động (iPhone X - 375x812), tự động xác nhận tính năng Responsive của website.
