import logging


def test_log_demo():

    # make object of logging
    logger = logging.getLogger(__name__)

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
    logger.setLevel(logging.INFO)

    logger.debug("debug statement")
    logger.info("information")
    logger.warning("warning")
    logger.error("error message")
    logger.critical("critical message")

