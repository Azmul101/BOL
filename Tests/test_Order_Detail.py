from Pages.Order_Detail import Order_detail
from Utilities.BaseClass import BaseClass


class Test_Two(BaseClass):
    def test_detail(self):
        log = self.getlogger()
        Order = Order_detail(self.driver)
        Order.login()
        Orders = Order.orders()
        log.info("Click Order side menu" + str(Orders))
