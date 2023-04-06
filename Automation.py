# Below code shows testing activities by controlling a URL in chrome Browser
#with Selenium and python


# Importing selenium libraries(webdriver, time and service)
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

#Giving chromedriver path to the service
service=Service(executable_path='./chromedriver')

#Including various options like for screen to stay and 
#ignoring SSL errors
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_experimental_option("detach",True)
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')

#including chrome driver and a web URL for automation testing
chrome_browser = webdriver.Chrome(service=service,options=options)
chrome_browser.maximize_window()
chrome_browser.get('https://demo.seleniumeasy.com/basic-first-form-demo.html')

#Below 2 line code is to get Button name by it;s class name
# button_text = chrome_browser.find_element(By.CLASS_NAME, 'btn-primary')
# print(button_text.get_attribute('innerHTML'))

show_message_button = chrome_browser.find_element(By.CLASS_NAME, 'btn-primary')

assert 'Show Message' in chrome_browser.page_source

# Below message is asserted into input field and checked if the assertion works
user_message = chrome_browser.find_element(By.ID, 'user-message')
user_button2 = chrome_browser.find_element(By.CSS_SELECTOR, "#get-input > .btn")
user_message.clear()
user_message.send_keys("I am Testing")
# print(user_button2)

show_message_button.click()

output_message = chrome_browser.find_element(By.ID, 'display')

print('I am Testing' in output_message.text)

#assert 'I am Testing' in output_message.text

# chrome_browser.quit()
# chrome_browser.close()

