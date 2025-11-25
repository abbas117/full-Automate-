from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time 

driver = webdriver.Chrome()
driver.get("https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php")
driver.maximize_window()
time.sleep(2)

element = driver.find_element(By.ID,"headingOne").click()
time.sleep(3)

brokenLinkImage = driver.find_element(By.XPATH, "//a[@href='broken-links.php']").click()
time.sleep(2)

brokenlink = driver.find_element(By.LINK_TEXT,"Click Here for Broken Link").click()
time.sleep(3)

statusCode = driver.find_element(By.TAG_NAME,"h5")
print(statusCode.text)
goBackbtn = driver.find_element(By.LINK_TEXT,"Go Back").click()

time.sleep(3)
driver.quit()

# wait  = WebDriverWait(driver, 10)
# wait.until(EC.url_changes)

