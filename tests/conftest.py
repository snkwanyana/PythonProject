import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller

#chromedriver_autoinstaller.install()


# Hook to add a custom command-line option for specifying the browser
def pytest_addoption(parser):
    # Add a command-line option "--browser" to specify the browser
    parser.addoption("--browser", action="store", default="chrome", help="Browser name")

# Fixture to retrieve the browser name from the command-line option
@pytest.fixture()
def browser(request):
    # Get the value of the "--browser" option
    return request.config.getoption("--browser")

# Fixture to set up the WebDriver based on the browser name provided
@pytest.fixture
def setup(browser):
    # Initialize the WebDriver based on the browser name
    if browser.lower() == 'chrome':
        options = Options()
        options.add_argument("--headless=new")  # modern headless mode
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-gpu")  # Additional flag for CI stability
        driver = webdriver.Chrome(options=options)

    elif browser.lower() == 'edge':
        driver = webdriver.Edge()

    else:
        driver = webdriver.Safari()

    # Yield the WebDriver instance and ensure cleanup
    yield driver
    driver.quit()
