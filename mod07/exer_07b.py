import random


sides = int(input("How many sides has yor dice? "))
def roll_dice(sides):
    return random.randint(1, sides)

while True:
    result = roll_dice(sides)
    print(result)
    if result == sides:
        break

