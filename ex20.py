from sys import argv
# This is setting up the script 
script, input_file = argv
# this sets up the function by defining it and telling it that it needs to read that file
def print_all(f):
    print(f.read())
# defining rewind as the function that will seek where the first line in the file is and write it
# if you were to do seek and another number it would start from that specific line of text
def rewind(f):
    f.seek(0)
# setting up and defining another function and telling the program to read the lines of text from the sample with 
# the corresponding line of text based off of its line number
def print_a_line(line_count, f):
    print(line_count, f.readline())
# this is saying that when you use current_file that the program should open the input script for input_file
current_file = open(input_file)
# printing the given dialogue on a new line after it before it reads the text
print("First let's print the whole file:\n")
# printing the current_file or the script: input_file
print_all(current_file)

print("Now let's rewind, kind of like a tape.")
# using the function that was previously defined to read the sample text but starting at a specific line within it
rewind(current_file)

print("Let's print three lines:")

# all of the below are telling the program how to present the sample text, where it starts at one line and continues 
# by adding a new line for each line of text from the sample
current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1 
print_a_line(current_line, current_file)

