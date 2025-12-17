from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time 

driver = webdriver.Chrome()
driver.get("https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php")
driver.maximize_window()

wait = WebDriverWait(driver, 10)

widgets = driver.find_element(By.XPATH,'(//button[@type= "button"])[4]').click()
time.sleep(2)

autocomplete = driver.find_element(By.XPATH, "//a[@href='auto-complete.php']")
autocomplete.click()
time.sleep(2)


