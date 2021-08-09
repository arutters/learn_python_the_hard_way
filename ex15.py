from os import close
from sys import argv
# the first 2 lines are using argv to get a filename
script, filename = argv

# below is saying what txt is going to do when it is used
txt = open(filename)

# # just simple printing below using argv and filling in the script
print(f"Here's your file {filename}:")

# #  seems like below is just asking the computer to read what the file is
print(txt.read())

print("Type the file name again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())

close
# since something is being pulled from another file, when running the program you would say
#  python ex15.py ex15_sample.txt
