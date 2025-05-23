import logging

logging.basicConfig(level=logging.NOTSET)
logger = logging.getLogger(__name__)
logger.debug('debug message')
logger.info("info message")
logger.warning("warning message")
logger.error("error message")
logger.critical("critical message")
