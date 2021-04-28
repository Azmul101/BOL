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
        except:
            raise NoSuchElementException("Case is broken")
