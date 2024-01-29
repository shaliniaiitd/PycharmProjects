"""
This module contains all common action methods.
"""
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import TimeoutException

from framework.core.common.decorators import handle_on_exceptions
from framework.core.utils.logger_factory import LoggerFactory
from framework.ui.base.base_locator import Locator
from framework.ui.base.base_wait import Wait
from framework.ui.constants.ui_constants import ErrorMessages as EM

logger = LoggerFactory.get_logger()
ELEM_NOT_FOUND_MSG = EM.GENERAL_ELEMENT_NOT_FOUND


class BaseActions:

    def __init__(self, driver):
        self.driver = driver
        self.locate = Locator(driver)
        self.wait = Wait(driver)

    @handle_on_exceptions(exceptions=TimeoutException, msg_on_exception=ELEM_NOT_FOUND_MSG)
    def input_text(self, locator_string, input_text):
        self.wait.wait_for_element_until_clickable(locator_string).send_keys(input_text)
        return self

    @handle_on_exceptions(exceptions=TimeoutException, msg_on_exception=ELEM_NOT_FOUND_MSG)
    def clear_value(self, locator_string):
        self.wait.wait_for_element_until_clickable(locator_string).clear()
        return self

    @handle_on_exceptions(exceptions=TimeoutException, msg_on_exception=ELEM_NOT_FOUND_MSG)
    def get_value(self, locator_string):
        return self.wait.wait_for_element_until_clickable(locator_string).get_attribute("value")

    @handle_on_exceptions(exceptions=TimeoutException, msg_on_exception=ELEM_NOT_FOUND_MSG)
    def get_text(self, locator_string):
        return self.wait.wait_for_element_until_clickable(locator_string).text

    @handle_on_exceptions(exceptions=TimeoutException, msg_on_exception=ELEM_NOT_FOUND_MSG)
    def click(self, locator_string):
        self.wait.wait_for_element_until_clickable(locator_string).click()
        return self

    @handle_on_exceptions(exceptions=TimeoutException, msg_on_exception=ELEM_NOT_FOUND_MSG)
    def double_click(self, locator_string):
        elem = self.wait.wait_for_element_until_clickable(locator_string)
        elem.click()
        elem.click()
        return self

    @handle_on_exceptions(exceptions=TimeoutException, msg_on_exception=ELEM_NOT_FOUND_MSG)
    def drop_down_select_item_by_index(self, locator_string, id):
        Select(self.wait.wait_for_element_until_clickable(locator_string)).select_by_index(id - 1)
        return self

    @handle_on_exceptions(exceptions=TimeoutException, msg_on_exception=ELEM_NOT_FOUND_MSG)
    def drop_down_select_item_by_value(self, locator_string, value):
        Select(self.wait.wait_for_element_until_clickable(locator_string)).select_by_value(value)
        return self

    @handle_on_exceptions(exceptions=TimeoutException, msg_on_exception=ELEM_NOT_FOUND_MSG)
    def drop_down_select_item_by_text(self, locator_string, text):
        Select(self.wait.wait_for_element_until_clickable(locator_string)).select_by_visible_text(text)
        return self

    @handle_on_exceptions(exceptions=TimeoutException, msg_on_exception=ELEM_NOT_FOUND_MSG)
    def drop_down_get_selected_value(self, locator_string):
        return Select(self.wait.wait_for_element_until_clickable(locator_string)).first_selected_option.get_attribute(
            "value")

    @handle_on_exceptions(exceptions=TimeoutException, msg_on_exception=ELEM_NOT_FOUND_MSG)
    def drop_down_get_selected_text(self, locator_string):
        return Select(self.wait.wait_for_element_until_clickable(locator_string)).first_selected_option.text

    @handle_on_exceptions(exceptions=TimeoutException, msg_on_exception=ELEM_NOT_FOUND_MSG)
    def combo_box_deselect_item_by_index(self, locator_string, id):
        Select(self.wait.wait_for_element_until_clickable(locator_string)).deselect_by_index(id - 1)
        return self

    @handle_on_exceptions(exceptions=TimeoutException, msg_on_exception=ELEM_NOT_FOUND_MSG)
    def combo_box_deselect_item_by_value(self, locator_string, value):
        Select(self.wait.wait_for_element_until_clickable(locator_string)).deselect_by_value(value)
        return self

    @handle_on_exceptions(exceptions=TimeoutException, msg_on_exception=ELEM_NOT_FOUND_MSG)
    def combo_box_deselect_item_by_text(self, locator_string, text):
        Select(self.wait.wait_for_element_until_clickable(locator_string)).deselect_by_visible_text(text)
        return self

    @handle_on_exceptions(exceptions=TimeoutException, msg_on_exception=ELEM_NOT_FOUND_MSG)
    def combo_box_is_multiple_select(self, locator_string):
        return Select(self.wait.wait_for_element_until_clickable(locator_string)).is_multiple

    @handle_on_exceptions(exceptions=TimeoutException, msg_on_exception=ELEM_NOT_FOUND_MSG)
    def combo_box_deselect_all_items(self, locator_string):
        combo_box = Select(self.wait.wait_for_element_until_clickable(locator_string))
        if combo_box.is_multiple:
            combo_box.deselect_all()
            return self
        else:
            raise Exception("Drop down is not multiple select")

    @handle_on_exceptions(exceptions=TimeoutException, msg_on_exception=ELEM_NOT_FOUND_MSG)
    def combo_box_get_all_selected_values(self, locator_string):
        return [x.get_attribute("value") for x in
                Select(self.wait.wait_for_element_until_clickable(locator_string)).all_selected_options]

    @handle_on_exceptions(exceptions=TimeoutException, msg_on_exception=ELEM_NOT_FOUND_MSG)
    def combo_box_get_all_selected_texts(self, locator_string):
        return [x.text for x in Select(self.wait.wait_for_element_until_clickable(locator_string)).all_selected_options]

    @handle_on_exceptions(exceptions=TimeoutException, msg_on_exception=ELEM_NOT_FOUND_MSG)
    def get_attribute(self, locator_string, attribute):
        return self.wait.wait_for_element_until_clickable(locator_string).get_attribute(attribute)

    @handle_on_exceptions(exceptions=TimeoutException, msg_on_exception=ELEM_NOT_FOUND_MSG)
    def get_property(self, locator_string, prop_name):
        return self.wait.wait_for_element_until_clickable(locator_string).get_property(prop_name)

    @handle_on_exceptions(exceptions=TimeoutException, msg_on_exception=ELEM_NOT_FOUND_MSG)
    def get_value_of_css_property(self, locator_string, css_property):
        return self.wait.wait_for_element_until_clickable(locator_string).value_of_css_property(css_property)

    @handle_on_exceptions(exceptions=TimeoutException, msg_on_exception=ELEM_NOT_FOUND_MSG)
    def select_option(self, locator_string):
        option = self.wait.wait_for_element_until_clickable(locator_string)
        option.click()

    @handle_on_exceptions(exceptions=TimeoutException, msg_on_exception=ELEM_NOT_FOUND_MSG)
    def deselect_option(self, locator_string):
        option = self.wait.wait_for_element_until_clickable(locator_string)
        if option.get_attribute("checked"):
            option.click()

    @handle_on_exceptions(exceptions=TimeoutException, msg_on_exception=ELEM_NOT_FOUND_MSG)
    def is_option_selected(self, locator_string):
        option = self.wait.wait_for_element_until_clickable(locator_string)
        if option.get_attribute("checked"):
            return True
        return False

    @handle_on_exceptions(exceptions=TimeoutException, msg_on_exception=ELEM_NOT_FOUND_MSG)
    def is_element_selected(self, locator_string):
        return self.wait.wait_for_element_until_clickable(locator_string).is_selected()

    @handle_on_exceptions(exceptions=TimeoutException, msg_on_exception=ELEM_NOT_FOUND_MSG)
    def is_attribute_present(self, locator_string, attribute_name):
        att_value = self.wait.wait_for_element_until_clickable(locator_string).getAttribute(attribute_name)
        if att_value is None or att_value == "" or att_value == " ":
            return False
        return True

    def switch_to_iframe_by_index(self, index):
        self.driver.switch_to.frame(index)
        return self

    def switch_to_iframe_by_name(self, name):
        self.driver.switch_to.frame(name)
        return self

    @handle_on_exceptions(exceptions=TimeoutException, msg_on_exception=ELEM_NOT_FOUND_MSG)
    def switch_to_iframe_by_element(self, locator_string):
        elem = self.wait.wait_for_element_until_clickable(locator_string)
        self.driver.switch_to.frame(elem)
        return self

    def switch_to_default_content(self):
        self.driver.switch_to.default_content()
        return self

    def switch_to_parent_frame(self):
        self.driver.switch_to.parent_frame()
        return self
