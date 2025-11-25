from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

autoSuggestion = driver.find_element(By.ID, "autocomplete")
autoSuggestion.click()
time.sleep(2)
autoSuggestion.send_keys("Ame")
time.sleep(2)

countries = driver.find_elements(By.XPATH, "//li[@class='ui-menu-item']")

for country in countries:
    print(country.text)
    if country.text == "American Samoa":
        country.click()
        break

time.sleep(2)
driver.quit()