while True:
    inc = input("Enter length in inches (negative value to quit): ")
    if inc == "":
        print("Program ended.")
        break
    cm = float(inc)*(2.54)
    print(f"{float(inc):.1f} inches is {cm:.2f} centimeters")
