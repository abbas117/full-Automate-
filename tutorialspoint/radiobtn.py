from selenium import webdriver
from selenium.webdriver.common.by import By

import time 

driver = webdriver.Chrome()
driver.get("https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php")
driver.maximize_window()
time.sleep(2)

element = driver.find_element(By.ID,"headingOne").click()
time.sleep(3)


driver.find_element(By.XPATH,'//a[@href="radio-button.php"]').click()
time.sleep(1)

text = driver.find_element(By.TAG_NAME,"p")
print(text.text)

radioBtn = driver.find_elements(By.CSS_SELECTOR,".form-check-input")

for radio in radioBtn:
    radioBtn[1].click()
time.sleep(2)

labels = driver.find_elements(By.CSS_SELECTOR,'.form-check-label')   
for label in labels:
    print(label.text)

successText = driver.find_element(By.ID, 'check1')
print(successText.text)

assert "Impressive" in successText.text
