from .exceptions import *


# internal helpers
def _position_is_empty_in_board(position, board):
    """
    Checks if given position is empty ("-") in the board.

    :param position: Two-elements tuple representing a
                     position in the board. Example: (0, 1)
    :param board: Game board.

    Returns True if given position is empty, False otherwise.
    """
    row = position[0]
    column = position[1]
    return board[row][column] == "-"
    
    
def _position_is_valid(position):
    """
    Checks if given position is a valid. To consider a position as valid, it
    must be a two-elements tuple, containing values from 0 to 2.
    Examples of valid positions: (0,0), (1,0)
    Examples of invalid positions: (0,0,1), (9,8), False

    :param position: Two-elements tuple representing a
                     position in the board. Example: (0, 1)

    Returns True if given position is valid, False otherwise.
    """
    try: 
        row = position[0]
        column = position[1]
        rowIsInRange = (0 <= row <= 2)
        columnIsInRange = (0 <= column <= 2)
        tupleIsLengthTwo = (len(position) == 2)
        return (rowIsInRange and columnIsInRange and tupleIsLengthTwo)
    except:
        return False
    

def _board_is_full(board):
    """
    Returns True if all positions in given board are occupied.

    :param board: Game board.
    """
    for row in board:
        if "-" in row: return False
    return True


def _is_winning_combination(board, combination, player):
    """
    Checks if all 3 positions in given combination are occupied by given player.

    :param board: Game board.
    :param combination: Tuple containing three position elements.
                        Example: ((0,0), (0,1), (0,2))

    Returns True of all three positions in the combination belongs to given
    player, False otherwise.
    """
    for boardEntry in combination:
        posX, posY = boardEntry
        if board[posX][posY] != player: return False
    return True
    

def _check_winning_combinations(board, player):
    """
    There are 8 posible combinations (3 horizontals, 3, verticals and 2 diagonals)
    to win the Tic-tac-toe game.
    This helper loops through all these combinations and checks if any of them
    belongs to the given player.

    :param board: Game board.
    :param player: One of the two playing players.

    Returns the player (winner) of any of the winning combinations is completed
    by given player, or None otherwise.
    """
    diagonals = [ 
                    ((2, 0), (1, 1), (0, 2)),
                    ((0, 0), (1, 1), (2, 2))
                ]
    columns = [
                    ((0, 0), (1, 0), (2, 0)),
                    ((0, 1), (1, 1), (2, 1)),
                    ((0, 2), (1, 2), (2, 2))
              ]
    rows = [         
                    ((0, 0), (0, 1), (0, 2)),
                    ((1, 0), (1, 1), (1, 2)),
                    ((2, 0), (2, 1), (2, 2))
           ]

    for diagonal in diagonals:
        if _is_winning_combination(board, diagonal, player): return player
    for column in columns:
        if _is_winning_combination(board, column, player): return player
    for row in rows:
        if _is_winning_combination(board, row, player): return player
    return None


def _swapTurn(game, player, playerOne, playerTwo):
    """
    Swaps game["next_turn] to the other player

    :param game: game configuration.
    :param player: the current player from move function
    :param playerOne: player1 from game configuration
    :param playerTwo: player2 from game configuration
    """
    if (playerOne == player):
        game["next_turn"] = playerTwo
    else: game["next_turn"] = playerOne


# public interface
def start_new_game(player1, player2):
    """
    Creates and returns a new game configuration.
    """
    board = [["-", "-", "-"] for x in range(3)]
    
    gameState = { 
                    "player1" : player1,
                    "player2" : player2,
                    "board" : board,
                    "next_turn" : player1,
                    "winner" : None
                }
    return gameState
    

def get_winner(game):
    """
    Returns the winner player if any, or None otherwise.
    """
    return game["winner"]


def move(game, player, position):
    """
    Performs a player movement in the game. Must ensure all the pre requisites
    checks before the actual movement is done.
    After registering the movement it must check if the game is over.
    """
    board = game["board"]
    nextTurn = game["next_turn"]
    playerOne = game["player1"]
    playerTwo = game["player2"]
    weHaveWinner = game["winner"]
    
    if (_board_is_full(board) or weHaveWinner):
        raise InvalidMovement("Game is over.")
    elif not (_position_is_valid(position)):
        raise InvalidMovement("Position out of range.") 
    elif not (_position_is_empty_in_board(position, board)):
        raise InvalidMovement("Position already taken.")
    elif (nextTurn != player):
        raise InvalidMovement("\"{}\" moves next".format(nextTurn))
    else:
        board[position[0]][position[1]] = player
        
        playerWon = _check_winning_combinations(board, player)
        if playerWon:
            game["winner"] = player
            raise GameOver("\"{}\" wins!".format(player))
        if _board_is_full(board): raise GameOver("Game is tied!")
        
        _swapTurn(game, player, playerOne, playerTwo)

def get_board_as_string(game):
    """
    Returns a string representation of the game board in the current state.
    """
    board = game["board"]

    currentBoard = """
{0}  |  {1}  |  {2}
--------------
{3}  |  {4}  |  {5}
--------------
{6}  |  {7}  |  {8}
"""
    currentBoard = currentBoard.format(board[0][0], board[0][1], board[0][2],
                                       board[1][0], board[1][1], board[1][2],
                                       board[2][0], board[2][1], board[2][2])
    return currentBoard


def get_next_turn(game):
    """
    Returns the player who plays next, or None if the game is already over.
    """
    return None if game['winner'] else game['next_turn']
