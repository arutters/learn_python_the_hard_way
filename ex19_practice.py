def number_of_pets(number_dogs, number_cats):
    print(f"I have {number_dogs} dogs, and {number_cats} cats.")
    print("One day I will want even more!")

number_of_pets(2,5)

def users_pets(user_dogs, user_cats):
    print(f"You have {user_dogs} dogs.")
    print(f"You have {user_cats} cats.")
    print("That's pretty neat!")
    
users_pets(int(input("How many dogs do you have? ")), int(input("How many cats do you have? ")))


# below is another way of doing what is written above
# print("How many dogs do you have?")
# # user_dogs = input("~ ") 
# print("How many cats do you have?")
# # user_cats = input("~ ")
# print(f"So, you have {user_dogs} dogs, and {user_cats} cats.")

# below is just a little practice
# print("One day:")
# goal_dogs = 10
# goal_cats = 3
# number_of_pets(goal_dogs, goal_cats)