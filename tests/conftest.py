import pytest
from selenium import webdriver


# Fixture to set up the WebDriver based on the browser name provided
@pytest.fixture
def setup(browser):
    # Initialize the WebDriver based on the browser name
    if browser.lower() == 'chrome':
        driver = webdriver.Chrome()

    elif browser.lower() == 'edge':
        driver = webdriver.Edge()

    else:
        driver = webdriver.Safari()

    # Return the WebDriver instance
    return driver


# Hook to add a custom command-line option for specifying the browser
def pytest_addoption(parser):
    # Add a command-line option "--browser" to specify the browser
    parser.addoption("--browser", action="store", default="chrome", help="Browser name")

# Fixture to retrieve the browser name from the command-line option
@pytest.fixture()
def browser(request):
    # Get the value of the "--browser" option
    return request.config.getoption("--browser")

@pytest.fixture
def setup(browser):
    if browser.lower() == "chrome":
        driver = webdriver.Chrome()
    yield driver
    driver.quit()
