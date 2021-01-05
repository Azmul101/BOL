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
        title = Order.get_title(Testdata.order_aging_title)
        assert title == Testdata.order_aging_title


        # log.info("Text received from application is " + title)
        # assert ("Orders | Find Order" in title)
