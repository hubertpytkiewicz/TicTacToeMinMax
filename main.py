from game import Game
import sys
import time

if len(sys.argv) != 2:
    option = "rva"
else:
    option = sys.argv[1]

if option not in {"rva", "hva", "hvr", "aitest"}:
    option = "rva"

test_quantitiy = 1

if option == "aitest":
    test_quantitiy = int(input("How many tests to run? "))
    option = "rva"

random_wins = 0
ai_wins = 0
ties = 0

start = time.time()
for i in range(0, test_quantitiy):
    new_game = Game(option)
    winner = new_game.game_loop()
    if winner == "X":
        random_wins += 1
    elif winner == "O":
        ai_wins += 1
    else:
        ties += 1

end = time.time()

if test_quantitiy > 1:
    print(f"Random player won {random_wins} times.")
    print(f"AI player won {ai_wins} times.")
    print(f"There were {ties} ties.")

print(f"It took {end-start} seconds.")