from selenium import webdriver
from Utilities.config import Config

def get_driver():
    if Config.BROWSER == "chrome":
        driver = webdriver.Chrome()
    elif Config.BROWSER == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError("Browser no soportado")

    driver.maximize_window()
    return driver
