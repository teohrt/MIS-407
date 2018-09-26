"""
Trace Ohrt
9/26/2018
MIS407
"""
import os
import sys
from datetime import datetime

if (__name__ == '__main__'):
    print("Sorry, not for human consumption.")
    quit()

def log_function(f,  message):
    print('{} {} {}: {}'.format(datetime.now().isoformat(sep=' '), dir(f), f.__name__, message))
