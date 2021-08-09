print("""You enter a dark room with two doors.
Do you go through door #1 or door #2?""")

door = input("~ ")

if door == "1":
    print("Jackson is waiting for you there with a toy, and wants you to play with him.")
    print("What do you do?")
    print("1. Grab the toy and play tug-o-war.")
    print("2. Exit though the door you entered.")

    jackson = input("~ ")

    if jackson == "1":
        # print("You have tired him out from playing with him.")
        # print("On a scale from 1-10, how much do you love him?")
        #This is an alternate version i made to see if this would work with a sliding scale. 
        # love = input(0 < 10)

        # if love == (1 <= 5):
        #     print("That is not a lot and you should be ashamed of yourself.")
        # elif love == (6 <= 10):
        #     print("Jackson loves you just as much.")
        # else:
        #     print("Please stop with the shenanigans.")
        print("You have made Jackson very happy, and he will smother you with kisses for the rest of eternity.")
        print("He is now hungry from all of that playtime. Will you feed him?")
        print("1. Yes")
        print("2. No")

        food  = input("~ ")

        if food == "1":
            print("His belly is full and now he's ready for a nap.")
        elif food == "2":
            print("He is starved and now eats you.")
        else:
            print("Stop trying to break things.")

    elif jackson == "2":
        print("You can hear Jackson wimpering with sadness on the other side of the door.")
        print("You are an awful person to make a puppy cry, and now you will die.")
    else: 
        print("Why are you trying to be difficult?")
        print("Did you really thing I'd leave a loose end like this?")

elif door == "2":
    print("Max is asleep in his bed.")
    print("There are a bag of treats on the floor.")
    print("What do you do?")
    print("1. Wake Max and give him a treat.")
    print("2. Let Max sleep and don't give him anything.")

    max = input("~ ")
    
    if max == "1":
        print("Max happily eats the treats and lets you pet him for ever and ever and ever and ever...")
    elif max == "2":
        print("Max wakes and see's that you did not give him any treats.")
        print("He teaches you a lesson by biting you.")
    else:
        print("You really thought you were doing something by typing in something other than 1 or 2, didn't you?")
        print("I got this shit on lock.")

else:
    print("Congratulations, you played yourself and now you don't get to see any cute dogs.")