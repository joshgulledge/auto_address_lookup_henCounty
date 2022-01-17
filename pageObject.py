from selenium import webdriver

from trainingPage import TrainingGroundPage


browser= webdriver.Firefox()
training_page = TrainingGroundPage(driver=browser)
training_page.go()
training_page.button1().click()
browser.quit()