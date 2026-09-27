from models import Item, Player, Room


def show_mission(): # <-- Show mission funcion
    print()
    print(yellow + "Mission:" + reset)
    print("You need to prepare and serve a salad, then clean up responsibly")
    print("Remember also to dispose of the Bio Bag and return the dirty clothes and towel")


def show_room(player): # <-- Show room funcion
    print()
    print(yellow + "You are in the " + player.location.name + ". Around you there are:" + reset)
    print(green + "Items:" + reset)
    # If there are no items in the room
    if len(player.location.items) == 0:
        print("- none")
    else:
        number = 1
        # Otherwise print them with the number
        for item in player.location.items:
            print(str(number) + ". " + item.name)
            number = number + 1
    print()
    print(green + "The exits for other 2 rooms:" + reset)
    number = 1
    # Print the rooms available
    for room in player.location.exits:
        print(str(number) + ". " + room.name)
        number = number + 1


def show_inventory(player):  # <-- Show inventory funcion
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
            print(str(number) + ". " + item.name + " (" + str(item.weight) + " kg)")
            number = number + 1


def show_tip(): # <-- Show tip funcion
    print()
    print(yellow + "Sustainability Tip:" + reset)
    print("Check what you already have before shopping, and plan meals around food that will expire soon.")


def show_menu():
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
    print()
    command = input("Enter number: ").strip()
    return command


def play(player):
    print()
    print(green + "Welcome, " + player.name + "!" + reset)
    print(yellow + "The kitchen needs your help!" + reset)
    print(blue + "You are in the Changing Room now" + reset)
    while True:
        # All the commands here
        command = show_menu()
        if command == "1":
            show_mission()
        elif command == "2":
            show_room(player)
        elif command == "3":
            print()
            # Repeat the available rooms
            print(yellow + "Available rooms:" + reset)
            number = 1
            for room in player.location.exits:
                print(str(number) + ". " + room.name)
                number = number + 1
            print()
            # Ask for choice
            choice = input("Choose a room number: ").strip()
            # Loop for all the other rooms
            selected_room = None
            number = 1
            # For the other rooms
            for room in player.location.exits:
                # If choice it's 1
                if choice == str(number):
                    # Match
                    selected_room = room
                # Otherwise add 1 and repete
                number = number + 1
            # In case of error
            if selected_room is None:
                print(red + "Invalid room number!" + reset)
            # Otherwise message
            else:
                print(player.move(selected_room.name))
        elif command == "4":
            print(player.wash_hands())
        elif command == "5":
            # No items
            if len(player.location.items) == 0:
                print(red + "There are no items to collect here!" + reset)
            else:
                print()
                print(green + "Items in this room:" + reset)
                number = 1
                for item in player.location.items:
                    print(str(number) + ". " + item.name)
                    number = number + 1
                choice = input("Choose an item number: ").strip()
                # Same as for room loop
                selected_item = None
                number = 1
                for item in player.location.items:
                    if choice == str(number):
                        selected_item = item
                    number = number + 1
                if selected_item is None:
                    print(red + "Invalid item number!" + reset)
                else:
                    print(player.collect(selected_item.name))
        elif command == "6":
            show_inventory(player)
        elif command == "7":
            print(player.prepare_salad())
        elif command == "8":
            print(player.clean_kitchen())
        elif command == "9":
            print(player.dispose_bag())
        elif command == "10":
            print(player.return_clothes())
        elif command == "11":
            # Endgame only if salad is plated, kitchen is clean and clothes are returned
            if (player.salad_plated and player.kitchen_clean
                    and player.bio_bag_disposed and player.towel_returned
                    and player.clothes_returned):
                print(green + "You served the salad and closed the clean Kitchen. Good job!" + reset)
                print()
                break
            else:
                print(blue + "Something is still missing. Look carefully!" + reset)
                print()
        elif command == "12":
            show_tip()
        elif command == "13":
            print("Thank you for playing Green Kitchen Adventure!")
            print()
            break
        else:
            print(red + "Invalid menu number! Please choose a number from 1 to 13!" + reset)
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
# For each couple of rooms different than the actual one, so we know the exits
for room in rooms:
    for other_room in rooms:
        if other_room != room:
            room.exits.append(other_room)

player_name = input("Enter your name: ")
player_age = int(input("Enter your age: "))

print()
print("Player: " + player_name)
print("Age: " + str(player_age))


if player_age < 12:
    print()
    print(red + "You are under 12, lucky you!" + reset)
    print()
    print(red + "But, unfortunately you cannot play yet!" + reset)
    print()
    print(red + "The game will now close" + reset)
else:
    player = Player(player_name, player_age, changing_room)
    play(player)
