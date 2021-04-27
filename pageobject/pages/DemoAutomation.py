from pageobject import Locators
from selenium.webdriver.common.by import By
class RegisterPage:
    def __init__(self, driver):
        self.first_name = driver.find_element(By.XPATH, Locators.firstname_xpath)
        self.last_name = driver.find_element(By.XPATH, Locators.lastname_xpath)
        self.address = driver.find_element(By.XPATH, Locators.address_xpath)
        self.email = driver.find_element(By.XPATH, Locators.email_xpath)
        self.phone = driver.find_element(By.XPATH, Locators.phone_xpath)
        self.gender = driver.find_element(By.XPATH, Locators.gender_xpath)
        self.hobbies = driver.find_element(By.ID, Locators.hobbies_id)
        self.language = driver.find_element(By.ID, Locators.language_id)
        self.select_lang_1 = driver.find_element(By.XPATH, Locators.lan_1_xpath)
        self.select_lang_2 = driver.find_element(By.XPATH, Locators.lan_2_xpath)
        self.select_lang_3 = driver.find_element(By.XPATH, Locators.lan_3_xpath)
        self.select_lang_4 = driver.find_element(By.XPATH, Locators.lan_4_xpath)
        self.skills = driver.find_element(By.ID, Locators.skills_id)
        self.country = driver.find_element(By.ID, Locators.country_id)
        self.s_country = driver.find_element(By.XPATH, Locators.s_country_xpath)
        self.dob_yr = driver.find_element(By.ID, Locators.dob_year_id)
        self.dob_mn = driver.find_element(By.XPATH, Locators.dob_month_xpath)
        self.dob_dat = driver.find_element(By.ID, Locators.dob_date_id)
        self.password = driver.find_element(By.ID, Locators.pass_id)
        self.c_password = driver.find_element(By.ID, Locators.c_pass_id)
     #getter
    def getFirstName(self):
        return self.first_name
    def getLastName(self):
        return self.last_name
    def getAddress(self):
        return self.address
    def getEmail(self):
        return self.email
    def getPhone(self):
        return self.phone
    def getGender(self):
        return self.gender
    def getHobbies(self):
        return self.hobbies
    def getLang(self):
        return self.language
    def getSelectLang1(self):
        return self.select_lang_1
    def getSelectLang2(self):
        return self.select_lang_2
    def getSelectLang3(self):
        return self.select_lang_3
    def getSelectLang4(self):
        return self.select_lang_4
    def getSkills(self):
        return self.skills
    def getCountry(self):
        return self.country
    def getS_Country(self):
        return self.s_country
    def getDobYear(self):
        return self.dob_yr
    def getDobMonth(self):
        return self.dob_mn
    def getDobDate(self):
        return self.dob_dat
    def getPassword(self):
        return self.password
    def getCPassword(self):
        return self.c_password
