"""
This module contains wait selenium element using WebDriverWait
"""
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from framework.core.utils.logger_factory import LoggerFactory
from framework.ui.common.helper import get_locator_by
from framework.ui.constants.ui_constants import ErrorMessages as EM
from framework.ui.constants.ui_constants import WaitConst

logger = LoggerFactory.get_logger()

GLOBAL_TIMEOUT_DEFAULT = WaitConst.WAIT_TIMEOUT_DEFAULT
GLOBAL_TIMEOUT_SHORT = WaitConst.WAIT_TIMEOUT_SHORT
GLOBAL_TIMEOUT_LONG = WaitConst.WAIT_TIMEOUT_LONG
GLOBAL_POLL_FREQUENCY = WaitConst.POLL_FREQUENCY


class Wait:

    def __init__(self, driver):
        self.driver = driver
        self.EC = EC

    def wait_for_element_until_visible(self, locator_string, timeout=GLOBAL_TIMEOUT_DEFAULT,
                                       poll_frequency=GLOBAL_POLL_FREQUENCY,
                                       ignored_exceptions=None):
        return self.wait_for_element_until_condition(EC.visibility_of_element_located(get_locator_by(locator_string)),
                                                     timeout,
                                                     poll_frequency,
                                                     ignored_exceptions,
                                                     msg=EM.wait_msg_element_is_not_visible.format(timeout,
                                                                                                   poll_frequency))

    def wait_for_element_until_present(self, locator_string, timeout=GLOBAL_TIMEOUT_DEFAULT,
                                       poll_frequency=GLOBAL_POLL_FREQUENCY,
                                       ignored_exceptions=None):
        return self.wait_for_element_until_condition(EC.presence_of_element_located(get_locator_by(locator_string)),
                                                     timeout,
                                                     poll_frequency,
                                                     ignored_exceptions,
                                                     msg=EM.wait_msg_element_is_not_present.format(timeout,
                                                                                                   poll_frequency))

    def wait_for_element_until_clickable(self, locator_string, timeout=GLOBAL_TIMEOUT_DEFAULT,
                                         poll_frequency=GLOBAL_POLL_FREQUENCY,
                                         ignored_exceptions=None):
        return self.wait_for_element_until_condition(EC.element_to_be_clickable(get_locator_by(locator_string)),
                                                     timeout,
                                                     poll_frequency,
                                                     ignored_exceptions,
                                                     msg=EM.wait_msg_element_is_not_clickable.format(timeout,
                                                                                                     poll_frequency))

    def wait_for_element_until_not_visible(self, locator_string, timeout=GLOBAL_TIMEOUT_DEFAULT,
                                           poll_frequency=GLOBAL_POLL_FREQUENCY,
                                           ignored_exceptions=None):
        return self.wait_for_element_until_condition(EC.invisibility_of_element_located(get_locator_by(locator_string)),
                                                     timeout,
                                                     poll_frequency,
                                                     ignored_exceptions,
                                                     msg=EM.wait_msg_element_is_not_visible.format(timeout,
                                                                                                   poll_frequency))

    def wait_for_element_until_condition(self, expected_condition_obj, timeout=GLOBAL_TIMEOUT_DEFAULT,
                                         poll_frequency=GLOBAL_POLL_FREQUENCY, ignored_exceptions=None,
                                         msg="Unable to find element"):
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll_frequency,
                             ignored_exceptions=ignored_exceptions).until(
            expected_condition_obj, msg)

    def wait_until_page_fully_loaded(self, timeout=GLOBAL_TIMEOUT_DEFAULT, poll_frequency=GLOBAL_POLL_FREQUENCY,
                                     ignored_exceptions=None):
        wait = WebDriverWait(self.driver,
                             timeout=timeout,
                             poll_frequency=poll_frequency,
                             ignored_exceptions=ignored_exceptions)
        msg = EM.wait_msg_page_is_not_fully_loaded.format(timeout)
        return wait.until(self.is_document_ready_state_complete, msg)

    def wait_explicitly(self, time_to_wait):
        """
         - time_to_wait: Amount of time to wait (in seconds)
        :Usage:
            driver.implicitly_wait(30)
        """
        if time_to_wait <= WaitConst.MAX_EXPLICIT_WAIT:
            logger.info("Waiting explicity for {} seconds".format(time_to_wait))
            time.sleep(time_to_wait)
        else:
            logger.info("Can't wait beyond max explict allowed wait - {}".format(WaitConst.MAX_EXPLICIT_WAIT))

    @staticmethod
    def wait_explicitly_for_seconds(time_in_seconds):
        time.sleep(time_in_seconds)

    @staticmethod
    def is_document_ready_state_complete(driver):
        return driver.execute_script('return document.readyState;') == 'complete'

    @staticmethod
    def get_document_ready_state(driver):
        return driver.execute_script('return document.readyState;')
