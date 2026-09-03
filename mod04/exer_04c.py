""" # Write a program that asks for the biological gender and hemoglobin value (g/l). 
The program the notifies the user if the hemoglobin value is low, normal or high.
A normal hemoglobin value for adult females is between 117-155 g/l.
A normal hemoglobin value for adult males is between 134-167 g/l. """


gender = input("What is your biological gender? ")
hemo = int(input("What is your hemoglobin value? "))

low = "Your hemoglobine level is low"
normal = "Your hemoglobine level is normal"
high = "Your hemoglobine level is high"

if gender == "male":
    if hemo < 134:
        print(low)
    elif hemo < 168:
        print(normal)
    else:
        print(high)
if gender == "female":
    if hemo < 117:
        print(low)
    elif hemo < 156:
        print(normal)
    else:
        print(high)

