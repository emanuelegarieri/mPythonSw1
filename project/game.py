from models import Item, Player, Room
from storage import load_game, save_game, save_path


def show_mission(): # <-- Show mission function
    print()
    print(yellow + "Mission:" + reset)
    print("You need to prepare and serve a salad, then clean up responsibly")
    print("Remember also to dispose of the Bio Bag and return the dirty clothes and towel")


def show_room(player): # <-- Show room function
    print()
    print(yellow + "You are in the " + player.location.name + ". Around you there are:" + reset)
    print(green + "Items:" + reset)

    # If there are no items in the room
    if len(player.location.items) == 0:
        print("- none")
    # Otherwise print them with the number
    else:
        number = 1
        for item in player.location.items:
            print(str(number) + ". " + item.name)
            number = number + 1
            
    # Prints the other rooms
    print()
    print(green + "The exits for other 2 rooms:" + reset)
    number = 1
    # Print the rooms available
    for room in player.location.exits:
        print(f"{number}. {room.name}")
        number = number + 1


def show_inventory(player):  # <-- Show inventory function
    print()
    print(yellow + "Inventory:" + reset)

    # If empty
    if len(player.items) == 0:
        print("Your inventory is empty!")

    # If not empty
    else:
        number = 1
        # For each of the player's item
        for item in player.items:
            # Print it
            print(f"{number}. {item.name} ({item.weight} kg)")
            number = number + 1


def show_tip(): # <-- Show tip function
    print()
    print(yellow + "Sustainability Tip:" + reset)
    print("Check what you already have before shopping, and plan meals around food that will expire soon.")


def show_menu(): # <-- Show menu command function
    print()
    print(yellow + "What do you want to do?" + reset)
    print("1. Mission   - Show the mission")
    print("2. Look      - Look around")
    print("3. Move      - Go to another room")
    print("4. Wash      - Wash your hands")
    print("5. Collect   - Collect an item")
    print("6. Inventory - Show your items")
    print("7. Prepare   - Prepare and plate the salad")
    print("8. Clean     - Clean the Kitchen")
    print("9. Dispose   - Throw away the full Bio Bag")
    print("10. Return   - Return dirty clothes and towel")
    print("11. Finish   - Serve the salad and close the Kitchen")
    print("12. Tip      - Show a sustainability tip")
    print("13. Exit     - Exit the game")
    print("14. Save     - Save your progress")
    print()
    command = input("Enter number: ").strip()
    return command


def start_game():  # <-- Start the game and get player and save code
    # Intro and Instructions files
    start_files = ["intro.txt", "instructions.txt"]

    # Open and print both files
    for filename in start_files:
        text_file = open(filename, "r", encoding="utf-8")
        text = text_file.read()
        text_file.close()

        print()
        print(text)

    # Start the selection
    while True:
        print()
        print("1. New game")
        print("2. Continue a saved game")
        print("3. Close")
        choice = input("Enter number: ").strip()

        # If close, return empty player and save code
        if choice == "3":
            return None, None
        
        # If wrong choice, go back
        if choice != "1" and choice != "2":
            print("Choose a number from 1 to 3.")
            continue

        # Ask the code for the saved game
        code = input(
            "Enter your save code using letters a-z and numbers: "
        ).strip().lower()

        # If the code is empty, go back
        if code == "":
            print("Please enter a save code.")
            continue

        # Create the path for this save code
        path = save_path(code)

        # If the player wants to continue a saved game
        if choice == "2":

            # If the saved game does not exist, go back
            if not path.exists():
                print("No saved game was found with that code.")
                continue

            # Load the player from the saved game
            player = load_game(rooms, code)
            print("Saved game loaded.")
            return player, code
        
        # If the code already exists, ask for another code
        if path.exists():
            print("That code already has a saved game. Continue it or choose another code.")
            continue

        # Ask the player name
        player_name = input("Enter your name: ").strip()

        # If the name is empty, go back
        if not player_name:
            print("Please enter a name.")
            continue

        # Ask the player age as text
        player_age = input("Enter your age: ").strip()

        # If the age is not a number, go back
        if not player_age.isdigit():
            print("Please enter your age as a whole number.")
            continue

        # Change the age from text to number
        player_age = int(player_age)
        print()
        print("Player: " + player_name)
        print("Age: " + str(player_age))

        # If the player is under 12, close the game
        if player_age < 12:
            print()
            print(red + "You are under 12, lucky you!" + reset)
            print()
            print(red + "But, unfortunately you cannot play yet!" + reset)
            print()
            print(red + "The game will now close" + reset)
            return None, None
        
        # Create the new player in the Changing Room
        player = Player(player_name, player_age, changing_room)

        # Return the player and the save code
        return player, code

    
def play(player, save_code):  # <-- Main game function
    # Print welcome messages
    print()
    print(green + "Welcome, " + player.name + "!" + reset)
    print(yellow + "The kitchen needs your help!" + reset)
    print(blue + "You are in the " + player.location.name + " now" + reset)

    # Keep the game running
    while True:
        # Show the menu and get the command
        command = show_menu()

        # Show the mission
        if command == "1":
            show_mission()

        # Show the current room
        elif command == "2":
            show_room(player)

        # Move to another room
        elif command == "3":
            print()
            print(yellow + "Available rooms:" + reset)

            # Print all the available rooms with a number
            number = 1
            for room in player.location.exits:
                print(str(number) + ". " + room.name)
                number = number + 1

            print()

            # Ask which room the player wants
            choice = input("Choose a room number: ").strip()

            # Start without a selected room
            selected_room = None
            number = 1

            # Search for the room with the selected number
            for room in player.location.exits:
                if choice == str(number):
                    selected_room = room

                number = number + 1

            # If no room matches the number
            if selected_room is None:
                print(red + "Invalid room number!" + reset)

            # Otherwise move to the selected room
            else:
                print(player.move(selected_room.name))

        # Wash the player's hands
        elif command == "4":
            print(player.wash_hands())

        # Collect an item
        elif command == "5":
            # If there are no items in the room
            if len(player.location.items) == 0:
                print(red + "There are no items to collect here!" + reset)

            else:
                print()
                print(green + "Items in this room:" + reset)

                # Print all the items with a number
                number = 1
                for item in player.location.items:
                    print(str(number) + ". " + item.name)
                    number = number + 1

                # Ask which item the player wants
                choice = input("Choose an item number: ").strip()

                # Start without a selected item
                selected_item = None
                number = 1

                # Search for the item with the selected number
                for item in player.location.items:
                    if choice == str(number):
                        selected_item = item

                    number = number + 1

                # If no item matches the number
                if selected_item is None:
                    print(red + "Invalid item number!" + reset)

                # Otherwise collect the selected item
                else:
                    print(player.collect(selected_item.name))

        # Show the player inventory
        elif command == "6":
            show_inventory(player)

        # Prepare and plate the salad
        elif command == "7":
            print(player.prepare_salad())

        # Clean the Kitchen
        elif command == "8":
            print(player.clean_kitchen())

        # Dispose of the Bio Bag
        elif command == "9":
            print(player.dispose_bag())

        # Return the dirty clothes and towel
        elif command == "10":
            print(player.return_clothes())

        # Try to finish the game
        elif command == "11":
            # Finish only if all the required jobs are done
            if (player.salad_plated and player.kitchen_clean
                    and player.bio_bag_disposed and player.towel_returned
                    and player.clothes_returned):
                print(
                    green
                    + "You served the salad and closed the clean Kitchen. Good job!"
                    + reset
                )
                print()
                break

            # Otherwise tell the player that something is missing
            else:
                print(
                    blue
                    + "Something is still missing. Look carefully!"
                    + reset
                )
                print()

        # Show a sustainability tip
        elif command == "12":
            show_tip()

        # Save and exit the game
        elif command == "13":
            save_game(player, rooms, save_code)
            print("Game saved. Your code is: " + save_code)
            print("Thank you for playing Green Kitchen Adventure!")
            print()
            break

        # Save without exiting the game
        elif command == "14":
            save_game(player, rooms, save_code)
            print("Game saved. Your code is: " + save_code)

        # If the menu command is wrong
        else:
            print(
                red
                + "Invalid menu number! Please choose a number from 1 to 14!"
                + reset
            )
            print()

# Colors
blue = "\033[34m"
yellow = "\033[33m"
green = "\033[32m"
red = "\033[31m"
reset = "\033[0m"

# Create rooms 
garbage_room = Room("Garbage Room", [])

changing_room = Room("Changing Room", [
    Item("Work Clothes", 0.8),
    Item("Clean Towel", 0.2)
])

kitchen = Room("Kitchen", [
    Item("Lettuce", 0.2),
    Item("Feta", 0.2),
    Item("Tomatoes", 0.3),
    Item("Olive Oil", 0.5),
    Item("Salt and Pepper", 0.1),
    Item("Cucumber", 0.3),
    Item("Bowl", 0.5),
    Item("Plate", 0.4),
    Item("Bio Bag", 0.1)
])

# Make the rooms as a list
rooms = [changing_room, kitchen, garbage_room]
# Connect each room with all the other rooms
for room in rooms:
    for other_room in rooms:
        if other_room != room:
            room.exits.append(other_room)

# Start or load the game
player, save_code = start_game()

# Play only if the player did not close the game
if player is not None:
    play(player, save_code)