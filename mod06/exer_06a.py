import random

rolls = int(input("How many dices you want to roll?"))
result = 0

for n in range(rolls):
    result += random.randint(1,6)

print(result)