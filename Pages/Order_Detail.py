from selenium.webdriver.common.by import By

from Pages.BasePage import Common


class Order_detail(Common):
    # Locators
    Orders = (By.XPATH, "//ul[@id='collapse1']//li[5]")
    Select_Order = (By.CSS_SELECTOR, "a[id$='OrderList_orderId_0_orderDetail']")
    Product = (By.CSS_SELECTOR, "a[id=OrderItems_productLink_0_0_editProduct]")
    # Table_id = (By.CSS_SELECTOR, "table[id='OrderItems_0_table']")
    # rows = Table_id.find_elements(By.TAG_NAME, "tr")

    # Constructor of the page
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def login(self):
        return self.login_page()

    def orders(self):
        return self.do_click(self.Orders)

    def get_select_order(self):
        return self.do_click(self.Select_Order)

    def get_line_item(self):
        return self.is_visible(self.Product)
