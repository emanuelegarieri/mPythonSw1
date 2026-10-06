import csv

from pathlib import Path
from models import Player


# Find the folder where this file is
project_folder = Path(__file__).parent


def save_path(code):
    # Create the name of the save file
    filename = "save_" + code + ".csv"

    # Create the full path for the file
    path = project_folder / filename
    return path


def save_game(player, rooms, code):
    # Find the path for the save file
    path = save_path(code)

    # Open the save file for writing
    save_file = open(path, "w", newline="", encoding="utf-8")

    # Create the CSV writer
    writer = csv.writer(save_file)

    # Save the player information
    writer.writerow(["name", player.name])
    writer.writerow(["age", player.age])
    writer.writerow(["location", player.location.name])

    # Take the names of the items in the inventory
    inventory_names = []

    for item in player.items:
        inventory_names.append(item.name)

    # Save the inventory in one row
    writer.writerow(["inventory", "|".join(inventory_names)])

    # Save the items in each room
    for room in rooms:
        room_item_names = []
        for item in room.items:
            room_item_names.append(item.name)
        writer.writerow(["room_" + room.name, "|".join(room_item_names)])

    # Save all the jobs done by the player
    writer.writerow(["work_clothes_worn", player.work_clothes_worn])
    writer.writerow(["hands_washed", player.hands_washed])
    writer.writerow(["salad_prepared", player.salad_prepared])
    writer.writerow(["salad_plated", player.salad_plated])
    writer.writerow(["kitchen_clean", player.kitchen_clean])
    writer.writerow(["bio_bag_full", player.bio_bag_full])
    writer.writerow(["bio_bag_disposed", player.bio_bag_disposed])
    writer.writerow(["clothes_dirty", player.clothes_dirty])
    writer.writerow(["towel_dirty", player.towel_dirty])
    writer.writerow(["clothes_returned", player.clothes_returned])
    writer.writerow(["towel_returned", player.towel_returned])

    # Close the save file
    save_file.close()


def load_game(rooms, code):
    # Find the path of the saved game
    path = save_path(code)

    # Dictionary for all the saved information
    data = {}

    # Open the saved game for reading
    save_file = open(path, "r", newline="", encoding="utf-8")

    # Create the CSV reader
    reader = csv.reader(save_file)

    # Put each saved row in the dictionary
    for row in reader:
        if len(row) == 2:
            data[row[0]] = row[1]

    # Close the save file
    save_file.close()

    # Dictionaries for finding rooms and items by name
    room_lookup = {}
    item_lookup = {}

    # Add all the rooms and items to the dictionaries
    for room in rooms:
        room_lookup[room.name] = room

        for item in room.items:
            item_lookup[item.name] = item

    # Create the player with the saved information
    player = Player(data["name"], int(data["age"]), room_lookup[data["location"]])

    # Take the names of the saved inventory items
    inventory_names = data["inventory"].split("|")

    # Return the saved items to the player inventory
    for item_name in inventory_names:
        if item_name:
            player.items.append(item_lookup[item_name])

    # Return the saved items to each room
    for room in rooms:
        room.items = []
        saved_items = data["room_" + room.name].split("|")

        for item_name in saved_items:
            if item_name:
                room.items.append(item_lookup[item_name])

    # Return all the saved jobs to the player
    player.work_clothes_worn = data["work_clothes_worn"] == "True"
    player.hands_washed = data["hands_washed"] == "True"
    player.salad_prepared = data["salad_prepared"] == "True"
    player.salad_plated = data["salad_plated"] == "True"
    player.kitchen_clean = data["kitchen_clean"] == "True"
    player.bio_bag_full = data["bio_bag_full"] == "True"
    player.bio_bag_disposed = data["bio_bag_disposed"] == "True"
    player.clothes_dirty = data["clothes_dirty"] == "True"
    player.towel_dirty = data["towel_dirty"] == "True"
    player.clothes_returned = data["clothes_returned"] == "True"
    player.towel_returned = data["towel_returned"] == "True"

    # Return the loaded player to the main game
    return player