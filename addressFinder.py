# add the geckodriver exe to your path

# imports from selenium
from selenium import webdriver
from selenium.webdriver.common.by import By

# starts the browser, goes to webpage
browser = webdriver.Firefox()
browser2.get('https://gis.hennepin.us/property/map/default.aspx')

# gets the elements
map_input = browser2.find_element(By.ID, "search-input")
map_search_btn = browser2.find_element(By.ID, "search-btn")

# manipulates the elements
map_input.send_keys("9726 Utica Road, Bloomington") # input whatever address
map_button.click()