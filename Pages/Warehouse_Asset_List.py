from selenium.webdriver.common.by import By

from Pages.BasePage import Common


class Warehouse_List(Common):
    # Locators
    side_menu = By.XPATH, "//a[@id='/apps/wms/dashboard']"
    Asset_List = By.XPATH, "//a[@href='/vapps/wms/Asset/dashboard']"
    Asset_button = By.CSS_SELECTOR, "a[href^='/vapps/wms/Asset/Asset/FindAsset']"
    Find_option = By.ID, "ListAssets_hdialog_button"
    Asset_ID = By.ID, "ListAssets_header_assetId"
    Asset_find_button = By.ID, "ListAssets_header_submitButton"
    title = By.CSS_SELECTOR, "h1[class='content-title']"
    csv = (By.XPATH, "//a[normalize-space()='CSV']")
    xls = (By.XPATH, "//a[normalize-space()='XLS']")

    # Constructor of the class
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Methods
    def login(self):
        return self.login_page()

    def get_side_menu(self):
        return self.do_click(self.side_menu)

    def get_menu_list(self):
        return self.do_click(self.Asset_List)

    def get_asset_button(self):
        return self.do_click(self.Asset_button)

    def get_find_option(self):
        return self.do_click(self.Find_option)

    def get_asset_id(self):
        return self.do_send_keys(self.Asset_ID, 11)

    def get_asset_find_button(self):
        return self.do_click(self.Asset_find_button)

    def get_page_title(self):
        return self.get_element_text(self.title)

    def get_xls(self):
        return self.do_click(self.xls)

    def get_csv(self):
        return self.do_click(self.csv)
