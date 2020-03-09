import logging

fmt = '%(asctime)s %(levelname)s %(lineno)s %(message)s'

logging.basicConfig(level=logging.DEBUG, format=fmt)

logging.error('1 != 1')
