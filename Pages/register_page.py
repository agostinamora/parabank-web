from Pages.base_page import BasePage
from Utilities.config import Config
from Locators.register_locators import RegisterLocators

class RegisterPage(BasePage):

    _FIELD_LOCATORS = {
        "first_name": RegisterLocators.first_name_input,
        "last_name": RegisterLocators.last_name_input,
        "address": RegisterLocators.address_input,
        "city": RegisterLocators.city_input,
        "state": RegisterLocators.state_input,
        "zip": RegisterLocators.zip_input,
        "phone": RegisterLocators.phone_input,
        "ssn": RegisterLocators.ssn_input,
        "username": RegisterLocators.username_input,
        "password": RegisterLocators.password_input,
        "confirm": RegisterLocators.confirm_password_input
    }

    def complete_form(self, form_data: dict):
        self.logger.info("Completando el form")
        for field, value in form_data.items():
            locator = self._FIELD_LOCATORS.get(field)
            if locator:
                self.type(locator, value)
        self.click(RegisterLocators.register_button)

    def is_completed_form_successfully(self):
        visible = self.is_element_visible(RegisterLocators.welcome_text)
        messageOk = self.get_text(RegisterLocators.welcome_text)
        if visible:
            self.logger.info(f"Registro exitoso: {messageOk}")
        else:
            message = self.get_text(RegisterLocators.random_error_message)
            self.logger.warning(f"Registro NO exitoso, aparece este mensaje: {message}" )
        return visible
    
    def is_confirm_password_not_same(self):
        visible = self.is_element_visible(RegisterLocators.mismatch_password)
        messagePass = self.get_text(RegisterLocators.mismatch_password)
        if visible:
            self.logger.info(f"La contraseña no es la misma: {messagePass}")
        else:
            self.logger.warning("La contraseña es la misma")
        return visible
