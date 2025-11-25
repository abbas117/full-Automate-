from selenium import webdriver
from selenium.webdriver.common.by import By

import time 

driver = webdriver.Chrome()
driver.get("https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php")
driver.maximize_window()
time.sleep(1)

element = driver.find_element(By.ID,"headingOne").click()
time.sleep(3)

textBox = driver.find_element(By.XPATH,"//a[@href='text-box.php']").click()
time.sleep(3)

fullname = driver.find_element(By.ID , "fullname")
fullname.click()
fullname.send_keys("Muttaqui Abbas")
time.sleep(1)

email_address = driver.find_element(By.ID , "email")
email_address.click()
email_address.send_keys("muttaquiabbas20@gmail.com")
time.sleep(1)

address = driver.find_element(By.ID , "address")
address.click()
address.send_keys("my home")
time.sleep(1)

password = driver.find_element(By.ID , "password")
password.click()
password.send_keys("India")
time.sleep(1)

submit = driver.find_element(By.XPATH , '//input[@type = "submit"]')
submit.click()
time.sleep(1)

driver.close()


