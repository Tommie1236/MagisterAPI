#©tommie1236 2022
#just a simple magister api
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def InitApi(school_name, student_number, user_password):
    driver = webdriver.Chrome() #Optional argument, if not specified will search path.
    driver.get("https://www.google.com")

    try: 
        driver.find_element(By.XPATH, '//*[@id="L2AGLb"]').click()
        print("google tos passed")
    except:
        print("no google tos :)")

    driver.get("https://accounts.magister.net")

    time.sleep(1) #decreases the chance of failing

    school = driver.find_element(By.ID, "scholenkiezer_value")
    school.send_keys(school_name)
    school.submit()

    time.sleep(1) #decreases the chance of failing

    student = driver.find_element(By.ID, "username")
    student.send_keys(student_number)
    student.submit()

    time.sleep(1) #decreases the chance of failing

    password = driver.find_element(By.ID, "password")
    password.send_keys(user_password)
    password.submit()
    
    print("succesfully logged into magister.net using "+school_name+", "+str(student_number)+", "+user_password)
    time.sleep(15)

InitApi("your school",your_number,"your password")