"""
Trace Ohrt
9/26/2018
MIS407
"""
import os
import sys
from datetime import datetime

"""
Only allows the module to be used when it's imported
"""
if (__name__ == '__main__'):
    print("Sorry, not for human consumption.")
    quit()

"""
Logs datetime, function's module, name and message
"""
def log_function(f,  message):
    print('{} {} {}: {}'.format(datetime.now().isoformat(sep=' '), f.__module__, f.__name__, message))
