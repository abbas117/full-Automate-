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

ModalDialogs = wait.until(EC.element_to_be_clickable((By.XPATH,"//a[@href='modal-dialogs.php']")))
ModalDialogs.click()
time.sleep(2)

smallModel = driver.find_element(By.XPATH,'(//button[@class="btn btn-primary"])[1]')
smallModel.click()
time.sleep(1)

model1text = driver.find_element(By.XPATH,"(//div[@class='modal-body'])[1]")
print(model1text.text)
time.sleep(1)

closebtn = driver.find_element(By.XPATH,'(//button[@class="btn btn-primary"])[3]')
closebtn.click()
time.sleep(1)

largeModel = driver.find_element(By.XPATH,'(//button[@class="btn btn-primary"])[2]')
largeModel.click()

largeModeltext = driver.find_element(By.XPATH,"(//div[@class='modal-body'])[2]")
print(largeModeltext.text)
time.sleep(1)

closebtn2 = driver.find_element(By.XPATH,'(//button[@class="btn btn-primary"])[4]')
closebtn2.click()

time.sleep(1)

driver.quit()


