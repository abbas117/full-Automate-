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

widgets = driver.find_element(By.XPATH,'(//button[@type= "button"])[4]').click()
time.sleep(2)

accordiontab = driver.find_element(By.XPATH, "//a[@href = 'accordion.php']")
accordiontab.click()
time.sleep(2)

#first Tab opened
accordion1 = driver.find_element(By.ID,'headingTwentyOne')   
accordion1.click()
time.sleep(3)

#tab first text
paragraph1 = driver.find_element(By.XPATH,'(//p[@class = "text-justify"])[1]')
print(paragraph1.text) 
time.sleep(3)

#tab first closed
accordion1 = driver.find_element(By.ID,'headingTwentyOne')   
accordion1.click()
time.sleep(1)

#Second tab opened
accordion2 = driver.find_element(By.ID,'headingTwentyTwo')
accordion2.click()
time.sleep(1)

#tab second text
paragraph2 = driver.find_element(By.XPATH,'(//p[@class = "text-justify"])[2]')
print(paragraph2.text)
time.sleep(1)

#tab second closed
accordion2 = driver.find_element(By.ID,'headingTwentyTwo')
accordion2.click()
time.sleep(1)

#third tab opened
accordion3 = driver.find_element(By.ID,'headingTwentyThree')
accordion3.click()
time.sleep(1)

#tab threee text
paragraph3 = driver.find_element(By.XPATH,'(//p[@class = "text-justify"])[3]')
print(paragraph3.text)
time.sleep(1)

#tab closed 
accordion3 = driver.find_element(By.ID,'headingTwentyThree')
accordion3.click()
time.sleep(1)

driver.quit()