from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
import time

driver = webdriver.Chrome()

driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.XPATH, "//*[@class='search-keyword']").send_keys('Brocolli')
driver.find_element(By.XPATH, "//button[text()='ADD TO CART']").click()
driver.find_element(By.XPATH, "//*[@class='cart-icon']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
print(driver.title)

driver.close()

