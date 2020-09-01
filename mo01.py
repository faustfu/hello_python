# 1. Use "import" statement to include packages, modules or functions.
# 2. A python script is a module.
# 3. Module search paths keep in sys.path
# 4. Use a folder with __init__.py to declare a package.
# 5. A module is a singleton, it will be loaded once at runtime.
# 6. Auto-loaded module: __builtins__, includes common functions likes print(), input(), dir(), ...

import sys
from sys import argv
from sys import argv as aa
import scope01
from sources import daily, weekly

print('arguments:', sys.argv) # Show command arguments.
print('arguments:', argv)
print('arguments:', aa)

scope01.change1()

for place in sys.path:
    print(place)

daily.forecast()
weekly.forecast()

print('module path:', sys.path) # Show module including paths.