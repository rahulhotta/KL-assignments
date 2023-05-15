import logging

def getLogger():
    __logger__ = logging.basicConfig(filename='logs/app.log',format=f"%(levelname)-8s: \t %(filename)s %(funcName)s %(lineno)s - %(message)s")
    return __logger__