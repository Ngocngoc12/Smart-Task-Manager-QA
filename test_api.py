import pytest
import requests

# Link API giả lập hệ thống Quản lý công việc
BASE_URL = "https://jsonplaceholder.typicode.com/todos"

def test_api_lay_danh_sach_cong_viec():
    """Test Case: Kiểm tra API lấy danh sách Task có hoạt động không"""
    response = requests.get(BASE_URL)
    
    # Kiểm tra Status Code (200 là thành công)
    assert response.status_code == 200, "Lỗi: Server không phản hồi 200"
    
    # Kiểm tra dữ liệu trả về phải có nội dung
    data = response.json()
    assert len(data) > 0, "Lỗi: Danh sách trả về bị trống"

def test_api_tao_cong_viec_moi():
    """Test Case: Kiểm tra API tạo Task mới"""
    payload = {
        "userId": 1,
        "title": "Học Automation Test API",
        "completed": False
    }
    
    response = requests.post(BASE_URL, json=payload)
    
    # Kiểm tra Status Code (201 là Created - Đã tạo mới thành công)
    assert response.status_code == 201
    
    # Xác nhận dữ liệu server trả về khớp với dữ liệu mình đã gửi lên
    response_data = response.json()
    assert response_data["title"] == "Học Automation Test API"