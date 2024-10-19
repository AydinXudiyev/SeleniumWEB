from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
service=Service(executable_path="./chromedriver.exe")
driver=webdriver.Chrome(service=service)
driver.get("https://www.apple.com")
link=driver.current_url 
header=driver.title
print("başlıq "+ header)
if "apple.com" in link:
    print("that's right, we are on the apple page:"+link)
else:
    print("wrong, we are not on the apple page")
driver.maximize_window()
print("Indiki Başlıq:"+link)
driver.get("https://www.etsy.com")
link=driver.current_url
header=driver.title
driver.save_screenshot("./etsyscreen.png")
print("başlıq "+ header)
if "etsy.com" in link:
    print("that's right, we are on the etsy page:"+link)
else:
    print("wrong, we are not on the etsy page")
driver.maximize_window()
driver.back()
header=driver.title
driver.save_screenshot("./ekrangoruntusu.png")
if "Apple" in header:
    print("Go to Apple")
#else:
    #driver.save_screenshot("./ekrangoruntusu.png")
driver.quit()

#driver.close() --> axrinci səhifə hansıdırsa onu bağlar.
#driver.quit() --> Seleniumdakı bütün səhifələri bağlayır.

