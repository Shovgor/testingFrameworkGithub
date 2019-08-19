from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from page_objects.create_new_repository_page import CreateNewRepository


class UserWorkSpacePage(object):
    """
        Test Adaptation Layer
    """

    def __init__(self, web_driver: WebDriver):
        # Initialize web driver
        self.web_driver = web_driver

        self.profile_button = WebDriverWait(self.web_driver, 25).until(
            expected_conditions.visibility_of_element_located(
                (By.CSS_SELECTOR, "summary[aria-label='View profile and more']"))
        )
        self.github_logo = self.web_driver.find_element_by_css_selector("svg")
        self.user_avatar = self.web_driver.find_element_by_css_selector("summary[aria-label='View profile and more']")
        self.start_a_project_button = self.web_driver.find_element_by_css_selector("a[class = 'btn shelf-cta mx-2 "
                                                                                   "mb-3']")

    def click_on_create_new_project(self):
        self.start_a_project_button.click()
        return CreateNewRepository(self.web_driver)
