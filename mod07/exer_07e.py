list = []


def clean(list):
    cleaned = []
    for n in list:
        if n % 2 == 0:
            cleaned.append(n)
    return cleaned


while True:
    number = input("Add a number to the least to clean: ")
    if number == "":
        break
    list.append(int(number))    

print(clean(list))