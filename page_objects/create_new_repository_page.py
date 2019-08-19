from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from page_objects.repository_page import NewRepositoryPage
import random


class CreateNewRepository(object):
    """
    Test Adaptation layer
    """

    def __init__(self, web_driver: WebDriver):
        # Initialize web driver
        self.web_driver = web_driver
        self.repository_owner_button = WebDriverWait(self.web_driver, 25).until(
            expected_conditions.visibility_of_element_located((By.ID, "repository-owner"))
        )

        self.github_logo = self.web_driver.find_element_by_css_selector("svg")
        self.create_repository_inscription = self.web_driver.find_element_by_xpath("//h2[@class='Subhead-heading']")
        self.create_repository_name = self.web_driver.find_element_by_css_selector(
            "input[aria-describedby='repo-name-suggestion']")
        self.create_repository_button = self.web_driver.find_element_by_xpath(
            "//*[@class='js-with-permission-fields']/button")

    def name_of_repository(self):
        random_string = random.randint(100, 9999)
        self.create_repository_name.send_keys(f"hop_{random_string}_letter")
        return CreateNewRepository

    def click_on_create_repository_button(self):
        self.create_repository_button = WebDriverWait(self.web_driver, 25).until(
            expected_conditions.element_to_be_clickable(
                (By.XPATH, "//*[@class='js-with-permission-fields']/button"))).click()
        return NewRepositoryPage(self.web_driver)
