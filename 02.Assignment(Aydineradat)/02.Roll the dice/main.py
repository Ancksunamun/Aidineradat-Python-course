
import random

dice = random.randint(1,6)

print("Dice is : " , dice)

while dice == 6:
    print("congratulations dice is:" , dice)
    dice = random.randint(1,6)
    if dice != 6:
        print("Dice is : " , dice)
