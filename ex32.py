the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']
# Above here: these are called lists and strings will have singl quotes, numbers have nothing surrounding, all followed by a comma
# this first kind of for-loop goes through a list, also redefining what the variable can be called. Seen: number/the_count
for number in the_count:
    print(f"This is the count {number}")

# same as above
for fruit in fruits:
    print(f"A fruit of type: {fruit}")

# also we can go through mixed lists too
# notice we have to use {} since we don't know what's in it
for i in change:
    print(f"I got {i}")

# we can also build lists, first start with an empty one
elements = [ ]

# then use the range function to do 0 to 5 counts. Must always used one more than you think so that it lists all. seen as 6 instead of 5 
for i in range(0,6):
    print(f"Adding {i} to the lists.")
    # append is a function that list understands.
    # there are a bunch of other list operations you can use
    # you cant use certain ones in this example though becuase of the range()
    elements.append(i)

# now we can print them out too
for i in elements:
    print(f"Element was: {i}")



# an example of what lists look like:
# hairs = ['brown', 'blonde', 'red']
# eyes = ['brown', 'blue', 'green']
# weights = [1, 2, 3, 4]
