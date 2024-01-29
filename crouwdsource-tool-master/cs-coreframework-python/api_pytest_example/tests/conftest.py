"""
Shared fixtures for setting up Base URL, Authentication, Headers, ContentType etc.
"""


import pytest
import sys

from framework.api.requests.base_api import APIConfiguration
from framework.core.utils.logger_factory import LoggerFactory
from framework.core.utils.prop_file_reader import PropFileReader
import logging
from pytest_reportportal import RPLogger, RPLogHandler

logger = LoggerFactory.get_logger("TEST")

"""
    This fixture will provide the api_config object with required base_url, content_type and authentication valid
    across the session.
        - Refer to Class APIConfiguration: for setting up required configs for API under test 
"""


@pytest.fixture(scope="session")
def api_config():
    # Read the properties files
    logger.info("Loading properties file..")
    PropFileReader.load_all_props()
    api_config = APIConfiguration()
    logger.info("Setting up base configurations for the API ..")
    api_config.base_url = PropFileReader.environment_prop['api.base.uri'].data
    api_config.content_type = "application/json"
    '''
    Depending on the type of authentication, setup the auth for api configuration
    '''
    # api_config.addBearerTokenAuth()
    logger.info("Base Configurations are set for the API under test ..")
    return api_config


# ------------------------------------------------
# Reporting Portal Fixtures - Python logging handler to log into report portal
# ------------------------------------------------
@pytest.fixture(scope="session")
def rp_logger(request):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    # Create handler for Report Portal if the service has been
    # configured and started.
    if hasattr(request.node.config, 'py_test_service'):
        # Import Report Portal logger and handler to the test module.
        logging.setLoggerClass(RPLogger)
        rp_handler = RPLogHandler(request.node.config.py_test_service)
        # Add additional handlers if it is necessary
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.INFO)
        logger.addHandler(console_handler)
    else:
        rp_handler = logging.StreamHandler(sys.stdout)
    # Set INFO level for Report Portal handler.
    rp_handler.setLevel(logging.INFO)
    return logger