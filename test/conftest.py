import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as fOptions

from page_objects.main_page import MainPage


"""
Test Execution Layer
"""


def pytest_addoption(parser):
    parser.addoption("--firefox",
                     action='store_true',
                     default=False,
                     help="Start Firefox WebDriver")
    parser.addoption("--ie",
                     action='store_true',
                     default=False,
                     help="Start Internet Explorer WebDriver")
    parser.addoption("--google-chrome",
                     action='store_true',
                     default=False,
                     help="Start Google Chrome WebDriver")
    parser.addoption("--webdriver-location",
                     action='store',
                     help="Where to get the webdriver")
    parser.addoption("--username",
                     action='store',
                     help="Username to login to DataCamp")
    parser.addoption("--password",
                     action='store',
                     help="Password to login to DataCamp")


@pytest.fixture(scope='class', autouse=True)
def web_driver_setup(request):
    request.cls.webdriver_path = request.config.getoption("--webdriver-location")

    if request.config.getoption("--firefox"):
        request.cls.webdriver = webdriver.Firefox
    elif request.config.getoption("--ie"):
        request.cls.webdriver = webdriver.Ie
    elif request.config.getoption("--google-chrome"):
        request.cls.webdriver = webdriver.Chrome
    else:
        raise ValueError("Incorrect browser")


@pytest.fixture(scope='function', autouse=True)
def load_app(request):
    if isinstance(request.cls.webdriver, webdriver.Chrome):
        chrome_options = Options()
        # chrome_options.add_argument("--headless")
        prefs = {"profile.default_content_setting_values.notifications": 2}
        chrome_options.add_experimental_option("prefs", prefs)
        request.instance.initialized_webdriver = request.cls.webdriver(executable_path=request.cls.webdriver_path,
                                                                       chrome_options=chrome_options)

    elif isinstance(request.cls.webdriver, webdriver.Firefox):
        _browser_profile = webdriver.FirefoxProfile()
        _browser_profile.set_preference("dom.webnotifications.enabled", False)
        _browser_profile.set_preference("dom.push"
                                        ".enabled", False)
        options = fOptions()
        # options.set_headless(headless=True)
        request.instance.initialized_webdriver = request.cls.webdriver(executable_path=request.cls.webdriver_path,
                                                                       firefox_options=options,
                                                                       firefox_profile=_browser_profile)
    else:
        request.instance.initialized_webdriver = request.cls.webdriver(executable_path=request.cls.webdriver_path)

    request.instance.main_page = MainPage(request.instance.initialized_webdriver)

    def driver_close():
        request.instance.initialized_webdriver.quit()

    request.addfinalizer(driver_close)


def pytest_generate_tests(metafunc):
    metafunc.parametrize("username, password", (
        (
            metafunc.config.getoption("--username"), metafunc.config.getoption("--password")
        ),
    )
                         )
