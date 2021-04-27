from selenium.webdriver.common.by import By
from pageobject import Locators
class BookHotelPage:
    def __init__(self, driver):
        self.first_name = driver.find_element(By.NAME, Locators.first_name_name)
        self.last_name = driver.find_element(By.ID, Locators.last_name_id)
        self.bill_address = driver.find_element(By.ID, Locators.bill_address_id)
        self.credit_card_num = driver.find_element(By.XPATH, Locators.credit_card_no_xpath)
        self.credit_card_type = driver.find_element(By.ID, Locators.credit_card_type_id)
        self.exp_date_month =driver.find_element(By.ID, Locators.exp_date_month_id)
        self.exp_date_year = driver.find_element(By.ID, Locators.exp_date_year_id)
        self.cvv = driver.find_element(By.NAME, Locators.cvv_num_name)
        self.booknow = driver.find_element(By.NAME, Locators.btn_booknow_name)
    #getters
    def getFirstName(self):
        return self.first_name
    def getLastName(self):
        return self.last_name
    def getBillAddress(self):
        return self.bill_address
    def getCreditCardNo(self):
        return self.credit_card_num
    def getCreditCardType(self):
        return self.credit_card_type
    def getExpireDateM(self):
        return self.exp_date_month
    def getExpiredateY(self):
        return self.exp_date_year
    def getCvv(self):
        return self.cvv
    def getBookNow(self):
        return self.booknow
