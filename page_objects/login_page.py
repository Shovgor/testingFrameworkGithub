from selenium.webdriver.remote.webdriver import WebDriver
from page_objects.user_workspace_page import UserWorkSpacePage


class LoginPage(object):
    """
        Test Adaptation Layer
    """

    def __init__(self, web_driver: WebDriver):
        # Initialize web driver
        self.web_driver = web_driver

        self.github_logo = self.web_driver.find_element_by_css_selector("svg")
        self.login_form = self.web_driver.find_element_by_css_selector('div[class="auth-form-body mt-3"]')
        self.username_field = self.web_driver.find_element_by_id("login_field")
        self.password_field = self.web_driver.find_element_by_id("password")
        self.sing_in_button = self.web_driver.find_element_by_css_selector("input[type='submit']")
        self.error_message = self.web_driver.find_elements_by_css_selector("#js-pjax-container .container")

    def enter_login(self, username):
        self.username_field.send_keys(username)
        return self

    def enter_password(self, password):
        self.password_field.send_keys(password)
        return self

    def click_on_login_button(self):
        self.sing_in_button.click()
        return UserWorkSpacePage(self.web_driver)

    def click_on_login_button_with_invalid_credential(self):
        self.sing_in_button.click()
        return LoginPage(self.web_driver)
