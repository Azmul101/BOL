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
        time.sleep(10)
