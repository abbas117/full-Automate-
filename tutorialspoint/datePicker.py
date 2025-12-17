from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://www.tutorialspoint.com/selenium/practice/date-picker.php")
driver.maximize_window()
time.sleep(2)

wait = WebDriverWait(driver, 10)

driver.find_element(By.ID, "datetimepicker1").click()
time.sleep(2)


Select(
    wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME,"flatpickr-monthDropdown-months")))
        ).select_by_visible_text("August")

year = wait.until(
    EC.visibility_of_element_located((By.XPATH,"(//input[@class='numInput cur-year'])[1]")))
year.clear()
year.send_keys("1998")
time.sleep(2)

date = wait.until(
    EC.presence_of_element_located((By.XPATH,'(//span[@class = "flatpickr-day"][.= "20"])[1]')))

date.click()
time.sleep(2)

hours = driver.find_element(By.XPATH,'(//input[@class = "numInput flatpickr-hour"])[1]')
hours.click()
hours.clear()
hours.send_keys("07")
time.sleep(2)

minutes = driver.find_element(By.XPATH,"(//input[@aria-label='Minute'])[1]")
minutes.click()
minutes.clear()
minutes.send_keys("30")
time.sleep(2)

am_pm = driver.find_element(By.XPATH,"(//span[@class='flatpickr-am-pm'])[1]").click()
time.sleep(2)