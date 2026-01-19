import pytest
import json
from Pages.login_page import LoginPage
from Pages.register_page import RegisterPage
from Data.test_login_data import TestData
from Utilities.logger import get_logger

logger = get_logger("TestRegister")

with open("Data/test_register_data.json", encoding="utf-8") as f:
    test_data = json.load(f)

class TestRegister:

    @pytest.mark.smoke
    def test_register_ok(self, driver):
        logger.info("Ejecutando registro válido")
        login = LoginPage(driver)
        login.load_page()
        login.register()
        assert login.is_register_succesfully()
        register = RegisterPage(driver)
        register.complete_form(test_data)
        assert register.is_completed_form_successfully()

    @pytest.mark.negative
    def test_register_mismatch(self, driver):
        logger.info("Ejecutando registro con 2 contraseñas distintas")
        login = LoginPage(driver)
        login.load_page()
        login.register()
        assert login.is_register_succesfully()
        register = RegisterPage(driver)
        register.complete_form(test_data)
        assert register.is_confirm_password_not_same()
        
