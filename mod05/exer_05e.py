real_u = "python"
real_psw = "rules"

count = 0
while True:
    user = input("Username: ")
    password = input("Password: ")
    count += 1

    if count == 5:
        print("Access denied")
        break

    if user == real_u and password == real_psw:
        print("Welcome")
        break
    else:
        continue

