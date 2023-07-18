
import random
print("Welcome to our guess nummber game choose a number between 10-40")

cp_num = random.randint(10,40)

counter = 0

while True:
    counter += 1
    player_num = int(input("Plz enter your number"))
    if player_num == cp_num:
        break
    elif player_num > cp_num:
        print("go lower")
    elif player_num < cp_num:
        print("go higher")

print("the number was: " , cp_num , " you found it in: " , counter , " trys")