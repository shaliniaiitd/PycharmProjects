"""
This module contains base page class to provide of the base features to each sub page class.
"""
from framework.core.utils.logger_factory import LoggerFactory
from framework.ui.base.base_actions import BaseActions
from framework.ui.base.base_verifications import BaseVerifications
from framework.ui.base.base_locator import Locator
from framework.ui.base.base_wait import Wait

logger = LoggerFactory.get_logger()


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = Wait(driver)
        self.locate = Locator(driver)
        self.do = BaseActions(driver)
        self.verify = BaseVerifications(driver)

    def open_url(self, url):
        logger.info("Launching url {}".format(url))
        self.driver.get(url)
        self.wait.wait_until_page_fully_loaded()

    def get_title(self):
        logger.info("Getting page title")
        return self.driver.title

    def switch_to_nth_window(self, nth):
        number_of_windows = len(self.driver.window_handles)
        if nth > number_of_windows or nth < 0:
            logger.error("Incorrect window number({}) passed, actual number of windows: {}"
                         .format(nth, number_of_windows))
            return self
        else:
            logger.info("Switching to {} window".format(nth))
            self.driver.switch_to.window(self.driver.window_handles[nth - 1])
