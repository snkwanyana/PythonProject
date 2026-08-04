import pytest
from selenium import webdriver
from selenium.common.exceptions import WebDriverException


# Fixture to set up the WebDriver based on the browser name provided
@pytest.fixture
def setup(browser):
    # Initialize the WebDriver based on the browser name
    if browser.lower() == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        try:
            driver = webdriver.Chrome(options=options)
        except WebDriverException as exc:
            pytest.skip(f"Chrome WebDriver unavailable: {exc}")

    elif browser.lower() == 'edge':
        try:
            driver = webdriver.Edge()
        except WebDriverException as exc:
            pytest.skip(f"Edge WebDriver unavailable: {exc}")

    else:
        try:
            driver = webdriver.Safari()
        except WebDriverException as exc:
            pytest.skip(f"Safari WebDriver unavailable: {exc}")

    # Return the WebDriver instance
    return driver


# Hook to add a custom command-line option for specifying the browser
def pytest_addoption(parser):
    # Add a command-line option "--browser" to specify the browser
    parser.addoption("--browser", default="chrome")


# Fixture to retrieve the browser name from the command-line option
@pytest.fixture()
def browser(request):
    # Get the value of the "--browser" option
    return request.config.getoption("--browser")
