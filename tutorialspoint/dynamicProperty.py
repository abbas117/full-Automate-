from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time 

driver = webdriver.Chrome()
driver.get("https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php")
driver.maximize_window()
time.sleep(2)

element = driver.find_element(By.ID,"headingOne").click()
time.sleep(2)

action = ActionChains(driver)
action.scroll_by_amount(0,500).perform()

dynamicproperty = driver.find_element(By.XPATH, "//a[@href='dynamic-prop.php']").click()
time.sleep(2)

wait = WebDriverWait(driver, 10)
changecolorbtn = wait.until(EC.element_to_be_clickable((By.ID,"colorChange")))
changecolorbtn.click()
print(changecolorbtn.text)

visiblebtn = wait.until(EC.element_to_be_clickable((By.ID,'visibleAfter')))
visiblebtn.click()
print(visiblebtn.text)

time.sleep(3)