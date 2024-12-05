from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import time

driver_path = r"D:\Users\2721338\Desktop\DevOps-Session\Selenium_Testing\Chrome\chromedriver.exe"
service_obj = Service(driver_path)

driver = webdriver.Chrome(service=service_obj)
driver.get("http://172.20.200.15:5501/index.html")
time.sleep(3)
driver.maximize_window()
time.sleep(3)
# radio_btn = driver.find_elements(By.CLASS_NAME,'radio_btn')
# radio_btn[1].click()
# time.sleep(4)

# vehicle1 = driver.find_element(By.ID,'vehicle2')
# vehicle2 = driver.find_element(By.ID,'vehicle3')
# vehicle1.click()
# time.sleep(2)
# vehicle2.click()
# time.sleep(2)

# dropdown =  Select(driver.find_element(By.ID,'cars'))
# dropdown.select_by_index(2)
# time.sleep(2)

# alert_btn1 = driver.find_element(By.ID,'alert').click()
# time.sleep(4)
# alert1 = driver.switch_to.alert
# time.sleep(2)
# alert1.send_keys("Welcome to Selenium")
# alert1.accept()

# alert_btn2 = driver.find_element(By.ID,'delay_alert').click()
# wait = WebDriverWait(driver,10)
# alert2 = wait.until(EC.alert_is_present())
# alert2.send_keys("Hi Ignite")
# time.sleep(2)
# alert2.accept()
# time.sleep(2)

country_info = driver.find_element(By.PARTIAL_LINK_TEXT,'Redirect to Country').click()
time.sleep(3)

driver.switch_to.window(driver.window_handles[1])
time.sleep(2)
# dropdown = Select(driver.find_element(By.ID,'pageSize'))
# time.sleep(2)
# hv_element = driver.find_element(By.ID,'hoverDiv')
# hv_action = ActionChains(driver)
# hv_action.move_to_element(hv_element).perform()
# time.sleep(2)
# data1 = driver.find_element(By.LINK_TEXT,'Data 1')
# data1.click()
# time.sleep(2)
# alert=driver.switch_to.alert
# alert.accept()
# time.sleep(2)
# upload_file = driver.find_element(By.ID,'uploadFile')
# file_path = r"D:\Users\2721338\Desktop\DevOps-Session\Selenium_Testing\Edge"
# upload_file.send_keys(file_path)
# time.sleep(5)

driver.close()

driver.switch_to.window(driver.window_handles[0])
time.sleep(4)

drag_drop=driver.find_element(By.CSS_SELECTOR,'a[href="/drag.html"]').click()
time.sleep(3)

driver.switch_to.window(driver.window_handles[1])
time.sleep(2)

base_div = driver.find_element(By.ID,'dragFrom')
target_div = driver.find_element(By.ID,'dropzone')

drag_action = ActionChains(driver)
drag_action.drag_and_drop(base_div,target_div).perform()
time.sleep(3)

driver.close()

driver.switch_to.window(driver.window_handles[0])
time.sleep(3)

input("Press Enter to close")

driver.quit()

