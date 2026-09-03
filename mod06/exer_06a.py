import random

rolls = int(input("How many dice to roll: "))
result = 0

for n in range(rolls):
    result += random.randint(1,6)

print(f"Sum of the dice: {result}")