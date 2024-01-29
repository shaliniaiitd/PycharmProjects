import pytest

from framework.core.utils.logger_factory import LoggerFactory
# example action import. Please add/updates as per the generated poms.
# from ui_pytest.pageobjects.actions import HomePage
# example verification import.  Please add/updates as per the generated poms.
# from ui_pytest.pageobjects.verifications import HomePageVerifications
from ui_pytest.pageobjects.actions.HomePage import HomePage

logger = LoggerFactory.get_logger("TEST")


class PageObjects:

    def __init__(self, driver, prop):
        self.driver = driver
        self.prop = prop
        self.base_url = prop.environment_prop["test.baseURI3.theinternet.home"].data
        # associate page objects of actions and verification classes below. Example given below.
        self.home = HomePage(driver)  # example action object
        # self.home_verify = HomePageVerification(driver)  #example verification object




class TestClass:

    # @pytest.mark.skip # remove skip marker after completing the test function
    def test_dynamic_loading(self, driver, prop):
        page = PageObjects(driver, prop)
        # open page
        page.home.open_url(page.base_url)

        # assert page title
        assert page.home.get_title() == "The Internet"