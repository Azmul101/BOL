from selenium.webdriver.common.by import By

from Pages.BasePage import Common


class Shipment_List(Common):
    # Locators
    menu_link = By.XPATH, "//ul[@id='collapse1']//li[8]"
    create_outgoing_shipment = By.CSS_SELECTOR, "[id='NewOutgoingShipmentDialog-button']"
    outgoing_dialog_text = By.CSS_SELECTOR, "div[id='NewOutgoingShipmentDialog'] h4[class='modal-title']"
    outgoing_close = By.CSS_SELECTOR, "div[id='NewOutgoingShipmentDialog'] button[type='button']"
    create_incoming_shipment = By.CSS_SELECTOR, "[id='NewIncomingShipmentDialog-button']"
    incoming_dialog_text = By.CSS_SELECTOR, "div[id='NewIncomingShipmentDialog'] h4[class='modal-title']"
    incoming_close = By.CSS_SELECTOR, "div[id='NewIncomingShipmentDialog'] button[type='button']"
    create_transfer_shipment = By.CSS_SELECTOR, "[id='NewTransferShipmentDialog-button']"
    transfer_dialog_text = By.CSS_SELECTOR, "div[id='NewTransferShipmentDialog'] h4[class='modal-title']"
    transfer_close = By.CSS_SELECTOR, "div[id='NewTransferShipmentDialog'] button[type='button']"
    find_button = By.CSS_SELECTOR, "[id='ShipmentList_hdialog_button']"
    clear = (By.CSS_SELECTOR, "div[class='col-sm-10'] button[name='clearParameters']")
    order_by = (By.CSS_SELECTOR, "//a[@class='selectivity-multiple-selected-item-remove']")
    find = (By.CSS_SELECTOR, "[id='ShipmentList_header_findButton']")
    csv = (By.XPATH, "//a[normalize-space()='CSV']")

    # Constructor of the class
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        # Methods
    def login(self):
        return self.login_page()

    def get_menu_link(self):
        return self.do_click(self.menu_link)

    def get_outgoing_shipment(self):
        return self.do_click(self.create_outgoing_shipment)

    def get_outgoing_dialog(self):
        return self.get_element_text(self.outgoing_dialog_text)

    def get_outgoing_close(self):
        return self.do_click(self.outgoing_close)

    def get_incoming_shipment(self):
        return self.do_click(self.create_incoming_shipment)

    def get_incoming_dialog(self):
        return self.get_element_text(self.incoming_dialog_text)

    def get_incoming_close(self):
        return self.do_click(self.incoming_close)

    def get_transfer_shipment(self):
        return self.do_click(self.create_transfer_shipment)

    def get_transfer_text(self):
        return self.get_element_text(self.transfer_dialog_text)

    def get_transfer_close(self):
        return self.do_click(self.transfer_close)

    def get_find_element(self):
        return self.do_click(self.find_button)

    def get_clear_param(self):
        return self.do_click(self.clear)

    def get_find(self):
        return self.do_click(self.find)

    def get_csv(self):
        return self.do_click(self.csv)
