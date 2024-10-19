from selenium import webdriver 
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
service=Service(executable_path="./chromedriver.exe")

driver=webdriver.Chrome(service=service)

driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/upload")

file=r"c:\Users\User\Pictures\WhatsApp Şəkil 2024-10-11 saat 21.24.36_8b63d5b5.jpg"
file_upload=driver.find_element(By.ID,"file-upload")
sleep(2)
file_upload.send_keys(file)
driver.find_element(By.ID,"file-submit").click()
WebDriverWait(driver,30).until(EC.presence_of_element_located((By.TAG_NAME,"h3")))
header=driver.find_element(By.TAG_NAME,"h3").text
print(header)
document=driver.find_element(By.ID,"uploaded-files").text 
print(document)
sleep(2)
driver.quit()
#File Uploaded! h3
#id uploaded-files