import inspect
import logging


def custom_logger(log_level=logging.DEBUG):
    # Gets the name of the class / method from where this method is called
    logger_name = inspect.stack()[1][3]
    logger = logging.getLogger(logger_name)

    logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler("automation.log", mode='a')
    file_handler.setLevel(log_level)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                    datefmt='%d/%m/%Y %I:%M:%S %p')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.WARNING)
    logger.addHandler(stream_handler)

    return logger
