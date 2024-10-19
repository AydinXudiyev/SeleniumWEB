import selenium 
from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select 
from selenium.webdriver.chrome.options import Options 
from time import sleep
import os

# Chrome options configuration
chrome_option = Options()
chrome_option.add_argument("--disable-extensions")
chrome_option.add_argument("--lang=en")  # Set language to English
chrome_option.add_argument("--allow-insecure-localhost")

# Initialize Chrome WebDriver
service = Service(executable_path="./chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_option)
driver.maximize_window()

# Open the specified URL
driver.get("https://tomspizzeria.b4a.app/")

def Siparis():
    """Click the 'Sipariş' button to place an order."""
    driver.find_element(By.ID, "siparis").click()

def Mesaj():
    """Get the message displayed on the page."""
    return driver.find_element(By.ID, "mesaj").text

# Customer name
name = "Aydin Khudiyev"
# Enter the customer name
driver.find_element(By.ID, "musteri-adi").send_keys(name)

# Attempt to place an order without selecting a size
Siparis()
mesaj = Mesaj()
assert mesaj == "Pizza boyu seçmediniz"  # Assert that the correct message is displayed

# Select the pizza size
driver.find_element(By.CSS_SELECTOR, "input[value='Küçük']").click()
Siparis()
mesaj = Mesaj()
assert mesaj == "Ödeme tipi seçmediniz"  # Assert that the correct message is displayed for payment type

# Select toppings
driver.find_element(By.CSS_SELECTOR, "input[value='zeytin']").click()  # Select olives
driver.find_element(By.CSS_SELECTOR, "input[value='mantar']").click()    # Select mushrooms

# Select payment type from the dropdown
dropdown = driver.find_element(By.ID, "odeme-tipi")
odeme = Select(dropdown)
odeme.select_by_index(3)  # Select payment type by index

# Attempt to place an order again
Siparis()
mesaj = Mesaj()
assert mesaj == "Siparişiniz alındı"  # Assert that the order was received

# Take a screenshot of the results
sleep(2)
screenshot_path = os.path.join(os.getcwd(), "results.png")
driver.save_screenshot(screenshot_path)

# Retrieve and print order details
SipText = driver.find_element(By.ID, "siparis-detay")
print(SipText.text)
musteri = driver.find_element(By.ID, "musteri").text
boy = driver.find_element(By.ID, "pizzaboyu").text
ek = driver.find_element(By.ID, "pizzaustu").text
odeme = driver.find_element(By.ID, "odeme").text
tutar = driver.find_element(By.ID, "tutar").text 

# Assertions for order details
sleep(2)
assert musteri == "Müşteri ismi: " + name 
assert boy == "Pizza boyu: Küçük"
assert ek == "Pizza üstü: zeytin, mantar"
assert odeme == "Ödeme tipi: Yemek Kartı"
assert tutar == "Tutar: 11 TL"

sleep(2)
# Close the browser at the end if needed
# driver.quit()
