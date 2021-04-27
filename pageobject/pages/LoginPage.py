from selenium.webdriver.common.by import By
from pageobject import Locators
class LoginPage:
    def __init__(self, driver):
        self.username = driver.find_element(By.ID, Locators.username_id)
        self.password = driver.find_element(By.ID, Locators.password_id)
        self.btn_login = driver.find_element(By.XPATH, Locators.btn_login_xpath)
    # Getters
    def getUserName(self):
        return self.username
    def getPassWord(self):
        return self.password
    def getBtnLogin(self):
        return self.btn_login