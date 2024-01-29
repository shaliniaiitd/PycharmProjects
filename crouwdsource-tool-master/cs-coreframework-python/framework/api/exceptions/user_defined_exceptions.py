"""
Module to contain all the user defined exception classes.
"""


class ParamsMissing(Exception):
    """
    Custom Exception class for paramaters missing

    Attributes:
        message -- explanation of the error
    """
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class InvalidURLException(Exception):
    """
    Custom Exception class for missing or invalid URL (starts with http or https)

    Attributes:
        message -- explanation of the error
    """
    def __init__(self, message="Invalid URL"):
        self.message = message
        super().__init__(self.message)


class InValidParam(Exception):
    """
    Custom Exception class for Invalid paramaters

    Attributes:
        message -- explanation of the error
    """
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
