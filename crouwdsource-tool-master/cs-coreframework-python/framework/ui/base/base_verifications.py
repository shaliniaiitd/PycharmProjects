"""
This module contains all common verification methods.
"""
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import NoSuchElementException

from framework.core.common.decorators import avoid_exceptions
from framework.core.utils.logger_factory import LoggerFactory
from framework.ui.base.base_locator import Locator
from framework.ui.base.base_wait import Wait

logger = LoggerFactory.get_logger()


class BaseVerifications:

    def __init__(self, driver):
        self.driver = driver
        self.locate = Locator(driver)
        self.wait = Wait(driver)

    def is_text(self, locator_string, expected_value):
        return self.locate.get_element(locator_string).text == expected_value

    def is_value(self, locator_string, expected_value):
        return self.locate.get_element(locator_string).get_attribute("value") == expected_value

    def is_attribute_value(self, locator_string, attribute_name, expected_value):
        return self.locate.get_element(locator_string).get_attribute(attribute_name) == expected_value

    def is_value_of_css_property(self, locator_string, css_property, expected_value):
        return self.locate.get_element(locator_string).value_of_css_property(
            css_property) == expected_value

    def is_property_value(self, locator_string, property_name, expected_value):
        return self.locate.get_element(locator_string).get_property(property_name) == expected_value

    def is_displayed(self, locator_string):
        return self.locate.get_element(locator_string).is_displayed()

    def is_not_displayed(self, locator_string):
        return self.is_displayed(locator_string) is False

    @avoid_exceptions(exceptions=NoSuchElementException, replacement=False)
    def is_present(self, locator_string):
        if self.locate.get_element(locator_string):
            return True
        return False

    @avoid_exceptions(exceptions=NoSuchElementException, replacement=True)
    def is_not_present(self, locator_string):
        return self.is_present(locator_string) is False

    @avoid_exceptions(exceptions=NoSuchElementException, replacement=True)
    def is_disappeared(self, locator_string):
        self.wait.wait_for_element_until_not_visible(locator_string)

    def is_enabled(self, locator_string):
        return self.locate.get_element(locator_string).is_enabled()

    def is_not_enabled(self, locator_string):
        return self.is_enabled(locator_string) is False

    def are_dropdown_values(self, locator_string, drop_down_values):
        actual_values = [x.get_attribute("value") for x in
                         Select(self.locate.get_element(locator_string)).all_selected_options]
        for item in drop_down_values:
            if item not in actual_values:
                return False
        return True

    def are_dropdown_texts(self, locator_string, drop_down_texts):
        actual_texts = [x.text for x in
                        Select(self.locate.get_element(locator_string)).all_selected_options]
        for item in drop_down_texts:
            if item not in actual_texts:
                return False
        return True

    def is_dropdown_contains_value(self, locator_string, expected_value):
        actual_values = [x.get_attribute("value") for x in
                         Select(self.locate.get_element(locator_string)).all_selected_options]
        if expected_value in actual_values:
            return True
        return False

    def is_dropdown_contains_text(self, locator_string, expected_text):
        actual_texts = [x.text for x in
                        Select(self.locate.get_element(locator_string)).all_selected_options]
        if expected_text in actual_texts:
            return True
        return False
