from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
import chromedriver_autoinstaller
import time

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
time.sleep(5)
print(driver.title)

driver.maximize_window()
time.sleep(2)
driver.refresh()
time.sleep(2)
driver.back()
time.sleep(2)
driver.minimize_window()
time.sleep(2)
driver.forward()
time.sleep(2)
driver.close()
