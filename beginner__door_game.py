# from sys import exit


def start():
    print("You enter a room filled with happiness and sunshine.")
    print("There are two doors in front of you.")
    print("Which door do you enter?")

    choice = input("~ ")

    if choice == "1":
        jacksons_room()
    elif choice == "2":
        maxs_room()
    else:
        print("All of the sunshine and happiness is replaced by a bad storm. You are killed by lightning.")

def jacksons_room():
    print("There is a small dog inside with a beautiful brindle coat.")
    print("He is very cute. Like literally the cutest dog you have ever seen.")
    print("He looks like he has a collar with a name tag. Do you want to find out what his name is?")

    choice = input("~ ")

    if choice == "yes":
        jacksons_name()
    elif choice == "no":
        trap_door()
    else:
        print("You lose. Job not well done.")

def maxs_room():
    print("There is a very cute, long, pudgy little doggie curled up in a soft bed.")
    print("There is a bowl right by him with the name, 'MAX' written on it.")
    print("Are you going to fill it with food, and then wake him?")

    choice = input("~ ")

    if choice == "yes":
        max_wake_up()
    elif choice == "no":
        print("Max hears you and wakes up to eat you alive.")
    else:
        print("You lose. Job not well done.")

def max_wake_up():
    print("Max is very grateful that you have filled his food bowl.")
    print("He repays your kindness by rolling over and letting you pet him.")
    print("Will you?")

    choice = input("~ ")

    if choice == "yes":
        print("You have won the ultimate prize of having Max as your best friend (so long as you keep petting him).")
    elif choice == "no":
        trap_door()
    else: 
        print("You lose. Job not well done.")



def jacksons_name():
    print("His name is Jackson!")
    print("What a cute name for a cute dog.")
    print("Jackson gets real close, trying to find out more about you.")
    print("Will you let him sniff your butt?")

    choice = input("~ ")

    if choice == "yes":
        print("Jackson got a deep whiff and now you two will be friends for ever and ever and ever and ever...")
    elif choice == "no":
        trap_door()
    else:
        print("You lose. Job not well done.")

def trap_door():
    print("You fall through a trap door in the floor, and land on rocks and die.")



start()

# if choice == 1:
        # print("There is a small dog inside with a beautiful brindle coat.")
        # print("He is very cute. Literally the cutest dog you have ever seen.")
        # print("He looks like he has a collar with a name tag. Do you want to find out what his name is?")

        # choice = input("~ ")

        # if choice == "yes":
        #     print("The dog tag says his name is Jackson!")
        #     print("What a cute name for a cute dog.")
        #     print("He gets real close to, trying to find out more about you.")
        #     print("Will you let him sniff your butt?")

        #     choice = input("~ ")

        #     if choice == "yes":
        #         print("He got a deep whiff, and now you two are the best of friends.")
        #         start()print("You and Jackson know each other very well now, and will be BFF's forever and ever and ever and ever...")
        #     elif choice == "no":
        #         print("He doesn't know who you are, so he kills you.")
        #     else: 

 