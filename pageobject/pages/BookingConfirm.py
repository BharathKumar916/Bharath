from pageobject import Locators
from selenium.webdriver.common.by import By
class BookingConfirm:
    def __init__(self,driver):
        self.orderno = driver.find_element(By.ID, Locators.order_no_id)
    #getters:
    def getOrderNo(self):
        return self.orderno
