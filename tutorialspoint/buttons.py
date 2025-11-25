from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php")
driver.maximize_window()
time.sleep(2)

element = driver.find_element(By.ID,"headingOne").click()
time.sleep(3)

buttons  = driver.find_element(By.XPATH,'//a[@href = "buttons.php"]')
buttons.click()
time.sleep(2)

clickbtn = driver.find_element(By.XPATH,'//button[@class= "btn btn-primary"]')
clickbtn.click()
print(clickbtn.text)

clickBtnText = driver.find_element(By.ID,"welcomeDiv")
print(clickBtnText.text)
time.sleep(2)   

action = ActionChains(driver)
rightClickbtn = driver.find_element(By.XPATH,'//button[@class= "btn btn-secondary"]')
action.context_click(rightClickbtn).perform()
print(rightClickbtn.text)
time.sleep(2)

doubleClickbtn = driver.find_element(By.XPATH,'//button[@class= "btn btn-success"]')
action.double_click(doubleClickbtn)
print(doubleClickbtn.text)
time.sleep(2)

