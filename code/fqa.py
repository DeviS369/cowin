


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time ,os

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()

try:
    driver.get("https://www.cowin.gov.in/")
    time.sleep(5)
    faq_link = driver.find_element(By.LINK_TEXT, "FAQ")
    partners_link = driver.find_element(By.LINK_TEXT, "PARTNERS")
    ActionChains(driver).key_down(Keys.CONTROL).click(faq_link).key_up(Keys.CONTROL).perform()
    ActionChains(driver).key_down(Keys.CONTROL).click(partners_link).key_up(Keys.CONTROL).perform()
    time.sleep(2)
    window_handles = driver.window_handles
    print("Window Handles:", window_handles)
    for handle in window_handles[1:]:
        driver.switch_to.window(handle)
        driver.close()
    driver.switch_to.window(window_handles[0])
    print("Returned to Home Page.")
    
finally:
    driver.quit()

# Navigate to Labour website




