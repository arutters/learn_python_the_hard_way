people = 40
cars = 30
trucks = 15


if cars > people:
    print("We should take the cars.")
elif cars < people:
    print("We should not take the cars.") #This or the statement before this in the same block will print if true.
else:
    print("We can't decide.") #This is to print when the rest of the if statement block is false.

if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe we could take the trucks.")
else:
    print("We still can't decide.")

if people > trucks:
    print("Alright, let's just take the trucks.")
else: 
    print("Fine, let's stay home then.")

# What do you think the if does to the code under it?
# If this boolean expression is true, run it; otherwise skip it

# Why does the code under if need to be indented four spaces?
# indenting tells python how many lines of code are going to be in the block after the previously line ended on a :

# What happens if it isnt indented? 
# it will most likely create a python error

# What happens if multiple elif blocks are true? 
# Python starts at the top and runs the first block that is True, so it will only run the first one.  

