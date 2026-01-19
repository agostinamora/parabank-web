from selenium.webdriver.common.by import By

class TransferLocators:

    transfer_fund_button = (By.XPATH,'//li//a[contains(text(), "Transfer Funds")]')
    random_error_message = (By.XPATH,'//p[@class = "error"]')
    transfer_funds_title = (By.XPATH, '//h1[contains(text(), "Transfer Funds")]')
    amount_input = (By.XPATH, '//input[@id = "amount"]')
    transfer_button = (By.XPATH, '//input[@value = "Transfer"]')
    transfer_ok_title = (By.XPATH, '//h1[contains(text(), "Transfer Complete!")]')
    confirmation_transfund_text = (By.XPATH, '//div[@id = "showResult"]//p//span')