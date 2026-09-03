import random


def roll():
    return random.randint(1, 6)

while True:
    result = roll()
    print(result)
    if result == 6:
        break

