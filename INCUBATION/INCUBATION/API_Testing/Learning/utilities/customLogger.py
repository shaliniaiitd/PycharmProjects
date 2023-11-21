import logging

class LogGen():
    @staticmethod
    def loggen():
        logging.basicConfig(filename="../logs/api_test.log")
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
import os
import logging
from logging.handlers import RotatingFileHandler

class TestLogger:
    def __init__(self, log_file_path, log_level=logging.INFO):
        # Create a logger
        self.logger = logging.getLogger("test_logger")
        self.logger.setLevel(log_level)

        # Create a log formatter
        log_formatter = logging.Formatter("%(asctime)s [%(levelname)s] - %(message)s")

        # Log to a file
        if log_file_path:
            os.makedirs(os.path.dirname(log_file_path), exist_ok=True)
            log_file_handler = RotatingFileHandler(log_file_path, maxBytes=1024*1024, backupCount=3)
            log_file_handler.setFormatter(log_formatter)
            self.logger.addHandler(log_file_handler)

        # Log to the console
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(log_formatter)
        self.logger.addHandler(console_handler)

    def info(self, message):
        self.logger.info(message)

    def error(self, message):
        self.logger.error(message)

    def warning(self, message):
        self.logger.warning(message)

    def debug(self, message):
        self.logger.debug(message)

# Usage example:
if __name__ == "__main__":
    # Configure the logger
    log_file_path = "test.log"
    logger = TestLogger(log_file_path)

    # Log messages
    logger.info("This is an info message")
    logger.error("This is an error message")
    logger.warning("This is a warning message")
    logger.debug("This is a debug message")
