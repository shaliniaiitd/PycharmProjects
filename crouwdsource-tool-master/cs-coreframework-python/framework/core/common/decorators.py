"""
Module to contain all the decorators to be used across the framework
"""
import math
import time
from functools import wraps

from framework.core.utils.logger_factory import LoggerFactory

logger = LoggerFactory.get_logger()

#  Register any function to PLUGINS dict using register decorator
#  then use that function anywhere using PLUGINS
PLUGINS = dict()


def register(func):
    """Register a function as a plug-in"""
    PLUGINS[func.__name__] = func
    return func


def slow_down(func):
    """Sleep 1 second before calling the function"""

    @wraps(func)
    def wrapper_slow_down(*args, **kwargs):
        time.sleep(1)
        return func(*args, **kwargs)

    return wrapper_slow_down


def debug(func):
    """Print the function signature and return value"""

    @wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]  # 1
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]  # 2
        signature = ", ".join(args_repr + kwargs_repr)  # 3
        logger.info(f"Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        logger.info(f"{func.__name__!r} returned {value!r}")  # 4
        return value

    return wrapper_debug


def timer(func):
    """Print the runtime of the decorated function"""

    @wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()  # 1
        value = func(*args, **kwargs)
        end_time = time.perf_counter()  # 2
        run_time = end_time - start_time  # 3
        logger.info(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value

    return wrapper_timer


def handle_on_exceptions(exceptions=(), msg_on_exception="", replacement=None):
    def decorated_exceptions(func):
        """
        A decorator that wraps the passed in function   and logs
        exceptions should one occur
        """

        @wraps(func)
        def handling_exceptions(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exceptions as e:
                # log the exception
                err = "There was an exception in "
                err += func.__name__ + ". "
                err = msg_on_exception
                logger.error(err, exc_info=True)
                return replacement

        return handling_exceptions

    return decorated_exceptions


def avoid_exceptions(exceptions=(), replacement=None, msg_on_exception=None):
    def decorated_exceptions(func):
        """
        A decorator that wraps the passed in function and logs
        exceptions should one occur
        """

        @wraps(func)
        def bypassing_exceptions(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exceptions as e:
                if msg_on_exception:
                    logger.info(msg_on_exception)
                return replacement

        return bypassing_exceptions

    return decorated_exceptions


def retry_on_exception(tries=3, delay=3, backoff=2, max_delay=15):
    '''
    Decorator for implementing exponential backoff for retrying on failures.
    tries: Max number of tries to execute the wrapped function before failing.
    delay: Delay time in seconds before the FIRST retry.
    backoff: Multiplier to extend the initial delay by for each retry.
    max_delay: Max time in seconds to wait between retries.
    '''
    tries = math.floor(tries)
    if tries < 1:
        raise ValueError('"tries" must be greater than or equal to 1.')
    if delay < 0:
        raise ValueError('"delay" must be greater than or equal to 0.')
    if backoff < 1:
        raise ValueError('"backoff" must be greater than or equal to 1.')
    if max_delay < delay:
        raise ValueError('"max_delay" must be greater than or equal to delay.')

    def decorated_function_with_retry(func):
        @wraps(func)
        def function_to_retry(*args, **kwargs):
            local_tries, local_delay = tries, delay
            while local_tries > 1:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if local_delay > max_delay:
                        local_delay = max_delay
                    logger.error('%s: Retrying in %d seconds...'
                                 % (str(e), local_delay), exc_info=True)
                    time.sleep(local_delay)
                    local_tries -= 1
                    local_delay *= backoff
            return func(*args, **kwargs)

        return function_to_retry

    return decorated_function_with_retry
