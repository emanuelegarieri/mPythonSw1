import random


sides = int(input("How many sides has yor dice? "))
def roll(sides):
    return random.randint(1, sides)

while True:
    result = roll()
    print(result)
    if result == sides:
        break

