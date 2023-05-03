import logging
import datetime as dt

today = dt.datetime.today()
filename = f'{today.year}-{today.month:02d}-{today.day:02d}.log'

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("TEST LOGGER")

file_handler = logging.FileHandler(filename)
file_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s: %(levelname)s: - %(message)s',"%Y-%m-%d %H:%M:%S")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

logger.critical("Your message goes here")
logger.error("Your message goes here")
logger.warning("Your message goes here")
logger.info("Your message goes here")
logger.debug("Your message goes here")

