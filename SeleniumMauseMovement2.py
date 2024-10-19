from selenium import webdriver 
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
service=Service(executable_path="./chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--disable-web-security')
options.add_argument('--allow-running-insecure-content')
driver = webdriver.Chrome(service=service, options=options)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://crossbrowsertesting.github.io/drag-and-drop")

source=driver.find_element(By.ID,"draggable") #"//*[@id='draggable']"
target=driver.find_element(By.ID,"droppable") #
print("before:",target.text)
action=ActionChains(driver)
action.drag_and_drop(source,target).perform()
sleep(2)
print("after:",target.text)
sleep(2)


#twillo - AydinN070402#.@/












#driver.get("https://demoqa.com/droppable/")
