player_name = input("Enter your name: ")
player_age = int(input("Enter your age: "))
inventory = []


def show_mission():
    print("\nMISSION")
    print("The community kitchen is producing too much waste.")
    print("Your objective is to collect useful items and make the kitchen sustainable.\n")


def collect_item(items):
    item = input("What item did you find? ").strip()
    if item == "":
        print("No item was added.\n")
    else:
        items.append(item)
        print(f"{item} was added to your inventory.\n")


def show_inventory(items):
    print("\nINVENTORY")
    if len(items) == 0:
        print("Your inventory is empty.\n")
    else:
        for item in items:
            print(f"- {item}")
        print()


def show_tip():
    print("\nSUSTAINABILITY TIP")
    print("Plan meals and reuse ingredients to reduce food waste.\n")


def quit_game():
    print("\nThank you for playing Green Kitchen Adventure!")


print(f"\nPlayer: {player_name}")
print(f"Age: {player_age}")

if player_age < 12:
    print("You are a minor. The game will now close.")
else:
    print(f"\nWelcome, {player_name}!")
    print("The community kitchen needs your help.")
    while True:
        command = input(
            "\nMAIN MENU\n"
            "mission   - Show the mission\n"
            "collect   - Collect an item\n"
            "inventory - Show your inventory\n"
            "tip       - Show a sustainability tip\n"
            "exit    - Exit the game\n"
            "Enter command: "
        ).strip().lower()
        if command == "mission":
            show_mission()
        elif command == "collect":
            collect_item(inventory)
        elif command == "inventory":
            show_inventory(inventory)
        elif command == "tip":
            show_tip()
        elif command == "exit":
            quit_game()
            break
        else:
            print("Unknown command. Please choose a command from the menu.")