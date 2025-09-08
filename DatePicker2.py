import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.expected_conditions import element_to_be_clickable
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

URL="https://www.yatra.com/"
Departue_Calendar_XPATH="//div[@class='css-w7k25o']"
Departure_Date_XPATH="(//span[text()='22'])[2]"
Return_Calendar_XPATH="//div[@class='css-164qbto']"
Return_Date_XPATH="(//span[text()='30'])[2]"
Scroll_Depar_XPATH="//div[@class='MuiBox-root css-89knyc']"
Scroll_return_XPATH="//div[@class='MuiBox-root css-89knyc']"

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

#Function to select departure date
def Departure_Date(driver, depar_xpath,date_xpath,Scroll_xpath,timeout):
    wait=WebDriverWait(driver, timeout)
    departure=wait.until(EC.element_to_be_clickable((By.XPATH,depar_xpath)))
    departure.click()
    print("Departure calendar clicked.")
    time.sleep(5)
    #Scroll calnedar into the view
    scroll=driver.find_element(By.XPATH,Scroll_xpath)
    driver.execute_script("arguments[0].scrollIntoView();",scroll)
    print("Scrolled into the Departure Calender view.")
    time.sleep(3)
    date=driver.find_element(By.XPATH,date_xpath)
    date.click()
    time.sleep(3)
    print("Departure date selected.")

#Function to select return date or (By giving value in JS function)
def Return_Date(driver, return_xpath,scroll_xpath,value,timeout):
    wait=WebDriverWait(driver, timeout)
    retur=wait.until(EC.element_to_be_clickable((By.XPATH,return_xpath)))
    retur.click()
    print("Return calendar clicked.")
    time.sleep(5)
    # Scroll calnedar into the view
    scroll = driver.find_element(By.XPATH, scroll_xpath)
    driver.execute_script("arguments[0].scrollIntoView();", scroll)
    time.sleep(3)
    print("Scrolled into the Return Calender view.")
    # date=driver.find_element(By.XPATH,date_xpath)
    # date.click()
    # time.sleep(3)
    driver.execute_script("arguments[0].value=arguments[1];", return_xpath, value)
    print(f"dat set to: {value}")
    print("Return date selected.")

def main():
    driver=initialize_driver()

    open_url(driver,URL)

    Departure_Date(driver, Departue_Calendar_XPATH, Departure_Date_XPATH,Scroll_Depar_XPATH, 10)

    Return_Date(driver, Return_Calendar_XPATH, Scroll_return_XPATH,'30',10)

    time.sleep(3)

    driver.quit()

if __name__=='__main__':
    main()



