cars = 100
#The = equal symbol is used to give data a name
space_in_a_car = 4
#By taking out the decimal after a number, it eleminates it from the translated variable altogether
#The decimal is considered a "floating point" number
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

#The _ underscore character is used a lot to put an imaginary space between words in variable names


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
#The words that come after the first comma and before the second are the specific variable the program will input into the text
