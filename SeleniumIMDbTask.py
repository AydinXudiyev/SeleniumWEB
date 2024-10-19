from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

service = Service(executable_path="./chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://www.imdb.com/")
wait=WebDriverWait(driver,10)

wait.until(EC.element_to_be_clickable((By.ID, "imdbHeader-navDrawerOpen"))).click()

wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='imdbHeader']/div[2]/aside[1]/div/div[2]/div/div[1]/span/div/div/ul/a[2]/span"))).click()

film_list = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//*[@id='__next']/main/div/div[3]/section/div/div[2]/div/ul/li")))

for i in range(min(20, len(film_list))):  
    film_info = film_list[i].text.split("\n")
    if len(film_info) > 1:
        film_name = film_info[0]
        film_year_info = film_info[1].strip()
        try:
            if '–' in film_year_info:
                film_year = film_year_info.split('–')[0].strip()
            else:
                film_year = film_year_info
            film_year_int = int(film_year)
            if film_year_int == 2002:
                print(f"{film_name} {film_year_int}")
        except ValueError:
            print(f"{film_name}: İl tapılmadı.")
sleep(3) 
driver.quit()





# for i in range(min(20,len(film))):
#   film_list=film_list[0].text.split("\n")
#   if len(film_list)>1:
#       film_name=film_list[0]
#       film_year_info=film_list[1].strip()
#       try:
#           if "-" in film_date:
#               film_year=film_date.split("-")[0].strip()
#           else:
#               film_year = film_year_info
#       film_year_int=int(film_year)   
#       if film_year_int==1998:
#           print(f"{film_name}","{film_year_int}")
#       except ValueError:
#       print("Il yoxdu")                 
