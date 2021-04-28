from selenium.webdriver.common.by import By
from Pages.BasePage import Common


class HH_Warehouse(Common):
    # by Locators
    side_menu = By.XPATH, "//a[@id='/apps/hhwh/dashboard']"
    # H_Warehouse = By.XPATH, "//a[@id='/apps/hhwh/dashboard']"

    # Constructor of the class
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Methods
    def login(self):
        return self.login_page()

    def get_side_menu(self):
        return self.do_click(self.side_menu)
