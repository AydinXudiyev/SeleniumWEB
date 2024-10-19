import selenium 
from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver import Chrome 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select 
from selenium.webdriver.support import expected_conditions 
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.alert import Alert
from time import sleep
import os
service=Service(executable_path="./chromedriver.exe")
driver=webdriver.Chrome(service=service)
driver.maximize_window()
#driver.implicitly_wait(30)
driver.get("https://the-internet.herokuapp.com/javascript_alerts")

button2=driver.find_element(By.XPATH,"(//button)[3]")
button2.click()
WebDriverWait(driver,3).until(expected_conditions.alert_is_present())
alert=Alert(driver)
sleep(1)
alert.send_keys("selenium alert test")
message=alert.text
alert.accept()
sleep(2)
result=driver.find_element(By.ID,"result").text
print("message: ",message)
print("result: ",result)
driver.quit()

