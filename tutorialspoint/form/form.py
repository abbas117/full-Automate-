from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time 

driver = webdriver.Chrome()
driver.get("https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php")
driver.maximize_window()
time.sleep(2)

formtext = driver.find_element(By.CSS_SELECTOR,".mb-3.fw-normal.border-bottom.text-left.pb-2.mb-4")
print(formtext)

name = "Abbas"
email = "Abbas@gmail.com" 
mobileNumber = "7417184760"
nameField = driver.find_element(By.ID,"name").send_keys(name)
time.sleep(1)
emailfield = driver.find_element(By.ID,"email").send_keys(email)
time.sleep(1)

radiobtn = driver.find_elements(By.XPATH,'//input[@type="radio"]')

for radio in radiobtn:
    radiobtn[0].click()
print(radio)

mobileField = driver.find_element(By.ID,'mobile').send_keys(mobileNumber)
time.sleep(1)

dobfiled = driver.find_element(By.ID,"dob")
dobfiled.clear()
dobfiled.send_keys("20-08-1998")
time.sleep(1)

subject_field = driver.find_element(By.ID,"subjects").send_keys("Computer Science")

checkbox = driver.find_elements(By.XPATH,'//input[@type= "checkbox"]')
for check in checkbox:
    check.click()
    time.sleep(0.1)
print(check.text)

uploadfile = driver.find_element(By.ID,'picture').send_keys(r"C:\Users\mutta\Downloads\download.jpg")
time.sleep(2)

addressfield = driver.find_element(By.TAG_NAME,"textarea").send_keys(" KIDWAINAGAR MUZAFFARNAGAR")

state_field = driver.find_element(By.ID,"state").send_keys("Uttar Pardesh")
time.sleep(3)

cityfield = driver.find_element(By.ID,"city").send_keys("Meerut")
time.sleep(2)
  
loginbtn = driver.find_element(By.XPATH,"//input[@value='Login']").click()
time.sleep(2)