from selenium.webdriver.remote.webdriver import WebDriver
from page_objects.login_page import LoginPage
from page_objects.user_workspace_page import UserWorkSpacePage


class MainPage(object):
    """
    Test Adaptation Layer
    """
    def __init__(self, web_driver: WebDriver):
        # Initialize web driver
        self.web_driver = web_driver
        self.web_driver.maximize_window()
        self.web_driver.get("https://github.com/")

        # Instantiating web elements
        self.github_logo = self.web_driver.find_element_by_css_selector("svg")
        self.sing_in_button = self.web_driver.find_element_by_css_selector("a[href='/login']")
        self.sing_up_form = self.web_driver.find_element_by_css_selector("form[action='/join']")
        self.sign_up_button = self.web_driver.find_elements_by_xpath("a[href='/join?source=header-home']")

    def click_on_sing_in_button(self):
        self.sing_in_button.click()
        return LoginPage(self.web_driver)
