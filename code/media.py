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

def gallery():
    folder_name = "Photo_Gallery"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    try:
        driver.get("https://labour.gov.in/")
        time.sleep(5)
        close_btn = driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div/div[2]/button').click()

        media_menu = driver.find_element(By.LINK_TEXT, "Media")
        ActionChains(driver).move_to_element(media_menu).perform()
        time.sleep(2)
        photo_gallery = driver.find_element(By.LINK_TEXT, "Photo Gallery")
        photo_gallery.click()
        time.sleep(5)
        images = driver.find_elements(By.TAG_NAME, "img")[:10]
        for index, img in enumerate(images):
            src = img.get_attribute("src")
            response = requests.get(src)
            if response.status_code == 200:
                with open(os.path.join(folder_name, f"photo_{index + 1}.jpg"), "wb") as file:
                    file.write(response.content)
        print(f"Downloaded {len(images)} photos into '{folder_name}' folder.")

    finally:
        driver.quit()
gallery()