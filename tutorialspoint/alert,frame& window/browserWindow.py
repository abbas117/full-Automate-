from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time 

driver = webdriver.Chrome()
driver.get("https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php")
driver.maximize_window()
time.sleep(2)

wait = WebDriverWait(driver , 10)
alert_Window_frame = driver.find_element(By.ID,"headingThree").click()
time.sleep(2)

time.sleep(2)

brownser_window = wait.until(EC.element_to_be_clickable((By.XPATH,"//a[@href='browser-windows.php']")))
brownser_window.click()
time.sleep(2)

main = driver.current_window_handle

newtab = driver.find_element(By.XPATH,"(//button[@class='btn btn-primary'])[1]")
newtab.click()

alltabs = driver.window_handles

for tab in alltabs:
    if tab != main:
        driver.switch_to.window(tab)
        break
print("First new tab", driver.title)

time.sleep(5)

driver.switch_to.window(main)
print("main title", driver.title)
time.sleep(2)

newWindow = driver.window_handles

for windown in newWindow:
    if windown != main:
        driver.switch_to.window(windown)
print(driver.title)

driver.switch_to.window(main)
time.sleep(1)

driver.maximize_window()
time.sleep(3)

windowmessage = driver.find_element(By.XPATH,'(//button[@class = "btn btn-primary"])[3]')
windowmessage.click()

# get all window handles
winmsgbtn = driver.window_handles

for winmsg in winmsgbtn:
    if winmsg != main:
        driver.switch_to.window(winmsg)
        break   # stop after switching to the new window

# print title of the new window
print("Third window", driver.title)

time.sleep(3)

