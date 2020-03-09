import logging

logging.basicConfig(filename='error.log', level=logging.ERROR)
fileLogger = logging.getLogger('XXX')  # create a group.
fileLogger.error('Oh no!!')
