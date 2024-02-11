from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import chromedriver_autoinstaller
import time

driver = webdriver.Chrome()

#driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.XPATH, "//*[@class='search-keyword']").send_keys('Brocolli')
driver.find_element(By.XPATH, "//button[text()='ADD TO CART']").click()
driver.find_element(By.XPATH, "//*[@class='cart-icon']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

wait = WebDriverWait(driver, 10)
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.promoCode')))

driver.find_element(By.XPATH, "//*[@class='promoCode']").send_keys('rahulshetty')
driver.find_element(By.CLASS_NAME, "promoBtn").click()

print(driver.title)

driver.close()

