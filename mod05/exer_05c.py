num = input("Enter a number: ")
smallest = 0
largest = 0

while num != "":
    if smallest == 0:
        smallest = int(num)
    if int(num) < smallest:
        smallest = int(num)
    if int(num) > largest:
        largest = int(num)
    num = input("Enter a number: ")

print(smallest)
print(largest)