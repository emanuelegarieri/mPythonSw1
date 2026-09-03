import math


def calculate_unit_price(diam, price):
    radius = diam / 200
    area = math.pi * radius**2
    value = price / area

    return value

diam1 = float(input("Enter the diameter of the first pizza (cm): "))
price1 = float(input("Enter the price of the first pizza (euros): "))
diam2 = float(input("Enter the diameter of the second pizza (cm): "))
price2 = float(input("Enter the price of the second pizza (euros): "))

value1 = calculate_unit_price (diam1, price1)
value2 = calculate_unit_price (diam2, price2)

print(f"Unit price of the first pizza: {value1:.2f} euros/m²")
print(f"Unit price of the second pizza: {value2:.2f} euros/m²")

if value1 < value2:
    print("The first pizza provides better value for money.")
elif value2 < value1:
    print("The second pizza provides better value for money.")   
else: 
    print("Same Same!")