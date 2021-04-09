from puzzles.battleship import BattleShip

print("Let's play Battleship!")

battlehip = BattleShip([])

print(battlehip.print_board())

ship_row = battlehip.random_row()
ship_col = battlehip.random_col()

# Everything from here on should go in your for loop!
# Be sure to indent four spaces!
for turn in range(4):

    guess_row = int(input("Guess Row:"))
    guess_col = int(input("Guess Col:"))

    if guess_row == ship_row and guess_col == ship_col:
        print("Congratulations! You sunk my battleship!")
        break
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print("Oops, that's not even in the ocean.")
        elif battlehip.board[guess_row][guess_col] == "X":
            print("You guessed that one already.")
        else:
            print("You missed my battleship!")
            battlehip.board[guess_row][guess_col] = "X"
            if turn == 3:
                print("Game Over")
    # Print (turn + 1) here!
    print("Turn", turn + 1)
    print(battlehip.print_board())
