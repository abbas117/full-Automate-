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

linkbtn = driver.find_element(By.XPATH, "//a[@href='links.php']").click()
time.sleep(2)

wait = WebDriverWait(driver, 10 )
main_window = driver.current_window_handle
home = driver.find_element(By.LINK_TEXT,"Home").click()
wait.until(EC.number_of_windows_to_be(2))

for w in driver.window_handles:
    if w != main_window:
        driver.switch_to.window(w)
        break

print(main_window)
print(w.title)
time.sleep(3)

driver.switch_to.window(main_window)
time.sleep(3)
print("revisit tab", main_window.title)

main_tab = driver.current_window_handle
tab = driver.find_element(By.LINK_TEXT,"HomewPWPU").click()


second_tab = driver.window_handles[1]

time.sleep(4)
driver.switch_to.window(main_tab)
print("SECOND TAB", second_tab)
time.sleep(3)