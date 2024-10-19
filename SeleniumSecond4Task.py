from selenium import webdriver 
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.service import Service 
import time
service=Service(executable_path="./chromedriver.exe")
driver=webdriver.Chrome(service=service)
driver.get("https://www.duckduckgo.com") 
selectbox=driver.find_element(By.NAME,"q")
selectbox.send_keys("Selenium")
time.sleep(2)
driver.find_element(By.CSS_SELECTOR,"#searchbox_homepage > div > div > div").click()
##r1-1 > div.ikg2IXiCD14iVX7AdZo1 > h2 > a > span
driver.find_element(By.ID,"r1-2").click()
time.sleep(5)