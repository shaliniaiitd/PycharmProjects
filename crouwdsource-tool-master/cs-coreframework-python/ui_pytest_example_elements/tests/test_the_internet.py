import time
import pytest

from framework.core.utils.logger_factory import LoggerFactory
from ui_pytest_example_elements.pageobjects.actions.HomePage import HomePage
from ui_pytest_example_elements.pageobjects.verifications.HomePageVerification import HomePageVerification

logger = LoggerFactory.get_logger("TEST")


class PageObjects:

    def __init__(self, driver, prop):
        self.driver = driver
        self.prop = prop
        self.home = HomePage(driver)
        self.home_verify = HomePageVerification(driver)
        self.base_url = prop.environment_prop["test.baseURI3.theinternet.home"].data
        self.path_url_dynamic_loading = prop.environment_prop["test.baseURI4.theinternet.dynamicloading"].data


class TestTheInternet:

    @pytest.mark.skip
    def test_dynamic_loading(self, driver, prop):
        page = PageObjects(driver, prop)
        page.home.open_url(page.path_url_dynamic_loading)
        logger.info(" --- first phase --- ")

        assert page.home_verify.is_present_btn_start_loading() is True
        assert page.home_verify.is_present_div_loading() is False
        assert page.home_verify.is_present_lb_hello_world() is False

        assert page.home.get_text_lb_hello_world() == "Hello World"

        logger.info(" --- second phase --- ")

        page.home.click_btn_start_loading()

        assert page.home.verify.is_displayed(page.home.btn_start_loading) == False
        assert page.home.verify.is_displayed(page.home.div_loading) == True
        assert page.home.verify.is_displayed(page.home.lb_hello_world) == False

        time.sleep(4)
        logger.info(" --- third phase --- ")

        assert page.home.locate.get_element(page.home.btn_start_loading).is_displayed() == False
        assert page.home.locate.get_element(page.home.div_loading).is_displayed() == False
        assert page.home.locate.get_element(page.home.lb_hello_world).is_displayed() == True

        time.sleep(3)

    # @pytest.mark.skip
    def test_open_form_authentication(self, driver, prop):
        page = PageObjects(driver, prop)
        page.home.open_url(page.base_url)
        time.sleep(5)
        assert page.home.get_title() == "The Internet"

    @pytest.mark.skip
    def test_validate_link_textbox_label(self, driver, prop):
        page = PageObjects(driver, prop)

        page.home.open_url(page.base_url)

        # # link
        # getText
        assert page.home.get_text_link_form_authentication() == "Form Authentication"

        # click
        page.home.click_link_form_authentication()

        # #text box
        # setText
        page.home.input_text_tb_form_username("Hello Team")

        # getText
        assert page.home.get_value_tb_form_username() == "Hello Team"

        # clearText
        page.home.clear_value_tb_form_username()
        assert page.home.get_value_tb_form_username() == ''

        # getAttribute
        assert page.home.get_attribute_tb_form_username("type") == "text"

        # label
        assert "Login Page" == page.home.get_text_lb_h2()

    @pytest.mark.skip
    def test_validate_checkbox(self, driver, prop):
        page = PageObjects(driver, prop)

        # page.home.open_url(page.base_url)
        page.home.open_url(page.base_url)
        page.home.click_link_dynamic_page_link_dynamic("checkboxes")

        # # checkbox

        # isChecked
        assert page.home.is_option_selected_chk_checkbox_1() == False
        assert page.home.is_option_selected_chk_checkbox_2() == True

        # check
        page.home.select_option_chk_checkbox_1()
        # uncheck
        page.home.deselect_option_chk_checkbox_2()

        # getAttribute
        assert str(page.home.get_attribute_chk_checkbox_1("checked")) == "true"
        assert page.home.get_attribute_chk_checkbox_2("checked") is None

        assert "The Internet" == page.home.get_title()

    @pytest.mark.skip
    def test_validate_dropdown(self, driver, prop):
        page = PageObjects(driver, prop)
        page.home.open_url(page.base_url)
        page.home.click_link_dynamic_page_link_dynamic("dropdown")

        # # Drop Down

        # selectByIndex
        page.home.drop_down_select_item_by_index_ddn_dropdown_1(1)
        time.sleep(3)
        # selectByValue
        page.home.drop_down_select_item_by_value_ddn_dropdown_1("2")
        time.sleep(3)
        # selectByText
        page.home.drop_down_select_item_by_text_ddn_dropdown_1("Option 1")
        time.sleep(3)

        # getSelectedValue
        assert page.home.drop_down_get_selected_value_ddn_dropdown_1() == "1"
        # getSelectedText
        assert page.home.drop_down_get_selected_text_ddn_dropdown_1() == "Option 1"
