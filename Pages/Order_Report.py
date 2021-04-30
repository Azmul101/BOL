from selenium.webdriver.common.by import By
from Pages.BasePage import Common


class report_order(Common):
    # Locators
    report_menu = By.XPATH, "//ul[@id='collapse1']//li[14]"
    select_store = By.CSS_SELECTOR, "button[id*='ChooseStoreDialog-button']"
    store_id = By.ID, "ChooseStoreForm_integrationId"
    go_button = By.ID, "ChooseStoreForm_submitButton"
    csv = By.XPATH, "//a[normalize-space()='CSV']"
    xls = By.XPATH, "//a[normalize-space()='XLS']"
    retrieve_button = By.CSS_SELECTOR, "button[id='OrderDiscrepanciesReport_action_0_retrieveOrder_button']"
    internal_status = By.XPATH, "//tbody/tr[1]/td[7]/div[1]/span[1]"

    # class Constructor
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Methods
    def login(self):
        return self.login_page()

    def report(self):
        return self.do_click(report_order.report_menu)

    def get_select_store(self):
        return self.do_click(report_order.select_store)

    def get_store(self):
        self.selectOptionByText(self.store_id, "KK_SHOPIFY")

    def click_on_button(self):
        self.do_click(self.go_button)

    def get_csv(self):
        return self.do_click(self.csv)

    def get_xls(self):
        return self.do_click(self.xls)

    def get_retrieve(self):
        return self.driver.find_element(*self.retrieve_button)

    def get_internal_status(self):
        return self.driver.find_element(*self.internal_status)
