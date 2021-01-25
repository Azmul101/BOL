from selenium.webdriver.common.by import By

from Pages.BasePage import Common


class Shipment_Detail(Common):
    # Locators
    menu_link = By.XPATH, "//ul[@id='collapse1']//li[8]"
    shipment = By.XPATH, "//tbody/tr[1]/td[2]/div[1]"

    # Constructor of the class
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        # Methods

    def login(self):
        return self.login_page()

    def get_menu_link(self):
        return self.do_click(self.menu_link)

    def get_shipment(self):
        return self.do_click(self.shipment)

