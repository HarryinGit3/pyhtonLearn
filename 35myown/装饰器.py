import logging
def foo():
    print("foo")

def use_logging(func):
    logging.warning('%s is running'%func.__name__)
    func() 


use_logging(foo)