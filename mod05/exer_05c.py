num = input("Enter a number (or press Enter to quit): ")
smallest = 0
largest = 0

while num != "":
    if smallest == 0:
        smallest = float(num)
    if float(num) < smallest:
        smallest = float(num)
    if float(num) > largest:
        largest = float(num)
    num = input("Enter a number (or press Enter to quit): ")

print(f"Smallest number: {smallest:.1f}")
print(f"Largest number: {largest:.1f}")