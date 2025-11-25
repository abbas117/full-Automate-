from selenium import webdriver
from selenium.webdriver.common.by import By

import time 

driver = webdriver.Chrome()
driver.get("https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php")
driver.maximize_window()
time.sleep(2)

element = driver.find_element(By.ID,"headingOne").click()
time.sleep(3)

check_box = driver.find_element(By.XPATH, "//a[@href='check-box.php']").click()
time.sleep(2)

plusMinus = driver.find_element(By.XPATH,"(//span[@class='plus'])[4]").click()
time.sleep(2)

check_box1 = driver.find_element(By.ID,'c_bs_2').click()
time.sleep(2)

