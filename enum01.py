# 1. Use module:enum and class to declare an enum class.
# 2. A enum class cannot be initialized and its properties are immutable.

from enum import IntEnum, unique

# case 1: Inherite IntEnum or Enum to be an enum.
class Action(IntEnum):
  stop = 1
  right = 2
  left = 3
  up = 4
  down = 5
print('Action is ', Action, dir(Action))

# case 2: Get a member of the enum by enum value.
print('Action(3) =', Action(3), ', Action(3).name =', Action(3).name, ', Action(3).value =', Action(3).value)

# case 3: Loop by enum members.
for m in Action:
  print(m.name,'\t:', m.value)

# case 4: Duplicated enum value.
class Role(IntEnum):
  admin = 1
  user = 2
  guest = 3
  anonymous = 3 # 'anonymous' is an alias of 'guest'
print('Role(anonymous) is ', Role(3))

# case 5: Use modifier:unique to force members to be unique.
@unique
class Dept(IntEnum):
  sales = 1
  agent = 2