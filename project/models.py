class Item:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight


class Room:
    def __init__(self, name, items):
        self.name = name
        self.items = items
        self.exits = []


class Player:
    def __init__(self, name, age, location):
        self.name = name
        self.age = age
        self.location = location
        self.items = []
        # Boolean party!!
        self.work_clothes_worn = False
        self.hands_washed = False
        self.salad_prepared = False
        self.salad_plated = False
        self.kitchen_clean = False
        self.bio_bag_full = False
        self.bio_bag_disposed = False
        self.clothes_dirty = False
        self.towel_dirty = False
        self.clothes_returned = False
        self.towel_returned = False


    def has_item(self, name):
        for item in self.items:
            if item.name == name:
                # If it has collected
                return True
        # If not
        return False


    def move(self, destination):
        # For each other room
        for room in self.location.exits:
            # if it's equal to the destination
            if room.name.lower() == destination.lower():
                # If kitchen, check for blocks, if any message and exit
                if room.name == "Kitchen":
                    if not self.work_clothes_worn:
                        return blue + "Put on the work clothes first" + reset
                    if not self.has_item("Clean Towel"):
                        return blue + "Take the clean towel first" + reset
                # Otherwise move
                self.location = room
                return blue + "You entered the " + room.name + reset


    def collect(self, name):
        # :)
        if self.location.name == "Kitchen" and not self.hands_washed:
            return red + "Wash your hands before collecting kitchen items!" + reset
        # Collect the available items and remove them from the room
        for item in self.location.items:
            if item.name.lower() == name.lower():
                self.location.items.remove(item)
                self.items.append(item)
                # Unlock the kitchen
                if item.name == "Work Clothes":
                    self.work_clothes_worn = True
                    return blue + "You collected and put on the Work Clothes" + reset
                return blue + item.name + " was added to your inventory" + reset


    def wash_hands(self):
        # Filter
        if self.location.name != "Kitchen":
            return blue + "Wash your hands in the Kitchen" + reset
        # Otherwise wash hands is true, we can wash them multiple times :)
        self.hands_washed = True
        return blue + "You washed your hands" + reset


    def prepare_salad(self):
        # If not kitchen
        if self.location.name != "Kitchen":
            return blue + "You can only prepare the salad in the Kitchen" + reset
        # If already prepared
        if self.salad_prepared:
            return blue + "The salad is already prepared and plated" + reset
        # If there are still items to collect in the kitchen (easy way)
        if len(self.location.items) != 0:
            return blue + "Collect all the Kitchen items first" + reset
        # Boolean swithch
        self.salad_prepared = True
        self.salad_plated = True
        self.bio_bag_full = True
        self.clothes_dirty = True
        return blue + "The salad is prepared and plated! The Bio Bag is now full" + reset


    def clean_kitchen(self):
        # If NOT kitchen
        if self.location.name != "Kitchen":
            return blue + "Clean the Kitchen while you are there" + reset
        # If NOT already prepared
        if not self.salad_prepared:
            return blue + "Prepare the salad before cleaning" + reset
        # If already clean
        if self.kitchen_clean:
            return blue + "The Kitchen is already clean" + reset
        # If the player has not the cleaning towel
        if not self.has_item("Clean Towel"):
            return red + "You need the towel to clean!" + reset
        # Boolean party!!
        self.kitchen_clean = True
        self.towel_dirty = True
        return blue + "You cleaned the Kitchen! The towel is now dirty" + reset


    def dispose_bag(self):
        # Not in the room
        if self.location.name != "Garbage Room":
            return blue + "Take the Bio Bag to the Garbage Room" + reset
        # If not prepared or not bio bag collected
        if not self.bio_bag_full or self.bio_bag_disposed:
            return blue + "You do not have a full Bio Bag to dispose of" + reset
        # Throw it away
        for item in self.items:
            if item.name == "Bio Bag":
                # Remove also the bag
                self.items.remove(item)
                # Bool
                self.bio_bag_disposed = True
                return blue + "You disposed of the full Bio Bag" + reset
        return blue + "The Bio Bag is not in your inventory" + reset


    def return_clothes(self):
        # No room
        if self.location.name != "Changing Room":
            return blue + "Return dirty clothes in the Changing Room" + reset
        # All prepared and clean
        if not self.salad_plated or not self.kitchen_clean:
            return blue + "Prepare the salad and clean the Kitchen first" + reset
        # If clothes are changed and towel is away
        if self.clothes_returned and self.towel_returned:
            return blue + "The dirty clothes and towel are already returned" + reset
        # If never collected
        if not self.clothes_dirty or not self.towel_dirty:
            return blue + "There are no dirty clothes and towel to return" + reset
        # If is missing one of the changing room item before returning them
        clothes_item = None
        towel_item = None
        for item in self.items:
            if item.name == "Work Clothes":
                clothes_item = item
            if item.name == "Clean Towel":
                towel_item = item
        if clothes_item is None or towel_item is None:
            return blue + "The work clothes or towel are missing" + reset
        # Put to wash and remove
        self.items.remove(clothes_item)
        self.items.remove(towel_item)
        # Boolean switch
        self.work_clothes_worn = False
        self.clothes_returned = True
        self.towel_returned = True
        return blue + "You returned the dirty work clothes and towel" + reset


# Colors
blue = "\033[34m"
red = "\033[31m"
reset = "\033[0m"