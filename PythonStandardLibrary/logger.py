import logging
# import logging.config

def main():
    logger_name = 'example'
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)

    log_path = './log.log'
    fh = logging.FileHandler(log_path)
    fh.setLevel(logging.WARN)

    fmt = "%(asctime)-15s %(levelname)s %(filename)s %(lineno)d %(process)d %(message)s"
    datefmt = "%a %d %b %Y %H:%M:%S"
    formatter = logging.Formatter(fmt, datefmt)

    fh.setFormatter(formatter)
    logger.addHandler(fh)

    logger.debug('debug message')
    logger.info('info message')
    logger.warn('warn message')
    logger.error('error message')
    logger.critical('critical message')

if __name__ == '__main__':
    main()