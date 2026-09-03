name = input("Enter your name: ")
age = int(input("Enter your age: "))

guesses = []


def new_game(guesses):
    length = input("Choose the word length (5-8): ")
    guess = input("Enter a " + length + "-letter word: ").strip().lower()

    guesses.append(guess)

    print("Guess added!\n")


def game_rules():
    print(
        "GAME RULES\n"
        "Choose the length of the word.\n"
        "Enter a word with the selected number of letters.\n"
        "Try to find the correct word in as few attempts as possible.\n"
    )


def show_stats(guesses):
    print("STATS\n")

    if len(guesses) == 0:
        print("No guesses yet.\n")
        return

    print("Previous guesses:")

    for guess in guesses:
        print(guess)

    print("Total guesses:", len(guesses))
    print()


def quit_game():
    print("Exit the game..\n")


if age < 12:
    print("User is underage")
else:
    print("Welcome", name)
    print("Let's play Wordle!")

    while True:
        choice = input(
            "MAIN MENU\n"
            "play     - Start a new Wordle game\n"
            "rules    - Display the game rules\n"
            "stats    - Display your statistics\n"
            "lopeta   - Exit the program\n"
        ).strip().lower()

        if choice == "play":
            print("New Game:\n")
            new_game(guesses)

        elif choice == "rules":
            game_rules()

        elif choice == "stats":
            show_stats(guesses)

        elif choice == "lopeta":
            quit_game()
            break

        else:
            print("Invalid choice!\n")
            continue