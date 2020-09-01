import logging

fmt = '%(asctime)s %(levelname)s %(lineno)s %(message)s'

logging.basicConfig(level=logging.DEBUG, format=fmt)

a = 1
b = 2

logging.error(f'{a} != {b}')
