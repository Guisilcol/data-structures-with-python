import logging
import time

logging.basicConfig(
    level=logging.INFO,  # Set the log level to INFO
    format='%(asctime)s.%(msecs)03d %(levelname)s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)


def info(data: any):
    logging.info(data)
    
def debug(data: any):
    logging.debug(data)
    
def error(data: any):
    logging.error(data)
    
def warning(data: any):
    logging.warning(data)
    
def critical(data: any):
    logging.critical(data)
    
