from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.alert import Alert
from time import sleep
service=Service(executable_path="./chromedriver.exe")
driver=webdriver.Chrome(service=service)
driver.maximize_window()
driver.implicitly_wait(30)
driver.get("https://www.apple.com/")
sleep(3)
print(driver.title)
apple=driver.current_window_handle
driver.switch_to.new_window("tab")
tesla=driver.get("https://www.tesla.com/")
sleep(3)
#driver.switch_to.new_window("window")
print(driver.title)
tesla=driver.window_handles[1]
driver.switch_to.window(apple)
print(driver.title)
sleep(2)
driver.switch_to.window(tesla)
print(driver.title)
sleep(2)
driver.switch_to.window(apple)
print(driver.title)
sleep(1)
driver.quit()

