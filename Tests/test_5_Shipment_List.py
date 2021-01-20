from Pages.Shipment_List import Shipment_List
from Utilities.BaseClass import BaseClass


class Test_Five(BaseClass):
    def test_five_shipment(self):
        log = self.getlogger()  # For log file
        Order = Shipment_List(self.driver)  # Call the page class
        log.info("Login into system")
        Order.login()
