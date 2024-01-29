import pytest

from pytest_bdd import scenarios, given, when, then, parsers
from framework.core.utils.logger_factory import LoggerFactory
from ui_pytestbdd_example_timesheet.pageobjects.actions.LoginPage import LoginPage
from ui_pytestbdd_example_timesheet.pageobjects.actions.HomePage import HomePage
from ui_pytestbdd_example_timesheet.pageobjects.verifications.LoginPageVerification import LoginPageVerification
from ui_pytestbdd_example_timesheet.pageobjects.verifications.HomePageVerification import HomePageVerification


logger = LoggerFactory.get_logger("TEST")

# Scenarios
scenarios('../features/timesheet.feature')


class PageObjects:
    """
    Class to create single object of application to access all the pages and supported functions
    """

    def __init__(self, driver, prop):
        self.properties = prop
        self.driver = driver
        self.login = LoginPage(driver)
        self.home = HomePage(driver)
        self.login_verify = LoginPageVerification(driver)
        self.home_verify = HomePageVerification(driver)
        self.base_url = self.properties.environment_prop["test.baseURI1.timesheet.home"].data


# Fixtures
@pytest.fixture
def app(driver, prop):
    """
    Fixture to returns the app object containing all page objects of the application
    Args:
        driver: webdriver instance
        prop: properties instance

    Returns: app object containing all the page objects

    """
    pages = PageObjects(driver, prop)
    logger.info("-- Test Started --")
    yield pages
    del pages
    logger.info("-- Test Ended --")


# Given Steps

@given('the Timesheet home page is displayed')
def timesheet_home(app):
    app.login.open_url(app.base_url)


# When Steps
@when(parsers.parse('the user enter username as "{username}" and password as "{password}" and clicks login'))
def login(app, username,password):
    app.login.input_text_tb_username(username)
    app.login.input_text_tb_password(password)
    app.login.click_btn_login()


# Then Steps
@then('user should be navigated to welcome page')
def user_logged_in(app):
    assert app.home_verify.is_text_link_welcome_username("clbuser1")
