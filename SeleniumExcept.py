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
driver.get("https://pynishant.github.io/Selenium-python-waits.html")
tryit=driver.find_element(By.XPATH,"//button[contains(text(),'Try it')]").click()
#WebDriverWait(driver,45).until(expected_conditions.presence_of_element_located(By.XPATH,"//button[contains(text(),'CLICK ME')]"))
wait = WebDriverWait(driver, 45, poll_frequency=1, ignored_exceptions=[NotImplementedError, ModuleNotFoundError])
click_me_button = wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//button[contains(text(),'CLICK ME')]")))


#implicit wait- gizli gözləmə 
#explicit wait -aşkar gözləmə
