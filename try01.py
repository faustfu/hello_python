# 1. Exceptions are objects. Base exception is "Exception".
# 2. Use "raise" statement to throw an exception.
short_list = [1, 2, 3]
try:
    print(short_list[4])
except:
    print('got error')

try:
    print(short_list[4])
except IndexError as err:
    print('got index error')
except Exception as other:
    print('got unknown error', other)

try:
  raise Exception('huh?')
except Exception as err:
  print(err)
