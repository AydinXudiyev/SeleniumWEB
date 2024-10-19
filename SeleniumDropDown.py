import selenium 
from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver import Chrome 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select 
from time import sleep
service=Service(executable_path="./chromedriver.exe")
driver=webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://tomspizzeria.b4a.app/")
dropdown=driver.find_element(By.ID,"odeme-tipi")
odeme=Select(dropdown)
odeme_tipler=odeme.options # web element listi, her biri option tagi 
for tip in odeme_tipler:
    print(tip.text)
sleep(2)
odeme.select_by_visible_text("Kredi Kartı")
sleep(2)
odeme.select_by_index(3)
sleep(2)