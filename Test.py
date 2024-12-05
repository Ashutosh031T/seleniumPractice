from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

driver_path = r"D:\chromedriver-win64\chromedriver.exe"
serve = Service(driver_path)

driver = webdriver.Chrome(service=serve)

driver.get("https://www.saucedemo.com/")
driver.maximize_window()
time.sleep(4)

username = driver.find_element(By.ID,'user-name').send_keys("standard_user")
password = driver.find_element(By.ID,'password').send_keys("secret_sauce")
login = driver.find_element(By.ID,'login-button').click()
time.sleep(4)

driver.back()

time.sleep(5)
driver.quit()
