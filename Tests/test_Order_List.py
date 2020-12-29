
from TestData.Data import Testdata
from Pages.Order_List import Order_List
from Utilities.BaseClass import BaseClass


class Test_one(BaseClass):

    def test_order(self):
        log = self.getlogger()  # For log file
        Order = Order_List(self.driver)  # Call the page class
        Order.login()
        Order.orders()
        log.info("Click Order side menu")
        Order.get_find_element()
        Order.get_clear_param()
        Order.get_find()
        log.info("Orders showing in Descending")
        title = Order.get_title(Testdata.find_Option_page_title)
        assert title == Testdata.find_Option_page_title
        self.driver.refresh()
        Order.get_csv()
        Order.get_xls()
        Order.get_order()
        Create_Order_title = Order.get_create_order()
        assert Create_Order_title == Testdata.create_title
