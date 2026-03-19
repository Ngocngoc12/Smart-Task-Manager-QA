import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def test_giao_dien_mobile_responsive():
    """Test Case: Kiểm tra web hiển thị trên màn hình điện thoại"""
    chrome_options = Options()
    
    # Bật chế độ giả lập iPhone X
    mobile_emulation = { "deviceName": "iPhone X" }
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    # Tạm tắt headless để nhìn cho rõ
    # chrome_options.add_argument("--headless") 
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    
    print("\n[Mobile Test] Dang mo trang web tren giao dien iPhone X...")
    
    # ĐÃ ĐỔI URL: Dùng trang Github (Hỗ trợ mobile cực tốt) để test
    driver.get("https://github.com/")
    time.sleep(3) 
    
    inner_width = driver.execute_script("return window.innerWidth;")
    
    assert inner_width <= 430, f"Loi: Kich thuoc trang web dang la {inner_width}px, khong phai mobile!"
    
    print("[Mobile Test] => PASSED: Responsive hien thi rat tot!")
    driver.quit()