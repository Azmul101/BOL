from selenium.webdriver.common.by import By
from Pages.BasePage import Common


class Encore_HH(Common):
    # by Locators
    side_menu = By.XPATH, "//a[@id='/apps/hhwh2/dashboard']"
    E_HH_Warehouse = By.ID, "ActiveFacilityForm_facilityId"
    WW = By.ID, "ActiveFacilityForm_submitButton"
    LookUp = By.XPATH, "//a[@class='btn btn-primary btn-sm'][normalize-space()='Look Up']"
    MoveProduct = By.XPATH, "//a[@class='btn btn-primary btn-sm'][normalize-space()='Move Product']"

    # Constructor of the class
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Methods
    def login(self):
        return self.login_page()

    def get_side_menu(self):
        return self.do_click(self.side_menu)

    def get_warehouse(self):
        self.selectOptionByText(self.E_HH_Warehouse, "KK_FACILITY: Karen Kane Warehouse")

    def set_HH(self):
        self.do_click(self.WW)

    def set_LookUp(self):
        self.do_click(self.LookUp)

    def set_MoveProduct(self):
        self.do_click(self.MoveProduct)

