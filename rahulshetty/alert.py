from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

alert_field = driver.find_element(By.ID,'name')
alert_field.click()
alert_field.send_keys("Abbas")
time.sleep(1)

alert_btn = driver.find_element(By.ID,"alertbtn")
alert_btn.click()
time.sleep(1)

alert = driver.switch_to.alert
print(alert.text)
alert.accept()

time.sleep(2)

confirmbtn = driver.find_element(By.ID,"confirmbtn").click()
print(alert.text)
alert.dismiss()
time.sleep(2)
