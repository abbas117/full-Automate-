from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

checkBoxes = driver.find_elements(By.XPATH, '//input[@type = "checkbox"]')

for checkbox in checkBoxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
time.sleep(2)
