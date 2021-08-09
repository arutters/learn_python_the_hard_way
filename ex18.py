# this one is like scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

# so *args is actually pointless, and you can do this instead:
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# this takes just one argument
def print_one(arg1):
    print(f"arg1: {arg1}")

# this takes no argument:
def print_none():
    print("I got nothin'.")

print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()

# to run/call/use a function all mean the same thing
