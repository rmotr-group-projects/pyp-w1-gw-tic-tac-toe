try:
    from exceptions import *
except:
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
    if board[position[0]][position[1]] == "-":
        return True
    return False

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
    if type(position) == tuple and len(position) == 2 and _areNumbersInValidRange(position):
        return True
    return False

def _areNumbersInValidRange(position):
    #Check if elements of a tuple are numbers between 0 and 2
    for n in position:
        if n < 0 or n > 2 or type(n) != int:
            return False
    return True


def _board_is_full(board):
    """
    Returns True if all positions in given board are occupied.

    :param board: Game board.
    """
    for row in board:
        if "-" in row:
            return False
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
    for n in combination:
        if board[n[0]][n[1]] != player:
            return False
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
    for x in range(3):
        if _is_winning_combination(board, ((x, 0), (x, 1), (x, 2)), player): return player
        if _is_winning_combination(board, ((0, x), (1, x), (2, x)), player): return player
        
    if _is_winning_combination(board, ((0, 0), (1, 1), (2, 2)), player): return player
    if _is_winning_combination(board, ((0, 2), (1, 1), (2, 0)), player): return player
    
    return None
        


# public interface
def start_new_game(player1, player2):
    """
    Creates and returns a new game configuration.
    """
    return {
        "player1": player1,
        "player2": player2,
        "board": [
            ["-","-","-"],
            ["-","-","-"],
            ["-","-","-"]
            ],
            "next_turn": player1,
            "winner": None
        }


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
    
    #If the board is full, or we have a winner already
    if _board_is_full(game["board"]) or game["winner"]:
        raise InvalidMovement("Game is over.")
        
    #If it's not this player's turn
    if get_next_turn(game) != player:
        raise InvalidMovement('"{}" moves next.'.format(get_next_turn(game)))
    
    #If the position doesn't exist   
    if not _position_is_valid(position):
        raise InvalidMovement("Position out of range.")
    
    if not _position_is_empty_in_board(position, game["board"]):
        raise InvalidMovement("Position already taken.")
    
    #Otherwise update the board    
    game["board"][position[0]][position[1]] = player #Update the board with the new move
    if player == game["player1"]:
        game["next_turn"] = game["player2"]
    else:
        game["next_turn"] = game["player1"]
            
    
    #If player wins, update the winner and raise GameOver
    if _check_winning_combinations(game["board"], player):
       # game["next_turn"] = None
        game["winner"] = player
        raise GameOver('"' + player + '" wins!')
        
    #If the board is full after the move, it's a tie
    if _board_is_full(game["board"]):
        # game["next_turn"] = None
        game["winner"] = None
        raise GameOver("Game is tied!")



def get_board_as_string(game):
    """
    Returns a string representation of the game board in the current state.
    """
    return "\n"+("\n--------------\n".join([
        "  |  ".join([cell for cell in row ])
        for row in game["board"]
    ]))+"\n"


def get_next_turn(game):
    """
    Returns the player who plays next, or None if the game is already over.
    """
    return game["next_turn"] if not game["winner"] else None

