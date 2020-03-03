# 1. Use "import" statement to include packages, modules or functions.
# 2. A python script is a module.
# 3. Module search paths keep in sys.path
# 4. Use a folder with __init__.py to declare a package.

import sys
from sys import argv
from sys import argv as aa
import scope01
from sources import daily, weekly

print('arguments:', sys.argv)
print('arguments:', argv)
print('arguments:', aa)

scope01.change1()

for place in sys.path:
    print(place)

daily.forecast()
weekly.forecast()