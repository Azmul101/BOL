from selenium.webdriver.common.by import By

from Pages.BasePage import Common


class Shipment_Detail(Common):
    # Locators
    menu_link = By.XPATH, "//ul[@id='collapse1']//li[8]"
    shipment = By.XPATH, "//tbody/tr[1]/td[1]/div[1]/a"
    item = By.XPATH, "//*[@id='ShipmentPanel-tabpanel']/ul/li[2]/a"
    issue_pack_button = By.XPATH, "//button[@id='PackItemContainer_0-button']"
    update_button = By.ID, "UpdateItemForm_0_submitButton_0"
    reserve_button = By.ID, "ItemReserveDialog_0_0-button"
    reserve_title = By.XPATH, "//h4[normalize-space()='Reserve']"
    pack_button = By.ID, "PackItemContainer_0-button"
    pack_qty_btn = By.ID, "PackItemForm_0_submitButton_0"
    shipment_link = By.XPATH, "//*[@id='ShipmentPanel-tabpanel']/ul/li[1]/a"
    pack_pdf = By.XPATH, "//a[@class='btn btn-primary btn-sm '][1]"
    insert_pdf = By.XPATH, "//a[@class='btn btn-primary btn-sm '][2]"
    label = By.ID, "RequestPkgLabelDialog_0-button"
    label_button = By.XPATH, "//button[.='Get Label Anyway']"

    # Constructor of the class
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        # Methods

    def login(self):
        return self.login_page()

    def get_menu_link(self):
        return self.do_click(self.menu_link)

    def get_shipment(self):
        return self.do_click(self.shipment)

    def get_item(self):
        return self.do_click(self.item)

    def get_button_text(self):
        if self.is_visible(self.issue_pack_button):
            return self.get_element_text(self.issue_pack_button)
        else:
            print("Button is not available")

    def get_update_button(self):
        return self.do_click(self.update_button)

    def get_reserve_button(self):
        return self.do_click(self.reserve_button)

    def get_reserve_text(self):
        if self.is_visible(self.reserve_title):
            return self.get_element_text(self.reserve_title)
        else:
            print("Reserve Button is not available")

    def get_pack_button(self):
        return self.do_click(self.pack_button)

    def get_pack_qty_btn(self):
        return self.do_click(self.pack_qty_btn)

    def get_shipment_link(self):
        return self.do_click(self.shipment_link)

    def get_pack_pdf(self):
        return self.do_click(self.pack_pdf)

    def get_insert_pdf(self):
        return self.do_click(self.insert_pdf)

    def get_shipment_label(self):
        return self.do_click(self.label)

    def get_label_button(self):
        return self.do_click(self.label_button)
