import os
from datetime import datetime

SCREENSHOT_DIR = "screenshots"
os.makedirs(SCREENSHOT_DIR, exist_ok=True)

def take_screenshot(driver, test_name):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file_name = f"{test_name}_{timestamp}.png"
    file_path = os.path.join(SCREENSHOT_DIR, file_name)

    driver.save_screenshot(file_path)
    return file_path

