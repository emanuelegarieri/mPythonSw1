def gallons_to_liters(gallons):
    return gallons * 3.785

while True:
    gallons = float(input("Enter a volume in American gallons (negative value to quit): "))
    if gallons < 0:
        print("Program finished.")
        break
    else:
        print(f"{gallons:.1f} American gallons is {gallons_to_liters(gallons):.2f} liters.")