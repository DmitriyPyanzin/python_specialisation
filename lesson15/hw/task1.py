import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

debug_handler = logging.FileHandler('task1_debug.log')
debug_handler.setLevel(logging.DEBUG)
debug_handler.setFormatter(formatter)
logger.addHandler(debug_handler)

err_handler = logging.FileHandler('task1_error.log')
err_handler.setLevel(logging.ERROR)
err_handler.setFormatter(formatter)
logger.addHandler(err_handler)

logger.debug('debug message')
logger.info('info message')
logger.warning('warning message')
logger.error('error message')
logger.critical('critical message')
