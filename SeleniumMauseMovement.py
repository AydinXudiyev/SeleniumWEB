from selenium import webdriver 
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep

service=Service(executable_path="./chromedriver.exe")

driver=webdriver.Chrome(service=service)
driver.get("https://the-internet.herokuapp.com/hovers")
driver.maximize_window()
user=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"#content > div > div:nth-child(3)")))
name=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"#content > div > div:nth-child(3) > div")))
link=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"#content > div > div:nth-child(3) > div > a")))
print(name.is_displayed())
print("isim"+user.text)
sleep(2)
movement=ActionChains(driver)
movement.move_to_element(user)
movement.perform()

sleep(2)
print("----------")
print(name.is_displayed())
print("isim"+name.text)
link.click()
sleep(2)

url=driver.current_url 
assert  "users/1" in url 

driver.quit()
