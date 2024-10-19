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
driver.implicitly_wait(30)
driver.get("https://www.apple.com/")
sleep(3)
driver.switch_to.new_window("tab")
sleep(3)
#driver.switch_to.new_window("window")
driver.get("https://www.tesla.com/")
driver.quit()

