from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time , requests, os

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()
def progress_report():
    try:
        driver.get("https://labour.gov.in/")
        time.sleep(5)
        close_btn = driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div/div[2]/button').click()
        time.sleep(6)
        documents_menu = driver.find_element(By.LINK_TEXT, "Documents")
        time.sleep(2)
        ActionChains(driver).move_to_element(documents_menu).perform()
        time.sleep(2)
        report_link = driver.find_element(By.LINK_TEXT,'Monthly Progress Report')
        report_link.click()
        print("Monthly Progress Report downloaded successfully.")
    except Exception as e:
        print(e)
    finally:
        driver.quit()
progress_report()


