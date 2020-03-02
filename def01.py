# 1. Use "def" statement with function name, parameters and indented statements to declare a function.
# 2. Use "return" statement with data to return something from the function.
# 3. If there is no "return" statement, the function will return "None".
# 4. All parameters are references.
# 5. Parameters could be assigned by locations or by names.
# 6. Papameters could have defaults.
# 7. Default values of parameters are calculated when declaration.
# 8. Use "*<name>" to collect dynamic parameters as a tuple.
# 9. Use "**<name>" to collect dynamic naming parameters as a dictionary.
# 10. First string statement of a function is its description(docstring).
# 11. Docstring could be accessed by help() or <function name>.__doc__
def do_nothing():
    pass

def agree():
    return True

def echo(anything):
    anything.append("go")
    return ",".join(anything)

def attack(a, b = "me"):
    return a + ' attacked ' + b

def print_more(req, *args):
    'First parameter is required!'
    print("required parameter", req)
    print("rest parameters", args)

do_nothing()

yes = ["ok"]
if agree():
    print(echo(yes))
else :
    print("not ok")

print(yes)

print(attack("Bob", "Ada"))
print(attack(b = "Bob", a = "Ada"))
print(attack("Bob"))
print_more(1,2,3)
help(print_more)