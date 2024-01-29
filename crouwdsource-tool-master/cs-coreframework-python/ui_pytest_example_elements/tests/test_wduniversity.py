import time
import pytest

from framework.core.utils.logger_factory import LoggerFactory
from ui_pytest_example_elements.pageobjects.actions.WDUniversity import WDUniversity
from ui_pytest_example_elements.pageobjects.verifications.WDUniversityVerification import WDUniversityVerification

logger = LoggerFactory.get_logger("TEST")


class PageObjects:
    """
    Class to create single object of application to access all the pages and supported functions
    """
    def __init__(self, driver, prop):
        self.properties = prop
        self.driver = driver
        self.home = WDUniversity(driver)
        self.home_verify = WDUniversityVerification(driver)
        self.base_url = prop.environment_prop["test.baseURI1.wduniverisity.home"].data
        self.path_url = prop.environment_prop["test.baseURI2.wduniversity.optionpage"].data


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


class TestWDUniversity:

    # @pytest.mark.skip
    def test_open_wd_university(self, app):
        app.home.open_url(app.base_url)
        assert app.home.get_title() == "WebDriverUniversity.com"

    @pytest.mark.skip
    def test_open_wd_dropdown_checkbox_radio(self, app):
        app.home.open_url(app.path_url)
        assert app.home.get_title() == "WebDriver DD | Dropdown Menu(s) | Checkboxe(s) | Radio Button(s)"

    @pytest.mark.skip
    def test_dropdown(self, app):
        app.home.open_url(app.path_url)

        # Select by index
        app.home.drop_down_select_item_by_index_ddn_menu_1(2)
        # get selected value
        assert app.home.drop_down_get_selected_value_ddn_menu_1() == "c#"

        # get selected text
        assert app.home.drop_down_get_selected_text_ddn_menu_2() == "Eclipse"

        # select by value
        app.home.drop_down_select_item_by_value_ddn_menu_2("junit")

        # get selected value
        assert app.home.drop_down_get_selected_value_ddn_menu_2() == "junit"

        # select by text
        app.home.drop_down_select_item_by_text_ddn_menu_3("JavaScript")

        assert app.home.drop_down_get_selected_text_ddn_menu_3() == "JavaScript"

    @pytest.mark.skip
    def test_checkbox(self, app):
        app.home.open_url(app.path_url)

        # deselecting checkbox when its already not selected - no change - dynamic locator
        app.home.deselect_option_chk_options_dynamic("1")
        time.sleep(3)

        # selecting checkbox - dynamic locator.
        app.home.select_option_chk_options_dynamic("1")
        time.sleep(3)

        # checking if checkbox checked - dynamic locator
        assert app.home.is_option_selected_chk_options_dynamic("1") == True

        # deselecting checkbox - dynamic locator
        app.home.deselect_option_chk_options_dynamic("1")
        time.sleep(3)

        assert app.home.is_option_selected_chk_options_dynamic("1") == False

        # getting checkbox attribute
        assert app.home.get_attribute_chk_options_dynamic("value", "3") == "option-3"

    @pytest.mark.skip
    def test_radiobutton(self, app):
        app.home.open_url(app.path_url)

        # Selecting radio button
        app.home.click_rbtn_radiobuttons_dynamic("1")

        assert app.home.is_option_selected_rbtn_radiobuttons_dynamic("1") == True

        app.home.click_rbtn_radiobuttons_dynamic("2")

        assert app.home.is_option_selected_rbtn_radiobuttons_dynamic("1") == False

        assert app.home.get_attribute_rbtn_radiobuttons_dynamic("value", "3") == "yellow"
        time.sleep(4)

    @pytest.mark.skip
    def test_selected_disabled(self, driver):
        page = PageObjects(driver)
        app.home.open_url(app.path_url)

        # Checking if an option is selection or not
        assert app.home.is_option_selected_rbtn_radio_selected_disabled_dynamic("1") == False
        # checking if an option is disabled or not
        assert app.home.get_attribute_rbtn_radio_selected_disabled_dynamic("disabled", "2") == "true"
        # Checking if an option is selection or not
        assert app.home.is_option_selected_rbtn_radio_selected_disabled_dynamic("3") == True




