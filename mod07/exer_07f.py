def pizza(diam, price):
    area = (diam/2)*(diam/2)*3.14
    value = price/area
    return value


diam1 = float(input("Give me the diameter of the first pizza: "))
diam2 = float(input("Give me the diameter of the second pizza: "))
price1 = float(input("Give me the price of the first pizza: "))
price2 = float(input("Give me the price of the second pizza: "))

value1 = pizza(diam1, price1)
value2 = pizza(diam2, price2)

if value1 < value2:
    print("The first pizza cost less per square meter than the second one")
elif value2 < value1:
    print("The second pizza cost less per square meter than the first one")   
else: 
    print("Same Same!")