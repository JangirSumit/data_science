import random

DEF_NUMBER = random.randint(1, 10)

counter = 3

print("######### Guessing Challenge #########")
print("\n")
print("Do you think you are good in guessing. Lets play a Game!")
print("\n")
print("Game Rules")
print("1. You will be given 3 chances for Guess")
print("2. You can terminate the game by pressing 2")
print("\n")
print("Guess a number between 1 - 10")
user_number = int(input(">>> "))

while True:
    if DEF_NUMBER > user_number:
        print("Hint! Magic number is bigger than you entered. Please select number.")
        print("--->Available chances :" + str(counter))
        counter -= 1
        user_number = int(input(">>> "))
        continue
    elif DEF_NUMBER < user_number:
        print("Hint! Magic number is lesser than you entered. Please select lesser number.")
        print("--->Available chances :" + str(counter))
        counter -= 1
        user_number = int(input(">>> "))
        continue
    elif DEF_NUMBER == user_number:
        print("Bingo!! You are the champ")
        print("***************\n")
        break
    elif counter == 0:
        print("OOpss! You Loose. Try next time :)")
