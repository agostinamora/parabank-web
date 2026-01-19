from selenium.webdriver.common.by import By

class RegisterLocators:

    table_form = (By.XPATH,'//table[@class = "form2"]')
    first_name_input = (By.XPATH, '//input[@id="customer.firstName"]')
    last_name_input = (By.XPATH, '//input[@id="customer.lastName"]')
    address_input = (By.XPATH, '//input[@id="customer.address.street"]')
    city_input = (By.XPATH, '//input[@id="customer.address.city"]')
    state_input = (By.XPATH, '//input[@id="customer.address.state"]')
    zip_input = (By.XPATH, '//input[@id="customer.address.zipCode"]')
    phone_input = (By.XPATH, '//input[@id="customer.phoneNumber"]')
    ssn_input = (By.XPATH, '//input[@id="customer.ssn"]')
    username_input = (By.XPATH, '//input[@id="customer.username"]')
    password_input = (By.XPATH, '//input[@id="customer.password"]')
    confirm_password_input = (By.XPATH, '//input[@id="repeatedPassword"]')
    register_button = (By.XPATH, '//input[@value = "Register"]')
    welcome_text = (By.XPATH, '//h1[contains(text(), "Welcome")]//following-sibling::p')
    mismatch_password = (By.XPATH, '//span[@id = "repeatedPassword.errors"]')
    random_error_message = (By.XPATH,'//p[@class = "error"]')

    
    