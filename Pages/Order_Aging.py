from selenium.webdriver.common.by import By
from Pages.BasePage import Common


class Order_aging(Common):
    # Locators
    order_aging = By.XPATH, "//ul[@id='collapse1']//li[6]"
    select_facility = By.CSS_SELECTOR, ".select2.select2-container"
    value = By.XPATH, "//li[@role='treeitem']"
    select_button = By.CSS_SELECTOR, "button[id='SelectFacility_submitButton']"
    order = By.XPATH, "//tbody/tr[2]/td[6]/a"
    page_title = By.XPATH, "//*[@id='apps-root']/div[1]/section/h1"

    # Constructor
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Methods
    def login(self):
        return self.login_page()

    def get_Order_aging(self):
        return self.do_click(self.order_aging)

    def get_facility(self):
        self.do_click(self.select_facility)
        self.do_click(self.value)
        # self.driver.find_element(self.select_facility).send_keys()
        # self.select_facility.send_keys(Keys.ENTER)

    def get_button(self):
        return self.do_click(self.select_button)

    def get_order(self):
        return self.do_click(self.order)

    def get_page_title(self):
        if self.is_visible(self.page_title):
            return self.get_element_text(self.page_title)
