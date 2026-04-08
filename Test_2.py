import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()

driver.get('https://energy-ba-bih3.bharti.g002.saas.nokia.com/#/login')
time.sleep(2)

wait = WebDriverWait(driver, 2)

#username located by xpath
username = wait.until(
 EC.presence_of_element_located((By.XPATH, "//input[@formcontrolname='username']"))
)
username.send_keys("Reader")
#password located by xpath
password = wait.until(
    EC.presence_of_element_located((By.XPATH, "//input[@formcontrolname='password']"))
)

password.send_keys("Read#2025")

time.sleep(2)

#password login Button by xpath
login_btn: WebElement = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(@class,'ant-btn-primary')]"))
)
login_btn.click()
#time.sleep(2)
#route for automation path
wait = WebDriverWait(driver, 20)
wait = WebDriverWait(driver, 30)

# Wait for page load
wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

# Debug
print(driver.current_url)

# Check Automation presence
elements = driver.find_elements(By.XPATH, "//*[contains(text(),'Automation')]")
print("Automation found:", len(elements))

# Click Automation
automation = wait.until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'Automation')]"))
)

driver.execute_script("arguments[0].click();", automation)
time.sleep(3)
#Click FW Saving Monitor button.
FW_Saving = wait.until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'FW Saving Monitor')]"))
)

driver.execute_script("arguments[0].click();", FW_Saving)
time.sleep(3)

# Download Saving Report
Export_btn: WebElement = wait.until(
    EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'Export')]"))
)
driver.execute_script("arguments[0].click();", Export_btn)
time.sleep(8)
#print ("window title:", driver.title)
#print("window url:", driver.current_url)
print("FW Saving Monitor report downloaded")
driver.quit()