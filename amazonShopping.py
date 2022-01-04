# add the geckodriver exe to your path

# imports from selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# starts the browser, goes to webpage
browser = webdriver.Firefox()
browser.get('https://amazon.com')

# get elements
search_input = browser.find_element(By.ID, "twotabsearchtextbox")
search_button = browser.find_element(By.ID, "nav-search-submit-button")

# manipulate elements
search_input.send_keys("Playstation 5")
search_button.click()