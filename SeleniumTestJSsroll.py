import selenium 
from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver import Chrome 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select 
from time import sleep
import os
service=Service(executable_path="./chromedriver.exe")
driver=webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://www.harpersbazaar.com/uk/travel/g60211654/most-beautiful-places-in-the-worl1/")
driver.execute_script("window.scrollBy(0,300)")
sleep(3)
driver.execute_script("window.scrollBy(0,3000)")
sleep(3)
Lucia=driver.find_element(By.XPATH,"//h2[text()='Pitons, St Lucia']")
#driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
driver.execute_script("arguments[0].scrollIntoView()",Lucia)
sleep(3)
driver.execute_script("window.scrollBy(0,-200)")
sleep(3)
driver.quit()
