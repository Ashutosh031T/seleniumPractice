from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
import time

driver_path = "./msedgedriver.exe"
service_obj = Service(driver_path)
driver_obj = webdriver.Edge(service=service_obj)
driver_obj.get("http://172.20.200.15:5501/index.html")
driver_obj.maximize_window()
time.sleep(2)
coursename = driver_obj.find_elements(By.CLASS_NAME,"radio_btn")
coursename[2].click()
time.sleep(2)
userVehicle1 =driver_obj.find_element(By.ID,"vehicle2")
userVehicle1.click()
time.sleep(2)
userVehicle2 =driver_obj.find_element(By.ID,"vehicle3")
userVehicle2.click()
time.sleep(2)
div = driver_obj.find_element(By.ID,"textDiv")
print(div.text)
time.sleep(2)
selectBus = driver_obj.find_element(By.XPATH,"/html/body/div[2]/select/option[3]")
selectBus.click()
time.sleep(2)
btn1=driver_obj.find_element(By.ID,'alert').click()
time.sleep(5)
alert = driver_obj.switch_to.alert
time.sleep(1)
alert.send_keys("Hello Python")
time.sleep(2)
alert.accept()
# alert.dismiss()
time.sleep(2)
btn2 = driver_obj.find_element(By.ID,'delay_alert').click()
# time.sleep(7)
wait=WebDriverWait(driver_obj,10)
alert2= wait.until(EC.alert_is_present())
# alert2 = driver_obj.switch_to.alert
alert2.send_keys("Welcome to Selenium")
alert2.accept()
time.sleep(2)
# alert2.accept()
# time.sleep(3)
# linkText = driver_obj.find_element(By.LINK_TEXT,"Redirect to drag&drop page")
# linkText.click()
linkText = driver_obj.find_element(By.LINK_TEXT,"Redirect link page") 


# /html/body/div[2]/select/option[1]