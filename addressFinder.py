# add the geckodriver exe to your path

# imports from selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# starts the browser, goes to webpage
browser = webdriver.Firefox()
browser.get('https://gis.hennepin.us/property/map/default.aspx')

# gets the elements
map_input = browser.find_element(By.ID, "search-input")
map_search_btn = browser.find_element(By.ID, "search-btn")

# manipulates the elements
map_input.send_keys("8161 33rd Avenue South, Bloomington") # input whatever address
map_search_btn .click()

try:
    pop_up_present = EC.presence_of_element_located((By.XPATH, "//text()='503'"))
    WebDriverWait(browser, 10).until(pop_up_present)
except TimeoutException:
    print("pop up not on page")
finally:
    # click the address with the condo number
    print("pop up on page")

# try:
#     element_present = EC.presence_of_element_located((By.XPATH, "//td[@id='owner']"))
#     WebDriverWait(browser, 10).until(element_present)
# except TimeoutException:
#     print("Timed out, waiting for page to load")
# finally:
#     # print owner of house to console
#     owner_name = browser.find_element(By.XPATH, "//td[@id='owner']")
#     print(owner_name.text)

# # quit the browser
browser.quit()