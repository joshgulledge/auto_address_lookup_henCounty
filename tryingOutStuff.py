# add the geckodriver exe to your path

# imports from selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# starts the browser, goes to webpage
browser = webdriver.Firefox()
browser.get('https://techstepacademy.com/iframe-training')

# get elements
# iframe elements
iframe_one = browser.find_element(By.CSS_SELECTOR, 'iframe')

# go to iframe
browser.switch_to.frame(iframe_one)

# get elements
welcome_text = browser.find_element(By.CSS_SELECTOR, "div#block-ec928cee802cf918d26c")
print(welcome_text.text)

# # quit the browser
browser.quit()