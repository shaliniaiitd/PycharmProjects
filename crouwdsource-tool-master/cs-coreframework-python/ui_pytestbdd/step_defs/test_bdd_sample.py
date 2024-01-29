import pytest

from pytest_bdd import scenarios, given, when, then, parsers
from framework.core.utils.logger_factory import LoggerFactory
# example action import. Please add/updates as per the generated poms.
# from ui_pytestbdd.pageobjects.actions.LoginPage import LoginPage
# from ui_pytestbdd.pageobjects.actions.HomePage import HomePage
# from ui_pytestbdd.pageobjects.verifications.LoginPageVerification import LoginPageVerification
# from ui_pytestbdd.pageobjects.verifications.HomePageVerification import HomePageVerification


logger = LoggerFactory.get_logger("TEST")

# Scenarios
scenarios('../features/sample.feature')


class PageObjects:
    """
    Class to create single object of application to access all the pages and supported functions
    """

    def __init__(self, driver, prop):
        self.properties = prop
        self.driver = driver
        # self.login = LoginPage(driver)
        # self.home = HomePage(driver)
        # self.login_verify = LoginPageVerification(driver)
        # self.home_verify = HomePageVerification(driver)
        self.base_url = self.properties.environment_prop["test.baseURI1.example.home"].data


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

@given('the login page is loaded')
def open_login(app):
    # update code as per the page objects
    # app.login.open_url(app.base_url)
    pass


# When Steps
@when(parsers.parse('the user enter username as "{username}" and password as "{password}" and clicks login'))
def login(app, username,password):
    # update code as per the page objects
    # app.login.input_text_tb_username(username)
    # app.login.input_text_tb_password(password)
    # app.login.click_btn_login()
    pass


# Then Steps
@then('user should be navigated to homepage')
def user_logged_in(app):
    # update code as per the page objects
    # assert app.home.get_title()=="homepage"
    pass
