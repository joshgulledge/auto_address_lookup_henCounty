class TrainingGroundPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://techstepacademy.com/training-ground/'

    def go(self):
        self.driver.get(self.url)

    def give_input_text(self, text):
        input_one = self.driver.find_element(By.ID, 'ipt1')
        input_one.clear()
        input_one.send_keys(text)
        return None
    
    def get_input_text(self):
        page_input = self.driver.find_element(By.ID, 'ipt1')
        elem_text = page_input.get_attribute('value')
        return elem_text

    def click_button_one(self):
        button = self.driver.find_element(By.Id, 'b1')
        button.click()
        return None

## TRY IT
from selenium import webdriver
from selenium.webdriver.common.by import By

browser= webdriver.Firefox()
training_page = TrainingGroundPage(driver=browser)
training_page.go()
training_page.give_input_text("Hello World")
print(training_page.get_input_text())