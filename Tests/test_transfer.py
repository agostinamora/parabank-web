import pytest
from Pages.login_page import LoginPage
from Pages.transfer_page import TransferPage
from Utilities.logger import get_logger

logger = get_logger("TestTransfer")

class TestTransfer:

    @pytest.mark.order(2)
    @pytest.mark.smoke
    def test_transfund_ok(self, driver):
        logger.info("Ejecutando una transacción válida")
        login = LoginPage(driver)
        login.load_page()
        transfer= TransferPage(driver)
        transfer.enter_transer_section()
        assert transfer.is_transfer_section_ok()
        transfer.make_a_transfund()
        assert transfer.is_transfund_successfull()
        
