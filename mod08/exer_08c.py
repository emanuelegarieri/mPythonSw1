airports = {}

while True:
    print()
    print("Airport Data Management")
    print("1. Enter a new airport")
    print("2. Fetch airport information")
    print("3. Quit")
    choice = input("Please choose an option (1-3): ")
    if choice == "1":
        icao = input("Enter the ICAO code: ").upper()
        if len(icao) != 4:
            print("Enter a valid ICAO code")
            continue
        else:
            airport = input("Enter the airport name: Airport ")
            airports[icao] = airport
        print(f"{airport} with ICAO code {icao} has been added.")
    elif choice == "2":
        icao = input("Enter the ICAO code: ").upper()
        if icao in airports:
            print(f"The airport with ICAO code {icao} is {airports[icao]}.")
        else:
            print(f"No airport found with ICAO code {icao}.")

    elif choice == "3":
        print("Thank you for using the Airport Data Management system. Goodbye!")
        break

    else: continue