from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import string
import random

chrome_options= Options()
chrome_options.add_experimental_option("excludeSwitches",["enable-automation"])

#Driver selected for WebBrowser
driver_obj = webdriver.Chrome(options=chrome_options)

# IP of the website/webpage
driver_obj.get("https://172.20.200.35:3000/")
time.sleep(4)

driver_obj.maximize_window() # Maximaize the Window Screen

adv_btn0=driver_obj.find_element(By.XPATH,"/html/body/div/div[2]/button[3]")
adv_btn0.click()
time.sleep(2)
linkTEXT0=driver_obj.find_element(By.LINK_TEXT,"Proceed to 172.20.200.35 (unsafe)")
linkTEXT0.click()
time.sleep(2)
driver_obj.execute_script("window.open('https://172.20.200.35:8436/','_blank');") # Opeaning another Ip in a new Tab
time.sleep(2)
driver_obj.switch_to.window(driver_obj.window_handles[1]) # Switching to new tab
adv_btn1=driver_obj.find_element(By.ID,"details-button")
adv_btn1.click()
time.sleep(1)
linkTEXT1=driver_obj.find_element(By.LINK_TEXT,"Proceed to 172.20.200.35 (unsafe)")
linkTEXT1.click()
time.sleep(1)
driver_obj.switch_to.window(driver_obj.window_handles[0]) # Switching tab

#Login Page
username = driver_obj.find_element(By.XPATH,"/html/body/div/div/div/div[1]/div/div[3]/div[1]/div/input")
username.send_keys("2721338@tcs.com")
password=driver_obj.find_element(By.XPATH,"/html/body/div/div/div/div[1]/div/div[3]/div[2]/div/input")
password.send_keys("Tcs#1234")
time.sleep(1)
login_btn=driver_obj.find_element(By.ID,"loginbtn")
login_btn.click()
time.sleep(3)
WORDS = ("Hi! Good Morning","Welcome to Ignite","How was the weekend?","Test is postponed","Welcome to TCS","LOST AND NOT FOUND","After lunch we have session")
channel = driver_obj.find_element(By.CSS_SELECTOR,'a[href="/user/Channel"]')
channel1=1
channel2=1
channel3=1
test_sub_list = ['/html/body/div/div/div[2]/div[2]/div/div[1]/div[2]/div/div/div[2]/div/div/div[1]',
                 '/html/body/div/div/div[2]/div[2]/div/div[1]/div[2]/div/div/div[2]/div/div/div[2]',
                 '/html/body/div/div/div[2]/div[2]/div/div[1]/div[2]/div/div/div[2]/div/div/div[3]',
                 '/html/body/div/div/div[2]/div[2]/div/div[1]/div[2]/div/div/div[2]/div/div/div[4]',
                 '/html/body/div/div/div[2]/div[2]/div/div[1]/div[2]/div/div/div[2]/div/div/div[5]',
                 '/html/body/div/div/div[2]/div[2]/div/div[1]/div[2]/div/div/div[2]/div/div/div[6]',
                 '/html/body/div/div/div[2]/div[2]/div/div[1]/div[2]/div/div/div[2]/div/div/div[7]',
                 '/html/body/div/div/div[2]/div[2]/div/div[1]/div[2]/div/div/div[2]/div/div/div[8]',
                 '/html/body/div/div/div[2]/div[2]/div/div[1]/div[2]/div/div/div[2]/div/div/div[9]',
                 '/html/body/div/div/div[2]/div[2]/div/div[1]/div[2]/div/div/div[2]/div/div/div[10]']
ts = len(test_sub_list)
channel.click()
time.sleep(2)
try:
    channel1= driver_obj.find_element(By.XPATH,"/html/body/div/div/div[2]/div[2]/div/div[1]/div[2]/div/div/div[1]/a/span/div/span")
except:
    channel1 = None
try:
    channel2 = driver_obj.find_element(By.XPATH,"/html/body/div/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/div/a/span/div")
except:
    channel2=None
try:
    channel3=driver_obj.find_element(By.XPATH,"/html/body/div/div/div[2]/div[2]/div/div[1]/div[2]/div[3]/div/div[1]/a/span/div")
except:
    channel3=None
    actual_sub_list1 = []
actual_sub_list2 = []
actual_sub_list3 = []
if channel1 is not None:
    channel1.click()
    c=0
    sub=1
    for c in range(0,ts):
        try:
            subchannel = driver_obj.find_element(By.XPATH,test_sub_list[c])
        except:
            sub = None
        if sub is not None:
            actual_sub_list1.append(test_sub_list[c])
        else:
            sub= 1
            continue
    al1=len(actual_sub_list1)
    e=0
    for e in range(0,al1):
        subchannel = driver_obj.find_element(By.XPATH,actual_sub_list1[e])
        subchannel.click()
        time.sleep(2)
        sub_text = subchannel.text
        test_txt = subchannel.text
        # res = ''.join(random.choices(string.ascii_letters,k=7))
        res=random.choice(WORDS)
        if sub_text==test_txt:
            for i in range(1):
                input_msg = driver_obj.find_element(By.ID,'subchannelinput')
                input_msg.send_keys(f"{res}")
                time.sleep(3)
                send_btn = driver_obj.find_element(By.ID,'send')
                send_btn.click()
                time.sleep(2)
        
        time.sleep(1)
    channel1.click()
    time.sleep(2)
# driver_obj.refresh()
time.sleep(2)
test_sub_list2 = ['/html/body/div/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/div[2]/div/div/div[1]',
                 '/html/body/div/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/div[2]/div/div/div[2]',
                 '/html/body/div/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/div[2]/div/div/div[3]',
                 '/html/body/div/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/div[2]/div/div/div[4]',
                 '/html/body/div/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/div[2]/div/div/div[5]',
                 '/html/body/div/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/div[2]/div/div/div[6]',
                 '//html/body/div/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/div[2]/div/div/div[7]',
                 '//html/body/div/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/div[2]/div/div/div[8]',
                 '/html/body/div/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/div[2]/div/div/div[9]',
                 '/html/body/div/div/div[2]/div[2]/div/div[1]/div[2]/div[2]/div/div[2]/div/div/div[10]']
ts2 = len(test_sub_list2)
if channel2 is not None:
    channel2.click()
    time.sleep(2)
    c=0
    sub=1
    for c in range(0,ts2):
        try:
            subchannel = driver_obj.find_element(By.XPATH,test_sub_list2[c])
        except:
          sub = None
        if sub is not None:
            actual_sub_list2.append(test_sub_list2[c])
        else:
            sub= 1
            continue
    al2=len(actual_sub_list2)
    e=0
    for e in range(0,al2):
        subchannel = driver_obj.find_element(By.XPATH,actual_sub_list2[e])
        subchannel.click()
        time.sleep(2)
        sub_text = subchannel.text
        test_txt = subchannel.text
        # res = ''.join(random.choices(string.ascii_letters,k=7))
        res = random.choice(WORDS)
        if sub_text==test_txt:
            if test_txt=='Python / Python CCIP':
                test_txt='Python'
            elif test_txt=='SpringBoot / SpringBoot CCIP':
                test_txt='SpringBoot'
            print(subchannel.text)
            print(f"{test_txt}")
            for i in range(1):
                input_msg = driver_obj.find_element(By.ID,'subchannelinput')
                input_msg.send_keys(f"{res}")
                time.sleep(2)
                send_btn = driver_obj.find_element(By.ID,'send')
                send_btn.click()
                time.sleep(2)
    time.sleep(2)
    channel2.click()
# driver_obj.refresh()
time.sleep(2)
test_sub_list3=['/html/body/div/div/div[2]/div[2]/div/div[1]/div[2]/div[3]/div/div[2]/div/div/div[1]',
                '/html/body/div/div/div[2]/div[2]/div/div[1]/div[2]/div[3]/div/div[2]/div/div/div[2]',
                '/html/body/div/div/div[2]/div[2]/div/div[1]/div[2]/div[3]/div/div[2]/div/div/div[3]',
                '/html/body/div/div/div[2]/div[2]/div/div[1]/div[2]/div[3]/div/div[2]/div/div/div[4]',
                '/html/body/div/div/div[2]/div[2]/div/div[1]/div[2]/div[3]/div/div[2]/div/div/div[5]',
                '/html/body/div/div/div[2]/div[2]/div/div[1]/div[2]/div[3]/div/div[2]/div/div/div[6]',
                '/html/body/div/div/div[2]/div[2]/div/div[1]/div[2]/div[3]/div/div[2]/div/div/div[7]',
                '/html/body/div/div/div[2]/div[2]/div/div[1]/div[2]/div[3]/div/div[2]/div/div/div[8]',
                '/html/body/div/div/div[2]/div[2]/div/div[1]/div[2]/div[3]/div/div[2]/div/div/div[9]',
                '/html/body/div/div/div[2]/div[2]/div/div[1]/div[2]/div[3]/div/div[2]/div/div/div[10]']
ts3=len(test_sub_list3)
if channel3 is not None:
    channel3.click()
    c=0
    sub=1
    for c in range(0,ts3):
        try:
            subchannel = driver_obj.find_element(By.XPATH,test_sub_list3[c])
        except:
          sub = None
        if sub is not None:
            actual_sub_list3.append(test_sub_list3[c])
        else:
            sub= 1
            continue
    al3=len(actual_sub_list3)
    e=0
    for e in range(0,al3):
        subchannel = driver_obj.find_element(By.XPATH,actual_sub_list3[e])
        subchannel.click()
        time.sleep(2)
        sub_text = subchannel.text
        test_txt = subchannel.text
        res = ''.join(random.choices(string.ascii_letters,k=7))
        if sub_text==test_txt:
            if test_txt=='Python / Python CCIP':
                test_txt='Python'
            elif test_txt=='SpringBoot / SpringBoot CCIP':
                test_txt='SpringBoot'
            # print(subchannel.text)
            # print(f"{test_txt}")
            for i in range(1):
                input_msg = driver_obj.find_element(By.ID,'subchannelinput')
                input_msg.send_keys(f"{res}")
                time.sleep(2)
                send_btn = driver_obj.find_element(By.ID,'send')
                send_btn.click()
                time.sleep(2)
    time.sleep(2)
    channel3.click()
    time.sleep(2)
driver_obj.back()
time.sleep(2)
schedule = driver_obj.find_element(By.CSS_SELECTOR,'a[href="/user/Schedule"]')
schedule.click()
time.sleep(1)
agenda = driver_obj.find_element(By.XPATH,'//button[text()="Agenda"]')
agenda.click()
time.sleep(1)
week = driver_obj.find_element(By.XPATH,'//button[text()="Week"]')
week.click()
time.sleep(3)
driver_obj.back()
driver_obj.back()
time.sleep(3)
driver_obj.quit()