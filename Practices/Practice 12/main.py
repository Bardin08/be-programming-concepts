"""
Implement a simple number guessing game,
    where the computer randomly selects a number between 1 and 100,
1. Store game results to the CSV file
2. Design a game menu with the following options:
    - Play game
    - Show results
    - Exit
"""
import os
import random

MENU_OPTIONS = [
    "1. Play game",
    "2. Show results",
    "3. Exit"
]


def get_menu_action():
    """
    Get an action from the user based on the menu options.
    """

    print("\n".join(MENU_OPTIONS))
    selected_option = input("Select an option: ")
    while selected_option not in ["1", "2", "3"]:
        print("Invalid option. Try again.")
        selected_option = input("Select an option: ")

    return int(selected_option) - 1


def play_game():
    """
    Play the number guessing game.
    """

    ATTEMPTS = 3

    print("Playing the number guessing game.")
    number_to_guess = random.randint(1, 101)
    guessed_number = -1
    game_result = "lose"

    attempt = 0
    while attempt < ATTEMPTS:
        attempt += 1

        guessed_number = int(input("Enter a number between 1 and 100: "))

        if guessed_number == number_to_guess:
            print("Congratulations! You guessed the correct number.")
            game_result = "win"
            break
        elif guessed_number < number_to_guess:
            print("The number is higher.")
        else:
            print("The number is lower.")

    with open("game_results.csv", "a") as file:
        file.write(f"{guessed_number},{number_to_guess},{game_result}\n")


def show_results():
    """
    Show the game results.
    """

    print("Showing the game results.")

    file_exists = os.path.isfile('game_results.csv')
    if not file_exists:
        print("No game results found.")
        return

    with open("game_results.csv", "r") as file:
        for idx, line in enumerate(file.readlines()):
            if idx < 3:
                print(line.strip())

    if idx == 0:
        print("No game results found.")


def exit_game():
    """
    Exit the game.
    """

    print("Exiting the game.")
    exit(0)


MENU_OPTIONS_HANDLER = {
    0: play_game,
    1: show_results,
    2: exit_game
}


selected_action = get_menu_action()
MENU_OPTIONS_HANDLER[selected_action]()
