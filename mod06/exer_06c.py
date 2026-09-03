number = int(input("Check if this number is a prime number: "))

if number < 2:
    print("Nope!")
else:
    for n in range(2, number):
        if number % n == 0:
            print("Nope!")
            break
    else:
        print("Yep!")