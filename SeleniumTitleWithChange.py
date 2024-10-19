from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from time import sleep
service=Service(executable_path="./chromedriver.exe")
driver=webdriver.Chrome(service=service)
driver.maximize_window()
driver.implicitly_wait(30)
driver.get("https://tomspizzeria.b4a.app/yeni-sekme.html")
facebook=driver.find_element(By.ID,"facebook").click()
twitter=driver.find_element(By.ID,"twitter").click()
instagram=driver.find_element(By.ID,"instagram").click()
sleep(2)
def change_tab(header):
    for page in driver.window_handles:
        driver.switch_to.window(page)
        if header in driver.title.lower():
            break
change_tab("facebook")
print("facebook: "+driver.title)
change_tab("x")
print("x: "+driver.title)
change_tab("instagram")
print("instagram: "+driver.title)
change_tab("selenium")
print("homepage: "+driver.title)





# sleep(2)
# homepage=driver.window_handles[0]
# facebook=driver.window_handles[1]
# twitter=driver.window_handles[2]
# instagram=driver.window_handles[3]

# driver.switch_to.window(facebook)
# print("facebook:",driver.title)

# driver.switch_to.window(twitter)
# print("twitter:",driver.title)

# driver.switch_to.window(instagram)
# print("instagram:",driver.title)

