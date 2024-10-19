from selenium import webdriver 
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.service import Service 
import time
service=Service(executable_path="./chromedriver.exe")
driver=webdriver.Chrome(service=service)
driver.get("https://az.wikipedia.org/wiki/Ana_s%C9%99hif%C9%99")
secilmisler=driver.find_element(By.CSS_SELECTOR,"#tfa > div.mainBlockContent > table > tbody > tr > td")
secilmisler_yazisi=secilmisler.text
secilmisler_yazisi=secilmisler_yazisi.split(".")[0]
print("Seçilmişlər yazısı :"+secilmisler_yazisi)
heftenin_en_yaxsisi=driver.find_element(By.CSS_SELECTOR,"#tga > div.mainBlockContent > table > tbody > tr > td")
heftenin_en_yaxsisi_yazisi=heftenin_en_yaxsisi.text
heftenin_en_yaxsisi_yazisi=heftenin_en_yaxsisi_yazisi.split(".")[0]
print("Həftənin ən yaxşısı :"+heftenin_en_yaxsisi_yazisi)
driver.quit()