import inspect
import logging


def customLogger(logLevel=logging.DEBUG):
    loggerName = inspect.stack()[1][3]
    logger = logging.getLogger(loggerName)
    logger.setLevel(logging.DEBUG)

    fileHandler = logging.FileHandler("dailylog.log", mode='a')
    fileHandler.setLevel(logLevel)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                                  datefmt='%d/%m/%Y %I:%M:%S %p')
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)

    return logger
