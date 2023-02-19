from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

import time

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# sign into linkedin
browser.get("https://linkedin.com")
username = browser.find_element(By.XPATH, '//input[contains(@autocomplete, "username")]')
username.send_keys("mnakhaleh@gmail.com")

password = browser.find_element(By.XPATH, '//input[contains(@autocomplete, "current-password")]')
password.send_keys("<PASSWORD>")

sign_in = browser.find_element(By.XPATH, '//button[contains(@class, "sign-in-form__submit-button")]')
sign_in.click()

time.sleep(10)

browser.get("https://www.linkedin.com/jobs/search/?keywords=psychiatric%20registered%20nurse&location=Austin%2C%20Texas%2C%20United%20States&refresh=true")
try:
    easy_apply = WebDriverWait(browser, 20).until(EC.visibility_of_element_located((By.XPATH, "//li-icon[contains(text(), 'Easy Apply')]"))).get_attribute("value")
except TimeoutException:
    print("can't find easy apply")
    
for link in browser.find_elements(By.XPATH, '//a[contains(@class, "base-card__full-link")]'):
    easy_apply = link.find_element(By.XPATH, "//li-icon[contains(text(), 'Easy Apply')]")
    # easy_apply = WebDriverWait(browser, 20).until(EC.visibility_of_element_located(By.XPATH, "//li-icon[contains(text(), 'Easy Apply')]")).get_attribute("value")
    if easy_apply:
        print("this is an easy apply job")

browser.maximize_window()
print("window is maximized")
time.sleep(10)
browser.quit()