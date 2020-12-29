from selenium.webdriver.common.by import By

from Pages.BasePage import Common


class Order_detail(Common):
    # Locators
    Orders = (By.XPATH, "//ul[@id='collapse1']//li[5]")

    # Constructor of the page
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def login(self):
        return self.login_page()

    def orders(self):
        return self.do_click(self.Orders)
