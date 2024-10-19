import selenium 
from selenium import webdriver   
from selenium.webdriver.chrome.service import Service 
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://www.fifa.com/")
sleep(2)
driver.quit()