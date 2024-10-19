from selenium import webdriver 
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By
from time import sleep
service=Service(executable_path="./chromedriver.exe")
driver=webdriver.Chrome(service=service)
driver.get("https://www.duckduckgo.com")
driver.maximize_window()
search_box=driver.find_element(By.ID,"searchbox_input")
search_box.send_keys("Selenium")
sleep(5)
driver.find_element(By.CSS_SELECTOR,"#searchbox_homepage > div > div.searchbox_searchbox__eaWKL > div > button.iconButton_button__6x_9C.searchbox_searchButton__F5Bwq").click()
sleep(10)
driver.quit()