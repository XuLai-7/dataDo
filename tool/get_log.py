import logging


# logging 是一个包名
def get_logging():
    fm = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s (%(funcName)s:%(funcName)s:%(lineno)d)]-%(message)s"
    logging.basicConfig(level=logging.INFO, filename="../log/log01.log", format=fm)
    return logging
