from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 

driver = webdriver.Chrome()
driver.get("https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php")
driver.maximize_window()
time.sleep(2)

loginBtn = driver.find_element(By.XPATH,'//a[@href="login.php"]').click()
time.sleep(2)

newUser = driver.find_element(By.XPATH,"//a[@type='submit']").click()
time.sleep(1)

firstname = "Muttaki"
lastName = "Abbas"
Username = "abbas123"
password = "Abbas@123"

email = "abbas@gmail.com"
passowrd = "Abbas@1232323"

firstnameField = driver.find_element(By.ID,"firstname").send_keys(firstname)
time.sleep(1)

lastNameField = driver.find_element(By.ID,"lastname").send_keys(lastName)
time.sleep(1)

usernameField = driver.find_element(By.ID,"username").send_keys(Username)
time.sleep(1)

passowrdField = driver.find_element(By.ID,"password").send_keys(password)
time.sleep(1)

registerbtn = driver.find_element(By.XPATH,"//input[@type='submit']").click()
time.sleep(2)

backtologin = driver.find_element(By.XPATH,"//a[@type='submit']").click()
time.sleep(2)

emailField = driver.find_element(By.ID,'email').send_keys(email)
time.sleep(1)

passwordField = driver.find_element(By.ID,'password').send_keys(passowrd)
time.sleep(1)

login = driver.find_element(By.XPATH,'//input[@value="Login"]').click()
time.sleep(1)

form = driver.find_element(By.ID,'headingTwo').click()
time.sleep(1)

