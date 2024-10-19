from selenium import webdriver 
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
service=Service(executable_path="./chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.implicitly_wait(15)
driver.get("https://www.ucuzabilet.com/")

nereden=driver.find_element(By.ID,"from_text")
nereden.send_keys("Avust")
sleep(2)
element=driver.find_element(By.XPATH,"//*[@id='ui-id-7']/li[3]")
element.click()
sleep(2)
#driver.find_element(By.CSS_SELECTOR,"#ui-id-7 > li:nth-child(3)")
driver.quit()

#twillo - AydinN070402#.@/












#driver.get("https://demoqa.com/droppable/")
