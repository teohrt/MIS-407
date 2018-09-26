"""
Helper module to log info about function calls
Trace Ohrt 9/26/2018 MIS407
"""
from datetime import datetime

if (__name__ == '__main__'):
    print("Sorry, not for human consumption.")
    quit()

def log_function(f,  message):
    """Logs datetime, function's module and name followed by a message"""
    print('{} {} {}: {}'.format(datetime.now().isoformat(sep=' '), f.__module__, f.__name__, message))
