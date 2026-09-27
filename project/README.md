# Green Kitchen Adventure

Emanuele Garieri

## Game idea

Green Kitchen Adventure is a command-line game about preparing a salad and
leaving the kitchen clean.

The player starts in the Changing Room. First, they must collect the Work
Clothes and Clean Towel. Collecting the Work Clothes automatically puts them
on. Without both items, the player cannot enter the Kitchen.

In the Kitchen, the player must wash their hands before collecting ingredients
and objects. After collecting everything needed, they can prepare and plate
the salad. This also fills the Bio Bag with food waste.

To win, the player must clean the Kitchen, dispose of the full Bio Bag in the
Garbage Room, and return the dirty work clothes and towel to the Changing
Room. The `finish` command serves the salad only when every task is complete.
Otherwise, the game says that something is still missing.

The game has three rooms: Changing Room, Kitchen, and Garbage Room. The rooms
are connected, and the player chooses where to go using numbered options.
The game is suitable for players aged 12 and over.

## How to play

Enter the number beside an action in the main menu. When moving or collecting
an item, choose the number shown in that list. The numbers are assigned again
each time a list is displayed.

1. **Mission**:   Read the objective.
2. **Look**:      See the current room, its items, and its exits.
3. **Move**:      Go to another room.
4. **Wash**:      Wash your hands in the Kitchen.
5. **Collect**:   Pick up an item from the current room.
6. **Inventory**: See the items you are carrying and their weights.
7. **Prepare**:   Prepare and plate the salad when you have collected everything needed.
8. **Clean**:     Clean the Kitchen.
9. **Dispose**:   Throw away the full Bio Bag in the Garbage Room.
10. **Return**:   Return the dirty work clothes and towel in the Changing Room.
11. **Finish**:   Serve the salad and win if all tasks are complete.
12. **Tip**:      Read a real-life tip about reducing food waste.
13. **Exit**:     Leave the game.

## Sustainable development

The game relates to Sustainable Development Goal 12: Responsible Consumption
and Production. The player uses the available ingredients, separates food
waste into a Bio Bag, and cleans up after preparing the meal. The
sustainability tip also encourages checking food already at home before
shopping and using ingredients that will expire soon.

## Project structure

- `game.py` creates the rooms and items, displays the menus, and runs the game.
- `models.py` contains the `Item`, `Room`, and `Player` classes. The player
  object stores the inventory, current location, and progress through the game.

Run the game with `python game.py` from the project folder.

This is the Project 4 version. Reading the introduction from separate text
files and saving or loading progress are planned for Project 5 and are not
implemented yet.