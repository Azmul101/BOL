from Pages.Warehouse_Asset_Detail import Warehouse_Detail
from Utilities.BaseClass import BaseClass
from TestData.Data import Testdata
import time
from selenium.common.exceptions import NoSuchElementException


class Test_Fourteen(BaseClass):
    def test_asset_detail(self):
        try:
            log = self.getlogger()  # For log file
            Order = Warehouse_Detail(self.driver)  # Call the page class
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
            log.info("Pass the value and click on find button")
            Order.get_asset_find_button()
            Create_title = Order.get_page_title()
            assert Create_title == Testdata.asset_title
            log.info("Assertion")
            Order.get_detail_button()
            log.info("Get Detail Button")
            Order.get_detail()
            Order.get_Detail_history()
            log.info("Click on History Button")
            time.sleep(3)
            # Second Case
            Order.get_Asset_Detail()
            log.info("Click on Asset Detail Button")
            Order.get_status()
            Order.get_Alert()
            log.info("Click on Status title")
            time.sleep(2)
            status_text = Order.get_status_title().text
            assert ("On Hold" in status_text)
            # Third Case
            Order.get_move()
            move_title = Order.get_move_head()
            # self.assertTrue('Asset | Asset Detail' in self.selenium.page_source)
            assert move_title == Testdata.move_heading
        except:
            raise NoSuchElementException("Case is broken")
