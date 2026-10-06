# Green Kitchen Adventure

Emanuele Garieri

## Game idea

Green Kitchen Adventure is a command-line game about preparing a salad and leaving the Kitchen clean.

The player starts in the Changing Room. First, they must collect the Work Clothes and Clean Towel. Collecting the Work Clothes automatically puts them on. Without both items, the player cannot enter the Kitchen.

In the Kitchen, the player must wash their hands before collecting ingredients and objects. After collecting everything needed, they can prepare and plate the salad. This also fills the Bio Bag with food waste.

To win, the player must clean the Kitchen, dispose of the full Bio Bag in the Garbage Room, and return the dirty work clothes and towel to the Changing Room. The `Finish` command serves the salad only when every task is complete. Otherwise, the game says that something is still missing.

The game has three rooms: Changing Room, Kitchen, and Garbage Room. The rooms are connected, and the player chooses where to go using numbered options.

The game is suitable for players aged 12 and over.

## How to play

Enter the number beside an action in the main menu. When moving or collecting an item, choose the number shown in the list. The numbers are assigned again each time a list is displayed.

1. **Mission:** Read the objective.
2. **Look:** See the current room, its items, and its exits.
3. **Move:** Go to another room.
4. **Wash:** Wash your hands in the Kitchen.
5. **Collect:** Pick up an item from the current room.
6. **Inventory:** See the items you are carrying and their weights.
7. **Prepare:** Prepare and plate the salad after collecting everything needed.
8. **Clean:** Clean the Kitchen.
9. **Dispose:** Throw away the full Bio Bag in the Garbage Room.
10. **Return:** Return the dirty clothes and towel to the Changing Room.
11. **Finish:** Serve the salad and win if all tasks are complete.
12. **Tip:** Read a sustainability tip about reducing food waste.
13. **Exit:** Save progress and leave the game.
14. **Save:** Save progress and keep playing.

## Sustainable development

The game relates to Sustainable Development Goal 12: Responsible Consumption and Production.

The player uses the available ingredients, puts food waste in a Bio Bag, and cleans up after preparing the meal. The sustainability tip also encourages checking food already available at home before shopping and using ingredients that will expire soon.

## Project structure

- `game.py` creates the rooms and items, reads the introductory files, displays the menus, and runs the game.
- `models.py` contains the `Item`, `Room`, and `Player` classes.
- `storage.py` saves and loads game progress.
- `intro.txt` contains the introductory text shown when the game starts.
- `instructions.txt` contains the game instructions.
- `save_<code>.csv` stores the progress of a saved game.

Run the game with:

```text
python game.py
```

The command must be run from the project folder, where `intro.txt` and `instructions.txt` are located.

## Project 5: starting and saving

When the program starts, it reads the introduction and instructions from `intro.txt` and `instructions.txt`.

Choose **1. New game** and enter a new save code using letters `a-z` and numbers. Then enter the player's name and age.

Choose **2. Continue a saved game** and enter the same code to resume the game.

Choose **14. Save** while playing to save progress and continue playing.

Choose **13. Exit** to save progress before closing the game.

The CSV save file contains the player's name, age, current room, inventory, remaining room items, and mission progress.

The introductory text files must be present in the project folder. A saved game can be continued using a save code previously created by the game.