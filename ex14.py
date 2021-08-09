from sys import argv

script, user_name, friends_name = argv

# Whatever you put in single quotes (below here) is what will appear next to the prompt
prompt = '~ '

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print("How many friends are with you?")
friend_there = int(input(prompt))

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
You have {friend_there} friend there with you.
Is his name {friends_name}?
""")