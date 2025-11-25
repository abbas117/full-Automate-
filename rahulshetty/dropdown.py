from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

dropdown = Select(driver.find_element(By.ID,"dropdown-class-example"))
dropdown.select_by_index(2)
time.sleep(1)

driver.quit()