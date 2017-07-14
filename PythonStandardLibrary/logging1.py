import logging

#logging.basicConfig(filename='logger.log',level=logging.INFO)

# logger=logging.getLogger(logger_name)
# sh=logging.StreamHandler(stream=None)
# fh=logging.FileHandler(filename,mode='a',encoding=None,delay=False)
# formatter=logging.Formatter(fmt=None,datefmt=None)
# filter=logging.Filter(name='')

logging.debug('debug message')
logging.info('info message')
logging.warn('warn message')
logging.error('error message')
logging.critical('critical message')