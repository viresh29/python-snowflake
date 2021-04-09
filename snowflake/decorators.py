import logging
import time
from functools import wraps
from execptions import snowflakeException


def snowflake_decorator(func):
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        for _ in range(self.timeout_counter):
            try:
                return func(self, *args, **kwargs)
            except Exception as e:
                logging.error("Exception during {}".format(func.__name__))
                logging.error(e)
            time.sleep(self.timeout_sleep)
        logging.error("{} failed {} times".format(func.__name__, self.timeout_counter))
        raise snowflakeException("{} failed {} times".format(func.__name__, self.timeout_counter))

    return wrapper
