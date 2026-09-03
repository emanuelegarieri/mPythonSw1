def converter(gallons):
    return gallons * 3.785

while True:
    gallons = float(input("Convert gallons in liters: "))
    if gallons < 0:
        break
    else:
        print(converter(gallons))