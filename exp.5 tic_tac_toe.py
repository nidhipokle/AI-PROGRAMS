board = ["1", "2", "3",
         "4", "5", "6",
         "7", "8", "9"]

player = "X"

for turn in range(9):

    # Display the board
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()

    # Take input from player
    position = int(input("Player " + player + ", enter position: "))

    # Convert position to index
    position = position - 1

    # Put X or O on the board
    board[position] = player

    # Check winning conditions
    if (board[0] == board[1] == board[2] or
        board[3] == board[4] == board[5] or
        board[6] == board[7] == board[8] or
        board[0] == board[3] == board[6] or
        board[1] == board[4] == board[7] or
        board[2] == board[5] == board[8] or
        board[0] == board[4] == board[8] or
        board[2] == board[4] == board[6]):

        # Display final board
        print()
        print(board[0], "|", board[1], "|", board[2])
        print("--+---+--")
        print(board[3], "|", board[4], "|", board[5])
        print("--+---+--")
        print(board[6], "|", board[7], "|", board[8])
        print()

        print("Player", player, "wins!")
        break

    # Change player
    if player == "X":
        player = "O"
    else:
        player = "X"

else:
    print("Game Draw!")