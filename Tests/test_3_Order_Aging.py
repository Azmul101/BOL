import time

from Pages.Order_Aging import Order_aging
from TestData.Data import Testdata
from Utilities.BaseClass import BaseClass


class Test_Three(BaseClass):
    def test_aging(self):
        log = self.getlogger()
        Order = Order_aging(self.driver)
        Order.login()
        log.info("Go to Order Aging menu")
        Order.get_Order_aging()
        Order.get_facility()
        log.info("Select Facility")
        Order.get_button()
        log.info("Facility result are shown")
        Order.get_order()
        log.info("Go to Order list")
        flag = Order.get_page_title()
        assert flag
        time.sleep(5)
        # header = Order.get_page_title().text
        # print("Azmul" + header)
        # assert ("Orders | Find Order" in header)
