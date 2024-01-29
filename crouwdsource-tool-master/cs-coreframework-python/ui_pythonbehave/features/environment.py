"""
Shared Fixtures
"""
import os
import sys
import time

import allure
import behave
import logging

from reportportal_behave.behave_integration_service import BehaveIntegrationService

from framework import *
from framework.core.utils.prop_file_reader import PropFileReader
from framework.core.utils.logger_factory import LoggerFactory
from framework.ui.utils.browser import Browser
from behave import fixture
from behave import use_fixture
from ui_pythonbehave.pageobjects.actions.HomePage import HomePage
from ui_pythonbehave.pageobjects.actions.LoginPage import LoginPage
from ui_pythonbehave.pageobjects.verifications.HomePageVerification import HomePageVerification
from ui_pythonbehave.pageobjects.verifications.LoginPageVerification import LoginPageVerification

logger = LoggerFactory.get_logger("TEST")


# --------------------------------
# Fixture - driver  - it will provide the driver object
# --------------------------------


class PageObjects:
    """
    Class to create single object of application to access all the pages and supported functions
    """

    def __init__(self, driver, prop):
        self.properties = prop
        self.driver = driver
        self.login = LoginPage(driver)
        self.home = HomePage(driver)
        self.login_verify = LoginPageVerification(driver)
        self.home_verify = HomePageVerification(driver)
        self.base_url = self.properties.environment_prop["test.baseURI1.timesheet.home"].data
        print(self.base_url)

# Fixtures


@fixture
def driver(context, *args, **kwargs):
    # get WebDrivers
    logger.info('Initializing browser.')
    context.driver = Browser.get_driver(
        {"browser": context.prop.configs_prop['test.browser'].data,
         "environment": context.prop.configs_prop['test.environment'].data,
         "headless": context.prop.configs_prop["test.browser.headless"].data})
    context.driver.implicitly_wait(context.prop.configs_prop['test.wait.default'].data)
    logger.info("Initializing application")
    yield context.driver
    context.driver.quit()
    logger.info("Ending application.")


# --------------------------------
# Fixture - prop - Properties file fixture to get details from properties files.
# --------------------------------
@fixture
def prop(context,*args,**kwargs):
    logger.info("Loading properties")
    # Read the properties files
    PropFileReader.load_all_props()
    context.prop = PropFileReader
    # Return properties so it can be used
    return context.prop


def before_tag(context,tag):
    if tag == "web":
        use_fixture(prop, context)
        use_fixture(driver, context)
        # use_fixture(take_screenshot_as_per_status,context)
        context.pages = PageObjects(context.driver, context.prop)

# --------------------------------
# Hook Implementation for reporting and screenshots
# --------------------------------
@fixture
def pytest_runtest_makereport(context,item, call):
    outcome = yield
    rep = outcome.get_result()

    # set a report attribute for each phase of a call, which can
    # be "setup", "call", "teardown"
    setattr(item, "test_status_" + rep.when, rep)


# --------------------------------
# Fixture - Screen shot Taking.
# --------------------------------
@fixture
def take_screenshot_as_per_status(context,scenario):
    yield
    # checking if setup was passed
    # if scenario.status.passed:
        # getting screen shot flag
    screenshot_config = context.prop.configs_prop["test.screenshot.capture"].data
    time_string = ""
    # preparing time string to use in screen shot name.
    if context.prop.configs_prop["test.screenshot.appendtimestring"].data == "true":
        time_string = time.strftime("%Y%m%d-%H%M%S")

    # Screen shot saving for failed case.
    if scenario.status.failed and (screenshot_config == "failed" or screenshot_config == "all"):
        logger.info("taking failed screen shot")
        # save_screenshot(request, "failed", prop, driver)
        status = "failed"
        directory = context.prop.configs_prop["test.screenshot.directory"].data + status + "/"
        screenshot_name = "screenshot_" + scenario.name + "_" + status + "_" + time_string + ".png"
        if not os.path.exists(directory):
            os.makedirs(directory)
        context.driver.save_screenshot(directory + screenshot_name)

        # uncomment below line for Allure report
        allure.attach.file(directory + screenshot_name, attachment_type=allure.attachment_type.PNG)

    # Screen shot saving for Passed case.
    elif scenario.status.passed and (screenshot_config == "passed" or screenshot_config == "all"):
        logger.info("taking passed screen shot")
        # save_screenshot(request, "passed", prop, driver)
        status = "passed"
        directory = context.prop.configs_prop["test.screenshot.directory"].data + status + "/"
        screenshot_name = "screenshot_" + scenario.name + "_" + status + "_" + time_string + ".png"
        if not os.path.exists(directory):
            os.makedirs(directory)
        context.driver.save_screenshot(directory + screenshot_name)

        # uncomment below line for Allure report
        allure.attach.file(directory + screenshot_name, attachment_type=allure.attachment_type.PNG)


# -------------------------------- # -------------------------------- # -------------------------------- # --------------------------------
# Reporting Portal Fixtures  - Please uncomment below two fixtures while using Reporting portal.
# -------------------------------- # -------------------------------- # -------------------------------- # --------------------------------

def before_all(context):
    tags = ', '.join([tag for tags in context.config.tags.ands for tag in tags])
    rp_enable = context.config.userdata.getbool('rp_enable', False)
    step_based = context.config.userdata.getbool('step_based', True)
    context.requested_browser = context.config.userdata.get('browser', "chrome")
    add_screenshot = context.config.userdata.getbool('add_screenshot', True)
    context.behave_integration_service = BehaveIntegrationService(context.config.userdata['rp_endpoint'],
                                                                  context.config.userdata['rp_project'],
                                                                  context.config.userdata['rp_token'],
                                                                  context.config.userdata['rp_launch_name'],
                                                                  context.config.userdata['rp_launch_description'],
                                                                  rp_enable,
                                                                  step_based,
                                                                  add_screenshot)
    context.launch_id = context.behave_integration_service.launch_service(tags=tags)


def before_feature(context, feature):
    context.feature_id = context.behave_integration_service.before_feature(feature)


def before_scenario(context, scenario):
    context.scenario_id = context.behave_integration_service.before_scenario(scenario,
                                                                             feature_id=context.feature_id)


def before_step(context, step):
    context.step_id = context.behave_integration_service.before_step(step, scenario_id=context.scenario_id)


def after_step(context, step):
    context.behave_integration_service.after_step(step, context.step_id)


def after_scenario(context, scenario):
    use_fixture(take_screenshot_as_per_status, context,scenario)
    context.behave_integration_service.after_scenario(scenario, context.scenario_id)


def after_feature(context, feature):
    context.behave_integration_service.after_feature(feature, context.feature_id)


def after_all(context):
    context.behave_integration_service.after_all(context.launch_id)

# --------------------------------# --------------------------------# --------------------------------# --------------------------------