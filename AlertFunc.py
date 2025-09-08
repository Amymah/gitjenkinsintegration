import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

#function for intializing the driver
def initialize_driver():
    service=Service(ChromeDriverManager().install())
    driver=webdriver.Chrome(service=service)
    driver.maximize_window()
    return driver

#funtion for URL
def open_url(driver,url):
    driver.get(url)
# Handle JS Alert
def handle_js_alert(driver,alert_xpath):
    driver.find_element(By.XPATH, alert_xpath).click()
    time.sleep(2)
    alert = driver.switch_to.alert
    print("JS Alert message:", alert.text)
    alert.accept()

# Handle JS Confirm
def handle_js_confirm(driver,confirm_xpath,accept=True):
    driver.find_element(By.XPATH,confirm_xpath).click()
    time.sleep(2)
    alert = driver.switch_to.alert
    print("JS Confirm message:", alert.text)
    if accept:
        alert.accept()
    else:
        alert.dismiss()

# Handle JS Prompt
def handle_js_prompt(driver,propmpt_xpath, input_text=None):
    driver.find_element(By.XPATH, propmpt_xpath).click()
    time.sleep(2)
    alert = driver.switch_to.alert
    print("JS Prompt message:", alert.text)
    if input_text is not None:
        alert.send_keys(input_text)
        alert.accept()
    else:
        alert.dismiss()

# Main function
def main():
    JS_ALERT_XPATH= "//button[@onclick='jsAlert()']"
    JS_CONFIRM_XPATH= "//button[@onclick='jsConfirm()']"
    JS_PROMPT_XPATH= "//button[@onclick='jsPrompt()']"
    url="https://the-internet.herokuapp.com/javascript_alerts"
    driver=initialize_driver()

    open_url(driver,url)

    #simple alert
    handle_js_alert(driver, JS_ALERT_XPATH)
    time.sleep(2)

    #confirmation alert
    handle_js_confirm(driver, JS_CONFIRM_XPATH,True)
    time.sleep(2)

    handle_js_confirm(driver, JS_CONFIRM_XPATH,False)
    time.sleep(2)

    #Prompt alert
    handle_js_prompt(driver, JS_PROMPT_XPATH,"hello world!")
    time.sleep(2)

    handle_js_prompt(driver,JS_PROMPT_XPATH)
    time.sleep(2)

    driver.close()

if __name__ == "__main__":
    main()
