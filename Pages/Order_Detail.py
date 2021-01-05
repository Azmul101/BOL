from selenium.webdriver.common.by import By

from Pages.BasePage import Common


class Order_detail(Common):
    # Locators
    Orders = (By.XPATH, "//ul[@id='collapse1']//li[5]")
    Select_Order = (By.CSS_SELECTOR, "a[id='OrderList_orderId_0_orderDetail']")
    Product = (By.CSS_SELECTOR, "a[id=OrderItems_productLink_0_0_editProduct]")
    Address = (By.XPATH, "//div[@class='row']//address[1]")
    Payment = (By.XPATH, "//*[@id='OrderPanel-tabpanel']/div/div[2]/div[2]/div[1]/div[2]/div/div")
    Close_button = (By.CSS_SELECTOR, "button[id='CloseOrderDialog-button']")
    Other_buttons = (By.CSS_SELECTOR, "button[onclick][class='btn btn-primary btn-sm']")
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

    def get_address(self):
        return self.is_visible(self.Address)

    def get_payment(self):
        return self.is_visible(self.Payment)

    def get_buttons(self):
        return self.is_visible(self.Close_button)

    def get_other_button(self):
        return self.is_visible(self.Other_buttons)
