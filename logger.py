import logging, sys
import datetime as dt
from logging.config import fileConfig

def logSetup(filename:str, echo:bool):
    today = dt.datetime.today()
    logfile = f'{today.year}-{today.month:02d}-{today.day:02d}.log'

    try:
        fileConfig(filename, defaults={'logfilename':logfile})
    except Exception as e:
        print(f'Could not find logger.ini file')
        sys.exit()
    
    logger = logging.getLogger('MONTY')
    logger.propagate=echo

    return logger

if __name__ == '__main__':
    logger = logSetup('logger.ini', False)
    
    logger.critical("Your message goes here")
    logger.error("Your message goes here")
    logger.warning("Your message goes here")
    logger.info("Your message goes here")
    logger.debug("Your message goes here")