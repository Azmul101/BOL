from selenium.webdriver.common.by import By

from Pages.BasePage import Common


class Warehouse_Detail(Common):
    # Locators
    side_menu = By.XPATH, "//a[@id='/apps/wms/dashboard']"
    Asset_List = By.XPATH, "//a[@href='/vapps/wms/Asset/dashboard']"
    Asset_button = By.CSS_SELECTOR, "a[href^='/vapps/wms/Asset/Asset/FindSummary']"
    Find_option = By.ID, "AssetSummary_hdialog_button"
    Product_ID = By.ID, "AssetSummary_header_pseudoId"
    Asset_find_button = By.ID, "AssetSummary_header_findButton"
    title = By.CSS_SELECTOR, "h1[class='content-title']"
    Detail_button = By.ID, "AssetSummary_assetsLink_0_findAsset"
    Detail = By.ID, "ListAssets_submitButton_0_assetDetail"
    Detail_History = By.XPATH, "//*[@id='AssetPanel-tabpanel']/ul/li[2]/a"
    Asset_Detail = By.XPATH, "//*[@id='AssetPanel-tabpanel']/ul/li[1]/a"
    Status = By.XPATH, "//*[@id='AssetPanel-tabpanel']/div/div/div[2]/span/ul/li[3]/form/button"
    status_t = By.XPATH, "//p[@class='text-inline text-success']"
    Move = By.XPATH, "//*[@id='AssetPanel-tabpanel']/ul/li[3]/a"
    move_head = By.CSS_SELECTOR, "h1[class='content-title']"

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
        return self.do_send_keys(self.Product_ID, 19)

    def get_asset_find_button(self):
        return self.do_click(self.Asset_find_button)

    def get_page_title(self):
        return self.get_element_text(self.title)

    def get_detail_button(self):
        return self.do_click(self.Detail_button)

    def get_detail(self):
        return self.do_click(self.Detail)

    def get_Detail_history(self):
        return self.do_click(self.Detail_History)

    def get_Asset_Detail(self):
        return self.do_click(self.Asset_Detail)

    def get_status(self):
        return self.do_click(self.Status)

    def get_Alert(self):
        return self.confirmation_alert()

    def get_status_title(self):
        return self.driver.find_element(*self.status_t)

    def get_move(self):
        return self.do_click(self.Move)

    def get_move_head(self):
        return self.get_element_text(self.move_head)
