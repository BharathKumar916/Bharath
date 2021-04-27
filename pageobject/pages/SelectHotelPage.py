from selenium.webdriver.common.by import By
from pageobject import Locators
class SelectHotelPage:
    def __init__(self,driver):
        self.btn_select = driver.find_element(By.ID, Locators.btn_select_id)
        self.btn_continue = driver.find_element(By.ID, Locators.btn_continue_id)

    #getters
    def getSelect(self):
        return self.btn_select
    def getContinue(self):
        return self.btn_continue