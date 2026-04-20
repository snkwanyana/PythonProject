import time

import allure
import pytest

from utils.config_properties import ReadConfig_CommonDetails


class TestLogin:
    dev_url = ReadConfig_CommonDetails().getDevUrl()
    username = ReadConfig_CommonDetails().getUsername()
    password = ReadConfig_CommonDetails().getPassword()


@pytest.mark.sanity
@allure.severity(allure.severity_level.CRITICAL)
def test_login_valid(self, setup):
    self.driver = setup
    self.driver.get(self.dev_url)
    self.driver.maximize_window()

    time.sleep(5)
