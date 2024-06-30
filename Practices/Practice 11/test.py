import random
from colorama import Fore, Back, Style

game_field = [["_" for i in range(2)] for j in range(3)]
visible_game_field = [["_" for i in range(2)] for j in range(3)]

elements = ("+", "-", "*")
possible_positions = [[i, j] for i in range(3) for j in range(2)]

while "_" in [item for sublist in game_field for item in sublist]:
    positions = random.sample(possible_positions, 1)
    for i, j in positions:
        if game_field[i][j] == "_":
            game_field[i][j] = random.choice(elements)
print(game_field)

lives = 3
last_guessed_element = None
while lives > 0:
    move = list(map(lambda x: int(x), input("Введи координати через пробіл: ").split(" ")))
    if visible_game_field[move[0]][move[1]] != "_":
        print("Клітинка вже була була названа")
        print(visible_game_field)
        lives -= 1

    entered_element = input("Enter the element (+, -, *): ")
    while entered_element not in elements:
        entered_element = input("Enter the CORRECT element (+, -, *): ")

    if game_field[move[0]][move[1]] == last_guessed_element:
        print(Back.YELLOW + "Ти вгадав двічі поспіль! Ти справжній переможець!" + Style.RESET_ALL)
        visible_game_field[move[0]][move[1]] = entered_element
        break

    if visible_game_field[move[0]][move[1]] == "_" and game_field[move[0]][move[1]] == entered_element:
        print(Back.GREEN + "Ти вгадав!" + Style.RESET_ALL)
        visible_game_field[move[0]][move[1]] = entered_element
        print(visible_game_field)
        last_guessed_element = entered_element
        lives -= 1
    else:
        print(Back.RED + "На жаль, ти не вгадав" + Style.RESET_ALL)
        lives -= 1
else:
    print(Fore.RED + "У тебе більше не залишилось спроб" + Style.RESET_ALL)
