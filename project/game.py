player_name = input("Enter your name: ")
player_age = int(input("Enter your age: "))
inventory = []


def show_mission():
    print("\nMISSION")
    print("The kitchen is producing too much waste.")
    print("Your objective is to collect useful items and make the kitchen sustainable.\n")


def collect_item(items):
    item = input("What item did you find? ").strip()
    if item == "":
        print("It dropped from your hands!\n")
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
    print("Plan properly your meals and ingredients to reduce food waste.\n")


def quit_game():
    print("\nThank you for playing Green Kitchen Adventure!")


# Print Name and Age
print(f"\nPlayer: {player_name}")
print(f"Age: {player_age}")

# Block if underage
if player_age < 12:
    print("You are a minor. The game will now close.")

# Otherwise
else:
    #Welcome and options
    print(f"\nWelcome, {player_name}!")
    print("The kitchen needs your help.")
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
        # If mission
        if command == "mission":
            show_mission()
        # If collect
        elif command == "collect":
            collect_item(inventory)
        # If Inventory
        elif command == "inventory":
            show_inventory(inventory)
        # If tip
        elif command == "tip":
            show_tip()
        # IF exit
        elif command == "exit":
            quit_game()
            break
        # If error
        else:
            print("Unknown command. Please choose a command from the menu.")