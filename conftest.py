import pytest
from Utilities.screenshots import take_screenshot
from Utilities.logger import get_logger
from Utilities.driver_factory import get_driver
import pytest
import pytest_html

logger = get_logger("PytestHooks")


@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            screenshot_path = take_screenshot(driver, item.name)

            extra = getattr(report, "extra", [])
            extra.append(pytest_html.extras.image(screenshot_path))
            report.extra = extra





