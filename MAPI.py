#©tommie1236 2022
#just a simple magister api
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#You will see some time.sleep() statements on multiple locations if you get an error like this:
#"{"method":"css selector","selector":"[id="username"]"}" 
#Try making the delay before the dirver function a little longer, a second can go a long way.

SCHOOL_LINK = "" #Put your link to your magister here
STUDENT_NUMBER = 00000 #Put your student number here
USER_PASSWORD = "" #Putt your Magister password here

#Uncomment the browser you want to use:     The argument is optional if not specified it will search for path.
driver = webdriver.Chrome() 
#driver = webdriver.Firefox()
#driver = webdriver.Edge()
#driver = webdriver.Safari()

driver.get(SCHOOL_LINK)

time.sleep(1) #decreases the chance of failing. 

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

time.sleep(10)

agenda = driver.find_element(By.XPATH, '//*[@id="afsprakenLijst"]/div[2]/table/tbody/tr[2]/td[3]/span/span[2]')

print(agenda.text)

x = input("quit? ")
x.lower()
if x == "y" or "yes":
    driver.quit()