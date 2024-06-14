# ## Level 3: Write the game
#
# 1. Define the game board as a 2x3 grid and initialize it with random signs.
# 2. Display the grid with hidden signs.
# 3. Handle the user's moves:
#    1. Allow the user to input their move by selecting a cell to uncover.
#    2. Reveal the sign in the selected cell and display the updated grid.
# 4. Track the number of moves and check if the user has uncovered two matching signs.
# 5. Display a win or lose message based on the user's performance.
# 6. User has 3 attempts to uncover the cell.
import random

ATTEMPTS = 3
ALLOWED_NUMBERS = tuple(range(1, 7))
ASK_USER_MESSAGE = "Enter your guess (allowed numbers from 1 to 6 ): "

game_field_visual = [['?' for _ in range(3)] for _ in range(2)]

game_field = [['+', '-', '*'], ['+', '-', '*']]
for row in game_field:
    random.shuffle(row)

chars_stats = {}

attempt = 0
while attempt < ATTEMPTS:
    attempt += 1

    cell_number = int(input(ASK_USER_MESSAGE))
    while cell_number not in ALLOWED_NUMBERS:
        print("Invalid guess. Try again.")
        cell_number = int(input(ASK_USER_MESSAGE))

    row, col = int(cell_number // 3), int(cell_number % 3)

    uncovered_char = game_field[row][col]
    print(f"Uncovered character: {uncovered_char}")

    game_field_visual[row][col] = uncovered_char
    if uncovered_char in chars_stats:
        chars_stats[uncovered_char] += 1
        print(f"You won! You uncovered the same character({uncovered_char}) twice.")
        break
    else:
        chars_stats[uncovered_char] = 1

    print("Game field:")
    for row in game_field_visual:
        print(row)
