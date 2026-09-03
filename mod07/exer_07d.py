list = []


def calculate(list):
    sum = 0
    for n in list:
        sum += n
    return sum


while True:
    number = input("Add a number in the sum: ")
    if number == "":
        break
    list.append(int(number))    

print(calculate(list))