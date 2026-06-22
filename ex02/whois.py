import sys

if len(sys.argv) == 1:
    sys.exit()

if len(sys.argv) > 2:
    raise AssertionError("more than one argument is provided")

arg = sys.argv[1]

if not arg.lstrip("-").isdigit():
    raise AssertionError("argument is not an integer")

num = int(arg)

if num == 0:
    print("I'm Zero.")
elif num % 2 == 0:
    print("I'm Even.")
else:
    print("I'm Odd.")
