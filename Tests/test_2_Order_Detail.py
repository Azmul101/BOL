import time

from Pages.Order_Detail import Order_detail
from Utilities.BaseClass import BaseClass


class Test_Two(BaseClass):
    def test_detail(self):
        log = self.getlogger()
        Order = Order_detail(self.driver)
        Order.login()
        log.info("Go to Order")
        Order.orders()
        log.info("Click Order side menu")
        Order.get_select_order()
        flag = Order.get_line_item()
        log.info("Line item verifying")
        assert flag
        flag = Order.get_address()
        assert flag
        credit_payment = Order.get_payment()
        log.info("payment amount  " + str(credit_payment))
        assert ("True" in str(credit_payment))
        flag = Order.get_buttons()
        log.info("Close button present")
        assert flag
        flag = Order.get_other_button()
        log.info("Other button present")
        assert flag
