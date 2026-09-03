gender = input("Enter biological gender (male/female): ").lower()
hemo = float(input("Enter hemoglobin value (g/l): "))

low = "Your hemoglobin is low."
normal = "Your hemoglobin is normal."
high = "Your hemoglobin is high."

if gender == "male":
    if hemo < 134:
        print(low)
    elif hemo < 168:
        print(normal)
    else:
        print(high)
elif gender == "female":
    if hemo < 117:
        print(low)
    elif hemo < 156:
        print(normal)
    else:
        print(high)
else:
    print("Invalid gender.")

