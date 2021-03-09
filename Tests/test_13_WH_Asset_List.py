import time

from TestData.Data import Testdata
from Utilities.BaseClass import BaseClass
from Pages.Warehouse_Asset_List import Warehouse_List


class Test_Thirteen(BaseClass):
    def test_asset_list(self):
        log = self.getlogger()  # For log file
        Order = Warehouse_List(self.driver)  # Call the page class
        log.info("Login into system")
        Order.login()
        log.info("Click on the menu link")
        Order.get_side_menu()
        log.info("Click on the menu list")
        # First case
        Order.get_menu_list()
        log.info("Click on the asset button")
        Order.get_asset_button()
        log.info("Click on the Find Option button")
        Order.get_find_option()
        log.info("Click on the asset button")
        Order.get_asset_id()
        time.sleep(3)
        log.info("Pass the value and click on find button")
        Order.get_asset_find_button()
        Create_title = Order.get_page_title()
        assert Create_title == Testdata.asset_title
        # Second case
        Order.get_xls()
        Order.get_csv()
        time.sleep(3)
