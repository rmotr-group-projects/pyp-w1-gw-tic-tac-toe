from exceptions import *

# internal helpers
def _position_is_empty_in_board(position, board):
    """
    Checks if given position is empty ("-") in the board.

    :param position: Two-elements tuple representing a
                     position in the board. Example: (0, 1)
    :param board: Game board.

    Returns True if given position is empty, False otherwise.
    """
    if board[position(0)][position(1)] == "-":
        return True
    else:
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
    pass

    # Ensure length = 2 and each entry is between 0 and 2
    if len(position) != 2:
        return False
        
    elif position(0) < 0 or position(0) > 2 or position(1) < 0 or position(1) > 2:
        return False
        
    else:
        return True
    


def _board_is_full(board):
    """
    Returns True if all positions in given board are occupied.

    :param board: Game board.
    """
    board_full = all([True if (c != '-') else False for r in board for c in r])
    if board_full:
        return True
    else:
        return False




def _is_winning_combination(board, combination, player):
    """
    Checks if all 3 positions in given combination are occupied by given player.

    :param board: Game board.
    :param combination: Tuple containing three position elements.
                        Example: ((0,0), (0,1), (0,2))

    Returns True of all three positions in the combination belongs to given
    player, False otherwise.
    """
    pass


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
    pass

    # winning_combinations = (
    #         #Three horizontals (first index all equal)
    #         ((0, 0), (0, 1), (0, 2)),
    #         ((1, 0), (1, 1), (1, 2)),
    #         ((2, 0), (2, 1), (2, 2)),
    #         #Three verticals (second index all equal)
    #         ((0, 0), (1, 0), (2, 0)),
    #         ((0, 1), (1, 1), (2, 1)),
    #         ((0, 2), (1, 2), (2, 2)),
    #         #Two diagonals
    #         ((0, 0), (1, 1), (2, 2)),
    #         ((0, 2), (1, 1), (2, 0))
    #     )


# public interface
def start_new_game(player1, player2):
    """
    Creates and returns a new game configuration.
    """
    game = {
        'player1': player1,
        'player2': player2,
        'board': [
            ["-", "-", "-"],
            ["-", "-", "-"],
            ["-", "-", "-"],
        ],
        'next_turn': player1,
        'winner': None
    }
    return game

def get_winner(game):
    """
    Returns the winner player if any, or None otherwise.
    """
    return game['winner']

def move(game, player, position):
    """
    Performs a player movement in the game. Must ensure all the pre requisites
    checks before the actual movement is done.
    After registering the movement it must check if the game is over.
    """
    # Do validity checks first
    # Check if postition is valid
    if not _position_is_valid(position):
        raise InvalidMovement("Position out of range")
        
    # Check if position is taken
    if not  _position_is_empty_in_board(position, game['Game']):
        raise InvalidMovement("Position already taken.")
    
    # If there is a winner or tie(board=full), raise error
    if get_winner(game) or _board_is_full(game['board']):
        raise InvalidMovement('The game is over.')
        
    # Check if correct player made move
    if game['next_turn'] != player:
        raise InvalidMovement("{} moves next".format(game['next_turn'])

def get_board_as_string(game):
    """
    Returns a string representation of the game board in the current state.
    """
    pass


def get_next_turn(game):
    """
    Returns the player who plays next, or None if the game is already over.
    """
    pass
