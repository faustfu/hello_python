import logging
from sub_log import hello

logger = logging.getLogger(__name__)

logger.error('2010')

hello.world()

logger.error('2020')