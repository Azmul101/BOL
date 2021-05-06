from Utilities.BaseClass import BaseClass
from Pages.Return_List import ReturnList
import time
from selenium.common.exceptions import NoSuchElementException


class Test_eighteen(BaseClass):
    def test_eighteen(self):
        try:
            log = self.getlogger()  # For log file
            Order = ReturnList(self.driver)  # Call the page class
            log.info("Login into system")
            Order.login()
            log.info("Click on the menu list")
            Order.get_side_menu()
            log.info("Click on find option")
            Order.get_find_option()
            log.info("Click on find button")
            Order.get_find_button()
            log.info("Return List Screen")
            Order.get_order_list()
            flag = Order.get_Order_title
            assert flag
            Order.get_side_menu()
            Order.get_return_list()
            flag = Order.get_Order_title
            assert flag
            time.sleep(5)
        except:
            raise NoSuchElementException("Case is broken")
