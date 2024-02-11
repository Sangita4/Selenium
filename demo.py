from selenium import webdriver
#from selenium.webdriver.chrome.service import Service
import time
import chromedriver_autoinstaller

#service_obj = Service()
#driver = webdriver.Chrome(service=service_obj)

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/")
driver.maximize_window()
print(driver.title)

driver.get("https://courses.rahulshettyacademy.com/courses/")
print(f"URL: {driver.current_url}")
print(driver.title)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.minimize_window()
time.sleep(5)

driver.back()
time.sleep(5)

driver.refresh()
time.sleep(5)

driver.forward()
time.sleep(5)

driver.close()

