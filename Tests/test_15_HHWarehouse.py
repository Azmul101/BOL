from Pages.HH_Warehouse import HH_Warehouse
from Utilities.BaseClass import BaseClass
import time
from selenium.common.exceptions import NoSuchElementException


class Test_Fifteen(BaseClass):
    def test_fifteen(self):
        try:
            log = self.getlogger()  # For log file
            Order = HH_Warehouse(self.driver)  # Call the page class
            log.info("Login into system")
            Order.login()
            log.info("Click on the menu link")
            Order.get_side_menu()
            log.info("Click on the menu list")
            time.sleep(5)
            Order.get_warehouse()
            Order.get_set_Button()
            log.info("Set Warehouse")
            Order.get_Scan()
            Order.get_set_Button()
            log.info("Scan asset")
            Order.get_side_menu()
            log.info("Move Asset")
            Order.get_move()
            Order.get_side_menu()
            log.info("Receive direct")
            Order.get_direct()
        except:
            raise NoSuchElementException("Case is broken")
