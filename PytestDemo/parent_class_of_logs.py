import inspect
import logging


class Base_class:
     def log_demo(self):

        loggername= inspect.stack()[1][3]

        # make object of logging
        logger = logging.getLogger(loggername)

        # make file handler, where the logs will be stored
        file_handler = logging.FileHandler('logs.log')

        # set format to print
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")

        # add format to file handler
        file_handler.setFormatter(formatter)

        # pass the file handler to logger now, so logger will now know
        # the file to store logs and the format

        logger.addHandler(file_handler)

        # now set the level hierarchy debug - info - warning - error - critical
        logger.setLevel(logging.DEBUG)

        return logger
