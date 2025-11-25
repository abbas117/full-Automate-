from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
url = "https://rahulshettyacademy.com/loginpagePractise/"
driver.get(url)
driver.maximize_window()

# driver.get("https://rahulshettyacademy.com/AutomationPractice/")


print(driver.title)
username = "rahulshettyacademy"
password = "learnng"

username_input = driver.find_element(By.ID,'username')
username_input.send_keys(username)

time.sleep(2)

password_input = driver.find_element(By.ID,'password').send_keys(password)
time.sleep(2)

radiobuttons = driver.find_elements(By.XPATH,"//span[@class = 'checkmark']")
for radio in radiobuttons:
    radio.click()
time.sleep(1)

popUp = driver.find_element(By.XPATH,"//div[@class = 'modal-body']/p").text
print(f"pop says:- ", {popUp})

okaybtn = driver.find_element(By.CSS_SELECTOR,"button[id = 'okayBtn']").click()
time.sleep(1)

dropDown = driver.find_element(By.XPATH,'//select[@class = "form-control" ]')
select = Select(dropDown)
select.select_by_visible_text("Consultant")
time.sleep(1)

checkbox = driver.find_element(By.CSS_SELECTOR,'input[id = "terms"]').click()
signInbtn = driver.find_element(By.NAME,"signin").click()

wait = WebDriverWait(driver, 5)
incorrectPass = wait.until(
    EC.visibility_of_element_located((By.XPATH, "//div[@class = 'alert alert-danger col-md-12']"))
)
print(incorrectPass.text)


