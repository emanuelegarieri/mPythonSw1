import csv
import os

from pathlib import Path
from models import Player


progress_names = [
    "work_clothes_worn",
    "hands_washed",
    "salad_prepared",
    "salad_plated",
    "kitchen_clean",
    "bio_bag_full",
    "bio_bag_disposed",
    "clothes_dirty",
    "towel_dirty",
    "clothes_returned",
    "towel_returned"
]

project_folder = Path(__file__).parent


def save_path(code):
    if not code or len(code) > 40:
        raise ValueError("The save code is not valid.")

    for character in code:
        if character not in "abcdefghijklmnopqrstuvwxyz0123456789":
            raise ValueError("Use only letters a-z and numbers.")

    filename = "save_" + code + ".csv"
    return project_folder / filename


def show_start_text(filename):
    path = os.path.join(project_folder, filename)

    try:
        with open(path, "r", encoding="utf-8") as file:
            print()
            print(file.read().strip())
    except OSError:
        print("Could not read " + filename)


def save_game(player, rooms, code):
    try:
        with open(
            save_path(code),
            "w",
            newline="",
            encoding="utf-8"
        ) as file:
            writer = csv.writer(file)

            writer.writerow(["name", player.name])
            writer.writerow(["age", player.age])
            writer.writerow(["location", player.location.name])

            inventory_names = []
            for item in player.items:
                inventory_names.append(item.name)

            writer.writerow(["inventory", "|".join(inventory_names)])

            for room in rooms:
                room_item_names = []

                for item in room.items:
                    room_item_names.append(item.name)

                writer.writerow([
                    "room_" + room.name,
                    "|".join(room_item_names)
                ])

            for progress_name in progress_names:
                writer.writerow([
                    progress_name,
                    getattr(player, progress_name)
                ])

        return True

    except (OSError, ValueError):
        print("Could not save the game.")
        return False


def load_game(rooms, code):
    try:
        data = {}

        with open(
            save_path(code),
            "r",
            newline="",
            encoding="utf-8"
        ) as file:
            reader = csv.reader(file)

            for row in reader:
                if len(row) == 2:
                    data[row[0]] = row[1]

        room_lookup = {}
        item_lookup = {}

        for room in rooms:
            room_lookup[room.name] = room

            for item in room.items:
                item_lookup[item.name] = item

        player = Player(
            data["name"],
            int(data["age"]),
            room_lookup[data["location"]]
        )

        inventory_names = data["inventory"].split("|")

        for item_name in inventory_names:
            if item_name:
                player.items.append(item_lookup[item_name])

        for room in rooms:
            room.items = []
            saved_items = data["room_" + room.name].split("|")

            for item_name in saved_items:
                if item_name:
                    room.items.append(item_lookup[item_name])

        for progress_name in progress_names:
            value = data[progress_name] == "True"
            setattr(player, progress_name, value)

        return player

    except (OSError, ValueError, KeyError, csv.Error):
        raise ValueError("The saved game is missing or invalid.")