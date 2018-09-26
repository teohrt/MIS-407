""" Test the logging functionality. """
from ia02 import logging
import csv
import sys


def read_csv(filename):
    with open(filename, 'r', newline='') as reader:
        csvReader = csv.reader(reader)
        headers = next(csvReader)
        rows = list(csvReader)
        return headers, rows


for fn in sys.argv[1:]:
    logging.log_function(read_csv, "Reading {}".format(fn))
    headings, rows = read_csv(fn)
    logging.log_function(read_csv, "Read {} rows from {}".format(len(rows), fn))

print("Help on using ia02.logging:\n{}".format(logging.__doc__))
print("Help on using ia02.logging log_function:\n{}".
      format(logging.log_function.__doc__))
