from Pages.base_page import BasePage
from Utilities.config import Config
from Locators.transfer_locators import TransferLocators

class TransferPage(BasePage):

    def enter_transer_section(self):
        self.logger.info("Elección de sección de transferencias")
        self.click(TransferLocators.transfer_fund_button)

    def is_transfer_section_ok(self):
        visible = self.is_element_visible(TransferLocators.transfer_funds_title)
        if visible:
            self.logger.info(f"Nos encontramos en la página de transfernecias")
        else:
            message = self.get_text(TransferLocators.random_error_message)
            self.logger.warning(f"Error al entrar a la página de transferencias, aparece este mensaje: {message}" )
        return visible
    
    def make_a_transfund(self):
        self.type(TransferLocators.amount_input, "20000")
        self.click(TransferLocators.transfer_button)

    def is_transfund_successfull(self):
        visible = self.is_element_visible(TransferLocators.transfer_ok_title)
        messageOk = self.get_text(TransferLocators.confirmation_transfund_text)
        if visible:
            self.logger.info(f"Tranferencia exitosa: {messageOk}")
        else:
            message = self.get_text(TransferLocators.random_error_message)
            self.logger.warning(f"No se pudo completar la transferencia, aparece este mensaje: {message}" )
        return visible