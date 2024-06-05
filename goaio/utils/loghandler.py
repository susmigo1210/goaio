"""
Log handler
"""
import logging


def get_logger(file_name: str) -> logging.Logger:
    logger = logging.getLogger(file_name)

    # Check if logger already has handlers to avoid adding multiple handlers
    if not logger.hasHandlers():
        logger.setLevel(logging.DEBUG)
        handler = logging.StreamHandler()
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(module)s-%(lineno)d  - %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger


if __name__ == "__main__":
    test_logger = get_logger(__name__)
    test_logger.info('hi there')
    test_logger.debug('testing debug')
    test_logger.warning("testing warning")
    test_logger.fatal('testing fatal')
