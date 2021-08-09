from sys import argv 
#  read the WYSS section for how to run this
script, first, second, third, fourth = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
print("Your fourth variable is:", fourth)

#  when running this, you would not include 'script' in the command line, only 
# the three variables as it will already name the script whe it prints
# run: python ex.13 first second third

#  if you get an error that means you didnt give it enough parameters or not enough
# arguments on the command line when you run it
