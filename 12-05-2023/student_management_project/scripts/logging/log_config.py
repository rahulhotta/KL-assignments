import logging
from logging import StreamHandler
from logging.handlers import RotatingFileHandler, SocketHandler
def getLogger():
    __logger__ = logging.getLogger("")
    log_formatter = "%(asctime)s - %(levelname)-6s - [%(threadName)5s: %(filename)s  :%(funcName)5s():" "" "%(lineno)s] - %(message)s"
    time_format = "%Y-%m-%d %H:%M:%S"
    formatter = logging.Formatter(log_formatter, time_format)
    log_file = "logs/app.log"
    temp_handler = RotatingFileHandler(
        log_file, maxBytes=1000000
    )
    temp_handler.setFormatter(formatter)
    __logger__.addHandler(temp_handler)
    __logger__.addHandler(StreamHandler().setFormatter(formatter))

    return __logger__

logger = getLogger()