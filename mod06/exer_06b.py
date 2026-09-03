numbers = []

number = input("Add a number: ")
while True:
    number = input("Add a number: ")
    if number == "":
        break
    numbers.append(int(number))


print(sorted(numbers, reverse=True)[:5])