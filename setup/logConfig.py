import logging

"""
Log configuration
"""

logformat = '%(asctime)s %(message)s'
timeformat = '%d/%m/%Y %H:%M:%S'
log = logging


# script logs will go to a file name parse_log.log
log.basicConfig(format=logformat, datefmt=timeformat,
                    filename="parse_log.log", level=log.INFO)