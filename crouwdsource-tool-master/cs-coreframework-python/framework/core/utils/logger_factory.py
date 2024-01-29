"""
This module logger Factory class to configure and get logger as per ini file.
"""
import logging
import logging.config

from framework.core.constants.core_constants import LogConst

DEFAULT_LOGGER_NAME = LogConst.DEFAULT_LOGGER_NAME


class LoggerFactory:

    @classmethod
    def get_conf_file_path(cls):
        return LogConst.CONFIG_FILE_PATH

    @classmethod
    def get_logger(cls, logger_name=DEFAULT_LOGGER_NAME):
        logging.config.fileConfig(fname=cls.get_conf_file_path())
        return logging.getLogger(logger_name)
