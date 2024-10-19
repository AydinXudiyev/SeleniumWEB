from selenium import webdriver 
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By
from time import sleep

# Start the ChromeDriver service
service = Service(executable_path="./chromedriver.exe")

# Create a new instance of the Chrome WebDriver
driver = webdriver.Chrome(service=service)

# Navigate to DuckDuckGo
driver.get("https://duckduckgo.com")

# Find the search box using its ID
search_box = driver.find_element(By.ID, "searchbox_input")

# Type 'Selenium' into the search box
search_box.send_keys("Selenium") 

# Wait for 2 seconds
sleep(2)

# Press the Enter key to submit the search
search_box.send_keys(Keys.ENTER)

# Wait for 5 seconds to see the results
sleep(5)

# Close the browser (optional)
driver.quit()