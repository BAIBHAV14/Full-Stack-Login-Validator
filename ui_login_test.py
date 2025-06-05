from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://example.com/login")

driver.find_element(By.ID, "username").send_keys("test_user")
driver.find_element(By.ID, "password").send_keys("secure_password")
driver.find_element(By.ID, "login-btn").click()

time.sleep(2)
assert "dashboard" in driver.current_url
driver.quit()
