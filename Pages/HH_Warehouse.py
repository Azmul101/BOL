from selenium.webdriver.common.by import By
from Pages.BasePage import Common


class HH_Warehouse(Common):
    # by Locators
    side_menu = By.XPATH, "//a[@id='/apps/hhwh/dashboard']"
    A_Warehouse = By.ID, "ActiveFacilityForm_facilityId"
    Set_button = By.ID, "ActiveFacilityForm_submitButton"
    Scan = By.ID, "ScanAssetForm_scanId"
    Scan_Button = By.ID, "ScanAssetForm_submitButton"
    Select_Move = By.XPATH, "//a[normalize-space()='Select Move']"
    R_Direct = By.XPATH, "//a[@href='/vapps/hhwh/Asset/ReceiveAsset?facilityId=KK_FACILITY']"

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
        self.selectOptionByText(self.A_Warehouse, "KK_FACILITY: Karen Kane Warehouse")

    def get_set_Button(self):
        self.do_click(self.Set_button)

    def get_Scan(self):
        self.do_send_keys(self.Scan, 1010)

    def get_Scan_Button(self):
        self.do_click(self.Scan_Button)

    def get_move(self):
        self.do_click(self.Select_Move)

    def get_direct(self):
        self.do_click(self.R_Direct)
