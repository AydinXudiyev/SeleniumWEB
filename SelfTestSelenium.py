from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from time import sleep

# SSL hatalarını göz ardı etme
chrome_options = Options()
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--ignore-ssl-errors')

# WebDriver ayarları
service = Service(executable_path="./chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get("https://www.tamgame.com/")

# İlgili elemente kaydırma işlemi ve tıklama
tamgame = driver.find_element(By.CSS_SELECTOR, "#container > section.news_banner > div > div.left_banner > div > a")
driver.execute_script("arguments[0].scrollIntoView()", tamgame)
sleep(2)

# Tıklama işlemi
tamgame.click()

# Sayfanın tamamen yüklenmesini bekle
WebDriverWait(driver, 30).until(lambda d: d.execute_script("return document.readyState") == "complete")

# Yeni sayfanın yüklenmesini bekle ve elementleri bul
WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, "//*[@id='tab_klan']/ul/li[@class='tit_last_on']")))

# Şu anki URL'i al ve yazdır
c_driver = driver.current_url
print(f"Current URL: {c_driver}")

# Klanlar listesini bul ve yazdır
klanlar = driver.find_elements(By.CSS_SELECTOR, "#tab_klan > ul > li.tit_last_on")
for klan in klanlar:
    print(klan.text)

# Tarayıcıyı kapatma
driver.quit()
