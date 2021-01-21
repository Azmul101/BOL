from Pages.Shipment_List import Shipment_List
from TestData.Data import Testdata
from Utilities.BaseClass import BaseClass


class Test_Five(BaseClass):
    def test_five_shipment(self):
        log = self.getlogger()  # For log file
        Order = Shipment_List(self.driver)  # Call the page class
        log.info("Login into system")
        Order.login()
        log.info("Click on the menu link")
        Order.get_menu_link()
        Order.get_outgoing_shipment()
        outgoing = Order.get_outgoing_dialog()
        assert outgoing == Testdata.outgoing_title
        Order.get_outgoing_close()
        log.info("Incoming Shipment dialog box")
        Order.get_incoming_shipment()
        incoming = Order.get_incoming_dialog()
        assert incoming == Testdata.incoming_title
        Order.get_incoming_close()
        log.info("Transfer dialog box")
        Order.get_transfer_shipment()
        transfer = Order.get_transfer_text()
        assert transfer == Testdata.transfer_title
        Order.get_transfer_close()
        log.info("Load the shipment data")
        Order.get_find_element()
        Order.get_clear_param()
        Order.get_find()
        log.info("Shipment data is shown")
        Order.get_csv()
        title = Order.get_title(Testdata.csv_download)
        assert title == Testdata.csv_download
