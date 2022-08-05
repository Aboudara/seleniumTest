import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_object = Service("C:\Program Files (x86)\chromedriver.exe")
driver = webdriver.Chrome(service=service_object)
driver.get("https://www.rahulshettyacademy.com/client/")
driver.maximize_window()
time.sleep(1)
driver.find_element(By.LINK_TEXT, "Forgot password?").click()
driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("demo@gmail.com")
#driver.find_element(By.XPATH, "//form/div[2]/input").send_keys("Hello@1234")
#for cc selector
driver.find_element(By.CSS_SELECTOR, "form div:nth-child(2) input").send_keys("Hello@1234")
driver.find_element(By.CSS_SELECTOR, "#confirmPassword").send_keys("Hello@1234")
driver.find_element(By.XPATH, "//button[@type='submit']").click()
#driver.close()