from selenium.webdriver.support.wait import WebDriverWait


class home_page:
    main_login_button_xpath = "//div[@class='nav-user-section']"

    def __init__(self, driver):
        self.driver = driver

    def click_main_login_button(self):
        wait_for_element = WebDriverWait(self.driver, 10)
        wait_for_element.until(self.driver.find_element_by_xpath(self.main_login_button_xpath).click())