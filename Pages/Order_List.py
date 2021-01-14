from selenium.webdriver.common.by import By

from Pages.BasePage import Common


class Order_List(Common):
    # Locators
    Orders = (By.XPATH, "//ul[@id='collapse1']//li[5]")
    find_element = (By.CSS_SELECTOR, "[id='OrderList_hdialog_button']")
    clear = (By.CSS_SELECTOR, "div[class='col-sm-10'] button[name='clearParameters']")
    order_by = (By.CSS_SELECTOR, "//a[@class='selectivity-multiple-selected-item-remove']")
    find = (By.CSS_SELECTOR, "[id='OrderList_header_submitButton']")
    csv = (By.XPATH, "//a[normalize-space()='CSV']")
    xls = (By.XPATH, "//a[normalize-space()='XLS']")
    create_order = (By.CSS_SELECTOR, "button[id='CreatePurchaseOrderDialog-button']")
    order_title = (By.XPATH, "//h4[normalize-space()='Create Purchase Order']")

    # Constructor of the page
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def login(self, ):
        return self.login_page()

    def orders(self):
        return self.do_click(self.Orders)

    def get_find_element(self):
        return self.do_click(self.find_element)

    def get_clear_param(self):
        return self.do_click(self.clear)

    def get_find(self):
        return self.do_click(self.find)

    def get_csv(self):
        return self.do_click(self.csv)

    def get_xls(self):
        return self.do_click(self.xls)

    def get_order(self):
        return self.do_click(self.create_order)

    def get_create_order(self):
        return self.get_element_text(self.order_title)
