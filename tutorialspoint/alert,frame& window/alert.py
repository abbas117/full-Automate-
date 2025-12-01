from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

import time 

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php")
driver.maximize_window()

wait = WebDriverWait(driver, 10)

# Navigate to Alert Page
driver.find_element(By.ID, "headingThree").click()
wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='alerts.php']"))).click()
time.sleep(2)

# ---------------- Alert 1 : Simple Alert ----------------
alert_btn1 = wait.until(EC.element_to_be_clickable((By.XPATH, '(//button[@class="btn btn-primary"])[1]')))
time.sleep(2)
alert_btn1.click()

alert = wait.until(EC.alert_is_present())
print("Alert 1:", alert.text)
alert.accept()

# ---------------- Alert 2 : Confirmation Alert ----------------
alert_btn2 = wait.until(EC.element_to_be_clickable((By.XPATH, '(//button[@class="btn btn-primary"])[2]')))
time.sleep(2)

alert_btn2.click()

alert = wait.until(EC.alert_is_present())
print("Alert 2:", alert.text)
alert.accept()

# ---------------- Alert 3 : Cancel Alert ----------------
alert_btn3 = wait.until(EC.element_to_be_clickable((By.XPATH, '(//button[@class="btn btn-primary"])[3]')))
time.sleep(2)

alert_btn3.click()

alert = wait.until(EC.alert_is_present())
print("Alert 3:", alert.text)
time.sleep(2)

alert.dismiss()

# ---------------- Alert 4 : Prompt (Input Alert) ----------------
alert_btn4 = wait.until(EC.element_to_be_clickable((By.XPATH, '(//button[@class="btn btn-primary"])[4]')))
time.sleep(2)
alert_btn4.click()


alert = wait.until(EC.alert_is_present())
print("Alert 4:", alert.text)

alert = driver.switch_to.alert
time.sleep(2)
alert.send_keys("Abbas")


alert.accept()

time.sleep(2)
driver.quit()
