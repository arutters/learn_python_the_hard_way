# View the "name" of the script as cheese_and_crackers to make it easier to 
# think about. Anywhere that you put cheese_and_crackers it will also put
# what follows it in the script. You can change the variables when you
# "unpack it" later on so: changing it from cheese_count to any other defined variable
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses.")
    print(f"You have {boxes_of_crackers} boxes of crackers.")
    print("Man that's enough for a party!")
    print("Get a blanket. \n")

print("We can just give the function numbers directly.")
cheese_and_crackers(20, 30)
# ^ this is the variable that you previously defined at the top
# by using commas to separate the numbers in () you are assigning counts to
# the cheese_count and boxes_of_crackers count 

print("Or we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese,amount_of_crackers)
# this is technically replacing what was input into the script before
# such as the cheese_count and boxes_of_crackers

print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
