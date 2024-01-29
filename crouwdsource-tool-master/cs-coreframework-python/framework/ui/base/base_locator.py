"""
This is module to contain commonly used functionality like find elements
"""
from framework.core.utils.logger_factory import LoggerFactory
from framework.ui.common.helper import *

logger = LoggerFactory.get_logger()


class Locator:

    def __init__(self, driver):
        self.driver = driver

    def get_element(self, locator, driver=None):
        """
        custom wrapper to find element using initiated driver or passed driver/element object

        locator param should be of "css|string" style
        """
        if driver:
            return driver.find_element(*get_locator_by(locator))
        else:
            return self.driver.find_element(*get_locator_by(locator))

    def get_elements(self, locator, driver=None):
        """
        custom wrapper to find elements using initiated driver or passed driver/element

        locator param should be of "css|string" style
        """
        if driver:
            return driver.find_elements(*get_locator_by(locator))
        else:
            return self.driver.find_elements(*get_locator_by(locator))
