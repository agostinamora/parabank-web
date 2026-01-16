import pytest
from Pages.login_page import LoginPage
from Data.test_data import TestData
from Utilities.logger import get_logger

logger = get_logger("TestLogin")


class TestLogin:

    @pytest.mark.smoke
    def test_login_ok(self, driver):
        logger.info("Ejecutando login válido")
        login = LoginPage(driver)
        login.load_page()
        login.login(TestData.valid_user, TestData.valid_password)
        assert login.is_login_successful()

    @pytest.mark.negative
    def test_login_invalid_password(self, driver):
        logger.info("Ejecutando login con usuario inválido")
        login = LoginPage(driver)
        login.load_page()
        login.login(TestData.invalid_user, TestData.valid_password)
        assert login.is_login_failed()
        
