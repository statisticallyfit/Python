""" A program to play a game of tic-tac-toe between a human and a computer.
"""
import random




# TODO - implement with object oriented approach
# TODO - implement a gui board (with nice and sticky-type xs and os).


def getInitialBoard():
    """Gets an empty board to play tic-tac-toe. """
    board = []
    for i in range(9):
        board.append(" ")
    return board

def displayBoard(board):
    """Prints out the board passed as an argument to standard output."""
    print("| " + board[0] + " | " + board[1] + " | " + board[2] + " |")
    print("-------------")
    print("| " + board[3] + " | " + board[4] + " | " + board[5] + " |")
    print("-------------")
    print("| " + board[6] + " | " + board[7] + " | " + board[8] + " |")



def getPlayerMove(board):
    """Gets the position a player wishes to play their next move.
       Guarantees the position is between 0 and 8 inclusive.
       Guarantees the computer mvoe does not replace a previously filled move.
       Arguments:
           board - the board to make the move in.
    """
    movePosition = -1

    while movePosition < 0 or movePosition > 8:
        print("--------------------------------------------------------------")
        move = input("Enter position: ")
        try:
            movePosition = int(move) # to check for empty string
            if movePosition < 0 or movePosition > 8:
                raise ValueError()
            if board[movePosition] != " ":
                print("Please select an empty space!")
                movePosition = -1
        except ValueError:
            print("Invalid position. Position must be between 0 and 8 inclusive.")
    return movePosition




def getComputerMove(board, computerPreference):
    """Gets the move a computer wishes to make.
       Guarantees the position is between 0 and 8 inclusive.
       Guarantees the computer mvoe does not replace a previously filled move.
       Arguments:
           board - the board to make the move in.
           computerPreference - the symbol of the computer.
    """
    # PLAY 1: if computer can win, win it
    boardCopy = board[:]
    for i in range(len(boardCopy)):
        if boardCopy[i] == " ":
            boardCopy[i] = computerPreference
            if isWinner(boardCopy, computerPreference):
                return i # winning move
            boardCopy[i] = " " # erase it, continue looping

    playerPreference = getOppositePreference(computerPreference)

    # PLAY 2: if cannot win but can stop player, stop him.
    for i in range(len(boardCopy)):
        if boardCopy[i] == " ":
            boardCopy[i] = playerPreference
            if isWinner(boardCopy, playerPreference):
                return i # the computer should stop opposing player.
            boardCopy[i] = " " #erase!


    # TODO: Computer play could be improved to make it perfect - no player can win against it.
    # TODO: i.e. find optimal strategy.



    # PLAY 3: if not finding any winning move and no stopping player, then use random move.
    # note: possible to get the same wrong number an arbitrary number of times.
    # note: Millions of zeroes are possible equally. Not better than bogosort.
    # note: Average runtime increases as board gets fuller.

    # just choosing a random position
    computerMove = random.randint(0, 8)
    while board[computerMove] != " ":
        computerMove = random.randint(0, 8)
    return computerMove



def isBoardFull(board):
    """Checks if this board does not have any more valid moves."""

    # checking no empty spaces left.
    for i in range(len(board)):
        if board[i] == " ":
            return False
    return True


def isGameOver(board):
    """Determines if game has finished on given board."""
    return isBoardFull(board) or getWinner(board) != None


def isWinner(board, playerSymbol):
    """Checks if the given player has won on this board."""

    # horizontals
    if board[0] == playerSymbol and board[1] == playerSymbol and board[2] == playerSymbol:
        return True
    if board[3] == playerSymbol and board[4] == playerSymbol and board[5] == playerSymbol:
        return True
    if board[6] == playerSymbol and board[7] == playerSymbol and board[8] == playerSymbol:
        return True

    # verticals
    if board[0] == playerSymbol and board[3] == playerSymbol and board[6] == playerSymbol:
        return True
    if board[1] == playerSymbol and board[4] == playerSymbol and board[7] == playerSymbol:
        return True
    if board[2] == playerSymbol and board[5] == playerSymbol and board[8] == playerSymbol:
        return True

    # diagonals
    if board[0] == playerSymbol and board[4] == playerSymbol and board[8] == playerSymbol:
        return True
    if board[2] == playerSymbol and board[4] == playerSymbol and board[6] == playerSymbol:
        return True

    return False


def getWinner(board):
    """Gets the winner for the given board, returning None if there is no winner."""
    if isWinner(board, "O"):
        return "O"
    if isWinner(board, "X"):
        return "X"
    return None



def playGame(board, playerPreference):
    """Plays a game of tic-tac-toe on the given board.

    Arguments:
        board - the board being played on.
        playerPreference - the player symbol, O or X.
    """
    computerPreference = getOppositePreference(preference)
    displayBoard(board)

    # random decision who should go first
    playerHasNextMove = random.random() > 0.5 # (uniform distribution)

    while not isGameOver(board):
        if playerHasNextMove:
            move = getPlayerMove(board)
            board[move] = playerPreference
        else:
            move = getComputerMove(board, computerPreference)
            board[move] = computerPreference

        print("Current game state: ")
        displayBoard(board)

        playerHasNextMove = not playerHasNextMove # inversing it.

    winner = getWinner(board)
    if winner == None:
        print("The game was a draw!")
    else:
        print("Player {0} wins!".format(winner))



def getOppositePreference(preference):
    """Get the opposite mark of the one given."""
    if preference == "X":
        return "O"
    if preference == "O":
        return "X"
    raise ValueError("Preference mus tbe O or X.")


def getPlayerPreference():
    """Determine whether player wants to be O or X, returning their choice."""
    preference = ""
    while preference != "O" and preference != "X":
        preference = input("Do you want to be O or X? = ")
    return preference



if __name__ == "__main__":
    board = getInitialBoard()
    preference = getPlayerPreference()
    playGame(board, preference)