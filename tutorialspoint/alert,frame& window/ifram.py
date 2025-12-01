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

iframtab = wait.until(EC.element_to_be_clickable((By.XPATH,"//a[@href='frames.php']")))
iframtab.click()
time.sleep(2)
main = driver.current_window_handle
iframe = driver.find_element(By.XPATH,"(//iframe[@src='new-tab-sample.php'])[1]")
driver.switch_to.frame(iframe)

linkInFrame = wait.until(EC.presence_of_element_located((By.XPATH,"//a[@class = 'external-link']")))
linkInFrame.click()
time.sleep(4)
print(driver.title)

driver.switch_to.default_content()
time.sleep(2)

driver.switch_to.window(main)
time.sleep(2)
driver.quit()

# iframe2 = driver.find_element(By.XPATH,"(//iframe[@src='new-tab-sample.php'])[2]")
# driver.switch_to.frame(iframe2)

# linkInFrame2 = wait.until(
#     EC.presence_of_element_located((By.CSS_SELECTOR, ".external-link"))
# )

# driver.execute_script("arguments[0].scrollIntoView(true);", linkInFrame2)
# linkInFrame2.click()
# time.sleep(2)

# driver.switch_to.default_content()
# time.sleep(1)
