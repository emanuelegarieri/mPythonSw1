where = input("Enter the cabin class (LUX, A, B, or C): ")
if where == "LUX":
    print("Upper-deck cabin with a balcony.")
elif where == "A":
    print("Above the car deck, equipped with a window.")
elif where == "B":
    print("Windowless cabin above the car deck.")
elif where == "C":
    print("Windowless cabin below the car deck.")
else:
    print("Invalid cabin class.")

    