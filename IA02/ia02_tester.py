from ia02 import logging

def hello():
    print("Hello, world!")


logging.log_function(hello, "Calling hello")
hello()
logging.log_function(hello, "Finished hello")
