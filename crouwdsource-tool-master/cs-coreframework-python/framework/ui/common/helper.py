"""
This module contains all the helper functions, which can be directly used.
"""
from selenium.webdriver.common.by import By

from framework.ui.constants.ui_constants import Generic


def get_locator_by(locator):
    separator = Generic.LOCATOR_BY_VALUE_SEPARATOR
    if separator in locator:
        locator_by, locator_str = locator.split(separator)

        if locator_by.lower() == "id":
            return By.ID, locator_str
        elif locator_by.lower() == "name":
            return By.NAME, locator_str
        elif locator_by.lower() == "class_name":
            return By.CLASS_NAME, locator_str
        elif locator_by.lower() == "tag_name":
            return By.TAG_NAME, locator_str
        elif locator_by.lower() == "xpath":
            return By.XPATH, locator_str
        elif locator_by.lower() == "css_selector":
            return By.CSS_SELECTOR, locator_str
        elif locator_by.lower() == "link_text":
            return By.LINK_TEXT, locator_str
        elif locator_by.lower() == "partial_link_text":
            return By.PARTIAL_LINK_TEXT, locator_str
        else:
            raise Exception("Invalid locator type : {}".format(locator))
    else:
        raise Exception("Invalid locator string : {}".format(locator))
