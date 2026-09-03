real_u = "python"
real_psw = "rules"

count = 0
while True:
    user = input("Enter username: ")
    password = input("Enter password: ")
    count += 1

    if count == 5:
        print("Incorrect username or password. Please try again.")
        break

    if user == real_u and password == real_psw:
        print("Welcome")
        break
    else:
        continue

