
class landing_page:

    def __init__(self, driver):
        self.driver = driver

        self.landing_page_xpath = "//h2"

    def is_landing_page_displayed(self):
        return self.driver.find_element_by_xpath(self.landing_page_xpath).is_displayed()