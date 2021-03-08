import time

from Pages.Shipment_Details import Shipment_Detail
from TestData.Data import Testdata
from Utilities.BaseClass import BaseClass


class Test_Six(BaseClass):
    def test_six_shipment(self):
        log = self.getlogger()  # For log file
        Order = Shipment_Detail(self.driver)  # Call the page class
        log.info("Login into system")
        Order.login()
        log.info("Click on the menu link")
        Order.get_menu_link()
        Order.get_shipment()
        Order.get_item()
        text = Order.get_button_text()
        assert text == Testdata.issue_pack_button
        Order.get_update_button()
        Order.get_reserve_button()
        title = Order.get_reserve_text()
        assert title == Testdata.reserve
        Order.get_pack_button()
        Order.get_pack_qty_btn()
        time.sleep(10)
        Order.get_shipment_link()
        Order.get_pack_pdf()
        Order.get_insert_pdf()
        time.sleep(10)
        Order.get_shipment_label()
        Order.get_label_button()
