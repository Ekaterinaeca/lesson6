from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.ID, "updatingButton"), "SkyPro")
)

try:
    driver.get("http://uitestingplayground.com/ajax")

    ajax_button = driver.find_element(By.ID, "ajaxButton")
    ajax_button.click()

    green_label = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CLASS_NAME, "bg-success"))
    )

    text = green_label.text

    print(text)

finally:
    driver.quit()