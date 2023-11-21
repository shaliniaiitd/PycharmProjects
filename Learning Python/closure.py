#Use case for closure


import logging

def logger(func):
    def log_func(*args):
        logging.info("Running function {} with arguments {}".format(func.__name__,args))
        print(func(*args))
        return (log_func)

def add(x,y):
    return x+y

def sub(x,y):
    return x-y

add_logger = logger(add)
sub_logger = logger(sub)

add_logger(2,3)  # prints 5 on console and "INFO:Running function add with arguments 2,3 in log file".
sub_logger(9,5)  # prints 4 on console and "INFO:Running function add with arguments 9,5 in log file".





