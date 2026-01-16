from selenium.webdriver.common.by import By

class LoginLocators:

    username_input = (By.XPATH,'//input[@name="username"]')
    password_input = (By.XPATH,'//input[@name="password"]')
    login_button = (By.XPATH,'//input[@value="Log In"]')
    welcome_text = (By.XPATH,'//b[contains(text(), "Welcome")]')
    title_account_overview = (By.XPATH,'//h1[contains(text(),"Accounts Overview")]')
    error_text = (By.XPATH,'//p[contains(text(), "Please enter a username and password.")]')
    random_error_message = (By.XPATH,'//p[@class = "error"]')

    
    