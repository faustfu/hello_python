import logging

# change log level to debug.(default=WARN)
logging.basicConfig(level=logging.DEBUG)

logging.debug('debug')
logging.info('info')
logging.warning('warning')
logging.error('error')
logging.critical('critical')

testLogger = logging.getLogger('test')  # create a group.
testLogger.debug('debug')
