from selenium.webdriver.common.by import By

from Pages.BasePage import Common


class Shipment_List(Common):
    # Locators
    menu_link = By.XPATH, "//ul[@id='collapse1']//li[8]"

    # Constructor of the class
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        # Methods
    def login(self):
        return self.login_page()
