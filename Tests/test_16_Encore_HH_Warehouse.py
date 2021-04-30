from Pages.Encore_HH_Warehouse import Encore_HH
from Utilities.BaseClass import BaseClass
import time
from selenium.common.exceptions import NoSuchElementException


class Test_sixteen(BaseClass):
    def test_sixteen(self):
        try:
            log = self.getlogger()  # For log file
            Order = Encore_HH(self.driver)  # Call the page class
            log.info("Login into system")
            Order.login()
            log.info("Click on the menu link")
            Order.get_side_menu()
            log.info("Click on the menu list")
            time.sleep(5)
            log.info("Warehouse Select")
            Order.get_warehouse()
            Order.set_HH()
            log.info("Click on LookUp")
            Order.set_LookUp()
            Order.get_side_menu()
            log.info("Click on MoveProduct")
            Order.set_MoveProduct()
        except:
            raise NoSuchElementException("Case is broken")
