"""
Module to contain all constants of framework
"""
import os
import pdb


class ConfConst:
    CONFIG_PROP_PATH = os.getcwd() + "\\properties\\common\\config.properties"
    ENVIRONMENT_PROP_PATH = os.getcwd() + "\\properties\\environments\\" + os.getenv("ENV", "qa") + ".properties"


class LogConst:
    DEFAULT_LOGGER_NAME = "COLLAB"
    CONFIG_FILE_PATH = os.getcwd() + '\\properties\\common\\logger.ini'
