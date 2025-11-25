from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

driver = webdriver.Chrome()
driver.get("https://www.tutorialspoint.com/selenium/practice/selenium_automation_practice.php")
driver.maximize_window()
time.sleep(2)

element = driver.find_element(By.ID,"headingOne").click()
time.sleep(3)

textBox = driver.find_element(By.XPATH,"//a[@href='webtables.php']").click()
time.sleep(3)

addbtn = driver.find_element(By.XPATH,'//button[@class= "btn btn-primary"]').click()
time.sleep(3)

firstname = driver.find_element(By.ID,"firstname")
firstname.click()
firstname.send_keys("Muttaki")
print("first name:-", firstname.get_attribute("value")) 
time.sleep(1)

lastname = driver.find_element(By.ID,"lastname")
lastname.click()
lastname.send_keys("Abbas")
print("last name:-", lastname.get_attribute("value")) 
time.sleep(1)

email = driver.find_element(By.ID,"email")
email.click()
email.send_keys("Muttaquiabbas20@gmail.com")
print("email:-", email.get_attribute("value")) 
time.sleep(1)

age = driver.find_element(By.ID,"age")
age.click()
age.send_keys("0035")
print("age:-", age.get_attribute("value")) 
time.sleep(1)

salary = driver.find_element(By.ID,"salary")
salary.click()
salary.send_keys("20000000000000")
print("salary:-", salary.get_attribute("value")) 
time.sleep(1)

department = driver.find_element(By.ID,"deparment")
department.click()
department.send_keys("IT")
print("department:-", department.get_attribute("value")) 
time.sleep(1)

loginbtn = driver.find_element(By.ID,"deparment").click()

tableheader = driver.find_elements(By.XPATH,'//th[@scope = "col"]')
for header in tableheader:
    print(header.text)

all_data = driver.find_elements(By.XPATH,"//tbody/tr/td")
print(all_data)

for data in all_data:
    print(data.text)

deletbtn = driver.find_element(By.XPATH,'(//a[@class = "delete-wrap confirmdeletebtn"])[3]').click()
time.sleep(2)

searchbar = driver.find_element(By.XPATH,'(//input[@type= "text"])[1]')
searchbar.send_keys("Abbas")

searchbarbtn = driver.find_element(By.XPATH,'//button[@class= "btn btn-outline-secondary"]')
searchbarbtn.click()
time.sleep(2)

