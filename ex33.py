i = 0
numbers = []

while i < 6:
# while i in range(0, 6): (This will also work if you want to use a range of numbers)
    print(f"At the top of i is {i}")
    numbers.append(i)

    i = i + 1
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")


print("The numbers: ")

for num in numbers:
    print(num)
# a while-loop will keep executing the code block under it as long as a boolean expression is True, itll keep running till its false
# make sure to use while-loops sparingly
# review your statements and make sure that the boolean test will become false at some point
# whe in doubt print your variable at the top and bottom of the while-loop to see what its doing

