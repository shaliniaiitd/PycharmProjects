"""
Shared Fixtures
"""
import os
import sys
import time
import pytest
import logging
from pytest_reportportal import RPLogger, RPLogHandler

from framework.core.utils.prop_file_reader import PropFileReader
from framework.core.utils.logger_factory import LoggerFactory
from framework.ui.utils.browser import Browser

logger = LoggerFactory.get_logger("TEST")


# --------------------------------
# Fixture - driver  - it will provide the driver object
# --------------------------------
@pytest.fixture()
def driver(prop):
    # get WebDrivers
    logger.info('Initializing browser.')
    driver = Browser.get_driver(
        {"browser": prop.configs_prop['test.browser'].data,
         "environment": prop.configs_prop['test.environment'].data,
         "headless": prop.configs_prop["test.browser.headless"].data})

    driver.implicitly_wait(prop.configs_prop['test.wait.default'].data)

    logger.info("Initializing application")

    # #load base url
    # driver.get(prop.environment_prop["test.baseURI1.homepage"].data)
    yield driver

    logger.info('Quiting browser.')
    driver.quit()
    logger.info("Ending application.")
    del driver


# --------------------------------
# Fixture - prop - Properties file fixture to get details from properties files.
# --------------------------------
@pytest.fixture(scope='session')
def prop():
    logger.info("Loading properties")
    # Read the properties files
    PropFileReader.load_all_props()
    # Return properties so it can be used
    return PropFileReader


# --------------------------------
# Hook Implementation for reporting and screenshots
# --------------------------------
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    # set a report attribute for each phase of a call, which can
    # be "setup", "call", "teardown"
    setattr(item, "test_status_" + rep.when, rep)


# --------------------------------
# Fixture - Screen shot Taking.
# --------------------------------
@pytest.fixture(scope="function", autouse=True)
def take_screenshot_as_per_status(request, prop, driver):
    yield
    # things can be used
    # logger.info(request.node.rep_call.failed)
    # logger.info(request.node.rep_call.passed)
    # logger.info(request.node.rep_call.duration)
    # logger.info(request.node.rep_call.outcome)

    # checking if setup was passed
    if request.node.test_status_setup.passed:
        # getting screen shot flag
        screenshot_config = prop.configs_prop["test.screenshot.capture"].data
        time_string = ""
        # preparing time string to use in screen shot name.
        if prop.configs_prop["test.screenshot.appendtimestring"].data == "true":
            time_string = time.strftime("%Y%m%d-%H%M%S")

        # Screen shot saving for failed case.
        if request.node.test_status_call.failed and (screenshot_config == "failed" or screenshot_config == "all"):
            logger.info("taking failed screen shot")
            # save_screenshot(request, "failed", prop, driver)
            status = "failed"
            directory = prop.configs_prop["test.screenshot.directory"].data + status + "/"
            screenshot_name = "screenshot_" + request.node.name + "_" + status + "_" + time_string + ".png"
            if not os.path.exists(directory):
                os.makedirs(directory)
            driver.save_screenshot(directory + screenshot_name)

            # uncomment below line for Allure report
            # allure.attach.file(directory + screenshot_name, attachment_type=allure.attachment_type.PNG)

        # Screen shot saving for Passed case.
        elif request.node.test_status_call.passed and (screenshot_config == "passed" or screenshot_config == "all"):
            logger.info("taking passed screen shot")
            # save_screenshot(request, "passed", prop, driver)
            status = "passed"
            directory = prop.configs_prop["test.screenshot.directory"].data + status + "/"
            screenshot_name = "screenshot_" + request.node.name + "_" + status + "_" + time_string + ".png"
            if not os.path.exists(directory):
                os.makedirs(directory)
            driver.save_screenshot(directory + screenshot_name)

            # uncomment below line for Allure report
            # allure.attach.file(directory + screenshot_name, attachment_type=allure.attachment_type.PNG)


# -------------------------------- # -------------------------------- # -------------------------------- # --------------------------------
# Reporting Portal Fixtures  - Please uncomment below two fixtures while using Reporting portal.
# -------------------------------- # -------------------------------- # -------------------------------- # --------------------------------

# ------------------------------------------------
# Reporting Portal Fixtures - Python logging handler to log into report portal
# ------------------------------------------------
@pytest.fixture(scope="session")
def rp_logger(request):
    logger_rp = logging.getLogger(__name__)
    logger_rp.setLevel(logging.DEBUG)
    if hasattr(request.node.config, 'py_test_service'):
        logging.setLoggerClass(RPLogger)
        rp_handler = RPLogHandler(request.node.config.py_test_service)
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.INFO)
        logger_rp.addHandler(console_handler)
    else:
        rp_handler = logging.StreamHandler(sys.stdout)
    rp_handler.setLevel(logging.INFO)
    return logger_rp


# --------------------------------
# Reporting Portal Fixtures - saving screen shot
# --------------------------------
@pytest.fixture(scope="function", autouse=True)
def take_screenshot_reporting_portal(driver, request, rp_logger, prop):
    yield
    # Make sure to run the test in following way -  pytest --reportportal
    # To attach screenshot in the report portal
    screenshot_config = prop.configs_prop["test.screenshot.capture"].data
    if request.node.test_status_setup.passed:
        if request.node.test_status_call.passed and (screenshot_config == "passed" or screenshot_config == "all"):
            rp_logger.info("Test passed",
                           attachment={"name": request.node.name + ".png",
                                       "data": driver.get_screenshot_as_png(),
                                       "mime": "image/png"})
        elif request.node.test_status_call.failed and (screenshot_config == "failed" or screenshot_config == "all"):
            rp_logger.info("Test failed",
                           attachment={"name": request.node.name + ".png",
                                       "data": driver.get_screenshot_as_png(),
                                       "mime": "image/png"})

# --------------------------------# --------------------------------# --------------------------------# --------------------------------