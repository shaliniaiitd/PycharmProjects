import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from framework.core.utils.logger_factory import LoggerFactory
from framework.ui.exceptions.user_defined_exceptions import BrowserException

logger = LoggerFactory.get_logger()
dir_path = os.path.dirname(os.path.realpath(__file__))
remote_grid_url = "http://localhost:4444/wd/hub"


class Browser:
    DRIVER_PATH = "C:\\Users\\Kapil_Kumar\\Downloads"

    @classmethod
    def get_driver(cls, settings={"browser": "chrome", "environment": "local",
                                  "headless": "false"}):
        if settings["environment"] == "local":
            return cls.get_local_driver_instance(settings)
        elif settings["environment"] == "remote":
            return cls.get_remote_driver_instance(settings)

    @classmethod
    def get_local_driver_instance(cls, settings):
        chrome_options = cls.set_chrome_driver_options(settings)
        if settings["browser"] == 'chrome' and "version" not in settings.keys():
            driver = webdriver.Chrome(
                ChromeDriverManager(path=cls.DRIVER_PATH).install(),
                options=chrome_options)
        elif settings["browser"] == 'chrome' and "version" in settings.keys():
            driver = webdriver.Chrome(
                ChromeDriverManager(version=settings["version"]).install(),
                options=chrome_options)
        else:
            logger.error("Invalid Browser passed", exc_info=True)
            raise BrowserException("Invalid Browser passed")
        return driver

    @classmethod
    def get_remote_driver_instance(cls, settings):
        # Make sure to run "docker-compose up -d" before running test
        chrome_options = cls.set_chrome_driver_options(settings)
        capabilities = {'browserName': 'chrome', 'javascriptEnabled': True}
        capabilities.update(chrome_options.to_capabilities())
        return webdriver.Remote(
            command_executor=remote_grid_url,
            desired_capabilities=capabilities)

    @staticmethod
    def set_chrome_driver_options(settings):
        chrome_options = Options()
        if settings["headless"] == "true":
            chrome_options.add_argument("--headless")
        else:
            chrome_options.add_argument("--start-maximized")
        return chrome_options
