from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class NewRepositoryPage(object):
    """
    Test Adaptation layer
    """

    def __init__(self, web_driver: WebDriver):
        # Initialize web driver
        self.web_driver = web_driver
        self.repository_owner_button = WebDriverWait(self.web_driver, 25).until(
            expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "a[target='_blank']"))
        )
        self.repository_name = self.web_driver.find_element_by_xpath("//a[@data-pjax='#js-repo-pjax-container']")
        self.github_logo = self.web_driver.find_element_by_css_selector("svg")
        self.read_the_guide_button = self.web_driver.find_element_by_xpath("//a[@class='btn btn-primary shelf-cta']")
