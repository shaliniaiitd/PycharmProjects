import pytest

from framework.core.utils.logger_factory import LoggerFactory
from ui_pytest_example_timesheet.pageobjects.actions.LoginPage import LoginPage
from ui_pytest_example_timesheet.pageobjects.actions.HomePage import HomePage
from ui_pytest_example_timesheet.pageobjects.verifications.LoginPageVerification import LoginPageVerification
from ui_pytest_example_timesheet.pageobjects.verifications.HomePageVerification import HomePageVerification

logger = LoggerFactory.get_logger("TEST")


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


class TestTimeSheet:

    # @pytest.mark.skip
    def test_open_timesheet(self, app):
        app.login.open_url(app.base_url)
        assert app.login.get_title() == "Online Timesheet • Qualitypointtech.com"

    @pytest.mark.skip
    def test_login_timesheet(self, app):
        app.login.open_url(app.base_url)
        app.login.input_text_tb_username("clbuser1")
        app.login.input_text_tb_password("password")
        app.login.click_btn_login()
        assert app.home_verify.is_text_link_welcome_username("clbuser1")

    # @pytest.mark.skip
    def test_my_profile_validate_joining_date(self, app):
        app.login.open_url(app.base_url)
        app.login.input_text_tb_username("clbuser1")
        app.login.input_text_tb_password("password")
        app.login.click_btn_login()
        app.home.click_btn_nav_my_profile()
        assert app.home_verify.is_value_tb_profile_doj("2021-06-01")

    # @pytest.mark.skip
    def test_my_profile_validate_last_name(self, app):
        app.login.open_url(app.base_url)
        app.login.input_text_tb_username("clbuser1")
        app.login.input_text_tb_password("password")
        app.login.click_btn_login()
        app.home.click_btn_nav_my_profile()
        assert app.home_verify.is_value_tb_profile_last_name("last_name")



