import selenium 
from selenium.webdriver.chrome.service import Service 
from selenium import webdriver 
from selenium.webdriver.common.by import By
import time
service=Service(executable_path="./chromedriver.exe")
driver=webdriver.Chrome(service=service)
# driver.get("https://the-internet.herokuapp.com/login")
# # login=driver.find_element(By.ID,"username")
# # login.send_keys("tomsmith")
# # password=driver.find_element(By.ID,"password")
# # password.send_keys("SuperSecretPassword!")
# # driver.find_element(By.CSS_SELECTOR,"#login > button").click()
# # time.sleep(2)
# driver.maximize_window()
# driver.find_element(By.ID,"username").send_keys("test")
# driver.find_element(By.ID,"password")
# driver.find_element(By.CSS_SELECTOR,"#login > button").click()
# mesaj1=driver.find_element(By.ID,"flash").text

# if "Your username is invalid!" in mesaj1:
#     print("OK,yanlis istifadeci adi duzgun calisir")
# else:
#     print("XETA,yanlis istifadeci adi yanlis calisir")
# print(mesaj1)

# driver.find_element(By.ID,"username").send_keys("tomsmith")
# driver.find_element(By.ID,"password")
# driver.find_element(By.CSS_SELECTOR,"#login > button").click()
# mesaj2=driver.find_element(By.ID,"flash").text

# if "Your password is invalid!" in mesaj2:
#     print("OK,dogru istifadeci adi duzgun calisir")
# else:
#     print("XETA,dogru istifadeci adi yanlis calisir")

# print(mesaj2)
# driver.find_element(By.ID,"username").send_keys("tomsmith")
# driver.find_element(By.ID,"password").send_keys("tested")
# driver.find_element(By.CSS_SELECTOR,"#login > button").click()
# mesaj3=driver.find_element(By.ID,"flash").text

# if "Your password is invalid!" in mesaj3:
#     print("OK,yanlis sifre duzgun calisir")
# else:
#     print("XETA,yanlis sifre duzgun calisirmir")

# print(mesaj3)
# driver.find_element(By.ID,"username").send_keys("tomsmith")
# driver.find_element(By.ID,"password").send_keys("SuperSecretPassword!")
# driver.find_element(By.CSS_SELECTOR,"#login > button").click()
# mesaj=driver.find_element(By.ID,"flash").text
# #You logged into a secure area!

# if "You logged into a secure area!" in mesaj:
#     print("OK,dogru sifre duzgun calisir")
# else:
#     print("XETA,dogru sifre duzgun calisirmir")

# print(mesaj)
# link=driver.current_url 
# if "secure" in link:
#     print("linkde secure var")
# else:
#     print("linkde secure yoxdur")

# dogrulama_mesaji=driver.find_element(By.CSS_SELECTOR,"#content > div > h2").text

# if "Secure Area" in dogrulama_mesaji:
#     print("OK,Seyfe basligi dogrudur")
# else:
#     print("XETA,Seyfe basligi yanlisdir")

# driver.find_element(By.CSS_SELECTOR,"#content > div > a").click()

# if "login" in driver.current_url:
#     print("OK,Login seyfesine geri donduk.")
# else:
#     print("XETA,Login seyfesine geri done bilmedik.")
# driver.quit()

def login(username,password):
    driver.get("https://the-internet.herokuapp.com/login")
    driver.find_element(By.ID,"username").send_keys(username)
    driver.find_element(By.ID,"password").send_keys(password)
    driver.find_element(By.CSS_SELECTOR,"#login > button").click()
    mesaj=driver.find_element(By.ID,"flash").text
    return mesaj

mesaj=login("sdsd","xyzd")
if "Your username is invalid!" in mesaj:
    print("OK,yanlis istifadeci adi duzgun calisir")
else:
    print("XETA,yanlis istifadeci adi yanlis calisir")
# assert "Your username is invalid!" in mesaj
mesaj=login("tomsmith","adada")
if "Your password is invalid!" in mesaj:
    print("OK,dogru istifadeci adi duzgun calisir")
else:
    print("XETA,dogru istifadeci adi yanlis calisir")
# assert "Your password is invalid!" in mesaj
mesaj=login("tomsmith","SuperSecretPassword!")


if "You logged into a secure area!" in mesaj:
    print("OK,dogru sifre duzgun calisir")
else:
    print("XETA,dogru sifre duzgun calisirmir")
# assert "You logged into a secure area!" in mesaj

def check_link_and_message(expected_text, css_selector):
    link = driver.current_url
    mesaj = driver.find_element(By.CSS_SELECTOR, css_selector).text
    print(f"{'OK' if expected_text in mesaj else 'XETA'}, linkdə '{expected_text}' {'var' if expected_text in link else 'yoxdur'}")
    return link

def navigate_to_login():
    driver.find_element(By.CSS_SELECTOR, "#content > div > a").click()
    print(f"{'OK' if 'login' in driver.current_url else 'XETA'}, Login səhifəsinə geri {'dondük' if 'login' in driver.current_url else 'döne bilmedik'}.")

link = check_link_and_message("secure", "#content > div > h2")

navigate_to_login()

driver.quit()
