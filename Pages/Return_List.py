from selenium.webdriver.common.by import By
from Pages.BasePage import Common


class ReturnList(Common):
    # Locators
    side_menu = By.XPATH, "//ul[@id='collapse1']//li[9]"
    find_option = By.ID, "returnHeaderBySearch_hdialog_button"
    find_button = By.XPATH, "//button[normalize-space()='Find']"
    Order_List = By.ID, "returnHeaderList_orderId_0_orderDetail"
    Return_List = By.ID, "returnHeaderList_returnId_0_editReturn"
    content_title = By.CSS_SELECTOR, "h1[class='content-title']"

    # Constructor of the class
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Methods
    def login(self):
        return self.login_page()

    def get_side_menu(self):
        return self.do_click(self.side_menu)

    def get_find_option(self):
        self.do_click(self.find_option)

    def get_find_button(self):
        self.do_click(self.find_button)

    def get_order_list(self):
        self.do_click(self.Order_List)

    def get_return_list(self):
        self.do_click(self.Return_List)

    def get_Order_title(self):
        self.is_visible(self.content_title)

