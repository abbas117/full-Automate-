from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time 

driver = webdriver.Chrome()
driver.get("https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php")
driver.maximize_window()
time.sleep(2)

element = driver.find_element(By.ID,"headingOne").click()
time.sleep(3)

textBox = driver.find_element(By.XPATH,"//a[@href='upload-download.php']").click()
time.sleep(3)

downloadbtn = driver.find_element(By.ID,"downloadButton")
downloadbtn.click()
time.sleep(2)

#validate file downloaded or not !!!
filePath = r"C:\Users\mutta\Downloads"
filename = "sampleFile.jpeg"
file = os.listdir(filePath)

if filename in file:
    print("File download successfully")
else:
    print("Not found")

print("This is file", filename)

uploadFile = driver.find_element(By.ID,'uploadFile')
# uploadFile.click()
uploadFile.send_keys(r"C:\Users\mutta\Downloads\sampleFile.jpeg")
print("file successfully uploaded",uploadFile)
time.sleep(5)