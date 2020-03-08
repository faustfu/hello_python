# 1. Module:datetime is for normal date processing.
# 2. Module:time is for epoch.
# 3. Module:locale is for localization.

from datetime import date
from datetime import timedelta
from datetime import datetime
import time
import locale

fmt = '%Y-%m-%d %H:%M:%S'

# print(locale.locale_alias.keys())
# locale.setlocale(locale.LC_TIME, 'zh_tw')

print('Today is', date.today())
print('Tomorrow is', date.today()+timedelta(days=1))

print('Current time is', datetime.now())
print('Current epoch is %s(%s)' %
      (time.time(), time.ctime(time.time())))
print('Current UTC timestamp is',
      time.gmtime(time.time()))
print('Current local timestamp is',
      time.localtime(time.time()))

print('Current formatted UTC time is',
      time.strftime(fmt, time.gmtime(time.time())))
print('Current formatted datetime is', datetime.now().strftime(fmt))
print('Current datetime object is', datetime.strptime(
    datetime.now().strftime(fmt), fmt)) # convert string to a datetime object
