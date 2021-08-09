print("What is your goal at the end of this?", end=' ')
goal = input()
print("How will you accomplish this?", end = ' ')
accomplish_it = input()
print("How many months will it take you to accomplish this?", end = ' ')
time = int(input())

print(f"So your goal is {goal}, and you plan on accomplishing it by {accomplish_it}.")
print(f"It will take you {time} months to complete this.")