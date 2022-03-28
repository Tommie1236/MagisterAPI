#©tommie1236 2022
#just a simple magister api
from selenium import webdriver
from selenium.webdriver.common.by import By
import asyncio
import time

async def InitApi(link_to_your_magister, student_number, user_password):
    driver = webdriver.Chrome() #Optional argument, if not specified will search path.
    driver.get("https://www.google.com")

    try: 
        driver.find_element(By.XPATH, '//*[@id="L2AGLb"]').click()
        print("google tos passed")
    except:
        print("no google tos :)")

    driver.get(link_to_your_magister)

    time.sleep(1) #decreases the chance of failing

    student = driver.find_element(By.ID, "username")
    student.send_keys(student_number)
    student.submit()

    time.sleep(1) #decreases the chance of failing

    password = driver.find_element(By.ID, "password")
    password.send_keys(user_password)
    password.submit()
    
    print("succesfully logged into", link_to_your_magister +"using"+str(student_number)+", "+user_password)
    
    while True:
        time.sleep(1)

async def QuitApi():
    driver.quit()

# InitApi("link to your magister.net",student_number,"password")
