from selenium.webdriver.common.by import By
from pageobject import Locators
class SearchHotelPage:
    def __init__(self, driver):
     self.location = driver.find_element(By.NAME, Locators.location_name)
     self.hotels = driver.find_element(By.ID, Locators.hotels_id)
     self.roomtype = driver.find_element(By.NAME, Locators.room_type_name)
     self.no_of_room = driver.find_element(By.ID, Locators.no_of_room_id)
     self.check_in = driver.find_element(By.XPATH, Locators.check_in_xpath)
     self.check_out = driver.find_element(By.XPATH, Locators.check_out_xpath)
     self.adult = driver.find_element(By.ID, Locators.adult_per_room_id)
     self.child = driver.find_element(By.ID, Locators.child_per_room_name)
     self.btn_search =driver.find_element(By.NAME, Locators.btn_search_name)

     #getters
    def getLocation(self):
        return self.location
    def getHotels(self):
        return self.hotels
    def getRoomtype(self):
        return self.roomtype
    def getNoOfRoom(self):
        return self.no_of_room
    def getCheckIn(self):
        return self.check_in
    def getCheckOut(self):
        return self.check_out
    def getAdult(self):
        return self.adult
    def getChildrens(self):
        return self.child
    def getBtnSearch(self):
        return self.btn_search
