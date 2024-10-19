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
driver.get("https://tomspizzeria.b4a.app/")

def Siparis():
    driver.find_element(By.ID,"siparis").click()

def Mesaj():
    return driver.find_element(By.ID,"mesaj").text

name="Aydin Khudiyev"
driver.find_element(By.ID,"musteri-adi").send_keys(name)
Siparis()
mesaj=Mesaj()
assert mesaj=="Pizza boyu seçmediniz"

driver.find_element(By.CSS_SELECTOR,"input[value='Küçük']").click()
Siparis()
mesaj=Mesaj()
assert mesaj=="Ödeme tipi seçmediniz"

zeytin=driver.find_element(By.CSS_SELECTOR,"input[value='zeytin']").click()
mantar=driver.find_element(By.CSS_SELECTOR,"input[value='mantar']").click()

dropdown=driver.find_element(By.ID,"odeme-tipi")
odeme=Select(dropdown)
odeme.select_by_index(3)
Siparis()
mesaj=Mesaj()

assert mesaj=="Siparişiniz alındı"
sleep(2)
SipText=driver.find_element(By.ID,"siparis-detay")
print(SipText.text)
musteri=driver.find_element(By.ID,"musteri").text
boy=driver.find_element(By.ID,"pizzaboyu").text
ek=driver.find_element(By.ID,"pizzaustu").text
odeme=driver.find_element(By.ID,"odeme").text
tutar=driver.find_element(By.ID,"tutar").text 
sleep(2)
assert musteri=="Müşteri ismi: "+ name 
assert boy=="Pizza boyu: Küçük"
assert ek=="Pizza üstü: zeytin, mantar"
assert odeme=="Ödeme tipi: Yemek Kartı"
assert tutar=="Tutar: 11 TL"

driver.execute_script("window.scrollBy(0,150)")
sleep(2)
driver.execute_script("window.scrollBy(0,-150)")
screenshot_path = os.path.join(os.getcwd(), "netice.png")
driver.save_screenshot(screenshot_path)