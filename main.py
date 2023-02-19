from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

import time

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
browser.get("https://www.linkedin.com/jobs/search/?keywords=psychiatric%20registered%20nurse&location=Austin%2C%20Texas%2C%20United%20States&refresh=true")
for link in browser.find_elements(By.XPATH, '//a[@class="base-card__full-link"]'):
    pass

browser.maximize_window()
print("window is maximized")
time.sleep(10)
browser.quit()