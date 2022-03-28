#©tommie1236 2022
#just a simple magister api
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

SCHOOL_LINK = "" #link to your magister
STUDENT_NUMBER = "" #Student number
USER_PASSWORD = "" #Magister password 

#Uncomment the browser you want to use:
driver = webdriver.Chrome() #Optional argument, if not specified will search path.
#driver = webdriver.Firefox()
#driver = webdriver.Edge()
#driver = webdriver.Safari()

driver.get(SCHOOL_LINK)

time.sleep(1) #decreases the chance of failing

student = driver.find_element(By.ID, "username")
student.send_keys(STUDENT_NUMBER)
student.submit()

time.sleep(1) #decreases the chance of failing

password = driver.find_element(By.ID, "password")
password.send_keys(USER_PASSWORD)
password.submit()
 
print(f"succesfully logged into {SCHOOL_LINK} using {str(STUDENT_NUMBER)}, {USER_PASSWORD}")

time.sleep(5)

driver.get(SCHOOL_LINK+"/magister/#/agenda")

x = input("quit? ")
x.lower()
if x == "y" or "yes":
    driver.quit()