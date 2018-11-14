import logging
import inspect


def customlogfile(loglevel):

    # Get logger name from method/class
    log_name = inspect.stack()[1][3]
    logger = logging.getLogger(log_name)
    logger.setLevel(logging.DEBUG)

    # Handler
    handler_set = logging.FileHandler("{0}.log".format(log_name), mode='w')
    handler_set.setLevel(loglevel)

    # Formatter
    formatter_set = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')
    handler_set.setFormatter(formatter_set)

    # Add Handler to logger
    logger.addHandler(handler_set)
    return logger
