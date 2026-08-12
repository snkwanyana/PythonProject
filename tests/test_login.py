
import allure
import pytest

from utils.LaunchBrowser import launch_browser
from utils.config_properties import ReadConfig_CommonDetails
from utils.LoginFunction import login
from pages.landing_page import landing_page


class TestLogin:
    dev_url = ReadConfig_CommonDetails().getDevUrl()
    username = ReadConfig_CommonDetails().getUsername()
    password = ReadConfig_CommonDetails().getPassword()


    @pytest.mark.sanity
    @pytest.mark.order(1)
#   @allure.severity(allure.severity_level.CRITICAL)
    def test_login(self, setup):

        self.driver = launch_browser(setup)
        login(self.driver, self.username, self.password)
        langing = landing_page(self.driver)
        langing.is_landing_page_displayed()
        allure.attach(self.driver.get_screenshot_as_png(), name="Login Positive", attachment_type=allure.attachment_type.PNG)

    @pytest.mark.sanity
    @pytest.mark.order(2)
    def test_invalid_login(self, setup):
        self.driver = launch_browser(setup)
        login(self.driver, self.username, self.password+"invalid")
        allure.attach(self.driver.get_screenshot_as_png(), name="Login Nagative", attachment_type=allure.attachment_type.PNG)
