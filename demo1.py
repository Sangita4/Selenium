from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
import time

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.find_element(By.NAME, "email").send_keys(skalane@gmail.com)
time.sleep(5)
driver.close()
