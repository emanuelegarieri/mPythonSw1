while True:
    inc = float(input("Enter length in inches (negative value to quit): "))
    if inc < 0:
        print("Program ended.")
        break
    cm = inc*(2.54)
    print(f"{inc:.1f} inches is {cm:.2f} centimeters")