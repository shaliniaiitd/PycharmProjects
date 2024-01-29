"""
This module to read different (Common and Environment) properties files and to provide in single object.
"""
from jproperties import Properties

from framework.core.constants.core_constants import ConfConst


class PropFileReader:
    configs_prop = Properties()
    environment_prop = Properties()

    CONFIG_PROP_PATH = ConfConst.CONFIG_PROP_PATH
    ENVIRONMENT_PROP_PATH = ConfConst.ENVIRONMENT_PROP_PATH

    @classmethod
    def load_config_prop(cls):
        with open(cls.CONFIG_PROP_PATH, 'rb') as config_file:
            cls.configs_prop.load(config_file)

    @classmethod
    def load_env_prop(cls):
        with open(cls.ENVIRONMENT_PROP_PATH, 'rb') as env_file:
            cls.environment_prop.load(env_file)

    @classmethod
    def load_all_props(cls):
        cls.load_config_prop()
        cls.load_env_prop()
