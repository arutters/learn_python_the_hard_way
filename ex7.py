print("Mary had a little lamb.")
print("Its fleece was white as {}.".format('snow'))
# typically you use ' ' for shorter strings
# 'snow' used above, is just a string with the word in it. 
# variables wont have a single quotes around them 
print("And everywhere that Mary went.")
print("." * 10) # what'd that do?

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch end = ' ' at the end. try removing it to see what happens
# adding end = '\n' will start a new line
# the end = ' ' is to add a space to the end of the word before the next
# you can add text in between the ' ' to add it to the other text that its taking
print(end1 + end2 + end3 + end4 + end5 + end6, end = '\n\n@')
print(end7 + end8 + end9 + end10 + end11 + end12)
