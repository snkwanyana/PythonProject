import time

import allure
import pytest
from selenium.common.exceptions import WebDriverException

from utils.config_properties import ReadConfig_CommonDetails


class Test_Login:
    dev_url = ReadConfig_CommonDetails().getDevUrl()
    username = ReadConfig_CommonDetails().getUsername()
    password = ReadConfig_CommonDetails().getPassword()

    @pytest.mark.sanity
#   @allure.severity(allure.severity_level.CRITICAL)
    def test_login(self, setup):
        self.driver = setup
        try:
            self.driver.get(self.dev_url)
        except WebDriverException as exc:
            pytest.skip(f"Test site unavailable: {exc}")
        self.driver.maximize_window()
        allure.attach(self.driver.get_screenshot_as_png(), name="Login Page", attachment_type=allure.attachment_type.PNG)

        time.sleep(5)
