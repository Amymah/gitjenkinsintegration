import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

URL="https://jqueryui.com/datepicker/"
Frame_XPATH="//iframe[@class='demo-frame']"
Date_XPATH="//input[@id='datepicker']"
Table_XPATH="//table[@class='ui-datepicker-calendar']"

#function for intializing the driver
def initialize_driver():
    service=Service(ChromeDriverManager().install())
    driver=webdriver.Chrome(service=service)
    #driver.maximize_window()
    return driver

#funtion for URL
def open_url(driver,url):
    driver.get(url)
    driver.maximize_window()

#function to switch to the frame
def switch_to_frame(driver, frame_XPATH):
    iframe=driver.find_element(By.XPATH, frame_XPATH)
    driver.switch_to.frame(iframe)
    time.sleep(2)
    print("switched to the frame.")

#function to click the field and entering date using JS script
def pick_date_JS(driver, date_xpath,table_xpath, value):
    date_picker=driver.find_element(By.XPATH, date_xpath)
    date_picker.click()
    time.sleep(3)
    table=driver.find_element(By.XPATH,table_xpath)
    # scroll element into the view:
    driver.execute_script("arguments[0].scrollIntoView();", table)
    time.sleep(2)
    print("clicked the date field.")
    time.sleep(2)
    driver.execute_script("arguments[0].value=arguments[1];",date_xpath,value)
    print(f"dat set to: {value}")

def main():
    driver=initialize_driver()

    open_url(driver,URL)

    switch_to_frame(driver,Frame_XPATH)

    pick_date_JS(driver, Date_XPATH,Table_XPATH,"2025-04-21")

    time.sleep(2)

    driver.quit()

if __name__=='__main__':
    main()






