#©tommie1236 2022
#just a simple magister api
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

SCHOOL_NAME = "passie" #School name 
STUDENT_NUMBER = "36006" #Student number
USER_PASSWORD = "MS3548to" #Magister password 

driver = webdriver.Chrome()  # Optional argument, if not specified will search path.
driver.get("https://www.google.com")

try: 
    driver.find_element(By.XPATH, '//*[@id="L2AGLb"]').click()
    print("google tos passed")
except:
    print("no google tos :)")

driver.get("https://accounts.magister.net")

school = driver.find_element(By.ID, "scholenkiezer_value")
school.send_keys(SCHOOL_NAME)
school.submit()

student = driver.find_element(By.ID, "username")
student.send_keys(STUDENT_NUMBER)
student.submit()

password = driver.find_element(By.ID, "password")
password.send_keys(USER_PASSWORD)
password.submit()

time.sleep(15) 

driver.quit()