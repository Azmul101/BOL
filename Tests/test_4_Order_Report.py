import time

from Pages.Order_Report import report_order
from Utilities.BaseClass import BaseClass


class Test_Four(BaseClass):

    def test_report(self):
        log = self.getlogger()  # For log file
        Order = report_order(self.driver)  # Call the page class
        log.info("Login into system")
        Order.login()
        log.info("Go to side menu")
        Order.report()
        log.info("Go to report detail page")
        Order.get_select_store()
        log.info("Selecting the store")
        Order.get_store()
        Order.click_on_button()
        log.info("Downloading the CSV and XML files")
        Order.get_csv()
        Order.get_xls()
        log.info("CLick on Retrieve button")
        Order.get_retrieve().click()
        # buttons = Order.get_retrieve()
        # for button in buttons:
        #     if button.is_displayed():
        #         return button.click()
        # else:
        #     pass
        time.sleep(10)
        self.driver.refresh()
        time.sleep(10)
        status_message = Order.get_internal_status().text
        assert ("OrderApproved" in status_message)
