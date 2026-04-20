
class login_page:
    login_page_xpath = "//h2[@id='login-heading']"
    username_field_xpath = "//input[@id='login-email']"
    password_field_xpath = "//input[@id='login-password']"
    login_button_xpath = "//button[@id='login-submit']"

    def __init__(self, driver):
        self.driver = driver

    def verify_login_page(self):
        self.driver.find_element_by_xpath(self.login_page_xpath).is_displayed()

    def enter_username(self, username):
        self.driver.find_element_by_xpath(self.username_field_xpath).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_xpath(self.password_field_xpath).send_keys(password)

    def click_login_button(self):
        self.driver.find_element_by_xpath(self.login_button_xpath).click()