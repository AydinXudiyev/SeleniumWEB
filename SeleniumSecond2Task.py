from selenium import webdriver 
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By
from time import sleep
service=Service(executable_path="./chromedriver.exe")
driver=webdriver.Chrome(service=service)
driver.get("https://www.google.com")
search_box=driver.find_element(By.NAME,"q")
search_box.send_keys("Selenium") 
sleep(2)
search_box.send_keys(Keys.ENTER)
sleep(5)