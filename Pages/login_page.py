from Pages.base_page import BasePage
from Utilities.config import Config
from Locators.login_locators import LoginLocators

class LoginPage(BasePage):

    def load_page(self):
        self.logger.info("Entrando a la página principal")
        self.open(f"{Config.BASE_URL}")

    def login(self, username, password):
        self.logger.info(f"Login con usuario: {username}")
        self.type(LoginLocators.username_input, username)
        self.type(LoginLocators.password_input, password)
        self.click(LoginLocators.login_button)

    def is_login_successful(self):
        visible = self.is_element_visible(LoginLocators.welcome_text)
        if visible:
            self.logger.info("Login exitoso: mensaje de bienvenida visible")
        else:
            message = self.get_text(LoginLocators.random_error_message)
            self.logger.warning(f"Mensaje de bienvenida NO visible, aparece este mensaje: {message}" )
        return visible

    def is_login_failed(self):
        visible = self.is_element_visible(LoginLocators.error_text)
        if visible:
            self.logger.info("Login exitoso: mensaje de error visible")
        else:
            message = self.get_text(LoginLocators.random_error_message)
            self.logger.warning(f"Mensaje de error NO visible, aparece este mensaje: {message}" )
        return visible

        

